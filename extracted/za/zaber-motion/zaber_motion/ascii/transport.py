﻿# ===== THIS FILE IS GENERATED FROM A TEMPLATE ===== #
# ============== DO NOT EDIT DIRECTLY ============== #

from typing import Any

from ..call import call, call_async, call_sync

from ..dto import requests as dto


class Transport:
    """
    Connection transport backend allowing to carry Zaber ASCII protocol over arbitrary protocols.
    Can only be used with a single connection.
    """

    @property
    def transport_id(self) -> int:
        """
        The transport ID identifies this transport instance with the underlying library.
        """
        return self._transport_id

    def __init__(self, transport_id: int):
        self._transport_id = transport_id

    @staticmethod
    def open() -> 'Transport':
        """
        Creates new instance allowing to read/write messages from/to a single connection.

        Returns:
            New instance of transport.
        """
        request = dto.EmptyRequest(
        )
        response = call_sync(
            "custom/interface/open",
            request,
            dto.CustomInterfaceOpenResponse.from_binary)
        return Transport(response.transport_id)

    def close(
            self
    ) -> None:
        """
        Closes the transport.
        Also closes the connection using the transport.
        """
        request = dto.CustomInterfaceCloseRequest(
            transport_id=self.transport_id,
        )
        call("custom/interface/close", request)

    async def close_async(
            self
    ) -> None:
        """
        Closes the transport.
        Also closes the connection using the transport.
        """
        request = dto.CustomInterfaceCloseRequest(
            transport_id=self.transport_id,
        )
        await call_async("custom/interface/close", request)

    @staticmethod
    def __free(
            transport_id: int
    ) -> None:
        """
        Frees the transport instance.

        Args:
            transport_id: Transport ID to be freed.
        """
        request = dto.CustomInterfaceCloseRequest(
            transport_id=transport_id,
        )
        call_sync("custom/interface/free", request)

    def close_with_error(
            self,
            error_message: str
    ) -> None:
        """
        Closes the transport with error.
        Also closes the connection using the transport propagating the error.

        Args:
            error_message: Error to be propagated.
        """
        request = dto.CustomInterfaceCloseRequest(
            transport_id=self.transport_id,
            error_message=error_message,
        )
        call("custom/interface/close", request)

    async def close_with_error_async(
            self,
            error_message: str
    ) -> None:
        """
        Closes the transport with error.
        Also closes the connection using the transport propagating the error.

        Args:
            error_message: Error to be propagated.
        """
        request = dto.CustomInterfaceCloseRequest(
            transport_id=self.transport_id,
            error_message=error_message,
        )
        await call_async("custom/interface/close", request)

    def write(
            self,
            message: str
    ) -> None:
        """
        Writes a single message to the connection.
        The message will be processed as a reply from the device.

        Args:
            message: Single message of Zaber ASCII protocol.
        """
        request = dto.CustomInterfaceWriteRequest(
            transport_id=self.transport_id,
            message=message,
        )
        call("custom/interface/write", request)

    async def write_async(
            self,
            message: str
    ) -> None:
        """
        Writes a single message to the connection.
        The message will be processed as a reply from the device.

        Args:
            message: Single message of Zaber ASCII protocol.
        """
        request = dto.CustomInterfaceWriteRequest(
            transport_id=self.transport_id,
            message=message,
        )
        await call_async("custom/interface/write", request)

    def read(
            self
    ) -> str:
        """
        Reads a single message generated by the connection.
        The message is a request for the device.
        Read should be called continuously in a loop to ensure all generated messages are processed.
        Subsequent read call confirms that previous message was delivered to the device.

        Returns:
            Message generated by the connection.
        """
        request = dto.CustomInterfaceReadRequest(
            transport_id=self.transport_id,
        )
        response = call(
            "custom/interface/read",
            request,
            dto.StringResponse.from_binary)
        return response.value

    async def read_async(
            self
    ) -> str:
        """
        Reads a single message generated by the connection.
        The message is a request for the device.
        Read should be called continuously in a loop to ensure all generated messages are processed.
        Subsequent read call confirms that previous message was delivered to the device.

        Returns:
            Message generated by the connection.
        """
        request = dto.CustomInterfaceReadRequest(
            transport_id=self.transport_id,
        )
        response = await call_async(
            "custom/interface/read",
            request,
            dto.StringResponse.from_binary)
        return response.value

    def __enter__(self) -> 'Transport':
        """ __enter__ """
        return self

    def __exit__(self, _type: Any, _value: Any, _traceback: Any) -> None:
        """ __exit__ """
        self.close()

    def __del__(self) -> None:
        """ __del__ """
        Transport.__free(self.transport_id)
