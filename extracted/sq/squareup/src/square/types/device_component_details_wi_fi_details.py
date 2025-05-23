# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .device_component_details_measurement import DeviceComponentDetailsMeasurement
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DeviceComponentDetailsWiFiDetails(UncheckedBaseModel):
    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean to represent whether the WiFI interface is currently active.
    """

    ssid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the connected WIFI network.
    """

    ip_address_v4: typing.Optional[str] = pydantic.Field(default=None)
    """
    The string representation of the device’s IPv4 address.
    """

    secure_connection: typing.Optional[str] = pydantic.Field(default=None)
    """
    The security protocol for a secure connection (e.g. WPA2). None provided if the connection
    is unsecured.
    """

    signal_strength: typing.Optional[DeviceComponentDetailsMeasurement] = pydantic.Field(default=None)
    """
    A representation of signal strength of the WIFI network connection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
