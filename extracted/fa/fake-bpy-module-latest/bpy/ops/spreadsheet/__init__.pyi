import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def add_row_filter_rule(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Add a filter to remove rows from the displayed data

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def change_spreadsheet_data_source(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    component_type: int | None = 0,
    attribute_domain_type: int | None = 0,
) -> None:
    """Change visible data source in the spreadsheet

    :type execution_context: int | str | None
    :type undo: bool | None
    :param component_type: Component Type
    :type component_type: int | None
    :param attribute_domain_type: Attribute Domain Type
    :type attribute_domain_type: int | None
    """

def fit_column(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Resize a spreadsheet column to the width of the data

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def remove_row_filter_rule(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    index: int | None = 0,
) -> None:
    """Remove a row filter from the rules

    :type execution_context: int | str | None
    :type undo: bool | None
    :param index: Index
    :type index: int | None
    """

def reorder_columns(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Change the order of columns

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def resize_column(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Resize a spreadsheet column

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def toggle_pin(
    execution_context: int | str | None = None, undo: bool | None = None
) -> None:
    """Turn on or off pinning

    :type execution_context: int | str | None
    :type undo: bool | None
    """
