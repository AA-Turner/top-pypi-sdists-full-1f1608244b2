# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class ListPaymentActivityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.pay_period_start_date: Optional[str] = None
        self.pay_period_end_date: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.statuses: Optional[List[int]] = None

    @staticmethod
    def builder() -> "ListPaymentActivityRequestBuilder":
        return ListPaymentActivityRequestBuilder()


class ListPaymentActivityRequestBuilder(object):

    def __init__(self) -> None:
        list_payment_activity_request = ListPaymentActivityRequest()
        list_payment_activity_request.http_method = HttpMethod.GET
        list_payment_activity_request.uri = "/open-apis/payroll/v1/payment_activitys"
        list_payment_activity_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._list_payment_activity_request: ListPaymentActivityRequest = list_payment_activity_request

    def pay_period_start_date(self, pay_period_start_date: str) -> "ListPaymentActivityRequestBuilder":
        self._list_payment_activity_request.pay_period_start_date = pay_period_start_date
        self._list_payment_activity_request.add_query("pay_period_start_date", pay_period_start_date)
        return self

    def pay_period_end_date(self, pay_period_end_date: str) -> "ListPaymentActivityRequestBuilder":
        self._list_payment_activity_request.pay_period_end_date = pay_period_end_date
        self._list_payment_activity_request.add_query("pay_period_end_date", pay_period_end_date)
        return self

    def page_size(self, page_size: int) -> "ListPaymentActivityRequestBuilder":
        self._list_payment_activity_request.page_size = page_size
        self._list_payment_activity_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListPaymentActivityRequestBuilder":
        self._list_payment_activity_request.page_token = page_token
        self._list_payment_activity_request.add_query("page_token", page_token)
        return self

    def statuses(self, statuses: List[int]) -> "ListPaymentActivityRequestBuilder":
        self._list_payment_activity_request.statuses = statuses
        self._list_payment_activity_request.add_query("statuses", statuses)
        return self

    def build(self) -> ListPaymentActivityRequest:
        return self._list_payment_activity_request
