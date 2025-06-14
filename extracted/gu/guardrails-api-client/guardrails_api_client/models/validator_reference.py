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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional

from typing import Set
from typing_extensions import Self

class ValidatorReference(BaseModel):
    """
    ValidatorReference
    """ # noqa: E501
    id: Optional[str] = Field(description="The unique identifier for this Validator.  Often the hub id; e.g. guardrails/regex_match")
    on: Optional[str] = Field(default=None, description="A reference to the property this validator should be applied against.  Can be a valid JSON path or a meta-property such as \"prompt\" or \"output\"")
    on_fail: Optional[str] = Field(default=None, alias="onFail")
    args: Optional[List[object]] = None
    kwargs: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["args", "kwargs"]

    @field_validator('on_fail')
    def on_fail_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['exception', 'filter', 'fix', 'fix_reask', 'noop', 'reask', 'refrain', 'custom']):
            raise ValueError("must be one of enum values ('exception', 'filter', 'fix', 'fix_reask', 'noop', 'reask', 'refrain', 'custom')")
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
        """Create an instance of ValidatorReference from a JSON string"""
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
        """Create an instance of ValidatorReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            **obj,
"args": obj.get("args"),
        })
        return _obj


