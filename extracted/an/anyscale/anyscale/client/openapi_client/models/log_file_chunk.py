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


class LogFileChunk(object):
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
        'cluster_id': 'str',
        'chunk_name': 'str',
        'chunk_url': 'str',
        'size': 'int',
        'file_name': 'str',
        'node_type': 'NodeType',
        'node_ip': 'str',
        'instance_id': 'str',
        'session_id': 'str',
        'ray_pid': 'str',
        'ray_worker_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'chunk_name': 'chunk_name',
        'chunk_url': 'chunk_url',
        'size': 'size',
        'file_name': 'file_name',
        'node_type': 'node_type',
        'node_ip': 'node_ip',
        'instance_id': 'instance_id',
        'session_id': 'session_id',
        'ray_pid': 'ray_pid',
        'ray_worker_id': 'ray_worker_id',
        'job_id': 'job_id'
    }

    def __init__(self, cluster_id=None, chunk_name=None, chunk_url=None, size=None, file_name=None, node_type=None, node_ip=None, instance_id=None, session_id=None, ray_pid=None, ray_worker_id=None, job_id=None, local_vars_configuration=None):  # noqa: E501
        """LogFileChunk - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_id = None
        self._chunk_name = None
        self._chunk_url = None
        self._size = None
        self._file_name = None
        self._node_type = None
        self._node_ip = None
        self._instance_id = None
        self._session_id = None
        self._ray_pid = None
        self._ray_worker_id = None
        self._job_id = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.chunk_name = chunk_name
        self.chunk_url = chunk_url
        self.size = size
        self.file_name = file_name
        self.node_type = node_type
        self.node_ip = node_ip
        self.instance_id = instance_id
        self.session_id = session_id
        if ray_pid is not None:
            self.ray_pid = ray_pid
        if ray_worker_id is not None:
            self.ray_worker_id = ray_worker_id
        if job_id is not None:
            self.job_id = job_id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this LogFileChunk.  # noqa: E501

        The cluster ID that this file originates from.  # noqa: E501

        :return: The cluster_id of this LogFileChunk.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this LogFileChunk.

        The cluster ID that this file originates from.  # noqa: E501

        :param cluster_id: The cluster_id of this LogFileChunk.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def chunk_name(self):
        """Gets the chunk_name of this LogFileChunk.  # noqa: E501

        The full object name of a chunk (e.g. .../dashboard_agent.log/chunk-one.log)  # noqa: E501

        :return: The chunk_name of this LogFileChunk.  # noqa: E501
        :rtype: str
        """
        return self._chunk_name

    @chunk_name.setter
    def chunk_name(self, chunk_name):
        """Sets the chunk_name of this LogFileChunk.

        The full object name of a chunk (e.g. .../dashboard_agent.log/chunk-one.log)  # noqa: E501

        :param chunk_name: The chunk_name of this LogFileChunk.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and chunk_name is None:  # noqa: E501
            raise ValueError("Invalid value for `chunk_name`, must not be `None`")  # noqa: E501

        self._chunk_name = chunk_name

    @property
    def chunk_url(self):
        """Gets the chunk_url of this LogFileChunk.  # noqa: E501

        A presigned URL to download this chunk.  # noqa: E501

        :return: The chunk_url of this LogFileChunk.  # noqa: E501
        :rtype: str
        """
        return self._chunk_url

    @chunk_url.setter
    def chunk_url(self, chunk_url):
        """Sets the chunk_url of this LogFileChunk.

        A presigned URL to download this chunk.  # noqa: E501

        :param chunk_url: The chunk_url of this LogFileChunk.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and chunk_url is None:  # noqa: E501
            raise ValueError("Invalid value for `chunk_url`, must not be `None`")  # noqa: E501

        self._chunk_url = chunk_url

    @property
    def size(self):
        """Gets the size of this LogFileChunk.  # noqa: E501

        The size of this chunk (should never exceed 10MB).  # noqa: E501

        :return: The size of this LogFileChunk.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LogFileChunk.

        The size of this chunk (should never exceed 10MB).  # noqa: E501

        :param size: The size of this LogFileChunk.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def file_name(self):
        """Gets the file_name of this LogFileChunk.  # noqa: E501

        The full file name (path) of a file (e.g. .../dashboard_agent.log  # noqa: E501

        :return: The file_name of this LogFileChunk.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this LogFileChunk.

        The full file name (path) of a file (e.g. .../dashboard_agent.log  # noqa: E501

        :param file_name: The file_name of this LogFileChunk.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and file_name is None:  # noqa: E501
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def node_type(self):
        """Gets the node_type of this LogFileChunk.  # noqa: E501

        The type of node that this file originated from (e.g. head-node, worker-nodes  # noqa: E501

        :return: The node_type of this LogFileChunk.  # noqa: E501
        :rtype: NodeType
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this LogFileChunk.

        The type of node that this file originated from (e.g. head-node, worker-nodes  # noqa: E501

        :param node_type: The node_type of this LogFileChunk.  # noqa: E501
        :type: NodeType
        """
        if self.local_vars_configuration.client_side_validation and node_type is None:  # noqa: E501
            raise ValueError("Invalid value for `node_type`, must not be `None`")  # noqa: E501

        self._node_type = node_type

    @property
    def node_ip(self):
        """Gets the node_ip of this LogFileChunk.  # noqa: E501

        The node IP that this file originated from.  # noqa: E501

        :return: The node_ip of this LogFileChunk.  # noqa: E501
        :rtype: str
        """
        return self._node_ip

    @node_ip.setter
    def node_ip(self, node_ip):
        """Sets the node_ip of this LogFileChunk.

        The node IP that this file originated from.  # noqa: E501

        :param node_ip: The node_ip of this LogFileChunk.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and node_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `node_ip`, must not be `None`")  # noqa: E501

        self._node_ip = node_ip

    @property
    def instance_id(self):
        """Gets the instance_id of this LogFileChunk.  # noqa: E501

        The instance ID that this file originated from.  # noqa: E501

        :return: The instance_id of this LogFileChunk.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this LogFileChunk.

        The instance ID that this file originated from.  # noqa: E501

        :param instance_id: The instance_id of this LogFileChunk.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and instance_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def session_id(self):
        """Gets the session_id of this LogFileChunk.  # noqa: E501

        The session ID that this file originated from.  # noqa: E501

        :return: The session_id of this LogFileChunk.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this LogFileChunk.

        The session ID that this file originated from.  # noqa: E501

        :param session_id: The session_id of this LogFileChunk.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and session_id is None:  # noqa: E501
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

    @property
    def ray_pid(self):
        """Gets the ray_pid of this LogFileChunk.  # noqa: E501

        The PID that this file originated from, if appropriate.  # noqa: E501

        :return: The ray_pid of this LogFileChunk.  # noqa: E501
        :rtype: str
        """
        return self._ray_pid

    @ray_pid.setter
    def ray_pid(self, ray_pid):
        """Sets the ray_pid of this LogFileChunk.

        The PID that this file originated from, if appropriate.  # noqa: E501

        :param ray_pid: The ray_pid of this LogFileChunk.  # noqa: E501
        :type: str
        """

        self._ray_pid = ray_pid

    @property
    def ray_worker_id(self):
        """Gets the ray_worker_id of this LogFileChunk.  # noqa: E501

        The Ray worker ID that this file originated from, if appropriate.  # noqa: E501

        :return: The ray_worker_id of this LogFileChunk.  # noqa: E501
        :rtype: str
        """
        return self._ray_worker_id

    @ray_worker_id.setter
    def ray_worker_id(self, ray_worker_id):
        """Sets the ray_worker_id of this LogFileChunk.

        The Ray worker ID that this file originated from, if appropriate.  # noqa: E501

        :param ray_worker_id: The ray_worker_id of this LogFileChunk.  # noqa: E501
        :type: str
        """

        self._ray_worker_id = ray_worker_id

    @property
    def job_id(self):
        """Gets the job_id of this LogFileChunk.  # noqa: E501

        The Ray job ID that this file originated from, if appropriate.  # noqa: E501

        :return: The job_id of this LogFileChunk.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this LogFileChunk.

        The Ray job ID that this file originated from, if appropriate.  # noqa: E501

        :param job_id: The job_id of this LogFileChunk.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

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
        if not isinstance(other, LogFileChunk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LogFileChunk):
            return True

        return self.to_dict() != other.to_dict()
