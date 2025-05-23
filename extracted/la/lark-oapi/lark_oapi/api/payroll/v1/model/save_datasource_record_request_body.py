# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .datasource_record import DatasourceRecord


class SaveDatasourceRecordRequestBody(object):
    _types = {
        "source_code": str,
        "records": List[DatasourceRecord],
    }

    def __init__(self, d=None):
        self.source_code: Optional[str] = None
        self.records: Optional[List[DatasourceRecord]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SaveDatasourceRecordRequestBodyBuilder":
        return SaveDatasourceRecordRequestBodyBuilder()


class SaveDatasourceRecordRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._save_datasource_record_request_body = SaveDatasourceRecordRequestBody()

    def source_code(self, source_code: str) -> "SaveDatasourceRecordRequestBodyBuilder":
        self._save_datasource_record_request_body.source_code = source_code
        return self

    def records(self, records: List[DatasourceRecord]) -> "SaveDatasourceRecordRequestBodyBuilder":
        self._save_datasource_record_request_body.records = records
        return self

    def build(self) -> "SaveDatasourceRecordRequestBody":
        return self._save_datasource_record_request_body
