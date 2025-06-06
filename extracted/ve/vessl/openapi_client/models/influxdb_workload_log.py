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


class InfluxdbWorkloadLog(object):
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
        'entity': 'str',
        'message': 'str',
        'source': 'str',
        'stream': 'str',
        'timestamp': 'float'
    }

    attribute_map = {
        'entity': 'entity',
        'message': 'message',
        'source': 'source',
        'stream': 'stream',
        'timestamp': 'timestamp'
    }

    def __init__(self, entity=None, message=None, source=None, stream=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """InfluxdbWorkloadLog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._entity = None
        self._message = None
        self._source = None
        self._stream = None
        self._timestamp = None
        self.discriminator = None

        self.entity = entity
        self.message = message
        self.source = source
        self.stream = stream
        self.timestamp = timestamp

    @property
    def entity(self):
        """Gets the entity of this InfluxdbWorkloadLog.  # noqa: E501


        :return: The entity of this InfluxdbWorkloadLog.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this InfluxdbWorkloadLog.


        :param entity: The entity of this InfluxdbWorkloadLog.  # noqa: E501
        :type entity: str
        """
        if self.local_vars_configuration.client_side_validation and entity is None:  # noqa: E501
            raise ValueError("Invalid value for `entity`, must not be `None`")  # noqa: E501

        self._entity = entity

    @property
    def message(self):
        """Gets the message of this InfluxdbWorkloadLog.  # noqa: E501


        :return: The message of this InfluxdbWorkloadLog.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InfluxdbWorkloadLog.


        :param message: The message of this InfluxdbWorkloadLog.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def source(self):
        """Gets the source of this InfluxdbWorkloadLog.  # noqa: E501


        :return: The source of this InfluxdbWorkloadLog.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this InfluxdbWorkloadLog.


        :param source: The source of this InfluxdbWorkloadLog.  # noqa: E501
        :type source: str
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def stream(self):
        """Gets the stream of this InfluxdbWorkloadLog.  # noqa: E501


        :return: The stream of this InfluxdbWorkloadLog.  # noqa: E501
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this InfluxdbWorkloadLog.


        :param stream: The stream of this InfluxdbWorkloadLog.  # noqa: E501
        :type stream: str
        """
        if self.local_vars_configuration.client_side_validation and stream is None:  # noqa: E501
            raise ValueError("Invalid value for `stream`, must not be `None`")  # noqa: E501

        self._stream = stream

    @property
    def timestamp(self):
        """Gets the timestamp of this InfluxdbWorkloadLog.  # noqa: E501


        :return: The timestamp of this InfluxdbWorkloadLog.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this InfluxdbWorkloadLog.


        :param timestamp: The timestamp of this InfluxdbWorkloadLog.  # noqa: E501
        :type timestamp: float
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

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
        if not isinstance(other, InfluxdbWorkloadLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InfluxdbWorkloadLog):
            return True

        return self.to_dict() != other.to_dict()
