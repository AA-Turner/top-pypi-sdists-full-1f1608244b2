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


class NetTopologyLinear(Base):
    """Linear topology
    The NetTopologyLinear class encapsulates a list of netTopologyLinear resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetTopologyLinear.find() method.
    The list can be managed by using the NetTopologyLinear.add() and NetTopologyLinear.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "netTopologyLinear"
    _SDM_ATT_MAP = {
        "IncludeEntryPoint": "includeEntryPoint",
        "LinkMultiplier": "linkMultiplier",
        "Nodes": "nodes",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(NetTopologyLinear, self).__init__(parent, list_op)

    @property
    def IncludeEntryPoint(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: if true, entry node belongs to ring topology, otherwise it is outside of ring
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeEntryPoint"])

    @IncludeEntryPoint.setter
    def IncludeEntryPoint(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeEntryPoint"], value)

    @property
    def LinkMultiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: number of links between two nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkMultiplier"])

    @LinkMultiplier.setter
    def LinkMultiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinkMultiplier"], value)

    @property
    def Nodes(self):
        # type: () -> int
        """
        Returns
        -------
        - number: number of nodes
        """
        return self._get_attribute(self._SDM_ATT_MAP["Nodes"])

    @Nodes.setter
    def Nodes(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Nodes"], value)

    def update(self, IncludeEntryPoint=None, LinkMultiplier=None, Nodes=None):
        # type: (bool, int, int) -> NetTopologyLinear
        """Updates netTopologyLinear resource on the server.

        Args
        ----
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - Nodes (number): number of nodes

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IncludeEntryPoint=None, LinkMultiplier=None, Nodes=None):
        # type: (bool, int, int) -> NetTopologyLinear
        """Adds a new netTopologyLinear resource on the server and adds it to the container.

        Args
        ----
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - Nodes (number): number of nodes

        Returns
        -------
        - self: This instance with all currently retrieved netTopologyLinear resources using find and the newly added netTopologyLinear resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained netTopologyLinear resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IncludeEntryPoint=None, LinkMultiplier=None, Nodes=None):
        # type: (bool, int, int) -> NetTopologyLinear
        """Finds and retrieves netTopologyLinear resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve netTopologyLinear resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all netTopologyLinear resources from the server.

        Args
        ----
        - IncludeEntryPoint (bool): if true, entry node belongs to ring topology, otherwise it is outside of ring
        - LinkMultiplier (number): number of links between two nodes
        - Nodes (number): number of nodes

        Returns
        -------
        - self: This instance with matching netTopologyLinear resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of netTopologyLinear data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the netTopologyLinear resources from the server available through an iterator or index

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
