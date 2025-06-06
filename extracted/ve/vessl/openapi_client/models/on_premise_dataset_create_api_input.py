# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class OnPremiseDatasetCreateAPIInput(object):
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
        'description': 'str',
        'name': 'str',
        'on_premise_volume': 'OrmOnPremiseVolumeConfig'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'on_premise_volume': 'on_premise_volume'
    }

    def __init__(self, description=None, name=None, on_premise_volume=None, local_vars_configuration=None):  # noqa: E501
        """OnPremiseDatasetCreateAPIInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._name = None
        self._on_premise_volume = None
        self.discriminator = None

        self.description = description
        self.name = name
        self.on_premise_volume = on_premise_volume

    @property
    def description(self):
        """Gets the description of this OnPremiseDatasetCreateAPIInput.  # noqa: E501


        :return: The description of this OnPremiseDatasetCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OnPremiseDatasetCreateAPIInput.


        :param description: The description of this OnPremiseDatasetCreateAPIInput.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this OnPremiseDatasetCreateAPIInput.  # noqa: E501


        :return: The name of this OnPremiseDatasetCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OnPremiseDatasetCreateAPIInput.


        :param name: The name of this OnPremiseDatasetCreateAPIInput.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def on_premise_volume(self):
        """Gets the on_premise_volume of this OnPremiseDatasetCreateAPIInput.  # noqa: E501


        :return: The on_premise_volume of this OnPremiseDatasetCreateAPIInput.  # noqa: E501
        :rtype: OrmOnPremiseVolumeConfig
        """
        return self._on_premise_volume

    @on_premise_volume.setter
    def on_premise_volume(self, on_premise_volume):
        """Sets the on_premise_volume of this OnPremiseDatasetCreateAPIInput.


        :param on_premise_volume: The on_premise_volume of this OnPremiseDatasetCreateAPIInput.  # noqa: E501
        :type on_premise_volume: OrmOnPremiseVolumeConfig
        """
        if self.local_vars_configuration.client_side_validation and on_premise_volume is None:  # noqa: E501
            raise ValueError("Invalid value for `on_premise_volume`, must not be `None`")  # noqa: E501

        self._on_premise_volume = on_premise_volume

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
        if not isinstance(other, OnPremiseDatasetCreateAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OnPremiseDatasetCreateAPIInput):
            return True

        return self.to_dict() != other.to_dict()
