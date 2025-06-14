# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class CancelOnboardApplicationResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CancelOnboardApplicationResponseBodyBuilder":
        return CancelOnboardApplicationResponseBodyBuilder()


class CancelOnboardApplicationResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._cancel_onboard_application_response_body = CancelOnboardApplicationResponseBody()

    def build(self) -> "CancelOnboardApplicationResponseBody":
        return self._cancel_onboard_application_response_body
