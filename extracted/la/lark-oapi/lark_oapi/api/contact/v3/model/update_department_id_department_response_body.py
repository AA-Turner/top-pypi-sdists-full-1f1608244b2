# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class UpdateDepartmentIdDepartmentResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateDepartmentIdDepartmentResponseBodyBuilder":
        return UpdateDepartmentIdDepartmentResponseBodyBuilder()


class UpdateDepartmentIdDepartmentResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_department_id_department_response_body = UpdateDepartmentIdDepartmentResponseBody()

    def build(self) -> "UpdateDepartmentIdDepartmentResponseBody":
        return self._update_department_id_department_response_body
