# coding: utf-8

"""
    vod20250101

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ConvertModelForGetExecutionOutput(object):
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
        'doubao_input_tokens': 'int',
        'doubao_output_tokens': 'int',
        'doubao_total_tokens': 'int'
    }

    attribute_map = {
        'doubao_input_tokens': 'DoubaoInputTokens',
        'doubao_output_tokens': 'DoubaoOutputTokens',
        'doubao_total_tokens': 'DoubaoTotalTokens'
    }

    def __init__(self, doubao_input_tokens=None, doubao_output_tokens=None, doubao_total_tokens=None, _configuration=None):  # noqa: E501
        """ConvertModelForGetExecutionOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._doubao_input_tokens = None
        self._doubao_output_tokens = None
        self._doubao_total_tokens = None
        self.discriminator = None

        if doubao_input_tokens is not None:
            self.doubao_input_tokens = doubao_input_tokens
        if doubao_output_tokens is not None:
            self.doubao_output_tokens = doubao_output_tokens
        if doubao_total_tokens is not None:
            self.doubao_total_tokens = doubao_total_tokens

    @property
    def doubao_input_tokens(self):
        """Gets the doubao_input_tokens of this ConvertModelForGetExecutionOutput.  # noqa: E501


        :return: The doubao_input_tokens of this ConvertModelForGetExecutionOutput.  # noqa: E501
        :rtype: int
        """
        return self._doubao_input_tokens

    @doubao_input_tokens.setter
    def doubao_input_tokens(self, doubao_input_tokens):
        """Sets the doubao_input_tokens of this ConvertModelForGetExecutionOutput.


        :param doubao_input_tokens: The doubao_input_tokens of this ConvertModelForGetExecutionOutput.  # noqa: E501
        :type: int
        """

        self._doubao_input_tokens = doubao_input_tokens

    @property
    def doubao_output_tokens(self):
        """Gets the doubao_output_tokens of this ConvertModelForGetExecutionOutput.  # noqa: E501


        :return: The doubao_output_tokens of this ConvertModelForGetExecutionOutput.  # noqa: E501
        :rtype: int
        """
        return self._doubao_output_tokens

    @doubao_output_tokens.setter
    def doubao_output_tokens(self, doubao_output_tokens):
        """Sets the doubao_output_tokens of this ConvertModelForGetExecutionOutput.


        :param doubao_output_tokens: The doubao_output_tokens of this ConvertModelForGetExecutionOutput.  # noqa: E501
        :type: int
        """

        self._doubao_output_tokens = doubao_output_tokens

    @property
    def doubao_total_tokens(self):
        """Gets the doubao_total_tokens of this ConvertModelForGetExecutionOutput.  # noqa: E501


        :return: The doubao_total_tokens of this ConvertModelForGetExecutionOutput.  # noqa: E501
        :rtype: int
        """
        return self._doubao_total_tokens

    @doubao_total_tokens.setter
    def doubao_total_tokens(self, doubao_total_tokens):
        """Sets the doubao_total_tokens of this ConvertModelForGetExecutionOutput.


        :param doubao_total_tokens: The doubao_total_tokens of this ConvertModelForGetExecutionOutput.  # noqa: E501
        :type: int
        """

        self._doubao_total_tokens = doubao_total_tokens

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
        if issubclass(ConvertModelForGetExecutionOutput, dict):
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
        if not isinstance(other, ConvertModelForGetExecutionOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConvertModelForGetExecutionOutput):
            return True

        return self.to_dict() != other.to_dict()
