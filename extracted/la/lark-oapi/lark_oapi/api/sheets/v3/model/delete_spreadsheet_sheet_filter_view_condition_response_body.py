# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteSpreadsheetSheetFilterViewConditionResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteSpreadsheetSheetFilterViewConditionResponseBodyBuilder":
        return DeleteSpreadsheetSheetFilterViewConditionResponseBodyBuilder()


class DeleteSpreadsheetSheetFilterViewConditionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_spreadsheet_sheet_filter_view_condition_response_body = DeleteSpreadsheetSheetFilterViewConditionResponseBody()

    def build(self) -> "DeleteSpreadsheetSheetFilterViewConditionResponseBody":
        return self._delete_spreadsheet_sheet_filter_view_condition_response_body
