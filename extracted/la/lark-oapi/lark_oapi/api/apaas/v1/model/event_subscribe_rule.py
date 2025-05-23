# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .lookup_with_avatar import LookupWithAvatar


class EventSubscribeRule(object):
    _types = {
        "namespace": str,
        "event_type": str,
        "creator": str,
        "create_time": str,
        "id": str,
        "created_by": LookupWithAvatar,
    }

    def __init__(self, d=None):
        self.namespace: Optional[str] = None
        self.event_type: Optional[str] = None
        self.creator: Optional[str] = None
        self.create_time: Optional[str] = None
        self.id: Optional[str] = None
        self.created_by: Optional[LookupWithAvatar] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EventSubscribeRuleBuilder":
        return EventSubscribeRuleBuilder()


class EventSubscribeRuleBuilder(object):
    def __init__(self) -> None:
        self._event_subscribe_rule = EventSubscribeRule()

    def namespace(self, namespace: str) -> "EventSubscribeRuleBuilder":
        self._event_subscribe_rule.namespace = namespace
        return self

    def event_type(self, event_type: str) -> "EventSubscribeRuleBuilder":
        self._event_subscribe_rule.event_type = event_type
        return self

    def creator(self, creator: str) -> "EventSubscribeRuleBuilder":
        self._event_subscribe_rule.creator = creator
        return self

    def create_time(self, create_time: str) -> "EventSubscribeRuleBuilder":
        self._event_subscribe_rule.create_time = create_time
        return self

    def id(self, id: str) -> "EventSubscribeRuleBuilder":
        self._event_subscribe_rule.id = id
        return self

    def created_by(self, created_by: LookupWithAvatar) -> "EventSubscribeRuleBuilder":
        self._event_subscribe_rule.created_by = created_by
        return self

    def build(self) -> "EventSubscribeRule":
        return self._event_subscribe_rule
