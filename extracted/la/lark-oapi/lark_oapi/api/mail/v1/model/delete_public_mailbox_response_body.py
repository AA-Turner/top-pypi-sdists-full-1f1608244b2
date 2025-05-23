# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeletePublicMailboxResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeletePublicMailboxResponseBodyBuilder":
        return DeletePublicMailboxResponseBodyBuilder()


class DeletePublicMailboxResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_public_mailbox_response_body = DeletePublicMailboxResponseBody()

    def build(self) -> "DeletePublicMailboxResponseBody":
        return self._delete_public_mailbox_response_body
