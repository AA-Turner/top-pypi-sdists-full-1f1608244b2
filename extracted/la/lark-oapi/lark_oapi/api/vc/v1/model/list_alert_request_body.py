# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ListAlertRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListAlertRequestBodyBuilder":
        return ListAlertRequestBodyBuilder()


class ListAlertRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._list_alert_request_body = ListAlertRequestBody()

    def build(self) -> "ListAlertRequestBody":
        return self._list_alert_request_body
