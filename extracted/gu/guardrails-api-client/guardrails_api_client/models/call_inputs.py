# coding: utf-8

"""
    Guardrails API

    Guardrails CRUD API

    The version of the OpenAPI document: 0.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional

from typing import Set
from typing_extensions import Self

class CallInputs(BaseModel):
    """
    CallInputs
    """ # noqa: E501
    llm_api: Optional[str] = Field(default=None, description="The LLM resource targeted by the user. e.g. openai.chat.completions.create", alias="llmApi")
    llm_output: Optional[str] = Field(default=None, description="The string output from an external LLM call provided by the user via Guard.parse.", alias="llmOutput")
    instructions: Optional[str] = Field(default=None, description="The instructions for chat models.")
    prompt: Optional[str] = Field(default=None, description="The prompt for the LLM.")
    msg_history: Optional[List[Dict[str, Any]]] = Field(default=None, description="The message history for chat models.", alias="msgHistory")
    prompt_params: Optional[Dict[str, Any]] = Field(default=None, description="Parameters to be formatted into the prompt.", alias="promptParams")
    num_reasks: Optional[int] = Field(default=None, description="The total number of times the LLM can be called to correct output excluding the initial call.", alias="numReasks")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Additional data to be used by Validators during execution time.")
    full_schema_reask: Optional[bool] = Field(default=None, description="Whether to perform reasks for the entire schema rather than for individual fields.", alias="fullSchemaReask")
    stream: Optional[bool] = Field(default=None, description="Whether to use streaming.")
    args: Optional[List[object]] = None
    kwargs: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["llmApi", "llmOutput", "instructions", "prompt", "msgHistory", "promptParams", "numReasks", "metadata", "fullSchemaReask", "stream", "args", "kwargs"]

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
        """Create an instance of CallInputs from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in args (list)
        _items = []
        if self.args:
            for _item in self.args:
                if _item:
                    _items.append(_item.to_dict() if hasattr(_item, "to_dict") and callable(_item.to_dict) else _item)
            _dict['args'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallInputs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
			"promptParams": obj.get("promptParams"),
			"metadata": obj.get("metadata"),
			"kwargs": obj.get("kwargs"),
            "llmApi": obj.get("llmApi"),
            "llmOutput": obj.get("llmOutput"),
            "instructions": obj.get("instructions"),
            "prompt": obj.get("prompt"),
            "msgHistory": obj.get("msgHistory"),
            "numReasks": obj.get("numReasks"),
            "fullSchemaReask": obj.get("fullSchemaReask"),
            "stream": obj.get("stream"),
            "args": obj.get("args"),
        })
        return _obj


