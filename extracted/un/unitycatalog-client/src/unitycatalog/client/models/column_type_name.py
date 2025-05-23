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


class ColumnTypeName(str, Enum):
    """
    Name of type (INT, STRUCT, MAP, etc.).
    """

    """
    allowed enum values
    """
    BOOLEAN = 'BOOLEAN'
    BYTE = 'BYTE'
    SHORT = 'SHORT'
    INT = 'INT'
    LONG = 'LONG'
    FLOAT = 'FLOAT'
    DOUBLE = 'DOUBLE'
    DATE = 'DATE'
    TIMESTAMP = 'TIMESTAMP'
    TIMESTAMP_NTZ = 'TIMESTAMP_NTZ'
    STRING = 'STRING'
    BINARY = 'BINARY'
    DECIMAL = 'DECIMAL'
    INTERVAL = 'INTERVAL'
    ARRAY = 'ARRAY'
    STRUCT = 'STRUCT'
    MAP = 'MAP'
    CHAR = 'CHAR'
    NULL = 'NULL'
    USER_DEFINED_TYPE = 'USER_DEFINED_TYPE'
    TABLE_TYPE = 'TABLE_TYPE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ColumnTypeName from a JSON string"""
        return cls(json.loads(json_str))


