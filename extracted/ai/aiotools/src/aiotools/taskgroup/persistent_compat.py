from __future__ import annotations

import asyncio
import itertools
import logging
import sys
import traceback
import weakref
from contextvars import ContextVar, Token
from types import TracebackType
from typing import (
    Any,
    Awaitable,
    Callable,
    Coroutine,
    Optional,
    Sequence,
    TypeVar,
)

from typing_extensions import Self

from .. import compat
from .common import create_task_with_name, patch_task
from .types import AsyncExceptionHandler

__all__ = [
    "PersistentTaskGroup",
    "current_ptaskgroup",
]

current_ptaskgroup: ContextVar["PersistentTaskGroup"] = ContextVar("current_ptaskgroup")

_ptaskgroup_idx = itertools.count()
_log = logging.getLogger(__name__)
_all_ptaskgroups: weakref.WeakSet[PersistentTaskGroup] = weakref.WeakSet()

T_co = TypeVar("T_co", covariant=True)


async def _default_exc_handler(
    exc_type: type[BaseException],
    exc_obj: BaseException,
    exc_tb: TracebackType,
) -> None:
    traceback.print_exc()


class PersistentTaskGroup:
    _base_error: Optional[BaseException]
    _exc_handler: AsyncExceptionHandler
    _tasks: set[asyncio.Task[Any]]
    _on_completed_fut: Optional[asyncio.Future[Any]]
    _current_taskgroup_token: Optional[Token[PersistentTaskGroup]]

    @classmethod
    def all_ptaskgroups(cls) -> Sequence[PersistentTaskGroup]:
        return list(_all_ptaskgroups)

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        exception_handler: Optional[AsyncExceptionHandler] = None,
    ) -> None:
        self._entered = False
        self._exiting = False
        self._aborting = False
        self._base_error = None
        self._name = name or f"{next(_ptaskgroup_idx)}"
        self._parent_cancel_requested = False
        self._unfinished_tasks = 0
        self._on_completed_fut = None
        self._parent_task = compat.current_task()
        self._tasks = set()
        self._current_taskgroup_token = None
        _all_ptaskgroups.add(self)
        if exception_handler is None:
            self._exc_handler = _default_exc_handler
        else:
            self._exc_handler = exception_handler

    # TODO: task statistics and enumeration (for aiomonitor)
    # TODO: two-phase shutdown

    def get_name(self) -> str:
        return self._name

    def create_task(
        self,
        coro: Coroutine[Any, Any, T_co] | Awaitable[T_co],
        *,
        name: Optional[str] = None,
    ) -> asyncio.Future[T_co]:
        if not self._entered:
            # When used as object attribute, auto-enter.
            self._entered = True
        if self._exiting and self._unfinished_tasks == 0:
            raise RuntimeError(f"{self!r} has already finished")
        return self._create_task_with_name(coro, name=name, cb=self._on_task_done)

    def _create_task_with_name(
        self,
        coro: Coroutine[Any, Any, T_co] | Awaitable[T_co],
        *,
        name: Optional[str] = None,
        cb: Callable[[asyncio.Task[None]], Any],
    ) -> asyncio.Future[T_co]:
        loop = compat.get_running_loop()
        result_future = loop.create_future()
        child_task = create_task_with_name(
            self._task_wrapper(coro, weakref.ref(result_future)),
            name=name,
        )
        _log.debug("%r is spawned in %r.", child_task, self)
        self._unfinished_tasks += 1
        child_task.add_done_callback(cb)
        self._tasks.add(child_task)
        return result_future

    def _is_base_error(self, exc: BaseException) -> bool:
        assert isinstance(exc, BaseException)
        return isinstance(exc, (SystemExit, KeyboardInterrupt))

    async def _wait_completion(self) -> Optional[bool]:
        loop = compat.get_running_loop()
        propagate_cancellation_error = None
        while self._unfinished_tasks:
            if self._on_completed_fut is None:
                self._on_completed_fut = loop.create_future()
            try:
                await self._on_completed_fut
            except asyncio.CancelledError:
                if not self._aborting:
                    propagate_cancellation_error = True
                    self._trigger_shutdown()
            self._on_completed_fut = None

        assert self._unfinished_tasks == 0
        self._on_completed_fut = None
        _all_ptaskgroups.discard(self)
        return propagate_cancellation_error

    def _trigger_shutdown(self) -> None:
        self._aborting = True
        for t in self._tasks:
            if not t.done():
                t.cancel()

    async def shutdown(self) -> None:
        self._trigger_shutdown()
        await self._wait_completion()

    async def _task_wrapper(
        self,
        coro: Coroutine[Any, Any, T_co] | Awaitable[T_co],
        result_future: weakref.ref[asyncio.Future[T_co]],
    ) -> T_co | None:
        loop = compat.get_running_loop()
        task = compat.current_task()
        fut = result_future()
        try:
            ret = await coro
            if fut is not None:
                fut.set_result(ret)
            return ret
        except asyncio.CancelledError:
            if fut is not None:
                fut.cancel()
            raise
        except Exception as e:
            # Swallow unhandled exceptions by our own and
            # prevent abortion of the task group bu them.
            # Wrapping corotuines directly has advantage for
            # exception handlers to access full traceback
            # and there is no need to implement separate
            # mechanism to wait for exception handler tasks.
            try:
                if fut is not None:
                    fut.set_exception(e)
                exc_info = sys.exc_info()
                assert exc_info[0] is not None
                assert exc_info[1] is not None
                assert exc_info[2] is not None
                await self._exc_handler(*exc_info)
            except Exception as exc:
                # If there are exceptions inside the exception handler
                # we report it as soon as possible using the event loop's
                # exception handler, instead of postponing
                # to the timing when PersistentTaskGroup terminates.
                loop.call_exception_handler({
                    "message": (
                        "Got an unhandled exception "
                        f"in the exception handler of Task {task!r}"
                    ),
                    "exception": exc,
                    "task": task,
                })
            return None
        finally:
            del fut

    def _on_task_done(self, task: asyncio.Task[None]) -> None:
        try:
            self._unfinished_tasks -= 1
            assert self._unfinished_tasks >= 0
            assert self._parent_task is not None

            if self._on_completed_fut is not None and not self._unfinished_tasks:
                if not self._on_completed_fut.done():
                    self._on_completed_fut.set_result(True)

            if task.cancelled():
                _log.debug("%r in %r has been cancelled.", task, self)
                return

            exc = task.exception()
            if exc is None:
                return

            # Now the exception is BaseException.
            if self._base_error is None:
                self._base_error = exc

            self._trigger_shutdown()
            if not self._parent_task.__cancel_requested__:  # type: ignore
                self._parent_cancel_requested = True
        finally:
            self._tasks.discard(task)

    async def __aenter__(self) -> Self:
        self._parent_task = compat.current_task()
        patch_task(self._parent_task)
        self._current_taskgroup_token = current_ptaskgroup.set(self)
        self._entered = True
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool | None:
        self._exiting = True
        propagate_cancelation = False

        if (
            exc_val is not None
            and self._is_base_error(exc_val)
            and self._base_error is None
        ):
            self._base_error = exc_val

        if exc_type is asyncio.CancelledError or exc_type is asyncio.TimeoutError:
            if self._parent_cancel_requested:
                # Only if we did request task to cancel ourselves
                # we mark it as no longer cancelled.
                self._parent_task.__cancel_requested__ = False  # type: ignore
            else:
                propagate_cancelation = True

        if exc_type is not None and not self._aborting:
            if exc_type is asyncio.CancelledError or exc_type is asyncio.TimeoutError:
                propagate_cancelation = True
            self._trigger_shutdown()

        prop_ex = await self._wait_completion()
        if prop_ex is not None:
            propagate_cancelation = prop_ex
        if self._current_taskgroup_token:
            current_ptaskgroup.reset(self._current_taskgroup_token)
            self._current_taskgroup_token = None

        if propagate_cancelation:
            # The wrapping task was cancelled; since we're done with
            # closing all child tasks, just propagate the cancellation
            # request now.
            raise asyncio.CancelledError()

        return None

    def __repr__(self) -> str:
        info = [""]
        if self._name:
            info.append(f"name={self._name}")
        if self._tasks:
            info.append(f"tasks={len(self._tasks)}")
        if self._unfinished_tasks:
            info.append(f"unfinished={self._unfinished_tasks}")
        if self._aborting:
            info.append("cancelling")
        elif self._entered:
            info.append("entered")
        info_str = " ".join(info)
        return f"<PersistentTaskGroup({info_str})>"
