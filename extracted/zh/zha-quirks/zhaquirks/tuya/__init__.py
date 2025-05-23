"""Tuya devices."""

from __future__ import annotations

from collections.abc import Callable
import dataclasses
import datetime
import enum
import logging
from typing import Any

from zigpy.quirks import BaseCustomDevice, CustomCluster, CustomDevice
import zigpy.types as t
from zigpy.typing import AddressingMode
from zigpy.zcl import BaseAttributeDefs, foundation
from zigpy.zcl.clusters.closures import WindowCovering
from zigpy.zcl.clusters.general import Basic, LevelControl, OnOff, PowerConfiguration
from zigpy.zcl.clusters.homeautomation import ElectricalMeasurement
from zigpy.zcl.clusters.hvac import Thermostat, UserInterface
from zigpy.zcl.clusters.smartenergy import Metering

from zhaquirks import Bus, EventableCluster, LocalDataCluster
from zhaquirks.const import (
    DOUBLE_PRESS,
    LEFT,
    LONG_PRESS,
    RIGHT,
    SHORT_PRESS,
    ZHA_SEND_EVENT,
    BatterySize,
)

# ---------------------------------------------------------
# Tuya Custom Cluster ID
# ---------------------------------------------------------
TUYA_CLUSTER_ID = 0xEF00
TUYA_CLUSTER_E000_ID = 0xE000
TUYA_CLUSTER_E001_ID = 0xE001
TUYA_CLUSTER_1888_ID = 0x1888
TUYA_CLUSTER_ED00_ID = 0xED00
# ---------------------------------------------------------
# Tuya Cluster Commands
# ---------------------------------------------------------
TUYA_SET_DATA = 0x00
TUYA_GET_DATA = 0x01
TUYA_SET_DATA_RESPONSE = 0x02
TUYA_QUERY_DATA = 0x03
TUYA_SEND_DATA = 0x04
TUYA_ACTIVE_STATUS_RPT = 0x06
TUYA_SET_TIME = 0x24
# TODO: To be checked
TUYA_MCU_VERSION_REQ = 0x10
TUYA_MCU_VERSION_RSP = 0x11
TUYA_LEVEL_COMMAND = 514

LEVEL_EVENT = "level_event"
TUYA_MCU_COMMAND = "tuya_mcu_command"

# Rotating for remotes
STOP = "stop"  # To constants

# ---------------------------------------------------------
# Value for dp_type
# ---------------------------------------------------------
# ID    Name            Description
# ---------------------------------------------------------
# 0x00 	DP_TYPE_RAW 	?
# 0x01 	DP_TYPE_BOOL 	?
# 0x02 	DP_TYPE_VALUE 	4 byte unsigned integer
# 0x03 	DP_TYPE_STRING 	variable length string
# 0x04 	DP_TYPE_ENUM 	1 byte enum
# 0x05 	DP_TYPE_FAULT 	1 byte bitmap (didn't test yet)
TUYA_DP_TYPE_RAW = 0x0000
TUYA_DP_TYPE_BOOL = 0x0100
TUYA_DP_TYPE_VALUE = 0x0200
TUYA_DP_TYPE_STRING = 0x0300
TUYA_DP_TYPE_ENUM = 0x0400
TUYA_DP_TYPE_FAULT = 0x0500
# ---------------------------------------------------------
# Value for dp_identifier (These are device specific)
# ---------------------------------------------------------
# ID    Name               Type    Description
# ---------------------------------------------------------
# 0x01  control            enum    open, stop, close, continue
# 0x02  percent_control    value   0-100% control
# 0x03  percent_state      value   Report from motor about current percentage
# 0x04  control_back       enum    Configures motor direction (untested)
# 0x05  work_state         enum    Motor Direction Setting
# 0x06  situation_set      enum    Configures if 100% equals to fully closed or fully open (untested)
# 0x07  fault              bitmap  Anything but 0 means something went wrong (untested)
TUYA_DP_ID_CONTROL = 0x01
TUYA_DP_ID_PERCENT_CONTROL = 0x02
TUYA_DP_ID_PERCENT_STATE = 0x03
TUYA_DP_ID_DIRECTION_CHANGE = 0x05
TUYA_DP_ID_COVER_INVERTED = 0x06
# ---------------------------------------------------------
# Window Cover Server Commands
# ---------------------------------------------------------
WINDOW_COVER_COMMAND_UPOPEN = 0x0000
WINDOW_COVER_COMMAND_DOWNCLOSE = 0x0001
WINDOW_COVER_COMMAND_STOP = 0x0002
WINDOW_COVER_COMMAND_LIFTPERCENT = 0x0005
WINDOW_COVER_COMMAND_CUSTOM = 0x0006
# ---------------------------------------------------------
# TUYA Cover Custom Values
# ---------------------------------------------------------
COVER_EVENT = "cover_event"
ATTR_COVER_POSITION = 0x0008
ATTR_COVER_DIRECTION = 0x8001
ATTR_COVER_INVERTED = 0x8002

# ---------------------------------------------------------
# TUYA Switch Custom Values
# ---------------------------------------------------------
SWITCH_EVENT = "switch_event"
ATTR_ON_OFF = 0x0000
TUYA_CMD_BASE = 0x0100
# ---------------------------------------------------------
# DP Value meanings in Status Report
# ---------------------------------------------------------
# Type ID    IntDP   Description
# ---------------------------------------------------------
# 0x04 0x01  1025    Confirm opening/closing/stopping (triggered from Zigbee)
# 0x02 0x02   514    Started moving to position (triggered from Zigbee)
# 0x04 0x07  1031    Started moving (triggered by transmitter order pulling on curtain)
# 0x02 0x03   515    Arrived at position
# 0x01 0x05   261    Returned by configuration set; ignore
# 0x02 0x69   617    Not sure what this is
# 0x04 0x05  1029    Changed the Motor Direction
# 0x04 0x65  1125    Change of tilt/lift mode 1 = lift 0=tilt
# ---------------------------------------------------------

_LOGGER = logging.getLogger(__name__)


class TuyaTimePayload(t.LVList, item_type=t.uint8_t, length_type=t.uint16_t_be):
    """Tuya set time payload definition."""


class TuyaDPType(t.enum8):
    """DataPoint Type."""

    RAW = 0x00
    BOOL = 0x01
    VALUE = 0x02
    STRING = 0x03
    ENUM = 0x04
    BITMAP = 0x05


class TuyaData(t.Struct):
    """Tuya Data type."""

    dp_type: TuyaDPType
    function: t.uint8_t
    raw: t.LVBytes

    @property
    def payload(
        self,
    ) -> (
        t.int32s_be
        | t.Bool
        | t.CharacterString
        | t.enum8
        | t.bitmap8
        | t.bitmap16
        | t.bitmap32
        | t.LVBytes
    ):
        """Payload accordingly to data point type."""
        if self.dp_type == TuyaDPType.VALUE:
            return t.int32s_be.deserialize(self.raw)[0]
        elif self.dp_type == TuyaDPType.BOOL:
            return t.Bool.deserialize(self.raw)[0]
        elif self.dp_type == TuyaDPType.STRING:
            return t.CharacterString(self.raw.decode("utf8"))
        elif self.dp_type == TuyaDPType.ENUM:
            return t.enum8.deserialize(self.raw)[0]
        elif self.dp_type == TuyaDPType.BITMAP:
            bitmaps = {1: t.bitmap8, 2: t.bitmap16, 4: t.bitmap32}
            try:
                return bitmaps[len(self.raw)].deserialize(self.raw)[0]
            except KeyError as exc:
                raise ValueError(f"Wrong bitmap length: {len(self.raw)}") from exc
        elif self.dp_type == TuyaDPType.RAW:
            return self.raw
        else:
            raise ValueError(f"Unknown {self.dp_type} datapoint type")

    @payload.setter
    def payload(self, value):
        """Set payload accordingly to data point type."""
        if self.dp_type == TuyaDPType.VALUE:
            self.raw = t.int32s_be(value).serialize()
        elif self.dp_type == TuyaDPType.BOOL:
            self.raw = t.Bool(value).serialize()
        elif self.dp_type == TuyaDPType.STRING:
            self.raw = value.encode("utf8")
        elif self.dp_type == TuyaDPType.ENUM:
            self.raw = t.enum8(value).serialize()
        elif self.dp_type == TuyaDPType.BITMAP:
            if not isinstance(value, (t.bitmap8, t.bitmap16, t.bitmap32)):
                value = t.bitmap8(value)
            self.raw = value.serialize()[::-1]
        elif self.dp_type == TuyaDPType.RAW:
            self.raw = value.serialize()
        else:
            raise ValueError(f"Unknown {self.dp_type} datapoint type")

    def __new__(cls, *args, **kwargs):
        """Disable copy constructor."""
        return super().__new__(cls)

    def __init__(self, value=None, function=0, *args, **kwargs):
        """Convert from a zigpy typed value to a tuya data payload."""
        self.function = function

        if value is None:
            return
        elif isinstance(value, (t.bitmap8, t.bitmap16, t.bitmap32)):
            self.dp_type = TuyaDPType.BITMAP
        elif isinstance(value, (bool, t.Bool)):
            self.dp_type = TuyaDPType.BOOL
        elif isinstance(value, enum.Enum):  # type: ignore
            self.dp_type = TuyaDPType.ENUM
        elif isinstance(value, int):
            self.dp_type = TuyaDPType.VALUE
        elif isinstance(value, str):
            self.dp_type = TuyaDPType.STRING
        else:
            self.dp_type = TuyaDPType.RAW

        self.payload = value


class Data(t.List, item_type=t.uint8_t):
    """list of uint8_t."""

    def __init__(self, value=None):
        """Convert from a zigpy typed value to a tuya data payload."""
        if value is None:
            super().__init__()
            return
        if type(value) is list or type(value) is bytes:  # noqa: E721
            super().__init__(value)
            return
        # serialized in little-endian by zigpy
        super().__init__(value.serialize())
        # we want big-endian, with length prepended
        self.append(len(self))
        self.reverse()

    def __int__(self):
        """Convert from a tuya data payload to an int typed value."""
        # first uint8_t is the length of the remaining data
        # tuya data is in big endian whereas ztypes use little endian
        ints = {
            1: t.int8s,
            2: t.int16s,
            3: t.int24s,
            4: t.int32s,
            5: t.int40s,
            6: t.int48s,
            7: t.int56s,
            8: t.int64s,
        }
        return ints[self[0]].deserialize(bytes(reversed(self[1:])))[0]

    def __iter__(self):
        """Convert from a tuya data payload to a list typed value."""
        return iter(reversed(self[1:]))

    def serialize(self) -> bytes:
        """Overload serialize to avoid prior implicit conversion to list."""
        assert self._item_type is not None
        return b"".join([self._item_type(i).serialize() for i in self[:]])


class TuyaDatapointData(t.Struct):
    """Tuya Datapoint and Data."""

    dp: t.uint8_t
    data: TuyaData


class TuyaCommand(t.Struct):
    """Tuya manufacturer cluster command."""

    status: t.uint8_t
    tsn: t.uint8_t
    datapoints: t.List[TuyaDatapointData]


class NoManufacturerCluster(CustomCluster):
    """Forces the NO manufacturer id in command."""

    async def command(
        self,
        command_id: foundation.GeneralCommand | int | t.uint8_t,
        *args,
        manufacturer: int | t.uint16_t | None = None,
        expect_reply: bool = True,
        tsn: int | t.uint8_t | None = None,
        **kwargs: Any,
    ):
        """Override the default Cluster command."""
        self.debug("Setting the NO manufacturer id in command: %s", command_id)
        return await super().command(
            command_id,
            *args,
            manufacturer=foundation.ZCLHeader.NO_MANUFACTURER_ID,
            expect_reply=expect_reply,
            tsn=tsn,
            **kwargs,
        )


class TuyaManufCluster(CustomCluster):
    """Tuya manufacturer specific cluster."""

    name = "Tuya Manufacturer Specicific"
    cluster_id = TUYA_CLUSTER_ID
    ep_attribute = "tuya_manufacturer"
    set_time_offset = 0
    set_time_local_offset = None

    # remove manufacturer id for cluster, important for `TUYA_SET_DATA` commands
    manufacturer_id_override: t.uint16_t = foundation.ZCLHeader.NO_MANUFACTURER_ID

    class Command(t.Struct):
        """Tuya manufacturer cluster command."""

        status: t.uint8_t
        tsn: t.uint8_t
        command_id: t.uint16_t
        function: t.uint8_t
        data: Data

    class MCUVersionRsp(t.Struct):
        """Tuya MCU version response Zcl payload."""

        tsn: t.uint16_t
        version: t.uint8_t

    """ Time sync command (It's transparent between MCU and server)
            Time request device -> server
               payloadSize = 0
            Set time, server -> device
               payloadSize, should be always 8
               payload[0-3] - UTC timestamp (big endian)
               payload[4-7] - Local timestamp (big endian)

            Zigbee payload is very similar to the UART payload which is described here: https://developer.tuya.com/en/docs/iot/device-development/access-mode-mcu/zigbee-general-solution/tuya-zigbee-module-uart-communication-protocol/tuya-zigbee-module-uart-communication-protocol?id=K9ear5khsqoty#title-10-Time%20synchronization

            Some devices need the timestamp in seconds from 1/1/1970 and others in seconds from 1/1/2000.
            Also, there is devices which uses both timestamps variants (probably bug). Use set_time_local_offset var in this cases.

            NOTE: You need to wait for time request before setting it. You can't set time without request."""

    server_commands = {
        0x0000: foundation.ZCLCommandDef(
            "set_data", {"param": Command}, False, is_manufacturer_specific=True
        ),
        0x0010: foundation.ZCLCommandDef(
            "mcu_version_req",
            {"param": t.uint16_t},
            False,
            is_manufacturer_specific=True,
        ),
        0x0024: foundation.ZCLCommandDef(
            "set_time", {"param": TuyaTimePayload}, False, is_manufacturer_specific=True
        ),
    }

    client_commands = {
        0x0001: foundation.ZCLCommandDef(
            "get_data", {"param": Command}, True, is_manufacturer_specific=True
        ),
        0x0002: foundation.ZCLCommandDef(
            "set_data_response", {"param": Command}, True, is_manufacturer_specific=True
        ),
        0x0006: foundation.ZCLCommandDef(
            "active_status_report",
            {"param": Command},
            True,
            is_manufacturer_specific=True,
        ),
        0x0011: foundation.ZCLCommandDef(
            "mcu_version_rsp",
            {"param": MCUVersionRsp},
            True,
            is_manufacturer_specific=True,
        ),
        0x0024: foundation.ZCLCommandDef(
            "set_time_request", {"param": t.data16}, True, is_manufacturer_specific=True
        ),
    }

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self.endpoint.device.command_bus = Bus()
        self.endpoint.device.command_bus.add_listener(self)  # listen MCU commands

    def tuya_mcu_command(self, command: Command):
        """Tuya MCU command listener. Only endpoint:1 must listen to MCU commands."""

        self.create_catching_task(
            self.command(TUYA_SET_DATA, command, expect_reply=True)
        )

    def handle_cluster_request(
        self,
        hdr: foundation.ZCLHeader,
        args: list[Any],
        *,
        dst_addressing: AddressingMode | None = None,
    ) -> None:
        """Handle time request."""

        if hdr.command_id != 0x0024 or self.set_time_offset == 0:
            return super().handle_cluster_request(
                hdr, args, dst_addressing=dst_addressing
            )

        # Send default response because the MCU expects it
        if not hdr.frame_control.disable_default_response:
            self.send_default_rsp(hdr, status=foundation.Status.SUCCESS)

        _LOGGER.debug(
            "[0x%04x:%s:0x%04x] Got set time request (command 0x%04x)",
            self.endpoint.device.nwk,
            self.endpoint.endpoint_id,
            self.cluster_id,
            hdr.command_id,
        )
        payload = TuyaTimePayload()
        utc_timestamp = int(
            (
                datetime.datetime.utcnow()  # noqa: DTZ003
                - datetime.datetime(self.set_time_offset, 1, 1)
            ).total_seconds()
        )
        local_timestamp = int(
            (
                datetime.datetime.now()
                - datetime.datetime(
                    self.set_time_local_offset or self.set_time_offset, 1, 1
                )
            ).total_seconds()
        )
        payload.extend(utc_timestamp.to_bytes(4, "big", signed=False))
        payload.extend(local_timestamp.to_bytes(4, "big", signed=False))

        self.create_catching_task(
            super().command(TUYA_SET_TIME, payload, expect_reply=False)
        )


class TuyaManufClusterAttributes(TuyaManufCluster):
    """Manufacturer specific cluster for Tuya converting attributes <-> commands."""

    def handle_cluster_request(
        self,
        hdr: foundation.ZCLHeader,
        args: list[Any],
        *,
        dst_addressing: AddressingMode | None = None,
    ) -> None:
        """Handle cluster request."""
        if hdr.command_id not in (0x0001, 0x0002):
            return super().handle_cluster_request(
                hdr, args, dst_addressing=dst_addressing
            )

        # Send default response because the MCU expects it
        if not hdr.frame_control.disable_default_response:
            self.send_default_rsp(hdr, status=foundation.Status.SUCCESS)

        tuya_cmd = args[0].command_id
        tuya_data = args[0].data

        _LOGGER.debug(
            "[0x%04x:%s:0x%04x] Received value %s "
            "for attribute 0x%04x (command 0x%04x)",
            self.endpoint.device.nwk,
            self.endpoint.endpoint_id,
            self.cluster_id,
            repr(tuya_data[1:]),
            tuya_cmd,
            hdr.command_id,
        )

        if tuya_cmd not in self.attributes:
            return

        ztype = self.attributes[tuya_cmd].type
        zvalue = ztype(tuya_data)
        self._update_attribute(tuya_cmd, zvalue)

    async def read_attributes(
        self, attributes, allow_cache=False, only_cache=False, manufacturer=None
    ):
        """Ignore remote reads as the "get_data" command doesn't seem to do anything."""

        return await super().read_attributes(
            attributes, allow_cache=True, only_cache=True, manufacturer=manufacturer
        )

    async def write_attributes(self, attributes, manufacturer=None):
        """Defer attributes writing to the set_data tuya command."""

        records = self._write_attr_records(attributes)

        for record in records:
            cmd_payload = TuyaManufCluster.Command()
            cmd_payload.status = 0
            cmd_payload.tsn = self.endpoint.device.application.get_sequence()
            cmd_payload.command_id = record.attrid
            cmd_payload.function = 0
            cmd_payload.data = record.value.value

            await super().command(
                TUYA_SET_DATA,
                cmd_payload,
                manufacturer=manufacturer,
                expect_reply=False,
                tsn=cmd_payload.tsn,
            )

        return [[foundation.WriteAttributesStatusRecord(foundation.Status.SUCCESS)]]


class BaseEnchantedDevice(BaseCustomDevice):
    """Class for Tuya devices which need to be unlocked by casting a 'spell'.

    The spell is applied during device configuration.
    """

    # These values can be overridden from a quirk to enable (or disable) additional Tuya spells:
    tuya_spell_read_attributes: bool = True  # spell reading attributes on Basic cluster
    tuya_spell_data_query: bool = False  # additional spell needed for some devices

    async def apply_custom_configuration(self, *args, **kwargs):
        """Hooks device configuration to apply custom configuration."""
        # cast Tuya spell
        if self.tuya_spell_read_attributes:
            await self.spell_attribute_reads()
        if self.tuya_spell_data_query:
            await self.spell_data_query()

        # also apply custom configuration to clusters if defined
        await super().apply_custom_configuration(*args, **kwargs)

    async def spell_attribute_reads(self):
        """Cast 'attribute read' spell, so the Tuya device works correctly."""
        self.debug(
            "Executing attribute read spell on Tuya device %s",
            self.ieee,
        )
        attr_to_read = [4, 0, 1, 5, 7, 0xFFFE]
        basic_cluster = self.endpoints[1].in_clusters[Basic.cluster_id]
        await basic_cluster.read_attributes(attr_to_read)
        self.debug("Executed attribute read spell on Tuya device %s", self.ieee)

    async def spell_data_query(self):
        """Cast 'data query' spell, also required for some Tuya devices to send data."""
        self.debug("Executing data query spell on Tuya device %s", self.ieee)
        # tests verify that a device with an enabled 'data query spell' has a TuyaNewManufCluster (subclass)
        tuya_cluster = self.endpoints[1].in_clusters[TuyaNewManufCluster.cluster_id]
        await tuya_cluster.command(TUYA_QUERY_DATA)
        self.debug("Executed data query spell on Tuya device %s", self.ieee)


class EnchantedDevice(CustomDevice, BaseEnchantedDevice):
    """Enchanted device class for v1 quirks."""


class TuyaOnOff(CustomCluster, OnOff):
    """Tuya On/Off cluster for On/Off device."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self.endpoint.device.switch_bus.add_listener(self)

    def switch_event(self, channel, state):
        """Switch event."""
        _LOGGER.debug(
            "%s - Received switch event message, channel: %d, state: %d",
            self.endpoint.device.ieee,
            channel,
            state,
        )
        # update status only if event == endpoint
        if self.endpoint.endpoint_id == channel:
            self._update_attribute(ATTR_ON_OFF, state)

    async def command(
        self,
        command_id: foundation.GeneralCommand | int | t.uint8_t,
        *args,
        manufacturer: int | t.uint16_t | None = None,
        expect_reply: bool = True,
        tsn: int | t.uint8_t | None = None,
        **kwargs: Any,
    ):
        """Override the default Cluster command."""

        if command_id in (0x0000, 0x0001):
            cmd_payload = TuyaManufCluster.Command()
            cmd_payload.status = 0
            # cmd_payload.tsn = tsn if tsn else self.endpoint.device.application.get_sequence()
            cmd_payload.tsn = 0
            cmd_payload.command_id = TUYA_CMD_BASE + self.endpoint.endpoint_id
            cmd_payload.function = 0
            cmd_payload.data = [1, command_id]

            self.endpoint.device.command_bus.listener_event(
                TUYA_MCU_COMMAND,
                cmd_payload,
            )
            return foundation.GENERAL_COMMANDS[
                foundation.GeneralCommand.Default_Response
            ].schema(command_id=command_id, status=foundation.Status.SUCCESS)

        return foundation.GENERAL_COMMANDS[
            foundation.GeneralCommand.Default_Response
        ].schema(command_id=command_id, status=foundation.Status.UNSUP_CLUSTER_COMMAND)


class TuyaManufacturerClusterOnOff(TuyaManufCluster):
    """Manufacturer Specific Cluster of On/Off device."""

    def handle_cluster_request(
        self,
        hdr: foundation.ZCLHeader,
        args: list[Any],
        *,
        dst_addressing: AddressingMode | None = None,
    ) -> None:
        """Handle cluster request."""

        if hdr.command_id in (0x0002, 0x0001):
            # Send default response because the MCU expects it
            if not hdr.frame_control.disable_default_response:
                self.send_default_rsp(hdr, status=foundation.Status.SUCCESS)

            tuya_payload = args[0]
            self.endpoint.device.switch_bus.listener_event(
                SWITCH_EVENT,
                tuya_payload.command_id - TUYA_CMD_BASE,
                tuya_payload.data[1],
            )
        elif hdr.command_id == TUYA_SET_TIME:
            """Time event call super"""
            _LOGGER.debug("TUYA_SET_TIME --> hdr: %s, args: %s", hdr, args)
            super().handle_cluster_request(hdr, args, dst_addressing=dst_addressing)
        else:
            _LOGGER.warning("Unsupported command: %s", hdr)


class TuyaSwitch(CustomDevice):
    """Tuya switch device."""

    def __init__(self, *args, **kwargs):
        """Init device."""
        self.switch_bus = Bus()
        super().__init__(*args, **kwargs)


class TuyaDimmerSwitch(TuyaSwitch):
    """Tuya dimmer switch device."""

    def __init__(self, *args, **kwargs):
        """Init device."""
        self.dimmer_bus = Bus()
        super().__init__(*args, **kwargs)


class TuyaThermostatCluster(LocalDataCluster, Thermostat):
    """Thermostat cluster for Tuya thermostats."""

    _CONSTANT_ATTRIBUTES = {0x001B: Thermostat.ControlSequenceOfOperation.Heating_Only}

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self.endpoint.device.thermostat_bus.add_listener(self)

    def temperature_change(self, attr, value):
        """Local or target temperature change from device."""
        self._update_attribute(self.attributes_by_name[attr].id, value)

    def state_change(self, value):
        """State update from device."""
        if value == 0:
            mode = self.RunningMode.Off
            state = self.RunningState.Idle
        else:
            mode = self.RunningMode.Heat
            state = self.RunningState.Heat_State_On
        self._update_attribute(self.attributes_by_name["running_mode"].id, mode)
        self._update_attribute(self.attributes_by_name["running_state"].id, state)

    # pylint: disable=R0201
    def map_attribute(self, attribute, value):
        """Map standardized attribute value to dict of manufacturer values."""
        return {}

    async def write_attributes(self, attributes, manufacturer=None):
        """Implement writeable attributes."""

        records = self._write_attr_records(attributes)

        if not records:
            return [[foundation.WriteAttributesStatusRecord(foundation.Status.SUCCESS)]]

        manufacturer_attrs = {}
        for record in records:
            attr_name = self.attributes[record.attrid].name
            new_attrs = self.map_attribute(attr_name, record.value.value)

            _LOGGER.debug(
                "[0x%04x:%s:0x%04x] Mapping standard %s (0x%04x) "
                "with value %s to custom %s",
                self.endpoint.device.nwk,
                self.endpoint.endpoint_id,
                self.cluster_id,
                attr_name,
                record.attrid,
                repr(record.value.value),
                repr(new_attrs),
            )

            manufacturer_attrs.update(new_attrs)

        if not manufacturer_attrs:
            return [
                [
                    foundation.WriteAttributesStatusRecord(
                        foundation.Status.FAILURE, r.attrid
                    )
                    for r in records
                ]
            ]

        await self.endpoint.tuya_manufacturer.write_attributes(
            manufacturer_attrs, manufacturer=manufacturer
        )

        return [[foundation.WriteAttributesStatusRecord(foundation.Status.SUCCESS)]]

    # pylint: disable=W0236
    async def command(
        self,
        command_id: foundation.GeneralCommand | int | t.uint8_t,
        *args,
        manufacturer: int | t.uint16_t | None = None,
        expect_reply: bool = True,
        tsn: int | t.uint8_t | None = None,
        **kwargs: Any,
    ):
        """Implement thermostat commands."""

        if command_id != 0x0000:
            return foundation.GENERAL_COMMANDS[
                foundation.GeneralCommand.Default_Response
            ].schema(
                command_id=command_id, status=foundation.Status.UNSUP_CLUSTER_COMMAND
            )

        mode, offset = args
        if mode not in (self.SetpointMode.Heat, self.SetpointMode.Both):
            return foundation.GENERAL_COMMANDS[
                foundation.GeneralCommand.Default_Response
            ].schema(command_id=command_id, status=foundation.Status.INVALID_VALUE)

        attrid = self.attributes_by_name["occupied_heating_setpoint"].id

        success, _ = await self.read_attributes((attrid,), manufacturer=manufacturer)
        try:
            current = success[attrid]
        except KeyError:
            return foundation.GENERAL_COMMANDS[
                foundation.GeneralCommand.Default_Response
            ].schema(command_id=command_id, status=foundation.Status.FAILURE)

        # offset is given in decidegrees, see Zigbee cluster specification
        (res,) = await self.write_attributes(
            {"occupied_heating_setpoint": current + offset * 10},
            manufacturer=manufacturer,
        )
        return foundation.GENERAL_COMMANDS[
            foundation.GeneralCommand.Default_Response
        ].schema(command_id=command_id, status=res[0].status)


class TuyaUserInterfaceCluster(LocalDataCluster, UserInterface):
    """HVAC User interface cluster for tuya thermostats."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self.endpoint.device.ui_bus.add_listener(self)

    def child_lock_change(self, mode):
        """Change of child lock setting."""
        if mode == 0:
            lockout = self.KeypadLockout.No_lockout
        else:
            lockout = self.KeypadLockout.Level_1_lockout

        self._update_attribute(self.attributes_by_name["keypad_lockout"].id, lockout)

    def map_attribute(self, attribute, value):
        """Map standardized attribute value to dict of manufacturer values."""
        return {}

    async def write_attributes(self, attributes, manufacturer=None):
        """Defer the keypad_lockout attribute to child_lock."""

        records = self._write_attr_records(attributes)

        manufacturer_attrs = {}
        for record in records:
            if record.attrid == self.attributes_by_name["keypad_lockout"].id:
                lock = 0 if record.value.value == self.KeypadLockout.No_lockout else 1
                new_attrs = {self._CHILD_LOCK_ATTR: lock}
            else:
                attr_name = self.attributes[record.attrid].name
                new_attrs = self.map_attribute(attr_name, record.value.value)

                _LOGGER.debug(
                    "[0x%04x:%s:0x%04x] Mapping standard %s (0x%04x) "
                    "with value %s to custom %s",
                    self.endpoint.device.nwk,
                    self.endpoint.endpoint_id,
                    self.cluster_id,
                    attr_name,
                    record.attrid,
                    repr(record.value.value),
                    repr(new_attrs),
                )

            manufacturer_attrs.update(new_attrs)

        if not manufacturer_attrs:
            return [
                [
                    foundation.WriteAttributesStatusRecord(
                        foundation.Status.FAILURE, r.attrid
                    )
                    for r in records
                ]
            ]

        await self.endpoint.tuya_manufacturer.write_attributes(
            manufacturer_attrs, manufacturer=manufacturer
        )

        return [[foundation.WriteAttributesStatusRecord(foundation.Status.SUCCESS)]]


class TuyaLocalCluster(LocalDataCluster):
    """Tuya virtual clusters.

    Prevents attribute reads and writes. Attribute writes could be converted
    to DataPoint updates.
    """

    def update_attribute(self, attr_name: str, value: Any) -> None:
        """Update attribute by name and safeguard against unknown attributes."""

        try:
            attr = self.attributes_by_name[attr_name]
        except KeyError:
            self.debug("no such attribute: %s", attr_name)
            return
        return self._update_attribute(attr.id, value)


class TuyaNoBindPowerConfigurationCluster(CustomCluster, PowerConfiguration):
    """PowerConfiguration cluster that prevents setting up binding/attribute reports in order to stop battery drain."""

    async def bind(self):
        """Prevent bind."""
        return (foundation.Status.SUCCESS,)

    async def _configure_reporting(self, *args, **kwargs):  # pylint: disable=W0221
        """Prevent remote configure reporting."""
        return (foundation.ConfigureReportingResponse.deserialize(b"\x00")[0],)


class TuyaPowerConfigurationCluster(PowerConfiguration, TuyaLocalCluster):
    """PowerConfiguration cluster for battery-operated thermostats."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        # listening to battery_bus required for legacy and custom Tuya TRV quirks
        if hasattr(self.endpoint.device, "battery_bus"):
            self.endpoint.device.battery_bus.add_listener(self)

    def battery_change(self, value):
        """Change of reported battery percentage remaining."""
        self.update_attribute("battery_percentage_remaining", value * 2)


class TuyaPowerConfigurationCluster2AAA(PowerConfiguration, TuyaLocalCluster):
    """PowerConfiguration cluster for devices with 2 AAA."""

    _CONSTANT_ATTRIBUTES = {
        PowerConfiguration.AttributeDefs.battery_size.id: BatterySize.AAA,
        PowerConfiguration.AttributeDefs.battery_rated_voltage.id: 15,
        PowerConfiguration.AttributeDefs.battery_quantity.id: 2,
    }


class TuyaPowerConfigurationCluster2AA(TuyaPowerConfigurationCluster):
    """PowerConfiguration cluster for devices with 2 AA."""

    _CONSTANT_ATTRIBUTES = {
        PowerConfiguration.AttributeDefs.battery_size.id: BatterySize.AA,
        PowerConfiguration.AttributeDefs.battery_rated_voltage.id: 15,
        PowerConfiguration.AttributeDefs.battery_quantity.id: 2,
    }


class TuyaPowerConfigurationCluster3AA(TuyaPowerConfigurationCluster):
    """PowerConfiguration cluster for devices with 3 AA."""

    _CONSTANT_ATTRIBUTES = {
        PowerConfiguration.AttributeDefs.battery_size.id: BatterySize.AA,
        PowerConfiguration.AttributeDefs.battery_rated_voltage.id: 15,
        PowerConfiguration.AttributeDefs.battery_quantity.id: 3,
    }


class TuyaPowerConfigurationCluster4AA(PowerConfiguration, TuyaLocalCluster):
    """PowerConfiguration cluster for devices with 4 AA."""

    _CONSTANT_ATTRIBUTES = {
        PowerConfiguration.AttributeDefs.battery_size.id: BatterySize.AA,
        PowerConfiguration.AttributeDefs.battery_rated_voltage.id: 15,
        PowerConfiguration.AttributeDefs.battery_quantity.id: 4,
    }


class TuyaPowerConfigurationClusterOther(PowerConfiguration, TuyaLocalCluster):
    """PowerConfiguration cluster for devices with other."""

    _CONSTANT_ATTRIBUTES = {
        PowerConfiguration.AttributeDefs.battery_size.id: BatterySize.Other,
        PowerConfiguration.AttributeDefs.battery_rated_voltage.id: 36,
        PowerConfiguration.AttributeDefs.battery_quantity.id: 1,
    }


class TuyaThermostat(CustomDevice):
    """Generic Tuya thermostat device."""

    def __init__(self, *args, **kwargs):
        """Init device."""
        self.thermostat_bus = Bus()
        self.ui_bus = Bus()
        self.battery_bus = Bus()
        super().__init__(*args, **kwargs)


# Tuya Zigbee OnOff Cluster Attribute Implementation
class SwitchBackLight(t.enum8):
    """Tuya switch back light mode enum."""

    Mode_0 = 0x00
    Mode_1 = 0x01
    Mode_2 = 0x02


class SwitchMode(t.enum8):
    """Tuya switch mode enum."""

    Command = 0x00
    Event = 0x01


class PowerOnState(t.enum8):
    """Tuya power on state enum."""

    Off = 0x00
    On = 0x01
    LastState = 0x02


class TuyaZBOnOffAttributeCluster(CustomCluster, OnOff):
    """Tuya Zigbee On Off cluster with extra attributes."""

    attributes = OnOff.attributes.copy()
    attributes.update({0x8000: ("child_lock", t.Bool)})
    attributes.update({0x8001: ("backlight_mode", SwitchBackLight)})
    attributes.update({0x8002: ("power_on_state", PowerOnState)})
    attributes.update({0x8004: ("switch_mode", SwitchMode)})


class TuyaSmartRemoteOnOffCluster(OnOff, EventableCluster):
    """TuyaSmartRemoteOnOffCluster: fire events corresponding to press type."""

    rotate_type = {
        0x00: RIGHT,
        0x01: LEFT,
        0x02: STOP,
    }
    press_type = {
        0x00: SHORT_PRESS,
        0x01: DOUBLE_PRESS,
        0x02: LONG_PRESS,
    }
    name = "TS004X_cluster"
    ep_attribute = "TS004X_cluster"
    attributes = OnOff.attributes.copy()
    attributes.update({0x8001: ("backlight_mode", SwitchBackLight)})
    attributes.update({0x8002: ("power_on_state", PowerOnState)})
    attributes.update({0x8004: ("switch_mode", SwitchMode)})

    def __init__(self, *args, **kwargs):
        """Init."""
        self.last_tsn = -1
        super().__init__(*args, **kwargs)

    server_commands = OnOff.server_commands.copy()
    server_commands.update(
        {
            0xFC: foundation.ZCLCommandDef(
                "rotate_type",
                {"rotate_type": t.uint8_t},
                False,
                is_manufacturer_specific=True,
            ),
            0xFD: foundation.ZCLCommandDef(
                "press_type",
                {"press_type": t.uint8_t},
                False,
                is_manufacturer_specific=True,
            ),
        }
    )

    def handle_cluster_request(
        self,
        hdr: foundation.ZCLHeader,
        args: list[Any],
        *,
        dst_addressing: AddressingMode | None = None,
    ) -> None:
        """Handle press_types command."""
        # normally if default response sent, TS004x wouldn't send such repeated zclframe (with same sequence number),
        # but for stability reasons (e. g. the case the response doesn't arrive the device), we can simply ignore it
        if hdr.tsn == self.last_tsn:
            _LOGGER.debug("TS004X: ignoring duplicate frame")
            return
        # save last sequence number
        self.last_tsn = hdr.tsn

        # send default response (as soon as possible), so avoid repeated zclframe from device
        if not hdr.frame_control.disable_default_response:
            self.debug("TS004X: send default response")
            self.send_default_rsp(hdr, status=foundation.Status.SUCCESS)
        # handle command
        if hdr.command_id == 0xFC:
            rotate_type = args[0]
            self.listener_event(
                ZHA_SEND_EVENT, self.rotate_type.get(rotate_type, "unknown"), []
            )
        elif hdr.command_id == 0xFD:
            press_type = args[0]
            self.listener_event(
                ZHA_SEND_EVENT, self.press_type.get(press_type, "unknown"), []
            )


MULTIPLIER = 0x0301
DIVISOR = 0x0302


# Tuya Zigbee Metering Cluster Correction Implementation
class TuyaZBMeteringCluster(CustomCluster, Metering):
    """Divides the kWh for tuya."""

    _CONSTANT_ATTRIBUTES = {MULTIPLIER: 1, DIVISOR: 100}


# Tuya Zigbee Metering Cluster Correction Implementation
class TuyaZBMeteringClusterWithUnit(CustomCluster, Metering):
    """Divides the kWh for tuya."""

    UNIT_OF_MEASURE = 0x0300
    _CONSTANT_ATTRIBUTES = {UNIT_OF_MEASURE: 0, MULTIPLIER: 1, DIVISOR: 100}


class TuyaZBElectricalMeasurement(CustomCluster, ElectricalMeasurement):
    """Divides the Current for tuya."""

    AC_CURRENT_MULTIPLIER = 0x0602
    AC_CURRENT_DIVISOR = 0x0603
    _CONSTANT_ATTRIBUTES = {AC_CURRENT_MULTIPLIER: 1, AC_CURRENT_DIVISOR: 1000}


# Tuya Zigbee Cluster 0xE000 Implementation
class TuyaZBE000Cluster(CustomCluster):
    """Tuya manufacturer specific cluster 57344."""

    name = "Tuya Manufacturer Specific 0"
    cluster_id = TUYA_CLUSTER_E000_ID
    ep_attribute = "tuya_manufacturer_specific_57344"


# Tuya Zigbee Cluster 0xE001 Implementation
class ExternalSwitchType(t.enum8):
    """Tuya external switch type enum."""

    Toggle = 0x00
    State = 0x01
    Momentary = 0x02


class TuyaZBExternalSwitchTypeCluster(CustomCluster):
    """Tuya External Switch Type Cluster."""

    name = "Tuya External Switch Type Cluster"
    cluster_id = TUYA_CLUSTER_E001_ID
    ep_attribute = "tuya_external_switch_type"
    attributes = {0xD030: ("external_switch_type", ExternalSwitchType)}


# Tuya Zigbee Cluster 0x1888 Implementation
class TuyaZB1888Cluster(CustomCluster):
    """Tuya manufacturer specific cluster 6280."""

    name = "Tuya Manufacturer Specific 1"
    cluster_id = TUYA_CLUSTER_1888_ID
    ep_attribute = "tuya_manufacturer_specific_6280"


# Tuya Window Cover Implementation
class TuyaManufacturerWindowCover(TuyaManufCluster):
    """Manufacturer Specific Cluster for cover device."""

    def handle_cluster_request(
        self,
        hdr: foundation.ZCLHeader,
        args: list[Any],
        *,
        dst_addressing: AddressingMode | None = None,
    ) -> None:
        """Handle cluster request."""
        # Tuya Specific Cluster Commands
        if hdr.command_id in (TUYA_GET_DATA, TUYA_SET_DATA_RESPONSE):
            tuya_payload = args[0]
            _LOGGER.debug(
                "%s Received Attribute Report. Command is 0x%04x, Tuya Paylod values"
                "[Status : %s, TSN: %s, Command: 0x%04x, Function: 0x%02x, Data: %s]",
                self.endpoint.device.ieee,
                hdr.command_id,
                tuya_payload.status,
                tuya_payload.tsn,
                tuya_payload.command_id,
                tuya_payload.function,
                tuya_payload.data,
            )

            ids = [
                TUYA_DP_TYPE_VALUE + TUYA_DP_ID_PERCENT_STATE,
                TUYA_DP_TYPE_VALUE + TUYA_DP_ID_PERCENT_CONTROL,
            ]
            if tuya_payload.command_id in ids:
                self.endpoint.device.cover_bus.listener_event(
                    COVER_EVENT,
                    ATTR_COVER_POSITION,
                    tuya_payload.data[4],
                )
            elif (
                tuya_payload.command_id
                == TUYA_DP_TYPE_ENUM + TUYA_DP_ID_DIRECTION_CHANGE
            ):
                self.endpoint.device.cover_bus.listener_event(
                    COVER_EVENT,
                    ATTR_COVER_DIRECTION,
                    tuya_payload.data[1],
                )
            elif (
                tuya_payload.command_id == TUYA_DP_TYPE_ENUM + TUYA_DP_ID_COVER_INVERTED
            ):
                self.endpoint.device.cover_bus.listener_event(
                    COVER_EVENT,
                    ATTR_COVER_INVERTED,
                    tuya_payload.data[1],  # Check this
                )
        elif hdr.command_id == TUYA_SET_TIME:
            """Time event call super"""
            super().handle_cluster_request(hdr, args, dst_addressing=dst_addressing)
        else:
            _LOGGER.debug(
                "%s Received Attribute Report - Unknown Command. Self [%s], Header [%s], Tuya Paylod [%s]",
                self.endpoint.device.ieee,
                self,
                hdr,
                args,
            )


class TuyaWindowCoverControl(LocalDataCluster, WindowCovering):
    """Manufacturer Specific Cluster of Device cover."""

    # Add additional attributes for direction
    attributes = WindowCovering.attributes.copy()
    attributes.update({ATTR_COVER_DIRECTION: ("motor_direction", t.Bool)})
    attributes.update({ATTR_COVER_INVERTED: ("cover_inverted", t.Bool)})

    def __init__(self, *args, **kwargs):
        """Initialize instance."""
        super().__init__(*args, **kwargs)
        self.endpoint.device.cover_bus.add_listener(self)

    def cover_event(self, attribute, value):
        """Event listener for cover events."""
        if attribute == ATTR_COVER_POSITION:
            invert_attr = self._attr_cache.get(ATTR_COVER_INVERTED) == 1
            invert = (
                not invert_attr
                if self.endpoint.device.tuya_cover_inverted_by_default
                else invert_attr
            )
            value = value if invert else 100 - value
        self._update_attribute(attribute, value)
        _LOGGER.debug(
            "%s Tuya Attribute Cache : [%s]",
            self.endpoint.device.ieee,
            self._attr_cache,
        )

    def command(
        self,
        command_id: foundation.GeneralCommand | int | t.uint8_t,
        *args,
        manufacturer: int | t.uint16_t | None = None,
        expect_reply: bool = True,
        tsn: int | t.uint8_t | None = None,
        **kwargs: Any,
    ):
        """Override the default Cluster command."""
        if manufacturer is None:
            manufacturer = self.endpoint.device.manufacturer
        _LOGGER.debug(
            "%s Sending Tuya Cluster Command.. Manufacturer is %s Cluster Command is 0x%04x, Arguments are %s",
            self.endpoint.device.ieee,
            manufacturer,
            command_id,
            args,
        )
        # Open Close or Stop commands
        tuya_payload = TuyaManufCluster.Command()
        if command_id in (
            WINDOW_COVER_COMMAND_UPOPEN,
            WINDOW_COVER_COMMAND_DOWNCLOSE,
            WINDOW_COVER_COMMAND_STOP,
        ):
            tuya_payload.status = 0
            tuya_payload.tsn = tsn if tsn else 0
            tuya_payload.command_id = TUYA_DP_TYPE_ENUM + TUYA_DP_ID_CONTROL
            tuya_payload.function = 0
            tuya_payload.data = [
                1,
                # need to implement direction change
                self.endpoint.device.tuya_cover_command[command_id],
            ]  # remap the command to the Tuya command
        # Set Position Command
        elif command_id == WINDOW_COVER_COMMAND_LIFTPERCENT:
            tuya_payload.status = 0
            tuya_payload.tsn = tsn if tsn else 0
            tuya_payload.command_id = TUYA_DP_TYPE_VALUE + TUYA_DP_ID_PERCENT_CONTROL
            tuya_payload.function = 0
            """Check direction and correct value"""
            invert_attr = self._attr_cache.get(ATTR_COVER_INVERTED) == 1
            invert = (
                not invert_attr
                if self.endpoint.device.tuya_cover_inverted_by_default
                else invert_attr
            )
            position = args[0] if invert else 100 - args[0]
            tuya_payload.data = [
                4,
                0,
                0,
                0,
                position,
            ]
        # Custom Command
        elif command_id == WINDOW_COVER_COMMAND_CUSTOM:
            tuya_payload.status = args[0]
            tuya_payload.tsn = args[1]
            tuya_payload.command_id = args[2]
            tuya_payload.function = args[3]
            tuya_payload.data = args[4]
        else:
            tuya_payload = None
        # Send the command
        if tuya_payload.command_id:
            _LOGGER.debug(
                "%s Sending Tuya Command. Paylod values [endpoint_id : %s, "
                "Status : %s, TSN: %s, Command: 0x%04x, Function: %s, Data: %s]",
                self.endpoint.device.ieee,
                self.endpoint.endpoint_id,
                tuya_payload.status,
                tuya_payload.tsn,
                tuya_payload.command_id,
                tuya_payload.function,
                tuya_payload.data,
            )

            return self.endpoint.tuya_manufacturer.command(
                TUYA_SET_DATA, tuya_payload, expect_reply=True
            )
        else:
            _LOGGER.debug("Unrecognised command: %x", command_id)
            return foundation.Status.UNSUP_CLUSTER_COMMAND


class TuyaWindowCover(CustomDevice):
    """Tuya Window cover device."""

    # For most tuya devices 0 = Up/Open, 1 = Stop, 2 = Down/Close
    tuya_cover_command = {0x0000: 0x0000, 0x0001: 0x0002, 0x0002: 0x0001}

    # For all covers which need their position inverted by default
    # Default (False) is 100 = open, 0 = closed; When True use 0 = open, 100 = closed instead
    # Don't invert _TZE200_cowvfni3: https://github.com/Koenkk/zigbee2mqtt/issues/6043
    tuya_cover_inverted_by_default = False

    def __init__(self, *args, **kwargs):
        """Init device."""
        self.cover_bus = Bus()
        super().__init__(*args, **kwargs)


class TuyaManufacturerLevelControl(TuyaManufCluster):
    """Manufacturer Specific Cluster for cover device."""

    def handle_cluster_request(
        self,
        hdr: foundation.ZCLHeader,
        args: list[Any],
        *,
        dst_addressing: AddressingMode | None = None,
    ) -> None:
        """Handle cluster request."""
        tuya_payload = args[0]

        _LOGGER.debug(
            "%s Received Attribute Report. Command is %x, Tuya Paylod values"
            "[Status : %s, TSN: %s, Command: %s, Function: %s, Data: %s]",
            self.endpoint.device.ieee,
            hdr.command_id,
            tuya_payload.status,
            tuya_payload.tsn,
            tuya_payload.command_id,
            tuya_payload.function,
            tuya_payload.data,
        )

        if hdr.command_id in (0x0002, 0x0001):
            if tuya_payload.command_id == TUYA_LEVEL_COMMAND:
                self.endpoint.device.dimmer_bus.listener_event(
                    LEVEL_EVENT,
                    tuya_payload.command_id,
                    tuya_payload.data,
                )
            else:
                self.endpoint.device.switch_bus.listener_event(
                    SWITCH_EVENT,
                    tuya_payload.command_id - TUYA_CMD_BASE,
                    tuya_payload.data[1],
                )


class TuyaLevelControl(CustomCluster, LevelControl):
    """Tuya Level cluster for dimmable device."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self.endpoint.device.dimmer_bus.add_listener(self)

    def level_event(self, channel, state):
        """Level event."""
        level = (((state[3] << 8) + state[4]) * 255) // 1000
        _LOGGER.debug(
            "%s - Received level event message, channel: %d, level: %d, data: %d",
            self.endpoint.device.ieee,
            channel,
            level,
            state,
        )
        self._update_attribute(self.attributes_by_name["current_level"].id, level)

    def command(
        self,
        command_id: foundation.GeneralCommand | int | t.uint8_t,
        *args,
        manufacturer: int | t.uint16_t | None = None,
        expect_reply: bool = True,
        tsn: int | t.uint8_t | None = None,
        **kwargs: Any,
    ):
        """Override the default Cluster command."""
        _LOGGER.debug(
            "%s Sending Tuya Cluster Command.. Cluster Command is %x, Arguments are %s, %s",
            self.endpoint.device.ieee,
            command_id,
            args,
            kwargs,
        )
        # Move to level
        # move_to_level_with_on_off
        if command_id in (0x0000, 0x0001, 0x0004):
            cmd_payload = TuyaManufCluster.Command()
            cmd_payload.status = 0
            cmd_payload.tsn = 0
            cmd_payload.command_id = TUYA_LEVEL_COMMAND
            cmd_payload.function = 0

            if kwargs and "level" in kwargs:
                level = kwargs["level"]
            elif args:
                level = args[0]
            else:
                level = 0
            brightness = (level * 1000) // 255
            val1 = brightness >> 8
            val2 = brightness & 0xFF
            cmd_payload.data = [4, 0, 0, val1, val2]  # Custom Command

            return self.endpoint.tuya_manufacturer.command(
                TUYA_SET_DATA, cmd_payload, expect_reply=True
            )

        return foundation.Status.UNSUP_CLUSTER_COMMAND


@dataclasses.dataclass
class DPToAttributeMapping:
    """Container for datapoint to cluster attribute update mapping."""

    ep_attribute: str
    attribute_name: str | tuple[str, ...]
    converter: Callable[[Any], Any] | None = None
    endpoint_id: int | None = None


@dataclasses.dataclass
class AttributeWithMask:
    """Container for the attribute and its mask."""

    value: Any
    mask: int


class TuyaNewManufCluster(CustomCluster):
    """Tuya manufacturer specific cluster.

    This is an attempt to consolidate the multiple above clusters into a
    single framework. Instead of overriding the handle_cluster_request()
    method, implement handlers for commands, like get_data, set_data_response,
    set_time_request, etc.
    """

    name: str = "Tuya Manufacturer Specific"
    cluster_id: t.uint16_t = TUYA_CLUSTER_ID
    ep_attribute: str = "tuya_manufacturer"

    # command for writing datapoint values to the device, some use TUYA_SEND_DATA
    mcu_write_command: foundation.GeneralCommand | int | t.uint8_t = TUYA_SET_DATA

    # remove manufacturer id for cluster, important for `TUYA_SET_DATA` commands
    manufacturer_id_override: t.uint16_t = foundation.ZCLHeader.NO_MANUFACTURER_ID

    class AttributeDefs(BaseAttributeDefs):
        """Attribute Definitions."""

    server_commands = {
        TUYA_QUERY_DATA: foundation.ZCLCommandDef(
            "query_data", {}, False, is_manufacturer_specific=True
        ),
        TUYA_SET_DATA: foundation.ZCLCommandDef(
            "set_data", {"data": TuyaCommand}, False, is_manufacturer_specific=True
        ),
        TUYA_SEND_DATA: foundation.ZCLCommandDef(
            "send_data", {"data": TuyaCommand}, False, is_manufacturer_specific=True
        ),
        TUYA_SET_TIME: foundation.ZCLCommandDef(
            "set_time", {"time": TuyaTimePayload}, False, is_manufacturer_specific=True
        ),
    }

    client_commands = {
        TUYA_GET_DATA: foundation.ZCLCommandDef(
            "get_data", {"data": TuyaCommand}, True, is_manufacturer_specific=True
        ),
        TUYA_SET_DATA_RESPONSE: foundation.ZCLCommandDef(
            "set_data_response",
            {"data": TuyaCommand},
            True,
            is_manufacturer_specific=True,
        ),
        TUYA_ACTIVE_STATUS_RPT: foundation.ZCLCommandDef(
            "active_status_report",
            {"data": TuyaCommand},
            True,
            is_manufacturer_specific=True,
        ),
        TUYA_SET_TIME: foundation.ZCLCommandDef(
            "set_time_request", {"data": t.data16}, True, is_manufacturer_specific=True
        ),
    }

    dp_to_attribute: dict[int, DPToAttributeMapping | list[DPToAttributeMapping]] = {}
    data_point_handlers: dict[int, str] = {}

    def __init__(self, *args, **kwargs):
        """Initialize the cluster and mark attributes as valid on LocalDataClusters."""
        super().__init__(*args, **kwargs)

        self._dp_to_attributes: dict[int, list[DPToAttributeMapping]] = {
            dp: attr if isinstance(attr, list) else [attr]
            for dp, attr in self.dp_to_attribute.items()
        }
        for dp_map in self._dp_to_attributes.values():
            # get the endpoint that is being mapped to
            endpoint = self.endpoint
            for mapped_attr in dp_map:
                if mapped_attr.endpoint_id:
                    endpoint = self.endpoint.device.endpoints.get(
                        mapped_attr.endpoint_id
                    )

                # the endpoint to be mapped to might not actually exist within all quirks
                if not endpoint:
                    continue

                cluster = getattr(endpoint, mapped_attr.ep_attribute, None)
                # the cluster to be mapped to might not actually exist within all quirks
                if not cluster:
                    continue

                # mark mapped to attribute as valid if existing and if on a LocalDataCluster
                attr = cluster.attributes_by_name.get(mapped_attr.attribute_name)
                if attr and isinstance(cluster, LocalDataCluster):
                    # _VALID_ATTRIBUTES is only a class variable, but as want to modify it
                    # per instance here, we need to create an instance variable first
                    if "_VALID_ATTRIBUTES" not in cluster.__dict__:
                        cluster._VALID_ATTRIBUTES = set()
                    cluster._VALID_ATTRIBUTES.add(attr.id)

    def handle_cluster_request(
        self,
        hdr: foundation.ZCLHeader,
        args: list[Any],
        *,
        dst_addressing: AddressingMode | None = None,
    ) -> None:
        """Handle cluster specific request."""

        try:
            if hdr.direction == foundation.Direction.Server_to_Client:
                # server_cluster -> client_cluster cluster specific command
                handler_name = f"handle_{self.client_commands[hdr.command_id].name}"
            else:
                handler_name = f"handle_{self.server_commands[hdr.command_id].name}"
        except KeyError:
            self.debug(
                "Received unknown manufacturer command %s: %s", hdr.command_id, args
            )
            if not hdr.frame_control.disable_default_response:
                self.send_default_rsp(
                    hdr, status=foundation.Status.UNSUP_CLUSTER_COMMAND
                )
                return

        try:
            status = getattr(self, handler_name)(*args)
        except AttributeError:
            self.warning(
                "No '%s' tuya handler found for %s",
                handler_name,
                args,
            )
            status = foundation.Status.UNSUP_CLUSTER_COMMAND

        if not hdr.frame_control.disable_default_response:
            self.send_default_rsp(hdr, status=status)

    def handle_get_data(self, command: TuyaCommand) -> foundation.Status:
        """Handle get_data response (report)."""
        dp_error = False
        for record in command.datapoints:
            try:
                dp_handler = self.data_point_handlers[record.dp]
                getattr(self, dp_handler)(record)
            except (AttributeError, KeyError):
                self.debug("No datapoint handler for %s", record)
                dp_error = True
                # return foundation.Status.UNSUPPORTED_ATTRIBUTE

        _LOGGER.debug(
            "[0x%04x:%s:0x%04x] Received value %s for attribute 0x%04x",
            self.endpoint.device.nwk,
            self.endpoint.endpoint_id,
            self.cluster_id,
            record.data.payload,
            record.dp,
        )

        return (
            foundation.Status.SUCCESS
            if not dp_error
            else foundation.Status.UNSUPPORTED_ATTRIBUTE
        )

    handle_set_data_response = handle_get_data
    handle_active_status_report = handle_get_data

    def handle_set_time_request(self, payload: t.uint16_t) -> foundation.Status:
        """Handle Time set request."""
        return foundation.Status.SUCCESS

    def _dp_2_attr_update(self, datapoint: TuyaDatapointData) -> None:
        """Handle data point to attribute report conversion."""
        try:
            dp_map = self._dp_to_attributes[datapoint.dp]
        except KeyError:
            self.debug("No attribute mapping for %s data point", datapoint.dp)
            return

        endpoint = self.endpoint
        for mapped_attr in dp_map:
            if mapped_attr.endpoint_id:
                endpoint = self.endpoint.device.endpoints[mapped_attr.endpoint_id]
            cluster = getattr(endpoint, mapped_attr.ep_attribute)
            value = datapoint.data.payload
            if mapped_attr.converter:
                value = mapped_attr.converter(value)

            if isinstance(mapped_attr.attribute_name, tuple):
                for k, v in zip(mapped_attr.attribute_name, value):
                    if isinstance(v, AttributeWithMask):
                        v = cluster.get(k, 0) & (~v.mask) | v.value
                    cluster.update_attribute(k, v)
            else:
                if isinstance(value, AttributeWithMask):
                    value = (
                        cluster.get(mapped_attr.attribute_name, 0) & (~value.mask)
                        | value.value
                    )
                cluster.update_attribute(mapped_attr.attribute_name, value)
