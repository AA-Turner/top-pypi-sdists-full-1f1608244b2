# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteJobGradeResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteJobGradeResponseBodyBuilder":
        return DeleteJobGradeResponseBodyBuilder()


class DeleteJobGradeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_job_grade_response_body = DeleteJobGradeResponseBody()

    def build(self) -> "DeleteJobGradeResponseBody":
        return self._delete_job_grade_response_body
