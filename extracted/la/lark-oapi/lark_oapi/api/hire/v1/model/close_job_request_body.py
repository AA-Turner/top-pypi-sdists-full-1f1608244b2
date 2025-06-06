# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CloseJobRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CloseJobRequestBodyBuilder":
        return CloseJobRequestBodyBuilder()


class CloseJobRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._close_job_request_body = CloseJobRequestBody()

    def build(self) -> "CloseJobRequestBody":
        return self._close_job_request_body
