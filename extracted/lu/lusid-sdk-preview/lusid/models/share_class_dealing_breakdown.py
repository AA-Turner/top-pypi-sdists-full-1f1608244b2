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


class ShareClassDealingBreakdown(object):
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
        'class_dealing': 'dict(str, ShareClassAmount)',
        'class_dealing_units': 'dict(str, Amount)'
    }

    attribute_map = {
        'class_dealing': 'classDealing',
        'class_dealing_units': 'classDealingUnits'
    }

    required_map = {
        'class_dealing': 'required',
        'class_dealing_units': 'required'
    }

    def __init__(self, class_dealing=None, class_dealing_units=None, local_vars_configuration=None):  # noqa: E501
        """ShareClassDealingBreakdown - a model defined in OpenAPI"
        
        :param class_dealing:  Bucket of detail for any 'Dealing' specific to the share class that has occured inside the queried period. (required)
        :type class_dealing: dict[str, lusid.ShareClassAmount]
        :param class_dealing_units:  Bucket of detail for any 'Dealing' units specific to the share class that has occured inside the queried period. (required)
        :type class_dealing_units: dict[str, lusid.Amount]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._class_dealing = None
        self._class_dealing_units = None
        self.discriminator = None

        self.class_dealing = class_dealing
        self.class_dealing_units = class_dealing_units

    @property
    def class_dealing(self):
        """Gets the class_dealing of this ShareClassDealingBreakdown.  # noqa: E501

        Bucket of detail for any 'Dealing' specific to the share class that has occured inside the queried period.  # noqa: E501

        :return: The class_dealing of this ShareClassDealingBreakdown.  # noqa: E501
        :rtype: dict[str, lusid.ShareClassAmount]
        """
        return self._class_dealing

    @class_dealing.setter
    def class_dealing(self, class_dealing):
        """Sets the class_dealing of this ShareClassDealingBreakdown.

        Bucket of detail for any 'Dealing' specific to the share class that has occured inside the queried period.  # noqa: E501

        :param class_dealing: The class_dealing of this ShareClassDealingBreakdown.  # noqa: E501
        :type class_dealing: dict[str, lusid.ShareClassAmount]
        """
        if self.local_vars_configuration.client_side_validation and class_dealing is None:  # noqa: E501
            raise ValueError("Invalid value for `class_dealing`, must not be `None`")  # noqa: E501

        self._class_dealing = class_dealing

    @property
    def class_dealing_units(self):
        """Gets the class_dealing_units of this ShareClassDealingBreakdown.  # noqa: E501

        Bucket of detail for any 'Dealing' units specific to the share class that has occured inside the queried period.  # noqa: E501

        :return: The class_dealing_units of this ShareClassDealingBreakdown.  # noqa: E501
        :rtype: dict[str, lusid.Amount]
        """
        return self._class_dealing_units

    @class_dealing_units.setter
    def class_dealing_units(self, class_dealing_units):
        """Sets the class_dealing_units of this ShareClassDealingBreakdown.

        Bucket of detail for any 'Dealing' units specific to the share class that has occured inside the queried period.  # noqa: E501

        :param class_dealing_units: The class_dealing_units of this ShareClassDealingBreakdown.  # noqa: E501
        :type class_dealing_units: dict[str, lusid.Amount]
        """
        if self.local_vars_configuration.client_side_validation and class_dealing_units is None:  # noqa: E501
            raise ValueError("Invalid value for `class_dealing_units`, must not be `None`")  # noqa: E501

        self._class_dealing_units = class_dealing_units

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
        if not isinstance(other, ShareClassDealingBreakdown):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShareClassDealingBreakdown):
            return True

        return self.to_dict() != other.to_dict()
