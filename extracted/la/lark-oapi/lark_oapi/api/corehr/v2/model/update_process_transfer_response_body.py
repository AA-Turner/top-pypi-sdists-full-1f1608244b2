# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class UpdateProcessTransferResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateProcessTransferResponseBodyBuilder":
        return UpdateProcessTransferResponseBodyBuilder()


class UpdateProcessTransferResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_process_transfer_response_body = UpdateProcessTransferResponseBody()

    def build(self) -> "UpdateProcessTransferResponseBody":
        return self._update_process_transfer_response_body
