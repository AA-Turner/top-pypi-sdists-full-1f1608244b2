# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteContractRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteContractRequestBodyBuilder":
        return DeleteContractRequestBodyBuilder()


class DeleteContractRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_contract_request_body = DeleteContractRequestBody()

    def build(self) -> "DeleteContractRequestBody":
        return self._delete_contract_request_body
