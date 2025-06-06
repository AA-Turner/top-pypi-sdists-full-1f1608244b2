# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class TerminateApplicationRequestBody(object):
    _types = {
        "termination_type": int,
        "termination_reason_list": List[str],
        "termination_reason_note": str,
        "need_terminate_offer": bool,
        "terminate_offer_operate_type": int,
        "cancel_offer_termination_type": int,
        "cancel_offer_termination_reason_list": List[str],
        "candidate_reject_offer_termination_reason_list": List[str],
        "need_withdraw_offer_approval": bool,
    }

    def __init__(self, d=None):
        self.termination_type: Optional[int] = None
        self.termination_reason_list: Optional[List[str]] = None
        self.termination_reason_note: Optional[str] = None
        self.need_terminate_offer: Optional[bool] = None
        self.terminate_offer_operate_type: Optional[int] = None
        self.cancel_offer_termination_type: Optional[int] = None
        self.cancel_offer_termination_reason_list: Optional[List[str]] = None
        self.candidate_reject_offer_termination_reason_list: Optional[List[str]] = None
        self.need_withdraw_offer_approval: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TerminateApplicationRequestBodyBuilder":
        return TerminateApplicationRequestBodyBuilder()


class TerminateApplicationRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._terminate_application_request_body = TerminateApplicationRequestBody()

    def termination_type(self, termination_type: int) -> "TerminateApplicationRequestBodyBuilder":
        self._terminate_application_request_body.termination_type = termination_type
        return self

    def termination_reason_list(self, termination_reason_list: List[str]) -> "TerminateApplicationRequestBodyBuilder":
        self._terminate_application_request_body.termination_reason_list = termination_reason_list
        return self

    def termination_reason_note(self, termination_reason_note: str) -> "TerminateApplicationRequestBodyBuilder":
        self._terminate_application_request_body.termination_reason_note = termination_reason_note
        return self

    def need_terminate_offer(self, need_terminate_offer: bool) -> "TerminateApplicationRequestBodyBuilder":
        self._terminate_application_request_body.need_terminate_offer = need_terminate_offer
        return self

    def terminate_offer_operate_type(self,
                                     terminate_offer_operate_type: int) -> "TerminateApplicationRequestBodyBuilder":
        self._terminate_application_request_body.terminate_offer_operate_type = terminate_offer_operate_type
        return self

    def cancel_offer_termination_type(self,
                                      cancel_offer_termination_type: int) -> "TerminateApplicationRequestBodyBuilder":
        self._terminate_application_request_body.cancel_offer_termination_type = cancel_offer_termination_type
        return self

    def cancel_offer_termination_reason_list(self, cancel_offer_termination_reason_list: List[
        str]) -> "TerminateApplicationRequestBodyBuilder":
        self._terminate_application_request_body.cancel_offer_termination_reason_list = cancel_offer_termination_reason_list
        return self

    def candidate_reject_offer_termination_reason_list(self, candidate_reject_offer_termination_reason_list: List[
        str]) -> "TerminateApplicationRequestBodyBuilder":
        self._terminate_application_request_body.candidate_reject_offer_termination_reason_list = candidate_reject_offer_termination_reason_list
        return self

    def need_withdraw_offer_approval(self,
                                     need_withdraw_offer_approval: bool) -> "TerminateApplicationRequestBodyBuilder":
        self._terminate_application_request_body.need_withdraw_offer_approval = need_withdraw_offer_approval
        return self

    def build(self) -> "TerminateApplicationRequestBody":
        return self._terminate_application_request_body
