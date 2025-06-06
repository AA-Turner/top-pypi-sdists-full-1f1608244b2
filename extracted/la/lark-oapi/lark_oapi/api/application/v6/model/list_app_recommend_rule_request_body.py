# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ListAppRecommendRuleRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListAppRecommendRuleRequestBodyBuilder":
        return ListAppRecommendRuleRequestBodyBuilder()


class ListAppRecommendRuleRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._list_app_recommend_rule_request_body = ListAppRecommendRuleRequestBody()

    def build(self) -> "ListAppRecommendRuleRequestBody":
        return self._list_app_recommend_rule_request_body
