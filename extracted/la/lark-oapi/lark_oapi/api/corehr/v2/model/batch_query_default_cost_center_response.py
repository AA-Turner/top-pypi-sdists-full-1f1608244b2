# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_query_default_cost_center_response_body import BatchQueryDefaultCostCenterResponseBody


class BatchQueryDefaultCostCenterResponse(BaseResponse):
    _types = {
        "data": BatchQueryDefaultCostCenterResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[BatchQueryDefaultCostCenterResponseBody] = None
        init(self, d, self._types)
