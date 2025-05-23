"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class AccountingContactPaymentMethodType(str, Enum):
    ACH = "ACH"
    ALIPAY = "ALIPAY"
    CARD = "CARD"
    GIROPAY = "GIROPAY"
    IDEAL = "IDEAL"
    OTHER = "OTHER"
    PAYPAL = "PAYPAL"
    WIRE = "WIRE"
    CHECK = "CHECK"


class AccountingContactPaymentMethodTypedDict(TypedDict):
    type: AccountingContactPaymentMethodType
    default: NotRequired[bool]
    id: NotRequired[str]
    name: NotRequired[str]


class AccountingContactPaymentMethod(BaseModel):
    type: AccountingContactPaymentMethodType

    default: Optional[bool] = None

    id: Optional[str] = None

    name: Optional[str] = None
