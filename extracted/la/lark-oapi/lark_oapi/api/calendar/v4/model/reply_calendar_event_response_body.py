# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ReplyCalendarEventResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReplyCalendarEventResponseBodyBuilder":
        return ReplyCalendarEventResponseBodyBuilder()


class ReplyCalendarEventResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._reply_calendar_event_response_body = ReplyCalendarEventResponseBody()

    def build(self) -> "ReplyCalendarEventResponseBody":
        return self._reply_calendar_event_response_body
