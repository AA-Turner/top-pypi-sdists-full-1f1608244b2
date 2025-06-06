# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class GetTaskRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetTaskRequestBodyBuilder":
        return GetTaskRequestBodyBuilder()


class GetTaskRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._get_task_request_body = GetTaskRequestBody()

    def build(self) -> "GetTaskRequestBody":
        return self._get_task_request_body
