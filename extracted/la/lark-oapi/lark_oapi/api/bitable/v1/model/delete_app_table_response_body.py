# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteAppTableResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteAppTableResponseBodyBuilder":
        return DeleteAppTableResponseBodyBuilder()


class DeleteAppTableResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_app_table_response_body = DeleteAppTableResponseBody()

    def build(self) -> "DeleteAppTableResponseBody":
        return self._delete_app_table_response_body
