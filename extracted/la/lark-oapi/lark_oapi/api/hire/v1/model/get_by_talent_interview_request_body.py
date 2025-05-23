# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class GetByTalentInterviewRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetByTalentInterviewRequestBodyBuilder":
        return GetByTalentInterviewRequestBodyBuilder()


class GetByTalentInterviewRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._get_by_talent_interview_request_body = GetByTalentInterviewRequestBody()

    def build(self) -> "GetByTalentInterviewRequestBody":
        return self._get_by_talent_interview_request_body
