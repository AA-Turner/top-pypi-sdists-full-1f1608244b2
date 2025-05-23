"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class ScimPhotoType(str, Enum):
    PHOTO = "photo"
    THUMBNAIL = "thumbnail"


class ScimPhotoTypedDict(TypedDict):
    display: NotRequired[str]
    primary: NotRequired[bool]
    type: NotRequired[ScimPhotoType]
    value: NotRequired[str]


class ScimPhoto(BaseModel):
    display: Optional[str] = None

    primary: Optional[bool] = None

    type: Optional[ScimPhotoType] = None

    value: Optional[str] = None
