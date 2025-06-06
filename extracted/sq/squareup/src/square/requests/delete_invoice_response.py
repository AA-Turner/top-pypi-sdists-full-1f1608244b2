# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams


class DeleteInvoiceResponseParams(typing_extensions.TypedDict):
    """
    Describes a `DeleteInvoice` response.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Information about errors encountered during the request.
    """
