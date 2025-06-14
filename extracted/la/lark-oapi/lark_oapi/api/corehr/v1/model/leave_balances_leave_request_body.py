# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class LeaveBalancesLeaveRequestBody(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LeaveBalancesLeaveRequestBodyBuilder":
        return LeaveBalancesLeaveRequestBodyBuilder()


class LeaveBalancesLeaveRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._leave_balances_leave_request_body = LeaveBalancesLeaveRequestBody()

    def build(self) -> "LeaveBalancesLeaveRequestBody":
        return self._leave_balances_leave_request_body
