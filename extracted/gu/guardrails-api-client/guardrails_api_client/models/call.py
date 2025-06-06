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
from guardrails_api_client.models.call_inputs import CallInputs
from guardrails_api_client.models.iteration import Iteration
from typing import Set
from typing_extensions import Self

class Call(BaseModel):
    """
    Call
    """ # noqa: E501
    id: str = Field(description="The unique identifier for this Call.  Can be used as an identifier for a specific execution of a Guard.")
    iterations: Optional[List[Iteration]] = None
    inputs: Optional[CallInputs] = None
    exception: Optional[str] = None
    __properties: ClassVar[List[str]] = ["id", "iterations", "inputs", "exception"]

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
        """Create an instance of Call from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in iterations (list)
        _items = []
        if self.iterations:
            for _item in self.iterations:
                if _item:
                    _items.append(_item.to_dict() if hasattr(_item, "to_dict") and callable(_item.to_dict) else _item)
            _dict['iterations'] = _items
        # override the default output from pydantic by calling `to_dict()` of inputs
        if self.inputs:
            _dict['inputs'] = self.inputs.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Call from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "iterations": [Iteration.from_dict(_item) for _item in obj["iterations"]] if obj.get("iterations") is not None else None,
            "inputs": CallInputs.from_dict(obj["inputs"]) if obj.get("inputs") is not None else None,
            "exception": obj.get("exception")
        })
        return _obj


