# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_application_environment_variable_response_body import QueryApplicationEnvironmentVariableResponseBody


class QueryApplicationEnvironmentVariableResponse(BaseResponse):
    _types = {
        "data": QueryApplicationEnvironmentVariableResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[QueryApplicationEnvironmentVariableResponseBody] = None
        init(self, d, self._types)
