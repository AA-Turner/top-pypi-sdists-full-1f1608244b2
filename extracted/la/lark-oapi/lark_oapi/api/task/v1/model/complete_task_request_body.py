# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CompleteTaskRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CompleteTaskRequestBodyBuilder":
        return CompleteTaskRequestBodyBuilder()


class CompleteTaskRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._complete_task_request_body = CompleteTaskRequestBody()

    def build(self) -> "CompleteTaskRequestBody":
        return self._complete_task_request_body
