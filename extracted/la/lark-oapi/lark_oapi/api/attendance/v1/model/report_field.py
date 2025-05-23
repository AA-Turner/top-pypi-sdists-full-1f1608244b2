# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n_resource import I18nResource


class ReportField(object):
    _types = {
        "code": str,
        "title": str,
        "is_calculable": bool,
        "field_id": str,
        "sub_fields": str,
        "i18n_name": List[I18nResource],
    }

    def __init__(self, d=None):
        self.code: Optional[str] = None
        self.title: Optional[str] = None
        self.is_calculable: Optional[bool] = None
        self.field_id: Optional[str] = None
        self.sub_fields: Optional[str] = None
        self.i18n_name: Optional[List[I18nResource]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReportFieldBuilder":
        return ReportFieldBuilder()


class ReportFieldBuilder(object):
    def __init__(self) -> None:
        self._report_field = ReportField()

    def code(self, code: str) -> "ReportFieldBuilder":
        self._report_field.code = code
        return self

    def title(self, title: str) -> "ReportFieldBuilder":
        self._report_field.title = title
        return self

    def is_calculable(self, is_calculable: bool) -> "ReportFieldBuilder":
        self._report_field.is_calculable = is_calculable
        return self

    def field_id(self, field_id: str) -> "ReportFieldBuilder":
        self._report_field.field_id = field_id
        return self

    def sub_fields(self, sub_fields: str) -> "ReportFieldBuilder":
        self._report_field.sub_fields = sub_fields
        return self

    def i18n_name(self, i18n_name: List[I18nResource]) -> "ReportFieldBuilder":
        self._report_field.i18n_name = i18n_name
        return self

    def build(self) -> "ReportField":
        return self._report_field
