#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import copy
import logging
import random
import time
from time import monotonic as now

from oslo_service._i18n import _
from oslo_service import _options
from oslo_utils import reflection

LOG = logging.getLogger(__name__)

DEFAULT_INTERVAL = 60.0


def list_opts():
    """Entry point for oslo-config-generator."""
    return [(None, copy.deepcopy(_options.periodic_opts))]


class InvalidPeriodicTaskArg(Exception):
    message = _("Unexpected argument for periodic task creation: %(arg)s.")


def periodic_task(*args, **kwargs):
    """Decorator to indicate that a method is a periodic task.

    This decorator can be used in two ways:

        1. Without arguments '@periodic_task', this will be run on the default
           interval of 60 seconds.

        2. With arguments:
           @periodic_task(spacing=N [, run_immediately=[True|False]]
           [, name=[None|"string"])
           this will be run on approximately every N seconds. If this number is
           negative the periodic task will be disabled. If the run_immediately
           argument is provided and has a value of 'True', the first run of the
           task will be shortly after task scheduler starts.  If
           run_immediately is omitted or set to 'False', the first time the
           task runs will be approximately N seconds after the task scheduler
           starts. If name is not provided, __name__ of function is used.
    """
    def decorator(f):
        # Test for old style invocation
        if 'ticks_between_runs' in kwargs:
            raise InvalidPeriodicTaskArg(arg='ticks_between_runs')

        # Control if run at all
        f._periodic_task = True
        f._periodic_external_ok = kwargs.pop('external_process_ok', False)
        f._periodic_enabled = kwargs.pop('enabled', True)
        f._periodic_name = kwargs.pop('name', f.__name__)

        # Control frequency
        f._periodic_spacing = kwargs.pop('spacing', 0)
        f._periodic_immediate = kwargs.pop('run_immediately', False)
        if f._periodic_immediate:
            f._periodic_last_run = None
        else:
            f._periodic_last_run = now()
        return f

    # NOTE(sirp): The `if` is necessary to allow the decorator to be used with
    # and without parenthesis.
    #
    # In the 'with-parenthesis' case (with kwargs present), this function needs
    # to return a decorator function since the interpreter will invoke it like:
    #
    #   periodic_task(*args, **kwargs)(f)
    #
    # In the 'without-parenthesis' case, the original function will be passed
    # in as the first argument, like:
    #
    #   periodic_task(f)
    if kwargs:
        return decorator
    else:
        return decorator(args[0])


class _PeriodicTasksMeta(type):
    def _add_periodic_task(cls, task):
        """Add a periodic task to the list of periodic tasks.

        The task should already be decorated by @periodic_task.

        :return: whether task was actually enabled
        """
        name = task._periodic_name

        if task._periodic_spacing < 0:
            LOG.info('Skipping periodic task %(task)s because '
                     'its interval is negative',
                     {'task': name})
            return False
        if not task._periodic_enabled:
            LOG.info('Skipping periodic task %(task)s because '
                     'it is disabled',
                     {'task': name})
            return False

        # A periodic spacing of zero indicates that this task should
        # be run on the default interval to avoid running too
        # frequently.
        if task._periodic_spacing == 0:
            task._periodic_spacing = DEFAULT_INTERVAL

        cls._periodic_tasks.append((name, task))
        cls._periodic_spacing[name] = task._periodic_spacing
        return True

    def __init__(cls, names, bases, dict_):
        """Metaclass that allows us to collect decorated periodic tasks."""
        super().__init__(names, bases, dict_)

        # NOTE(sirp): if the attribute is not present then we must be the base
        # class, so, go ahead an initialize it. If the attribute is present,
        # then we're a subclass so make a copy of it so we don't step on our
        # parent's toes.
        try:
            cls._periodic_tasks = cls._periodic_tasks[:]
        except AttributeError:
            cls._periodic_tasks = []

        try:
            cls._periodic_spacing = cls._periodic_spacing.copy()
        except AttributeError:
            cls._periodic_spacing = {}

        for value in cls.__dict__.values():
            if getattr(value, '_periodic_task', False):
                cls._add_periodic_task(value)


def _nearest_boundary(last_run, spacing):
    """Find the nearest boundary in the past.

    The boundary is a multiple of the spacing with the last run as an offset.

    Eg if last run was 10 and spacing was 7, the new last run could be: 17, 24,
    31, 38...

    0% to 5% of the spacing value will be added to this value to ensure tasks
    do not synchronize. This jitter is rounded to the nearest second, this
    means that spacings smaller than 20 seconds will not have jitter.
    """
    current_time = now()
    if last_run is None:
        return current_time
    delta = current_time - last_run
    offset = delta % spacing
    # Add up to 5% jitter
    jitter = int(spacing * (random.random() / 20))  # nosec
    return current_time - offset + jitter


class PeriodicTasks(metaclass=_PeriodicTasksMeta):
    def __init__(self, conf):
        super().__init__()
        self.conf = conf
        self.conf.register_opts(_options.periodic_opts)
        self._periodic_last_run = {}
        for name, task in self._periodic_tasks:
            self._periodic_last_run[name] = task._periodic_last_run

    def add_periodic_task(self, task):
        """Add a periodic task to the list of periodic tasks.

        The task should already be decorated by @periodic_task.
        """
        if self.__class__._add_periodic_task(task):
            self._periodic_last_run[task._periodic_name] = (
                task._periodic_last_run)

    def run_periodic_tasks(self, context, raise_on_error=False):
        """Tasks to be run at a periodic interval."""
        idle_for = DEFAULT_INTERVAL
        for task_name, task in self._periodic_tasks:
            if (task._periodic_external_ok and not
               self.conf.run_external_periodic_tasks):
                continue
            cls_name = reflection.get_class_name(self, fully_qualified=False)
            full_task_name = '.'.join([cls_name, task_name])

            spacing = self._periodic_spacing[task_name]
            last_run = self._periodic_last_run[task_name]

            # Check if due, if not skip
            idle_for = min(idle_for, spacing)
            if last_run is not None:
                delta = last_run + spacing - now()
                if delta > 0:
                    idle_for = min(idle_for, delta)
                    continue

            LOG.debug("Running periodic task %(full_task_name)s",
                      {"full_task_name": full_task_name})
            self._periodic_last_run[task_name] = _nearest_boundary(
                last_run, spacing)

            try:
                task(self, context)
            except BaseException:
                if raise_on_error:
                    raise
                LOG.exception("Error during %(full_task_name)s",
                              {"full_task_name": full_task_name})
            time.sleep(0)

        return idle_for
