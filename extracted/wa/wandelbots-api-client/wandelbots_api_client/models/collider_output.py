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
from wandelbots_api_client.models.collider_output_shape import ColliderOutputShape
from wandelbots_api_client.models.pyjectory_datatypes_core_pose import PyjectoryDatatypesCorePose
from typing import Optional, Set
from typing_extensions import Self

class ColliderOutput(BaseModel):
    """
    Defines a collider with a single shape.  Pose describes where the shape of the collider is positioned. 
    """ # noqa: E501
    shape: ColliderOutputShape
    pose: PyjectoryDatatypesCorePose
    margin: Optional[Union[StrictFloat, StrictInt]] = Field(default=0, description="Increases the shape's size in all dimensions. Applied in [mm]. Can be used to keep a safe distance to the shape.")
    __properties: ClassVar[List[str]] = ["shape", "pose", "margin"]

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
        """Create an instance of ColliderOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of shape
        if self.shape:
            _dict['shape'] = self.shape.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pose
        if self.pose:
            _dict['pose'] = self.pose.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ColliderOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shape": ColliderOutputShape.from_dict(obj["shape"]) if obj.get("shape") is not None else None,
            "pose": PyjectoryDatatypesCorePose.from_dict(obj["pose"]) if obj.get("pose") is not None else None,
            "margin": obj.get("margin") if obj.get("margin") is not None else 0
        })
        return _obj


