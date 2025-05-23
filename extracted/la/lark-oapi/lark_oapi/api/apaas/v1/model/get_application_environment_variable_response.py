# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_application_environment_variable_response_body import GetApplicationEnvironmentVariableResponseBody


class GetApplicationEnvironmentVariableResponse(BaseResponse):
    _types = {
        "data": GetApplicationEnvironmentVariableResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetApplicationEnvironmentVariableResponseBody] = None
        init(self, d, self._types)
