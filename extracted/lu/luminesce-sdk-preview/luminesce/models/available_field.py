# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.16.765
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

from luminesce.configuration import Configuration


class AvailableField(object):
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
        'name': 'str',
        'data_type': 'DataType',
        'field_type': 'FieldType',
        'is_main': 'bool',
        'is_primary_key': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'data_type': 'dataType',
        'field_type': 'fieldType',
        'is_main': 'isMain',
        'is_primary_key': 'isPrimaryKey'
    }

    required_map = {
        'name': 'required',
        'data_type': 'optional',
        'field_type': 'required',
        'is_main': 'optional',
        'is_primary_key': 'optional'
    }

    def __init__(self, name=None, data_type=None, field_type=None, is_main=None, is_primary_key=None, local_vars_configuration=None):  # noqa: E501
        """AvailableField - a model defined in OpenAPI"
        
        :param name:  Name of the Field (required)
        :type name: str
        :param data_type: 
        :type data_type: luminesce.DataType
        :param field_type:  (required)
        :type field_type: luminesce.FieldType
        :param is_main:  Is this a Main Field within the Provider
        :type is_main: bool
        :param is_primary_key:  Is this a member of the PrimaryKey of the Provider
        :type is_primary_key: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._data_type = None
        self._field_type = None
        self._is_main = None
        self._is_primary_key = None
        self.discriminator = None

        self.name = name
        if data_type is not None:
            self.data_type = data_type
        self.field_type = field_type
        self.is_main = is_main
        self.is_primary_key = is_primary_key

    @property
    def name(self):
        """Gets the name of this AvailableField.  # noqa: E501

        Name of the Field  # noqa: E501

        :return: The name of this AvailableField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AvailableField.

        Name of the Field  # noqa: E501

        :param name: The name of this AvailableField.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 256):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def data_type(self):
        """Gets the data_type of this AvailableField.  # noqa: E501


        :return: The data_type of this AvailableField.  # noqa: E501
        :rtype: luminesce.DataType
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this AvailableField.


        :param data_type: The data_type of this AvailableField.  # noqa: E501
        :type data_type: luminesce.DataType
        """

        self._data_type = data_type

    @property
    def field_type(self):
        """Gets the field_type of this AvailableField.  # noqa: E501


        :return: The field_type of this AvailableField.  # noqa: E501
        :rtype: luminesce.FieldType
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this AvailableField.


        :param field_type: The field_type of this AvailableField.  # noqa: E501
        :type field_type: luminesce.FieldType
        """
        if self.local_vars_configuration.client_side_validation and field_type is None:  # noqa: E501
            raise ValueError("Invalid value for `field_type`, must not be `None`")  # noqa: E501

        self._field_type = field_type

    @property
    def is_main(self):
        """Gets the is_main of this AvailableField.  # noqa: E501

        Is this a Main Field within the Provider  # noqa: E501

        :return: The is_main of this AvailableField.  # noqa: E501
        :rtype: bool
        """
        return self._is_main

    @is_main.setter
    def is_main(self, is_main):
        """Sets the is_main of this AvailableField.

        Is this a Main Field within the Provider  # noqa: E501

        :param is_main: The is_main of this AvailableField.  # noqa: E501
        :type is_main: bool
        """

        self._is_main = is_main

    @property
    def is_primary_key(self):
        """Gets the is_primary_key of this AvailableField.  # noqa: E501

        Is this a member of the PrimaryKey of the Provider  # noqa: E501

        :return: The is_primary_key of this AvailableField.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary_key

    @is_primary_key.setter
    def is_primary_key(self, is_primary_key):
        """Sets the is_primary_key of this AvailableField.

        Is this a member of the PrimaryKey of the Provider  # noqa: E501

        :param is_primary_key: The is_primary_key of this AvailableField.  # noqa: E501
        :type is_primary_key: bool
        """

        self._is_primary_key = is_primary_key

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
        if not isinstance(other, AvailableField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AvailableField):
            return True

        return self.to_dict() != other.to_dict()
