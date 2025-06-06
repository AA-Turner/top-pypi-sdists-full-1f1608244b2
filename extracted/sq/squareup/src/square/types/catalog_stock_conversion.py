# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class CatalogStockConversion(UncheckedBaseModel):
    """
    Represents the rule of conversion between a stockable [CatalogItemVariation](entity:CatalogItemVariation)
    and a non-stockable sell-by or receive-by `CatalogItemVariation` that
    share the same underlying stock.
    """

    stockable_item_variation_id: str = pydantic.Field()
    """
    References to the stockable [CatalogItemVariation](entity:CatalogItemVariation)
    for this stock conversion. Selling, receiving or recounting the non-stockable `CatalogItemVariation`
    defined with a stock conversion results in adjustments of this stockable `CatalogItemVariation`.
    This immutable field must reference a stockable `CatalogItemVariation`
    that shares the parent [CatalogItem](entity:CatalogItem) of the converted `CatalogItemVariation.`
    """

    stockable_quantity: str = pydantic.Field()
    """
    The quantity of the stockable item variation (as identified by `stockable_item_variation_id`)
    equivalent to the non-stockable item variation quantity (as specified in `nonstockable_quantity`)
    as defined by this stock conversion.  It accepts a decimal number in a string format that can take
    up to 10 digits before the decimal point and up to 5 digits after the decimal point.
    """

    nonstockable_quantity: str = pydantic.Field()
    """
    The converted equivalent quantity of the non-stockable [CatalogItemVariation](entity:CatalogItemVariation)
    in its measurement unit. The `stockable_quantity` value and this `nonstockable_quantity` value together
    define the conversion ratio between stockable item variation and the non-stockable item variation.
    It accepts a decimal number in a string format that can take up to 10 digits before the decimal point
    and up to 5 digits after the decimal point.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
