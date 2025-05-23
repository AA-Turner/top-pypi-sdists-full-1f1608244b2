from . import RenaultConfigEntry as RenaultConfigEntry
from .const import CONF_KAMEREON_ACCOUNT_ID as CONF_KAMEREON_ACCOUNT_ID, COOLING_UPDATES_SECONDS as COOLING_UPDATES_SECONDS, MAX_CALLS_PER_HOURS as MAX_CALLS_PER_HOURS
from .renault_vehicle import COORDINATORS as COORDINATORS, RenaultVehicleProxy as RenaultVehicleProxy
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.const import ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_MODEL_ID as ATTR_MODEL_ID, ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from renault_api.kamereon.models import KamereonVehiclesLink as KamereonVehiclesLink
from renault_api.renault_account import RenaultAccount as RenaultAccount

LOGGER: Incomplete

class RenaultHub:
    _hass: Incomplete
    _client: Incomplete
    _account: RenaultAccount | None
    _vehicles: dict[str, RenaultVehicleProxy]
    _got_throttled_at_time: float | None
    def __init__(self, hass: HomeAssistant, locale: str) -> None: ...
    def set_throttled(self) -> None: ...
    def is_throttled(self) -> bool: ...
    async def attempt_login(self, username: str, password: str) -> bool: ...
    async def async_initialise(self, config_entry: RenaultConfigEntry) -> None: ...
    async def async_initialise_vehicle(self, vehicle_link: KamereonVehiclesLink, renault_account: RenaultAccount, scan_interval: timedelta, config_entry: RenaultConfigEntry, device_registry: dr.DeviceRegistry) -> None: ...
    async def get_account_ids(self) -> list[str]: ...
    @property
    def vehicles(self) -> dict[str, RenaultVehicleProxy]: ...
