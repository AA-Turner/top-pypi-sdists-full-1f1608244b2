# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class I18nContent(object):
    _types = {
        "locale": str,
        "value": str,
        "id": str,
    }

    def __init__(self, d=None):
        self.locale: Optional[str] = None
        self.value: Optional[str] = None
        self.id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "I18nContentBuilder":
        return I18nContentBuilder()


class I18nContentBuilder(object):
    def __init__(self) -> None:
        self._i18n_content = I18nContent()

    def locale(self, locale: str) -> "I18nContentBuilder":
        self._i18n_content.locale = locale
        return self

    def value(self, value: str) -> "I18nContentBuilder":
        self._i18n_content.value = value
        return self

    def id(self, id: str) -> "I18nContentBuilder":
        self._i18n_content.id = id
        return self

    def build(self) -> "I18nContent":
        return self._i18n_content
