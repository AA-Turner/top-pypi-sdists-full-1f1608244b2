# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .knowledge_source_helpdesk_filter import KnowledgeSourceHelpdeskFilter


class EnterpriseKnowledgeSourceHelpdeskParam(object):
    _types = {
        "searchable": bool,
        "filter": KnowledgeSourceHelpdeskFilter,
    }

    def __init__(self, d=None):
        self.searchable: Optional[bool] = None
        self.filter: Optional[KnowledgeSourceHelpdeskFilter] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EnterpriseKnowledgeSourceHelpdeskParamBuilder":
        return EnterpriseKnowledgeSourceHelpdeskParamBuilder()


class EnterpriseKnowledgeSourceHelpdeskParamBuilder(object):
    def __init__(self) -> None:
        self._enterprise_knowledge_source_helpdesk_param = EnterpriseKnowledgeSourceHelpdeskParam()

    def searchable(self, searchable: bool) -> "EnterpriseKnowledgeSourceHelpdeskParamBuilder":
        self._enterprise_knowledge_source_helpdesk_param.searchable = searchable
        return self

    def filter(self, filter: KnowledgeSourceHelpdeskFilter) -> "EnterpriseKnowledgeSourceHelpdeskParamBuilder":
        self._enterprise_knowledge_source_helpdesk_param.filter = filter
        return self

    def build(self) -> "EnterpriseKnowledgeSourceHelpdeskParam":
        return self._enterprise_knowledge_source_helpdesk_param
