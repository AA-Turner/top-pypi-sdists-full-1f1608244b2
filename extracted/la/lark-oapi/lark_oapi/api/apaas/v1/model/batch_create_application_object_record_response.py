# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_create_application_object_record_response_body import BatchCreateApplicationObjectRecordResponseBody


class BatchCreateApplicationObjectRecordResponse(BaseResponse):
    _types = {
        "data": BatchCreateApplicationObjectRecordResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[BatchCreateApplicationObjectRecordResponseBody] = None
        init(self, d, self._types)
