from __future__ import annotations

from typing import Any

from . import auths, checks, contrib, experimental, fixups, graphql, hooks, runner, serializers, targets
from ._lazy_import import lazy_import
from .constants import SCHEMATHESIS_VERSION
from .generation import DataGenerationMethod, GenerationConfig, HeaderConfig
from .hooks import HookContext
from .models import Case
from .specs import openapi

__version__ = SCHEMATHESIS_VERSION

# Default loaders
from_aiohttp = openapi.from_aiohttp
from_asgi = openapi.from_asgi
from_dict = openapi.from_dict
from_file = openapi.from_file
from_path = openapi.from_path
from_pytest_fixture = openapi.from_pytest_fixture
from_uri = openapi.from_uri
from_wsgi = openapi.from_wsgi

# Public API
auth = auths.GLOBAL_AUTH_STORAGE
check = checks.register
hook = hooks.register
serializer = serializers.register
target = targets.register

# Backward compatibility
register_check = checks.register
register_target = targets.register
register_string_format = openapi.format

__all__ = [
    "auths",
    "checks",
    "experimental",
    "contrib",
    "fixups",
    "graphql",
    "hooks",
    "runner",
    "serializers",
    "targets",
    "DataGenerationMethod",
    "SCHEMATHESIS_VERSION",
    "Case",
    "openapi",
    "__version__",
    "from_aiohttp",
    "from_asgi",
    "from_dict",
    "from_file",
    "from_path",
    "from_pytest_fixture",
    "from_uri",
    "from_wsgi",
    "auth",
    "check",
    "hook",
    "serializer",
    "target",
    "register_check",
    "register_target",
    "register_string_format",
    "HookContext",
]


def _load_generic_response() -> Any:
    from .transports.responses import GenericResponse

    return GenericResponse


def _load_base_schema() -> Any:
    from .schemas import BaseSchema

    return BaseSchema


_imports = {"GenericResponse": _load_generic_response, "BaseSchema": _load_base_schema}


def __getattr__(name: str) -> Any:
    # Some modules are relatively heavy, hence load them lazily to improve startup time for CLI
    return lazy_import(__name__, name, _imports, globals())
