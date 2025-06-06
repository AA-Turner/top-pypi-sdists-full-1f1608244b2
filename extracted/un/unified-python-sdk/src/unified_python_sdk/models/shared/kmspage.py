"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .kmspagemetadata import KmsPageMetadata, KmsPageMetadataTypedDict
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class KmsPageType(str, Enum):
    HTML = "HTML"
    MARKDOWN = "MARKDOWN"
    TEXT = "TEXT"
    OTHER = "OTHER"


class KmsPageTypedDict(TypedDict):
    title: str
    type: KmsPageType
    created_at: NotRequired[datetime]
    download_url: NotRequired[str]
    has_children: NotRequired[bool]
    id: NotRequired[str]
    is_active: NotRequired[bool]
    metadata: NotRequired[List[KmsPageMetadataTypedDict]]
    parent_page_id: NotRequired[str]
    raw: NotRequired[Dict[str, Any]]
    space_id: NotRequired[str]
    updated_at: NotRequired[datetime]
    user_id: NotRequired[str]
    web_url: NotRequired[str]


class KmsPage(BaseModel):
    title: str

    type: KmsPageType

    created_at: Optional[datetime] = None

    download_url: Optional[str] = None

    has_children: Optional[bool] = None

    id: Optional[str] = None

    is_active: Optional[bool] = None

    metadata: Optional[List[KmsPageMetadata]] = None

    parent_page_id: Optional[str] = None

    raw: Optional[Dict[str, Any]] = None

    space_id: Optional[str] = None

    updated_at: Optional[datetime] = None

    user_id: Optional[str] = None

    web_url: Optional[str] = None
