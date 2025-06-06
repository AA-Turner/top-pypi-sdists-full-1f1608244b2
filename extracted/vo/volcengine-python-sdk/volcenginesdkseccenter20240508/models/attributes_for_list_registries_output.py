# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AttributesForListRegistriesOutput(object):
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
        'volc_region': 'str',
        'volc_status': 'str',
        'volc_type': 'str'
    }

    attribute_map = {
        'volc_region': 'VolcRegion',
        'volc_status': 'VolcStatus',
        'volc_type': 'VolcType'
    }

    def __init__(self, volc_region=None, volc_status=None, volc_type=None, _configuration=None):  # noqa: E501
        """AttributesForListRegistriesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._volc_region = None
        self._volc_status = None
        self._volc_type = None
        self.discriminator = None

        if volc_region is not None:
            self.volc_region = volc_region
        if volc_status is not None:
            self.volc_status = volc_status
        if volc_type is not None:
            self.volc_type = volc_type

    @property
    def volc_region(self):
        """Gets the volc_region of this AttributesForListRegistriesOutput.  # noqa: E501


        :return: The volc_region of this AttributesForListRegistriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._volc_region

    @volc_region.setter
    def volc_region(self, volc_region):
        """Sets the volc_region of this AttributesForListRegistriesOutput.


        :param volc_region: The volc_region of this AttributesForListRegistriesOutput.  # noqa: E501
        :type: str
        """

        self._volc_region = volc_region

    @property
    def volc_status(self):
        """Gets the volc_status of this AttributesForListRegistriesOutput.  # noqa: E501


        :return: The volc_status of this AttributesForListRegistriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._volc_status

    @volc_status.setter
    def volc_status(self, volc_status):
        """Sets the volc_status of this AttributesForListRegistriesOutput.


        :param volc_status: The volc_status of this AttributesForListRegistriesOutput.  # noqa: E501
        :type: str
        """

        self._volc_status = volc_status

    @property
    def volc_type(self):
        """Gets the volc_type of this AttributesForListRegistriesOutput.  # noqa: E501


        :return: The volc_type of this AttributesForListRegistriesOutput.  # noqa: E501
        :rtype: str
        """
        return self._volc_type

    @volc_type.setter
    def volc_type(self, volc_type):
        """Sets the volc_type of this AttributesForListRegistriesOutput.


        :param volc_type: The volc_type of this AttributesForListRegistriesOutput.  # noqa: E501
        :type: str
        """

        self._volc_type = volc_type

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
        if issubclass(AttributesForListRegistriesOutput, dict):
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
        if not isinstance(other, AttributesForListRegistriesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttributesForListRegistriesOutput):
            return True

        return self.to_dict() != other.to_dict()
