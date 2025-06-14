# generated by datamodel-codegen:
#   filename:  auth/loginRequest.json
#   timestamp: 2025-06-12T10:55:12+00:00

from __future__ import annotations

from pydantic import ConfigDict, Field
from typing_extensions import Annotated

from metadata.ingestion.models.custom_pydantic import BaseModel


class LoginRequest(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    email: Annotated[str, Field(description='Login Email')]
    password: Annotated[str, Field(description='Login Password in base64 format')]
