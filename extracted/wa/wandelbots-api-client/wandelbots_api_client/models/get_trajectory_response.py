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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from wandelbots_api_client.models.trajectory_sample import TrajectorySample
from typing import Optional, Set
from typing_extensions import Self

class GetTrajectoryResponse(BaseModel):
    """
    GetTrajectoryResponse
    """ # noqa: E501
    trajectory: Optional[List[TrajectorySample]] = Field(default=None, description="A list of points representing the trajectory of a planned motion with defined `sample_time` in milliseconds (ms).")
    __properties: ClassVar[List[str]] = ["trajectory"]

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
        """Create an instance of GetTrajectoryResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in trajectory (list)
        _items = []
        if self.trajectory:
            for _item in self.trajectory:
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to not drop empty elements in lists
                if _item is not None:
                    _items.append(_item.to_dict())
                # <<< End modification
            _dict['trajectory'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetTrajectoryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "trajectory": [
                # >>> Modified from https://github.com/OpenAPITools/openapi-generator/blob/v7.6.0/modules/openapi-generator/src/main/resources/python/model_generic.mustache
                #     to allow dicts in lists
                TrajectorySample.from_dict(_item) if hasattr(TrajectorySample, 'from_dict') else _item
                # <<< End modification
                for _item in obj["trajectory"]
            ] if obj.get("trajectory") is not None else None
        })
        return _obj


