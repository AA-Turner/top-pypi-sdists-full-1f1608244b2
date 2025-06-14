"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from orq_ai_sdk.types import BaseModel
from orq_ai_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    parse_datetime,
)
import pydantic
from typing import Any, Dict, List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class ListDatasetDatapointsRequestTypedDict(TypedDict):
    dataset_id: str
    limit: NotRequired[float]
    r"""A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10"""
    starting_after: NotRequired[str]
    r"""A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list."""
    ending_before: NotRequired[str]
    r"""A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list."""


class ListDatasetDatapointsRequest(BaseModel):
    dataset_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    limit: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10
    r"""A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10"""

    starting_after: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `after=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the next page of the list."""

    ending_before: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, starting with `01JJ1HDHN79XAS7A01WB3HYSDB`, your subsequent call can include `before=01JJ1HDHN79XAS7A01WB3HYSDB` in order to fetch the previous page of the list."""


ListDatasetDatapointsObject = Literal["list"]

ListDatasetDatapointsRole = Literal[
    "system",
    "assistant",
    "user",
    "exception",
    "tool",
    "prompt",
    "correction",
    "expected_output",
]
r"""The role of the prompt message"""

ListDatasetDatapoints2DatasetsResponseType = Literal["file"]
r"""The type of the content part. Always `file`."""


class ListDatasetDatapoints2FileTypedDict(TypedDict):
    file_data: str
    r"""The base64 encoded file data, used when passing the file to the model as a string."""
    filename: NotRequired[str]
    r"""The name of the file, used when passing the file to the model as a string."""


class ListDatasetDatapoints2File(BaseModel):
    file_data: str
    r"""The base64 encoded file data, used when passing the file to the model as a string."""

    filename: Optional[str] = None
    r"""The name of the file, used when passing the file to the model as a string."""


class ListDatasetDatapoints23TypedDict(TypedDict):
    type: ListDatasetDatapoints2DatasetsResponseType
    r"""The type of the content part. Always `file`."""
    file: ListDatasetDatapoints2FileTypedDict


class ListDatasetDatapoints23(BaseModel):
    type: ListDatasetDatapoints2DatasetsResponseType
    r"""The type of the content part. Always `file`."""

    file: ListDatasetDatapoints2File


ListDatasetDatapoints2DatasetsType = Literal["image_url"]


class ListDatasetDatapoints2ImageURLTypedDict(TypedDict):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""
    id: NotRequired[str]
    r"""The orq.ai id of the image"""
    detail: NotRequired[str]
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class ListDatasetDatapoints2ImageURL(BaseModel):
    url: str
    r"""Either a URL of the image or the base64 encoded data URI."""

    id: Optional[str] = None
    r"""The orq.ai id of the image"""

    detail: Optional[str] = None
    r"""Specifies the detail level of the image. Currently only supported with OpenAI models"""


class ListDatasetDatapoints22TypedDict(TypedDict):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: ListDatasetDatapoints2DatasetsType
    image_url: ListDatasetDatapoints2ImageURLTypedDict


class ListDatasetDatapoints22(BaseModel):
    r"""The image part of the prompt message. Only supported with vision models."""

    type: ListDatasetDatapoints2DatasetsType

    image_url: ListDatasetDatapoints2ImageURL


ListDatasetDatapoints2Type = Literal["text"]


class ListDatasetDatapoints21TypedDict(TypedDict):
    r"""Text content part of a prompt message"""

    type: ListDatasetDatapoints2Type
    text: str


class ListDatasetDatapoints21(BaseModel):
    r"""Text content part of a prompt message"""

    type: ListDatasetDatapoints2Type

    text: str


ListDatasetDatapointsContent2TypedDict = TypeAliasType(
    "ListDatasetDatapointsContent2TypedDict",
    Union[
        ListDatasetDatapoints21TypedDict,
        ListDatasetDatapoints22TypedDict,
        ListDatasetDatapoints23TypedDict,
    ],
)


ListDatasetDatapointsContent2 = TypeAliasType(
    "ListDatasetDatapointsContent2",
    Union[ListDatasetDatapoints21, ListDatasetDatapoints22, ListDatasetDatapoints23],
)


ListDatasetDatapointsContentTypedDict = TypeAliasType(
    "ListDatasetDatapointsContentTypedDict",
    Union[str, List[ListDatasetDatapointsContent2TypedDict]],
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


ListDatasetDatapointsContent = TypeAliasType(
    "ListDatasetDatapointsContent", Union[str, List[ListDatasetDatapointsContent2]]
)
r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""


ListDatasetDatapointsType = Literal["function"]


class ListDatasetDatapointsFunctionTypedDict(TypedDict):
    name: str
    arguments: str
    r"""JSON string arguments for the functions"""


class ListDatasetDatapointsFunction(BaseModel):
    name: str

    arguments: str
    r"""JSON string arguments for the functions"""


class ListDatasetDatapointsToolCallsTypedDict(TypedDict):
    type: ListDatasetDatapointsType
    function: ListDatasetDatapointsFunctionTypedDict
    id: NotRequired[str]
    index: NotRequired[float]


class ListDatasetDatapointsToolCalls(BaseModel):
    type: ListDatasetDatapointsType

    function: ListDatasetDatapointsFunction

    id: Optional[str] = None

    index: Optional[float] = None


class ListDatasetDatapointsMessagesTypedDict(TypedDict):
    role: ListDatasetDatapointsRole
    r"""The role of the prompt message"""
    content: ListDatasetDatapointsContentTypedDict
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""
    tool_calls: NotRequired[List[ListDatasetDatapointsToolCallsTypedDict]]
    tool_call_id: NotRequired[str]


class ListDatasetDatapointsMessages(BaseModel):
    role: ListDatasetDatapointsRole
    r"""The role of the prompt message"""

    content: ListDatasetDatapointsContent
    r"""The contents of the user message. Either the text content of the message or an array of content parts with a defined type, each can be of type `text` or `image_url` when passing in images. You can pass multiple images by adding multiple `image_url` content parts."""

    tool_calls: Optional[List[ListDatasetDatapointsToolCalls]] = None

    tool_call_id: Optional[str] = None


class ListDatasetDatapointsDataTypedDict(TypedDict):
    id: str
    r"""The unique identifier of the dataset item"""
    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""
    dataset_id: str
    r"""The unique identifier of the dataset"""
    inputs: NotRequired[Dict[str, Any]]
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""
    messages: NotRequired[List[ListDatasetDatapointsMessagesTypedDict]]
    r"""The prompt template messages"""
    expected_output: NotRequired[str]
    created_by_id: NotRequired[str]
    r"""The unique identifier of the user who created the dataset"""
    updated_by_id: NotRequired[str]
    r"""The unique identifier of the user who last updated the dataset"""
    created: NotRequired[datetime]
    r"""The date and time the resource was created"""
    updated: NotRequired[datetime]
    r"""The date and time the resource was last updated"""


class ListDatasetDatapointsData(BaseModel):
    id: Annotated[str, pydantic.Field(alias="_id")]
    r"""The unique identifier of the dataset item"""

    workspace_id: str
    r"""The unique identifier of the workspace it belongs to"""

    dataset_id: str
    r"""The unique identifier of the dataset"""

    inputs: Optional[Dict[str, Any]] = None
    r"""The inputs of the dataset. Key value pairs where the key is the input name and the value is the input value. Nested objects are not supported."""

    messages: Optional[List[ListDatasetDatapointsMessages]] = None
    r"""The prompt template messages"""

    expected_output: Optional[str] = None

    created_by_id: Optional[str] = None
    r"""The unique identifier of the user who created the dataset"""

    updated_by_id: Optional[str] = None
    r"""The unique identifier of the user who last updated the dataset"""

    created: Optional[datetime] = None
    r"""The date and time the resource was created"""

    updated: Optional[datetime] = parse_datetime("2025-06-12T09:58:41.410Z")
    r"""The date and time the resource was last updated"""


class ListDatasetDatapointsResponseBodyTypedDict(TypedDict):
    r"""Datapoints retrieved successfully. Returns a paginated list of datapoints."""

    object: ListDatasetDatapointsObject
    data: List[ListDatasetDatapointsDataTypedDict]
    has_more: bool


class ListDatasetDatapointsResponseBody(BaseModel):
    r"""Datapoints retrieved successfully. Returns a paginated list of datapoints."""

    object: ListDatasetDatapointsObject

    data: List[ListDatasetDatapointsData]

    has_more: bool
