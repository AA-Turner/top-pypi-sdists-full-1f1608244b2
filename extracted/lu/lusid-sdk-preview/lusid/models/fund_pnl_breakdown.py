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


class FundPnlBreakdown(object):
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
        'non_class_specific_pnl': 'dict(str, FundAmount)',
        'aggregated_class_pnl': 'dict(str, FundAmount)',
        'total_pnl': 'dict(str, FundAmount)'
    }

    attribute_map = {
        'non_class_specific_pnl': 'nonClassSpecificPnl',
        'aggregated_class_pnl': 'aggregatedClassPnl',
        'total_pnl': 'totalPnl'
    }

    required_map = {
        'non_class_specific_pnl': 'required',
        'aggregated_class_pnl': 'required',
        'total_pnl': 'required'
    }

    def __init__(self, non_class_specific_pnl=None, aggregated_class_pnl=None, total_pnl=None, local_vars_configuration=None):  # noqa: E501
        """FundPnlBreakdown - a model defined in OpenAPI"
        
        :param non_class_specific_pnl:  Bucket of detail for PnL within the queried period that is not specific to any share class. (required)
        :type non_class_specific_pnl: dict[str, lusid.FundAmount]
        :param aggregated_class_pnl:  Bucket of detail for the sum of class PnL across all share classes in a fund and within the queried period. (required)
        :type aggregated_class_pnl: dict[str, lusid.FundAmount]
        :param total_pnl:  Bucket of detail for the sum of class PnL and PnL not specific to a class within the queried period. (required)
        :type total_pnl: dict[str, lusid.FundAmount]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._non_class_specific_pnl = None
        self._aggregated_class_pnl = None
        self._total_pnl = None
        self.discriminator = None

        self.non_class_specific_pnl = non_class_specific_pnl
        self.aggregated_class_pnl = aggregated_class_pnl
        self.total_pnl = total_pnl

    @property
    def non_class_specific_pnl(self):
        """Gets the non_class_specific_pnl of this FundPnlBreakdown.  # noqa: E501

        Bucket of detail for PnL within the queried period that is not specific to any share class.  # noqa: E501

        :return: The non_class_specific_pnl of this FundPnlBreakdown.  # noqa: E501
        :rtype: dict[str, lusid.FundAmount]
        """
        return self._non_class_specific_pnl

    @non_class_specific_pnl.setter
    def non_class_specific_pnl(self, non_class_specific_pnl):
        """Sets the non_class_specific_pnl of this FundPnlBreakdown.

        Bucket of detail for PnL within the queried period that is not specific to any share class.  # noqa: E501

        :param non_class_specific_pnl: The non_class_specific_pnl of this FundPnlBreakdown.  # noqa: E501
        :type non_class_specific_pnl: dict[str, lusid.FundAmount]
        """
        if self.local_vars_configuration.client_side_validation and non_class_specific_pnl is None:  # noqa: E501
            raise ValueError("Invalid value for `non_class_specific_pnl`, must not be `None`")  # noqa: E501

        self._non_class_specific_pnl = non_class_specific_pnl

    @property
    def aggregated_class_pnl(self):
        """Gets the aggregated_class_pnl of this FundPnlBreakdown.  # noqa: E501

        Bucket of detail for the sum of class PnL across all share classes in a fund and within the queried period.  # noqa: E501

        :return: The aggregated_class_pnl of this FundPnlBreakdown.  # noqa: E501
        :rtype: dict[str, lusid.FundAmount]
        """
        return self._aggregated_class_pnl

    @aggregated_class_pnl.setter
    def aggregated_class_pnl(self, aggregated_class_pnl):
        """Sets the aggregated_class_pnl of this FundPnlBreakdown.

        Bucket of detail for the sum of class PnL across all share classes in a fund and within the queried period.  # noqa: E501

        :param aggregated_class_pnl: The aggregated_class_pnl of this FundPnlBreakdown.  # noqa: E501
        :type aggregated_class_pnl: dict[str, lusid.FundAmount]
        """
        if self.local_vars_configuration.client_side_validation and aggregated_class_pnl is None:  # noqa: E501
            raise ValueError("Invalid value for `aggregated_class_pnl`, must not be `None`")  # noqa: E501

        self._aggregated_class_pnl = aggregated_class_pnl

    @property
    def total_pnl(self):
        """Gets the total_pnl of this FundPnlBreakdown.  # noqa: E501

        Bucket of detail for the sum of class PnL and PnL not specific to a class within the queried period.  # noqa: E501

        :return: The total_pnl of this FundPnlBreakdown.  # noqa: E501
        :rtype: dict[str, lusid.FundAmount]
        """
        return self._total_pnl

    @total_pnl.setter
    def total_pnl(self, total_pnl):
        """Sets the total_pnl of this FundPnlBreakdown.

        Bucket of detail for the sum of class PnL and PnL not specific to a class within the queried period.  # noqa: E501

        :param total_pnl: The total_pnl of this FundPnlBreakdown.  # noqa: E501
        :type total_pnl: dict[str, lusid.FundAmount]
        """
        if self.local_vars_configuration.client_side_validation and total_pnl is None:  # noqa: E501
            raise ValueError("Invalid value for `total_pnl`, must not be `None`")  # noqa: E501

        self._total_pnl = total_pnl

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
        if not isinstance(other, FundPnlBreakdown):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FundPnlBreakdown):
            return True

        return self.to_dict() != other.to_dict()
