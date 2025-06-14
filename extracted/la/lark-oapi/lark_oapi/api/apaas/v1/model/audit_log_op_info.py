# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .lookup_with_avatar import LookupWithAvatar


class AuditLogOpInfo(object):
    _types = {
        "operator": LookupWithAvatar,
        "outsider": bool,
        "op_detail": Dict[str, str],
        "status": str,
        "failed_reason": str,
        "failed_reason_i18n": Dict[str, str],
        "op_time": str,
        "data_object": str,
        "op_source": str,
        "data_changes": List[str],
    }

    def __init__(self, d=None):
        self.operator: Optional[LookupWithAvatar] = None
        self.outsider: Optional[bool] = None
        self.op_detail: Optional[Dict[str, str]] = None
        self.status: Optional[str] = None
        self.failed_reason: Optional[str] = None
        self.failed_reason_i18n: Optional[Dict[str, str]] = None
        self.op_time: Optional[str] = None
        self.data_object: Optional[str] = None
        self.op_source: Optional[str] = None
        self.data_changes: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AuditLogOpInfoBuilder":
        return AuditLogOpInfoBuilder()


class AuditLogOpInfoBuilder(object):
    def __init__(self) -> None:
        self._audit_log_op_info = AuditLogOpInfo()

    def operator(self, operator: LookupWithAvatar) -> "AuditLogOpInfoBuilder":
        self._audit_log_op_info.operator = operator
        return self

    def outsider(self, outsider: bool) -> "AuditLogOpInfoBuilder":
        self._audit_log_op_info.outsider = outsider
        return self

    def op_detail(self, op_detail: Dict[str, str]) -> "AuditLogOpInfoBuilder":
        self._audit_log_op_info.op_detail = op_detail
        return self

    def status(self, status: str) -> "AuditLogOpInfoBuilder":
        self._audit_log_op_info.status = status
        return self

    def failed_reason(self, failed_reason: str) -> "AuditLogOpInfoBuilder":
        self._audit_log_op_info.failed_reason = failed_reason
        return self

    def failed_reason_i18n(self, failed_reason_i18n: Dict[str, str]) -> "AuditLogOpInfoBuilder":
        self._audit_log_op_info.failed_reason_i18n = failed_reason_i18n
        return self

    def op_time(self, op_time: str) -> "AuditLogOpInfoBuilder":
        self._audit_log_op_info.op_time = op_time
        return self

    def data_object(self, data_object: str) -> "AuditLogOpInfoBuilder":
        self._audit_log_op_info.data_object = data_object
        return self

    def op_source(self, op_source: str) -> "AuditLogOpInfoBuilder":
        self._audit_log_op_info.op_source = op_source
        return self

    def data_changes(self, data_changes: List[str]) -> "AuditLogOpInfoBuilder":
        self._audit_log_op_info.data_changes = data_changes
        return self

    def build(self) -> "AuditLogOpInfo":
        return self._audit_log_op_info
