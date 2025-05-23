# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .money import Money
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class OrderLineItemAppliedServiceCharge(UncheckedBaseModel):
    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID that identifies the applied service charge only within this order.
    """

    service_charge_uid: str = pydantic.Field()
    """
    The `uid` of the service charge that the applied service charge represents. It must
    reference a service charge present in the `order.service_charges` field.
    
    This field is immutable. To change which service charges apply to a line item,
    delete and add a new `OrderLineItemAppliedServiceCharge`.
    """

    applied_money: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The amount of money applied by the service charge to the line item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
