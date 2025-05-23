# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class QueryOperationLogsDepartmentRequestBody(object):
    _types = {
        "department_ids": List[str],
        "start_date": str,
        "end_date": str,
    }

    def __init__(self, d=None):
        self.department_ids: Optional[List[str]] = None
        self.start_date: Optional[str] = None
        self.end_date: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryOperationLogsDepartmentRequestBodyBuilder":
        return QueryOperationLogsDepartmentRequestBodyBuilder()


class QueryOperationLogsDepartmentRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._query_operation_logs_department_request_body = QueryOperationLogsDepartmentRequestBody()

    def department_ids(self, department_ids: List[str]) -> "QueryOperationLogsDepartmentRequestBodyBuilder":
        self._query_operation_logs_department_request_body.department_ids = department_ids
        return self

    def start_date(self, start_date: str) -> "QueryOperationLogsDepartmentRequestBodyBuilder":
        self._query_operation_logs_department_request_body.start_date = start_date
        return self

    def end_date(self, end_date: str) -> "QueryOperationLogsDepartmentRequestBodyBuilder":
        self._query_operation_logs_department_request_body.end_date = end_date
        return self

    def build(self) -> "QueryOperationLogsDepartmentRequestBody":
        return self._query_operation_logs_department_request_body
