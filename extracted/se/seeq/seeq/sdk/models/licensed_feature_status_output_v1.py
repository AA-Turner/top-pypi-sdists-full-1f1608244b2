# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 66.22.1-v202505231115-CD
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class LicensedFeatureStatusOutputV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'days_to_expiration': 'int',
        'name': 'str',
        'valid_through': 'str',
        'validity': 'str'
    }

    attribute_map = {
        'days_to_expiration': 'daysToExpiration',
        'name': 'name',
        'valid_through': 'validThrough',
        'validity': 'validity'
    }

    def __init__(self, days_to_expiration=None, name=None, valid_through=None, validity=None):
        """
        LicensedFeatureStatusOutputV1 - a model defined in Swagger
        """

        self._days_to_expiration = None
        self._name = None
        self._valid_through = None
        self._validity = None

        if days_to_expiration is not None:
          self.days_to_expiration = days_to_expiration
        if name is not None:
          self.name = name
        if valid_through is not None:
          self.valid_through = valid_through
        if validity is not None:
          self.validity = validity

    @property
    def days_to_expiration(self):
        """
        Gets the days_to_expiration of this LicensedFeatureStatusOutputV1.
        The number of days left before the current licensed feature will expire

        :return: The days_to_expiration of this LicensedFeatureStatusOutputV1.
        :rtype: int
        """
        return self._days_to_expiration

    @days_to_expiration.setter
    def days_to_expiration(self, days_to_expiration):
        """
        Sets the days_to_expiration of this LicensedFeatureStatusOutputV1.
        The number of days left before the current licensed feature will expire

        :param days_to_expiration: The days_to_expiration of this LicensedFeatureStatusOutputV1.
        :type: int
        """

        self._days_to_expiration = days_to_expiration

    @property
    def name(self):
        """
        Gets the name of this LicensedFeatureStatusOutputV1.
        The licensed feature name

        :return: The name of this LicensedFeatureStatusOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LicensedFeatureStatusOutputV1.
        The licensed feature name

        :param name: The name of this LicensedFeatureStatusOutputV1.
        :type: str
        """

        self._name = name

    @property
    def valid_through(self):
        """
        Gets the valid_through of this LicensedFeatureStatusOutputV1.
        The final day this licensed feature will be valid for

        :return: The valid_through of this LicensedFeatureStatusOutputV1.
        :rtype: str
        """
        return self._valid_through

    @valid_through.setter
    def valid_through(self, valid_through):
        """
        Sets the valid_through of this LicensedFeatureStatusOutputV1.
        The final day this licensed feature will be valid for

        :param valid_through: The valid_through of this LicensedFeatureStatusOutputV1.
        :type: str
        """

        self._valid_through = valid_through

    @property
    def validity(self):
        """
        Gets the validity of this LicensedFeatureStatusOutputV1.
        Validity status

        :return: The validity of this LicensedFeatureStatusOutputV1.
        :rtype: str
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """
        Sets the validity of this LicensedFeatureStatusOutputV1.
        Validity status

        :param validity: The validity of this LicensedFeatureStatusOutputV1.
        :type: str
        """
        allowed_values = ["UnknownError", "Valid", "NoLicense", "Expired", "WrongHost", "BadSignature", "ClockTampering", "OverLimit"]
        if validity not in allowed_values:
            raise ValueError(
                "Invalid value for `validity` ({0}), must be one of {1}"
                .format(validity, allowed_values)
            )

        self._validity = validity

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, LicensedFeatureStatusOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
