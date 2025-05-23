# coding: utf-8

"""
    Arthur Scope

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ModelProblemType(str, Enum):
    """
    ModelProblemType
    """

    """
    allowed enum values
    """
    REGRESSION = 'regression'
    BINARY_CLASSIFICATION = 'binary_classification'
    ARTHUR_SHIELD = 'arthur_shield'
    CUSTOM = 'custom'
    MULTICLASS_CLASSIFICATION = 'multiclass_classification'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ModelProblemType from a JSON string"""
        return cls(json.loads(json_str))


