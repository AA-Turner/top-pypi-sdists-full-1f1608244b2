# coding: utf-8

"""
    Managed Ray API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class WorkspaceEvent(object):
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
        'id': 'str',
        'cluster_id': 'str',
        'workspace_id': 'str',
        'created_at': 'datetime',
        'level': 'EventLevel',
        'source': 'WorkspaceEventSource',
        'message': 'str',
        'metadata': 'object'
    }

    attribute_map = {
        'id': 'id',
        'cluster_id': 'cluster_id',
        'workspace_id': 'workspace_id',
        'created_at': 'created_at',
        'level': 'level',
        'source': 'source',
        'message': 'message',
        'metadata': 'metadata'
    }

    def __init__(self, id=None, cluster_id=None, workspace_id=None, created_at=None, level=None, source=None, message=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """WorkspaceEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._cluster_id = None
        self._workspace_id = None
        self._created_at = None
        self._level = None
        self._source = None
        self._message = None
        self._metadata = None
        self.discriminator = None

        self.id = id
        self.cluster_id = cluster_id
        self.workspace_id = workspace_id
        self.created_at = created_at
        self.level = level
        self.source = source
        self.message = message
        if metadata is not None:
            self.metadata = metadata

    @property
    def id(self):
        """Gets the id of this WorkspaceEvent.  # noqa: E501

        The unique identifier for the workspace event  # noqa: E501

        :return: The id of this WorkspaceEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkspaceEvent.

        The unique identifier for the workspace event  # noqa: E501

        :param id: The id of this WorkspaceEvent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this WorkspaceEvent.  # noqa: E501

        The cluster the event originated from  # noqa: E501

        :return: The cluster_id of this WorkspaceEvent.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this WorkspaceEvent.

        The cluster the event originated from  # noqa: E501

        :param cluster_id: The cluster_id of this WorkspaceEvent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this WorkspaceEvent.  # noqa: E501

        The workspace the event originated from  # noqa: E501

        :return: The workspace_id of this WorkspaceEvent.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this WorkspaceEvent.

        The workspace the event originated from  # noqa: E501

        :param workspace_id: The workspace_id of this WorkspaceEvent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and workspace_id is None:  # noqa: E501
            raise ValueError("Invalid value for `workspace_id`, must not be `None`")  # noqa: E501

        self._workspace_id = workspace_id

    @property
    def created_at(self):
        """Gets the created_at of this WorkspaceEvent.  # noqa: E501

        The time the event was emitted  # noqa: E501

        :return: The created_at of this WorkspaceEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WorkspaceEvent.

        The time the event was emitted  # noqa: E501

        :param created_at: The created_at of this WorkspaceEvent.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def level(self):
        """Gets the level of this WorkspaceEvent.  # noqa: E501

        The level of the event  # noqa: E501

        :return: The level of this WorkspaceEvent.  # noqa: E501
        :rtype: EventLevel
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this WorkspaceEvent.

        The level of the event  # noqa: E501

        :param level: The level of this WorkspaceEvent.  # noqa: E501
        :type: EventLevel
        """
        if self.local_vars_configuration.client_side_validation and level is None:  # noqa: E501
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def source(self):
        """Gets the source of this WorkspaceEvent.  # noqa: E501

        The source of the event  # noqa: E501

        :return: The source of this WorkspaceEvent.  # noqa: E501
        :rtype: WorkspaceEventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this WorkspaceEvent.

        The source of the event  # noqa: E501

        :param source: The source of this WorkspaceEvent.  # noqa: E501
        :type: WorkspaceEventSource
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def message(self):
        """Gets the message of this WorkspaceEvent.  # noqa: E501

        The message of the event  # noqa: E501

        :return: The message of this WorkspaceEvent.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this WorkspaceEvent.

        The message of the event  # noqa: E501

        :param message: The message of this WorkspaceEvent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def metadata(self):
        """Gets the metadata of this WorkspaceEvent.  # noqa: E501

        The metadata of the event  # noqa: E501

        :return: The metadata of this WorkspaceEvent.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this WorkspaceEvent.

        The metadata of the event  # noqa: E501

        :param metadata: The metadata of this WorkspaceEvent.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkspaceEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkspaceEvent):
            return True

        return self.to_dict() != other.to_dict()
