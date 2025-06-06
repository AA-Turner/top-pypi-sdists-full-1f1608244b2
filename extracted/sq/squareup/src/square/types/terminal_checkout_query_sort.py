# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .sort_order import SortOrder
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TerminalCheckoutQuerySort(UncheckedBaseModel):
    sort_order: typing.Optional[SortOrder] = pydantic.Field(default=None)
    """
    The order in which results are listed.
    Default: `DESC`
    See [SortOrder](#type-sortorder) for possible values
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
