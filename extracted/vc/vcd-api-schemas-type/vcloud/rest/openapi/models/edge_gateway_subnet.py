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


class EdgeGatewaySubnet(object):
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
        'gateway': 'str',
        'prefix_length': 'int',
        'dns_suffix': 'str',
        'dns_server1': 'str',
        'dns_server2': 'str',
        'ip_ranges': 'IpRanges',
        'enabled': 'bool',
        'total_ip_count': 'int',
        'used_ip_count': 'int',
        'primary_ip': 'str',
        'auto_allocate_ip_ranges': 'bool'
    }

    attribute_map = {
        'gateway': 'gateway',
        'prefix_length': 'prefixLength',
        'dns_suffix': 'dnsSuffix',
        'dns_server1': 'dnsServer1',
        'dns_server2': 'dnsServer2',
        'ip_ranges': 'ipRanges',
        'enabled': 'enabled',
        'total_ip_count': 'totalIpCount',
        'used_ip_count': 'usedIpCount',
        'primary_ip': 'primaryIp',
        'auto_allocate_ip_ranges': 'autoAllocateIpRanges'
    }

    def __init__(self, gateway=None, prefix_length=None, dns_suffix=None, dns_server1=None, dns_server2=None, ip_ranges=None, enabled=True, total_ip_count=None, used_ip_count=None, primary_ip=None, auto_allocate_ip_ranges=False):
        """
        EdgeGatewaySubnet - a model defined in Swagger
        """

        self._gateway = None
        self._prefix_length = None
        self._dns_suffix = None
        self._dns_server1 = None
        self._dns_server2 = None
        self._ip_ranges = None
        self._enabled = None
        self._total_ip_count = None
        self._used_ip_count = None
        self._primary_ip = None
        self._auto_allocate_ip_ranges = None

        self.gateway = gateway
        self.prefix_length = prefix_length
        if dns_suffix is not None:
          self.dns_suffix = dns_suffix
        if dns_server1 is not None:
          self.dns_server1 = dns_server1
        if dns_server2 is not None:
          self.dns_server2 = dns_server2
        if ip_ranges is not None:
          self.ip_ranges = ip_ranges
        if enabled is not None:
          self.enabled = enabled
        if total_ip_count is not None:
          self.total_ip_count = total_ip_count
        if used_ip_count is not None:
          self.used_ip_count = used_ip_count
        if primary_ip is not None:
          self.primary_ip = primary_ip
        if auto_allocate_ip_ranges is not None:
          self.auto_allocate_ip_ranges = auto_allocate_ip_ranges

    @property
    def gateway(self):
        """
        Gets the gateway of this EdgeGatewaySubnet.
        The gateway for the subnet.

        :return: The gateway of this EdgeGatewaySubnet.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """
        Sets the gateway of this EdgeGatewaySubnet.
        The gateway for the subnet.

        :param gateway: The gateway of this EdgeGatewaySubnet.
        :type: str
        """
        if gateway is None:
            raise ValueError("Invalid value for `gateway`, must not be `None`")

        self._gateway = gateway

    @property
    def prefix_length(self):
        """
        Gets the prefix_length of this EdgeGatewaySubnet.
        The prefix length of the subnet.

        :return: The prefix_length of this EdgeGatewaySubnet.
        :rtype: int
        """
        return self._prefix_length

    @prefix_length.setter
    def prefix_length(self, prefix_length):
        """
        Sets the prefix_length of this EdgeGatewaySubnet.
        The prefix length of the subnet.

        :param prefix_length: The prefix_length of this EdgeGatewaySubnet.
        :type: int
        """
        if prefix_length is None:
            raise ValueError("Invalid value for `prefix_length`, must not be `None`")

        self._prefix_length = prefix_length

    @property
    def dns_suffix(self):
        """
        Gets the dns_suffix of this EdgeGatewaySubnet.
        The DNS suffix that VMs attached to this network will use.

        :return: The dns_suffix of this EdgeGatewaySubnet.
        :rtype: str
        """
        return self._dns_suffix

    @dns_suffix.setter
    def dns_suffix(self, dns_suffix):
        """
        Sets the dns_suffix of this EdgeGatewaySubnet.
        The DNS suffix that VMs attached to this network will use.

        :param dns_suffix: The dns_suffix of this EdgeGatewaySubnet.
        :type: str
        """

        self._dns_suffix = dns_suffix

    @property
    def dns_server1(self):
        """
        Gets the dns_server1 of this EdgeGatewaySubnet.
        The first DNS server that VMs attached to this network will use.

        :return: The dns_server1 of this EdgeGatewaySubnet.
        :rtype: str
        """
        return self._dns_server1

    @dns_server1.setter
    def dns_server1(self, dns_server1):
        """
        Sets the dns_server1 of this EdgeGatewaySubnet.
        The first DNS server that VMs attached to this network will use.

        :param dns_server1: The dns_server1 of this EdgeGatewaySubnet.
        :type: str
        """

        self._dns_server1 = dns_server1

    @property
    def dns_server2(self):
        """
        Gets the dns_server2 of this EdgeGatewaySubnet.
        The second DNS server that VMs attached to this network will use.

        :return: The dns_server2 of this EdgeGatewaySubnet.
        :rtype: str
        """
        return self._dns_server2

    @dns_server2.setter
    def dns_server2(self, dns_server2):
        """
        Sets the dns_server2 of this EdgeGatewaySubnet.
        The second DNS server that VMs attached to this network will use.

        :param dns_server2: The dns_server2 of this EdgeGatewaySubnet.
        :type: str
        """

        self._dns_server2 = dns_server2

    @property
    def ip_ranges(self):
        """
        Gets the ip_ranges of this EdgeGatewaySubnet.
        Range of IPs within the subnet that can be used in this network. A VM attached to this network is assigned one of these IPs.

        :return: The ip_ranges of this EdgeGatewaySubnet.
        :rtype: IpRanges
        """
        return self._ip_ranges

    @ip_ranges.setter
    def ip_ranges(self, ip_ranges):
        """
        Sets the ip_ranges of this EdgeGatewaySubnet.
        Range of IPs within the subnet that can be used in this network. A VM attached to this network is assigned one of these IPs.

        :param ip_ranges: The ip_ranges of this EdgeGatewaySubnet.
        :type: IpRanges
        """

        self._ip_ranges = ip_ranges

    @property
    def enabled(self):
        """
        Gets the enabled of this EdgeGatewaySubnet.
        Indicates whether the external network subnet is currently enabled.

        :return: The enabled of this EdgeGatewaySubnet.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this EdgeGatewaySubnet.
        Indicates whether the external network subnet is currently enabled.

        :param enabled: The enabled of this EdgeGatewaySubnet.
        :type: bool
        """

        self._enabled = enabled

    @property
    def total_ip_count(self):
        """
        Gets the total_ip_count of this EdgeGatewaySubnet.
        The number of IP addresses defined by the static IP ranges.

        :return: The total_ip_count of this EdgeGatewaySubnet.
        :rtype: int
        """
        return self._total_ip_count

    @total_ip_count.setter
    def total_ip_count(self, total_ip_count):
        """
        Sets the total_ip_count of this EdgeGatewaySubnet.
        The number of IP addresses defined by the static IP ranges.

        :param total_ip_count: The total_ip_count of this EdgeGatewaySubnet.
        :type: int
        """

        self._total_ip_count = total_ip_count

    @property
    def used_ip_count(self):
        """
        Gets the used_ip_count of this EdgeGatewaySubnet.
        The number of IP address used from the static IP ranges.

        :return: The used_ip_count of this EdgeGatewaySubnet.
        :rtype: int
        """
        return self._used_ip_count

    @used_ip_count.setter
    def used_ip_count(self, used_ip_count):
        """
        Sets the used_ip_count of this EdgeGatewaySubnet.
        The number of IP address used from the static IP ranges.

        :param used_ip_count: The used_ip_count of this EdgeGatewaySubnet.
        :type: int
        """

        self._used_ip_count = used_ip_count

    @property
    def primary_ip(self):
        """
        Gets the primary_ip of this EdgeGatewaySubnet.
        The primary IP address allocated for this subnet. If not specified, this IP is auto-allocated.  This IP belongs to the external network and can be used for system-configured NAT rules such as DNS forwarder configuration. 

        :return: The primary_ip of this EdgeGatewaySubnet.
        :rtype: str
        """
        return self._primary_ip

    @primary_ip.setter
    def primary_ip(self, primary_ip):
        """
        Sets the primary_ip of this EdgeGatewaySubnet.
        The primary IP address allocated for this subnet. If not specified, this IP is auto-allocated.  This IP belongs to the external network and can be used for system-configured NAT rules such as DNS forwarder configuration. 

        :param primary_ip: The primary_ip of this EdgeGatewaySubnet.
        :type: str
        """

        self._primary_ip = primary_ip

    @property
    def auto_allocate_ip_ranges(self):
        """
        Gets the auto_allocate_ip_ranges of this EdgeGatewaySubnet.
        Used for create and update api calls. If set to true, IP Ranges are automatically generated based on totalIpCount.

        :return: The auto_allocate_ip_ranges of this EdgeGatewaySubnet.
        :rtype: bool
        """
        return self._auto_allocate_ip_ranges

    @auto_allocate_ip_ranges.setter
    def auto_allocate_ip_ranges(self, auto_allocate_ip_ranges):
        """
        Sets the auto_allocate_ip_ranges of this EdgeGatewaySubnet.
        Used for create and update api calls. If set to true, IP Ranges are automatically generated based on totalIpCount.

        :param auto_allocate_ip_ranges: The auto_allocate_ip_ranges of this EdgeGatewaySubnet.
        :type: bool
        """

        self._auto_allocate_ip_ranges = auto_allocate_ip_ranges

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
        if not isinstance(other, EdgeGatewaySubnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
