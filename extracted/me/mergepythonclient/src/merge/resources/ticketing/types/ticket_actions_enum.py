# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TicketActionsEnum(str, enum.Enum):
    """
    * `VIEW` - VIEW
    * `CREATE` - CREATE
    * `EDIT` - EDIT
    * `DELETE` - DELETE
    * `CLOSE` - CLOSE
    * `ASSIGN` - ASSIGN
    """

    VIEW = "VIEW"
    CREATE = "CREATE"
    EDIT = "EDIT"
    DELETE = "DELETE"
    CLOSE = "CLOSE"
    ASSIGN = "ASSIGN"

    def visit(
        self,
        view: typing.Callable[[], T_Result],
        create: typing.Callable[[], T_Result],
        edit: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        close: typing.Callable[[], T_Result],
        assign: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TicketActionsEnum.VIEW:
            return view()
        if self is TicketActionsEnum.CREATE:
            return create()
        if self is TicketActionsEnum.EDIT:
            return edit()
        if self is TicketActionsEnum.DELETE:
            return delete()
        if self is TicketActionsEnum.CLOSE:
            return close()
        if self is TicketActionsEnum.ASSIGN:
            return assign()
