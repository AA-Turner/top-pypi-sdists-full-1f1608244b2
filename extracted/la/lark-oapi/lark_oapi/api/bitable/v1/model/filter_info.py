# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .condition import Condition
from .children_filter import ChildrenFilter


class FilterInfo(object):
    _types = {
        "conjunction": str,
        "conditions": List[Condition],
        "children": List[ChildrenFilter],
    }

    def __init__(self, d=None):
        self.conjunction: Optional[str] = None
        self.conditions: Optional[List[Condition]] = None
        self.children: Optional[List[ChildrenFilter]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FilterInfoBuilder":
        return FilterInfoBuilder()


class FilterInfoBuilder(object):
    def __init__(self) -> None:
        self._filter_info = FilterInfo()

    def conjunction(self, conjunction: str) -> "FilterInfoBuilder":
        self._filter_info.conjunction = conjunction
        return self

    def conditions(self, conditions: List[Condition]) -> "FilterInfoBuilder":
        self._filter_info.conditions = conditions
        return self

    def children(self, children: List[ChildrenFilter]) -> "FilterInfoBuilder":
        self._filter_info.children = children
        return self

    def build(self) -> "FilterInfo":
        return self._filter_info
