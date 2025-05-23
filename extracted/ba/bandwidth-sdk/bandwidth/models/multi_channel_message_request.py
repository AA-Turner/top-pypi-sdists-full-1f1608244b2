# coding: utf-8

"""
    Bandwidth

    Bandwidth's Communication APIs

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from bandwidth.models.multi_channel_channel_list_object import MultiChannelChannelListObject
from bandwidth.models.priority_enum import PriorityEnum
from typing import Optional, Set
from typing_extensions import Self

class MultiChannelMessageRequest(BaseModel):
    """
    Multi-Channel Message Request
    """ # noqa: E501
    to: StrictStr = Field(description="The phone number the message should be sent to in E164 format.")
    channel_list: Annotated[List[MultiChannelChannelListObject], Field(max_length=4)] = Field(description="A list of message bodies. The messages will be attempted in the order they are listed. Once a message sends successfully, the others will be ignored.", alias="channelList")
    tag: Optional[StrictStr] = Field(default=None, description="A custom string that will be included in callback events of the message. Max 1024 characters.")
    priority: Optional[PriorityEnum] = None
    expiration: Optional[datetime] = Field(default=None, description="A string with the date/time value that the message will automatically expire by. This must be a valid RFC-3339 value, e.g., 2021-03-14T01:59:26Z or 2021-03-13T20:59:26-05:00. Must be a date-time in the future.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["to", "channelList", "tag", "priority", "expiration"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MultiChannelMessageRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in channel_list (list)
        _items = []
        if self.channel_list:
            for _item_channel_list in self.channel_list:
                if _item_channel_list:
                    _items.append(_item_channel_list.to_dict())
            _dict['channelList'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MultiChannelMessageRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "to": obj.get("to"),
            "channelList": [MultiChannelChannelListObject.from_dict(_item) for _item in obj["channelList"]] if obj.get("channelList") is not None else None,
            "tag": obj.get("tag"),
            "priority": obj.get("priority"),
            "expiration": obj.get("expiration")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


