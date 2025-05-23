# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .card import CardParams


class ListCardsResponseParams(typing_extensions.TypedDict):
    """
    Defines the fields that are included in the response body of
    a request to the [ListCards](api-endpoint:Cards-ListCards) endpoint.

    Note: if there are errors processing the request, the card field will not be
    present.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Information on errors encountered during the request.
    """

    cards: typing_extensions.NotRequired[typing.Sequence[CardParams]]
    """
    The requested list of `Card`s.
    """

    cursor: typing_extensions.NotRequired[str]
    """
    The pagination cursor to be used in a subsequent request. If empty,
    this is the final response.
    
    See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information.
    """
