# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CompleteTaskResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CompleteTaskResponseBodyBuilder":
        return CompleteTaskResponseBodyBuilder()


class CompleteTaskResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._complete_task_response_body = CompleteTaskResponseBody()

    def build(self) -> "CompleteTaskResponseBody":
        return self._complete_task_response_body
