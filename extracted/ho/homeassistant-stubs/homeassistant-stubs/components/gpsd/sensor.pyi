from . import GPSDConfigEntry as GPSDConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from gps3.agps3threaded import AGPS3mechanism as AGPS3mechanism
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_MODE as ATTR_MODE, ATTR_TIME as ATTR_TIME, EntityCategory as EntityCategory, UnitOfLength as UnitOfLength, UnitOfSpeed as UnitOfSpeed
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

_LOGGER: Incomplete
ATTR_CLIMB: str
ATTR_ELEVATION: str
ATTR_SPEED: str
ATTR_TOTAL_SATELLITES: str
ATTR_USED_SATELLITES: str
DEFAULT_NAME: str
_MODE_VALUES: Incomplete

def count_total_satellites_fn(agps_thread: AGPS3mechanism) -> int | None: ...
def count_used_satellites_fn(agps_thread: AGPS3mechanism) -> int | None: ...

@dataclass(frozen=True, kw_only=True)
class GpsdSensorDescription(SensorEntityDescription):
    value_fn: Callable[[AGPS3mechanism], StateType | datetime]

SENSOR_TYPES: tuple[GpsdSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: GPSDConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class GpsdSensor(SensorEntity):
    _attr_has_entity_name: bool
    entity_description: GpsdSensorDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    agps_thread: Incomplete
    def __init__(self, agps_thread: AGPS3mechanism, unique_id: str, description: GpsdSensorDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
