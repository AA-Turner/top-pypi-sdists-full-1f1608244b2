from aiopg import __version__
from aiopg.utils import _ContextManager
import wrapt

from ddtrace import config
from ddtrace.constants import _SPAN_MEASURED_KEY
from ddtrace.constants import SPAN_KIND
from ddtrace.contrib import dbapi
from ddtrace.contrib import trace_utils
from ddtrace.ext import SpanKind
from ddtrace.ext import SpanTypes
from ddtrace.ext import db
from ddtrace.internal.constants import COMPONENT
from ddtrace.internal.schema import schematize_database_operation
from ddtrace.internal.schema import schematize_service_name
from ddtrace.internal.utils.version import parse_version
from ddtrace.trace import Pin


AIOPG_VERSION = parse_version(__version__)


class AIOTracedCursor(wrapt.ObjectProxy):
    """TracedCursor wraps a psql cursor and traces its queries."""

    def __init__(self, cursor, pin):
        super(AIOTracedCursor, self).__init__(cursor)
        pin.onto(self)
        self._datadog_name = schematize_database_operation("postgres.query", database_provider="postgresql")

    async def _trace_method(self, method, resource, extra_tags, *args, **kwargs):
        pin = Pin.get_from(self)
        if not pin or not pin.enabled():
            result = await method(*args, **kwargs)
            return result

        with pin.tracer.trace(
            self._datadog_name,
            service=trace_utils.ext_service(pin, config.aiopg),
            resource=resource,
            span_type=SpanTypes.SQL,
        ) as s:
            s.set_tag_str(COMPONENT, config.aiopg.integration_name)
            s.set_tag_str(db.SYSTEM, "postgresql")

            # set span.kind to the type of request being performed
            s.set_tag_str(SPAN_KIND, SpanKind.CLIENT)

            s.set_tag(_SPAN_MEASURED_KEY)
            s.set_tags(pin.tags)
            s.set_tags(extra_tags)

            try:
                result = await method(*args, **kwargs)
                return result
            finally:
                s.set_metric(db.ROWCOUNT, self.rowcount)

    async def executemany(self, query, *args, **kwargs):
        # FIXME[matt] properly handle kwargs here. arg names can be different
        # with different libs.
        result = await self._trace_method(
            self.__wrapped__.executemany, query, {"sql.executemany": "true"}, query, *args, **kwargs
        )
        return result

    async def execute(self, query, *args, **kwargs):
        result = await self._trace_method(self.__wrapped__.execute, query, {}, query, *args, **kwargs)
        return result

    async def callproc(self, proc, args):
        result = await self._trace_method(self.__wrapped__.callproc, proc, {}, proc, args)
        return result

    def __aiter__(self):
        return self.__wrapped__.__aiter__()


class AIOTracedConnection(wrapt.ObjectProxy):
    """TracedConnection wraps a Connection with tracing code."""

    def __init__(self, conn, pin=None, cursor_cls=AIOTracedCursor):
        super(AIOTracedConnection, self).__init__(conn)
        vendor = dbapi._get_vendor(conn)
        name = schematize_service_name(vendor)
        db_pin = pin or Pin(service=name)
        db_pin.onto(self)
        # wrapt requires prefix of `_self` for attributes that are only in the
        # proxy (since some of our source objects will use `__slots__`)
        self._self_cursor_cls = cursor_cls

    # unfortunately we also need to patch this method as otherwise "self"
    # ends up being the aiopg connection object
    if AIOPG_VERSION >= (0, 16, 0):

        def cursor(self, *args, **kwargs):
            # Only one cursor per connection is allowed, as per DB API spec
            self.close_cursor()
            self._last_usage = self._loop.time()

            coro = self._cursor(*args, **kwargs)
            return _ContextManager(coro)

    else:

        def cursor(self, *args, **kwargs):
            coro = self._cursor(*args, **kwargs)
            return _ContextManager(coro)

    async def _cursor(self, *args, **kwargs):
        cursor = await self.__wrapped__._cursor(*args, **kwargs)
        pin = Pin.get_from(self)
        if not pin:
            return cursor
        return self._self_cursor_cls(cursor, pin)
