import collections

import grpc
import wrapt

from ddtrace import config
from ddtrace.constants import _SPAN_MEASURED_KEY
from ddtrace.constants import ERROR_MSG
from ddtrace.constants import ERROR_STACK
from ddtrace.constants import ERROR_TYPE
from ddtrace.constants import SPAN_KIND
from ddtrace.contrib import trace_utils
from ddtrace.contrib.internal.grpc import constants
from ddtrace.contrib.internal.grpc import utils
from ddtrace.ext import SpanKind
from ddtrace.ext import SpanTypes
from ddtrace.internal import core
from ddtrace.internal.compat import to_unicode
from ddtrace.internal.constants import COMPONENT
from ddtrace.internal.logger import get_logger
from ddtrace.internal.schema import schematize_url_operation
from ddtrace.internal.schema.span_attribute_schema import SpanDirection
from ddtrace.propagation.http import HTTPPropagator


log = get_logger(__name__)

# DEV: Follows Python interceptors RFC laid out in
# https://github.com/grpc/proposal/blob/master/L13-python-interceptors.md

# DEV: __version__ added in v1.21.4
# https://github.com/grpc/grpc/commit/dd4830eae80143f5b0a9a3a1a024af4cf60e7d02


def create_client_interceptor(pin, host, port):
    return _ClientInterceptor(pin, host, port)


def intercept_channel(wrapped, instance, args, kwargs):
    channel = args[0]
    interceptors = args[1:]
    if isinstance(getattr(channel, "_interceptor", None), _ClientInterceptor):
        dd_interceptor = channel._interceptor
        base_channel = getattr(channel, "_channel", None)
        if base_channel:
            new_channel = wrapped(channel._channel, *interceptors)
            return grpc.intercept_channel(new_channel, dd_interceptor)

    return wrapped(*args, **kwargs)


class _ClientCallDetails(
    collections.namedtuple("_ClientCallDetails", ("method", "timeout", "metadata", "credentials")),
    grpc.ClientCallDetails,
):
    pass


def _future_done_callback(span):
    def func(response):
        try:
            # pull out response code from gRPC response to use both for `grpc.status.code`
            # tag and the error type tag if the response is an exception
            response_code = response.code()
            # cast code to unicode for tags
            status_code = to_unicode(response_code)
            span.set_tag_str(constants.GRPC_STATUS_CODE_KEY, status_code)

            if response_code != grpc.StatusCode.OK:
                _handle_error(span, response, status_code)
        finally:
            span.finish()

    return func


def _handle_response(span, response):
    # use duck-typing to support future-like response as in the case of
    # google-api-core which has its own future base class
    # https://github.com/googleapis/python-api-core/blob/49c6755a21215bbb457b60db91bab098185b77da/google/api_core/future/base.py#L23
    if hasattr(response, "_response"):
        if response._response is not None:
            core.dispatch("grpc.client.response.message", (response._response,))

    if hasattr(response, "add_done_callback"):
        response.add_done_callback(_future_done_callback(span))


def _handle_error(span, response_error, status_code):
    # response_error should be a grpc.Future and so we expect to have cancelled(),
    # exception() and traceback() methods if a computation has resulted in an
    # exception being raised
    if (
        not callable(getattr(response_error, "cancelled", None))
        and not callable(getattr(response_error, "exception", None))
        and not callable(getattr(response_error, "traceback", None))
    ):
        return

    if response_error.cancelled():
        # handle cancelled futures separately to avoid raising grpc.FutureCancelledError
        span.error = 1
        exc_val = to_unicode(response_error.details())
        span.set_tag_str(ERROR_MSG, exc_val)
        span.set_tag_str(ERROR_TYPE, status_code)
        return

    exception = response_error.exception()
    traceback = response_error.traceback()

    if exception is not None and traceback is not None:
        span.error = 1
        if isinstance(exception, grpc.RpcError):
            # handle internal gRPC exceptions separately to get status code and
            # details as tags properly
            exc_val = to_unicode(response_error.details())
            span.set_tag_str(ERROR_MSG, exc_val)
            span.set_tag_str(ERROR_TYPE, status_code)
            span.set_tag_str(ERROR_STACK, str(traceback))
        else:
            exc_type = type(exception)
            span.set_exc_info(exc_type, exception, traceback)
            status_code = to_unicode(response_error.code())


class _WrappedResponseCallFuture(wrapt.ObjectProxy):
    def __init__(self, wrapped, span):
        super(_WrappedResponseCallFuture, self).__init__(wrapped)
        self._span = span
        # Registers callback on the _MultiThreadedRendezvous future to finish
        # span in case StopIteration is never raised but RPC is terminated
        _handle_response(self._span, self.__wrapped__)

    def __iter__(self):
        return self

    def _next(self):
        # While an iterator ObjectProxy requires only __iter__ and __next__, we
        # make sure to also proxy the grpc._channel._Rendezvous._next method in
        # case it is being called directly as in google.api_core.grpc_helpers
        # and grpc_gcp._channel.
        # https://github.com/grpc/grpc/blob/5195a06ddea8da6603c6672e0ed09fec9b5c16ac/src/python/grpcio/grpc/_channel.py#L418-L419
        # https://github.com/googleapis/python-api-core/blob/35e87e0aca52167029784379ca84e979098e1d6c/google/api_core/grpc_helpers.py#L84
        # https://github.com/GoogleCloudPlatform/grpc-gcp-python/blob/5a2cd9807bbaf1b85402a2a364775e5b65853df6/src/grpc_gcp/_channel.py#L102
        try:
            return next(self.__wrapped__)
        except StopIteration:
            # Callback will handle span finishing
            raise
        except grpc.RpcError as rpc_error:
            # DEV: grpcio<1.18.0 grpc.RpcError is raised rather than returned as response
            # https://github.com/grpc/grpc/commit/8199aff7a66460fbc4e9a82ade2e95ef076fd8f9
            # handle as a response
            _handle_response(self._span, rpc_error)
            raise
        except Exception:
            # DEV: added for safety though should not be reached since wrapped response
            log.debug("unexpected non-grpc exception raised, closing open span", exc_info=True)
            self._span.set_traceback()
            self._span.finish()
            raise

    def __next__(self):
        n = self._next()
        if n is not None:
            core.dispatch("grpc.client.response.message", (n,))
        return n

    next = __next__


class _ClientInterceptor(
    grpc.UnaryUnaryClientInterceptor,
    grpc.UnaryStreamClientInterceptor,
    grpc.StreamUnaryClientInterceptor,
    grpc.StreamStreamClientInterceptor,
):
    def __init__(self, pin, host, port):
        self._pin = pin
        self._host = host
        self._port = port

    def _intercept_client_call(self, method_kind, client_call_details):
        tracer = self._pin.tracer

        span = tracer.trace(
            schematize_url_operation("grpc", protocol="grpc", direction=SpanDirection.OUTBOUND),
            span_type=SpanTypes.GRPC,
            service=trace_utils.ext_service(self._pin, config.grpc),
            resource=client_call_details.method,
        )

        span.set_tag_str(COMPONENT, config.grpc.integration_name)

        # set span.kind to the type of operation being performed
        span.set_tag_str(SPAN_KIND, SpanKind.CLIENT)

        span.set_tag(_SPAN_MEASURED_KEY)

        utils.set_grpc_method_meta(span, client_call_details.method, method_kind)
        utils.set_grpc_client_meta(span, self._host, self._port)
        span.set_tag_str(constants.GRPC_SPAN_KIND_KEY, constants.GRPC_SPAN_KIND_VALUE_CLIENT)

        # inject tags from pin
        if self._pin.tags:
            span.set_tags(self._pin.tags)

        # propagate distributed tracing headers if available
        headers = {}
        if config.grpc.distributed_tracing_enabled:
            HTTPPropagator.inject(span.context, headers)

        metadata = []
        if client_call_details.metadata is not None:
            metadata = list(client_call_details.metadata)
        metadata.extend(headers.items())

        client_call_details = _ClientCallDetails(
            client_call_details.method,
            client_call_details.timeout,
            metadata,
            client_call_details.credentials,
        )

        return span, client_call_details

    def intercept_unary_unary(self, continuation, client_call_details, request):
        span, client_call_details = self._intercept_client_call(
            constants.GRPC_METHOD_KIND_UNARY,
            client_call_details,
        )
        try:
            response = continuation(client_call_details, request)
            _handle_response(span, response)
        except grpc.RpcError as rpc_error:
            # DEV: grpcio<1.18.0 grpc.RpcError is raised rather than returned as response
            # https://github.com/grpc/grpc/commit/8199aff7a66460fbc4e9a82ade2e95ef076fd8f9
            # handle as a response
            _handle_response(span, rpc_error)
            raise

        return response

    def intercept_unary_stream(self, continuation, client_call_details, request):
        span, client_call_details = self._intercept_client_call(
            constants.GRPC_METHOD_KIND_SERVER_STREAMING,
            client_call_details,
        )
        response_iterator = continuation(client_call_details, request)
        response_iterator = _WrappedResponseCallFuture(response_iterator, span)
        return response_iterator

    def intercept_stream_unary(self, continuation, client_call_details, request_iterator):
        span, client_call_details = self._intercept_client_call(
            constants.GRPC_METHOD_KIND_CLIENT_STREAMING,
            client_call_details,
        )
        try:
            response = continuation(client_call_details, request_iterator)
            _handle_response(span, response)
        except grpc.RpcError as rpc_error:
            # DEV: grpcio<1.18.0 grpc.RpcError is raised rather than returned as response
            # https://github.com/grpc/grpc/commit/8199aff7a66460fbc4e9a82ade2e95ef076fd8f9
            # handle as a response
            _handle_response(span, rpc_error)
            raise

        return response

    def intercept_stream_stream(self, continuation, client_call_details, request_iterator):
        span, client_call_details = self._intercept_client_call(
            constants.GRPC_METHOD_KIND_BIDI_STREAMING,
            client_call_details,
        )
        response_iterator = continuation(client_call_details, request_iterator)
        response_iterator = _WrappedResponseCallFuture(response_iterator, span)
        return response_iterator
