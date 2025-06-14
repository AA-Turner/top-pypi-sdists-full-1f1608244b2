from enum import Enum
from functools import lru_cache
from typing import cast

from ..extensions import Enums


class AssayRunUpdatedFieldsWebhookV2Type(Enums.KnownString):
    V2_ASSAYRUNUPDATEDFIELDS = "v2.assayRun.updated.fields"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    @lru_cache(maxsize=None)
    def of_unknown(val: str) -> "AssayRunUpdatedFieldsWebhookV2Type":
        if not isinstance(val, str):
            raise ValueError(
                f"Value of AssayRunUpdatedFieldsWebhookV2Type must be a string (encountered: {val})"
            )
        newcls = Enum("AssayRunUpdatedFieldsWebhookV2Type", {"_UNKNOWN": val}, type=Enums.UnknownString)  # type: ignore
        return cast(AssayRunUpdatedFieldsWebhookV2Type, getattr(newcls, "_UNKNOWN"))
