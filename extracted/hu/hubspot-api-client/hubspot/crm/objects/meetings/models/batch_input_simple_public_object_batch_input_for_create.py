# coding: utf-8

"""
    Meetings

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.crm.objects.meetings.configuration import Configuration


class BatchInputSimplePublicObjectBatchInputForCreate(object):
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
    openapi_types = {"inputs": "list[SimplePublicObjectBatchInputForCreate]"}

    attribute_map = {"inputs": "inputs"}

    def __init__(self, inputs=None, local_vars_configuration=None):  # noqa: E501
        """BatchInputSimplePublicObjectBatchInputForCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._inputs = None
        self.discriminator = None

        self.inputs = inputs

    @property
    def inputs(self):
        """Gets the inputs of this BatchInputSimplePublicObjectBatchInputForCreate.  # noqa: E501


        :return: The inputs of this BatchInputSimplePublicObjectBatchInputForCreate.  # noqa: E501
        :rtype: list[SimplePublicObjectBatchInputForCreate]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this BatchInputSimplePublicObjectBatchInputForCreate.


        :param inputs: The inputs of this BatchInputSimplePublicObjectBatchInputForCreate.  # noqa: E501
        :type inputs: list[SimplePublicObjectBatchInputForCreate]
        """
        if self.local_vars_configuration.client_side_validation and inputs is None:  # noqa: E501
            raise ValueError("Invalid value for `inputs`, must not be `None`")  # noqa: E501

        self._inputs = inputs

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
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
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
        if not isinstance(other, BatchInputSimplePublicObjectBatchInputForCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchInputSimplePublicObjectBatchInputForCreate):
            return True

        return self.to_dict() != other.to_dict()
