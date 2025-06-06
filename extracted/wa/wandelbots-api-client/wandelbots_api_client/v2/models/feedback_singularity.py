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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from wandelbots_api_client.v2.models.singularity_type_enum import SingularityTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class FeedbackSingularity(BaseModel):
    """
    A singularity is a point in the robot's workspace where the robot loses one or more degrees of freedom with regards to moving its TCP. This means the robot cannot move or rotate the TCP in a certain direction from this specific point.  Use PTP motions if possible. They will almost never fail due to singularities (only if the target point is at a singularity).  Alternatively change the robot TCP's path to avoid moving through this point or try to move the TCP through this point in a different direction. 
    """ # noqa: E501
    singularity_type: Optional[SingularityTypeEnum] = None
    singular_joint_position: Optional[List[Union[StrictFloat, StrictInt]]] = None
    error_feedback_name: StrictStr
    __properties: ClassVar[List[str]] = ["singularity_type", "singular_joint_position", "error_feedback_name"]

    @field_validator('error_feedback_name')
    def error_feedback_name_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['FeedbackSingularity']):
            raise ValueError("must be one of enum values ('FeedbackSingularity')")
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
        """Create an instance of FeedbackSingularity from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FeedbackSingularity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "singularity_type": obj.get("singularity_type"),
            "singular_joint_position": obj.get("singular_joint_position"),
            "error_feedback_name": obj.get("error_feedback_name")
        })
        return _obj


