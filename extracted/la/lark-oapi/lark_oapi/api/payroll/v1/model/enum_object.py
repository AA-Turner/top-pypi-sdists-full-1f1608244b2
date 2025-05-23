# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class EnumObject(object):
    _types = {
        "enum_value_id": str,
        "enum_key": str,
    }

    def __init__(self, d=None):
        self.enum_value_id: Optional[str] = None
        self.enum_key: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EnumObjectBuilder":
        return EnumObjectBuilder()


class EnumObjectBuilder(object):
    def __init__(self) -> None:
        self._enum_object = EnumObject()

    def enum_value_id(self, enum_value_id: str) -> "EnumObjectBuilder":
        self._enum_object.enum_value_id = enum_value_id
        return self

    def enum_key(self, enum_key: str) -> "EnumObjectBuilder":
        self._enum_object.enum_key = enum_key
        return self

    def build(self) -> "EnumObject":
        return self._enum_object
