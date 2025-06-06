from __future__ import annotations

import contextlib
from typing import TYPE_CHECKING

from prettyqt import core, gui


if TYPE_CHECKING:
    from collections.abc import Callable


class UndoStackMixin(core.ObjectMixin):
    def __len__(self) -> int:
        return self.count()

    def __getitem__(self, index: int) -> gui.QUndoCommand:
        cmd = self.command(index)
        if cmd is None:
            raise KeyError(index)
        return cmd

    @contextlib.contextmanager
    def create_macro(self, text: str):
        self.beginMacro(text)
        yield None
        self.endMacro()

    def add_command(self, title: str, redo: Callable, undo: Callable) -> gui.UndoCommand:
        class MyCommand(gui.UndoCommand):
            def redo(self):
                return redo()

            def undo(self):
                return undo()

        cmd = MyCommand(title)
        self.push(cmd)
        return cmd


class UndoStack(UndoStackMixin, gui.QUndoStack):
    pass
