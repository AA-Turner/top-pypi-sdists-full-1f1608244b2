# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class DeleteTasklistActivitySubscriptionResponseBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteTasklistActivitySubscriptionResponseBodyBuilder":
        return DeleteTasklistActivitySubscriptionResponseBodyBuilder()


class DeleteTasklistActivitySubscriptionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._delete_tasklist_activity_subscription_response_body = DeleteTasklistActivitySubscriptionResponseBody()

    def build(self) -> "DeleteTasklistActivitySubscriptionResponseBody":
        return self._delete_tasklist_activity_subscription_response_body
