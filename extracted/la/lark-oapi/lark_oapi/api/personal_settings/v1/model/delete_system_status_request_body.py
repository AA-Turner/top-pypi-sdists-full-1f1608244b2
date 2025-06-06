# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteSystemStatusRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteSystemStatusRequestBodyBuilder":
        return DeleteSystemStatusRequestBodyBuilder()


class DeleteSystemStatusRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_system_status_request_body = DeleteSystemStatusRequestBody()

    def build(self) -> "DeleteSystemStatusRequestBody":
        return self._delete_system_status_request_body
