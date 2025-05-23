# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_external_interview_response_body import UpdateExternalInterviewResponseBody


class UpdateExternalInterviewResponse(BaseResponse):
    _types = {
        "data": UpdateExternalInterviewResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UpdateExternalInterviewResponseBody] = None
        init(self, d, self._types)
