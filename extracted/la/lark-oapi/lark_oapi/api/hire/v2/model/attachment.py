# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Attachment(object):
    _types = {
        "file_id": str,
        "file_name": str,
        "content_type": str,
        "file_size": int,
        "create_time": str,
    }

    def __init__(self, d=None):
        self.file_id: Optional[str] = None
        self.file_name: Optional[str] = None
        self.content_type: Optional[str] = None
        self.file_size: Optional[int] = None
        self.create_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AttachmentBuilder":
        return AttachmentBuilder()


class AttachmentBuilder(object):
    def __init__(self) -> None:
        self._attachment = Attachment()

    def file_id(self, file_id: str) -> "AttachmentBuilder":
        self._attachment.file_id = file_id
        return self

    def file_name(self, file_name: str) -> "AttachmentBuilder":
        self._attachment.file_name = file_name
        return self

    def content_type(self, content_type: str) -> "AttachmentBuilder":
        self._attachment.content_type = content_type
        return self

    def file_size(self, file_size: int) -> "AttachmentBuilder":
        self._attachment.file_size = file_size
        return self

    def create_time(self, create_time: str) -> "AttachmentBuilder":
        self._attachment.create_time = create_time
        return self

    def build(self) -> "Attachment":
        return self._attachment
