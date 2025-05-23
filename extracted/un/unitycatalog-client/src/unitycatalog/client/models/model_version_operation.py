# coding: utf-8

"""
    Unity Catalog API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ModelVersionOperation(str, Enum):
    """
    ModelVersionOperation
    """

    """
    allowed enum values
    """
    UNKNOWN_MODEL_VERSION_OPERATION = 'UNKNOWN_MODEL_VERSION_OPERATION'
    READ_MODEL_VERSION = 'READ_MODEL_VERSION'
    READ_WRITE_MODEL_VERSION = 'READ_WRITE_MODEL_VERSION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ModelVersionOperation from a JSON string"""
        return cls(json.loads(json_str))


