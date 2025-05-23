# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class BatchGetOkrRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchGetOkrRequestBodyBuilder":
        return BatchGetOkrRequestBodyBuilder()


class BatchGetOkrRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_get_okr_request_body = BatchGetOkrRequestBody()

    def build(self) -> "BatchGetOkrRequestBody":
        return self._batch_get_okr_request_body
