# coding: utf-8

"""
    Wandelbots NOVA API

    Interact with robots in an easy and intuitive way.  > **Note:** API version 2 is experimental and will experience functional changes. 

    The version of the OpenAPI document: 2.0.0 beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from wandelbots_api_client.v2.models.collider import Collider
from wandelbots_api_client.v2.models.collision_motion_group import CollisionMotionGroup
from typing import Optional, Set
from typing_extensions import Self

class CollisionScene(BaseModel):
    """
    Defines the collision scene.  There are two types of objects in the scene: - `colliders`: Each collider is attached directly to the origin of the scene: Origin >> Collider - `motion-groups`: Each motion group is assigned a kinematic chain of links with a special collider, called tool, attached to the last element.   The motion group is attached to the origin of the scene via its mounting: Origin >> Mounting >> Motion Group Base >> […] 
    """ # noqa: E501
    colliders: Optional[Dict[str, Collider]] = Field(default=None, description="A collection of identifiable colliders.")
    motion_groups: Optional[Dict[str, CollisionMotionGroup]] = Field(default=None, description="Maps a Wandelbots NOVA motion group to its configuration in the collision scene. Key must be a motion group identifier.  Values are collision motion group objects.  A collision motion group defines a motion group in the collision scene.  The motion group is attached to the origin of the scene. To relocate the motion group, configure its mounting offset on the physical controller. This ensures that the definition of motion commands and collision scenes use the same coordinate system. The kinematic chain looks like this: - Origin >> Mounting >> Base >> Joint 0 >> Link 0 >> Joint 1 >> […] >> TCP  A `tool` is treated like another link attached to the end (flange) of the kinematic chain. All tool colliders are described in the flange frame. ")
    __properties: ClassVar[List[str]] = ["colliders", "motion_groups"]

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
        """Create an instance of CollisionScene from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in colliders (dict)
        _field_dict = {}
        if self.colliders:
            for _key in self.colliders:
                if self.colliders[_key]:
                    _field_dict[_key] = self.colliders[_key].to_dict()
            _dict['colliders'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in motion_groups (dict)
        _field_dict = {}
        if self.motion_groups:
            for _key in self.motion_groups:
                if self.motion_groups[_key]:
                    _field_dict[_key] = self.motion_groups[_key].to_dict()
            _dict['motion_groups'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CollisionScene from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "colliders": dict(
                (_k, Collider.from_dict(_v))
                for _k, _v in obj["colliders"].items()
            )
            if obj.get("colliders") is not None
            else None,
            "motion_groups": dict(
                (_k, CollisionMotionGroup.from_dict(_v))
                for _k, _v in obj["motion_groups"].items()
            )
            if obj.get("motion_groups") is not None
            else None
        })
        return _obj


