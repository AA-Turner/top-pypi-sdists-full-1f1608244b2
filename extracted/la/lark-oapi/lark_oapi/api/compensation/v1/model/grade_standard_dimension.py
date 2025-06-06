# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class GradeStandardDimension(object):
    _types = {
        "api_name": str,
        "contain_sub": bool,
        "values": List[str],
    }

    def __init__(self, d=None):
        self.api_name: Optional[str] = None
        self.contain_sub: Optional[bool] = None
        self.values: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GradeStandardDimensionBuilder":
        return GradeStandardDimensionBuilder()


class GradeStandardDimensionBuilder(object):
    def __init__(self) -> None:
        self._grade_standard_dimension = GradeStandardDimension()

    def api_name(self, api_name: str) -> "GradeStandardDimensionBuilder":
        self._grade_standard_dimension.api_name = api_name
        return self

    def contain_sub(self, contain_sub: bool) -> "GradeStandardDimensionBuilder":
        self._grade_standard_dimension.contain_sub = contain_sub
        return self

    def values(self, values: List[str]) -> "GradeStandardDimensionBuilder":
        self._grade_standard_dimension.values = values
        return self

    def build(self) -> "GradeStandardDimension":
        return self._grade_standard_dimension
