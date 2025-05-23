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


class LoadBalancerController(object):
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
        'description': 'str',
        'url': 'str',
        'username': 'str',
        'password': 'str',
        'license_type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'url': 'url',
        'username': 'username',
        'password': 'password',
        'license_type': 'licenseType',
        'version': 'version'
    }

    def __init__(self, id=None, name=None, description=None, url=None, username=None, password=None, license_type='BASIC', version=None):
        """
        LoadBalancerController - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._description = None
        self._url = None
        self._username = None
        self._password = None
        self._license_type = None
        self._version = None

        if id is not None:
          self.id = id
        self.name = name
        if description is not None:
          self.description = description
        self.url = url
        self.username = username
        self.password = password
        if license_type is not None:
          self.license_type = license_type
        if version is not None:
          self.version = version

    @property
    def id(self):
        """
        Gets the id of this LoadBalancerController.
        The id of the Load Balancer Controller in URN format.

        :return: The id of this LoadBalancerController.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LoadBalancerController.
        The id of the Load Balancer Controller in URN format.

        :param id: The id of this LoadBalancerController.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this LoadBalancerController.
        The name of the Load Balancer Controller. Names for Load Balancer Controllers must be unique across the system.

        :return: The name of this LoadBalancerController.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LoadBalancerController.
        The name of the Load Balancer Controller. Names for Load Balancer Controllers must be unique across the system.

        :param name: The name of this LoadBalancerController.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this LoadBalancerController.
        Description for the registered Load Balancer Controller.

        :return: The description of this LoadBalancerController.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LoadBalancerController.
        Description for the registered Load Balancer Controller.

        :param description: The description of this LoadBalancerController.
        :type: str
        """

        self._description = description

    @property
    def url(self):
        """
        Gets the url of this LoadBalancerController.
        The URL of the Load Balancer Controller. URLs for Load Balancer Controllers must be unique across the system.

        :return: The url of this LoadBalancerController.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this LoadBalancerController.
        The URL of the Load Balancer Controller. URLs for Load Balancer Controllers must be unique across the system.

        :param url: The url of this LoadBalancerController.
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url

    @property
    def username(self):
        """
        Gets the username of this LoadBalancerController.
        Username to connect to the Load Balancer Controller.

        :return: The username of this LoadBalancerController.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this LoadBalancerController.
        Username to connect to the Load Balancer Controller.

        :param username: The username of this LoadBalancerController.
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this LoadBalancerController.
        Cleartext password to connect to the Load Balancer Controller.

        :return: The password of this LoadBalancerController.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this LoadBalancerController.
        Cleartext password to connect to the Load Balancer Controller.

        :param password: The password of this LoadBalancerController.
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")

        self._password = password

    @property
    def license_type(self):
        """
        Gets the license_type of this LoadBalancerController.
        The license type of the Load Balancer Controller. <ul> <li>BASIC - Basic edition of the NSX Advanced Load Balancer. <li>ENTERPRISE - Full featured edition of the NSX Advanced Load Balancer. </ul> 

        :return: The license_type of this LoadBalancerController.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this LoadBalancerController.
        The license type of the Load Balancer Controller. <ul> <li>BASIC - Basic edition of the NSX Advanced Load Balancer. <li>ENTERPRISE - Full featured edition of the NSX Advanced Load Balancer. </ul> 

        :param license_type: The license_type of this LoadBalancerController.
        :type: str
        """

        self._license_type = license_type

    @property
    def version(self):
        """
        Gets the version of this LoadBalancerController.
        The version of the load balancer controller.

        :return: The version of this LoadBalancerController.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this LoadBalancerController.
        The version of the load balancer controller.

        :param version: The version of this LoadBalancerController.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, LoadBalancerController):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
