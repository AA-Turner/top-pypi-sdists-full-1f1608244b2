# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class InvokeApplicationFunctionResponseBody(object):
    _types = {
        "result": str,
    }

    def __init__(self, d=None):
        self.result: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InvokeApplicationFunctionResponseBodyBuilder":
        return InvokeApplicationFunctionResponseBodyBuilder()


class InvokeApplicationFunctionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._invoke_application_function_response_body = InvokeApplicationFunctionResponseBody()

    def result(self, result: str) -> "InvokeApplicationFunctionResponseBodyBuilder":
        self._invoke_application_function_response_body.result = result
        return self

    def build(self) -> "InvokeApplicationFunctionResponseBody":
        return self._invoke_application_function_response_body
