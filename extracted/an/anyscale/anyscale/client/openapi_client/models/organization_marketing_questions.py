# coding: utf-8

"""
    Managed Ray API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class OrganizationMarketingQuestions(object):
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
        'workload': 'str',
        'modalities': 'str',
        'model_types': 'str',
        'ray_maturity': 'str'
    }

    attribute_map = {
        'workload': 'workload',
        'modalities': 'modalities',
        'model_types': 'model_types',
        'ray_maturity': 'ray_maturity'
    }

    def __init__(self, workload=None, modalities=None, model_types=None, ray_maturity=None, local_vars_configuration=None):  # noqa: E501
        """OrganizationMarketingQuestions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._workload = None
        self._modalities = None
        self._model_types = None
        self._ray_maturity = None
        self.discriminator = None

        if workload is not None:
            self.workload = workload
        if modalities is not None:
            self.modalities = modalities
        if model_types is not None:
            self.model_types = model_types
        if ray_maturity is not None:
            self.ray_maturity = ray_maturity

    @property
    def workload(self):
        """Gets the workload of this OrganizationMarketingQuestions.  # noqa: E501


        :return: The workload of this OrganizationMarketingQuestions.  # noqa: E501
        :rtype: str
        """
        return self._workload

    @workload.setter
    def workload(self, workload):
        """Sets the workload of this OrganizationMarketingQuestions.


        :param workload: The workload of this OrganizationMarketingQuestions.  # noqa: E501
        :type: str
        """

        self._workload = workload

    @property
    def modalities(self):
        """Gets the modalities of this OrganizationMarketingQuestions.  # noqa: E501


        :return: The modalities of this OrganizationMarketingQuestions.  # noqa: E501
        :rtype: str
        """
        return self._modalities

    @modalities.setter
    def modalities(self, modalities):
        """Sets the modalities of this OrganizationMarketingQuestions.


        :param modalities: The modalities of this OrganizationMarketingQuestions.  # noqa: E501
        :type: str
        """

        self._modalities = modalities

    @property
    def model_types(self):
        """Gets the model_types of this OrganizationMarketingQuestions.  # noqa: E501


        :return: The model_types of this OrganizationMarketingQuestions.  # noqa: E501
        :rtype: str
        """
        return self._model_types

    @model_types.setter
    def model_types(self, model_types):
        """Sets the model_types of this OrganizationMarketingQuestions.


        :param model_types: The model_types of this OrganizationMarketingQuestions.  # noqa: E501
        :type: str
        """

        self._model_types = model_types

    @property
    def ray_maturity(self):
        """Gets the ray_maturity of this OrganizationMarketingQuestions.  # noqa: E501


        :return: The ray_maturity of this OrganizationMarketingQuestions.  # noqa: E501
        :rtype: str
        """
        return self._ray_maturity

    @ray_maturity.setter
    def ray_maturity(self, ray_maturity):
        """Sets the ray_maturity of this OrganizationMarketingQuestions.


        :param ray_maturity: The ray_maturity of this OrganizationMarketingQuestions.  # noqa: E501
        :type: str
        """

        self._ray_maturity = ray_maturity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrganizationMarketingQuestions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationMarketingQuestions):
            return True

        return self.to_dict() != other.to_dict()
