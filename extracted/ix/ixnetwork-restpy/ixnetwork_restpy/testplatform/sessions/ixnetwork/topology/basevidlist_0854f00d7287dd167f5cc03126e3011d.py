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


class BaseVidList(Base):
    """ISIS SPB Node BaseVID Configuration
    The BaseVidList class encapsulates a required baseVidList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "baseVidList"
    _SDM_ATT_MAP = {
        "Active": "active",
        "BaseVid": "baseVid",
        "BaseVlanPriority": "baseVlanPriority",
        "BvlanTpid": "bvlanTpid",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EctAlgorithm": "ectAlgorithm",
        "Name": "name",
        "TopologyId": "topologyId",
        "UseFlagBit": "useFlagBit",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BaseVidList, self).__init__(parent, list_op)

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
    def BaseVid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Base VID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BaseVid"]))

    @property
    def BaseVlanPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B-VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BaseVlanPriority"])
        )

    @property
    def BvlanTpid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B-VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BvlanTpid"]))

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
    def EctAlgorithm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ECT AlgorithmType
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EctAlgorithm"]))

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

    @property
    def TopologyId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Topology Id
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TopologyId"]))

    @property
    def UseFlagBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use Flag Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UseFlagBit"]))

    def update(self, Name=None):
        # type: (str) -> BaseVidList
        """Updates baseVidList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None):
        # type: (int, str, str) -> BaseVidList
        """Finds and retrieves baseVidList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve baseVidList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all baseVidList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching baseVidList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of baseVidList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the baseVidList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

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

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        BaseVid=None,
        BaseVlanPriority=None,
        BvlanTpid=None,
        EctAlgorithm=None,
        TopologyId=None,
        UseFlagBit=None,
    ):
        """Base class infrastructure that gets a list of baseVidList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - BaseVid (str): optional regex of baseVid
        - BaseVlanPriority (str): optional regex of baseVlanPriority
        - BvlanTpid (str): optional regex of bvlanTpid
        - EctAlgorithm (str): optional regex of ectAlgorithm
        - TopologyId (str): optional regex of topologyId
        - UseFlagBit (str): optional regex of useFlagBit

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
