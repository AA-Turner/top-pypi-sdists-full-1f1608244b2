import asyncio
import functools
from typing import Callable  # noqa:F401
from typing import Tuple  # noqa:F401
from typing import Union  # noqa:F401

import grpc
from grpc import aio
from grpc.aio._typing import RequestIterableType
from grpc.aio._typing import RequestType
from grpc.aio._typing import ResponseIterableType
from grpc.aio._typing import ResponseType

from ddtrace import config
from ddtrace.constants import _SPAN_MEASURED_KEY
from ddtrace.constants import ERROR_MSG
from ddtrace.constants import ERROR_TYPE
from ddtrace.constants import SPAN_KIND
from ddtrace.contrib import trace_utils
from ddtrace.contrib.internal.grpc import constants
from ddtrace.contrib.internal.grpc import utils
from ddtrace.ext import SpanKind
from ddtrace.ext import SpanTypes
from ddtrace.internal.compat import to_unicode
from ddtrace.internal.constants import COMPONENT
from ddtrace.internal.logger import get_logger
from ddtrace.internal.schema import schematize_url_operation
from ddtrace.internal.schema.span_attribute_schema import SpanDirection
from ddtrace.propagation.http import HTTPPropagator
from ddtrace.trace import Pin
from ddtrace.trace import Span


log = get_logger(__name__)


def create_aio_client_interceptors(pin, host, port):
    # type: (Pin, str, int) -> Tuple[aio.ClientInterceptor, ...]
    return (
        _UnaryUnaryClientInterceptor(pin, host, port),
        _UnaryStreamClientInterceptor(pin, host, port),
        _StreamUnaryClientInterceptor(pin, host, port),
        _StreamStreamClientInterceptor(pin, host, port),
    )


def _handle_add_callback(call, callback):
    try:
        call.add_done_callback(callback)
    except NotImplementedError:
        # add_done_callback is not implemented in UnaryUnaryCallResponse
        # https://github.com/grpc/grpc/blob/c54c69dcdd483eba78ed8dbc98c60a8c2d069758/src/python/grpcio/grpc/aio/_interceptor.py#L1058
        # If callback is not called, we need to finish the span here
        callback(call)


def _done_callback_unary(span, code, details):
    # type: (Span, grpc.StatusCode, str) -> Callable[[aio.Call], None]
    def func(call):
        # type: (aio.Call) -> None
        try:
            span.set_tag_str(constants.GRPC_STATUS_CODE_KEY, to_unicode(code))

            # Handle server-side error in unary response RPCs
            if code != grpc.StatusCode.OK:
                _handle_error(span, code, details)
        finally:
            span.finish()

    return func


def _done_callback_stream(span):
    # type: (Span) -> Callable[[aio.Call], None]
    def func(call):
        # type: (aio.Call) -> None
        try:
            if call.done():
                # check to ensure code and details are not already set, in which case this span
                # is an error span and already has all error tags from `_handle_cancelled_error`
                code_tag = span.get_tag(constants.GRPC_STATUS_CODE_KEY)
                details_tag = span.get_tag(ERROR_MSG)
                if not code_tag or not details_tag:
                    # we need to call __repr__ as we cannot call code() or details() since they are both async
                    code, details = utils._parse_rpc_repr_string(call.__repr__(), grpc)

                    span.set_tag_str(constants.GRPC_STATUS_CODE_KEY, to_unicode(code))

                    # Handle server-side error in unary response RPCs
                    if code != grpc.StatusCode.OK:
                        _handle_error(span, code, details)
            else:
                log.warning("Grpc call has not completed, unable to set status code and details on span.")
        except ValueError:
            # ValueError is thrown from _parse_rpc_repr_string
            log.warning("Unable to parse async grpc string for status code and details.")
        finally:
            span.finish()

    return func


def _handle_error(span, code, details):
    # type: (Span, grpc.StatusCode, str) -> None
    span.error = 1
    span.set_tag_str(ERROR_MSG, details)
    span.set_tag_str(ERROR_TYPE, to_unicode(code))


def _handle_rpc_error(span, rpc_error):
    # type: (Span, aio.AioRpcError) -> None
    code = to_unicode(rpc_error.code())
    span.error = 1
    span.set_tag_str(constants.GRPC_STATUS_CODE_KEY, code)
    span.set_tag_str(ERROR_MSG, rpc_error.details())
    span.set_tag_str(ERROR_TYPE, code)
    span.finish()


async def _handle_cancelled_error(call, span):
    # type: (aio.Call, Span) -> None
    code = to_unicode(await call.code())
    span.error = 1
    span.set_tag_str(constants.GRPC_STATUS_CODE_KEY, code)
    span.set_tag_str(ERROR_MSG, await call.details())
    span.set_tag_str(ERROR_TYPE, code)
    span.finish()


class _ClientInterceptor:
    def __init__(self, pin: Pin, host: str, port: int) -> None:
        self._pin = pin
        self._host = host
        self._port = port

    def _intercept_client_call(self, method_kind, client_call_details):
        # type: (str, aio.ClientCallDetails) -> Tuple[Span, aio.ClientCallDetails]
        tracer = self._pin.tracer

        method_as_str = client_call_details.method.decode()
        span = tracer.trace(
            schematize_url_operation("grpc", protocol="grpc", direction=SpanDirection.OUTBOUND),
            span_type=SpanTypes.GRPC,
            service=trace_utils.ext_service(self._pin, config.grpc_aio_client),
            resource=method_as_str,
        )

        span.set_tag_str(COMPONENT, config.grpc_aio_client.integration_name)

        # set span.kind to the type of operation being performed
        span.set_tag_str(SPAN_KIND, SpanKind.CLIENT)

        span.set_tag(_SPAN_MEASURED_KEY)

        utils.set_grpc_method_meta(span, method_as_str, method_kind)
        utils.set_grpc_client_meta(span, self._host, self._port)
        span.set_tag_str(constants.GRPC_SPAN_KIND_KEY, constants.GRPC_SPAN_KIND_VALUE_CLIENT)

        # inject tags from pin
        if self._pin.tags:
            span.set_tags(self._pin.tags)

        # propagate distributed tracing headers if available
        headers = {}
        if config.grpc_aio_client.distributed_tracing_enabled:
            HTTPPropagator.inject(span.context, headers)

        metadata = []
        if client_call_details.metadata is not None:
            metadata = list(client_call_details.metadata)
        metadata.extend(headers.items())

        client_call_details = aio.ClientCallDetails(
            client_call_details.method,
            client_call_details.timeout,
            metadata,
            client_call_details.credentials,
            client_call_details.wait_for_ready,
        )

        return span, client_call_details

    # NOTE: Since this function is executed as an async generator when the RPC is called,
    # `continuation` must be called before the RPC.
    async def _wrap_stream_response(
        self,
        call: Union[aio.StreamStreamCall, aio.UnaryStreamCall],
        span: Span,
    ) -> ResponseIterableType:
        try:
            _handle_add_callback(call, _done_callback_stream(span))
            async for response in call:
                yield response
        except StopAsyncIteration:
            # Callback will handle span finishing
            _handle_cancelled_error()
            raise
        except aio.AioRpcError as rpc_error:
            # NOTE: We can also handle the error in done callbacks,
            # but reuse this error handling function used in unary response RPCs.
            _handle_rpc_error(span, rpc_error)
            raise
        except asyncio.CancelledError:
            # NOTE: We can't handle the cancelled error in done callbacks
            # because they cannot handle awaitable functions.
            await _handle_cancelled_error(call, span)
            raise

    # NOTE: `continuation` must be called inside of this function to catch exceptions.
    async def _wrap_unary_response(
        self,
        continuation: Callable[[], Union[aio.StreamUnaryCall, aio.UnaryUnaryCall]],
        span: Span,
    ):
        # type: (...) -> Union[aio.StreamUnaryCall, aio.UnaryUnaryCall]
        try:
            call = await continuation()
            code = await call.code()
            details = await call.details()
            # NOTE: As both `code` and `details` are available after the RPC is done (= we get `call` object),
            # and we can't call awaitable functions inside the non-async callback,
            # there is no other way but to register the callback here.
            _handle_add_callback(call, _done_callback_unary(span, code, details))
            return call
        except aio.AioRpcError as rpc_error:
            # NOTE: `AioRpcError` is raised in `await continuation(...)`
            # and `call` object is not assigned yet in that case.
            # So we can't handle the error in done callbacks.
            _handle_rpc_error(span, rpc_error)
            raise


class _UnaryUnaryClientInterceptor(aio.UnaryUnaryClientInterceptor, _ClientInterceptor):
    async def intercept_unary_unary(
        self,
        continuation: Callable[[aio.ClientCallDetails, RequestType], aio.UnaryUnaryCall],
        client_call_details: aio.ClientCallDetails,
        request: RequestType,
    ) -> Union[aio.UnaryUnaryCall, ResponseType]:
        span, client_call_details = self._intercept_client_call(
            constants.GRPC_METHOD_KIND_UNARY,
            client_call_details,
        )
        continuation_with_args = functools.partial(continuation, client_call_details, request)
        return await self._wrap_unary_response(continuation_with_args, span)


class _UnaryStreamClientInterceptor(aio.UnaryStreamClientInterceptor, _ClientInterceptor):
    async def intercept_unary_stream(
        self,
        continuation: Callable[[aio.ClientCallDetails, RequestType], aio.UnaryStreamCall],
        client_call_details: aio.ClientCallDetails,
        request: RequestType,
    ) -> Union[aio.UnaryStreamCall, ResponseIterableType]:
        span, client_call_details = self._intercept_client_call(
            constants.GRPC_METHOD_KIND_SERVER_STREAMING,
            client_call_details,
        )
        call = await continuation(client_call_details, request)
        return self._wrap_stream_response(call, span)


class _StreamUnaryClientInterceptor(aio.StreamUnaryClientInterceptor, _ClientInterceptor):
    async def intercept_stream_unary(
        self,
        continuation: Callable[[aio.ClientCallDetails, RequestType], aio.StreamUnaryCall],
        client_call_details: aio.ClientCallDetails,
        request_iterator: RequestIterableType,
    ) -> aio.StreamUnaryCall:
        span, client_call_details = self._intercept_client_call(
            constants.GRPC_METHOD_KIND_CLIENT_STREAMING,
            client_call_details,
        )
        continuation_with_args = functools.partial(continuation, client_call_details, request_iterator)
        return await self._wrap_unary_response(continuation_with_args, span)


class _StreamStreamClientInterceptor(aio.StreamStreamClientInterceptor, _ClientInterceptor):
    async def intercept_stream_stream(
        self,
        continuation: Callable[[aio.ClientCallDetails, RequestType], aio.StreamStreamCall],
        client_call_details: aio.ClientCallDetails,
        request_iterator: RequestIterableType,
    ) -> Union[aio.StreamStreamCall, ResponseIterableType]:
        span, client_call_details = self._intercept_client_call(
            constants.GRPC_METHOD_KIND_BIDI_STREAMING,
            client_call_details,
        )
        call = await continuation(client_call_details, request_iterator)
        return self._wrap_stream_response(call, span)
