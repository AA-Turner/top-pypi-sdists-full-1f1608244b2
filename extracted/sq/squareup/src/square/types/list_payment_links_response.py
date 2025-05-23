# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .payment_link import PaymentLink
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ListPaymentLinksResponse(UncheckedBaseModel):
    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Errors that occurred during the request.
    """

    payment_links: typing.Optional[typing.List[PaymentLink]] = pydantic.Field(default=None)
    """
    The list of payment links.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
      When a response is truncated, it includes a cursor that you can use in a subsequent request
    to retrieve the next set of gift cards. If a cursor is not present, this is the final response.
    For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
