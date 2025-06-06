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


class UpdateReferenceDataRequest(object):
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
        'request_definitions': 'list[FieldDefinition]',
        'request_values': 'list[FieldValue]'
    }

    attribute_map = {
        'request_definitions': 'requestDefinitions',
        'request_values': 'requestValues'
    }

    required_map = {
        'request_definitions': 'required',
        'request_values': 'required'
    }

    def __init__(self, request_definitions=None, request_values=None, local_vars_configuration=None):  # noqa: E501
        """UpdateReferenceDataRequest - a model defined in OpenAPI"
        
        :param request_definitions:  Definition of a reference data field. (required)
        :type request_definitions: list[lusid.FieldDefinition]
        :param request_values:  Reference data. (required)
        :type request_values: list[lusid.FieldValue]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._request_definitions = None
        self._request_values = None
        self.discriminator = None

        self.request_definitions = request_definitions
        self.request_values = request_values

    @property
    def request_definitions(self):
        """Gets the request_definitions of this UpdateReferenceDataRequest.  # noqa: E501

        Definition of a reference data field.  # noqa: E501

        :return: The request_definitions of this UpdateReferenceDataRequest.  # noqa: E501
        :rtype: list[lusid.FieldDefinition]
        """
        return self._request_definitions

    @request_definitions.setter
    def request_definitions(self, request_definitions):
        """Sets the request_definitions of this UpdateReferenceDataRequest.

        Definition of a reference data field.  # noqa: E501

        :param request_definitions: The request_definitions of this UpdateReferenceDataRequest.  # noqa: E501
        :type request_definitions: list[lusid.FieldDefinition]
        """
        if self.local_vars_configuration.client_side_validation and request_definitions is None:  # noqa: E501
            raise ValueError("Invalid value for `request_definitions`, must not be `None`")  # noqa: E501

        self._request_definitions = request_definitions

    @property
    def request_values(self):
        """Gets the request_values of this UpdateReferenceDataRequest.  # noqa: E501

        Reference data.  # noqa: E501

        :return: The request_values of this UpdateReferenceDataRequest.  # noqa: E501
        :rtype: list[lusid.FieldValue]
        """
        return self._request_values

    @request_values.setter
    def request_values(self, request_values):
        """Sets the request_values of this UpdateReferenceDataRequest.

        Reference data.  # noqa: E501

        :param request_values: The request_values of this UpdateReferenceDataRequest.  # noqa: E501
        :type request_values: list[lusid.FieldValue]
        """
        if self.local_vars_configuration.client_side_validation and request_values is None:  # noqa: E501
            raise ValueError("Invalid value for `request_values`, must not be `None`")  # noqa: E501

        self._request_values = request_values

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
        if not isinstance(other, UpdateReferenceDataRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateReferenceDataRequest):
            return True

        return self.to_dict() != other.to_dict()
