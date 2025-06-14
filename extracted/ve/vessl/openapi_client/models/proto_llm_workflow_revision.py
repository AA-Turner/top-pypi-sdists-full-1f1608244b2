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


class ProtoLLMWorkflowRevision(object):
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
        'created_by': 'ProtoUser',
        'created_by_id': 'int',
        'created_dt': 'float',
        'id': 'int',
        'is_starred': 'bool',
        'message': 'str',
        'number': 'int',
        'spec': 'V1WorkflowRevisionSpec',
        'tags': 'list[ProtoTag]',
        'updated_dt': 'float',
        'workflow_id': 'int'
    }

    attribute_map = {
        'created_by': 'created_by',
        'created_by_id': 'created_by_id',
        'created_dt': 'created_dt',
        'id': 'id',
        'is_starred': 'is_starred',
        'message': 'message',
        'number': 'number',
        'spec': 'spec',
        'tags': 'tags',
        'updated_dt': 'updated_dt',
        'workflow_id': 'workflow_id'
    }

    def __init__(self, created_by=None, created_by_id=None, created_dt=None, id=None, is_starred=None, message=None, number=None, spec=None, tags=None, updated_dt=None, workflow_id=None, local_vars_configuration=None):  # noqa: E501
        """ProtoLLMWorkflowRevision - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_by = None
        self._created_by_id = None
        self._created_dt = None
        self._id = None
        self._is_starred = None
        self._message = None
        self._number = None
        self._spec = None
        self._tags = None
        self._updated_dt = None
        self._workflow_id = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        self.created_by_id = created_by_id
        self.created_dt = created_dt
        self.id = id
        if is_starred is not None:
            self.is_starred = is_starred
        if message is not None:
            self.message = message
        self.number = number
        self.spec = spec
        if tags is not None:
            self.tags = tags
        self.updated_dt = updated_dt
        self.workflow_id = workflow_id

    @property
    def created_by(self):
        """Gets the created_by of this ProtoLLMWorkflowRevision.  # noqa: E501


        :return: The created_by of this ProtoLLMWorkflowRevision.  # noqa: E501
        :rtype: ProtoUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ProtoLLMWorkflowRevision.


        :param created_by: The created_by of this ProtoLLMWorkflowRevision.  # noqa: E501
        :type created_by: ProtoUser
        """

        self._created_by = created_by

    @property
    def created_by_id(self):
        """Gets the created_by_id of this ProtoLLMWorkflowRevision.  # noqa: E501


        :return: The created_by_id of this ProtoLLMWorkflowRevision.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this ProtoLLMWorkflowRevision.


        :param created_by_id: The created_by_id of this ProtoLLMWorkflowRevision.  # noqa: E501
        :type created_by_id: int
        """
        if self.local_vars_configuration.client_side_validation and created_by_id is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by_id`, must not be `None`")  # noqa: E501

        self._created_by_id = created_by_id

    @property
    def created_dt(self):
        """Gets the created_dt of this ProtoLLMWorkflowRevision.  # noqa: E501


        :return: The created_dt of this ProtoLLMWorkflowRevision.  # noqa: E501
        :rtype: float
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ProtoLLMWorkflowRevision.


        :param created_dt: The created_dt of this ProtoLLMWorkflowRevision.  # noqa: E501
        :type created_dt: float
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def id(self):
        """Gets the id of this ProtoLLMWorkflowRevision.  # noqa: E501


        :return: The id of this ProtoLLMWorkflowRevision.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProtoLLMWorkflowRevision.


        :param id: The id of this ProtoLLMWorkflowRevision.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_starred(self):
        """Gets the is_starred of this ProtoLLMWorkflowRevision.  # noqa: E501


        :return: The is_starred of this ProtoLLMWorkflowRevision.  # noqa: E501
        :rtype: bool
        """
        return self._is_starred

    @is_starred.setter
    def is_starred(self, is_starred):
        """Sets the is_starred of this ProtoLLMWorkflowRevision.


        :param is_starred: The is_starred of this ProtoLLMWorkflowRevision.  # noqa: E501
        :type is_starred: bool
        """

        self._is_starred = is_starred

    @property
    def message(self):
        """Gets the message of this ProtoLLMWorkflowRevision.  # noqa: E501


        :return: The message of this ProtoLLMWorkflowRevision.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ProtoLLMWorkflowRevision.


        :param message: The message of this ProtoLLMWorkflowRevision.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def number(self):
        """Gets the number of this ProtoLLMWorkflowRevision.  # noqa: E501


        :return: The number of this ProtoLLMWorkflowRevision.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ProtoLLMWorkflowRevision.


        :param number: The number of this ProtoLLMWorkflowRevision.  # noqa: E501
        :type number: int
        """
        if self.local_vars_configuration.client_side_validation and number is None:  # noqa: E501
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def spec(self):
        """Gets the spec of this ProtoLLMWorkflowRevision.  # noqa: E501


        :return: The spec of this ProtoLLMWorkflowRevision.  # noqa: E501
        :rtype: V1WorkflowRevisionSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ProtoLLMWorkflowRevision.


        :param spec: The spec of this ProtoLLMWorkflowRevision.  # noqa: E501
        :type spec: V1WorkflowRevisionSpec
        """
        if self.local_vars_configuration.client_side_validation and spec is None:  # noqa: E501
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501

        self._spec = spec

    @property
    def tags(self):
        """Gets the tags of this ProtoLLMWorkflowRevision.  # noqa: E501


        :return: The tags of this ProtoLLMWorkflowRevision.  # noqa: E501
        :rtype: list[ProtoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ProtoLLMWorkflowRevision.


        :param tags: The tags of this ProtoLLMWorkflowRevision.  # noqa: E501
        :type tags: list[ProtoTag]
        """

        self._tags = tags

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ProtoLLMWorkflowRevision.  # noqa: E501


        :return: The updated_dt of this ProtoLLMWorkflowRevision.  # noqa: E501
        :rtype: float
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ProtoLLMWorkflowRevision.


        :param updated_dt: The updated_dt of this ProtoLLMWorkflowRevision.  # noqa: E501
        :type updated_dt: float
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def workflow_id(self):
        """Gets the workflow_id of this ProtoLLMWorkflowRevision.  # noqa: E501


        :return: The workflow_id of this ProtoLLMWorkflowRevision.  # noqa: E501
        :rtype: int
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this ProtoLLMWorkflowRevision.


        :param workflow_id: The workflow_id of this ProtoLLMWorkflowRevision.  # noqa: E501
        :type workflow_id: int
        """
        if self.local_vars_configuration.client_side_validation and workflow_id is None:  # noqa: E501
            raise ValueError("Invalid value for `workflow_id`, must not be `None`")  # noqa: E501

        self._workflow_id = workflow_id

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
        if not isinstance(other, ProtoLLMWorkflowRevision):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProtoLLMWorkflowRevision):
            return True

        return self.to_dict() != other.to_dict()
