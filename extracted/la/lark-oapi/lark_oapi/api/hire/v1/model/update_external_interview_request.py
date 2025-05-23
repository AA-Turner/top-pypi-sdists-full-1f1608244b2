# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .external_interview import ExternalInterview


class UpdateExternalInterviewRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.external_interview_id: Optional[str] = None
        self.request_body: Optional[ExternalInterview] = None

    @staticmethod
    def builder() -> "UpdateExternalInterviewRequestBuilder":
        return UpdateExternalInterviewRequestBuilder()


class UpdateExternalInterviewRequestBuilder(object):

    def __init__(self) -> None:
        update_external_interview_request = UpdateExternalInterviewRequest()
        update_external_interview_request.http_method = HttpMethod.PUT
        update_external_interview_request.uri = "/open-apis/hire/v1/external_interviews/:external_interview_id"
        update_external_interview_request.token_types = {AccessTokenType.TENANT}
        self._update_external_interview_request: UpdateExternalInterviewRequest = update_external_interview_request

    def external_interview_id(self, external_interview_id: str) -> "UpdateExternalInterviewRequestBuilder":
        self._update_external_interview_request.external_interview_id = external_interview_id
        self._update_external_interview_request.paths["external_interview_id"] = str(external_interview_id)
        return self

    def request_body(self, request_body: ExternalInterview) -> "UpdateExternalInterviewRequestBuilder":
        self._update_external_interview_request.request_body = request_body
        self._update_external_interview_request.body = request_body
        return self

    def build(self) -> UpdateExternalInterviewRequest:
        return self._update_external_interview_request
