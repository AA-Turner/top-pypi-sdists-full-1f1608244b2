# coding: utf-8

"""
    VMware Cloud Director OpenAPI

    VMware Cloud Director OpenAPI is a new API that is defined using the OpenAPI standards.<br/> This ReSTful API borrows some elements of the legacy VMware Cloud Director API and establishes new patterns for use as described below. <h4>Authentication</h4> Authentication and Authorization schemes are the same as those for the legacy APIs. You can authenticate using the JWT token via the <code>Authorization</code> header or specifying a session using <code>x-vcloud-authorization</code> (The latter form is deprecated). <h4>Operation Patterns</h4> This API follows the following general guidelines to establish a consistent CRUD pattern: <table> <tr>   <th>Operation</th><th>Description</th><th>Response Code</th><th>Response Content</th> </tr><tr>   <td>GET /items<td>Returns a paginated list of items<td>200<td>Response will include Navigational links to the items in the list. </tr><tr>   <td>POST /items<td>Returns newly created item<td>201<td>Content-Location header links to the newly created item </tr><tr>   <td>GET /items/urn<td>Returns an individual item<td>200<td>A single item using same data type as that included in list above </tr><tr>   <td>PUT /items/urn<td>Updates an individual item<td>200<td>Updated view of the item is returned </tr><tr>   <td>DELETE /items/urn<td>Deletes the item<td>204<td>No content is returned. </tr> </table> <h5>Asynchronous operations</h5> Asynchronous operations are determined by the server. In those cases, instead of responding as described above, the server responds with an HTTP Response code 202 and an empty body. The tracking task (which is the same task as all legacy API operations use) is linked via the URI provided in the <code>Location</code> header.<br/> All API calls can choose to service a request asynchronously or synchronously as determined by the server upon interpreting the request. Operations that choose to exhibit this dual behavior will have both options documented by specifying both response code(s) below. The caller must be prepared to handle responses to such API calls by inspecting the HTTP Response code. <h5>Error Conditions</h5> <b>All</b> operations report errors using the following error reporting rules: <ul>   <li>400: Bad Request - In event of bad request due to incorrect data or other user error</li>   <li>401: Bad Request - If user is unauthenticated or their session has expired</li>   <li>403: Forbidden - If the user is not authorized or the entity does not exist</li> </ul> <h4>OpenAPI Design Concepts and Principles</h4> <ul>   <li>IDs are full Uniform Resource Names (URNs).</li>   <li>OpenAPI's <code>Content-Type</code> is always <code>application/json</code></li>   <li>REST links are in the Link header.</li>   <ul>     <li>Multiple relationships for any link are represented by multiple values in a space-separated list.</li>     <li>Links have a custom VMware Cloud Director-specific &quot;model&quot; attribute that hints at the applicable data         type for the links.</li>     <li>title + rel + model attributes evaluates to a unique link.</li>     <li>Links follow Hypermedia as the Engine of Application State (HATEOAS) principles. Links are present if         certain operations are present and permitted for the user&quot;s current role and the state of the         referred entities.</li>   </ul>   <li>APIs follow a flat structure relying on cross-referencing other entities instead of the navigational style       used by the legacy VMware Cloud Director APIs.</li>   <li>Most endpoints that return a list support filtering and sorting similar to the query service in the legacy       VMware Cloud Director APIs.</li>   <li>Accept header must be included to specify the API version for the request similar to calls to existing legacy       VMware Cloud Director APIs.</li>   <li>Each feature has a version in the path element present in its URL.<br/>       <b>Note</b> API URL's without a version in their paths must be considered experimental.</li> </ul> 

    OpenAPI spec version: 36.0
    Contact: https://code.vmware.com/support
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VirtualMachineClass(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'cpu_reservation_requested_m_hz': 'int',
        'memory_reservation_requested_mb': 'int',
        'cpu_count': 'int',
        'memory_mb': 'int',
        'is_fully_reserved': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'cpu_reservation_requested_m_hz': 'cpuReservationRequestedMHz',
        'memory_reservation_requested_mb': 'memoryReservationRequestedMB',
        'cpu_count': 'cpuCount',
        'memory_mb': 'memoryMB',
        'is_fully_reserved': 'isFullyReserved'
    }

    def __init__(self, name=None, cpu_reservation_requested_m_hz=None, memory_reservation_requested_mb=None, cpu_count=None, memory_mb=None, is_fully_reserved=None):
        """
        VirtualMachineClass - a model defined in Swagger
        """

        self._name = None
        self._cpu_reservation_requested_m_hz = None
        self._memory_reservation_requested_mb = None
        self._cpu_count = None
        self._memory_mb = None
        self._is_fully_reserved = None

        if name is not None:
          self.name = name
        if cpu_reservation_requested_m_hz is not None:
          self.cpu_reservation_requested_m_hz = cpu_reservation_requested_m_hz
        if memory_reservation_requested_mb is not None:
          self.memory_reservation_requested_mb = memory_reservation_requested_mb
        if cpu_count is not None:
          self.cpu_count = cpu_count
        if memory_mb is not None:
          self.memory_mb = memory_mb
        if is_fully_reserved is not None:
          self.is_fully_reserved = is_fully_reserved

    @property
    def name(self):
        """
        Gets the name of this VirtualMachineClass.
        Name of the Virtual Machine Class. 

        :return: The name of this VirtualMachineClass.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VirtualMachineClass.
        Name of the Virtual Machine Class. 

        :param name: The name of this VirtualMachineClass.
        :type: str
        """

        self._name = name

    @property
    def cpu_reservation_requested_m_hz(self):
        """
        Gets the cpu_reservation_requested_m_hz of this VirtualMachineClass.
        CPU in MHz that a node reserves when this VirtualMachineClass is applied to the node of a Kubernetes cluster. 

        :return: The cpu_reservation_requested_m_hz of this VirtualMachineClass.
        :rtype: int
        """
        return self._cpu_reservation_requested_m_hz

    @cpu_reservation_requested_m_hz.setter
    def cpu_reservation_requested_m_hz(self, cpu_reservation_requested_m_hz):
        """
        Sets the cpu_reservation_requested_m_hz of this VirtualMachineClass.
        CPU in MHz that a node reserves when this VirtualMachineClass is applied to the node of a Kubernetes cluster. 

        :param cpu_reservation_requested_m_hz: The cpu_reservation_requested_m_hz of this VirtualMachineClass.
        :type: int
        """

        self._cpu_reservation_requested_m_hz = cpu_reservation_requested_m_hz

    @property
    def memory_reservation_requested_mb(self):
        """
        Gets the memory_reservation_requested_mb of this VirtualMachineClass.
        Memory in MB that a node reserves when this VirtualMachineClass is applied to the node of a Kubernetes cluster. 

        :return: The memory_reservation_requested_mb of this VirtualMachineClass.
        :rtype: int
        """
        return self._memory_reservation_requested_mb

    @memory_reservation_requested_mb.setter
    def memory_reservation_requested_mb(self, memory_reservation_requested_mb):
        """
        Sets the memory_reservation_requested_mb of this VirtualMachineClass.
        Memory in MB that a node reserves when this VirtualMachineClass is applied to the node of a Kubernetes cluster. 

        :param memory_reservation_requested_mb: The memory_reservation_requested_mb of this VirtualMachineClass.
        :type: int
        """

        self._memory_reservation_requested_mb = memory_reservation_requested_mb

    @property
    def cpu_count(self):
        """
        Gets the cpu_count of this VirtualMachineClass.
        Number of CPUs that a node gets when this VirtualMachineClass is applied to the node of a Kubernetes cluster. 

        :return: The cpu_count of this VirtualMachineClass.
        :rtype: int
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, cpu_count):
        """
        Sets the cpu_count of this VirtualMachineClass.
        Number of CPUs that a node gets when this VirtualMachineClass is applied to the node of a Kubernetes cluster. 

        :param cpu_count: The cpu_count of this VirtualMachineClass.
        :type: int
        """

        self._cpu_count = cpu_count

    @property
    def memory_mb(self):
        """
        Gets the memory_mb of this VirtualMachineClass.
        Memory in MB that a node gets when this VirtualMachineClass is applied to the node of a Kubernetes cluster. 

        :return: The memory_mb of this VirtualMachineClass.
        :rtype: int
        """
        return self._memory_mb

    @memory_mb.setter
    def memory_mb(self, memory_mb):
        """
        Sets the memory_mb of this VirtualMachineClass.
        Memory in MB that a node gets when this VirtualMachineClass is applied to the node of a Kubernetes cluster. 

        :param memory_mb: The memory_mb of this VirtualMachineClass.
        :type: int
        """

        self._memory_mb = memory_mb

    @property
    def is_fully_reserved(self):
        """
        Gets the is_fully_reserved of this VirtualMachineClass.
        This read-only field conveys whether CPU and memory resources are fully reserved or not when this VirtualMachineClass is applied to the node of the Kubernetes cluster. 

        :return: The is_fully_reserved of this VirtualMachineClass.
        :rtype: bool
        """
        return self._is_fully_reserved

    @is_fully_reserved.setter
    def is_fully_reserved(self, is_fully_reserved):
        """
        Sets the is_fully_reserved of this VirtualMachineClass.
        This read-only field conveys whether CPU and memory resources are fully reserved or not when this VirtualMachineClass is applied to the node of the Kubernetes cluster. 

        :param is_fully_reserved: The is_fully_reserved of this VirtualMachineClass.
        :type: bool
        """

        self._is_fully_reserved = is_fully_reserved

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, VirtualMachineClass):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
