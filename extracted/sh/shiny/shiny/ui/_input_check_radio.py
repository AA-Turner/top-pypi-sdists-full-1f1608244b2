from __future__ import annotations

__all__ = (
    "input_checkbox",
    "input_checkbox_group",
    "input_radio_buttons",
)

from typing import Mapping, Optional, Union

from htmltools import Tag, TagChild, css, div, span, tags

from .._docstring import add_example
from ..bookmark import restore_input
from ..module import resolve_id
from ._html_deps_shinyverse import components_dependencies
from ._utils import shiny_input_label

# Canonical format for representing select options.
_Choices = Mapping[str, TagChild]

# Formats available to the user
ChoicesArg = Union[
    # ["a", "b", "c"]
    "list[str]",
    # ("a", "b", "c")
    "tuple[str, ...]",
    # {"a": "Choice A", "b": tags.i("Choice B")}
    _Choices,
]


@add_example()
def input_checkbox(
    id: str, label: TagChild, value: bool = False, *, width: Optional[str] = None
) -> Tag:
    """
    Create a checkbox that can be used to specify logical values.

    Parameters
    ----------
    id
        An input id.
    label
        An input label.
    value
        Initial value.
    width
        The CSS width, e.g. '400px', or '100%'

    Returns
    -------
    :
        A UI element.

    Notes
    ------
    ::: {.callout-note title="Server value"}
    ``True`` if checked, ``False`` otherwise.
    :::

    See Also
    --------
    * :func:`~shiny.ui.input_switch`
    * :func:`~shiny.ui.update_checkbox`
    * :func:`~shiny.ui.input_checkbox_group`
    * :func:`~shiny.ui.input_radio_buttons`
    """
    resolved_id = resolve_id(id)
    value = restore_input(resolved_id, value)
    return div(
        div(
            tags.label(
                tags.input(
                    id=resolved_id,
                    type="checkbox",
                    checked="checked" if value else None,
                    class_="shiny-input-checkbox",
                ),
                " ",
                span(label),
            ),
            class_="checkbox",
        ),
        class_="form-group shiny-input-container",
        style=css(width=width),
    )


@add_example()
def input_switch(
    id: str, label: TagChild, value: bool = False, *, width: Optional[str] = None
) -> Tag:
    """
    Create a switch that can be used to specify logical values. Similar to
    :func:`~shiny.ui.input_checkbox`, but implies to the user that the change will take effect
    immediately.

    Parameters
    ----------
    id
        An input id.
    label
        An input label.
    value
        Initial value.
    width
        The CSS width, e.g. '400px', or '100%'

    Returns
    -------
    :
        A UI element.

    Notes
    ------
    ::: {.callout-note title="Server value"}
    ``True`` if checked, ``False`` otherwise.
    :::

    See Also
    --------
    * :func:`~shiny.ui.input_checkbox`
    * :func:`~shiny.ui.update_switch`
    * :func:`~shiny.ui.input_checkbox_group`
    * :func:`~shiny.ui.input_radio_buttons`
    """

    return _bslib_input_checkbox(
        id,
        label,
        "bslib-input-switch form-switch",
        value,
        width=width,
    )


def _bslib_input_checkbox(
    id: str,
    label: TagChild,
    class_: str = "bslib-input-checkbox",
    value: bool = False,
    *,
    width: Optional[str] = None,
) -> Tag:
    resolved_id = resolve_id(id)
    value = restore_input(resolved_id, value)
    return div(
        div(
            {"class": "form-check"},
            tags.input(
                id=resolved_id,
                class_="form-check-input",
                type="checkbox",
                role="switch",
                checked="checked" if value else None,
            ),
            " ",
            tags.label(
                # Must be wrapped in `span` for update_switch(label=) method to work
                tags.span(label),
                class_="form-check-label",
                for_=resolved_id,
            ),
            class_=class_,
        ),
        components_dependencies(),
        class_="form-group shiny-input-container",
        style=css(width=width),
    )


@add_example()
def input_checkbox_group(
    id: str,
    label: TagChild,
    choices: ChoicesArg,
    *,
    selected: Optional[str | list[str]] = None,
    inline: bool = False,
    width: Optional[str] = None,
) -> Tag:
    """
    Create a group of checkboxes that can be used to toggle multiple choices
    independently.

    Parameters
    ----------
    id
        An input id.
    label
        An input label.
    choices
        Either a list of choices or a dictionary mapping choice values to labels. Note
        that if a dictionary is provided, the keys are used as the (input) values so
        that the dictionary values can hold HTML labels.
    selected
        The values that should be initially selected, if any.
    inline
        If `True`, the result is displayed inline.
    width
        The CSS width, e.g. '400px', or '100%'.

    Returns
    -------
    :
        A UI element.

    Notes
    ------
    ::: {.callout-note title="Server value"}
    A tuple of string(s) with the selected value(s) (if any).
    :::

    See Also
    --------
    * :func:`~shiny.ui.update_checkbox_group`
    * :func:`~shiny.ui.input_checkbox`
    * :func:`~shiny.ui.input_radio_buttons`
    """

    resolved_id = resolve_id(id)
    input_label = shiny_input_label(resolved_id, label)

    options = _generate_options(
        id=resolved_id,
        type="checkbox",
        choices=choices,
        selected=restore_input(resolved_id, selected),
        inline=inline,
    )
    return div(
        input_label,
        options,
        id=resolved_id,
        style=css(width=width),
        class_="form-group shiny-input-checkboxgroup shiny-input-container"
        + (" shiny-input-container-inline" if inline else ""),
        # https://www.w3.org/TR/wai-aria-practices/examples/checkbox/checkbox-1/checkbox-1.html
        role="group",
        aria_labelledby=input_label.attrs.get("id"),
    )


@add_example()
def input_radio_buttons(
    id: str,
    label: TagChild,
    choices: ChoicesArg,
    *,
    selected: Optional[str] = None,
    inline: bool = False,
    width: Optional[str] = None,
) -> Tag:
    """
    Create a set of radio buttons used to select an item from a list.

    Parameters
    ----------
    id
        An input id.
    label
        An input label.
    choices
        Either a list of choices or a dictionary mapping choice values to labels. Note
        that if a dictionary is provided, the keys are used as the (input) values so
        that the dictionary values can hold HTML labels.
    selected
        The values that should be initially selected, if any.
    inline
        If ``True``, the result is displayed inline.
    width
        The CSS width, e.g. '400px', or '100%'.

    Returns
    -------
    :
        A UI element

    Notes
    ------
    ::: {.callout-note title="Server value"}
    A string with the selected value.
    :::

    See Also
    --------
    * :func:`~shiny.ui.update_radio_buttons`
    * :func:`~shiny.ui.input_checkbox_group`
    * :func:`~shiny.ui.input_checkbox`
    """

    resolved_id = resolve_id(id)
    input_label = shiny_input_label(resolved_id, label)

    options = _generate_options(
        id=resolved_id,
        type="radio",
        choices=choices,
        selected=restore_input(resolved_id, selected),
        inline=inline,
    )
    return div(
        input_label,
        options,
        id=resolved_id,
        style=css(width=width),
        class_="form-group shiny-input-radiogroup shiny-input-container"
        + (" shiny-input-container-inline" if inline else ""),
        # https://www.w3.org/TR/2017/WD-wai-aria-practices-1.1-20170628/examples/radio/radio-1/radio-1.html
        role="radiogroup",
        aria_labelledby=input_label.attrs.get("id"),
    )


def _generate_options(
    id: str,
    type: str,
    choices: ChoicesArg,
    selected: Optional[str | list[str] | tuple[str, ...]],
    inline: bool,
) -> Tag:
    choicez = _normalize_choices(choices)

    if selected is None:
        if type == "radio":
            selected = list(choicez.keys())[0]
        else:
            selected = []

    if isinstance(selected, tuple):
        selected = list(selected)
    elif not isinstance(selected, list):
        selected = [selected]

    return div(
        [
            _generate_option(
                id,
                type,
                value=choice[0],
                label=choice[1],
                checked=choice[0] in selected,
                inline=inline,
            )
            for choice in choicez.items()
        ],
        class_="shiny-options-group",
    )


def _generate_option(
    id: str,
    type: str,
    value: str,
    label: TagChild,
    checked: bool,
    inline: bool,
) -> Tag:
    input = tags.input(
        type=type,
        name=id,
        value=value,
        checked="checked" if checked else None,
    )
    if inline:
        return tags.label(
            input,
            " ",
            span(label),
            class_=type + "-inline",
            _add_ws=True,
        )
    else:
        return div(
            tags.label(input, " ", span(label)),
            class_=type,
        )


def _normalize_choices(x: ChoicesArg) -> _Choices:
    if isinstance(x, (list, tuple)):
        return {k: k for k in x}
    else:
        return x
