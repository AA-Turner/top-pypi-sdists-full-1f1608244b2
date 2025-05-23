# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .payout import Payout
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ListPayoutsResponse(UncheckedBaseModel):
    """
    The response to retrieve payout records entries.
    """

    payouts: typing.Optional[typing.List[Payout]] = pydantic.Field(default=None)
    """
    The requested list of payouts.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to be used in a subsequent request. If empty, this is the final response.
    For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
