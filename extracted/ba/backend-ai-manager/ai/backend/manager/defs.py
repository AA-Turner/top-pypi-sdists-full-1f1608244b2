"""
Common definitions/constants used throughout the manager.
"""

import enum
import re
from typing import Final

from ai.backend.common.arch import CURRENT_ARCH
from ai.backend.common.arch import DEFAULT_IMAGE_ARCH as DEFAULT_IMAGE_ARCH_
from ai.backend.common.arch import arch_name_aliases as arch_name_aliases_
from ai.backend.common.types import SlotName, SlotTypes

INTRINSIC_SLOTS: Final = {
    SlotName("cpu"): SlotTypes("count"),
    SlotName("mem"): SlotTypes("bytes"),
}

INTRINSIC_SLOTS_MIN: Final = {
    # Values below are representing default value of image label -
    # so they must be string instead of Decimal.
    SlotName("cpu"): "1",  # 1 core
    SlotName("mem"): "1073741824",  # 1 GiB
}

arch_name_aliases: Final = arch_name_aliases_
DEFAULT_IMAGE_ARCH: Final = DEFAULT_IMAGE_ARCH_
MANAGER_ARCH: Final = CURRENT_ARCH

# The default chunk size used for streaming network traffic
DEFAULT_CHUNK_SIZE: Final = 16 * (2**20)  # 16 MiB

# The default container role name for multi-container sessions
DEFAULT_ROLE: Final = "main"

PASSWORD_PLACEHOLDER: Final = "*****"

_RESERVED_VFOLDER_PATTERNS = [r"^\.[a-z0-9]+rc$", r"^\.[a-z0-9]+_profile$"]
RESERVED_DOTFILES = [".terminfo", ".jupyter", ".ssh", ".ssh/authorized_keys", ".local", ".config"]
RESERVED_VFOLDERS = [
    ".terminfo",
    ".jupyter",
    ".tmux.conf",
    ".ssh",
    "/bin",
    "/boot",
    "/dev",
    "/etc",
    "/lib",
    "/lib64",
    "/media",
    "/mnt",
    "/opt",
    "/proc",
    "/root",
    "/run",
    "/sbin",
    "/srv",
    "/sys",
    "/tmp",
    "/usr",
    "/var",
    "/home",
]
RESERVED_VFOLDER_PATTERNS = [re.compile(x) for x in _RESERVED_VFOLDER_PATTERNS]

# Mapping between vfolder names and their in-container paths.
VFOLDER_DSTPATHS_MAP = {
    ".linuxbrew": "/home/linuxbrew/.linuxbrew",
}


# The unique identifiers for distributed locks.
# To be used with PostgreSQL advisory locks, the values are defined as integers.
class LockID(enum.IntEnum):
    LOCKID_TEST = 42
    LOCKID_SCHEDULE = 91
    LOCKID_CHECK_PRECOND = 92
    LOCKID_START = 93
    LOCKID_SCHEDULE_TIMER = 191
    LOCKID_CHECK_PRECOND_TIMER = 192
    LOCKID_START_TIMER = 198
    LOCKID_SCALE_TIMER = 193
    LOCKID_LOG_CLEANUP_TIMER = 195
    LOCKID_IDLE_CHECK_TIMER = 196
    LOCKID_SESSION_STATUS_UPDATE_TIMER = 197


SERVICE_MAX_RETRIES = 5  # FIXME: make configurable

DEFAULT_KEYPAIR_RESOURCE_POLICY_NAME: Final = "default"
DEFAULT_KEYPAIR_RATE_LIMIT: Final = 10000

DEFAULT_SHARED_MEMORY_SIZE: Final[str] = "64m"
START_SESSION_TIMEOUT_SEC: Final[float] = 60 * 30  # 30 min


DEFAULT_METRIC_RANGE_VECTOR_TIMEWINDOW: Final[str] = "1m"
