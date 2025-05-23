# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ListShiftRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListShiftRequestBodyBuilder":
        return ListShiftRequestBodyBuilder()


class ListShiftRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._list_shift_request_body = ListShiftRequestBody()

    def build(self) -> "ListShiftRequestBody":
        return self._list_shift_request_body
