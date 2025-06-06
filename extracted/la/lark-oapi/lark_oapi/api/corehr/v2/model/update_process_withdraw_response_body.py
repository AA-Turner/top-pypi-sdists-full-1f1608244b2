# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class UpdateProcessWithdrawResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateProcessWithdrawResponseBodyBuilder":
        return UpdateProcessWithdrawResponseBodyBuilder()


class UpdateProcessWithdrawResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_process_withdraw_response_body = UpdateProcessWithdrawResponseBody()

    def build(self) -> "UpdateProcessWithdrawResponseBody":
        return self._update_process_withdraw_response_body
