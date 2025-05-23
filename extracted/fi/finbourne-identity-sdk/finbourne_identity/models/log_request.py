# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, conlist 
from finbourne_identity.models.log_ip_chain_entry import LogIpChainEntry

class LogRequest(BaseModel):
    """
    Represents a LogRequest resource in the Okta API  # noqa: E501
    """
    ip_chain: Optional[conlist(LogIpChainEntry)] = Field(None, alias="ipChain")
    __properties = ["ipChain"]

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
    def from_json(cls, json_str: str) -> LogRequest:
        """Create an instance of LogRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in ip_chain (list)
        _items = []
        if self.ip_chain:
            for _item in self.ip_chain:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ipChain'] = _items
        # set to None if ip_chain (nullable) is None
        # and __fields_set__ contains the field
        if self.ip_chain is None and "ip_chain" in self.__fields_set__:
            _dict['ipChain'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LogRequest:
        """Create an instance of LogRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LogRequest.parse_obj(obj)

        _obj = LogRequest.parse_obj({
            "ip_chain": [LogIpChainEntry.from_dict(_item) for _item in obj.get("ipChain")] if obj.get("ipChain") is not None else None
        })
        return _obj
