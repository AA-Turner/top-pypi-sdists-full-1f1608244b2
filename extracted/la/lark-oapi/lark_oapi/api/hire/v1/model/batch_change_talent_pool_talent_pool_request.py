# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .batch_change_talent_pool_talent_pool_request_body import BatchChangeTalentPoolTalentPoolRequestBody


class BatchChangeTalentPoolTalentPoolRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.talent_pool_id: Optional[str] = None
        self.request_body: Optional[BatchChangeTalentPoolTalentPoolRequestBody] = None

    @staticmethod
    def builder() -> "BatchChangeTalentPoolTalentPoolRequestBuilder":
        return BatchChangeTalentPoolTalentPoolRequestBuilder()


class BatchChangeTalentPoolTalentPoolRequestBuilder(object):

    def __init__(self) -> None:
        batch_change_talent_pool_talent_pool_request = BatchChangeTalentPoolTalentPoolRequest()
        batch_change_talent_pool_talent_pool_request.http_method = HttpMethod.POST
        batch_change_talent_pool_talent_pool_request.uri = "/open-apis/hire/v1/talent_pools/:talent_pool_id/batch_change_talent_pool"
        batch_change_talent_pool_talent_pool_request.token_types = {AccessTokenType.TENANT}
        self._batch_change_talent_pool_talent_pool_request: BatchChangeTalentPoolTalentPoolRequest = batch_change_talent_pool_talent_pool_request

    def talent_pool_id(self, talent_pool_id: str) -> "BatchChangeTalentPoolTalentPoolRequestBuilder":
        self._batch_change_talent_pool_talent_pool_request.talent_pool_id = talent_pool_id
        self._batch_change_talent_pool_talent_pool_request.paths["talent_pool_id"] = str(talent_pool_id)
        return self

    def request_body(self,
                     request_body: BatchChangeTalentPoolTalentPoolRequestBody) -> "BatchChangeTalentPoolTalentPoolRequestBuilder":
        self._batch_change_talent_pool_talent_pool_request.request_body = request_body
        self._batch_change_talent_pool_talent_pool_request.body = request_body
        return self

    def build(self) -> BatchChangeTalentPoolTalentPoolRequest:
        return self._batch_change_talent_pool_talent_pool_request
