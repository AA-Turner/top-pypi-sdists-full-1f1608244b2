from typing import Generic, Optional, Protocol, TypeVar, Union
from exponent.core.types.command_data import (
    DEFAULT_CODE_BLOCK_TIMEOUT,
    WRITE_STRATEGY_NATURAL_EDIT,
    CommandDataType,
    EditContent,
    FileWriteStrategyName,
    NaturalEditContent,
)
from pydantic import BaseModel, Field, JsonValue, ValidationInfo, field_validator
from datetime import datetime
from enum import Enum


class FileWriteErrorType(str, Enum):
    TERMINATION_REQUESTED = "TERMINATION_REQUESTED"
    NO_OP = "NO_OP"
    FAILED_APPLY = "FAILED_APPLY"
    FAILED_GENERATION = "FAILED_GENERATION"
    CLI_DISCONNECTED = "CLI_DISCONNECTED"


class ExponentEvent(BaseModel):
    chat_uuid: str
    event_uuid: str
    parent_uuid: Optional[str]
    turn_uuid: str

    metadata: dict[str, JsonValue] = Field(default_factory=dict)


class PersistedExponentEvent(ExponentEvent):
    db_timestamp: Union[datetime, None] = None


class CodeBlockEvent(PersistedExponentEvent):
    language: str
    content: str
    timeout: int = DEFAULT_CODE_BLOCK_TIMEOUT
    require_confirmation: bool = False


class FileWriteEvent(PersistedExponentEvent):
    file_path: str
    language: str
    write_strategy: FileWriteStrategyName
    write_content: Union[NaturalEditContent, EditContent]
    content: str
    error_content: Optional[str]
    error_type: Optional[FileWriteErrorType]
    require_confirmation: bool = False

    @field_validator("write_content")
    def validate_write_content_type(
        cls, v: Union[NaturalEditContent, EditContent], info: ValidationInfo
    ) -> Union[NaturalEditContent, EditContent]:
        write_strategy = info.data.get("write_strategy")
        if write_strategy == WRITE_STRATEGY_NATURAL_EDIT:
            if not isinstance(v, NaturalEditContent):
                raise ValueError(
                    "When write_strategy is NATURAL_EDIT, write_content must be NaturalEditContent"
                )
        else:
            if not isinstance(v, EditContent):
                raise ValueError(
                    "For non-NATURAL_EDIT strategies, write_content must be EditContent"
                )
        return v


T = TypeVar("T", bound=CommandDataType)


class HoldsCommandData(Protocol, Generic[T]):
    data: T


class CommandEvent(PersistedExponentEvent):
    data: CommandDataType
    require_confirmation: bool = False


class MultiCommandEvent(PersistedExponentEvent):
    data: list[CommandDataType]
    require_confirmation: bool = False


LocalEventType = Union[FileWriteEvent, CodeBlockEvent, CommandEvent]
