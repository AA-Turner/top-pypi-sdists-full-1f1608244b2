# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class RollbackPointsUserTaskRequestBody(object):
    _types = {
        "operator_user_id": str,
    }

    def __init__(self, d=None):
        self.operator_user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RollbackPointsUserTaskRequestBodyBuilder":
        return RollbackPointsUserTaskRequestBodyBuilder()


class RollbackPointsUserTaskRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._rollback_points_user_task_request_body = RollbackPointsUserTaskRequestBody()

    def operator_user_id(self, operator_user_id: str) -> "RollbackPointsUserTaskRequestBodyBuilder":
        self._rollback_points_user_task_request_body.operator_user_id = operator_user_id
        return self

    def build(self) -> "RollbackPointsUserTaskRequestBody":
        return self._rollback_points_user_task_request_body
