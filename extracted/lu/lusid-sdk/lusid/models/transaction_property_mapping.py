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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr 

class TransactionPropertyMapping(BaseModel):
    """
    TransactionPropertyMapping
    """
    property_key:  StrictStr = Field(...,alias="propertyKey", description="The key that uniquely identifies the property. It has the format {domain}/{scope}/{code}") 
    map_from:  Optional[StrictStr] = Field(None,alias="mapFrom", description="The Property Key of the Property to map from") 
    set_to: Optional[Any] = Field(None, alias="setTo", description="A pointer to the Property being mapped from")
    __properties = ["propertyKey", "mapFrom", "setTo"]

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
    def from_json(cls, json_str: str) -> TransactionPropertyMapping:
        """Create an instance of TransactionPropertyMapping from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if map_from (nullable) is None
        # and __fields_set__ contains the field
        if self.map_from is None and "map_from" in self.__fields_set__:
            _dict['mapFrom'] = None

        # set to None if set_to (nullable) is None
        # and __fields_set__ contains the field
        if self.set_to is None and "set_to" in self.__fields_set__:
            _dict['setTo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionPropertyMapping:
        """Create an instance of TransactionPropertyMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionPropertyMapping.parse_obj(obj)

        _obj = TransactionPropertyMapping.parse_obj({
            "property_key": obj.get("propertyKey"),
            "map_from": obj.get("mapFrom"),
            "set_to": obj.get("setTo")
        })
        return _obj
