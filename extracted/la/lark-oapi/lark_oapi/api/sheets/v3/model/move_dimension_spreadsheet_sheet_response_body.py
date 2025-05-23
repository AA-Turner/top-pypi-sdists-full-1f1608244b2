# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class MoveDimensionSpreadsheetSheetResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MoveDimensionSpreadsheetSheetResponseBodyBuilder":
        return MoveDimensionSpreadsheetSheetResponseBodyBuilder()


class MoveDimensionSpreadsheetSheetResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._move_dimension_spreadsheet_sheet_response_body = MoveDimensionSpreadsheetSheetResponseBody()

    def build(self) -> "MoveDimensionSpreadsheetSheetResponseBody":
        return self._move_dimension_spreadsheet_sheet_response_body
