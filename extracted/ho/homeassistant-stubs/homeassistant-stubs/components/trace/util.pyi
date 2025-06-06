from .const import DATA_TRACE as DATA_TRACE, DATA_TRACES_RESTORED as DATA_TRACES_RESTORED, DATA_TRACE_STORE as DATA_TRACE_STORE
from .models import ActionTrace as ActionTrace, BaseTrace as BaseTrace, RestoredTrace as RestoredTrace, TraceData as TraceData
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.limited_size_dict import LimitedSizeDict as LimitedSizeDict
from typing import Any

_LOGGER: Incomplete

async def async_get_trace(hass: HomeAssistant, key: str, run_id: str) -> dict[str, BaseTrace]: ...
async def async_list_contexts(hass: HomeAssistant, key: str | None) -> dict[str, dict[str, str]]: ...
def _get_debug_traces(hass: HomeAssistant, key: str) -> list[dict[str, Any]]: ...
async def async_list_traces(hass: HomeAssistant, wanted_domain: str, wanted_key: str | None) -> list[dict[str, Any]]: ...
def async_store_trace(hass: HomeAssistant, trace: ActionTrace, stored_traces: int) -> None: ...
def _async_store_restored_trace(hass: HomeAssistant, trace: RestoredTrace) -> None: ...
async def async_restore_traces(hass: HomeAssistant) -> None: ...
