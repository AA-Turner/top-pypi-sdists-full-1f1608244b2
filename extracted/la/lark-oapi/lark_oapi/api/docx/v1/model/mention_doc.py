# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .text_element_style import TextElementStyle


class MentionDoc(object):
    _types = {
        "token": str,
        "obj_type": int,
        "url": str,
        "title": str,
        "text_element_style": TextElementStyle,
        "fallback_type": str,
    }

    def __init__(self, d=None):
        self.token: Optional[str] = None
        self.obj_type: Optional[int] = None
        self.url: Optional[str] = None
        self.title: Optional[str] = None
        self.text_element_style: Optional[TextElementStyle] = None
        self.fallback_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MentionDocBuilder":
        return MentionDocBuilder()


class MentionDocBuilder(object):
    def __init__(self) -> None:
        self._mention_doc = MentionDoc()

    def token(self, token: str) -> "MentionDocBuilder":
        self._mention_doc.token = token
        return self

    def obj_type(self, obj_type: int) -> "MentionDocBuilder":
        self._mention_doc.obj_type = obj_type
        return self

    def url(self, url: str) -> "MentionDocBuilder":
        self._mention_doc.url = url
        return self

    def title(self, title: str) -> "MentionDocBuilder":
        self._mention_doc.title = title
        return self

    def text_element_style(self, text_element_style: TextElementStyle) -> "MentionDocBuilder":
        self._mention_doc.text_element_style = text_element_style
        return self

    def fallback_type(self, fallback_type: str) -> "MentionDocBuilder":
        self._mention_doc.fallback_type = fallback_type
        return self

    def build(self) -> "MentionDoc":
        return self._mention_doc
