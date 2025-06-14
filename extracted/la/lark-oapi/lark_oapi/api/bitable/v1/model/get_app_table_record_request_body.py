# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class GetAppTableRecordRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetAppTableRecordRequestBodyBuilder":
        return GetAppTableRecordRequestBodyBuilder()


class GetAppTableRecordRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._get_app_table_record_request_body = GetAppTableRecordRequestBody()

    def build(self) -> "GetAppTableRecordRequestBody":
        return self._get_app_table_record_request_body
