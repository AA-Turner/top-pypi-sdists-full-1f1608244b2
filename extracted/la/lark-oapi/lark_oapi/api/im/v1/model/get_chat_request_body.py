# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class GetChatRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetChatRequestBodyBuilder":
        return GetChatRequestBodyBuilder()


class GetChatRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._get_chat_request_body = GetChatRequestBody()

    def build(self) -> "GetChatRequestBody":
        return self._get_chat_request_body
