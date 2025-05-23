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


class FeeTransactionTemplateSpecification(object):
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
        'specification_type_name': 'str',
        'supported_template_fields': 'list[TemplateField]'
    }

    attribute_map = {
        'specification_type_name': 'specificationTypeName',
        'supported_template_fields': 'supportedTemplateFields'
    }

    required_map = {
        'specification_type_name': 'required',
        'supported_template_fields': 'required'
    }

    def __init__(self, specification_type_name=None, supported_template_fields=None, local_vars_configuration=None):  # noqa: E501
        """FeeTransactionTemplateSpecification - a model defined in OpenAPI"
        
        :param specification_type_name:  (required)
        :type specification_type_name: str
        :param supported_template_fields:  (required)
        :type supported_template_fields: list[lusid.TemplateField]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._specification_type_name = None
        self._supported_template_fields = None
        self.discriminator = None

        self.specification_type_name = specification_type_name
        self.supported_template_fields = supported_template_fields

    @property
    def specification_type_name(self):
        """Gets the specification_type_name of this FeeTransactionTemplateSpecification.  # noqa: E501


        :return: The specification_type_name of this FeeTransactionTemplateSpecification.  # noqa: E501
        :rtype: str
        """
        return self._specification_type_name

    @specification_type_name.setter
    def specification_type_name(self, specification_type_name):
        """Sets the specification_type_name of this FeeTransactionTemplateSpecification.


        :param specification_type_name: The specification_type_name of this FeeTransactionTemplateSpecification.  # noqa: E501
        :type specification_type_name: str
        """
        if self.local_vars_configuration.client_side_validation and specification_type_name is None:  # noqa: E501
            raise ValueError("Invalid value for `specification_type_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                specification_type_name is not None and len(specification_type_name) < 1):
            raise ValueError("Invalid value for `specification_type_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._specification_type_name = specification_type_name

    @property
    def supported_template_fields(self):
        """Gets the supported_template_fields of this FeeTransactionTemplateSpecification.  # noqa: E501


        :return: The supported_template_fields of this FeeTransactionTemplateSpecification.  # noqa: E501
        :rtype: list[lusid.TemplateField]
        """
        return self._supported_template_fields

    @supported_template_fields.setter
    def supported_template_fields(self, supported_template_fields):
        """Sets the supported_template_fields of this FeeTransactionTemplateSpecification.


        :param supported_template_fields: The supported_template_fields of this FeeTransactionTemplateSpecification.  # noqa: E501
        :type supported_template_fields: list[lusid.TemplateField]
        """
        if self.local_vars_configuration.client_side_validation and supported_template_fields is None:  # noqa: E501
            raise ValueError("Invalid value for `supported_template_fields`, must not be `None`")  # noqa: E501

        self._supported_template_fields = supported_template_fields

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
        if not isinstance(other, FeeTransactionTemplateSpecification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeeTransactionTemplateSpecification):
            return True

        return self.to_dict() != other.to_dict()
