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


class SetPersonPropertiesRequest(object):
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
        'properties': 'dict(str, ModelProperty)'
    }

    attribute_map = {
        'properties': 'properties'
    }

    required_map = {
        'properties': 'required'
    }

    def __init__(self, properties=None, local_vars_configuration=None):  # noqa: E501
        """SetPersonPropertiesRequest - a model defined in OpenAPI"
        
        :param properties:  Properties to set for a Person. All time-variant properties must have same EffectiveFrom date. Properties not included in the request will not be amended. (required)
        :type properties: dict[str, lusid.ModelProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._properties = None
        self.discriminator = None

        self.properties = properties

    @property
    def properties(self):
        """Gets the properties of this SetPersonPropertiesRequest.  # noqa: E501

        Properties to set for a Person. All time-variant properties must have same EffectiveFrom date. Properties not included in the request will not be amended.  # noqa: E501

        :return: The properties of this SetPersonPropertiesRequest.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SetPersonPropertiesRequest.

        Properties to set for a Person. All time-variant properties must have same EffectiveFrom date. Properties not included in the request will not be amended.  # noqa: E501

        :param properties: The properties of this SetPersonPropertiesRequest.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

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
        if not isinstance(other, SetPersonPropertiesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetPersonPropertiesRequest):
            return True

        return self.to_dict() != other.to_dict()
