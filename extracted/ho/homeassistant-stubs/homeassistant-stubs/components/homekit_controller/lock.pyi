from . import KNOWN_DEVICES as KNOWN_DEVICES
from .connection import HKDevice as HKDevice
from .entity import HomeKitEntity as HomeKitEntity
from _typeshed import Incomplete
from aiohomekit.model.services import Service as Service
from homeassistant.components.lock import LockEntity as LockEntity, LockState as LockState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, Platform as Platform, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

CURRENT_STATE_MAP: Incomplete
TARGET_STATE_MAP: Incomplete
REVERSED_TARGET_STATE_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeKitLock(HomeKitEntity, LockEntity):
    def get_characteristic_types(self) -> list[str]: ...
    @property
    def is_locked(self) -> bool | None: ...
    @property
    def is_locking(self) -> bool: ...
    @property
    def is_unlocking(self) -> bool: ...
    @property
    def is_jammed(self) -> bool: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def _set_lock_state(self, state: LockState) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
