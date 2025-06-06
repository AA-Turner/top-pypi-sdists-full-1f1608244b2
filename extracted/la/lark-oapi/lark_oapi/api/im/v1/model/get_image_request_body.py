# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class GetImageRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetImageRequestBodyBuilder":
        return GetImageRequestBodyBuilder()


class GetImageRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._get_image_request_body = GetImageRequestBody()

    def build(self) -> "GetImageRequestBody":
        return self._get_image_request_body
