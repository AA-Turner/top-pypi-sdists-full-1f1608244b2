# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ListCalendarAclRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListCalendarAclRequestBodyBuilder":
        return ListCalendarAclRequestBodyBuilder()


class ListCalendarAclRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._list_calendar_acl_request_body = ListCalendarAclRequestBody()

    def build(self) -> "ListCalendarAclRequestBody":
        return self._list_calendar_acl_request_body
