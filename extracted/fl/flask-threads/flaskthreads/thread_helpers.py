# Copyright 2019 Alexey Minakov. All Rights Reserved.

"""Implements ThreadPoolExecutor with flask AppContext."""

__author__ = 'Alexey Minakov (a@spb.host)'

import atexit
from concurrent.futures import _base
import itertools
import queue
import threading
import weakref
import os

from flask import has_app_context

_get_app_context = None
try:
    # For Flask <3.0.0
    from flask import _app_ctx_stack
    _get_app_context = lambda: _app_ctx_stack.top
except ImportError:
    # For Flask >=3.0.0
    from flask.globals import app_ctx as app_context
    _get_app_context = lambda: app_context._get_current_object()


APP_CONTEXT_ERROR = 'Running outside of Flask AppContext.'

# This code is 1-1 copy of ThreadPoolExecutor from Python standard library
# The only difference is the usage of Flask's app context.

# Workers are created as daemon threads. This is done to allow the interpreter
# to exit when there are still idle threads in a ThreadPoolExecutor's thread
# pool (i.e. shutdown() was not called). However, allowing workers to die with
# the interpreter has two undesirable properties:
#   - The workers would still be running during interpreter shutdown,
#     meaning that they would fail in unpredictable ways.
#   - The workers could be killed while evaluating a work item, which could
#     be bad if the callable being evaluated has external side-effects e.g.
#     writing to a file.
#
# To work around this problem, an exit handler is installed which tells the
# workers to exit when their work queues are empty and then waits until the
# threads finish.

_threads_queues = weakref.WeakKeyDictionary()
_shutdown = False


def _python_exit():
    global _shutdown
    _shutdown = True
    items = list(_threads_queues.items())
    for t, q in items:
        q.put(None)
    for t, q in items:
        t.join()


atexit.register(_python_exit)


class _WorkItemWithContext(object):
    def __init__(self, app_ctx, future, fn, args, kwargs):
        self.app_ctx = app_ctx
        self.future = future
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self):
        if not self.future.set_running_or_notify_cancel():
            return

        try:
            app_ctx = self.app_ctx  # Capture ctx since we may set self to None
            app_ctx.push()
            result = self.fn(*self.args, **self.kwargs)
        except BaseException as exc:
            self.future.set_exception(exc)
            # Break a reference cycle with the exception 'exc'
            self = None
        else:
            self.future.set_result(result)
        finally:
            app_ctx.pop()


def _worker(executor_reference, work_queue):
    try:
        while True:
            work_item = work_queue.get(block=True)
            if work_item is not None:
                work_item.run()
                # Delete references to object. See issue16284
                del work_item
                continue
            executor = executor_reference()
            # Exit if:
            #   - The interpreter is shutting down OR
            #   - The executor that owns the worker has been collected OR
            #   - The executor that owns the worker has been shutdown.
            if _shutdown or executor is None or executor._shutdown:
                # Notice other workers
                work_queue.put(None)
                return
            del executor
    except BaseException:
        _base.LOGGER.critical('Exception in worker', exc_info=True)


class ThreadPoolWithAppContextExecutor(_base.Executor):
    # Used to assign unique thread names when
    # thread_name_prefix is not supplied.
    _counter = itertools.count().__next__

    def __init__(self, max_workers=None, thread_name_prefix=''):
        """Initializes a new ThreadPoolExecutor instance.

        Args:
            max_workers: The maximum number of threads that can be used to
                execute the given calls.
            thread_name_prefix: An optional name prefix to give our threads.
        """
        if max_workers is None:
            # Use this number because ThreadPoolExecutor is often
            # used to overlap I/O instead of CPU work.
            max_workers = (os.cpu_count() or 1) * 5
        if max_workers <= 0:
            raise ValueError("max_workers must be greater than 0")

        if not has_app_context():
            raise RuntimeError(APP_CONTEXT_ERROR)

        self._app_ctx = _get_app_context()
        self._max_workers = max_workers
        self._work_queue = queue.Queue()
        self._threads = set()
        self._shutdown = False
        self._shutdown_lock = threading.Lock()
        self._thread_name_prefix = (
            thread_name_prefix or
            ("ThreadPoolExecutor-%d" % self._counter()))

    def submit(self, fn, *args, **kwargs):
        with self._shutdown_lock:
            if self._shutdown:
                raise RuntimeError(
                    'cannot schedule new futures after shutdown')

            f = _base.Future()
            w = _WorkItemWithContext(self._app_ctx, f, fn, args, kwargs)

            self._work_queue.put(w)
            self._adjust_thread_count()
            return f
    submit.__doc__ = _base.Executor.submit.__doc__

    def _adjust_thread_count(self):
        # When the executor gets lost, the weakref callback will wake up
        # the worker threads.
        def weakref_cb(_, q=self._work_queue):
            q.put(None)
        # TODO(bquinlan): Should avoid creating new threads if there are more
        # idle threads than items in the work queue.
        num_threads = len(self._threads)
        if num_threads < self._max_workers:
            thread_name = '%s_%d' % (self._thread_name_prefix or self,
                                     num_threads)
            t = threading.Thread(name=thread_name, target=_worker,
                                 args=(weakref.ref(self, weakref_cb),
                                       self._work_queue))
            t.daemon = True
            t.start()
            self._threads.add(t)
            _threads_queues[t] = self._work_queue

    def shutdown(self, wait=True):
        with self._shutdown_lock:
            self._shutdown = True
            self._work_queue.put(None)
        if wait:
            for t in self._threads:
                t.join()
    shutdown.__doc__ = _base.Executor.shutdown.__doc__


class AppContextThread(threading.Thread):
    """Implements Thread with flask AppContext."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not has_app_context():
            raise RuntimeError(APP_CONTEXT_ERROR)
        self.app_ctx = _get_app_context()

    def run(self):
        try:
            self.app_ctx.push()
            super().run()
        finally:
            self.app_ctx.pop()
