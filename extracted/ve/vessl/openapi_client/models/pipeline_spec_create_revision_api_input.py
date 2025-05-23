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


class PipelineSpecCreateRevisionAPIInput(object):
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
        'from_yaml': 'bool',
        'message': 'str',
        'yaml': 'str'
    }

    attribute_map = {
        'from_yaml': 'from_yaml',
        'message': 'message',
        'yaml': 'yaml'
    }

    def __init__(self, from_yaml=None, message=None, yaml=None, local_vars_configuration=None):  # noqa: E501
        """PipelineSpecCreateRevisionAPIInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._from_yaml = None
        self._message = None
        self._yaml = None
        self.discriminator = None

        if from_yaml is not None:
            self.from_yaml = from_yaml
        if message is not None:
            self.message = message
        if yaml is not None:
            self.yaml = yaml

    @property
    def from_yaml(self):
        """Gets the from_yaml of this PipelineSpecCreateRevisionAPIInput.  # noqa: E501


        :return: The from_yaml of this PipelineSpecCreateRevisionAPIInput.  # noqa: E501
        :rtype: bool
        """
        return self._from_yaml

    @from_yaml.setter
    def from_yaml(self, from_yaml):
        """Sets the from_yaml of this PipelineSpecCreateRevisionAPIInput.


        :param from_yaml: The from_yaml of this PipelineSpecCreateRevisionAPIInput.  # noqa: E501
        :type from_yaml: bool
        """

        self._from_yaml = from_yaml

    @property
    def message(self):
        """Gets the message of this PipelineSpecCreateRevisionAPIInput.  # noqa: E501


        :return: The message of this PipelineSpecCreateRevisionAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PipelineSpecCreateRevisionAPIInput.


        :param message: The message of this PipelineSpecCreateRevisionAPIInput.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def yaml(self):
        """Gets the yaml of this PipelineSpecCreateRevisionAPIInput.  # noqa: E501


        :return: The yaml of this PipelineSpecCreateRevisionAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._yaml

    @yaml.setter
    def yaml(self, yaml):
        """Sets the yaml of this PipelineSpecCreateRevisionAPIInput.


        :param yaml: The yaml of this PipelineSpecCreateRevisionAPIInput.  # noqa: E501
        :type yaml: str
        """

        self._yaml = yaml

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
        if not isinstance(other, PipelineSpecCreateRevisionAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineSpecCreateRevisionAPIInput):
            return True

        return self.to_dict() != other.to_dict()
