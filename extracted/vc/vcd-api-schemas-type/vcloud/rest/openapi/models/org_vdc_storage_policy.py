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


class OrgVdcStoragePolicy(object):
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
        'name': 'str',
        'is_enabled': 'bool',
        'is_default_storage_policy': 'bool',
        'storage_limit_mb': 'int',
        'org_vdc_ref': 'EntityReference',
        'pvdc_storage_policy_ref': 'EntityReference'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_enabled': 'isEnabled',
        'is_default_storage_policy': 'isDefaultStoragePolicy',
        'storage_limit_mb': 'storageLimitMb',
        'org_vdc_ref': 'orgVdcRef',
        'pvdc_storage_policy_ref': 'pvdcStoragePolicyRef'
    }

    def __init__(self, id=None, name=None, is_enabled=True, is_default_storage_policy=False, storage_limit_mb=None, org_vdc_ref=None, pvdc_storage_policy_ref=None):
        """
        OrgVdcStoragePolicy - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._is_enabled = None
        self._is_default_storage_policy = None
        self._storage_limit_mb = None
        self._org_vdc_ref = None
        self._pvdc_storage_policy_ref = None

        if id is not None:
          self.id = id
        self.name = name
        if is_enabled is not None:
          self.is_enabled = is_enabled
        if is_default_storage_policy is not None:
          self.is_default_storage_policy = is_default_storage_policy
        if storage_limit_mb is not None:
          self.storage_limit_mb = storage_limit_mb
        if org_vdc_ref is not None:
          self.org_vdc_ref = org_vdc_ref
        if pvdc_storage_policy_ref is not None:
          self.pvdc_storage_policy_ref = pvdc_storage_policy_ref

    @property
    def id(self):
        """
        Gets the id of this OrgVdcStoragePolicy.
        Unique VCD Id for the policy.

        :return: The id of this OrgVdcStoragePolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OrgVdcStoragePolicy.
        Unique VCD Id for the policy.

        :param id: The id of this OrgVdcStoragePolicy.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this OrgVdcStoragePolicy.
        Unique name for the policy.

        :return: The name of this OrgVdcStoragePolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrgVdcStoragePolicy.
        Unique name for the policy.

        :param name: The name of this OrgVdcStoragePolicy.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this OrgVdcStoragePolicy.
        Enabled state of the policy, defaults to true.

        :return: The is_enabled of this OrgVdcStoragePolicy.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this OrgVdcStoragePolicy.
        Enabled state of the policy, defaults to true.

        :param is_enabled: The is_enabled of this OrgVdcStoragePolicy.
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def is_default_storage_policy(self):
        """
        Gets the is_default_storage_policy of this OrgVdcStoragePolicy.
        Storage policy is marked as default, defaults to false.

        :return: The is_default_storage_policy of this OrgVdcStoragePolicy.
        :rtype: bool
        """
        return self._is_default_storage_policy

    @is_default_storage_policy.setter
    def is_default_storage_policy(self, is_default_storage_policy):
        """
        Sets the is_default_storage_policy of this OrgVdcStoragePolicy.
        Storage policy is marked as default, defaults to false.

        :param is_default_storage_policy: The is_default_storage_policy of this OrgVdcStoragePolicy.
        :type: bool
        """

        self._is_default_storage_policy = is_default_storage_policy

    @property
    def storage_limit_mb(self):
        """
        Gets the storage_limit_mb of this OrgVdcStoragePolicy.
        Storage limit for the policy.

        :return: The storage_limit_mb of this OrgVdcStoragePolicy.
        :rtype: int
        """
        return self._storage_limit_mb

    @storage_limit_mb.setter
    def storage_limit_mb(self, storage_limit_mb):
        """
        Sets the storage_limit_mb of this OrgVdcStoragePolicy.
        Storage limit for the policy.

        :param storage_limit_mb: The storage_limit_mb of this OrgVdcStoragePolicy.
        :type: int
        """

        self._storage_limit_mb = storage_limit_mb

    @property
    def org_vdc_ref(self):
        """
        Gets the org_vdc_ref of this OrgVdcStoragePolicy.
        The Org VDC that this policy belongs to.

        :return: The org_vdc_ref of this OrgVdcStoragePolicy.
        :rtype: EntityReference
        """
        return self._org_vdc_ref

    @org_vdc_ref.setter
    def org_vdc_ref(self, org_vdc_ref):
        """
        Sets the org_vdc_ref of this OrgVdcStoragePolicy.
        The Org VDC that this policy belongs to.

        :param org_vdc_ref: The org_vdc_ref of this OrgVdcStoragePolicy.
        :type: EntityReference
        """

        self._org_vdc_ref = org_vdc_ref

    @property
    def pvdc_storage_policy_ref(self):
        """
        Gets the pvdc_storage_policy_ref of this OrgVdcStoragePolicy.
        The parent PVDC storage policy for this Organization VDC storage policy.

        :return: The pvdc_storage_policy_ref of this OrgVdcStoragePolicy.
        :rtype: EntityReference
        """
        return self._pvdc_storage_policy_ref

    @pvdc_storage_policy_ref.setter
    def pvdc_storage_policy_ref(self, pvdc_storage_policy_ref):
        """
        Sets the pvdc_storage_policy_ref of this OrgVdcStoragePolicy.
        The parent PVDC storage policy for this Organization VDC storage policy.

        :param pvdc_storage_policy_ref: The pvdc_storage_policy_ref of this OrgVdcStoragePolicy.
        :type: EntityReference
        """

        self._pvdc_storage_policy_ref = pvdc_storage_policy_ref

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
        if not isinstance(other, OrgVdcStoragePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
