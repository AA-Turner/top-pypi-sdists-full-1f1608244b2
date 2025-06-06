"""System service."""

import json
import os
import platform
import sys
import time
from socket import AF_INET, SOCK_DGRAM, socket
from typing import Any, NotRequired, TypedDict, cast
from urllib.error import HTTPError

from pydantic_settings import BaseSettings
from requests import get

from ..utils import (  # noqa: TID252
    UNHIDE_SENSITIVE_INFO,
    BaseService,
    Health,
    __env__,
    __project_name__,
    __project_path__,
    __repository_url__,
    __version__,
    get_logger,
    get_process_info,
    load_settings,
    locate_subclasses,
)
from ._settings import Settings

log = get_logger(__name__)

# Note: There is multiple measurements and network calls
MEASURE_INTERVAL_SECONDS = 5
NETWORK_TIMEOUT = 5


class RuntimeDict(TypedDict, total=False):
    """Type for runtime information dictionary."""

    environment: str
    username: str
    process: dict[str, Any]
    host: dict[str, Any]
    python: dict[str, Any]
    environ: dict[str, str]


class InfoDict(TypedDict, total=False):
    """Type for the info dictionary."""

    package: dict[str, Any]
    runtime: RuntimeDict
    settings: dict[str, Any]
    __extra__: NotRequired[dict[str, Any]]


class Service(BaseService):
    """System service."""

    _settings: Settings

    def __init__(self) -> None:
        """Initialize service."""
        super().__init__(Settings)

    @staticmethod
    def _is_healthy() -> bool:
        """Check if the service itself is healthy.

        Returns:
            bool: True if the service is healthy, False otherwise.
        """
        return True

    def health(self) -> Health:
        """Determine aggregate health of the system.

        - Health exposed by implementations of BaseService in other
            modules is automatically included into the health tree.
        - See utils/_health.py:Health for an explanation of the health tree.

        Returns:
            Health: The aggregate health of the system.
        """
        components: dict[str, Health] = {}
        for service_class in locate_subclasses(BaseService):
            if service_class is not Service:
                components[f"{service_class.__module__}.{service_class.__name__}"] = service_class().health()

        # Set the system health status based on is_healthy attribute
        status = Health.Code.UP if self._is_healthy() else Health.Code.DOWN
        reason = None if self._is_healthy() else "System marked as unhealthy"
        return Health(status=status, components=components, reason=reason)

    def is_token_valid(self, token: str) -> bool:
        """Check if the presented token is valid.

        Returns:
            bool: True if the token is valid, False otherwise.
        """
        log.info(token)
        if not self._settings.token:
            log.warning("Token is not set in settings.")
            return False
        return token == self._settings.token.get_secret_value()

    @staticmethod
    def _get_public_ipv4(timeout: int = NETWORK_TIMEOUT) -> str | None:
        """Get the public IPv4 address of the system.

        Args:
            timeout (int): Timeout for the request in seconds.

        Returns:
            str: The public IPv4 address.
        """
        try:
            response = get(url="https://api.ipify.org", timeout=timeout)
            response.raise_for_status()
            return response.text
        except HTTPError as e:
            message = f"Failed to get public IP: {e}"
            log.exception(message)
            return None

    @staticmethod
    def _get_local_ipv4() -> str | None:
        """Get the local IPv4 address of the system.

        Returns:
            str: The local IPv4 address.
        """
        try:
            with socket(AF_INET, SOCK_DGRAM) as connection:
                connection.connect((".".join(str(1) for _ in range(4)), 53))
                return str(connection.getsockname()[0])
        except Exception as e:
            message = f"Failed to get local IP: {e}"
            log.exception(message)
            return None

    @staticmethod
    
    def info(include_environ: bool = False, filter_secrets: bool = True) -> dict[str, Any]:
        """
        Get info about configuration of service.

        - Runtime information is automatically compiled.
        - Settings are automatically aggregated from all implementations of
            Pydantic BaseSettings in this package.
        - Info exposed by implementations of BaseService in other modules is
            automatically included into the info dict.

        Returns:
            dict[str, Any]: Service configuration.
        """
        import psutil  # noqa: PLC0415
        from uptime import boottime, uptime  # noqa: PLC0415

        bootdatetime = boottime()
        vmem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        cpu_percent = psutil.cpu_percent(interval=MEASURE_INTERVAL_SECONDS)
        cpu_times_percent = psutil.cpu_times_percent(interval=MEASURE_INTERVAL_SECONDS)

        rtn: InfoDict = {
            "package": {
                "version": __version__,
                "name": __project_name__,
                "repository": __repository_url__,
                "local": __project_path__,
            },
            "runtime": {
                "environment": __env__,
                "username": psutil.Process().username(),
                "process": {
                    "command_line": " ".join(sys.argv),
                    "entry_point": sys.argv[0] if sys.argv else None,
                    "process_info": json.loads(get_process_info().model_dump_json()),
                },
                "host": {
                    "os": {
                        "platform": platform.platform(),
                        "system": platform.system(),
                        "release": platform.release(),
                        "version": platform.version(),
                    },
                    "machine": {
                        "cpu": {
                            "percent": cpu_percent,
                            "load_avg": psutil.getloadavg(),
                            "user": cpu_times_percent.user,
                            "system": cpu_times_percent.system,
                            "idle": cpu_times_percent.idle,
                            "arch": platform.machine(),
                            "processor": platform.processor(),
                            "count": os.cpu_count(),
                            "frequency": {
                                "current": psutil.cpu_freq().max,
                                "min": psutil.cpu_freq().max,
                                "max": psutil.cpu_freq().max,
                            },
                        },
                        "memory": {
                            "percent": vmem.percent,
                            "total": vmem.total,
                            "available": vmem.available,
                            "used": vmem.used,
                            "free": vmem.free,
                        },
                        "swap": {
                            "percent": swap.percent,
                            "total": swap.total,
                            "used": swap.used,
                            "free": swap.free,
                        },
                    },
                    "network": {
                        "hostname": platform.node(),
                        "local_ipv4": Service._get_local_ipv4(),
                        "public_ipv4": Service._get_public_ipv4(),
                    },
                    "uptime": {
                        "seconds": uptime(),
                        "boottime": bootdatetime.isoformat() if bootdatetime else None,
                    },
                },
                "python": {
                    "version": platform.python_version(),
                    "compiler": platform.python_compiler(),
                    "implementation": platform.python_implementation(),
                    "sys.path": sys.path,
                    "interpreter_path": sys.executable,
                },
            },
            "settings": {},
        }

        runtime = cast("RuntimeDict", rtn["runtime"])
        if include_environ:
            if filter_secrets:
                runtime["environ"] = {
                    k: v
                    for k, v in sorted(os.environ.items())
                    if not (
                        "token" in k.lower()
                        or "key" in k.lower()
                        or "secret" in k.lower()
                        or "password" in k.lower()
                        or "auth" in k.lower()
                    )
                }
            else:
                runtime["environ"] = dict(sorted(os.environ.items()))

        settings: dict[str, Any] = {}
        for settings_class in locate_subclasses(BaseSettings):
            settings_instance = load_settings(settings_class)
            env_prefix = settings_instance.model_config.get("env_prefix", "")
            settings_dict = json.loads(
                settings_instance.model_dump_json(context={UNHIDE_SENSITIVE_INFO: not filter_secrets})
            )
            for key, value in settings_dict.items():
                flat_key = f"{env_prefix}{key}".upper()
                settings[flat_key] = value
        rtn["settings"] = {k: settings[k] for k in sorted(settings)}

        # Convert the TypedDict to a regular dict before adding dynamic service keys
        result_dict: dict[str, Any] = dict(rtn)

        for service_class in locate_subclasses(BaseService):
            if service_class is not Service:
                service = service_class()
                result_dict[service.key()] = service.info()

        log.info("Service info: %s", result_dict)
        return result_dict

    @staticmethod
    def div_by_zero() -> float:
        """Divide by zero to trigger an error.

        - This function is used to validate error handling and instrumentation
            in the system.

        Returns:
            float: This function will raise a ZeroDivisionError before returning.
        """
        return 1 / 0

    @staticmethod
    def sleep(seconds: int) -> None:
        """Sleep for a given number of seconds.

        - This function is used to validate performance profiling in the system.

        Args:
            seconds (int): Number of seconds to sleep.
        """
        time.sleep(seconds)
