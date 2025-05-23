# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetTalentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.talent_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetTalentRequestBuilder":
        return GetTalentRequestBuilder()


class GetTalentRequestBuilder(object):

    def __init__(self) -> None:
        get_talent_request = GetTalentRequest()
        get_talent_request.http_method = HttpMethod.GET
        get_talent_request.uri = "/open-apis/hire/v2/talents/:talent_id"
        get_talent_request.token_types = {AccessTokenType.TENANT}
        self._get_talent_request: GetTalentRequest = get_talent_request

    def user_id_type(self, user_id_type: str) -> "GetTalentRequestBuilder":
        self._get_talent_request.user_id_type = user_id_type
        self._get_talent_request.add_query("user_id_type", user_id_type)
        return self

    def talent_id(self, talent_id: str) -> "GetTalentRequestBuilder":
        self._get_talent_request.talent_id = talent_id
        self._get_talent_request.paths["talent_id"] = str(talent_id)
        return self

    def build(self) -> GetTalentRequest:
        return self._get_talent_request
