# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .money import MoneyParams


class OrderReturnLineItemModifierParams(typing_extensions.TypedDict):
    """
    A line item modifier being returned.
    """

    uid: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A unique ID that identifies the return modifier only within this order.
    """

    source_modifier_uid: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The modifier `uid` from the order's line item that contains the
    original sale of this line item modifier.
    """

    catalog_object_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The catalog object ID referencing [CatalogModifier](entity:CatalogModifier).
    """

    catalog_version: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The version of the catalog object that this line item modifier references.
    """

    name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The name of the item modifier.
    """

    base_price_money: typing_extensions.NotRequired[MoneyParams]
    """
    The base price for the modifier.
    
    `base_price_money` is required for ad hoc modifiers.
    If both `catalog_object_id` and `base_price_money` are set, `base_price_money` overrides the predefined [CatalogModifier](entity:CatalogModifier) price.
    """

    total_price_money: typing_extensions.NotRequired[MoneyParams]
    """
    The total price of the item modifier for its line item.
    This is the modifier's `base_price_money` multiplied by the line item's quantity.
    """

    quantity: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The quantity of the line item modifier. The modifier quantity can be 0 or more.
    For example, suppose a restaurant offers a cheeseburger on the menu. When a buyer orders
    this item, the restaurant records the purchase by creating an `Order` object with a line item
    for a burger. The line item includes a line item modifier: the name is cheese and the quantity
    is 1. The buyer has the option to order extra cheese (or no cheese). If the buyer chooses
    the extra cheese option, the modifier quantity increases to 2. If the buyer does not want
    any cheese, the modifier quantity is set to 0.
    """
