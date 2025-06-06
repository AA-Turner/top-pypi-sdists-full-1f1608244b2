"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Fulcrum(str, Enum):
    FULCRUM = 'fulcrum'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFulcrum:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API key to use. Find it at https://web.fulcrumapp.com/settings/api"""
    SOURCE_TYPE: Final[Fulcrum] = dataclasses.field(default=Fulcrum.FULCRUM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

