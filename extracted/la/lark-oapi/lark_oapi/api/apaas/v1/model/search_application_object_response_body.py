# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .object_meta import ObjectMeta


class SearchApplicationObjectResponseBody(object):
    _types = {
        "records": str,
        "has_more": bool,
        "next_page_token": str,
        "objects": List[ObjectMeta],
    }

    def __init__(self, d=None):
        self.records: Optional[str] = None
        self.has_more: Optional[bool] = None
        self.next_page_token: Optional[str] = None
        self.objects: Optional[List[ObjectMeta]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchApplicationObjectResponseBodyBuilder":
        return SearchApplicationObjectResponseBodyBuilder()


class SearchApplicationObjectResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_application_object_response_body = SearchApplicationObjectResponseBody()

    def records(self, records: str) -> "SearchApplicationObjectResponseBodyBuilder":
        self._search_application_object_response_body.records = records
        return self

    def has_more(self, has_more: bool) -> "SearchApplicationObjectResponseBodyBuilder":
        self._search_application_object_response_body.has_more = has_more
        return self

    def next_page_token(self, next_page_token: str) -> "SearchApplicationObjectResponseBodyBuilder":
        self._search_application_object_response_body.next_page_token = next_page_token
        return self

    def objects(self, objects: List[ObjectMeta]) -> "SearchApplicationObjectResponseBodyBuilder":
        self._search_application_object_response_body.objects = objects
        return self

    def build(self) -> "SearchApplicationObjectResponseBody":
        return self._search_application_object_response_body
