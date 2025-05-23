# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .query_additional_information_request_body import QueryAdditionalInformationRequestBody


class QueryAdditionalInformationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.request_body: Optional[QueryAdditionalInformationRequestBody] = None

    @staticmethod
    def builder() -> "QueryAdditionalInformationRequestBuilder":
        return QueryAdditionalInformationRequestBuilder()


class QueryAdditionalInformationRequestBuilder(object):

    def __init__(self) -> None:
        query_additional_information_request = QueryAdditionalInformationRequest()
        query_additional_information_request.http_method = HttpMethod.POST
        query_additional_information_request.uri = "/open-apis/performance/v2/additional_informations/query"
        query_additional_information_request.token_types = {AccessTokenType.TENANT}
        self._query_additional_information_request: QueryAdditionalInformationRequest = query_additional_information_request

    def user_id_type(self, user_id_type: str) -> "QueryAdditionalInformationRequestBuilder":
        self._query_additional_information_request.user_id_type = user_id_type
        self._query_additional_information_request.add_query("user_id_type", user_id_type)
        return self

    def page_token(self, page_token: str) -> "QueryAdditionalInformationRequestBuilder":
        self._query_additional_information_request.page_token = page_token
        self._query_additional_information_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "QueryAdditionalInformationRequestBuilder":
        self._query_additional_information_request.page_size = page_size
        self._query_additional_information_request.add_query("page_size", page_size)
        return self

    def request_body(self,
                     request_body: QueryAdditionalInformationRequestBody) -> "QueryAdditionalInformationRequestBuilder":
        self._query_additional_information_request.request_body = request_body
        self._query_additional_information_request.body = request_body
        return self

    def build(self) -> QueryAdditionalInformationRequest:
        return self._query_additional_information_request
