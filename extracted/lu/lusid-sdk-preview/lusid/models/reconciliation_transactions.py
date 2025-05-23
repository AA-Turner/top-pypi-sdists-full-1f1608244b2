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


class ReconciliationTransactions(object):
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
        'transaction_window': 'DateRange',
        'mapping_id': 'ResourceId'
    }

    attribute_map = {
        'transaction_window': 'transactionWindow',
        'mapping_id': 'mappingId'
    }

    required_map = {
        'transaction_window': 'optional',
        'mapping_id': 'optional'
    }

    def __init__(self, transaction_window=None, mapping_id=None, local_vars_configuration=None):  # noqa: E501
        """ReconciliationTransactions - a model defined in OpenAPI"
        
        :param transaction_window: 
        :type transaction_window: lusid.DateRange
        :param mapping_id: 
        :type mapping_id: lusid.ResourceId

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._transaction_window = None
        self._mapping_id = None
        self.discriminator = None

        if transaction_window is not None:
            self.transaction_window = transaction_window
        if mapping_id is not None:
            self.mapping_id = mapping_id

    @property
    def transaction_window(self):
        """Gets the transaction_window of this ReconciliationTransactions.  # noqa: E501


        :return: The transaction_window of this ReconciliationTransactions.  # noqa: E501
        :rtype: lusid.DateRange
        """
        return self._transaction_window

    @transaction_window.setter
    def transaction_window(self, transaction_window):
        """Sets the transaction_window of this ReconciliationTransactions.


        :param transaction_window: The transaction_window of this ReconciliationTransactions.  # noqa: E501
        :type transaction_window: lusid.DateRange
        """

        self._transaction_window = transaction_window

    @property
    def mapping_id(self):
        """Gets the mapping_id of this ReconciliationTransactions.  # noqa: E501


        :return: The mapping_id of this ReconciliationTransactions.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        """Sets the mapping_id of this ReconciliationTransactions.


        :param mapping_id: The mapping_id of this ReconciliationTransactions.  # noqa: E501
        :type mapping_id: lusid.ResourceId
        """

        self._mapping_id = mapping_id

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
        if not isinstance(other, ReconciliationTransactions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReconciliationTransactions):
            return True

        return self.to_dict() != other.to_dict()
