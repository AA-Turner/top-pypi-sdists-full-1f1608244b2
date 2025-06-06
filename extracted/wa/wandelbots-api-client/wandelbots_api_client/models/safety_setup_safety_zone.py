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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from wandelbots_api_client.models.geometry import Geometry
from typing import Optional, Set
from typing_extensions import Self

class SafetySetupSafetyZone(BaseModel):
    """
    Describes the physical space in which the safety limitations will be applied.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier.")
    priority: Optional[StrictInt] = Field(default=None, description="The precedence if two zones overlap.")
    geometry: Optional[Geometry] = None
    motion_group_uid: Optional[StrictInt] = Field(default=None, description="Unique identifier of an specific motion-group if the safety zone only applies to it. If it is not set, then the safety zone applies to all motion-groups.")
    __properties: ClassVar[List[str]] = ["id", "priority", "geometry", "motion_group_uid"]

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
        """Create an instance of SafetySetupSafetyZone from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of geometry
        if self.geometry:
            _dict['geometry'] = self.geometry.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SafetySetupSafetyZone from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "priority": obj.get("priority"),
            "geometry": Geometry.from_dict(obj["geometry"]) if obj.get("geometry") is not None else None,
            "motion_group_uid": obj.get("motion_group_uid")
        })
        return _obj


