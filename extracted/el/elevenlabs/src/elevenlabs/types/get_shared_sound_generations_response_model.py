# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .shared_sound_generation_response_model import SharedSoundGenerationResponseModel


class GetSharedSoundGenerationsResponseModel(UncheckedBaseModel):
    shared_sound_generations: typing.List[SharedSoundGenerationResponseModel]
    last_sort_id: typing.Optional[str] = None
    has_more: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
