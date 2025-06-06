# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CreateCalendarEventMeetingMinuteRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateCalendarEventMeetingMinuteRequestBodyBuilder":
        return CreateCalendarEventMeetingMinuteRequestBodyBuilder()


class CreateCalendarEventMeetingMinuteRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_calendar_event_meeting_minute_request_body = CreateCalendarEventMeetingMinuteRequestBody()

    def build(self) -> "CreateCalendarEventMeetingMinuteRequestBody":
        return self._create_calendar_event_meeting_minute_request_body
