# generated by datamodel-codegen:
#   filename:  entity/feed/assets.json
#   timestamp: 2025-06-03T15:26:31+00:00

from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict

from metadata.ingestion.models.custom_pydantic import BaseModel

from ...type import entityReferenceList


class AssetsFeedInfo(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    updatedAssets: Optional[entityReferenceList.EntityReferenceList] = None
