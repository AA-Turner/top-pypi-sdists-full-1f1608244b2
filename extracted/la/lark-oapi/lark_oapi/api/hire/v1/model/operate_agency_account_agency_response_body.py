# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class OperateAgencyAccountAgencyResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OperateAgencyAccountAgencyResponseBodyBuilder":
        return OperateAgencyAccountAgencyResponseBodyBuilder()


class OperateAgencyAccountAgencyResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._operate_agency_account_agency_response_body = OperateAgencyAccountAgencyResponseBody()

    def build(self) -> "OperateAgencyAccountAgencyResponseBody":
        return self._operate_agency_account_agency_response_body
