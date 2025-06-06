"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class ScimEmailType(str, Enum):
    WORK = "work"
    HOME = "home"
    OTHER = "other"


class ScimEmailTypedDict(TypedDict):
    type: ScimEmailType
    display: NotRequired[str]
    primary: NotRequired[bool]
    value: NotRequired[str]


class ScimEmail(BaseModel):
    type: ScimEmailType

    display: Optional[str] = None

    primary: Optional[bool] = None

    value: Optional[str] = None
