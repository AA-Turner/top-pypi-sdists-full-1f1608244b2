# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ActiveCompanyResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ActiveCompanyResponseBodyBuilder":
        return ActiveCompanyResponseBodyBuilder()


class ActiveCompanyResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._active_company_response_body = ActiveCompanyResponseBody()

    def build(self) -> "ActiveCompanyResponseBody":
        return self._active_company_response_body
