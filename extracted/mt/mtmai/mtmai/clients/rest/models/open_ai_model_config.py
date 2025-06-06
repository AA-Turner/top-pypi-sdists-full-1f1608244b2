# coding: utf-8

"""
    Mtmai API

    The Mtmai API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from mtmai.clients.rest.models.model_info import ModelInfo
from typing import Optional, Set
from typing_extensions import Self

class OpenAIModelConfig(BaseModel):
    """
    OpenAIModelConfig
    """ # noqa: E501
    model: StrictStr
    model_type: StrictStr
    api_key: Optional[StrictStr] = None
    base_url: Optional[StrictStr] = None
    timeout: Optional[Union[StrictFloat, StrictInt]] = None
    max_retries: Optional[StrictInt] = None
    frequency_penalty: Optional[Union[StrictFloat, StrictInt]] = None
    logit_bias: Optional[StrictInt] = None
    max_tokens: Optional[StrictInt] = None
    n: Optional[StrictInt] = None
    presence_penalty: Optional[Union[StrictFloat, StrictInt]] = None
    response_format: Optional[StrictStr] = None
    seed: Optional[StrictInt] = None
    stop: Optional[List[StrictStr]] = None
    temperature: Optional[Union[StrictFloat, StrictInt]] = None
    top_p: Optional[Union[StrictFloat, StrictInt]] = None
    user: Optional[StrictStr] = None
    organization: Optional[StrictStr] = None
    default_headers: Optional[Dict[str, StrictStr]] = None
    model_info: Optional[ModelInfo] = None
    __properties: ClassVar[List[str]] = ["model", "model_type", "api_key", "base_url", "timeout", "max_retries", "frequency_penalty", "logit_bias", "max_tokens", "n", "presence_penalty", "response_format", "seed", "stop", "temperature", "top_p", "user", "organization", "default_headers", "model_info"]

    @field_validator('model_type')
    def model_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['OpenAIChatCompletionClient']):
            raise ValueError("must be one of enum values ('OpenAIChatCompletionClient')")
        return value

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
        """Create an instance of OpenAIModelConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of model_info
        if self.model_info:
            _dict['model_info'] = self.model_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OpenAIModelConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in OpenAIModelConfig) in the input: " + _key)

        _obj = cls.model_validate({
            "model": obj.get("model"),
            "model_type": obj.get("model_type"),
            "api_key": obj.get("api_key"),
            "base_url": obj.get("base_url"),
            "timeout": obj.get("timeout"),
            "max_retries": obj.get("max_retries"),
            "frequency_penalty": obj.get("frequency_penalty"),
            "logit_bias": obj.get("logit_bias"),
            "max_tokens": obj.get("max_tokens"),
            "n": obj.get("n"),
            "presence_penalty": obj.get("presence_penalty"),
            "response_format": obj.get("response_format"),
            "seed": obj.get("seed"),
            "stop": obj.get("stop"),
            "temperature": obj.get("temperature"),
            "top_p": obj.get("top_p"),
            "user": obj.get("user"),
            "organization": obj.get("organization"),
            "default_headers": obj.get("default_headers"),
            "model_info": ModelInfo.from_dict(obj["model_info"]) if obj.get("model_info") is not None else None
        })
        return _obj


