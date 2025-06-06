# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Icon(object):
    _types = {
        "type": int,
        "key": str,
        "fs_unit": str,
    }

    def __init__(self, d=None):
        self.type: Optional[int] = None
        self.key: Optional[str] = None
        self.fs_unit: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "IconBuilder":
        return IconBuilder()


class IconBuilder(object):
    def __init__(self) -> None:
        self._icon = Icon()

    def type(self, type: int) -> "IconBuilder":
        self._icon.type = type
        return self

    def key(self, key: str) -> "IconBuilder":
        self._icon.key = key
        return self

    def fs_unit(self, fs_unit: str) -> "IconBuilder":
        self._icon.fs_unit = fs_unit
        return self

    def build(self) -> "Icon":
        return self._icon
