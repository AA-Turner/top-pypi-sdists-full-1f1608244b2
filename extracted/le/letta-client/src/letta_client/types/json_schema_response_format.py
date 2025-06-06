# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class JsonSchemaResponseFormat(UncheckedBaseModel):
    """
    Response format for JSON schema-based responses.
    """

    type: typing.Literal["json_schema"] = "json_schema"
    json_schema: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    The JSON schema of the response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
