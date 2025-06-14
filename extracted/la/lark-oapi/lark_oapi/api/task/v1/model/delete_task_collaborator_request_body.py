# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteTaskCollaboratorRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteTaskCollaboratorRequestBodyBuilder":
        return DeleteTaskCollaboratorRequestBodyBuilder()


class DeleteTaskCollaboratorRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_task_collaborator_request_body = DeleteTaskCollaboratorRequestBody()

    def build(self) -> "DeleteTaskCollaboratorRequestBody":
        return self._delete_task_collaborator_request_body
