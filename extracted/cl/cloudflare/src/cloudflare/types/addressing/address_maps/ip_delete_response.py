# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["IPDeleteResponse", "Error", "ErrorSource", "Message", "MessageSource", "ResultInfo"]


class ErrorSource(BaseModel):
    pointer: Optional[str] = None


class Error(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[ErrorSource] = None


class MessageSource(BaseModel):
    pointer: Optional[str] = None


class Message(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[MessageSource] = None


class ResultInfo(BaseModel):
    count: Optional[float] = None
    """Total number of results for the requested service."""

    page: Optional[float] = None
    """Current page within paginated list of results."""

    per_page: Optional[float] = None
    """Number of results per page of results."""

    total_count: Optional[float] = None
    """Total results available without any search parameters."""


class IPDeleteResponse(BaseModel):
    errors: List[Error]

    messages: List[Message]

    success: Literal[True]
    """Whether the API call was successful."""

    result_info: Optional[ResultInfo] = None
