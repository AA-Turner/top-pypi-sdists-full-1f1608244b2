# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .money import MoneyParams


class ProcessingFeeParams(typing_extensions.TypedDict):
    """
    Represents the Square processing fee.
    """

    effective_at: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The timestamp of when the fee takes effect, in RFC 3339 format.
    """

    type: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The type of fee assessed or adjusted. The fee type can be `INITIAL` or `ADJUSTMENT`.
    """

    amount_money: typing_extensions.NotRequired[MoneyParams]
    """
    The fee amount, which might be negative, that is assessed or adjusted by Square.
    
    Positive values represent funds being assessed, while negative values represent
    funds being returned.
    """
