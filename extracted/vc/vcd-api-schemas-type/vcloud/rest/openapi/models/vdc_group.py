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


class VdcGroup(object):
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
        'id': 'str',
        'org_id': 'str',
        'name': 'str',
        'description': 'str',
        'local_egress': 'bool',
        'participating_org_vdcs': 'list[ParticipatingVdcReference]',
        'universal_networking_enabled': 'bool',
        'network_pool_universal_id': 'str',
        'network_pool_id': 'str',
        'status': 'VdcGroupEntityStatus',
        'type': 'str',
        'network_provider_type': 'str',
        'dfw_enabled': 'bool',
        'error_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'org_id': 'orgId',
        'name': 'name',
        'description': 'description',
        'local_egress': 'localEgress',
        'participating_org_vdcs': 'participatingOrgVdcs',
        'universal_networking_enabled': 'universalNetworkingEnabled',
        'network_pool_universal_id': 'networkPoolUniversalId',
        'network_pool_id': 'networkPoolId',
        'status': 'status',
        'type': 'type',
        'network_provider_type': 'networkProviderType',
        'dfw_enabled': 'dfwEnabled',
        'error_message': 'errorMessage'
    }

    def __init__(self, id=None, org_id=None, name=None, description=None, local_egress=False, participating_org_vdcs=None, universal_networking_enabled=None, network_pool_universal_id=None, network_pool_id=None, status=None, type='UNIVERSAL', network_provider_type='NSX_V', dfw_enabled=None, error_message=None):
        """
        VdcGroup - a model defined in Swagger
        """

        self._id = None
        self._org_id = None
        self._name = None
        self._description = None
        self._local_egress = None
        self._participating_org_vdcs = None
        self._universal_networking_enabled = None
        self._network_pool_universal_id = None
        self._network_pool_id = None
        self._status = None
        self._type = None
        self._network_provider_type = None
        self._dfw_enabled = None
        self._error_message = None

        if id is not None:
          self.id = id
        self.org_id = org_id
        self.name = name
        if description is not None:
          self.description = description
        if local_egress is not None:
          self.local_egress = local_egress
        self.participating_org_vdcs = participating_org_vdcs
        if universal_networking_enabled is not None:
          self.universal_networking_enabled = universal_networking_enabled
        if network_pool_universal_id is not None:
          self.network_pool_universal_id = network_pool_universal_id
        if network_pool_id is not None:
          self.network_pool_id = network_pool_id
        if status is not None:
          self.status = status
        if type is not None:
          self.type = type
        if network_provider_type is not None:
          self.network_provider_type = network_provider_type
        if dfw_enabled is not None:
          self.dfw_enabled = dfw_enabled
        if error_message is not None:
          self.error_message = error_message

    @property
    def id(self):
        """
        Gets the id of this VdcGroup.
        The unique ID for the vDC Group (read-only).

        :return: The id of this VdcGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VdcGroup.
        The unique ID for the vDC Group (read-only).

        :param id: The id of this VdcGroup.
        :type: str
        """

        self._id = id

    @property
    def org_id(self):
        """
        Gets the org_id of this VdcGroup.
        The organization that this group belongs to.

        :return: The org_id of this VdcGroup.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """
        Sets the org_id of this VdcGroup.
        The organization that this group belongs to.

        :param org_id: The org_id of this VdcGroup.
        :type: str
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")

        self._org_id = org_id

    @property
    def name(self):
        """
        Gets the name of this VdcGroup.
        The name of this group. The name must be unique.

        :return: The name of this VdcGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VdcGroup.
        The name of this group. The name must be unique.

        :param name: The name of this VdcGroup.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this VdcGroup.
        The description of this group.

        :return: The description of this VdcGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this VdcGroup.
        The description of this group.

        :param description: The description of this VdcGroup.
        :type: str
        """

        self._description = description

    @property
    def local_egress(self):
        """
        Gets the local_egress of this VdcGroup.
        Determines whether local egress is enabled for a universal router belonging to a universal vDC group. This value is used on create if universalNetworkingEnabled is set to true. This cannot be updated. This value is always false for local vDC groups. 

        :return: The local_egress of this VdcGroup.
        :rtype: bool
        """
        return self._local_egress

    @local_egress.setter
    def local_egress(self, local_egress):
        """
        Sets the local_egress of this VdcGroup.
        Determines whether local egress is enabled for a universal router belonging to a universal vDC group. This value is used on create if universalNetworkingEnabled is set to true. This cannot be updated. This value is always false for local vDC groups. 

        :param local_egress: The local_egress of this VdcGroup.
        :type: bool
        """

        self._local_egress = local_egress

    @property
    def participating_org_vdcs(self):
        """
        Gets the participating_org_vdcs of this VdcGroup.
        The list of organization vDCs that are participating in this group.

        :return: The participating_org_vdcs of this VdcGroup.
        :rtype: list[ParticipatingVdcReference]
        """
        return self._participating_org_vdcs

    @participating_org_vdcs.setter
    def participating_org_vdcs(self, participating_org_vdcs):
        """
        Sets the participating_org_vdcs of this VdcGroup.
        The list of organization vDCs that are participating in this group.

        :param participating_org_vdcs: The participating_org_vdcs of this VdcGroup.
        :type: list[ParticipatingVdcReference]
        """
        if participating_org_vdcs is None:
            raise ValueError("Invalid value for `participating_org_vdcs`, must not be `None`")

        self._participating_org_vdcs = participating_org_vdcs

    @property
    def universal_networking_enabled(self):
        """
        Gets the universal_networking_enabled of this VdcGroup.
        True means that a vDC group router has been created. If set to true for vdc group creation, a universal router will also be created.

        :return: The universal_networking_enabled of this VdcGroup.
        :rtype: bool
        """
        return self._universal_networking_enabled

    @universal_networking_enabled.setter
    def universal_networking_enabled(self, universal_networking_enabled):
        """
        Sets the universal_networking_enabled of this VdcGroup.
        True means that a vDC group router has been created. If set to true for vdc group creation, a universal router will also be created.

        :param universal_networking_enabled: The universal_networking_enabled of this VdcGroup.
        :type: bool
        """

        self._universal_networking_enabled = universal_networking_enabled

    @property
    def network_pool_universal_id(self):
        """
        Gets the network_pool_universal_id of this VdcGroup.
        The network provider's universal id that is backing the universal network pool. This field is read-only and is derived from the list of participating vDCs if a universal vDC group is created. For universal vDC groups, each participating vDC should have a universal network pool that is backed by this same id. 

        :return: The network_pool_universal_id of this VdcGroup.
        :rtype: str
        """
        return self._network_pool_universal_id

    @network_pool_universal_id.setter
    def network_pool_universal_id(self, network_pool_universal_id):
        """
        Sets the network_pool_universal_id of this VdcGroup.
        The network provider's universal id that is backing the universal network pool. This field is read-only and is derived from the list of participating vDCs if a universal vDC group is created. For universal vDC groups, each participating vDC should have a universal network pool that is backed by this same id. 

        :param network_pool_universal_id: The network_pool_universal_id of this VdcGroup.
        :type: str
        """

        self._network_pool_universal_id = network_pool_universal_id

    @property
    def network_pool_id(self):
        """
        Gets the network_pool_id of this VdcGroup.
        ID of network pool to use if creating a local vDC group router. Must be set if creating a local group. Ignored if creating a universal group. 

        :return: The network_pool_id of this VdcGroup.
        :rtype: str
        """
        return self._network_pool_id

    @network_pool_id.setter
    def network_pool_id(self, network_pool_id):
        """
        Sets the network_pool_id of this VdcGroup.
        ID of network pool to use if creating a local vDC group router. Must be set if creating a local group. Ignored if creating a universal group. 

        :param network_pool_id: The network_pool_id of this VdcGroup.
        :type: str
        """

        self._network_pool_id = network_pool_id

    @property
    def status(self):
        """
        Gets the status of this VdcGroup.
        The status that the group can be in.

        :return: The status of this VdcGroup.
        :rtype: VdcGroupEntityStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this VdcGroup.
        The status that the group can be in.

        :param status: The status of this VdcGroup.
        :type: VdcGroupEntityStatus
        """

        self._status = status

    @property
    def type(self):
        """
        Gets the type of this VdcGroup.
        Defines the group as LOCAL or UNIVERSAL. This cannot be changed. Local vDC Groups can have networks stretched across multiple vDCs in a single Cloud Director instance. Local vDC Groups share the same broadcast domain/transport zone and network provider scope. Universal vDC groups can have networks stretched across multiple vDCs in a single or multiple Cloud Director instance(s). Universal vDC groups are backed by a broadcast domain/transport zone that strectches across a single or multiple Cloud Director instance(s). Local vDC groups are supported for both NSX-V and NSX-T Network Provider Types. Universal vDC Groups are supported for only NSX_V Network Provider Type. 

        :return: The type of this VdcGroup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VdcGroup.
        Defines the group as LOCAL or UNIVERSAL. This cannot be changed. Local vDC Groups can have networks stretched across multiple vDCs in a single Cloud Director instance. Local vDC Groups share the same broadcast domain/transport zone and network provider scope. Universal vDC groups can have networks stretched across multiple vDCs in a single or multiple Cloud Director instance(s). Universal vDC groups are backed by a broadcast domain/transport zone that strectches across a single or multiple Cloud Director instance(s). Local vDC groups are supported for both NSX-V and NSX-T Network Provider Types. Universal vDC Groups are supported for only NSX_V Network Provider Type. 

        :param type: The type of this VdcGroup.
        :type: str
        """
        allowed_values = ["LOCAL", "UNIVERSAL"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def network_provider_type(self):
        """
        Gets the network_provider_type of this VdcGroup.
        The values currently supported are NSX_V and NSX_T. Defines the networking provider backing the vDC Group. This is used on create. If not specified, NSX_V value will be used. NSX_V is used for existing vDC Groups and vDC Groups where Cross-VC NSX is used for the underlying technology. NSX_T is used when the networking provider type for the Organization vDCs in the group is NSX-T. NSX_T only supports groups of type LOCAL (single site). 

        :return: The network_provider_type of this VdcGroup.
        :rtype: str
        """
        return self._network_provider_type

    @network_provider_type.setter
    def network_provider_type(self, network_provider_type):
        """
        Sets the network_provider_type of this VdcGroup.
        The values currently supported are NSX_V and NSX_T. Defines the networking provider backing the vDC Group. This is used on create. If not specified, NSX_V value will be used. NSX_V is used for existing vDC Groups and vDC Groups where Cross-VC NSX is used for the underlying technology. NSX_T is used when the networking provider type for the Organization vDCs in the group is NSX-T. NSX_T only supports groups of type LOCAL (single site). 

        :param network_provider_type: The network_provider_type of this VdcGroup.
        :type: str
        """

        self._network_provider_type = network_provider_type

    @property
    def dfw_enabled(self):
        """
        Gets the dfw_enabled of this VdcGroup.
        Whether Distributed Firewall is enabled for this vDC Group. Only applicable for NSX_T vDC Groups.

        :return: The dfw_enabled of this VdcGroup.
        :rtype: bool
        """
        return self._dfw_enabled

    @dfw_enabled.setter
    def dfw_enabled(self, dfw_enabled):
        """
        Sets the dfw_enabled of this VdcGroup.
        Whether Distributed Firewall is enabled for this vDC Group. Only applicable for NSX_T vDC Groups.

        :param dfw_enabled: The dfw_enabled of this VdcGroup.
        :type: bool
        """

        self._dfw_enabled = dfw_enabled

    @property
    def error_message(self):
        """
        Gets the error_message of this VdcGroup.
        If the group has an error status, a more detailed error message is set here.

        :return: The error_message of this VdcGroup.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this VdcGroup.
        If the group has an error status, a more detailed error message is set here.

        :param error_message: The error_message of this VdcGroup.
        :type: str
        """

        self._error_message = error_message

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
        if not isinstance(other, VdcGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
