from enum import Enum

from typing import Optional

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.schemas.ai_studio_agent_long_text_tool import AiStudioAgentLongTextTool

from box_sdk_gen.schemas.ai_studio_agent_basic_text_tool import (
    AiStudioAgentBasicTextTool,
)

from box_sdk_gen.box.errors import BoxSDKError


class AiStudioAgentAskTypeField(str, Enum):
    AI_AGENT_ASK = 'ai_agent_ask'


class AiStudioAgentAsk(BaseObject):
    _discriminator = 'type', {'ai_agent_ask'}

    def __init__(
        self,
        access_state: str,
        description: str,
        *,
        type: AiStudioAgentAskTypeField = AiStudioAgentAskTypeField.AI_AGENT_ASK,
        custom_instructions: Optional[str] = None,
        long_text: Optional[AiStudioAgentLongTextTool] = None,
        basic_text: Optional[AiStudioAgentBasicTextTool] = None,
        long_text_multi: Optional[AiStudioAgentLongTextTool] = None,
        basic_text_multi: Optional[AiStudioAgentBasicTextTool] = None,
        **kwargs
    ):
        """
        :param access_state: The state of the AI Agent capability. Possible values are: `enabled` and `disabled`.
        :type access_state: str
        :param description: The description of the AI Agent.
        :type description: str
        :param type: The type of AI agent used to handle queries., defaults to AiStudioAgentAskTypeField.AI_AGENT_ASK
        :type type: AiStudioAgentAskTypeField, optional
        :param custom_instructions: Custom instructions for the agent., defaults to None
        :type custom_instructions: Optional[str], optional
        """
        super().__init__(**kwargs)
        self.access_state = access_state
        self.description = description
        self.type = type
        self.custom_instructions = custom_instructions
        self.long_text = long_text
        self.basic_text = basic_text
        self.long_text_multi = long_text_multi
        self.basic_text_multi = basic_text_multi
