# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.257
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class ComparisonAttributeValuePair(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'attribute_name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'attribute_name': 'attributeName',
        'value': 'value'
    }

    required_map = {
        'attribute_name': 'required',
        'value': 'required'
    }

    def __init__(self, attribute_name=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ComparisonAttributeValuePair - a model defined in OpenAPI"
        
        :param attribute_name:  Comparison rule attribute name. (required)
        :type attribute_name: str
        :param value:  Computed value for the comparison rule attribute. (required)
        :type value: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._attribute_name = None
        self._value = None
        self.discriminator = None

        self.attribute_name = attribute_name
        self.value = value

    @property
    def attribute_name(self):
        """Gets the attribute_name of this ComparisonAttributeValuePair.  # noqa: E501

        Comparison rule attribute name.  # noqa: E501

        :return: The attribute_name of this ComparisonAttributeValuePair.  # noqa: E501
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """Sets the attribute_name of this ComparisonAttributeValuePair.

        Comparison rule attribute name.  # noqa: E501

        :param attribute_name: The attribute_name of this ComparisonAttributeValuePair.  # noqa: E501
        :type attribute_name: str
        """
        if self.local_vars_configuration.client_side_validation and attribute_name is None:  # noqa: E501
            raise ValueError("Invalid value for `attribute_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                attribute_name is not None and len(attribute_name) < 1):
            raise ValueError("Invalid value for `attribute_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._attribute_name = attribute_name

    @property
    def value(self):
        """Gets the value of this ComparisonAttributeValuePair.  # noqa: E501

        Computed value for the comparison rule attribute.  # noqa: E501

        :return: The value of this ComparisonAttributeValuePair.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ComparisonAttributeValuePair.

        Computed value for the comparison rule attribute.  # noqa: E501

        :param value: The value of this ComparisonAttributeValuePair.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) < 1):
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, ComparisonAttributeValuePair):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComparisonAttributeValuePair):
            return True

        return self.to_dict() != other.to_dict()
