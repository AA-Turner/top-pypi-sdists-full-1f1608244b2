# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, StrictStr 
from lusid.models.data_scope import DataScope

class ReconciliationId(BaseModel):
    """
    ReconciliationId
    """
    scope: Optional[DataScope] = None
    identifier:  Optional[StrictStr] = Field(None,alias="identifier") 
    __properties = ["scope", "identifier"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ReconciliationId:
        """Create an instance of ReconciliationId from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of scope
        if self.scope:
            _dict['scope'] = self.scope.to_dict()
        # set to None if identifier (nullable) is None
        # and __fields_set__ contains the field
        if self.identifier is None and "identifier" in self.__fields_set__:
            _dict['identifier'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReconciliationId:
        """Create an instance of ReconciliationId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReconciliationId.parse_obj(obj)

        _obj = ReconciliationId.parse_obj({
            "scope": DataScope.from_dict(obj.get("scope")) if obj.get("scope") is not None else None,
            "identifier": obj.get("identifier")
        })
        return _obj
