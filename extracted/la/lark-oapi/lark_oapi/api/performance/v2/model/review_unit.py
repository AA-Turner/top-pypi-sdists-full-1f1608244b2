# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .review_detail import ReviewDetail


class ReviewUnit(object):
    _types = {
        "unit_id": str,
        "is_unknown": bool,
        "data": List[ReviewDetail],
    }

    def __init__(self, d=None):
        self.unit_id: Optional[str] = None
        self.is_unknown: Optional[bool] = None
        self.data: Optional[List[ReviewDetail]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReviewUnitBuilder":
        return ReviewUnitBuilder()


class ReviewUnitBuilder(object):
    def __init__(self) -> None:
        self._review_unit = ReviewUnit()

    def unit_id(self, unit_id: str) -> "ReviewUnitBuilder":
        self._review_unit.unit_id = unit_id
        return self

    def is_unknown(self, is_unknown: bool) -> "ReviewUnitBuilder":
        self._review_unit.is_unknown = is_unknown
        return self

    def data(self, data: List[ReviewDetail]) -> "ReviewUnitBuilder":
        self._review_unit.data = data
        return self

    def build(self) -> "ReviewUnit":
        return self._review_unit
