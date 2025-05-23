# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ListUserRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListUserRequestBodyBuilder":
        return ListUserRequestBodyBuilder()


class ListUserRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._list_user_request_body = ListUserRequestBody()

    def build(self) -> "ListUserRequestBody":
        return self._list_user_request_body
