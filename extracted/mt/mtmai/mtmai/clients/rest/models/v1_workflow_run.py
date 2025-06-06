# coding: utf-8

"""
    Hatchet API

    The Hatchet API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mtmai.clients.rest.models.api_resource_meta import APIResourceMeta
from mtmai.clients.rest.models.v1_task_status import V1TaskStatus
from typing import Optional, Set
from typing_extensions import Self

class V1WorkflowRun(BaseModel):
    """
    V1WorkflowRun
    """ # noqa: E501
    metadata: APIResourceMeta
    status: V1TaskStatus
    started_at: Optional[datetime] = Field(default=None, description="The timestamp the task run started.", alias="startedAt")
    finished_at: Optional[datetime] = Field(default=None, description="The timestamp the task run finished.", alias="finishedAt")
    duration: Optional[StrictInt] = Field(default=None, description="The duration of the task run, in milliseconds.")
    tenant_id: Annotated[str, Field(min_length=36, strict=True, max_length=36)] = Field(description="The ID of the tenant.", alias="tenantId")
    additional_metadata: Optional[Dict[str, Any]] = Field(default=None, description="Additional metadata for the task run.", alias="additionalMetadata")
    display_name: StrictStr = Field(description="The display name of the task run.", alias="displayName")
    workflow_id: StrictStr = Field(alias="workflowId")
    output: Dict[str, Any] = Field(description="The output of the task run (for the latest run)")
    error_message: Optional[StrictStr] = Field(default=None, description="The error message of the task run (for the latest run)", alias="errorMessage")
    workflow_version_id: Optional[StrictStr] = Field(default=None, description="The ID of the workflow version.", alias="workflowVersionId")
    input: Dict[str, Any] = Field(description="The input of the task run.")
    created_at: Optional[datetime] = Field(default=None, description="The timestamp the task run was created.", alias="createdAt")
    parent_task_external_id: Optional[Annotated[str, Field(min_length=36, strict=True, max_length=36)]] = Field(default=None, alias="parentTaskExternalId")
    __properties: ClassVar[List[str]] = ["metadata", "status", "startedAt", "finishedAt", "duration", "tenantId", "additionalMetadata", "displayName", "workflowId", "output", "errorMessage", "workflowVersionId", "input", "createdAt", "parentTaskExternalId"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V1WorkflowRun from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1WorkflowRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in V1WorkflowRun) in the input: " + _key)

        _obj = cls.model_validate({
            "metadata": APIResourceMeta.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "status": obj.get("status"),
            "startedAt": obj.get("startedAt"),
            "finishedAt": obj.get("finishedAt"),
            "duration": obj.get("duration"),
            "tenantId": obj.get("tenantId"),
            "additionalMetadata": obj.get("additionalMetadata"),
            "displayName": obj.get("displayName"),
            "workflowId": obj.get("workflowId"),
            "output": obj.get("output"),
            "errorMessage": obj.get("errorMessage"),
            "workflowVersionId": obj.get("workflowVersionId"),
            "input": obj.get("input"),
            "createdAt": obj.get("createdAt"),
            "parentTaskExternalId": obj.get("parentTaskExternalId")
        })
        return _obj


