# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LlmConfigResultLlmType(str, enum.Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GEMINI = "gemini"
    AWS_BEDROCK = "aws_bedrock"
    AZURE_OPENAI = "azure_openai"

    def visit(
        self,
        openai: typing.Callable[[], T_Result],
        anthropic: typing.Callable[[], T_Result],
        gemini: typing.Callable[[], T_Result],
        aws_bedrock: typing.Callable[[], T_Result],
        azure_openai: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LlmConfigResultLlmType.OPENAI:
            return openai()
        if self is LlmConfigResultLlmType.ANTHROPIC:
            return anthropic()
        if self is LlmConfigResultLlmType.GEMINI:
            return gemini()
        if self is LlmConfigResultLlmType.AWS_BEDROCK:
            return aws_bedrock()
        if self is LlmConfigResultLlmType.AZURE_OPENAI:
            return azure_openai()
