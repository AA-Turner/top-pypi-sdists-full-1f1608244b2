# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .invoke_application_function_request_body import InvokeApplicationFunctionRequestBody


class InvokeApplicationFunctionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.namespace: Optional[str] = None
        self.function_api_name: Optional[str] = None
        self.request_body: Optional[InvokeApplicationFunctionRequestBody] = None

    @staticmethod
    def builder() -> "InvokeApplicationFunctionRequestBuilder":
        return InvokeApplicationFunctionRequestBuilder()


class InvokeApplicationFunctionRequestBuilder(object):

    def __init__(self) -> None:
        invoke_application_function_request = InvokeApplicationFunctionRequest()
        invoke_application_function_request.http_method = HttpMethod.POST
        invoke_application_function_request.uri = "/open-apis/apaas/v1/applications/:namespace/functions/:function_api_name/invoke"
        invoke_application_function_request.token_types = {AccessTokenType.TENANT}
        self._invoke_application_function_request: InvokeApplicationFunctionRequest = invoke_application_function_request

    def namespace(self, namespace: str) -> "InvokeApplicationFunctionRequestBuilder":
        self._invoke_application_function_request.namespace = namespace
        self._invoke_application_function_request.paths["namespace"] = str(namespace)
        return self

    def function_api_name(self, function_api_name: str) -> "InvokeApplicationFunctionRequestBuilder":
        self._invoke_application_function_request.function_api_name = function_api_name
        self._invoke_application_function_request.paths["function_api_name"] = str(function_api_name)
        return self

    def request_body(self,
                     request_body: InvokeApplicationFunctionRequestBody) -> "InvokeApplicationFunctionRequestBuilder":
        self._invoke_application_function_request.request_body = request_body
        self._invoke_application_function_request.body = request_body
        return self

    def build(self) -> InvokeApplicationFunctionRequest:
        return self._invoke_application_function_request
