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


class SystemVendor(object):
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
        'serial_number': 'str',
        'product_name': 'str',
        'manufacturer': 'str',
        'virtual': 'bool'
    }

    attribute_map = {
        'serial_number': 'serial_number',
        'product_name': 'product_name',
        'manufacturer': 'manufacturer',
        'virtual': 'virtual'
    }

    def __init__(self, serial_number=None, product_name=None, manufacturer=None, virtual=None):  # noqa: E501
        """SystemVendor - a model defined in Swagger"""  # noqa: E501

        self._serial_number = None
        self._product_name = None
        self._manufacturer = None
        self._virtual = None
        self.discriminator = None

        if serial_number is not None:
            self.serial_number = serial_number
        if product_name is not None:
            self.product_name = product_name
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if virtual is not None:
            self.virtual = virtual

    @property
    def serial_number(self):
        """Gets the serial_number of this SystemVendor.  # noqa: E501


        :return: The serial_number of this SystemVendor.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this SystemVendor.


        :param serial_number: The serial_number of this SystemVendor.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def product_name(self):
        """Gets the product_name of this SystemVendor.  # noqa: E501


        :return: The product_name of this SystemVendor.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this SystemVendor.


        :param product_name: The product_name of this SystemVendor.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def manufacturer(self):
        """Gets the manufacturer of this SystemVendor.  # noqa: E501


        :return: The manufacturer of this SystemVendor.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this SystemVendor.


        :param manufacturer: The manufacturer of this SystemVendor.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def virtual(self):
        """Gets the virtual of this SystemVendor.  # noqa: E501

        Whether the machine appears to be a virtual machine or not  # noqa: E501

        :return: The virtual of this SystemVendor.  # noqa: E501
        :rtype: bool
        """
        return self._virtual

    @virtual.setter
    def virtual(self, virtual):
        """Sets the virtual of this SystemVendor.

        Whether the machine appears to be a virtual machine or not  # noqa: E501

        :param virtual: The virtual of this SystemVendor.  # noqa: E501
        :type: bool
        """

        self._virtual = virtual

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
        if issubclass(SystemVendor, dict):
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
        if not isinstance(other, SystemVendor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
