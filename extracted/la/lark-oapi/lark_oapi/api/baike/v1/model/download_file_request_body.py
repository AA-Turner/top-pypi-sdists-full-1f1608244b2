# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DownloadFileRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DownloadFileRequestBodyBuilder":
        return DownloadFileRequestBodyBuilder()


class DownloadFileRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._download_file_request_body = DownloadFileRequestBody()

    def build(self) -> "DownloadFileRequestBody":
        return self._download_file_request_body
