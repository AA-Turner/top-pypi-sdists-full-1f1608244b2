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


class ParticipatingVdcReference(object):
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
        'vdc_ref': 'EntityReference',
        'org_ref': 'EntityReference',
        'site_ref': 'EntityReference',
        'network_provider_scope': 'str',
        'fault_domain_tag': 'str',
        'remote_org': 'bool',
        'status': 'VdcGroupEntityStatus'
    }

    attribute_map = {
        'vdc_ref': 'vdcRef',
        'org_ref': 'orgRef',
        'site_ref': 'siteRef',
        'network_provider_scope': 'networkProviderScope',
        'fault_domain_tag': 'faultDomainTag',
        'remote_org': 'remoteOrg',
        'status': 'status'
    }

    def __init__(self, vdc_ref=None, org_ref=None, site_ref=None, network_provider_scope=None, fault_domain_tag=None, remote_org=None, status=None):
        """
        ParticipatingVdcReference - a model defined in Swagger
        """

        self._vdc_ref = None
        self._org_ref = None
        self._site_ref = None
        self._network_provider_scope = None
        self._fault_domain_tag = None
        self._remote_org = None
        self._status = None

        self.vdc_ref = vdc_ref
        if org_ref is not None:
          self.org_ref = org_ref
        if site_ref is not None:
          self.site_ref = site_ref
        if network_provider_scope is not None:
          self.network_provider_scope = network_provider_scope
        if fault_domain_tag is not None:
          self.fault_domain_tag = fault_domain_tag
        if remote_org is not None:
          self.remote_org = remote_org
        if status is not None:
          self.status = status

    @property
    def vdc_ref(self):
        """
        Gets the vdc_ref of this ParticipatingVdcReference.
        The reference to the vDC that is part of this a vDC group.

        :return: The vdc_ref of this ParticipatingVdcReference.
        :rtype: EntityReference
        """
        return self._vdc_ref

    @vdc_ref.setter
    def vdc_ref(self, vdc_ref):
        """
        Sets the vdc_ref of this ParticipatingVdcReference.
        The reference to the vDC that is part of this a vDC group.

        :param vdc_ref: The vdc_ref of this ParticipatingVdcReference.
        :type: EntityReference
        """
        if vdc_ref is None:
            raise ValueError("Invalid value for `vdc_ref`, must not be `None`")

        self._vdc_ref = vdc_ref

    @property
    def org_ref(self):
        """
        Gets the org_ref of this ParticipatingVdcReference.
        Read-only field that specifies what organization this vDC is in.

        :return: The org_ref of this ParticipatingVdcReference.
        :rtype: EntityReference
        """
        return self._org_ref

    @org_ref.setter
    def org_ref(self, org_ref):
        """
        Sets the org_ref of this ParticipatingVdcReference.
        Read-only field that specifies what organization this vDC is in.

        :param org_ref: The org_ref of this ParticipatingVdcReference.
        :type: EntityReference
        """

        self._org_ref = org_ref

    @property
    def site_ref(self):
        """
        Gets the site_ref of this ParticipatingVdcReference.
        The site ID that this vDC belongs to. Required for universal vDC groups.

        :return: The site_ref of this ParticipatingVdcReference.
        :rtype: EntityReference
        """
        return self._site_ref

    @site_ref.setter
    def site_ref(self, site_ref):
        """
        Sets the site_ref of this ParticipatingVdcReference.
        The site ID that this vDC belongs to. Required for universal vDC groups.

        :param site_ref: The site_ref of this ParticipatingVdcReference.
        :type: EntityReference
        """

        self._site_ref = site_ref

    @property
    def network_provider_scope(self):
        """
        Gets the network_provider_scope of this ParticipatingVdcReference.
        Read-only field that specifies the network provider scope of the vDC.

        :return: The network_provider_scope of this ParticipatingVdcReference.
        :rtype: str
        """
        return self._network_provider_scope

    @network_provider_scope.setter
    def network_provider_scope(self, network_provider_scope):
        """
        Sets the network_provider_scope of this ParticipatingVdcReference.
        Read-only field that specifies the network provider scope of the vDC.

        :param network_provider_scope: The network_provider_scope of this ParticipatingVdcReference.
        :type: str
        """

        self._network_provider_scope = network_provider_scope

    @property
    def fault_domain_tag(self):
        """
        Gets the fault_domain_tag of this ParticipatingVdcReference.
        Represents the fault domain of a given organization vDC. For NSX_V backed organization vDCs, this is the network provider scope. For NSX_T backed organization vDCs, this can vary (for example name of the provider vDC or compute provider scope). 

        :return: The fault_domain_tag of this ParticipatingVdcReference.
        :rtype: str
        """
        return self._fault_domain_tag

    @fault_domain_tag.setter
    def fault_domain_tag(self, fault_domain_tag):
        """
        Sets the fault_domain_tag of this ParticipatingVdcReference.
        Represents the fault domain of a given organization vDC. For NSX_V backed organization vDCs, this is the network provider scope. For NSX_T backed organization vDCs, this can vary (for example name of the provider vDC or compute provider scope). 

        :param fault_domain_tag: The fault_domain_tag of this ParticipatingVdcReference.
        :type: str
        """

        self._fault_domain_tag = fault_domain_tag

    @property
    def remote_org(self):
        """
        Gets the remote_org of this ParticipatingVdcReference.
        Read-only field that specifies whether the vDC is local to this VCD site.

        :return: The remote_org of this ParticipatingVdcReference.
        :rtype: bool
        """
        return self._remote_org

    @remote_org.setter
    def remote_org(self, remote_org):
        """
        Sets the remote_org of this ParticipatingVdcReference.
        Read-only field that specifies whether the vDC is local to this VCD site.

        :param remote_org: The remote_org of this ParticipatingVdcReference.
        :type: bool
        """

        self._remote_org = remote_org

    @property
    def status(self):
        """
        Gets the status of this ParticipatingVdcReference.
        The status that the vDC can be in. An example is if the vDC has been deleted from the system but is still part of the group.

        :return: The status of this ParticipatingVdcReference.
        :rtype: VdcGroupEntityStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ParticipatingVdcReference.
        The status that the vDC can be in. An example is if the vDC has been deleted from the system but is still part of the group.

        :param status: The status of this ParticipatingVdcReference.
        :type: VdcGroupEntityStatus
        """

        self._status = status

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
        if not isinstance(other, ParticipatingVdcReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
