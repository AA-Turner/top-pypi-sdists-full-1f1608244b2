# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DownloadMediaRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DownloadMediaRequestBodyBuilder":
        return DownloadMediaRequestBodyBuilder()


class DownloadMediaRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._download_media_request_body = DownloadMediaRequestBody()

    def build(self) -> "DownloadMediaRequestBody":
        return self._download_media_request_body
