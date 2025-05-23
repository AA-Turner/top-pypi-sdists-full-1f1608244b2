# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .money import Money
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GiftCardActivityRefund(UncheckedBaseModel):
    """
    Represents details about a `REFUND` [gift card activity type](entity:GiftCardActivityType).
    """

    redeem_activity_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the refunded `REDEEM` gift card activity. Square populates this field if the 
    `payment_id` in the corresponding [RefundPayment](api-endpoint:Refunds-RefundPayment) request 
    represents a gift card redemption.
    
    For applications that use a custom payment processing system, this field is required when creating
    a `REFUND` activity. The provided `REDEEM` activity ID must be linked to the same gift card.
    """

    amount_money: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The amount added to the gift card for the refund. This value is a positive integer.
    
    This field is required when creating a `REFUND` activity. The amount can represent a full or partial refund.
    """

    reference_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A client-specified ID that associates the gift card activity with an entity in another system.
    """

    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the refunded payment. Square populates this field if the refund is for a 
    payment processed by Square. This field matches the `payment_id` in the corresponding
    [RefundPayment](api-endpoint:Refunds-RefundPayment) request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
