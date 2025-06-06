# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from ..types.inventory_state import InventoryState


class InventoryCountParams(typing_extensions.TypedDict):
    """
    Represents Square-estimated quantity of items in a particular state at a
    particular seller location based on the known history of physical counts and
    inventory adjustments.
    """

    catalog_object_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The Square-generated ID of the
    [CatalogObject](entity:CatalogObject) being tracked.
    """

    catalog_object_type: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The [type](entity:CatalogObjectType) of the [CatalogObject](entity:CatalogObject) being tracked. 
    
    The Inventory API supports setting and reading the `"catalog_object_type": "ITEM_VARIATION"` field value. 
    In addition, it can also read the `"catalog_object_type": "ITEM"` field value that is set by the Square Restaurants app.
    """

    state: typing_extensions.NotRequired[InventoryState]
    """
    The current [inventory state](entity:InventoryState) for the related
    quantity of items.
    See [InventoryState](#type-inventorystate) for possible values
    """

    location_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The Square-generated ID of the [Location](entity:Location) where the related
    quantity of items is being tracked.
    """

    quantity: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The number of items affected by the estimated count as a decimal string.
    Can support up to 5 digits after the decimal point.
    """

    calculated_at: typing_extensions.NotRequired[str]
    """
    An RFC 3339-formatted timestamp that indicates when the most recent physical count or adjustment affecting
    the estimated count is received.
    """

    is_estimated: typing_extensions.NotRequired[bool]
    """
    Whether the inventory count is for composed variation (TRUE) or not (FALSE). If true, the inventory count will not be present in the response of
    any of these endpoints: [BatchChangeInventory](api-endpoint:Inventory-BatchChangeInventory),
    [BatchRetrieveInventoryChanges](api-endpoint:Inventory-BatchRetrieveInventoryChanges),
    [BatchRetrieveInventoryCounts](api-endpoint:Inventory-BatchRetrieveInventoryCounts), and
    [RetrieveInventoryChanges](api-endpoint:Inventory-RetrieveInventoryChanges).
    """
