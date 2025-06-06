# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteSpreadsheetSheetFilterViewConditionRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteSpreadsheetSheetFilterViewConditionRequestBodyBuilder":
        return DeleteSpreadsheetSheetFilterViewConditionRequestBodyBuilder()


class DeleteSpreadsheetSheetFilterViewConditionRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_spreadsheet_sheet_filter_view_condition_request_body = DeleteSpreadsheetSheetFilterViewConditionRequestBody()

    def build(self) -> "DeleteSpreadsheetSheetFilterViewConditionRequestBody":
        return self._delete_spreadsheet_sheet_filter_view_condition_request_body
