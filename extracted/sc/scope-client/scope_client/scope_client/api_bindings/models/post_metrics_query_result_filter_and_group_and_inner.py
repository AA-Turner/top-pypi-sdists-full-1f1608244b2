# coding: utf-8

"""
    Arthur Scope

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from scope_client.api_bindings.models.post_metrics_query_result_filter import PostMetricsQueryResultFilter
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

POSTMETRICSQUERYRESULTFILTERANDGROUPANDINNER_ANY_OF_SCHEMAS = ["PostMetricsQueryResultFilter", "PostMetricsQueryResultFilterAndGroup", "PostMetricsQueryResultFilterOrGroup"]

class PostMetricsQueryResultFilterAndGroupAndInner(BaseModel):
    """
    PostMetricsQueryResultFilterAndGroupAndInner
    """

    # data type: PostMetricsQueryResultFilterAndGroup
    anyof_schema_1_validator: Optional[PostMetricsQueryResultFilterAndGroup] = None
    # data type: PostMetricsQueryResultFilterOrGroup
    anyof_schema_2_validator: Optional[PostMetricsQueryResultFilterOrGroup] = None
    # data type: PostMetricsQueryResultFilter
    anyof_schema_3_validator: Optional[PostMetricsQueryResultFilter] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[PostMetricsQueryResultFilter, PostMetricsQueryResultFilterAndGroup, PostMetricsQueryResultFilterOrGroup]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "PostMetricsQueryResultFilter", "PostMetricsQueryResultFilterAndGroup", "PostMetricsQueryResultFilterOrGroup" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = PostMetricsQueryResultFilterAndGroupAndInner.model_construct()
        error_messages = []
        # validate data type: PostMetricsQueryResultFilterAndGroup
        if not isinstance(v, PostMetricsQueryResultFilterAndGroup):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PostMetricsQueryResultFilterAndGroup`")
        else:
            return v

        # validate data type: PostMetricsQueryResultFilterOrGroup
        if not isinstance(v, PostMetricsQueryResultFilterOrGroup):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PostMetricsQueryResultFilterOrGroup`")
        else:
            return v

        # validate data type: PostMetricsQueryResultFilter
        if not isinstance(v, PostMetricsQueryResultFilter):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PostMetricsQueryResultFilter`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in PostMetricsQueryResultFilterAndGroupAndInner with anyOf schemas: PostMetricsQueryResultFilter, PostMetricsQueryResultFilterAndGroup, PostMetricsQueryResultFilterOrGroup. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[PostMetricsQueryResultFilterAndGroup] = None
        try:
            instance.actual_instance = PostMetricsQueryResultFilterAndGroup.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[PostMetricsQueryResultFilterOrGroup] = None
        try:
            instance.actual_instance = PostMetricsQueryResultFilterOrGroup.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[PostMetricsQueryResultFilter] = None
        try:
            instance.actual_instance = PostMetricsQueryResultFilter.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into PostMetricsQueryResultFilterAndGroupAndInner with anyOf schemas: PostMetricsQueryResultFilter, PostMetricsQueryResultFilterAndGroup, PostMetricsQueryResultFilterOrGroup. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], PostMetricsQueryResultFilter, PostMetricsQueryResultFilterAndGroup, PostMetricsQueryResultFilterOrGroup]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

from scope_client.api_bindings.models.post_metrics_query_result_filter_and_group import PostMetricsQueryResultFilterAndGroup
from scope_client.api_bindings.models.post_metrics_query_result_filter_or_group import PostMetricsQueryResultFilterOrGroup
# TODO: Rewrite to not use raise_errors
PostMetricsQueryResultFilterAndGroupAndInner.model_rebuild(raise_errors=False)

