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


class OrmLLMKnowledgeJob(object):
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
        'edges': 'OrmLLMKnowledgeJobEdges',
        'id': 'int',
        'input_yaml_serialized': 'str',
        'llm_knowledge_id': 'int',
        'number': 'int',
        'run_execution_id': 'int',
        'slug': 'str',
        'status': 'str',
        'status_message': 'str',
        'type': 'str',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'created_by_id': 'created_by_id',
        'created_dt': 'created_dt',
        'edges': 'edges',
        'id': 'id',
        'input_yaml_serialized': 'input_yaml_serialized',
        'llm_knowledge_id': 'llm_knowledge_id',
        'number': 'number',
        'run_execution_id': 'run_execution_id',
        'slug': 'slug',
        'status': 'status',
        'status_message': 'status_message',
        'type': 'type',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, created_by_id=None, created_dt=None, edges=None, id=None, input_yaml_serialized=None, llm_knowledge_id=None, number=None, run_execution_id=None, slug=None, status=None, status_message=None, type=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """OrmLLMKnowledgeJob - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_by_id = None
        self._created_dt = None
        self._edges = None
        self._id = None
        self._input_yaml_serialized = None
        self._llm_knowledge_id = None
        self._number = None
        self._run_execution_id = None
        self._slug = None
        self._status = None
        self._status_message = None
        self._type = None
        self._updated_dt = None
        self.discriminator = None

        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_dt is not None:
            self.created_dt = created_dt
        if edges is not None:
            self.edges = edges
        if id is not None:
            self.id = id
        if input_yaml_serialized is not None:
            self.input_yaml_serialized = input_yaml_serialized
        if llm_knowledge_id is not None:
            self.llm_knowledge_id = llm_knowledge_id
        if number is not None:
            self.number = number
        self.run_execution_id = run_execution_id
        if slug is not None:
            self.slug = slug
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if type is not None:
            self.type = type
        if updated_dt is not None:
            self.updated_dt = updated_dt

    @property
    def created_by_id(self):
        """Gets the created_by_id of this OrmLLMKnowledgeJob.  # noqa: E501


        :return: The created_by_id of this OrmLLMKnowledgeJob.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this OrmLLMKnowledgeJob.


        :param created_by_id: The created_by_id of this OrmLLMKnowledgeJob.  # noqa: E501
        :type created_by_id: int
        """

        self._created_by_id = created_by_id

    @property
    def created_dt(self):
        """Gets the created_dt of this OrmLLMKnowledgeJob.  # noqa: E501


        :return: The created_dt of this OrmLLMKnowledgeJob.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OrmLLMKnowledgeJob.


        :param created_dt: The created_dt of this OrmLLMKnowledgeJob.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this OrmLLMKnowledgeJob.  # noqa: E501


        :return: The edges of this OrmLLMKnowledgeJob.  # noqa: E501
        :rtype: OrmLLMKnowledgeJobEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this OrmLLMKnowledgeJob.


        :param edges: The edges of this OrmLLMKnowledgeJob.  # noqa: E501
        :type edges: OrmLLMKnowledgeJobEdges
        """

        self._edges = edges

    @property
    def id(self):
        """Gets the id of this OrmLLMKnowledgeJob.  # noqa: E501


        :return: The id of this OrmLLMKnowledgeJob.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrmLLMKnowledgeJob.


        :param id: The id of this OrmLLMKnowledgeJob.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def input_yaml_serialized(self):
        """Gets the input_yaml_serialized of this OrmLLMKnowledgeJob.  # noqa: E501


        :return: The input_yaml_serialized of this OrmLLMKnowledgeJob.  # noqa: E501
        :rtype: str
        """
        return self._input_yaml_serialized

    @input_yaml_serialized.setter
    def input_yaml_serialized(self, input_yaml_serialized):
        """Sets the input_yaml_serialized of this OrmLLMKnowledgeJob.


        :param input_yaml_serialized: The input_yaml_serialized of this OrmLLMKnowledgeJob.  # noqa: E501
        :type input_yaml_serialized: str
        """

        self._input_yaml_serialized = input_yaml_serialized

    @property
    def llm_knowledge_id(self):
        """Gets the llm_knowledge_id of this OrmLLMKnowledgeJob.  # noqa: E501


        :return: The llm_knowledge_id of this OrmLLMKnowledgeJob.  # noqa: E501
        :rtype: int
        """
        return self._llm_knowledge_id

    @llm_knowledge_id.setter
    def llm_knowledge_id(self, llm_knowledge_id):
        """Sets the llm_knowledge_id of this OrmLLMKnowledgeJob.


        :param llm_knowledge_id: The llm_knowledge_id of this OrmLLMKnowledgeJob.  # noqa: E501
        :type llm_knowledge_id: int
        """

        self._llm_knowledge_id = llm_knowledge_id

    @property
    def number(self):
        """Gets the number of this OrmLLMKnowledgeJob.  # noqa: E501


        :return: The number of this OrmLLMKnowledgeJob.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this OrmLLMKnowledgeJob.


        :param number: The number of this OrmLLMKnowledgeJob.  # noqa: E501
        :type number: int
        """

        self._number = number

    @property
    def run_execution_id(self):
        """Gets the run_execution_id of this OrmLLMKnowledgeJob.  # noqa: E501


        :return: The run_execution_id of this OrmLLMKnowledgeJob.  # noqa: E501
        :rtype: int
        """
        return self._run_execution_id

    @run_execution_id.setter
    def run_execution_id(self, run_execution_id):
        """Sets the run_execution_id of this OrmLLMKnowledgeJob.


        :param run_execution_id: The run_execution_id of this OrmLLMKnowledgeJob.  # noqa: E501
        :type run_execution_id: int
        """

        self._run_execution_id = run_execution_id

    @property
    def slug(self):
        """Gets the slug of this OrmLLMKnowledgeJob.  # noqa: E501


        :return: The slug of this OrmLLMKnowledgeJob.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this OrmLLMKnowledgeJob.


        :param slug: The slug of this OrmLLMKnowledgeJob.  # noqa: E501
        :type slug: str
        """

        self._slug = slug

    @property
    def status(self):
        """Gets the status of this OrmLLMKnowledgeJob.  # noqa: E501


        :return: The status of this OrmLLMKnowledgeJob.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrmLLMKnowledgeJob.


        :param status: The status of this OrmLLMKnowledgeJob.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this OrmLLMKnowledgeJob.  # noqa: E501


        :return: The status_message of this OrmLLMKnowledgeJob.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this OrmLLMKnowledgeJob.


        :param status_message: The status_message of this OrmLLMKnowledgeJob.  # noqa: E501
        :type status_message: str
        """

        self._status_message = status_message

    @property
    def type(self):
        """Gets the type of this OrmLLMKnowledgeJob.  # noqa: E501


        :return: The type of this OrmLLMKnowledgeJob.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OrmLLMKnowledgeJob.


        :param type: The type of this OrmLLMKnowledgeJob.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OrmLLMKnowledgeJob.  # noqa: E501


        :return: The updated_dt of this OrmLLMKnowledgeJob.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OrmLLMKnowledgeJob.


        :param updated_dt: The updated_dt of this OrmLLMKnowledgeJob.  # noqa: E501
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
        if not isinstance(other, OrmLLMKnowledgeJob):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmLLMKnowledgeJob):
            return True

        return self.to_dict() != other.to_dict()
