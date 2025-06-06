"""A field with a 'working on it message'."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING
from typing import Any

from .form_handler_working import FormHandlerWorking
from .sentinels import Unknown
from .sentinels import unknown
from .validators import FieldValidators


if TYPE_CHECKING:
    from collections.abc import Callable

    from .curses_window import Window


@dataclass
class FieldWorking:
    """A text input field."""

    name: str
    messages: list[str]
    current_error: str = ""
    window_handler = FormHandlerWorking
    valid: bool | Unknown = unknown
    validator: Callable[..., Any] = FieldValidators.null
    win: Window | None = None

    @property
    def full_prompt(self) -> str:
        """Return the max width information.

        This is needed because windows width and : placement
        is based on the largest 'prompt'.

        Returns:
            Max width information message
        """
        return max(self.messages)

    def validate(self, response: str) -> None:
        """No validation required for working field.

        Args:
            response: Field response
        """
        self.valid = True

    def conditional_validation(self, response: str) -> None:
        """No conditional validation.

        Args:
            response: Field response
        """
        self.validate(response)
