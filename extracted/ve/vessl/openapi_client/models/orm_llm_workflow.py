# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class OrmLLMWorkflow(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'created_by_id': 'int',
        'created_dt': 'datetime',
        'default_resource_spec_id': 'int',
        'description': 'str',
        'edges': 'OrmLLMWorkflowEdges',
        'id': 'int',
        'last_deployed_revision_number': 'int',
        'model_service_id': 'int',
        'name': 'str',
        'organization_id': 'int',
        'slug': 'str',
        'status': 'str',
        'test_session_run_execution_id': 'int',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'created_by_id': 'created_by_id',
        'created_dt': 'created_dt',
        'default_resource_spec_id': 'default_resource_spec_id',
        'description': 'description',
        'edges': 'edges',
        'id': 'id',
        'last_deployed_revision_number': 'last_deployed_revision_number',
        'model_service_id': 'model_service_id',
        'name': 'name',
        'organization_id': 'organization_id',
        'slug': 'slug',
        'status': 'status',
        'test_session_run_execution_id': 'test_session_run_execution_id',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, created_by_id=None, created_dt=None, default_resource_spec_id=None, description=None, edges=None, id=None, last_deployed_revision_number=None, model_service_id=None, name=None, organization_id=None, slug=None, status=None, test_session_run_execution_id=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """OrmLLMWorkflow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_by_id = None
        self._created_dt = None
        self._default_resource_spec_id = None
        self._description = None
        self._edges = None
        self._id = None
        self._last_deployed_revision_number = None
        self._model_service_id = None
        self._name = None
        self._organization_id = None
        self._slug = None
        self._status = None
        self._test_session_run_execution_id = None
        self._updated_dt = None
        self.discriminator = None

        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_dt is not None:
            self.created_dt = created_dt
        self.default_resource_spec_id = default_resource_spec_id
        if description is not None:
            self.description = description
        if edges is not None:
            self.edges = edges
        if id is not None:
            self.id = id
        self.last_deployed_revision_number = last_deployed_revision_number
        if model_service_id is not None:
            self.model_service_id = model_service_id
        if name is not None:
            self.name = name
        if organization_id is not None:
            self.organization_id = organization_id
        if slug is not None:
            self.slug = slug
        if status is not None:
            self.status = status
        self.test_session_run_execution_id = test_session_run_execution_id
        if updated_dt is not None:
            self.updated_dt = updated_dt

    @property
    def created_by_id(self):
        """Gets the created_by_id of this OrmLLMWorkflow.  # noqa: E501


        :return: The created_by_id of this OrmLLMWorkflow.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this OrmLLMWorkflow.


        :param created_by_id: The created_by_id of this OrmLLMWorkflow.  # noqa: E501
        :type created_by_id: int
        """

        self._created_by_id = created_by_id

    @property
    def created_dt(self):
        """Gets the created_dt of this OrmLLMWorkflow.  # noqa: E501


        :return: The created_dt of this OrmLLMWorkflow.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OrmLLMWorkflow.


        :param created_dt: The created_dt of this OrmLLMWorkflow.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def default_resource_spec_id(self):
        """Gets the default_resource_spec_id of this OrmLLMWorkflow.  # noqa: E501


        :return: The default_resource_spec_id of this OrmLLMWorkflow.  # noqa: E501
        :rtype: int
        """
        return self._default_resource_spec_id

    @default_resource_spec_id.setter
    def default_resource_spec_id(self, default_resource_spec_id):
        """Sets the default_resource_spec_id of this OrmLLMWorkflow.


        :param default_resource_spec_id: The default_resource_spec_id of this OrmLLMWorkflow.  # noqa: E501
        :type default_resource_spec_id: int
        """

        self._default_resource_spec_id = default_resource_spec_id

    @property
    def description(self):
        """Gets the description of this OrmLLMWorkflow.  # noqa: E501


        :return: The description of this OrmLLMWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OrmLLMWorkflow.


        :param description: The description of this OrmLLMWorkflow.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def edges(self):
        """Gets the edges of this OrmLLMWorkflow.  # noqa: E501


        :return: The edges of this OrmLLMWorkflow.  # noqa: E501
        :rtype: OrmLLMWorkflowEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this OrmLLMWorkflow.


        :param edges: The edges of this OrmLLMWorkflow.  # noqa: E501
        :type edges: OrmLLMWorkflowEdges
        """

        self._edges = edges

    @property
    def id(self):
        """Gets the id of this OrmLLMWorkflow.  # noqa: E501


        :return: The id of this OrmLLMWorkflow.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrmLLMWorkflow.


        :param id: The id of this OrmLLMWorkflow.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def last_deployed_revision_number(self):
        """Gets the last_deployed_revision_number of this OrmLLMWorkflow.  # noqa: E501


        :return: The last_deployed_revision_number of this OrmLLMWorkflow.  # noqa: E501
        :rtype: int
        """
        return self._last_deployed_revision_number

    @last_deployed_revision_number.setter
    def last_deployed_revision_number(self, last_deployed_revision_number):
        """Sets the last_deployed_revision_number of this OrmLLMWorkflow.


        :param last_deployed_revision_number: The last_deployed_revision_number of this OrmLLMWorkflow.  # noqa: E501
        :type last_deployed_revision_number: int
        """

        self._last_deployed_revision_number = last_deployed_revision_number

    @property
    def model_service_id(self):
        """Gets the model_service_id of this OrmLLMWorkflow.  # noqa: E501


        :return: The model_service_id of this OrmLLMWorkflow.  # noqa: E501
        :rtype: int
        """
        return self._model_service_id

    @model_service_id.setter
    def model_service_id(self, model_service_id):
        """Sets the model_service_id of this OrmLLMWorkflow.


        :param model_service_id: The model_service_id of this OrmLLMWorkflow.  # noqa: E501
        :type model_service_id: int
        """

        self._model_service_id = model_service_id

    @property
    def name(self):
        """Gets the name of this OrmLLMWorkflow.  # noqa: E501


        :return: The name of this OrmLLMWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrmLLMWorkflow.


        :param name: The name of this OrmLLMWorkflow.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this OrmLLMWorkflow.  # noqa: E501


        :return: The organization_id of this OrmLLMWorkflow.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this OrmLLMWorkflow.


        :param organization_id: The organization_id of this OrmLLMWorkflow.  # noqa: E501
        :type organization_id: int
        """

        self._organization_id = organization_id

    @property
    def slug(self):
        """Gets the slug of this OrmLLMWorkflow.  # noqa: E501


        :return: The slug of this OrmLLMWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this OrmLLMWorkflow.


        :param slug: The slug of this OrmLLMWorkflow.  # noqa: E501
        :type slug: str
        """

        self._slug = slug

    @property
    def status(self):
        """Gets the status of this OrmLLMWorkflow.  # noqa: E501


        :return: The status of this OrmLLMWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrmLLMWorkflow.


        :param status: The status of this OrmLLMWorkflow.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def test_session_run_execution_id(self):
        """Gets the test_session_run_execution_id of this OrmLLMWorkflow.  # noqa: E501


        :return: The test_session_run_execution_id of this OrmLLMWorkflow.  # noqa: E501
        :rtype: int
        """
        return self._test_session_run_execution_id

    @test_session_run_execution_id.setter
    def test_session_run_execution_id(self, test_session_run_execution_id):
        """Sets the test_session_run_execution_id of this OrmLLMWorkflow.


        :param test_session_run_execution_id: The test_session_run_execution_id of this OrmLLMWorkflow.  # noqa: E501
        :type test_session_run_execution_id: int
        """

        self._test_session_run_execution_id = test_session_run_execution_id

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OrmLLMWorkflow.  # noqa: E501


        :return: The updated_dt of this OrmLLMWorkflow.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OrmLLMWorkflow.


        :param updated_dt: The updated_dt of this OrmLLMWorkflow.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrmLLMWorkflow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmLLMWorkflow):
            return True

        return self.to_dict() != other.to_dict()
