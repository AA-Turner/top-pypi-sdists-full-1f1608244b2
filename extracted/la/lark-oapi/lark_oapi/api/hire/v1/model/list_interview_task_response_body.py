# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .interview_task import InterviewTask


class ListInterviewTaskResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "items": List[InterviewTask],
    }

    def __init__(self, d=None):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.items: Optional[List[InterviewTask]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListInterviewTaskResponseBodyBuilder":
        return ListInterviewTaskResponseBodyBuilder()


class ListInterviewTaskResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_interview_task_response_body = ListInterviewTaskResponseBody()

    def has_more(self, has_more: bool) -> "ListInterviewTaskResponseBodyBuilder":
        self._list_interview_task_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListInterviewTaskResponseBodyBuilder":
        self._list_interview_task_response_body.page_token = page_token
        return self

    def items(self, items: List[InterviewTask]) -> "ListInterviewTaskResponseBodyBuilder":
        self._list_interview_task_response_body.items = items
        return self

    def build(self) -> "ListInterviewTaskResponseBody":
        return self._list_interview_task_response_body
