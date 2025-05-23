from enum import Enum
from functools import lru_cache
from typing import cast

from ..extensions import Enums


class StringSelectFormFieldType(Enums.KnownString):
    STRING_SELECTION = "STRING_SELECTION"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    @lru_cache(maxsize=None)
    def of_unknown(val: str) -> "StringSelectFormFieldType":
        if not isinstance(val, str):
            raise ValueError(f"Value of StringSelectFormFieldType must be a string (encountered: {val})")
        newcls = Enum("StringSelectFormFieldType", {"_UNKNOWN": val}, type=Enums.UnknownString)  # type: ignore
        return cast(StringSelectFormFieldType, getattr(newcls, "_UNKNOWN"))
