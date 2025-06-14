# generated by datamodel-codegen:
#   filename:  entity/applications/liveExecutionContext.json
#   timestamp: 2025-06-12T10:55:12+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class JobRun(BaseModel):
    enabled: Annotated[
        Optional[bool], Field(False, description='If Live Execution is enabled')
    ]
    resources: Annotated[
        Optional[List[str]],
        Field(
            None,
            description='Resource full classname to register to extend any endpoints.',
        ),
    ]
