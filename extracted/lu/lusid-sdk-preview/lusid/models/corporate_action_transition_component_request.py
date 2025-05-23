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


class CorporateActionTransitionComponentRequest(object):
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
        'instrument_identifiers': 'dict(str, str)',
        'units_factor': 'float',
        'cost_factor': 'float'
    }

    attribute_map = {
        'instrument_identifiers': 'instrumentIdentifiers',
        'units_factor': 'unitsFactor',
        'cost_factor': 'costFactor'
    }

    required_map = {
        'instrument_identifiers': 'required',
        'units_factor': 'required',
        'cost_factor': 'required'
    }

    def __init__(self, instrument_identifiers=None, units_factor=None, cost_factor=None, local_vars_configuration=None):  # noqa: E501
        """CorporateActionTransitionComponentRequest - a model defined in OpenAPI"
        
        :param instrument_identifiers:  Unique instrument identifiers (required)
        :type instrument_identifiers: dict(str, str)
        :param units_factor:  The factor to scale units by (required)
        :type units_factor: float
        :param cost_factor:  The factor to scale cost by (required)
        :type cost_factor: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instrument_identifiers = None
        self._units_factor = None
        self._cost_factor = None
        self.discriminator = None

        self.instrument_identifiers = instrument_identifiers
        self.units_factor = units_factor
        self.cost_factor = cost_factor

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this CorporateActionTransitionComponentRequest.  # noqa: E501

        Unique instrument identifiers  # noqa: E501

        :return: The instrument_identifiers of this CorporateActionTransitionComponentRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this CorporateActionTransitionComponentRequest.

        Unique instrument identifiers  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this CorporateActionTransitionComponentRequest.  # noqa: E501
        :type instrument_identifiers: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and instrument_identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def units_factor(self):
        """Gets the units_factor of this CorporateActionTransitionComponentRequest.  # noqa: E501

        The factor to scale units by  # noqa: E501

        :return: The units_factor of this CorporateActionTransitionComponentRequest.  # noqa: E501
        :rtype: float
        """
        return self._units_factor

    @units_factor.setter
    def units_factor(self, units_factor):
        """Sets the units_factor of this CorporateActionTransitionComponentRequest.

        The factor to scale units by  # noqa: E501

        :param units_factor: The units_factor of this CorporateActionTransitionComponentRequest.  # noqa: E501
        :type units_factor: float
        """
        if self.local_vars_configuration.client_side_validation and units_factor is None:  # noqa: E501
            raise ValueError("Invalid value for `units_factor`, must not be `None`")  # noqa: E501

        self._units_factor = units_factor

    @property
    def cost_factor(self):
        """Gets the cost_factor of this CorporateActionTransitionComponentRequest.  # noqa: E501

        The factor to scale cost by  # noqa: E501

        :return: The cost_factor of this CorporateActionTransitionComponentRequest.  # noqa: E501
        :rtype: float
        """
        return self._cost_factor

    @cost_factor.setter
    def cost_factor(self, cost_factor):
        """Sets the cost_factor of this CorporateActionTransitionComponentRequest.

        The factor to scale cost by  # noqa: E501

        :param cost_factor: The cost_factor of this CorporateActionTransitionComponentRequest.  # noqa: E501
        :type cost_factor: float
        """
        if self.local_vars_configuration.client_side_validation and cost_factor is None:  # noqa: E501
            raise ValueError("Invalid value for `cost_factor`, must not be `None`")  # noqa: E501

        self._cost_factor = cost_factor

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
        if not isinstance(other, CorporateActionTransitionComponentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CorporateActionTransitionComponentRequest):
            return True

        return self.to_dict() != other.to_dict()
