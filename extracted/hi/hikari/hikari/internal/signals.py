# Copyright (c) 2020 Nekokatt
# Copyright (c) 2021-present davfsa
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Signal handling utilities."""

from __future__ import annotations

__all__: typing.Sequence[str] = ("handle_interrupts",)

import contextlib
import logging
import signal
import threading
import traceback
import typing

from hikari import errors
from hikari.internal import ux

if typing.TYPE_CHECKING:
    import asyncio
    import types

    _SignalHandlerT = typing.Callable[[int, typing.Optional[types.FrameType]], None]

_INTERRUPT_SIGNALS: tuple[str, ...] = ("SIGINT", "SIGTERM")
_LOGGER: typing.Final[logging.Logger] = logging.getLogger("hikari.signals")


def _raise_interrupt(signum: int) -> typing.NoReturn:
    signame = signal.strsignal(signum)
    assert signame is not None

    raise errors.HikariInterrupt(signum, signame)


def _interrupt_handler(loop: asyncio.AbstractEventLoop) -> _SignalHandlerT:
    loop_thread_id = threading.get_native_id()

    def handler(signum: int, frame: types.FrameType | None) -> None:
        # The loop may or may not be running, depending on the state of the application when this occurs.
        # Signals on POSIX only occur on the main thread usually, too, so we need to ensure this is
        # threadsafe.
        # We log native thread IDs purely for debugging purposes.
        if _LOGGER.isEnabledFor(ux.TRACE):
            _LOGGER.log(
                ux.TRACE,
                "interrupt %s occurred on thread %s, process on thread %s will be notified shortly\n"
                "Stacktrace for developer sanity:\n%s",
                signum,
                threading.get_native_id(),
                loop_thread_id,
                "".join(traceback.format_stack(frame)),
            )

        loop.call_soon_threadsafe(_raise_interrupt, signum)

    return handler


@contextlib.contextmanager
def handle_interrupts(
    loop: asyncio.AbstractEventLoop, *, propagate_interrupts: bool, enabled: bool | None
) -> typing.Generator[None, None, None]:
    """Context manager which cleanly exits on signal interrupts.

    Parameters
    ----------
    loop
        The event loop the interrupt will be raised in.
    propagate_interrupts
        Whether to propagate interrupts.
    enabled
        Whether to enable the signal interrupts.

        If set to [`None`][], then it will be enabled or not based on whether the running
        thread is the main one or not.
    """
    if enabled is None:
        enabled = threading.current_thread() is threading.main_thread()

    if not enabled:
        # NOOP context manager
        yield
        return

    interrupt_handler = _interrupt_handler(loop)
    original_handlers: dict[int, int | _SignalHandlerT | None] = {}

    for sig in _INTERRUPT_SIGNALS:
        try:
            signum = getattr(signal, sig)
        except AttributeError:  # noqa: PERF203 - no try except within a loop
            _LOGGER.log(ux.TRACE, "signal %s is not implemented on your platform; skipping", sig)
        else:
            original_handlers[signum] = signal.getsignal(signum)
            signal.signal(signum, interrupt_handler)

    try:
        yield

    except errors.HikariInterrupt:
        if propagate_interrupts:
            raise

    finally:
        for signum, handler in original_handlers.items():
            signal.signal(signum, handler)
