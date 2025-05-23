# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteCostCenterVersionResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteCostCenterVersionResponseBodyBuilder":
        return DeleteCostCenterVersionResponseBodyBuilder()


class DeleteCostCenterVersionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_cost_center_version_response_body = DeleteCostCenterVersionResponseBody()

    def build(self) -> "DeleteCostCenterVersionResponseBody":
        return self._delete_cost_center_version_response_body
