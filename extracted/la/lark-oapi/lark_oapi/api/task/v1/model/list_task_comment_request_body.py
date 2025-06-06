# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ListTaskCommentRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListTaskCommentRequestBodyBuilder":
        return ListTaskCommentRequestBodyBuilder()


class ListTaskCommentRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._list_task_comment_request_body = ListTaskCommentRequestBody()

    def build(self) -> "ListTaskCommentRequestBody":
        return self._list_task_comment_request_body
