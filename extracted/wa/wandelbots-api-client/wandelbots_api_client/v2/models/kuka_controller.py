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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from wandelbots_api_client.v2.models.kuka_controller_rsi_server import KukaControllerRsiServer
from typing import Optional, Set
from typing_extensions import Self

class KukaController(BaseModel):
    """
    The configuration of a physical KUKA robot controller has to contain an IP address. Additionally an RSI server configuration has to be specified in order to control the robot. Deploying the server is a functionality of this API. 
    """ # noqa: E501
    kind: Optional[StrictStr] = 'KukaController'
    controller_ip: StrictStr
    controller_port: StrictInt
    rsi_server: KukaControllerRsiServer
    __properties: ClassVar[List[str]] = ["kind", "controller_ip", "controller_port", "rsi_server"]

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['KukaController']):
            raise ValueError("must be one of enum values ('KukaController')")
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
        """Create an instance of KukaController from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rsi_server
        if self.rsi_server:
            _dict['rsi_server'] = self.rsi_server.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KukaController from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "kind": obj.get("kind") if obj.get("kind") is not None else 'KukaController',
            "controller_ip": obj.get("controller_ip"),
            "controller_port": obj.get("controller_port") if obj.get("controller_port") is not None else 54600,
            "rsi_server": KukaControllerRsiServer.from_dict(obj["rsi_server"]) if obj.get("rsi_server") is not None else None
        })
        return _obj


