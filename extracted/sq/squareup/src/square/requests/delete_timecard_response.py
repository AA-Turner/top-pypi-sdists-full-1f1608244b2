# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams


class DeleteTimecardResponseParams(typing_extensions.TypedDict):
    """
    The response to a request to delete a `Timecard`. The response might contain a set of
    `Error` objects if the request resulted in errors.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """
