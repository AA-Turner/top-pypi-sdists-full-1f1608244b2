# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class GetProcessFormVariableDataRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetProcessFormVariableDataRequestBodyBuilder":
        return GetProcessFormVariableDataRequestBodyBuilder()


class GetProcessFormVariableDataRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._get_process_form_variable_data_request_body = GetProcessFormVariableDataRequestBody()

    def build(self) -> "GetProcessFormVariableDataRequestBody":
        return self._get_process_form_variable_data_request_body
