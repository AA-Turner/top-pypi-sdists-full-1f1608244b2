# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class TransmissionControl(Base):
    """This object provides different options for Transmission Control.
    The TransmissionControl class encapsulates a required transmissionControl resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "transmissionControl"
    _SDM_ATT_MAP = {
        "BurstDuration": "burstDuration",
        "BurstModeUnits": "burstModeUnits",
        "BurstPacketCount": "burstPacketCount",
        "Duration": "duration",
        "EnableInterBurstGap": "enableInterBurstGap",
        "EnableInterStreamGap": "enableInterStreamGap",
        "FrameCount": "frameCount",
        "InterBurstGap": "interBurstGap",
        "InterBurstGapUnits": "interBurstGapUnits",
        "InterStreamGap": "interStreamGap",
        "InterStreamGapUnits": "interStreamGapUnits",
        "IterationCount": "iterationCount",
        "MinGapBytes": "minGapBytes",
        "RepeatBurst": "repeatBurst",
        "StartDelay": "startDelay",
        "StartDelayUnits": "startDelayUnits",
        "Type": "type",
    }
    _SDM_ENUM_MAP = {
        "burstModeUnits": [
            "bytes",
            "microseconds",
            "milliseconds",
            "nanoseconds",
            "packetCount",
            "seconds",
        ],
        "interBurstGapUnits": [
            "bytes",
            "microseconds",
            "milliseconds",
            "nanoseconds",
            "seconds",
        ],
        "interStreamGapUnits": [
            "bytes",
            "microseconds",
            "milliseconds",
            "nanoseconds",
            "seconds",
        ],
        "startDelayUnits": [
            "bytes",
            "microseconds",
            "milliseconds",
            "nanoseconds",
            "seconds",
        ],
        "type": [
            "auto",
            "burstFixedDuration",
            "continuous",
            "custom",
            "fixedDuration",
            "fixedFrameCount",
            "fixedIterationCount",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(TransmissionControl, self).__init__(parent, list_op)

    @property
    def BurstDuration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the duration of the burst. Use this attribute when configuring burst as a duration instead of packet count.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BurstDuration"])

    @BurstDuration.setter
    def BurstDuration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BurstDuration"], value)

    @property
    def BurstModeUnits(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bytes | microseconds | milliseconds | nanoseconds | packetCount | seconds): Specifies unit of Burst, whether it is packet count or a duration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BurstModeUnits"])

    @BurstModeUnits.setter
    def BurstModeUnits(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["BurstModeUnits"], value)

    @property
    def BurstPacketCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the number of packets per burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BurstPacketCount"])

    @BurstPacketCount.setter
    def BurstPacketCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BurstPacketCount"], value)

    @property
    def Duration(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the time duration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Duration"])

    @Duration.setter
    def Duration(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Duration"], value)

    @property
    def EnableInterBurstGap(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the inter-burst gap of a frame.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableInterBurstGap"])

    @EnableInterBurstGap.setter
    def EnableInterBurstGap(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableInterBurstGap"], value)

    @property
    def EnableInterStreamGap(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the inter-stream gap of a frame.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableInterStreamGap"])

    @EnableInterStreamGap.setter
    def EnableInterStreamGap(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableInterStreamGap"], value)

    @property
    def FrameCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies Fixed Packet Count when Transmission Mode is Interleaved.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FrameCount"])

    @FrameCount.setter
    def FrameCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FrameCount"], value)

    @property
    def InterBurstGap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the gap between any two consecutive burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterBurstGap"])

    @InterBurstGap.setter
    def InterBurstGap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterBurstGap"], value)

    @property
    def InterBurstGapUnits(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bytes | microseconds | milliseconds | nanoseconds | seconds): Specifies unit of Inter Burst Gap either in bytes or nanoseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterBurstGapUnits"])

    @InterBurstGapUnits.setter
    def InterBurstGapUnits(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterBurstGapUnits"], value)

    @property
    def InterStreamGap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the gap between any two consecutive Flow Groups when Transmission Mode is Sequential.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterStreamGap"])

    @InterStreamGap.setter
    def InterStreamGap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterStreamGap"], value)

    @property
    def InterStreamGapUnits(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bytes | microseconds | milliseconds | nanoseconds | seconds): Specifies unit of Inter Stream Gap either in bytes or nanoseconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterStreamGapUnits"])

    @InterStreamGapUnits.setter
    def InterStreamGapUnits(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterStreamGapUnits"], value)

    @property
    def IterationCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the number of iterations the Flow Group can have when Transmission Mode is Interleaved.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IterationCount"])

    @IterationCount.setter
    def IterationCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IterationCount"], value)

    @property
    def MinGapBytes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the minimum gap between any 2 packets or frames in term of bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MinGapBytes"])

    @MinGapBytes.setter
    def MinGapBytes(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MinGapBytes"], value)

    @property
    def RepeatBurst(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies number of times a burst can be repeated when Transmission Mode is Sequential.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RepeatBurst"])

    @RepeatBurst.setter
    def RepeatBurst(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RepeatBurst"], value)

    @property
    def StartDelay(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the delay in Start when Transmission Mode is Interleaved.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartDelay"])

    @StartDelay.setter
    def StartDelay(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartDelay"], value)

    @property
    def StartDelayUnits(self):
        # type: () -> str
        """
        Returns
        -------
        - str(bytes | microseconds | milliseconds | nanoseconds | seconds): Specifies the unit for Delay in Start when Transmission Mode is Interleaved.
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartDelayUnits"])

    @StartDelayUnits.setter
    def StartDelayUnits(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartDelayUnits"], value)

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str(auto | burstFixedDuration | continuous | custom | fixedDuration | fixedFrameCount | fixedIterationCount): The Transmission Control types.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Type"])

    @Type.setter
    def Type(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Type"], value)

    def update(
        self,
        BurstDuration=None,
        BurstModeUnits=None,
        BurstPacketCount=None,
        Duration=None,
        EnableInterBurstGap=None,
        EnableInterStreamGap=None,
        FrameCount=None,
        InterBurstGap=None,
        InterBurstGapUnits=None,
        InterStreamGap=None,
        InterStreamGapUnits=None,
        IterationCount=None,
        MinGapBytes=None,
        RepeatBurst=None,
        StartDelay=None,
        StartDelayUnits=None,
        Type=None,
    ):
        # type: (int, str, int, int, bool, bool, int, int, str, int, str, int, int, int, int, str, str) -> TransmissionControl
        """Updates transmissionControl resource on the server.

        Args
        ----
        - BurstDuration (number): Indicates the duration of the burst. Use this attribute when configuring burst as a duration instead of packet count.
        - BurstModeUnits (str(bytes | microseconds | milliseconds | nanoseconds | packetCount | seconds)): Specifies unit of Burst, whether it is packet count or a duration.
        - BurstPacketCount (number): Specifies the number of packets per burst.
        - Duration (number): Indicates the time duration.
        - EnableInterBurstGap (bool): Enables the inter-burst gap of a frame.
        - EnableInterStreamGap (bool): Enables the inter-stream gap of a frame.
        - FrameCount (number): Specifies Fixed Packet Count when Transmission Mode is Interleaved.
        - InterBurstGap (number): Specifies the gap between any two consecutive burst.
        - InterBurstGapUnits (str(bytes | microseconds | milliseconds | nanoseconds | seconds)): Specifies unit of Inter Burst Gap either in bytes or nanoseconds.
        - InterStreamGap (number): Specifies the gap between any two consecutive Flow Groups when Transmission Mode is Sequential.
        - InterStreamGapUnits (str(bytes | microseconds | milliseconds | nanoseconds | seconds)): Specifies unit of Inter Stream Gap either in bytes or nanoseconds.
        - IterationCount (number): Specifies the number of iterations the Flow Group can have when Transmission Mode is Interleaved.
        - MinGapBytes (number): Specifies the minimum gap between any 2 packets or frames in term of bytes.
        - RepeatBurst (number): Specifies number of times a burst can be repeated when Transmission Mode is Sequential.
        - StartDelay (number): Specifies the delay in Start when Transmission Mode is Interleaved.
        - StartDelayUnits (str(bytes | microseconds | milliseconds | nanoseconds | seconds)): Specifies the unit for Delay in Start when Transmission Mode is Interleaved.
        - Type (str(auto | burstFixedDuration | continuous | custom | fixedDuration | fixedFrameCount | fixedIterationCount)): The Transmission Control types.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BurstDuration=None,
        BurstModeUnits=None,
        BurstPacketCount=None,
        Duration=None,
        EnableInterBurstGap=None,
        EnableInterStreamGap=None,
        FrameCount=None,
        InterBurstGap=None,
        InterBurstGapUnits=None,
        InterStreamGap=None,
        InterStreamGapUnits=None,
        IterationCount=None,
        MinGapBytes=None,
        RepeatBurst=None,
        StartDelay=None,
        StartDelayUnits=None,
        Type=None,
    ):
        # type: (int, str, int, int, bool, bool, int, int, str, int, str, int, int, int, int, str, str) -> TransmissionControl
        """Finds and retrieves transmissionControl resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve transmissionControl resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all transmissionControl resources from the server.

        Args
        ----
        - BurstDuration (number): Indicates the duration of the burst. Use this attribute when configuring burst as a duration instead of packet count.
        - BurstModeUnits (str(bytes | microseconds | milliseconds | nanoseconds | packetCount | seconds)): Specifies unit of Burst, whether it is packet count or a duration.
        - BurstPacketCount (number): Specifies the number of packets per burst.
        - Duration (number): Indicates the time duration.
        - EnableInterBurstGap (bool): Enables the inter-burst gap of a frame.
        - EnableInterStreamGap (bool): Enables the inter-stream gap of a frame.
        - FrameCount (number): Specifies Fixed Packet Count when Transmission Mode is Interleaved.
        - InterBurstGap (number): Specifies the gap between any two consecutive burst.
        - InterBurstGapUnits (str(bytes | microseconds | milliseconds | nanoseconds | seconds)): Specifies unit of Inter Burst Gap either in bytes or nanoseconds.
        - InterStreamGap (number): Specifies the gap between any two consecutive Flow Groups when Transmission Mode is Sequential.
        - InterStreamGapUnits (str(bytes | microseconds | milliseconds | nanoseconds | seconds)): Specifies unit of Inter Stream Gap either in bytes or nanoseconds.
        - IterationCount (number): Specifies the number of iterations the Flow Group can have when Transmission Mode is Interleaved.
        - MinGapBytes (number): Specifies the minimum gap between any 2 packets or frames in term of bytes.
        - RepeatBurst (number): Specifies number of times a burst can be repeated when Transmission Mode is Sequential.
        - StartDelay (number): Specifies the delay in Start when Transmission Mode is Interleaved.
        - StartDelayUnits (str(bytes | microseconds | milliseconds | nanoseconds | seconds)): Specifies the unit for Delay in Start when Transmission Mode is Interleaved.
        - Type (str(auto | burstFixedDuration | continuous | custom | fixedDuration | fixedFrameCount | fixedIterationCount)): The Transmission Control types.

        Returns
        -------
        - self: This instance with matching transmissionControl resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of transmissionControl data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the transmissionControl resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
