# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ListGroupRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListGroupRequestBodyBuilder":
        return ListGroupRequestBodyBuilder()


class ListGroupRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._list_group_request_body = ListGroupRequestBody()

    def build(self) -> "ListGroupRequestBody":
        return self._list_group_request_body
