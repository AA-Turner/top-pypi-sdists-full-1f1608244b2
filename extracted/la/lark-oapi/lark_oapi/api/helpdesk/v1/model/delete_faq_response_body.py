# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteFaqResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteFaqResponseBodyBuilder":
        return DeleteFaqResponseBodyBuilder()


class DeleteFaqResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_faq_response_body = DeleteFaqResponseBody()

    def build(self) -> "DeleteFaqResponseBody":
        return self._delete_faq_response_body
