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


class Sddc(object):
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
        'id': 'str',
        'description': 'str',
        'enabled': 'bool',
        'vc_id': 'str',
        'version': 'str',
        'overall_status': 'OverallStatus',
        'stats': 'SddcStats',
        'default_proxy': 'SddcProxy',
        'default_endpoint': 'SddcEndpoint'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'description': 'description',
        'enabled': 'enabled',
        'vc_id': 'vcId',
        'version': 'version',
        'overall_status': 'overallStatus',
        'stats': 'stats',
        'default_proxy': 'defaultProxy',
        'default_endpoint': 'defaultEndpoint'
    }

    def __init__(self, name=None, id=None, description='', enabled=False, vc_id=None, version=None, overall_status=None, stats=None, default_proxy=None, default_endpoint=None):
        """
        Sddc - a model defined in Swagger
        """

        self._name = None
        self._id = None
        self._description = None
        self._enabled = None
        self._vc_id = None
        self._version = None
        self._overall_status = None
        self._stats = None
        self._default_proxy = None
        self._default_endpoint = None

        self.name = name
        if id is not None:
          self.id = id
        if description is not None:
          self.description = description
        if enabled is not None:
          self.enabled = enabled
        self.vc_id = vc_id
        if version is not None:
          self.version = version
        if overall_status is not None:
          self.overall_status = overall_status
        if stats is not None:
          self.stats = stats
        if default_proxy is not None:
          self.default_proxy = default_proxy
        if default_endpoint is not None:
          self.default_endpoint = default_endpoint

    @property
    def name(self):
        """
        Gets the name of this Sddc.

        :return: The name of this Sddc.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Sddc.

        :param name: The name of this Sddc.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this Sddc.

        :return: The id of this Sddc.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Sddc.

        :param id: The id of this Sddc.
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this Sddc.

        :return: The description of this Sddc.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Sddc.

        :param description: The description of this Sddc.
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """
        Gets the enabled of this Sddc.

        :return: The enabled of this Sddc.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this Sddc.

        :param enabled: The enabled of this Sddc.
        :type: bool
        """

        self._enabled = enabled

    @property
    def vc_id(self):
        """
        Gets the vc_id of this Sddc.
        URN of the associated vCenter. This is not editable once the SDDC has been created.

        :return: The vc_id of this Sddc.
        :rtype: str
        """
        return self._vc_id

    @vc_id.setter
    def vc_id(self, vc_id):
        """
        Sets the vc_id of this Sddc.
        URN of the associated vCenter. This is not editable once the SDDC has been created.

        :param vc_id: The vc_id of this Sddc.
        :type: str
        """
        if vc_id is None:
            raise ValueError("Invalid value for `vc_id`, must not be `None`")

        self._vc_id = vc_id

    @property
    def version(self):
        """
        Gets the version of this Sddc.
        Version of the associated vCenter. This is not editable.

        :return: The version of this Sddc.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Sddc.
        Version of the associated vCenter. This is not editable.

        :param version: The version of this Sddc.
        :type: str
        """

        self._version = version

    @property
    def overall_status(self):
        """
        Gets the overall_status of this Sddc.
        Overall status of the associated vCenter. This is not editable.

        :return: The overall_status of this Sddc.
        :rtype: OverallStatus
        """
        return self._overall_status

    @overall_status.setter
    def overall_status(self, overall_status):
        """
        Sets the overall_status of this Sddc.
        Overall status of the associated vCenter. This is not editable.

        :param overall_status: The overall_status of this Sddc.
        :type: OverallStatus
        """

        self._overall_status = overall_status

    @property
    def stats(self):
        """
        Gets the stats of this Sddc.
        Associated read-only statistics.

        :return: The stats of this Sddc.
        :rtype: SddcStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """
        Sets the stats of this Sddc.
        Associated read-only statistics.

        :param stats: The stats of this Sddc.
        :type: SddcStats
        """

        self._stats = stats

    @property
    def default_proxy(self):
        """
        Gets the default_proxy of this Sddc.
        Default proxy for the SDDC. This field is read-only. To set a new default, edit the proxy you wish to make the new default by modifying its defaultProxy flag. Deprecated in Api 34.0. 

        :return: The default_proxy of this Sddc.
        :rtype: SddcProxy
        """
        return self._default_proxy

    @default_proxy.setter
    def default_proxy(self, default_proxy):
        """
        Sets the default_proxy of this Sddc.
        Default proxy for the SDDC. This field is read-only. To set a new default, edit the proxy you wish to make the new default by modifying its defaultProxy flag. Deprecated in Api 34.0. 

        :param default_proxy: The default_proxy of this Sddc.
        :type: SddcProxy
        """

        self._default_proxy = default_proxy

    @property
    def default_endpoint(self):
        """
        Gets the default_endpoint of this Sddc.
        Default endpoint for the SDDC. There is an endpoint available for an SDDC even if there are no proxies configured for the SDDC. This indicates that an endpoint is available that doesn't require proxying, either because it is publicly accessible or because it assumes an established VPM connection. The field is read-only. 

        :return: The default_endpoint of this Sddc.
        :rtype: SddcEndpoint
        """
        return self._default_endpoint

    @default_endpoint.setter
    def default_endpoint(self, default_endpoint):
        """
        Sets the default_endpoint of this Sddc.
        Default endpoint for the SDDC. There is an endpoint available for an SDDC even if there are no proxies configured for the SDDC. This indicates that an endpoint is available that doesn't require proxying, either because it is publicly accessible or because it assumes an established VPM connection. The field is read-only. 

        :param default_endpoint: The default_endpoint of this Sddc.
        :type: SddcEndpoint
        """

        self._default_endpoint = default_endpoint

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
        if not isinstance(other, Sddc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
