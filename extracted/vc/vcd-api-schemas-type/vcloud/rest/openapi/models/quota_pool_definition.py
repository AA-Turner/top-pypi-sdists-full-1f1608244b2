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


class QuotaPoolDefinition(object):
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
        'quota_resource_name': 'str',
        'resource_type': 'str',
        'quota_resource_unit': 'str',
        'quota': 'int',
        'qualifiers': 'list[str]'
    }

    attribute_map = {
        'quota_resource_name': 'quotaResourceName',
        'resource_type': 'resourceType',
        'quota_resource_unit': 'quotaResourceUnit',
        'quota': 'quota',
        'qualifiers': 'qualifiers'
    }

    def __init__(self, quota_resource_name=None, resource_type=None, quota_resource_unit=None, quota=None, qualifiers=None):
        """
        QuotaPoolDefinition - a model defined in Swagger
        """

        self._quota_resource_name = None
        self._resource_type = None
        self._quota_resource_unit = None
        self._quota = None
        self._qualifiers = None

        if quota_resource_name is not None:
          self.quota_resource_name = quota_resource_name
        self.resource_type = resource_type
        if quota_resource_unit is not None:
          self.quota_resource_unit = quota_resource_unit
        self.quota = quota
        if qualifiers is not None:
          self.qualifiers = qualifiers

    @property
    def quota_resource_name(self):
        """
        Gets the quota_resource_name of this QuotaPoolDefinition.
        The localized name of quota resource type. 

        :return: The quota_resource_name of this QuotaPoolDefinition.
        :rtype: str
        """
        return self._quota_resource_name

    @quota_resource_name.setter
    def quota_resource_name(self, quota_resource_name):
        """
        Sets the quota_resource_name of this QuotaPoolDefinition.
        The localized name of quota resource type. 

        :param quota_resource_name: The quota_resource_name of this QuotaPoolDefinition.
        :type: str
        """

        self._quota_resource_name = quota_resource_name

    @property
    def resource_type(self):
        """
        Gets the resource_type of this QuotaPoolDefinition.
        The quota resource type such as memory, cpu, vm etc. Available resource types: memory, cpu, storage, urn:vcloud:legacy:vm, urn:vcloud:type:vmware.tkgcluster:1.0.0 

        :return: The resource_type of this QuotaPoolDefinition.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this QuotaPoolDefinition.
        The quota resource type such as memory, cpu, vm etc. Available resource types: memory, cpu, storage, urn:vcloud:legacy:vm, urn:vcloud:type:vmware.tkgcluster:1.0.0 

        :param resource_type: The resource_type of this QuotaPoolDefinition.
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")

        self._resource_type = resource_type

    @property
    def quota_resource_unit(self):
        """
        Gets the quota_resource_unit of this QuotaPoolDefinition.
        The unit of quota defined for quota resource type. Available quota units for resource types: memory - MB cpu - MHz storage - MB urn:vcloud:legacy:vm - count 

        :return: The quota_resource_unit of this QuotaPoolDefinition.
        :rtype: str
        """
        return self._quota_resource_unit

    @quota_resource_unit.setter
    def quota_resource_unit(self, quota_resource_unit):
        """
        Sets the quota_resource_unit of this QuotaPoolDefinition.
        The unit of quota defined for quota resource type. Available quota units for resource types: memory - MB cpu - MHz storage - MB urn:vcloud:legacy:vm - count 

        :param quota_resource_unit: The quota_resource_unit of this QuotaPoolDefinition.
        :type: str
        """

        self._quota_resource_unit = quota_resource_unit

    @property
    def quota(self):
        """
        Gets the quota of this QuotaPoolDefinition.
        The quota amount for this resource. 

        :return: The quota of this QuotaPoolDefinition.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """
        Sets the quota of this QuotaPoolDefinition.
        The quota amount for this resource. 

        :param quota: The quota of this QuotaPoolDefinition.
        :type: int
        """
        if quota is None:
            raise ValueError("Invalid value for `quota`, must not be `None`")

        self._quota = quota

    @property
    def qualifiers(self):
        """
        Gets the qualifiers of this QuotaPoolDefinition.
        The qualifiers for quota resource type, such as vm.guestOs == Windows. This is optional. Qualifiers just helps in narrowing down quota resource based on values of one or more of its properties. If vm is a quota resource, from the above example, only VMs with Windows guest OS will be considered for quota eligibility. If more than one qualifier is provided, system will use AND operator to process them. 

        :return: The qualifiers of this QuotaPoolDefinition.
        :rtype: list[str]
        """
        return self._qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers):
        """
        Sets the qualifiers of this QuotaPoolDefinition.
        The qualifiers for quota resource type, such as vm.guestOs == Windows. This is optional. Qualifiers just helps in narrowing down quota resource based on values of one or more of its properties. If vm is a quota resource, from the above example, only VMs with Windows guest OS will be considered for quota eligibility. If more than one qualifier is provided, system will use AND operator to process them. 

        :param qualifiers: The qualifiers of this QuotaPoolDefinition.
        :type: list[str]
        """

        self._qualifiers = qualifiers

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
        if not isinstance(other, QuotaPoolDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
