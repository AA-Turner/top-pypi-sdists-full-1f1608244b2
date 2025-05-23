# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_application_object_record_response_body import CreateApplicationObjectRecordResponseBody


class CreateApplicationObjectRecordResponse(BaseResponse):
    _types = {
        "data": CreateApplicationObjectRecordResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateApplicationObjectRecordResponseBody] = None
        init(self, d, self._types)
