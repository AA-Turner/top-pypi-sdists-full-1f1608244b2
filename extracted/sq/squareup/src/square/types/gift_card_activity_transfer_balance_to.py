# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
from .money import Money
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class GiftCardActivityTransferBalanceTo(UncheckedBaseModel):
    """
    Represents details about a `TRANSFER_BALANCE_TO` [gift card activity type](entity:GiftCardActivityType).
    """

    transfer_from_gift_card_id: str = pydantic.Field()
    """
    The ID of the gift card from which the specified amount was transferred.
    """

    amount_money: Money = pydantic.Field()
    """
    The amount added to the gift card balance for the transfer. This value is a positive integer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
