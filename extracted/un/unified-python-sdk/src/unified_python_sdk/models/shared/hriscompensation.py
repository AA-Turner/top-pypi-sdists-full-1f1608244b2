"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class HrisCompensationFrequency(str, Enum):
    ONE_TIME = "ONE_TIME"
    DAY = "DAY"
    QUARTER = "QUARTER"
    YEAR = "YEAR"
    HOUR = "HOUR"
    MONTH = "MONTH"
    WEEK = "WEEK"


class HrisCompensationType(str, Enum):
    SALARY = "SALARY"
    BONUS = "BONUS"
    STOCK_OPTIONS = "STOCK_OPTIONS"
    EQUITY = "EQUITY"
    OTHER = "OTHER"


class HrisCompensationTypedDict(TypedDict):
    amount: NotRequired[float]
    currency: NotRequired[str]
    frequency: NotRequired[HrisCompensationFrequency]
    type: NotRequired[HrisCompensationType]


class HrisCompensation(BaseModel):
    amount: Optional[float] = None

    currency: Optional[str] = None

    frequency: Optional[HrisCompensationFrequency] = None

    type: Optional[HrisCompensationType] = None
