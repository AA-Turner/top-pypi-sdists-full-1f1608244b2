"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from unified_python_sdk.types import BaseModel


class PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserManagerType(
    str, Enum
):
    DIRECT = "direct"
    INDIRECT = "indirect"


class PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserManagerTypedDict(
    TypedDict
):
    r"""\"id\" attribute of another User."""

    dollar_ref: NotRequired[str]
    display_name: NotRequired[str]
    manager_id: NotRequired[str]
    type: NotRequired[
        PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserManagerType
    ]
    value: NotRequired[str]


class PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserManager(
    BaseModel
):
    r"""\"id\" attribute of another User."""

    dollar_ref: Annotated[Optional[str], pydantic.Field(alias="$ref")] = None

    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None

    manager_id: Annotated[Optional[str], pydantic.Field(alias="managerId")] = None

    type: Optional[
        PropertyScimUserUrnIetfParamsScimSchemasExtensionEnterprise20UserManagerType
    ] = None

    value: Optional[str] = None
