# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteUserMailboxRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteUserMailboxRequestBodyBuilder":
        return DeleteUserMailboxRequestBodyBuilder()


class DeleteUserMailboxRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_user_mailbox_request_body = DeleteUserMailboxRequestBody()

    def build(self) -> "DeleteUserMailboxRequestBody":
        return self._delete_user_mailbox_request_body
