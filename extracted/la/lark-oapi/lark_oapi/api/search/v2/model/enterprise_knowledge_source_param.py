# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .enterprise_knowledge_source_space_param import EnterpriseKnowledgeSourceSpaceParam
from .enterprise_knowledge_source_wiki_param import EnterpriseKnowledgeSourceWikiParam
from .enterprise_knowledge_source_message_param import EnterpriseKnowledgeSourceMessageParam
from .enterprise_knowledge_source_helpdesk_param import EnterpriseKnowledgeSourceHelpdeskParam
from .enterprise_knowledge_source_lingo_param import EnterpriseKnowledgeSourceLingoParam


class EnterpriseKnowledgeSourceParam(object):
    _types = {
        "space": EnterpriseKnowledgeSourceSpaceParam,
        "wiki": EnterpriseKnowledgeSourceWikiParam,
        "message": EnterpriseKnowledgeSourceMessageParam,
        "helpdesk_faq": EnterpriseKnowledgeSourceHelpdeskParam,
        "lingo": EnterpriseKnowledgeSourceLingoParam,
    }

    def __init__(self, d=None):
        self.space: Optional[EnterpriseKnowledgeSourceSpaceParam] = None
        self.wiki: Optional[EnterpriseKnowledgeSourceWikiParam] = None
        self.message: Optional[EnterpriseKnowledgeSourceMessageParam] = None
        self.helpdesk_faq: Optional[EnterpriseKnowledgeSourceHelpdeskParam] = None
        self.lingo: Optional[EnterpriseKnowledgeSourceLingoParam] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EnterpriseKnowledgeSourceParamBuilder":
        return EnterpriseKnowledgeSourceParamBuilder()


class EnterpriseKnowledgeSourceParamBuilder(object):
    def __init__(self) -> None:
        self._enterprise_knowledge_source_param = EnterpriseKnowledgeSourceParam()

    def space(self, space: EnterpriseKnowledgeSourceSpaceParam) -> "EnterpriseKnowledgeSourceParamBuilder":
        self._enterprise_knowledge_source_param.space = space
        return self

    def wiki(self, wiki: EnterpriseKnowledgeSourceWikiParam) -> "EnterpriseKnowledgeSourceParamBuilder":
        self._enterprise_knowledge_source_param.wiki = wiki
        return self

    def message(self, message: EnterpriseKnowledgeSourceMessageParam) -> "EnterpriseKnowledgeSourceParamBuilder":
        self._enterprise_knowledge_source_param.message = message
        return self

    def helpdesk_faq(self,
                     helpdesk_faq: EnterpriseKnowledgeSourceHelpdeskParam) -> "EnterpriseKnowledgeSourceParamBuilder":
        self._enterprise_knowledge_source_param.helpdesk_faq = helpdesk_faq
        return self

    def lingo(self, lingo: EnterpriseKnowledgeSourceLingoParam) -> "EnterpriseKnowledgeSourceParamBuilder":
        self._enterprise_knowledge_source_param.lingo = lingo
        return self

    def build(self) -> "EnterpriseKnowledgeSourceParam":
        return self._enterprise_knowledge_source_param
