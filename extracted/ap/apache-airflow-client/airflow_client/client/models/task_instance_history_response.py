# coding: utf-8

"""
    Airflow API

    Airflow API. All endpoints located under ``/api/v2`` can be used safely, are stable and backward compatible. Endpoints located under ``/ui`` are dedicated to the UI and are subject to breaking change depending on the need of the frontend. Users should not rely on those but use the public ones instead.

    The version of the OpenAPI document: 2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from airflow_client.client.models.dag_version_response import DagVersionResponse
from airflow_client.client.models.task_instance_state import TaskInstanceState
from typing import Optional, Set
from typing_extensions import Self

class TaskInstanceHistoryResponse(BaseModel):
    """
    TaskInstanceHistory serializer for responses.
    """ # noqa: E501
    dag_id: StrictStr
    dag_run_id: StrictStr
    dag_version: Optional[DagVersionResponse] = None
    duration: Optional[Union[StrictFloat, StrictInt]] = None
    end_date: Optional[datetime] = None
    executor: Optional[StrictStr] = None
    executor_config: StrictStr
    hostname: Optional[StrictStr] = None
    map_index: StrictInt
    max_tries: StrictInt
    operator: Optional[StrictStr] = None
    pid: Optional[StrictInt] = None
    pool: StrictStr
    pool_slots: StrictInt
    priority_weight: Optional[StrictInt] = None
    queue: Optional[StrictStr] = None
    queued_when: Optional[datetime] = None
    scheduled_when: Optional[datetime] = None
    start_date: Optional[datetime] = None
    state: Optional[TaskInstanceState] = None
    task_display_name: StrictStr
    task_id: StrictStr
    try_number: StrictInt
    unixname: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["dag_id", "dag_run_id", "dag_version", "duration", "end_date", "executor", "executor_config", "hostname", "map_index", "max_tries", "operator", "pid", "pool", "pool_slots", "priority_weight", "queue", "queued_when", "scheduled_when", "start_date", "state", "task_display_name", "task_id", "try_number", "unixname"]

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
        """Create an instance of TaskInstanceHistoryResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dag_version
        if self.dag_version:
            _dict['dag_version'] = self.dag_version.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TaskInstanceHistoryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dag_id": obj.get("dag_id"),
            "dag_run_id": obj.get("dag_run_id"),
            "dag_version": DagVersionResponse.from_dict(obj["dag_version"]) if obj.get("dag_version") is not None else None,
            "duration": obj.get("duration"),
            "end_date": obj.get("end_date"),
            "executor": obj.get("executor"),
            "executor_config": obj.get("executor_config"),
            "hostname": obj.get("hostname"),
            "map_index": obj.get("map_index"),
            "max_tries": obj.get("max_tries"),
            "operator": obj.get("operator"),
            "pid": obj.get("pid"),
            "pool": obj.get("pool"),
            "pool_slots": obj.get("pool_slots"),
            "priority_weight": obj.get("priority_weight"),
            "queue": obj.get("queue"),
            "queued_when": obj.get("queued_when"),
            "scheduled_when": obj.get("scheduled_when"),
            "start_date": obj.get("start_date"),
            "state": obj.get("state"),
            "task_display_name": obj.get("task_display_name"),
            "task_id": obj.get("task_id"),
            "try_number": obj.get("try_number"),
            "unixname": obj.get("unixname")
        })
        return _obj


