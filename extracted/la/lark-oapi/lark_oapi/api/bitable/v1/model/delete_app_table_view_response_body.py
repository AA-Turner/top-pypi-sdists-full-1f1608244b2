# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteAppTableViewResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteAppTableViewResponseBodyBuilder":
        return DeleteAppTableViewResponseBodyBuilder()


class DeleteAppTableViewResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_app_table_view_response_body = DeleteAppTableViewResponseBody()

    def build(self) -> "DeleteAppTableViewResponseBody":
        return self._delete_app_table_view_response_body
