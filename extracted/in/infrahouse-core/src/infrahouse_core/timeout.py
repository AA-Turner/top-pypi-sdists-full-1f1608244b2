"""
InfraHouse timeout module.
"""

import signal
from contextlib import contextmanager


@contextmanager
def timeout(seconds: int):
    """
    Timeout context manager.

    :param seconds: Max execution time in seconds.
    :type seconds: int
    :raise TimeoutError: when the code under a ``with`` is running
        more than ``seconds``.
    """

    def handler(signum, frame):
        """
        Signal handler for SIGALRM.

        :param signum: The signal number sent by the OS.
        :type signum: int
        :param frame: The frame object from the signal handler.
        :type frame: frame

        :raise TimeoutError: when the signal is received.
        """
        if signum or frame:
            pass
        raise TimeoutError(f"Executing timed out after {seconds} seconds")

    original_handler = signal.signal(signal.SIGALRM, handler)
    try:
        signal.alarm(seconds)
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, original_handler)
