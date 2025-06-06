# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .calendar_period import CalendarPeriod


class CalendarSuccessItem(object):
    _types = {
        "id": str,
        "periods": List[CalendarPeriod],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.periods: Optional[List[CalendarPeriod]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CalendarSuccessItemBuilder":
        return CalendarSuccessItemBuilder()


class CalendarSuccessItemBuilder(object):
    def __init__(self) -> None:
        self._calendar_success_item = CalendarSuccessItem()

    def id(self, id: str) -> "CalendarSuccessItemBuilder":
        self._calendar_success_item.id = id
        return self

    def periods(self, periods: List[CalendarPeriod]) -> "CalendarSuccessItemBuilder":
        self._calendar_success_item.periods = periods
        return self

    def build(self) -> "CalendarSuccessItem":
        return self._calendar_success_item
