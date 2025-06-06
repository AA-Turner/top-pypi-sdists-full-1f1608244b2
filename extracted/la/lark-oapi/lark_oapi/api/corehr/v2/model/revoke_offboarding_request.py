# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .revoke_offboarding_request_body import RevokeOffboardingRequestBody


class RevokeOffboardingRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[RevokeOffboardingRequestBody] = None

    @staticmethod
    def builder() -> "RevokeOffboardingRequestBuilder":
        return RevokeOffboardingRequestBuilder()


class RevokeOffboardingRequestBuilder(object):

    def __init__(self) -> None:
        revoke_offboarding_request = RevokeOffboardingRequest()
        revoke_offboarding_request.http_method = HttpMethod.POST
        revoke_offboarding_request.uri = "/open-apis/corehr/v2/offboardings/revoke"
        revoke_offboarding_request.token_types = {AccessTokenType.TENANT}
        self._revoke_offboarding_request: RevokeOffboardingRequest = revoke_offboarding_request

    def user_id_type(self, user_id_type: str) -> "RevokeOffboardingRequestBuilder":
        self._revoke_offboarding_request.user_id_type = user_id_type
        self._revoke_offboarding_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: RevokeOffboardingRequestBody) -> "RevokeOffboardingRequestBuilder":
        self._revoke_offboarding_request.request_body = request_body
        self._revoke_offboarding_request.body = request_body
        return self

    def build(self) -> RevokeOffboardingRequest:
        return self._revoke_offboarding_request
