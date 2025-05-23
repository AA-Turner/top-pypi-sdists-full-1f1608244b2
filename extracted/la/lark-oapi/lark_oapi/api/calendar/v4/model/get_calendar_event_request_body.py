# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class GetCalendarEventRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetCalendarEventRequestBodyBuilder":
        return GetCalendarEventRequestBodyBuilder()


class GetCalendarEventRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._get_calendar_event_request_body = GetCalendarEventRequestBody()

    def build(self) -> "GetCalendarEventRequestBody":
        return self._get_calendar_event_request_body
