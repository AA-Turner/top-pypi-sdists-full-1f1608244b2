# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetChatAnnouncementRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.chat_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetChatAnnouncementRequestBuilder":
        return GetChatAnnouncementRequestBuilder()


class GetChatAnnouncementRequestBuilder(object):

    def __init__(self) -> None:
        get_chat_announcement_request = GetChatAnnouncementRequest()
        get_chat_announcement_request.http_method = HttpMethod.GET
        get_chat_announcement_request.uri = "/open-apis/docx/v1/chats/:chat_id/announcement"
        get_chat_announcement_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_chat_announcement_request: GetChatAnnouncementRequest = get_chat_announcement_request

    def user_id_type(self, user_id_type: str) -> "GetChatAnnouncementRequestBuilder":
        self._get_chat_announcement_request.user_id_type = user_id_type
        self._get_chat_announcement_request.add_query("user_id_type", user_id_type)
        return self

    def chat_id(self, chat_id: str) -> "GetChatAnnouncementRequestBuilder":
        self._get_chat_announcement_request.chat_id = chat_id
        self._get_chat_announcement_request.paths["chat_id"] = str(chat_id)
        return self

    def build(self) -> GetChatAnnouncementRequest:
        return self._get_chat_announcement_request
