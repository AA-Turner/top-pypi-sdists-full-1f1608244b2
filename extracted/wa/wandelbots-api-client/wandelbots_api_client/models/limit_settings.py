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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from wandelbots_api_client.models.joint_limit import JointLimit
from wandelbots_api_client.models.single_joint_limit import SingleJointLimit
from typing import Optional, Set
from typing_extensions import Self

class LimitSettings(BaseModel):
    """
    NOTE: if a joint or Cartesian limit is not set or present for the corresponding device, then the value is not present (in the list or the optional value is null). The unit depends on the kind of axis (rotational or linear).
    """ # noqa: E501
    joint_position_limits: Optional[List[JointLimit]] = Field(default=None, description="Joint position limits in [rad or mm], configured in the safety setup, starting at base.")
    joint_velocity_limits: Optional[List[SingleJointLimit]] = Field(default=None, description="Max allowed velocity for joints in [rad/s or mm/s] of the safety setup, starting at base.")
    joint_acceleration_limits: Optional[List[SingleJointLimit]] = Field(default=None, description="Max allowed acceleration for joints in [rad/s^2 or mm/s^2] of the safety setup, starting at base.")
    joint_torque_limits: Optional[List[SingleJointLimit]] = Field(default=None, description="Max allowed torque for joints in [Nm or N] of the safety setup, starting at base.")
    tcp_velocity_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="[mm/s] max. allowed velocity at the TCP, 1-dimensional.")
    tcp_acceleration_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="[mm/s^2] max. allowed acceleration at the TCP, 1-dimensional.")
    tcp_orientation_velocity_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="[rad/s] max. allowed orientation velocity at the TCP, 1-dimensional.")
    tcp_orientation_acceleration_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="[rad/s^2] max. allowed orientation acceleration at the TCP, 1-dimensional.")
    tcp_force_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="[N] max. allowed force at the TCP, 1-dimensional.")
    elbow_velocity_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="[mm/s] max. allowed velocity at the elbow, 1-dimensional.")
    elbow_acceleration_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="[mm/s^2] max. allowed acceleration at the elbow, 1-dimensional.")
    elbow_force_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="[N] max. allowed force at the elbow, 1-dimensional.")
    __properties: ClassVar[List[str]] = ["joint_position_limits", "joint_velocity_limits", "joint_acceleration_limits", "joint_torque_limits", "tcp_velocity_limit", "tcp_acceleration_limit", "tcp_orientation_velocity_limit", "tcp_orientation_acceleration_limit", "tcp_force_limit", "elbow_velocity_limit", "elbow_acceleration_limit", "elbow_force_limit"]

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
        """Create an instance of LimitSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in joint_position_limits (list)
        _items = []
        if self.joint_position_limits:
            for _item in self.joint_position_limits:
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to not drop empty elements in lists
                if _item is not None:
                    _items.append(_item.to_dict())
                # <<< End modification
            _dict['joint_position_limits'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in joint_velocity_limits (list)
        _items = []
        if self.joint_velocity_limits:
            for _item in self.joint_velocity_limits:
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to not drop empty elements in lists
                if _item is not None:
                    _items.append(_item.to_dict())
                # <<< End modification
            _dict['joint_velocity_limits'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in joint_acceleration_limits (list)
        _items = []
        if self.joint_acceleration_limits:
            for _item in self.joint_acceleration_limits:
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to not drop empty elements in lists
                if _item is not None:
                    _items.append(_item.to_dict())
                # <<< End modification
            _dict['joint_acceleration_limits'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in joint_torque_limits (list)
        _items = []
        if self.joint_torque_limits:
            for _item in self.joint_torque_limits:
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to not drop empty elements in lists
                if _item is not None:
                    _items.append(_item.to_dict())
                # <<< End modification
            _dict['joint_torque_limits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LimitSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "joint_position_limits": [
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to allow dicts in lists
                JointLimit.from_dict(_item) if hasattr(JointLimit, 'from_dict') else _item
                # <<< End modification
                for _item in obj["joint_position_limits"]
            ] if obj.get("joint_position_limits") is not None else None,
            "joint_velocity_limits": [
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to allow dicts in lists
                SingleJointLimit.from_dict(_item) if hasattr(SingleJointLimit, 'from_dict') else _item
                # <<< End modification
                for _item in obj["joint_velocity_limits"]
            ] if obj.get("joint_velocity_limits") is not None else None,
            "joint_acceleration_limits": [
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to allow dicts in lists
                SingleJointLimit.from_dict(_item) if hasattr(SingleJointLimit, 'from_dict') else _item
                # <<< End modification
                for _item in obj["joint_acceleration_limits"]
            ] if obj.get("joint_acceleration_limits") is not None else None,
            "joint_torque_limits": [
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to allow dicts in lists
                SingleJointLimit.from_dict(_item) if hasattr(SingleJointLimit, 'from_dict') else _item
                # <<< End modification
                for _item in obj["joint_torque_limits"]
            ] if obj.get("joint_torque_limits") is not None else None,
            "tcp_velocity_limit": obj.get("tcp_velocity_limit"),
            "tcp_acceleration_limit": obj.get("tcp_acceleration_limit"),
            "tcp_orientation_velocity_limit": obj.get("tcp_orientation_velocity_limit"),
            "tcp_orientation_acceleration_limit": obj.get("tcp_orientation_acceleration_limit"),
            "tcp_force_limit": obj.get("tcp_force_limit"),
            "elbow_velocity_limit": obj.get("elbow_velocity_limit"),
            "elbow_acceleration_limit": obj.get("elbow_acceleration_limit"),
            "elbow_force_limit": obj.get("elbow_force_limit")
        })
        return _obj


