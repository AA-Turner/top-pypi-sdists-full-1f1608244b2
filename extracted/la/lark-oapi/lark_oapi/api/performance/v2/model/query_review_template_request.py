# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .query_review_template_request_body import QueryReviewTemplateRequestBody


class QueryReviewTemplateRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.request_body: Optional[QueryReviewTemplateRequestBody] = None

    @staticmethod
    def builder() -> "QueryReviewTemplateRequestBuilder":
        return QueryReviewTemplateRequestBuilder()


class QueryReviewTemplateRequestBuilder(object):

    def __init__(self) -> None:
        query_review_template_request = QueryReviewTemplateRequest()
        query_review_template_request.http_method = HttpMethod.POST
        query_review_template_request.uri = "/open-apis/performance/v2/review_templates/query"
        query_review_template_request.token_types = {AccessTokenType.TENANT}
        self._query_review_template_request: QueryReviewTemplateRequest = query_review_template_request

    def page_token(self, page_token: str) -> "QueryReviewTemplateRequestBuilder":
        self._query_review_template_request.page_token = page_token
        self._query_review_template_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "QueryReviewTemplateRequestBuilder":
        self._query_review_template_request.page_size = page_size
        self._query_review_template_request.add_query("page_size", page_size)
        return self

    def request_body(self, request_body: QueryReviewTemplateRequestBody) -> "QueryReviewTemplateRequestBuilder":
        self._query_review_template_request.request_body = request_body
        self._query_review_template_request.body = request_body
        return self

    def build(self) -> QueryReviewTemplateRequest:
        return self._query_review_template_request
