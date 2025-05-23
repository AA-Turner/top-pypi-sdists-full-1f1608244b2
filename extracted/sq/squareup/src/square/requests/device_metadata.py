# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing


class DeviceMetadataParams(typing_extensions.TypedDict):
    battery_percentage: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The Terminal’s remaining battery percentage, between 1-100.
    """

    charging_state: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The current charging state of the Terminal.
    Options: `CHARGING`, `NOT_CHARGING`
    """

    location_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the Square seller business location associated with the Terminal.
    """

    merchant_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the Square merchant account that is currently signed-in to the Terminal.
    """

    network_connection_type: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The Terminal’s current network connection type.
    Options: `WIFI`, `ETHERNET`
    """

    payment_region: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The country in which the Terminal is authorized to take payments.
    """

    serial_number: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The unique identifier assigned to the Terminal, which can be found on the lower back
    of the device.
    """

    os_version: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The current version of the Terminal’s operating system.
    """

    app_version: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The current version of the application running on the Terminal.
    """

    wifi_network_name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The name of the Wi-Fi network to which the Terminal is connected.
    """

    wifi_network_strength: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The signal strength of the Wi-FI network connection.
    Options: `POOR`, `FAIR`, `GOOD`, `EXCELLENT`
    """

    ip_address: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The IP address of the Terminal.
    """
