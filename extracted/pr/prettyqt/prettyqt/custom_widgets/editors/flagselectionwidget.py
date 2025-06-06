from __future__ import annotations

from collections.abc import Iterable, Iterator, Mapping
from typing import Literal

from prettyqt import core, widgets


class FlagSelectionWidget(widgets.GroupBox):
    value_changed = core.Signal(int)

    def __init__(
        self,
        label: str = "",
        layout: Literal["horizontal", "vertical"] = "vertical",
        object_name: str = "flag_selection_widget",
        **kwargs,
    ):
        super().__init__(title=label, object_name=object_name, **kwargs)
        self.set_layout(layout)
        self.buttons: dict[widgets.CheckBox, int] = {}

    def __iter__(self) -> Iterator[tuple[widgets.CheckBox, int]]:
        return iter(self.buttons.items())

    def add_items(self, items: Iterable | Mapping):
        if isinstance(items, Mapping):
            for k, v in items.items():
                self.add(v, k)
        else:
            for i in items:
                if isinstance(i, Iterable):
                    self.add(*i)
                else:
                    msg = "Invalid item type"
                    raise TypeError(msg)

    def add(self, title: str, flag: int):
        checkbox = widgets.CheckBox(title, toggled=self.update_choice)
        self.buttons[checkbox] = flag
        self.box.add(checkbox)

    def current_choice(self) -> int:
        ret_val = 0
        for btn, flag in self.buttons.items():
            if btn.isChecked():
                ret_val |= flag
        return int(ret_val)

    @core.Slot(bool)
    def update_choice(self, checked: bool):
        choice = self.current_choice()
        self.value_changed.emit(choice)

    def set_value(self, value: int):
        for btn, flag in self.buttons.items():
            btn.setChecked(bool(value & flag))

    def get_value(self) -> int:
        return self.current_choice()


if __name__ == "__main__":
    import re

    app = widgets.app()
    widget = FlagSelectionWidget()
    items = {re.MULTILINE: "MultiLine", re.IGNORECASE: "Ignore case"}
    widget.add_items(items)
    widget.show()
    app.exec()
