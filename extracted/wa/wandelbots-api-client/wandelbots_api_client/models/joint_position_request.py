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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from wandelbots_api_client.models.joints import Joints
from wandelbots_api_client.models.tcp_pose import TcpPose
from typing import Optional, Set
from typing_extensions import Self

class JointPositionRequest(BaseModel):
    """
    Request to find the joint positions the motion-group needs to apply for its TCP to be in a specified pose (Inverse Kinematic Solution).
    """ # noqa: E501
    motion_group: StrictStr = Field(description="Identifier of the motion group.")
    tcp_pose: TcpPose
    reference_joint_position: Joints
    __properties: ClassVar[List[str]] = ["motion_group", "tcp_pose", "reference_joint_position"]

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
        """Create an instance of JointPositionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tcp_pose
        if self.tcp_pose:
            _dict['tcp_pose'] = self.tcp_pose.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reference_joint_position
        if self.reference_joint_position:
            _dict['reference_joint_position'] = self.reference_joint_position.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JointPositionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "motion_group": obj.get("motion_group"),
            "tcp_pose": TcpPose.from_dict(obj["tcp_pose"]) if obj.get("tcp_pose") is not None else None,
            "reference_joint_position": Joints.from_dict(obj["reference_joint_position"]) if obj.get("reference_joint_position") is not None else None
        })
        return _obj


