# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ListRegistrationSchemaRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListRegistrationSchemaRequestBodyBuilder":
        return ListRegistrationSchemaRequestBodyBuilder()


class ListRegistrationSchemaRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._list_registration_schema_request_body = ListRegistrationSchemaRequestBody()

    def build(self) -> "ListRegistrationSchemaRequestBody":
        return self._list_registration_schema_request_body
