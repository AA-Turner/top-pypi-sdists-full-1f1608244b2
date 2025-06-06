# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DownloadAsImageWhiteboardRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DownloadAsImageWhiteboardRequestBodyBuilder":
        return DownloadAsImageWhiteboardRequestBodyBuilder()


class DownloadAsImageWhiteboardRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._download_as_image_whiteboard_request_body = DownloadAsImageWhiteboardRequestBody()

    def build(self) -> "DownloadAsImageWhiteboardRequestBody":
        return self._download_as_image_whiteboard_request_body
