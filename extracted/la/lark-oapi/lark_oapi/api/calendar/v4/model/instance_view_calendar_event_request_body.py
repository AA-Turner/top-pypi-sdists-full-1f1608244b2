# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class InstanceViewCalendarEventRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InstanceViewCalendarEventRequestBodyBuilder":
        return InstanceViewCalendarEventRequestBodyBuilder()


class InstanceViewCalendarEventRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._instance_view_calendar_event_request_body = InstanceViewCalendarEventRequestBody()

    def build(self) -> "InstanceViewCalendarEventRequestBody":
        return self._instance_view_calendar_event_request_body
