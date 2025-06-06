# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteCalendarResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteCalendarResponseBodyBuilder":
        return DeleteCalendarResponseBodyBuilder()


class DeleteCalendarResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_calendar_response_body = DeleteCalendarResponseBody()

    def build(self) -> "DeleteCalendarResponseBody":
        return self._delete_calendar_response_body
