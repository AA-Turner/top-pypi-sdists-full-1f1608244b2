# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .expediting_user_task_request_body import ExpeditingUserTaskRequestBody


class ExpeditingUserTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.task_id: Optional[str] = None
        self.request_body: Optional[ExpeditingUserTaskRequestBody] = None

    @staticmethod
    def builder() -> "ExpeditingUserTaskRequestBuilder":
        return ExpeditingUserTaskRequestBuilder()


class ExpeditingUserTaskRequestBuilder(object):

    def __init__(self) -> None:
        expediting_user_task_request = ExpeditingUserTaskRequest()
        expediting_user_task_request.http_method = HttpMethod.POST
        expediting_user_task_request.uri = "/open-apis/apaas/v1/user_tasks/:task_id/expediting"
        expediting_user_task_request.token_types = {AccessTokenType.TENANT}
        self._expediting_user_task_request: ExpeditingUserTaskRequest = expediting_user_task_request

    def task_id(self, task_id: str) -> "ExpeditingUserTaskRequestBuilder":
        self._expediting_user_task_request.task_id = task_id
        self._expediting_user_task_request.paths["task_id"] = str(task_id)
        return self

    def request_body(self, request_body: ExpeditingUserTaskRequestBody) -> "ExpeditingUserTaskRequestBuilder":
        self._expediting_user_task_request.request_body = request_body
        self._expediting_user_task_request.body = request_body
        return self

    def build(self) -> ExpeditingUserTaskRequest:
        return self._expediting_user_task_request
