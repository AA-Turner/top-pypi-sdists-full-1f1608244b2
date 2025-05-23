# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class I18nResource(object):
    _types = {
        "text": str,
        "local": str,
        "is_default": bool,
    }

    def __init__(self, d=None):
        self.text: Optional[str] = None
        self.local: Optional[str] = None
        self.is_default: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "I18nResourceBuilder":
        return I18nResourceBuilder()


class I18nResourceBuilder(object):
    def __init__(self) -> None:
        self._i18n_resource = I18nResource()

    def text(self, text: str) -> "I18nResourceBuilder":
        self._i18n_resource.text = text
        return self

    def local(self, local: str) -> "I18nResourceBuilder":
        self._i18n_resource.local = local
        return self

    def is_default(self, is_default: bool) -> "I18nResourceBuilder":
        self._i18n_resource.is_default = is_default
        return self

    def build(self) -> "I18nResource":
        return self._i18n_resource
