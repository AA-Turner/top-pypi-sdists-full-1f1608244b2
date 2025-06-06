# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteSpreadsheetSheetFilterViewResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteSpreadsheetSheetFilterViewResponseBodyBuilder":
        return DeleteSpreadsheetSheetFilterViewResponseBodyBuilder()


class DeleteSpreadsheetSheetFilterViewResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_spreadsheet_sheet_filter_view_response_body = DeleteSpreadsheetSheetFilterViewResponseBody()

    def build(self) -> "DeleteSpreadsheetSheetFilterViewResponseBody":
        return self._delete_spreadsheet_sheet_filter_view_response_body
