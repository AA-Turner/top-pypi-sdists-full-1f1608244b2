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


class AggregatedTransactionsRequest(object):
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
        'from_transaction_date': 'datetime',
        'to_transaction_date': 'datetime',
        'portfolio_id': 'ResourceId',
        'as_at': 'datetime',
        'metrics': 'list[AggregateSpec]',
        'group_by': 'list[str]',
        'filters': 'list[PropertyFilter]',
        'sort': 'list[OrderBySpec]'
    }

    attribute_map = {
        'from_transaction_date': 'fromTransactionDate',
        'to_transaction_date': 'toTransactionDate',
        'portfolio_id': 'portfolioId',
        'as_at': 'asAt',
        'metrics': 'metrics',
        'group_by': 'groupBy',
        'filters': 'filters',
        'sort': 'sort'
    }

    required_map = {
        'from_transaction_date': 'required',
        'to_transaction_date': 'required',
        'portfolio_id': 'required',
        'as_at': 'optional',
        'metrics': 'required',
        'group_by': 'optional',
        'filters': 'optional',
        'sort': 'optional'
    }

    def __init__(self, from_transaction_date=None, to_transaction_date=None, portfolio_id=None, as_at=None, metrics=None, group_by=None, filters=None, sort=None, local_vars_configuration=None):  # noqa: E501
        """AggregatedTransactionsRequest - a model defined in OpenAPI"
        
        :param from_transaction_date:  (required)
        :type from_transaction_date: datetime
        :param to_transaction_date:  (required)
        :type to_transaction_date: datetime
        :param portfolio_id:  (required)
        :type portfolio_id: lusid.ResourceId
        :param as_at: 
        :type as_at: datetime
        :param metrics:  (required)
        :type metrics: list[lusid.AggregateSpec]
        :param group_by: 
        :type group_by: list[str]
        :param filters: 
        :type filters: list[lusid.PropertyFilter]
        :param sort: 
        :type sort: list[lusid.OrderBySpec]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._from_transaction_date = None
        self._to_transaction_date = None
        self._portfolio_id = None
        self._as_at = None
        self._metrics = None
        self._group_by = None
        self._filters = None
        self._sort = None
        self.discriminator = None

        self.from_transaction_date = from_transaction_date
        self.to_transaction_date = to_transaction_date
        self.portfolio_id = portfolio_id
        self.as_at = as_at
        self.metrics = metrics
        self.group_by = group_by
        self.filters = filters
        self.sort = sort

    @property
    def from_transaction_date(self):
        """Gets the from_transaction_date of this AggregatedTransactionsRequest.  # noqa: E501


        :return: The from_transaction_date of this AggregatedTransactionsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._from_transaction_date

    @from_transaction_date.setter
    def from_transaction_date(self, from_transaction_date):
        """Sets the from_transaction_date of this AggregatedTransactionsRequest.


        :param from_transaction_date: The from_transaction_date of this AggregatedTransactionsRequest.  # noqa: E501
        :type from_transaction_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and from_transaction_date is None:  # noqa: E501
            raise ValueError("Invalid value for `from_transaction_date`, must not be `None`")  # noqa: E501

        self._from_transaction_date = from_transaction_date

    @property
    def to_transaction_date(self):
        """Gets the to_transaction_date of this AggregatedTransactionsRequest.  # noqa: E501


        :return: The to_transaction_date of this AggregatedTransactionsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._to_transaction_date

    @to_transaction_date.setter
    def to_transaction_date(self, to_transaction_date):
        """Sets the to_transaction_date of this AggregatedTransactionsRequest.


        :param to_transaction_date: The to_transaction_date of this AggregatedTransactionsRequest.  # noqa: E501
        :type to_transaction_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and to_transaction_date is None:  # noqa: E501
            raise ValueError("Invalid value for `to_transaction_date`, must not be `None`")  # noqa: E501

        self._to_transaction_date = to_transaction_date

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this AggregatedTransactionsRequest.  # noqa: E501


        :return: The portfolio_id of this AggregatedTransactionsRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this AggregatedTransactionsRequest.


        :param portfolio_id: The portfolio_id of this AggregatedTransactionsRequest.  # noqa: E501
        :type portfolio_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and portfolio_id is None:  # noqa: E501
            raise ValueError("Invalid value for `portfolio_id`, must not be `None`")  # noqa: E501

        self._portfolio_id = portfolio_id

    @property
    def as_at(self):
        """Gets the as_at of this AggregatedTransactionsRequest.  # noqa: E501


        :return: The as_at of this AggregatedTransactionsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this AggregatedTransactionsRequest.


        :param as_at: The as_at of this AggregatedTransactionsRequest.  # noqa: E501
        :type as_at: datetime
        """

        self._as_at = as_at

    @property
    def metrics(self):
        """Gets the metrics of this AggregatedTransactionsRequest.  # noqa: E501


        :return: The metrics of this AggregatedTransactionsRequest.  # noqa: E501
        :rtype: list[lusid.AggregateSpec]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this AggregatedTransactionsRequest.


        :param metrics: The metrics of this AggregatedTransactionsRequest.  # noqa: E501
        :type metrics: list[lusid.AggregateSpec]
        """
        if self.local_vars_configuration.client_side_validation and metrics is None:  # noqa: E501
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501

        self._metrics = metrics

    @property
    def group_by(self):
        """Gets the group_by of this AggregatedTransactionsRequest.  # noqa: E501


        :return: The group_by of this AggregatedTransactionsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this AggregatedTransactionsRequest.


        :param group_by: The group_by of this AggregatedTransactionsRequest.  # noqa: E501
        :type group_by: list[str]
        """

        self._group_by = group_by

    @property
    def filters(self):
        """Gets the filters of this AggregatedTransactionsRequest.  # noqa: E501


        :return: The filters of this AggregatedTransactionsRequest.  # noqa: E501
        :rtype: list[lusid.PropertyFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this AggregatedTransactionsRequest.


        :param filters: The filters of this AggregatedTransactionsRequest.  # noqa: E501
        :type filters: list[lusid.PropertyFilter]
        """

        self._filters = filters

    @property
    def sort(self):
        """Gets the sort of this AggregatedTransactionsRequest.  # noqa: E501


        :return: The sort of this AggregatedTransactionsRequest.  # noqa: E501
        :rtype: list[lusid.OrderBySpec]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this AggregatedTransactionsRequest.


        :param sort: The sort of this AggregatedTransactionsRequest.  # noqa: E501
        :type sort: list[lusid.OrderBySpec]
        """

        self._sort = sort

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
        if not isinstance(other, AggregatedTransactionsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AggregatedTransactionsRequest):
            return True

        return self.to_dict() != other.to_dict()
