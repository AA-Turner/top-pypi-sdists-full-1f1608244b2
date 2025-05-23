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


from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictFloat, StrictInt, conlist 

class FixedLegAllOfOverrides(BaseModel):
    """
    Any overriding data for notionals, spreads or rates that would affect generation of a leg.  This supports the case where an amortisation schedule is given but otherwise generation is allowed as usual.  # noqa: E501
    """
    amortization: Optional[conlist(Union[StrictFloat, StrictInt])] = Field(None, alias="Amortization")
    spreads: Optional[conlist(Union[StrictFloat, StrictInt])] = Field(None, alias="Spreads")
    additional_properties: Dict[str, Any] = {}
    __properties = ["Amortization", "Spreads"]

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
    def from_json(cls, json_str: str) -> FixedLegAllOfOverrides:
        """Create an instance of FixedLegAllOfOverrides from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FixedLegAllOfOverrides:
        """Create an instance of FixedLegAllOfOverrides from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FixedLegAllOfOverrides.parse_obj(obj)

        _obj = FixedLegAllOfOverrides.parse_obj({
            "amortization": obj.get("Amortization"),
            "spreads": obj.get("Spreads")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
