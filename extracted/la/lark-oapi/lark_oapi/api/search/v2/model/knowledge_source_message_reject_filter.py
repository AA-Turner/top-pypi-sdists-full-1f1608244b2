# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class KnowledgeSourceMessageRejectFilter(object):
    _types = {
        "message_ids": List[str],
        "chat_ids": List[str],
    }

    def __init__(self, d=None):
        self.message_ids: Optional[List[str]] = None
        self.chat_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "KnowledgeSourceMessageRejectFilterBuilder":
        return KnowledgeSourceMessageRejectFilterBuilder()


class KnowledgeSourceMessageRejectFilterBuilder(object):
    def __init__(self) -> None:
        self._knowledge_source_message_reject_filter = KnowledgeSourceMessageRejectFilter()

    def message_ids(self, message_ids: List[str]) -> "KnowledgeSourceMessageRejectFilterBuilder":
        self._knowledge_source_message_reject_filter.message_ids = message_ids
        return self

    def chat_ids(self, chat_ids: List[str]) -> "KnowledgeSourceMessageRejectFilterBuilder":
        self._knowledge_source_message_reject_filter.chat_ids = chat_ids
        return self

    def build(self) -> "KnowledgeSourceMessageRejectFilter":
        return self._knowledge_source_message_reject_filter
