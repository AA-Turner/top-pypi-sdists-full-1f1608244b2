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
import json
from enum import Enum
from typing_extensions import Self


class ThumbnailAlignmentEnum(str, Enum):
    """
    The alignment of the thumbnail image in the card. Only applicable if the card using horizontal orientation.
    """

    """
    allowed enum values
    """
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ThumbnailAlignmentEnum from a JSON string"""
        return cls(json.loads(json_str))


