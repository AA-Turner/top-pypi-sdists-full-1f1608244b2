from contextlib import suppress
from typing import Generator

from wbcore.contrib.icons import WBIcon
from wbcore.enums import Button
from wbcore.metadata.configs.buttons.buttons import DropDownButton
from wbcore.signals.instance_buttons import (
    add_button,
    add_extra_button,
    add_instance_button,
)
from wbcore.utils.importlib import parse_signal_received_for_module

from ..base import WBCoreViewConfig


class ButtonViewConfig(WBCoreViewConfig):
    SHOW_INLINE: bool = False  # set to true if the class needs to show custom button on inline

    metadata_key = "buttons"
    config_class_attribute = "button_config_class"

    def serialize(self, base_buttons: set[Button], remote_resources):
        """
        Serialize the button view config

        Args:
            base_buttons: the base button gathered from the view config
            remote_resources: the return of the send function
        Returns:
            Yield the serialized button, without duplicates and appends the module prefix to the remote button
        """
        base_buttons = list(zip([None] * len(base_buttons), base_buttons))  # append an empty perfix for base buttons
        for prefix, btn in parse_signal_received_for_module(remote_resources):
            base_buttons.append((prefix, btn))

        keys = []
        for key_prefix, btn in sorted(
            filter(lambda x: x[1], base_buttons), key=lambda e: (e[1].weight, e[1].label, e[1].title)
        ):
            btn_serialized = btn.serialize(self.request, key_prefix=key_prefix)
            if "key" not in btn_serialized or btn_serialized["key"] not in keys:  # ensure we don't include duplicates
                yield btn_serialized

    # Utils
    def order_buttons(self, buttons: set, ordering: list):
        yield from filter(lambda b: b in buttons, ordering)

    # FSM Button Configuration
    FSM_LIST = True
    FSM_INSTANCE = True
    FSM_DROPDOWN = False
    FSM_DROPDOWN_ICON = WBIcon.ADD.icon
    FSM_DROPDOWN_LABEL = "Transitions"
    FSM_WEIGHT = 100

    def get_fsm_buttons(self) -> set:
        if self.FSM_DROPDOWN and (FSM_BUTTONS := getattr(self.view, "FSM_BUTTONS")) and len(FSM_BUTTONS) > 0:
            return {
                DropDownButton(
                    label=self.FSM_DROPDOWN_LABEL,
                    icon=self.FSM_DROPDOWN_ICON,
                    title=self.FSM_DROPDOWN_LABEL,
                    weight=self.FSM_WEIGHT,
                    buttons=tuple(FSM_BUTTONS),
                )
            }
        return getattr(self.view, "FSM_BUTTONS", set())

    # list Button Configuration
    LIST_BUTTONS = frozenset({Button.NEW.value, Button.REFRESH.value})
    LIST_BUTTONS_ORDERING = [Button.NEW.value, Button.REFRESH.value]

    def get_list_buttons(self) -> Generator[None, str, None]:
        if content_type := self.view.get_content_type():
            buttons = set(self.LIST_BUTTONS)
            add_permission = f"{content_type.app_label}.add_{content_type.model}"

            if not self.request.user.has_perm(add_permission):
                with suppress(KeyError):
                    buttons.remove(Button.NEW.value)

            yield from self.order_buttons(buttons, self.LIST_BUTTONS_ORDERING)

    # Instance Button Configuration
    INSTANCE_BUTTONS = frozenset({Button.SAVE.value, Button.REFRESH.value, Button.DELETE.value})
    INSTANCE_BUTTONS_ORDERING = [Button.SAVE.value, Button.REFRESH.value, Button.DELETE.value]

    def get_instance_buttons(self) -> Generator[None, str, None]:
        if content_type := self.view.get_content_type():
            buttons = set(self.INSTANCE_BUTTONS)
            change_permission = f"{content_type.app_label}.change_{content_type.model}"
            delete_permission = f"{content_type.app_label}.delete_{content_type.model}"

            if not self.request.user.has_perm(change_permission):
                with suppress(KeyError):
                    buttons.remove(Button.SAVE.value)

            if not self.request.user.has_perm(delete_permission):
                with suppress(KeyError):
                    buttons.remove(Button.DELETE.value)

            yield from self.order_buttons(buttons, self.INSTANCE_BUTTONS_ORDERING)

    # Create Button Configuration
    CREATE_BUTTONS = frozenset(
        {Button.SAVE.value, Button.SAVE_AND_CLOSE.value, Button.SAVE_AND_NEW.value, Button.RESET.value}
    )
    CREATE_BUTTONS_ORDERING = [
        Button.SAVE.value,
        Button.SAVE_AND_CLOSE.value,
        Button.SAVE_AND_NEW.value,
        Button.RESET.value,
    ]

    def get_create_buttons(self) -> Generator[None, str, None]:
        buttons = set(self.CREATE_BUTTONS)
        yield from self.order_buttons(buttons, self.CREATE_BUTTONS_ORDERING)

    # Custom Instance Button Configuration
    CUSTOM_INSTANCE_BUTTONS = frozenset()
    CUSTOM_LIST_INSTANCE_BUTTONS = frozenset()
    CUSTOM_EXTRA_BUTTONS = frozenset()

    def get_custom_instance_buttons(self) -> set:
        return set(self.CUSTOM_INSTANCE_BUTTONS)

    def get_custom_list_instance_buttons(self) -> set:
        return set(self.CUSTOM_LIST_INSTANCE_BUTTONS)

    def _get_custom_instance_buttons(self) -> Generator:
        custom_instance_buttons = set()
        if self.instance:
            custom_instance_buttons |= self.get_custom_instance_buttons()
            if self.FSM_INSTANCE:
                custom_instance_buttons |= self.get_fsm_buttons()

        else:
            custom_instance_buttons |= self.get_custom_list_instance_buttons()
            if self.FSM_LIST:
                custom_instance_buttons |= self.get_fsm_buttons()

        yield from self.serialize(
            custom_instance_buttons,
            add_instance_button.send(
                self.view.__class__, many=not self.instance, request=self.request, view=self.view, **self.view.kwargs
            ),
        )

    def get_custom_extra_buttons(self) -> set:
        return set(self.CUSTOM_EXTRA_BUTTONS)

    def _get_custom_extra_buttons(self):
        yield from self.serialize(
            self.get_custom_extra_buttons(),
            add_extra_button.send(
                self.view.__class__, instance=self.instance, request=self.request, view=self.view, **self.view.kwargs
            ),
        )

    # Custom Button Configuration
    CUSTOM_BUTTONS = frozenset()

    def get_custom_buttons(self) -> set:
        return set(self.CUSTOM_BUTTONS)

    def _get_custom_buttons(self):
        yield from self.serialize(
            self.get_custom_buttons(),
            add_button.send(self.view.__class__, request=self.request, view=self.view, **self.view.kwargs),
        )

    def get_metadata(self) -> dict:
        return {
            "custom_instance": self._get_custom_instance_buttons(),
            "custom": self._get_custom_buttons()
            if (not self.view.inline or self.SHOW_INLINE)
            else [],  # we do not show button for list display generated through inline
            "extra": self._get_custom_extra_buttons(),
        }
