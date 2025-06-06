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


class IsisL3SimulatedTopologyConfig(Base):
    """ISIS-L3 Simulated Topology Configuration
    The IsisL3SimulatedTopologyConfig class encapsulates a list of isisL3SimulatedTopologyConfig resources that are managed by the system.
    A list of resources can be retrieved from the server using the IsisL3SimulatedTopologyConfig.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "isisL3SimulatedTopologyConfig"
    _SDM_ATT_MAP = {
        "Active": "active",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EnableHostName": "enableHostName",
        "HostName": "hostName",
        "IsisL3Ipv4NodeRouteCount": "isisL3Ipv4NodeRouteCount",
        "IsisL3Ipv6NodeRouteCount": "isisL3Ipv6NodeRouteCount",
        "Name": "name",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(IsisL3SimulatedTopologyConfig, self).__init__(parent, list_op)

    @property
    def IsisL3ipv4NodeRouteList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3ipv4noderoutelist_ae7695e0538209b004b305811ac652f1.IsisL3ipv4NodeRouteList): An instance of the IsisL3ipv4NodeRouteList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3ipv4noderoutelist_ae7695e0538209b004b305811ac652f1 import (
            IsisL3ipv4NodeRouteList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisL3ipv4NodeRouteList", None) is not None:
                return self._properties.get("IsisL3ipv4NodeRouteList")
        return IsisL3ipv4NodeRouteList(self)._select()

    @property
    def IsisL3ipv6NodeRouteList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3ipv6noderoutelist_305cdb4f4026728819c2e41364d4f782.IsisL3ipv6NodeRouteList): An instance of the IsisL3ipv6NodeRouteList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3ipv6noderoutelist_305cdb4f4026728819c2e41364d4f782 import (
            IsisL3ipv6NodeRouteList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisL3ipv6NodeRouteList", None) is not None:
                return self._properties.get("IsisL3ipv6NodeRouteList")
        return IsisL3ipv6NodeRouteList(self)._select()

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def EnableHostName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Host Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableHostName"])
        )

    @property
    def HostName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Host Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HostName"]))

    @property
    def IsisL3Ipv4NodeRouteCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Node Route Range Count(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsisL3Ipv4NodeRouteCount"])

    @IsisL3Ipv4NodeRouteCount.setter
    def IsisL3Ipv4NodeRouteCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsisL3Ipv4NodeRouteCount"], value)

    @property
    def IsisL3Ipv6NodeRouteCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Node Route Range Count(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsisL3Ipv6NodeRouteCount"])

    @IsisL3Ipv6NodeRouteCount.setter
    def IsisL3Ipv6NodeRouteCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IsisL3Ipv6NodeRouteCount"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    def update(
        self, IsisL3Ipv4NodeRouteCount=None, IsisL3Ipv6NodeRouteCount=None, Name=None
    ):
        # type: (int, int, str) -> IsisL3SimulatedTopologyConfig
        """Updates isisL3SimulatedTopologyConfig resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - IsisL3Ipv4NodeRouteCount (number): Node Route Range Count(multiplier)
        - IsisL3Ipv6NodeRouteCount (number): Node Route Range Count(multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self, IsisL3Ipv4NodeRouteCount=None, IsisL3Ipv6NodeRouteCount=None, Name=None
    ):
        # type: (int, int, str) -> IsisL3SimulatedTopologyConfig
        """Adds a new isisL3SimulatedTopologyConfig resource on the json, only valid with batch add utility

        Args
        ----
        - IsisL3Ipv4NodeRouteCount (number): Node Route Range Count(multiplier)
        - IsisL3Ipv6NodeRouteCount (number): Node Route Range Count(multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with all currently retrieved isisL3SimulatedTopologyConfig resources using find and the newly added isisL3SimulatedTopologyConfig resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        IsisL3Ipv4NodeRouteCount=None,
        IsisL3Ipv6NodeRouteCount=None,
        Name=None,
    ):
        # type: (int, str, int, int, str) -> IsisL3SimulatedTopologyConfig
        """Finds and retrieves isisL3SimulatedTopologyConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve isisL3SimulatedTopologyConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all isisL3SimulatedTopologyConfig resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - IsisL3Ipv4NodeRouteCount (number): Node Route Range Count(multiplier)
        - IsisL3Ipv6NodeRouteCount (number): Node Route Range Count(multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching isisL3SimulatedTopologyConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of isisL3SimulatedTopologyConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the isisL3SimulatedTopologyConfig resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("abort", payload=payload, response_object=None)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, Arg3=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (bool):
        - Arg3 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def PerformActionOnAllObjects(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the performActionOnAllObjects operation on the server.

        Action on All Objects

        performActionOnAllObjects(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------------
        - Arg2 (str): Action Name
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "performActionOnAllObjects", payload=payload, response_object=None
        )

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=list, async_operation=bool)
        -----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=string, async_operation=bool)
        -------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def get_device_ids(
        self, PortNames=None, Active=None, EnableHostName=None, HostName=None
    ):
        """Base class infrastructure that gets a list of isisL3SimulatedTopologyConfig device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - EnableHostName (str): optional regex of enableHostName
        - HostName (str): optional regex of hostName

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
