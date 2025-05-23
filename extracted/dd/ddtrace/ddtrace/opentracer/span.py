import threading
from typing import TYPE_CHECKING  # noqa:F401
from typing import Any  # noqa:F401
from typing import Dict  # noqa:F401
from typing import Optional  # noqa:F401
from typing import Text  # noqa:F401
from typing import Union  # noqa:F401

from opentracing import Span as OpenTracingSpan
from opentracing.ext import tags as OTTags

from ddtrace.constants import ERROR_MSG
from ddtrace.constants import ERROR_STACK
from ddtrace.constants import ERROR_TYPE
from ddtrace.internal.compat import NumericType  # noqa:F401
from ddtrace.internal.constants import SPAN_API_OPENTRACING
from ddtrace.trace import Context as DatadogContext  # noqa:F401
from ddtrace.trace import Span as DatadogSpan

from .span_context import SpanContext
from .tags import Tags


if TYPE_CHECKING:  # pragma: no cover
    from ddtrace.trace import Tracer  # noqa:F401


_TagNameType = Union[Text, bytes]


class Span(OpenTracingSpan):
    """Datadog implementation of :class:`opentracing.Span`"""

    def __init__(self, tracer, context, operation_name):
        # type: (Tracer, Optional[SpanContext], str) -> None
        if context is not None:
            context = SpanContext(ddcontext=context._dd_context, baggage=context.baggage)
        else:
            context = SpanContext()

        super(Span, self).__init__(tracer, context)

        self.finished = False
        self._lock = threading.Lock()
        # use a datadog span
        self._dd_span = DatadogSpan(operation_name, context=context._dd_context, span_api=SPAN_API_OPENTRACING)

    def finish(self, finish_time=None):
        # type: (Optional[float]) -> None
        """Finish the span.

        This calls finish on the ddspan.

        :param finish_time: specify a custom finish time with a unix timestamp
            per time.time()
        :type timestamp: float
        """
        if self.finished:
            return

        # finish the datadog span
        self._dd_span.finish(finish_time)
        self.finished = True

    def set_baggage_item(self, key, value):
        # type: (str, Any) -> Span
        """Sets a baggage item in the span context of this span.

        Baggage is used to propagate state between spans.

        :param key: baggage item key
        :type key: str

        :param value: baggage item value
        :type value: a type that can be str'd

        :rtype: Span
        :return: itself for chaining calls
        """
        new_ctx = self.context.with_baggage_item(key, value)
        with self._lock:
            self._context = new_ctx
        return self

    def get_baggage_item(self, key):
        # type: (str) -> Optional[str]
        """Gets a baggage item from the span context of this span.

        :param key: baggage item key
        :type key: str

        :rtype: str
        :return: the baggage value for the given key or ``None``.
        """
        return self.context.get_baggage_item(key)

    def set_operation_name(self, operation_name):
        # type: (str) -> Span
        """Set the operation name."""
        self._dd_span.name = operation_name
        return self

    def log_kv(self, key_values, timestamp=None):
        # type: (Dict[_TagNameType, Any], Optional[float]) -> Span
        """Add a log record to this span.

        Passes on relevant opentracing key values onto the datadog span.

        :param key_values: a dict of string keys and values of any type
        :type key_values: dict

        :param timestamp: a unix timestamp per time.time()
        :type timestamp: float

        :return: the span itself, for call chaining
        :rtype: Span
        """

        # match opentracing defined keys to datadog functionality
        # opentracing/specification/blob/1be630515dafd4d2a468d083300900f89f28e24d/semantic_conventions.md#log-fields-table  # noqa: E501
        for key, val in key_values.items():
            if key == "event" and val == "error":
                # TODO: not sure if it's actually necessary to set the error manually
                self._dd_span.error = 1
                self.set_tag("error", 1)
            elif key == "error" or key == "error.object":
                self.set_tag(ERROR_TYPE, val)
            elif key == "message":
                self.set_tag(ERROR_MSG, val)
            elif key == "stack":
                self.set_tag(ERROR_STACK, val)
            else:
                pass

        return self

    def set_tag(self, key, value):
        # type: (_TagNameType, Any) -> Span
        """Set a tag on the span.

        This sets the tag on the underlying datadog span.
        """
        if key == Tags.SPAN_TYPE:
            self._dd_span.span_type = value
        elif key == Tags.SERVICE_NAME:
            self._dd_span.service = value
        elif key == Tags.RESOURCE_NAME or key == OTTags.DATABASE_STATEMENT:
            self._dd_span.resource = value
        elif key == OTTags.PEER_HOSTNAME:
            self._dd_span.set_tag_str(Tags.TARGET_HOST, value)
        elif key == OTTags.PEER_PORT:
            self._dd_span.set_tag(Tags.TARGET_PORT, value)
        elif key == Tags.SAMPLING_PRIORITY:
            self._dd_span.context.sampling_priority = value
        else:
            self._dd_span.set_tag(key, value)
        return self

    def _get_tag(self, key):
        # type: (_TagNameType) -> Optional[Text]
        """Gets a tag from the span.

        This method retrieves the tag from the underlying datadog span.
        """
        return self._dd_span.get_tag(key)

    def _get_metric(self, key):
        # type: (_TagNameType) -> Optional[NumericType]
        """Gets a metric from the span.

        This method retrieves the metric from the underlying datadog span.
        """
        return self._dd_span.get_metric(key)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._dd_span.set_exc_info(exc_type, exc_val, exc_tb)

        # note: self.finish() AND _dd_span.__exit__ will call _span.finish() but
        # it is idempotent
        self._dd_span.__exit__(exc_type, exc_val, exc_tb)
        self.finish()

    def _associate_dd_span(self, ddspan):
        # type: (DatadogSpan) -> None
        """Associates a DD span with this span."""
        # get the datadog span context
        self._dd_span = ddspan
        self.context._dd_context = ddspan.context

    @property
    def _dd_context(self):
        # type: () -> DatadogContext
        return self._dd_span.context
