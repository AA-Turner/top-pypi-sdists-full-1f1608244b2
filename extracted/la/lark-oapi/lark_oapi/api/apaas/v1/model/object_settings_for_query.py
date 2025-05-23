# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ObjectSettingsForQuery(object):
    _types = {
        "display_name": str,
        "allow_search_fields": List[str],
        "search_layouts": List[str],
    }

    def __init__(self, d=None):
        self.display_name: Optional[str] = None
        self.allow_search_fields: Optional[List[str]] = None
        self.search_layouts: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ObjectSettingsForQueryBuilder":
        return ObjectSettingsForQueryBuilder()


class ObjectSettingsForQueryBuilder(object):
    def __init__(self) -> None:
        self._object_settings_for_query = ObjectSettingsForQuery()

    def display_name(self, display_name: str) -> "ObjectSettingsForQueryBuilder":
        self._object_settings_for_query.display_name = display_name
        return self

    def allow_search_fields(self, allow_search_fields: List[str]) -> "ObjectSettingsForQueryBuilder":
        self._object_settings_for_query.allow_search_fields = allow_search_fields
        return self

    def search_layouts(self, search_layouts: List[str]) -> "ObjectSettingsForQueryBuilder":
        self._object_settings_for_query.search_layouts = search_layouts
        return self

    def build(self) -> "ObjectSettingsForQuery":
        return self._object_settings_for_query
