# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AddCustomFieldResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AddCustomFieldResponseBodyBuilder":
        return AddCustomFieldResponseBodyBuilder()


class AddCustomFieldResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._add_custom_field_response_body = AddCustomFieldResponseBody()

    def build(self) -> "AddCustomFieldResponseBody":
        return self._add_custom_field_response_body
