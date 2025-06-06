# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_question_response_body import QueryQuestionResponseBody


class QueryQuestionResponse(BaseResponse):
    _types = {
        "data": QueryQuestionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[QueryQuestionResponseBody] = None
        init(self, d, self._types)
