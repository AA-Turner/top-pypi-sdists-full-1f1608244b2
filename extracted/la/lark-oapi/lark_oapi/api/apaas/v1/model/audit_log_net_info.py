# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AuditLogNetInfo(object):
    _types = {
        "client_ip": str,
        "ip_loc": str,
        "ip_provider": str,
        "referer": str,
        "origin": str,
        "user_agent": str,
    }

    def __init__(self, d=None):
        self.client_ip: Optional[str] = None
        self.ip_loc: Optional[str] = None
        self.ip_provider: Optional[str] = None
        self.referer: Optional[str] = None
        self.origin: Optional[str] = None
        self.user_agent: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AuditLogNetInfoBuilder":
        return AuditLogNetInfoBuilder()


class AuditLogNetInfoBuilder(object):
    def __init__(self) -> None:
        self._audit_log_net_info = AuditLogNetInfo()

    def client_ip(self, client_ip: str) -> "AuditLogNetInfoBuilder":
        self._audit_log_net_info.client_ip = client_ip
        return self

    def ip_loc(self, ip_loc: str) -> "AuditLogNetInfoBuilder":
        self._audit_log_net_info.ip_loc = ip_loc
        return self

    def ip_provider(self, ip_provider: str) -> "AuditLogNetInfoBuilder":
        self._audit_log_net_info.ip_provider = ip_provider
        return self

    def referer(self, referer: str) -> "AuditLogNetInfoBuilder":
        self._audit_log_net_info.referer = referer
        return self

    def origin(self, origin: str) -> "AuditLogNetInfoBuilder":
        self._audit_log_net_info.origin = origin
        return self

    def user_agent(self, user_agent: str) -> "AuditLogNetInfoBuilder":
        self._audit_log_net_info.user_agent = user_agent
        return self

    def build(self) -> "AuditLogNetInfo":
        return self._audit_log_net_info
