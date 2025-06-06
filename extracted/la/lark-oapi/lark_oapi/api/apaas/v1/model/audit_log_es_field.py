# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .lookup_with_avatar import LookupWithAvatar


class AuditLogEsField(object):
    _types = {
        "log_id": str,
        "op_time": str,
        "log_type": str,
        "operator": LookupWithAvatar,
        "outsider": bool,
        "login_type": str,
        "lark_tenant_id": str,
        "apaas_tenant_id": str,
        "user_geo": str,
        "client_ip": str,
        "ip_loc": str,
        "ip_provider": str,
        "referer": str,
        "origin": str,
        "api_path": str,
        "full_path": str,
        "user_agent": str,
        "device_id": str,
        "web_device_id": str,
        "terminal_type": str,
        "os_type": str,
        "os_version": str,
        "module": str,
        "data_object": str,
        "audit_scope": str,
        "tenant_id": str,
        "namespace": str,
        "env_type": str,
        "op_type": str,
        "op_detail": Dict[str, str],
        "op_source": str,
        "status": str,
        "failed_reason_i18n": Dict[str, str],
        "data_changes": List[str],
        "app_name": Dict[str, str],
        "keyword_field_app_version": str,
        "keyword_field_functional_sub_module": str,
    }

    def __init__(self, d=None):
        self.log_id: Optional[str] = None
        self.op_time: Optional[str] = None
        self.log_type: Optional[str] = None
        self.operator: Optional[LookupWithAvatar] = None
        self.outsider: Optional[bool] = None
        self.login_type: Optional[str] = None
        self.lark_tenant_id: Optional[str] = None
        self.apaas_tenant_id: Optional[str] = None
        self.user_geo: Optional[str] = None
        self.client_ip: Optional[str] = None
        self.ip_loc: Optional[str] = None
        self.ip_provider: Optional[str] = None
        self.referer: Optional[str] = None
        self.origin: Optional[str] = None
        self.api_path: Optional[str] = None
        self.full_path: Optional[str] = None
        self.user_agent: Optional[str] = None
        self.device_id: Optional[str] = None
        self.web_device_id: Optional[str] = None
        self.terminal_type: Optional[str] = None
        self.os_type: Optional[str] = None
        self.os_version: Optional[str] = None
        self.module: Optional[str] = None
        self.data_object: Optional[str] = None
        self.audit_scope: Optional[str] = None
        self.tenant_id: Optional[str] = None
        self.namespace: Optional[str] = None
        self.env_type: Optional[str] = None
        self.op_type: Optional[str] = None
        self.op_detail: Optional[Dict[str, str]] = None
        self.op_source: Optional[str] = None
        self.status: Optional[str] = None
        self.failed_reason_i18n: Optional[Dict[str, str]] = None
        self.data_changes: Optional[List[str]] = None
        self.app_name: Optional[Dict[str, str]] = None
        self.keyword_field_app_version: Optional[str] = None
        self.keyword_field_functional_sub_module: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AuditLogEsFieldBuilder":
        return AuditLogEsFieldBuilder()


class AuditLogEsFieldBuilder(object):
    def __init__(self) -> None:
        self._audit_log_es_field = AuditLogEsField()

    def log_id(self, log_id: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.log_id = log_id
        return self

    def op_time(self, op_time: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.op_time = op_time
        return self

    def log_type(self, log_type: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.log_type = log_type
        return self

    def operator(self, operator: LookupWithAvatar) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.operator = operator
        return self

    def outsider(self, outsider: bool) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.outsider = outsider
        return self

    def login_type(self, login_type: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.login_type = login_type
        return self

    def lark_tenant_id(self, lark_tenant_id: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.lark_tenant_id = lark_tenant_id
        return self

    def apaas_tenant_id(self, apaas_tenant_id: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.apaas_tenant_id = apaas_tenant_id
        return self

    def user_geo(self, user_geo: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.user_geo = user_geo
        return self

    def client_ip(self, client_ip: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.client_ip = client_ip
        return self

    def ip_loc(self, ip_loc: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.ip_loc = ip_loc
        return self

    def ip_provider(self, ip_provider: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.ip_provider = ip_provider
        return self

    def referer(self, referer: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.referer = referer
        return self

    def origin(self, origin: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.origin = origin
        return self

    def api_path(self, api_path: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.api_path = api_path
        return self

    def full_path(self, full_path: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.full_path = full_path
        return self

    def user_agent(self, user_agent: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.user_agent = user_agent
        return self

    def device_id(self, device_id: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.device_id = device_id
        return self

    def web_device_id(self, web_device_id: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.web_device_id = web_device_id
        return self

    def terminal_type(self, terminal_type: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.terminal_type = terminal_type
        return self

    def os_type(self, os_type: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.os_type = os_type
        return self

    def os_version(self, os_version: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.os_version = os_version
        return self

    def module(self, module: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.module = module
        return self

    def data_object(self, data_object: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.data_object = data_object
        return self

    def audit_scope(self, audit_scope: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.audit_scope = audit_scope
        return self

    def tenant_id(self, tenant_id: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.tenant_id = tenant_id
        return self

    def namespace(self, namespace: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.namespace = namespace
        return self

    def env_type(self, env_type: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.env_type = env_type
        return self

    def op_type(self, op_type: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.op_type = op_type
        return self

    def op_detail(self, op_detail: Dict[str, str]) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.op_detail = op_detail
        return self

    def op_source(self, op_source: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.op_source = op_source
        return self

    def status(self, status: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.status = status
        return self

    def failed_reason_i18n(self, failed_reason_i18n: Dict[str, str]) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.failed_reason_i18n = failed_reason_i18n
        return self

    def data_changes(self, data_changes: List[str]) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.data_changes = data_changes
        return self

    def app_name(self, app_name: Dict[str, str]) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.app_name = app_name
        return self

    def keyword_field_app_version(self, keyword_field_app_version: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.keyword_field_app_version = keyword_field_app_version
        return self

    def keyword_field_functional_sub_module(self, keyword_field_functional_sub_module: str) -> "AuditLogEsFieldBuilder":
        self._audit_log_es_field.keyword_field_functional_sub_module = keyword_field_functional_sub_module
        return self

    def build(self) -> "AuditLogEsField":
        return self._audit_log_es_field
