"""Module for UART communication to the device."""

import asyncio
import logging
from typing import Any, Dict

import zigpy.config
import zigpy.serial

LOGGER = logging.getLogger(__name__)


class Gateway(zigpy.serial.SerialProtocol):
    """Class implementing the UART protocol."""

    START = b"\x7E"
    ESCAPE = b"\x7D"
    XON = b"\x11"
    XOFF = b"\x13"

    RESERVED = START + ESCAPE + XON + XOFF
    THIS_ONE = True

    def __init__(self, api):
        """Initialize instance."""
        super().__init__()
        self._api = api
        self._in_command_mode = False

    def send(self, data):
        """Send data, taking care of escaping and framing."""
        LOGGER.debug("Sending: %s", data)
        checksum = bytes([self._checksum(data)])
        frame = self.START + self._escape(
            len(data).to_bytes(2, "big") + data + checksum
        )
        self._transport.write(frame)

    @property
    def baudrate(self):
        """Baudrate."""
        return self._transport.serial.baudrate

    @baudrate.setter
    def baudrate(self, baudrate):
        """Set baudrate."""
        if baudrate in self._transport.serial.BAUDRATES:
            self._transport.serial.baudrate = baudrate
        else:
            raise ValueError(
                f"baudrate must be one of {self._transport.serial.BAUDRATES}"
            )

    def connection_lost(self, exc) -> None:
        """Port was closed expectedly or unexpectedly."""
        super().connection_lost(exc)

        if self._api is not None:
            self._api.connection_lost(exc)

    def command_mode_rsp(self, data):
        """Handle AT command mode response."""
        data = data.decode("ascii", "ignore")
        LOGGER.debug("Handling AT command mode response: %s", data)
        self._api.handle_command_mode_rsp(data)

    def command_mode_send(self, data):
        """Send data in command mode."""
        LOGGER.debug("Command mode sending %s to uart", data)
        self._in_command_mode = True
        self._transport.write(data)

    def data_received(self, data):
        """Handle data received from the UART callback."""
        super().data_received(data)
        while self._buffer:
            frame = self._extract_frame()
            if frame is None:
                break
            self.frame_received(frame)
        if self._in_command_mode and self._buffer[-1:] == b"\r":
            rsp = self._buffer[:-1]
            self._buffer.clear()
            self.command_mode_rsp(rsp)

    def frame_received(self, frame):
        """Frame receive handler."""
        LOGGER.debug("Frame received: %s", frame)
        self._api.frame_received(frame)

    def reset_command_mode(self):
        r"""Reset command mode and ignore '\r' character as command mode response."""
        self._in_command_mode = False

    def _extract_frame(self):
        first_start = self._buffer.find(self.START)
        if first_start < 0:
            return None

        data = self._buffer[first_start + 1 :]
        frame_len, data = self._get_unescaped(data, 2)
        if frame_len is None:
            return None

        frame_len = int.from_bytes(frame_len, "big")
        frame, data = self._get_unescaped(data, frame_len)
        if frame is None:
            return None
        checksum, data = self._get_unescaped(data, 1)
        if checksum is None:
            return None
        if self._checksum(frame) != checksum[0]:
            # TODO: Signal decode failure so that error frame can be sent
            self._buffer = data
            return None

        self._buffer = data
        return frame

    def _get_unescaped(self, data, n):
        ret = []
        idx = 0
        while len(ret) < n and idx < len(data):
            b = data[idx]
            if b == self.ESCAPE[0]:
                idx += 1
                if idx >= len(data):
                    return None, None
                b = data[idx] ^ 0x020
            ret.append(b)
            idx += 1

        if len(ret) >= n:
            return bytes(ret), data[idx:]
        return None, None

    def _escape(self, data):
        ret = []
        for b in data:
            if b in self.RESERVED:
                ret.append(ord(self.ESCAPE))
                ret.append(b ^ 0x20)
            else:
                ret.append(b)
        return bytes(ret)

    def _checksum(self, data):
        return 0xFF - (sum(data) % 0x100)


async def connect(device_config: Dict[str, Any], api) -> Gateway:
    """Connect to the device."""
    transport, protocol = await zigpy.serial.create_serial_connection(
        loop=asyncio.get_running_loop(),
        protocol_factory=lambda: Gateway(api),
        url=device_config[zigpy.config.CONF_DEVICE_PATH],
        baudrate=device_config[zigpy.config.CONF_DEVICE_BAUDRATE],
        xonxoff=device_config[zigpy.config.CONF_DEVICE_BAUDRATE],
    )

    await protocol.wait_until_connected()

    return protocol
