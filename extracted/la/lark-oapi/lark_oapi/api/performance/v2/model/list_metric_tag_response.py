# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_metric_tag_response_body import ListMetricTagResponseBody


class ListMetricTagResponse(BaseResponse):
    _types = {
        "data": ListMetricTagResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListMetricTagResponseBody] = None
        init(self, d, self._types)
