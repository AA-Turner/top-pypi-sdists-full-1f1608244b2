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


class DefinedEntity(object):
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
        'entity_type': 'str',
        'name': 'str',
        'external_id': 'str',
        'entity': 'dict(str, object)',
        'state': 'str',
        'owner': 'EntityReference',
        'org': 'EntityReference'
    }

    attribute_map = {
        'id': 'id',
        'entity_type': 'entityType',
        'name': 'name',
        'external_id': 'externalId',
        'entity': 'entity',
        'state': 'state',
        'owner': 'owner',
        'org': 'org'
    }

    def __init__(self, id=None, entity_type=None, name=None, external_id=None, entity=None, state=None, owner=None, org=None):
        """
        DefinedEntity - a model defined in Swagger
        """

        self._id = None
        self._entity_type = None
        self._name = None
        self._external_id = None
        self._entity = None
        self._state = None
        self._owner = None
        self._org = None

        if id is not None:
          self.id = id
        if entity_type is not None:
          self.entity_type = entity_type
        self.name = name
        if external_id is not None:
          self.external_id = external_id
        self.entity = entity
        if state is not None:
          self.state = state
        if owner is not None:
          self.owner = owner
        if org is not None:
          self.org = org

    @property
    def id(self):
        """
        Gets the id of this DefinedEntity.
        The id of the defined entity in URN format. 

        :return: The id of this DefinedEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DefinedEntity.
        The id of the defined entity in URN format. 

        :param id: The id of this DefinedEntity.
        :type: str
        """

        self._id = id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this DefinedEntity.
        The URN ID of the defined entity type that the entity is an instance of. This is a read-only field. 

        :return: The entity_type of this DefinedEntity.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this DefinedEntity.
        The URN ID of the defined entity type that the entity is an instance of. This is a read-only field. 

        :param entity_type: The entity_type of this DefinedEntity.
        :type: str
        """

        self._entity_type = entity_type

    @property
    def name(self):
        """
        Gets the name of this DefinedEntity.
        The name of the defined entity. 

        :return: The name of this DefinedEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DefinedEntity.
        The name of the defined entity. 

        :param name: The name of this DefinedEntity.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def external_id(self):
        """
        Gets the external_id of this DefinedEntity.
        An external entity's id that this entity may have a relation to. 

        :return: The external_id of this DefinedEntity.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this DefinedEntity.
        An external entity's id that this entity may have a relation to. 

        :param external_id: The external_id of this DefinedEntity.
        :type: str
        """

        self._external_id = external_id

    @property
    def entity(self):
        """
        Gets the entity of this DefinedEntity.
        A JSON value representation. The JSON will be validated against the schema of the entityType that the entity is an instance of. 

        :return: The entity of this DefinedEntity.
        :rtype: dict(str, object)
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this DefinedEntity.
        A JSON value representation. The JSON will be validated against the schema of the entityType that the entity is an instance of. 

        :param entity: The entity of this DefinedEntity.
        :type: dict(str, object)
        """
        if entity is None:
            raise ValueError("Invalid value for `entity`, must not be `None`")

        self._entity = entity

    @property
    def state(self):
        """
        Gets the state of this DefinedEntity.
        Every entity is created in the \"PRE_CREATED\" state. Once an entity is ready to be validated against its schema, it will transition in another state - RESOLVED, if the entity is valid according to the schema, or RESOLUTION_ERROR otherwise. If an entity in an \"RESOLUTION_ERROR\" state is updated, it will transition to the inital \"PRE_CREATED\" state without performing any validation. If its in the \"RESOLVED\" state, then it will be validated against the entity type schema and throw an exception if its invalid. 

        :return: The state of this DefinedEntity.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this DefinedEntity.
        Every entity is created in the \"PRE_CREATED\" state. Once an entity is ready to be validated against its schema, it will transition in another state - RESOLVED, if the entity is valid according to the schema, or RESOLUTION_ERROR otherwise. If an entity in an \"RESOLUTION_ERROR\" state is updated, it will transition to the inital \"PRE_CREATED\" state without performing any validation. If its in the \"RESOLVED\" state, then it will be validated against the entity type schema and throw an exception if its invalid. 

        :param state: The state of this DefinedEntity.
        :type: str
        """
        allowed_values = ["PRE_CREATED", "RESOLVED", "RESOLUTION_ERROR"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def owner(self):
        """
        Gets the owner of this DefinedEntity.
        The owner of the defined entity.

        :return: The owner of this DefinedEntity.
        :rtype: EntityReference
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this DefinedEntity.
        The owner of the defined entity.

        :param owner: The owner of this DefinedEntity.
        :type: EntityReference
        """

        self._owner = owner

    @property
    def org(self):
        """
        Gets the org of this DefinedEntity.
        The organization of the defined entity.

        :return: The org of this DefinedEntity.
        :rtype: EntityReference
        """
        return self._org

    @org.setter
    def org(self, org):
        """
        Sets the org of this DefinedEntity.
        The organization of the defined entity.

        :param org: The org of this DefinedEntity.
        :type: EntityReference
        """

        self._org = org

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
        if not isinstance(other, DefinedEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
