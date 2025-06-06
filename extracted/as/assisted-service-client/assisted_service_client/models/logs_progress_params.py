# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LogsProgressParams(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'logs_state': 'LogsState'
    }

    attribute_map = {
        'logs_state': 'logs_state'
    }

    def __init__(self, logs_state=None):  # noqa: E501
        """LogsProgressParams - a model defined in Swagger"""  # noqa: E501

        self._logs_state = None
        self.discriminator = None

        self.logs_state = logs_state

    @property
    def logs_state(self):
        """Gets the logs_state of this LogsProgressParams.  # noqa: E501

        The state of collecting logs.  # noqa: E501

        :return: The logs_state of this LogsProgressParams.  # noqa: E501
        :rtype: LogsState
        """
        return self._logs_state

    @logs_state.setter
    def logs_state(self, logs_state):
        """Sets the logs_state of this LogsProgressParams.

        The state of collecting logs.  # noqa: E501

        :param logs_state: The logs_state of this LogsProgressParams.  # noqa: E501
        :type: LogsState
        """
        if logs_state is None:
            raise ValueError("Invalid value for `logs_state`, must not be `None`")  # noqa: E501

        self._logs_state = logs_state

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(LogsProgressParams, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LogsProgressParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
