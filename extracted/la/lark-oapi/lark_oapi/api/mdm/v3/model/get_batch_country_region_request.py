# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .get_batch_country_region_request_body import GetBatchCountryRegionRequestBody


class GetBatchCountryRegionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.fields: Optional[List[str]] = None
        self.ids: Optional[List[str]] = None
        self.languages: Optional[List[str]] = None
        self.request_body: Optional[GetBatchCountryRegionRequestBody] = None

    @staticmethod
    def builder() -> "GetBatchCountryRegionRequestBuilder":
        return GetBatchCountryRegionRequestBuilder()


class GetBatchCountryRegionRequestBuilder(object):

    def __init__(self) -> None:
        get_batch_country_region_request = GetBatchCountryRegionRequest()
        get_batch_country_region_request.http_method = HttpMethod.GET
        get_batch_country_region_request.uri = "/open-apis/mdm/v3/batch_country_region"
        get_batch_country_region_request.token_types = {AccessTokenType.TENANT}
        self._get_batch_country_region_request: GetBatchCountryRegionRequest = get_batch_country_region_request

    def fields(self, fields: List[str]) -> "GetBatchCountryRegionRequestBuilder":
        self._get_batch_country_region_request.fields = fields
        self._get_batch_country_region_request.add_query("fields", fields)
        return self

    def ids(self, ids: List[str]) -> "GetBatchCountryRegionRequestBuilder":
        self._get_batch_country_region_request.ids = ids
        self._get_batch_country_region_request.add_query("ids", ids)
        return self

    def languages(self, languages: List[str]) -> "GetBatchCountryRegionRequestBuilder":
        self._get_batch_country_region_request.languages = languages
        self._get_batch_country_region_request.add_query("languages", languages)
        return self

    def request_body(self, request_body: GetBatchCountryRegionRequestBody) -> "GetBatchCountryRegionRequestBuilder":
        self._get_batch_country_region_request.request_body = request_body
        self._get_batch_country_region_request.body = request_body
        return self

    def build(self) -> GetBatchCountryRegionRequest:
        return self._get_batch_country_region_request
