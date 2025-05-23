# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .archive_item import ArchiveItem
from .archive_indicator import ArchiveIndicator


class ArchiveDetail(object):
    _types = {
        "user_id": str,
        "id": str,
        "tid": str,
        "plan_id": str,
        "plan_tid": str,
        "currency_id": str,
        "change_reason_id": str,
        "change_description": str,
        "effective_date": str,
        "expiration_date": str,
        "salary_level_id": str,
        "created_time": str,
        "updated_time": str,
        "archive_items": List[ArchiveItem],
        "archive_indicators": List[ArchiveIndicator],
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.id: Optional[str] = None
        self.tid: Optional[str] = None
        self.plan_id: Optional[str] = None
        self.plan_tid: Optional[str] = None
        self.currency_id: Optional[str] = None
        self.change_reason_id: Optional[str] = None
        self.change_description: Optional[str] = None
        self.effective_date: Optional[str] = None
        self.expiration_date: Optional[str] = None
        self.salary_level_id: Optional[str] = None
        self.created_time: Optional[str] = None
        self.updated_time: Optional[str] = None
        self.archive_items: Optional[List[ArchiveItem]] = None
        self.archive_indicators: Optional[List[ArchiveIndicator]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ArchiveDetailBuilder":
        return ArchiveDetailBuilder()


class ArchiveDetailBuilder(object):
    def __init__(self) -> None:
        self._archive_detail = ArchiveDetail()

    def user_id(self, user_id: str) -> "ArchiveDetailBuilder":
        self._archive_detail.user_id = user_id
        return self

    def id(self, id: str) -> "ArchiveDetailBuilder":
        self._archive_detail.id = id
        return self

    def tid(self, tid: str) -> "ArchiveDetailBuilder":
        self._archive_detail.tid = tid
        return self

    def plan_id(self, plan_id: str) -> "ArchiveDetailBuilder":
        self._archive_detail.plan_id = plan_id
        return self

    def plan_tid(self, plan_tid: str) -> "ArchiveDetailBuilder":
        self._archive_detail.plan_tid = plan_tid
        return self

    def currency_id(self, currency_id: str) -> "ArchiveDetailBuilder":
        self._archive_detail.currency_id = currency_id
        return self

    def change_reason_id(self, change_reason_id: str) -> "ArchiveDetailBuilder":
        self._archive_detail.change_reason_id = change_reason_id
        return self

    def change_description(self, change_description: str) -> "ArchiveDetailBuilder":
        self._archive_detail.change_description = change_description
        return self

    def effective_date(self, effective_date: str) -> "ArchiveDetailBuilder":
        self._archive_detail.effective_date = effective_date
        return self

    def expiration_date(self, expiration_date: str) -> "ArchiveDetailBuilder":
        self._archive_detail.expiration_date = expiration_date
        return self

    def salary_level_id(self, salary_level_id: str) -> "ArchiveDetailBuilder":
        self._archive_detail.salary_level_id = salary_level_id
        return self

    def created_time(self, created_time: str) -> "ArchiveDetailBuilder":
        self._archive_detail.created_time = created_time
        return self

    def updated_time(self, updated_time: str) -> "ArchiveDetailBuilder":
        self._archive_detail.updated_time = updated_time
        return self

    def archive_items(self, archive_items: List[ArchiveItem]) -> "ArchiveDetailBuilder":
        self._archive_detail.archive_items = archive_items
        return self

    def archive_indicators(self, archive_indicators: List[ArchiveIndicator]) -> "ArchiveDetailBuilder":
        self._archive_detail.archive_indicators = archive_indicators
        return self

    def build(self) -> "ArchiveDetail":
        return self._archive_detail
