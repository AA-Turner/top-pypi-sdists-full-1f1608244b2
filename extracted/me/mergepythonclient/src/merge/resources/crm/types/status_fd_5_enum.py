# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StatusFd5Enum(str, enum.Enum):
    """
    * `SYNCING` - SYNCING
    * `DONE` - DONE
    * `FAILED` - FAILED
    * `DISABLED` - DISABLED
    * `PAUSED` - PAUSED
    * `PARTIALLY_SYNCED` - PARTIALLY_SYNCED
    """

    SYNCING = "SYNCING"
    DONE = "DONE"
    FAILED = "FAILED"
    DISABLED = "DISABLED"
    PAUSED = "PAUSED"
    PARTIALLY_SYNCED = "PARTIALLY_SYNCED"

    def visit(
        self,
        syncing: typing.Callable[[], T_Result],
        done: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
        partially_synced: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StatusFd5Enum.SYNCING:
            return syncing()
        if self is StatusFd5Enum.DONE:
            return done()
        if self is StatusFd5Enum.FAILED:
            return failed()
        if self is StatusFd5Enum.DISABLED:
            return disabled()
        if self is StatusFd5Enum.PAUSED:
            return paused()
        if self is StatusFd5Enum.PARTIALLY_SYNCED:
            return partially_synced()
