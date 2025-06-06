import sys

import celery
from celery import signals

from ddtrace import config
from ddtrace._trace.pin import _DD_PIN_NAME
from ddtrace.constants import _SPAN_MEASURED_KEY
from ddtrace.constants import SPAN_KIND
from ddtrace.contrib import trace_utils
from ddtrace.contrib.internal.celery.signals import trace_after_publish
from ddtrace.contrib.internal.celery.signals import trace_before_publish
from ddtrace.contrib.internal.celery.signals import trace_failure
from ddtrace.contrib.internal.celery.signals import trace_postrun
from ddtrace.contrib.internal.celery.signals import trace_prerun
from ddtrace.contrib.internal.celery.signals import trace_retry
from ddtrace.ext import SpanKind
from ddtrace.ext import SpanTypes
from ddtrace.internal import core
from ddtrace.internal.logger import get_logger
from ddtrace.trace import Pin


log = get_logger(__name__)


def patch_app(app, pin=None):
    """Attach the Pin class to the application and connect
    our handlers to Celery signals.
    """
    if getattr(app, "__datadog_patch", False):
        return
    app.__datadog_patch = True

    # attach the PIN object
    pin = pin or Pin(
        service=config.celery["worker_service_name"],
        _config=config.celery,
    )
    pin.onto(app)

    trace_utils.wrap(
        "celery.beat",
        "Scheduler.apply_entry",
        _traced_beat_function(config.celery, "apply_entry", lambda args: args[0].name),
    )
    trace_utils.wrap("celery.beat", "Scheduler.tick", _traced_beat_function(config.celery, "tick"))
    pin.onto(celery.beat.Scheduler)

    # Patch apply_async
    trace_utils.wrap("celery.app.task", "Task.apply_async", _traced_apply_async_function(config.celery, "apply_async"))

    # connect to the Signal framework
    signals.task_prerun.connect(trace_prerun, weak=False)
    signals.task_postrun.connect(trace_postrun, weak=False)
    signals.before_task_publish.connect(trace_before_publish, weak=False)
    signals.after_task_publish.connect(trace_after_publish, weak=False)
    signals.task_failure.connect(trace_failure, weak=False)
    signals.task_retry.connect(trace_retry, weak=False)
    return app


def unpatch_app(app):
    """Remove the Pin instance from the application and disconnect
    our handlers from Celery signal framework.
    """
    if not getattr(app, "__datadog_patch", False):
        return
    app.__datadog_patch = False

    pin = Pin.get_from(app)
    if pin is not None:
        delattr(app, _DD_PIN_NAME)

    trace_utils.unwrap(celery.beat.Scheduler, "apply_entry")
    trace_utils.unwrap(celery.beat.Scheduler, "tick")
    trace_utils.unwrap(celery.app.task.Task, "apply_async")

    signals.task_prerun.disconnect(trace_prerun)
    signals.task_postrun.disconnect(trace_postrun)
    signals.before_task_publish.disconnect(trace_before_publish)
    signals.after_task_publish.disconnect(trace_after_publish)
    signals.task_failure.disconnect(trace_failure)
    signals.task_retry.disconnect(trace_retry)


def _traced_beat_function(integration_config, fn_name, resource_fn=None):
    def _traced_beat_inner(func, instance, args, kwargs):
        pin = Pin.get_from(instance)
        if not pin or not pin.enabled():
            return func(*args, **kwargs)

        with pin.tracer.trace(
            "celery.beat.{}".format(fn_name),
            span_type=SpanTypes.WORKER,
            service=trace_utils.ext_service(pin, integration_config),
        ) as span:
            if resource_fn:
                span.resource = resource_fn(args)
            span.set_tag_str(SPAN_KIND, SpanKind.PRODUCER)
            span.set_tag(_SPAN_MEASURED_KEY)

            return func(*args, **kwargs)

    return _traced_beat_inner


def _traced_apply_async_function(integration_config, fn_name, resource_fn=None):
    """
    When apply_async is called, it calls various Celery signals in order, which gets used
    to start and close the span.
    Example: before_task_publish starts the span while after_task_publish closes the span.
    If an exception occurs anywhere inside Celery or its dependencies, this can interrupt the
    closing signals.
    The purpose of _traced_apply_async_function is to close the spans even if one of the closing
    signals don't get called over the course of the apply_task lifecycle.
    This is done by fetching the stored span and closing it if it hasn't already been closed by a
    closing signal.
    """

    def _traced_apply_async_inner(func, instance, args, kwargs):
        with core.context_with_data("task_context"):
            try:
                return func(*args, **kwargs)
            except Exception:
                # If an internal exception occurs, record the exception in the span,
                # then raise the Celery error as usual
                task_span = core.get_item("task_span")
                if task_span:
                    task_span.set_exc_info(*sys.exc_info())

                raise
            finally:
                task_span = core.get_item("task_span")
                if task_span:
                    log.debug(
                        "The after_task_publish signal was not called, so manually closing span: %s",
                        task_span._pprint(),
                    )
                    task_span.finish()

    return _traced_apply_async_inner
