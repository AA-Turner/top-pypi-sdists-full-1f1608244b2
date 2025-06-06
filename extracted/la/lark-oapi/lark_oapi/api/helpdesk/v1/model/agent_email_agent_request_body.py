# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AgentEmailAgentRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AgentEmailAgentRequestBodyBuilder":
        return AgentEmailAgentRequestBodyBuilder()


class AgentEmailAgentRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._agent_email_agent_request_body = AgentEmailAgentRequestBody()

    def build(self) -> "AgentEmailAgentRequestBody":
        return self._agent_email_agent_request_body
