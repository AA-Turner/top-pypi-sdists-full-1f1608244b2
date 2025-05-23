# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteSubscribeFileResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteSubscribeFileResponseBodyBuilder":
        return DeleteSubscribeFileResponseBodyBuilder()


class DeleteSubscribeFileResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_subscribe_file_response_body = DeleteSubscribeFileResponseBody()

    def build(self) -> "DeleteSubscribeFileResponseBody":
        return self._delete_subscribe_file_response_body
