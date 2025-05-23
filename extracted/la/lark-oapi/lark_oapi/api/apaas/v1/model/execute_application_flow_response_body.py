# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ExecuteApplicationFlowResponseBody(object):
    _types = {
        "status": str,
        "out_params": str,
        "execution_id": str,
        "error_msg": str,
        "code": str,
    }

    def __init__(self, d=None):
        self.status: Optional[str] = None
        self.out_params: Optional[str] = None
        self.execution_id: Optional[str] = None
        self.error_msg: Optional[str] = None
        self.code: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExecuteApplicationFlowResponseBodyBuilder":
        return ExecuteApplicationFlowResponseBodyBuilder()


class ExecuteApplicationFlowResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._execute_application_flow_response_body = ExecuteApplicationFlowResponseBody()

    def status(self, status: str) -> "ExecuteApplicationFlowResponseBodyBuilder":
        self._execute_application_flow_response_body.status = status
        return self

    def out_params(self, out_params: str) -> "ExecuteApplicationFlowResponseBodyBuilder":
        self._execute_application_flow_response_body.out_params = out_params
        return self

    def execution_id(self, execution_id: str) -> "ExecuteApplicationFlowResponseBodyBuilder":
        self._execute_application_flow_response_body.execution_id = execution_id
        return self

    def error_msg(self, error_msg: str) -> "ExecuteApplicationFlowResponseBodyBuilder":
        self._execute_application_flow_response_body.error_msg = error_msg
        return self

    def code(self, code: str) -> "ExecuteApplicationFlowResponseBodyBuilder":
        self._execute_application_flow_response_body.code = code
        return self

    def build(self) -> "ExecuteApplicationFlowResponseBody":
        return self._execute_application_flow_response_body
