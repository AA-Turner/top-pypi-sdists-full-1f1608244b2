# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class OrderEntry(UncheckedBaseModel):
    """
    A lightweight description of an [order](entity:Order) that is returned when
    `returned_entries` is `true` on a [SearchOrdersRequest](api-endpoint:Orders-SearchOrders).
    """

    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the order.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version number, which is incremented each time an update is committed to the order.
    Orders that were not created through the API do not include a version number and
    therefore cannot be updated.
    
    [Read more about working with versions.](https://developer.squareup.com/docs/orders-api/manage-orders/update-orders)
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location ID the order belongs to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
