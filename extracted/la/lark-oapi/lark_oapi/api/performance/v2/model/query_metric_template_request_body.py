# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class QueryMetricTemplateRequestBody(object):
    _types = {
        "metrics_template_ids": List[int],
        "status": str,
    }

    def __init__(self, d=None):
        self.metrics_template_ids: Optional[List[int]] = None
        self.status: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryMetricTemplateRequestBodyBuilder":
        return QueryMetricTemplateRequestBodyBuilder()


class QueryMetricTemplateRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._query_metric_template_request_body = QueryMetricTemplateRequestBody()

    def metrics_template_ids(self, metrics_template_ids: List[int]) -> "QueryMetricTemplateRequestBodyBuilder":
        self._query_metric_template_request_body.metrics_template_ids = metrics_template_ids
        return self

    def status(self, status: str) -> "QueryMetricTemplateRequestBodyBuilder":
        self._query_metric_template_request_body.status = status
        return self

    def build(self) -> "QueryMetricTemplateRequestBody":
        return self._query_metric_template_request_body
