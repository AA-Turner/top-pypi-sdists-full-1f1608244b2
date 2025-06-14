# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .field_permission_deserializer import FieldPermissionDeserializer
from .model_permission_deserializer import ModelPermissionDeserializer


class IndividualCommonModelScopeDeserializer(UncheckedBaseModel):
    model_name: str
    model_permissions: typing.Optional[typing.Dict[str, ModelPermissionDeserializer]] = None
    field_permissions: typing.Optional[FieldPermissionDeserializer] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
