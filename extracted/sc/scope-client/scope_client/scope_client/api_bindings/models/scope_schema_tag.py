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


class ScopeSchemaTag(str, Enum):
    """
    ScopeSchemaTag
    """

    """
    allowed enum values
    """
    LLM_CONTEXT = 'llm_context'
    LLM_PROMPT = 'llm_prompt'
    LLM_RESPONSE = 'llm_response'
    PRIMARY_TIMESTAMP = 'primary_timestamp'
    CATEGORICAL = 'categorical'
    CONTINUOUS = 'continuous'
    PREDICTION = 'prediction'
    GROUND_TRUTH = 'ground_truth'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ScopeSchemaTag from a JSON string"""
        return cls(json.loads(json_str))


