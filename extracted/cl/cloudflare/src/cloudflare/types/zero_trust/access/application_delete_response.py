# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ApplicationDeleteResponse"]


class ApplicationDeleteResponse(BaseModel):
    id: Optional[str] = None
    """UUID."""
