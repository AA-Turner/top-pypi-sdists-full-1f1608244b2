# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .write_user_group_scope_data import WriteUserGroupScopeData


class WriteUserGroupUserRelResponseBody(object):
    _types = {
        "data": WriteUserGroupScopeData,
    }

    def __init__(self, d=None):
        self.data: Optional[WriteUserGroupScopeData] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WriteUserGroupUserRelResponseBodyBuilder":
        return WriteUserGroupUserRelResponseBodyBuilder()


class WriteUserGroupUserRelResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._write_user_group_user_rel_response_body = WriteUserGroupUserRelResponseBody()

    def data(self, data: WriteUserGroupScopeData) -> "WriteUserGroupUserRelResponseBodyBuilder":
        self._write_user_group_user_rel_response_body.data = data
        return self

    def build(self) -> "WriteUserGroupUserRelResponseBody":
        return self._write_user_group_user_rel_response_body
