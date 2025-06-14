# coding: utf-8

"""
    Wandelbots NOVA API

    Interact with robots in an easy and intuitive way. 

    The version of the OpenAPI document: 1.0.0 beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from wandelbots_api_client.models.pose2 import Pose2
from typing import Optional, Set
from typing_extensions import Self

class PathCircle(BaseModel):
    """
    A circular constructs a circle in translative space from 1) the start position which is provided via position, and 2) the indicated target position. The orientation is calculated via a [bezier spline](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) from start orientation to the indicated target orientation. The via point defines the control point for the bezier spline. Therefore, the control point will not be hit directly. 
    """ # noqa: E501
    via_pose: Pose2
    target_pose: Pose2
    path_definition_name: StrictStr
    __properties: ClassVar[List[str]] = ["via_pose", "target_pose", "path_definition_name"]

    @field_validator('path_definition_name')
    def path_definition_name_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PathCircle']):
            raise ValueError("must be one of enum values ('PathCircle')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True, exclude_none=True))

    def to_json(self) -> str:
        """
        Returns the JSON representation of the model using alias
        
        Do not use pydantic v2 .model_dump_json(by_alias=True, exclude_unset=True) here!
        It is unable to resolve nested types generated by openapi-generator.
        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PathCircle from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of via_pose
        if self.via_pose:
            _dict['via_pose'] = self.via_pose.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_pose
        if self.target_pose:
            _dict['target_pose'] = self.target_pose.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PathCircle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "via_pose": Pose2.from_dict(obj["via_pose"]) if obj.get("via_pose") is not None else None,
            "target_pose": Pose2.from_dict(obj["target_pose"]) if obj.get("target_pose") is not None else None,
            "path_definition_name": obj.get("path_definition_name")
        })
        return _obj


