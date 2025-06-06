# Copyright (c) 2025, NVIDIA CORPORATION.
# SPDX-License-Identifier: BSD-3-Clause

import inspect
import linecache
import os
import sys
import threading
import time
import traceback
from time import perf_counter
from typing import Any, Callable, Iterable, Iterator, Optional, TypeVar

import torch
from torch.distributed._shard.sharded_tensor import ShardedTensorBase

# For the watch_iter type
T = TypeVar("T")

# Maximum length of a single object string to print.
PRINT_LOCAL_MAX_LENGTH = 250


class Watchdog:
    """
    A watchdog timer that:
      - can be 'enabled' or 'disabled' by presence/absence of a deadline,
      - resets automatically when 'enable()' is called,
      - can be used as a context manager,
      - can wrap an iterator to watch only the time for 'next()' calls,
      - attempts a two-phase shutdown on callback error:
         1) sys.exit(1) for graceful,
         2) if still alive after 10s, os._exit(1).
    """

    def __init__(
        self,
        timeout: float,
        initial_timeout: Optional[float] = None,
        callback: Optional[Callable[[], None]] = None,
        dump_stacks: bool = True,
        enabled: bool = True,
    ) -> None:
        """
        Args:
            timeout: Number of seconds before the watchdog fires if not reset/disabled.
            initial_timeout: Number of seconds before the watchdog fires in the first iteration.
            callback: Optional function to call upon timeout.
            dump_stacks: If True, print full stack traces for all threads on timeout (except watchdog's own thread).
            enabled: If False, watchdog starts disabled until enable() is called.
        """
        self._timeout = timeout
        self._initial_timeout = initial_timeout
        self._callback = callback
        self._dump_stacks = dump_stacks
        self._is_first_iteration = True

        # If _deadline is None, the watchdog is disabled.
        # Otherwise, _deadline = time.time() + _timeout if enabled.
        if enabled:
            self._deadline: Optional[float] = perf_counter() + self._get_next_timeout()
        else:
            self._deadline = None

        self._stop = False  # signals permanent shutdown (finish)

        # Condition variable to manage state changes
        self._cv = threading.Condition()
        # Background thread (daemon) that monitors timeouts
        self._worker_thread = threading.Thread(target=self._worker, daemon=True)
        self._worker_thread.start()

    def _get_next_timeout(self) -> float:
        if self._is_first_iteration:
            self._is_first_iteration = False
            return self._initial_timeout if self._initial_timeout is not None else self._timeout
        else:
            return self._timeout

    def _worker(self) -> None:
        """
        Background thread that periodically checks if the watchdog has expired.
        Once it times out or is told to stop, it exits.
        """
        while True:
            with self._cv:
                if self._stop:
                    # finish() was called; end the worker.
                    return

                if self._deadline is None:
                    # Disabled; no deadline. Just wait a bit, then re-check.
                    self._cv.wait(timeout=1.0)
                    continue

                remaining = self._deadline - perf_counter()
                if remaining <= 0:
                    # We have timed out
                    self._on_timeout()
                    return
                else:
                    # Wait until either the deadline or a state change
                    self._cv.wait(timeout=remaining)

    def _on_timeout(self) -> None:
        """
        Called exactly once if the watchdog times out.
        1) Optionally dumps stacks,
        2) Calls user callback,
        3) If callback raises an error,
           - print traceback,
           - sys.exit(1),
           - fallback to os._exit(1) after 10s if process not terminated.
        """
        watchdog_thread_id = threading.get_ident()

        # 1) Dump stacks if requested
        if self._dump_stacks:
            print("Watchdog triggered: Dumping thread stacks")
            self._print_all_thread_stacks(skip_thread_id=watchdog_thread_id)

        # 2) Call user callback
        if self._callback:
            try:
                self._callback()
            except Exception:
                # Print the traceback
                traceback.print_exc()

                # Start a background kill-switch after 10 seconds
                def force_exit_after_delay() -> None:
                    time.sleep(10)
                    os._exit(1)

                killer = threading.Thread(target=force_exit_after_delay, daemon=True)
                killer.start()

                # Attempt graceful shutdown
                sys.exit(1)

    def _print_all_thread_stacks(self, skip_thread_id: Optional[int] = None) -> None:
        """
        Dump stacks of all threads in a style reminiscent of py-spy, from
        innermost (current) to outermost. Skip the watchdog's own thread if given.

        Args:
            skip_thread_id: If given, skip this thread's stack.
        """

        frames = sys._current_frames()  # thread_id -> frame
        # We gather known threads to print their names
        all_threads = {t.ident: t for t in threading.enumerate()}

        for thread_id, frame in frames.items():
            if skip_thread_id is not None and thread_id == skip_thread_id:
                continue

            thread = all_threads.get(thread_id)
            thread_name = thread.name if thread else f"Unknown-{thread_id}"
            print(f'Thread {thread_id}: "{thread_name}"')

            # Build the stack from current (innermost) to outermost
            stack_frames = []
            f = frame
            while f is not None:
                stack_frames.append(f)
                f = f.f_back

            for fr in stack_frames:
                code = fr.f_code
                func_name = code.co_name
                filename = code.co_filename
                lineno = fr.f_lineno

                print(f"    {func_name} ({filename}:{lineno})")

                # Attempt to read the actual line of source
                line = linecache.getline(filename, lineno).rstrip()
                if line:
                    print(f"        > {line}")

                # Show arguments and locals
                arg_info = inspect.getargvalues(fr)
                arg_names = arg_info.args
                varargs = arg_info.varargs
                varkw = arg_info.keywords
                local_vars = arg_info.locals

                # Separate out the arguments
                arg_dict = {}
                for arg in arg_names:
                    if arg in local_vars:
                        arg_dict[arg] = local_vars[arg]
                if varargs and varargs in local_vars:
                    arg_dict["*" + varargs] = local_vars[varargs]
                if varkw and varkw in local_vars:
                    arg_dict["**" + varkw] = local_vars[varkw]

                if arg_dict:
                    print("        Arguments:")
                    for k, v in arg_dict.items():
                        print(f"            {k}: {repr_short(v)}")

                other_locals = {k: v for k, v in local_vars.items() if k not in arg_dict}
                if other_locals:
                    print("        Locals:")
                    for k, v in other_locals.items():
                        print(f"            {k}: {repr_short(v)}")

            print(flush=True)

    def reset(self) -> None:
        """
        Reset the watchdog timer (push out deadline by `timeout` seconds),
        but only if currently enabled (i.e., _deadline is not None).
        """
        with self._cv:
            if self._deadline is not None:
                self._deadline = perf_counter() + self._timeout
                self._cv.notify()

    def enable(self) -> None:
        """
        Enable (or re-enable) the watchdog. Always resets the deadline to
        `time.time() + timeout`.
        """
        with self._cv:
            self._deadline = perf_counter() + self._get_next_timeout()
            self._cv.notify()

    def disable(self) -> None:
        """
        Disable the watchdog (no timeout will fire until re-enabled).
        """
        with self._cv:
            self._deadline = None
            self._cv.notify()

    def finish(self) -> None:
        """
        Permanently stop the watchdog thread and disarm the timer.
        After calling finish(), you cannot re-enable this watchdog.
        """
        with self._cv:
            self._stop = True
            self._cv.notify()
        self._worker_thread.join()

    def __enter__(self) -> "Watchdog":
        # If currently disabled, calling enable() will also reset the timer
        if self._deadline is None:
            self.enable()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        # End the watchdog on context exit
        self.finish()

    def watch_iter(self, iterable: Iterable[T]) -> Iterator[T]:
        """
        Wrap an iterable so that each 'next()' call is watched by the watchdog,
        but the time in between iterations is not watched. Usage:

            wd = Watchdog(timeout=3, enabled=False)
            for item in wd.watch_iter(generator()):
                # processing item not timed by the watchdog
                pass

        This pattern:
          - enable() -> sets/extends deadline
          - next(...) -> measured portion
          - disable() -> stops timer

        Args:
            iterable: The iterable to wrap and watch.

        Returns:
            An iterator that wraps the input iterable and watches for timeouts.
        """

        it = iter(iterable)
        while True:
            # Automatically resets timer
            self.enable()
            try:
                item = next(it)
            except StopIteration:
                self.disable()
                break
            except:
                # On any error, disable watchdog before re-raising
                self.disable()
                raise
            else:
                self.disable()
                yield item


def repr_short(obj: Any) -> str:
    """
    Return a short repr of an object.
    """
    if isinstance(obj, torch.Tensor):
        if isinstance(obj, ShardedTensorBase) or obj.is_cuda:
            return "<CUDA tensor>"

    s = repr(obj)
    if len(s) > PRINT_LOCAL_MAX_LENGTH:
        s = s[: PRINT_LOCAL_MAX_LENGTH // 2] + "..." + s[-PRINT_LOCAL_MAX_LENGTH // 2 :]
    return s


if __name__ == "__main__":
    # Example usage

    def my_callback() -> None:
        print("Watchdog timed out in callback.")
        # Demonstrate an error
        raise ValueError("Example error from callback.")

    print("Simple usage example:")
    wd = Watchdog(timeout=2, callback=my_callback, enabled=True)
    print("Sleeping 3s so the watchdog times out.")
    time.sleep(30)
    # Because we never reset or finish, the watchdog should fire and
    # forcibly exit, after printing the traceback and stack dumps.
    print("You won't see this line if the watchdog fired first.")
