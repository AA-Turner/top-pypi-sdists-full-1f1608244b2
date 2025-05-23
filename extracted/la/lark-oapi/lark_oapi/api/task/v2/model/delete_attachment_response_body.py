# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteAttachmentResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteAttachmentResponseBodyBuilder":
        return DeleteAttachmentResponseBodyBuilder()


class DeleteAttachmentResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_attachment_response_body = DeleteAttachmentResponseBody()

    def build(self) -> "DeleteAttachmentResponseBody":
        return self._delete_attachment_response_body
