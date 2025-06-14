# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ListInterviewRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListInterviewRequestBodyBuilder":
        return ListInterviewRequestBodyBuilder()


class ListInterviewRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._list_interview_request_body = ListInterviewRequestBody()

    def build(self) -> "ListInterviewRequestBody":
        return self._list_interview_request_body
