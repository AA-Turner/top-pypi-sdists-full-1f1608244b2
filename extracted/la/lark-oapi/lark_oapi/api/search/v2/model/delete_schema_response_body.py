# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteSchemaResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteSchemaResponseBodyBuilder":
        return DeleteSchemaResponseBodyBuilder()


class DeleteSchemaResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_schema_response_body = DeleteSchemaResponseBody()

    def build(self) -> "DeleteSchemaResponseBody":
        return self._delete_schema_response_body
