# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class GetSubdivisionRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetSubdivisionRequestBodyBuilder":
        return GetSubdivisionRequestBodyBuilder()


class GetSubdivisionRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._get_subdivision_request_body = GetSubdivisionRequestBody()

    def build(self) -> "GetSubdivisionRequestBody":
        return self._get_subdivision_request_body
