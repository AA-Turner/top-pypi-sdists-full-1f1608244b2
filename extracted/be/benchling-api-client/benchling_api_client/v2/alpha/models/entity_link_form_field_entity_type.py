from enum import Enum
from functools import lru_cache
from typing import cast

from ..extensions import Enums


class EntityLinkFormFieldEntityType(Enums.KnownString):
    CUSTOM_ENTITY = "custom_entity"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    @lru_cache(maxsize=None)
    def of_unknown(val: str) -> "EntityLinkFormFieldEntityType":
        if not isinstance(val, str):
            raise ValueError(f"Value of EntityLinkFormFieldEntityType must be a string (encountered: {val})")
        newcls = Enum("EntityLinkFormFieldEntityType", {"_UNKNOWN": val}, type=Enums.UnknownString)  # type: ignore
        return cast(EntityLinkFormFieldEntityType, getattr(newcls, "_UNKNOWN"))
