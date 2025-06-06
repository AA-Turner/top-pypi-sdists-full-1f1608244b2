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


class QueryCashFlowsRequest(object):
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
        'as_at': 'datetime',
        'window_start': 'datetime',
        'window_end': 'datetime',
        'portfolio_entity_ids': 'list[PortfolioEntityId]',
        'recipe_id': 'ResourceId',
        'effective_at': 'datetime'
    }

    attribute_map = {
        'as_at': 'asAt',
        'window_start': 'windowStart',
        'window_end': 'windowEnd',
        'portfolio_entity_ids': 'portfolioEntityIds',
        'recipe_id': 'recipeId',
        'effective_at': 'effectiveAt'
    }

    required_map = {
        'as_at': 'optional',
        'window_start': 'required',
        'window_end': 'required',
        'portfolio_entity_ids': 'required',
        'recipe_id': 'required',
        'effective_at': 'required'
    }

    def __init__(self, as_at=None, window_start=None, window_end=None, portfolio_entity_ids=None, recipe_id=None, effective_at=None, local_vars_configuration=None):  # noqa: E501
        """QueryCashFlowsRequest - a model defined in OpenAPI"
        
        :param as_at:  The time of the system at which to query for cashflows.
        :type as_at: datetime
        :param window_start:  The start date of the window. (required)
        :type window_start: datetime
        :param window_end:  The end date of the window. (required)
        :type window_end: datetime
        :param portfolio_entity_ids:  The set of portfolios and portfolio groups to which the instrument events must belong. (required)
        :type portfolio_entity_ids: list[lusid.PortfolioEntityId]
        :param recipe_id:  (required)
        :type recipe_id: lusid.ResourceId
        :param effective_at:  The Effective date used in the valuation of the cashflows. (required)
        :type effective_at: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._as_at = None
        self._window_start = None
        self._window_end = None
        self._portfolio_entity_ids = None
        self._recipe_id = None
        self._effective_at = None
        self.discriminator = None

        self.as_at = as_at
        self.window_start = window_start
        self.window_end = window_end
        self.portfolio_entity_ids = portfolio_entity_ids
        self.recipe_id = recipe_id
        self.effective_at = effective_at

    @property
    def as_at(self):
        """Gets the as_at of this QueryCashFlowsRequest.  # noqa: E501

        The time of the system at which to query for cashflows.  # noqa: E501

        :return: The as_at of this QueryCashFlowsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this QueryCashFlowsRequest.

        The time of the system at which to query for cashflows.  # noqa: E501

        :param as_at: The as_at of this QueryCashFlowsRequest.  # noqa: E501
        :type as_at: datetime
        """

        self._as_at = as_at

    @property
    def window_start(self):
        """Gets the window_start of this QueryCashFlowsRequest.  # noqa: E501

        The start date of the window.  # noqa: E501

        :return: The window_start of this QueryCashFlowsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._window_start

    @window_start.setter
    def window_start(self, window_start):
        """Sets the window_start of this QueryCashFlowsRequest.

        The start date of the window.  # noqa: E501

        :param window_start: The window_start of this QueryCashFlowsRequest.  # noqa: E501
        :type window_start: datetime
        """
        if self.local_vars_configuration.client_side_validation and window_start is None:  # noqa: E501
            raise ValueError("Invalid value for `window_start`, must not be `None`")  # noqa: E501

        self._window_start = window_start

    @property
    def window_end(self):
        """Gets the window_end of this QueryCashFlowsRequest.  # noqa: E501

        The end date of the window.  # noqa: E501

        :return: The window_end of this QueryCashFlowsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._window_end

    @window_end.setter
    def window_end(self, window_end):
        """Sets the window_end of this QueryCashFlowsRequest.

        The end date of the window.  # noqa: E501

        :param window_end: The window_end of this QueryCashFlowsRequest.  # noqa: E501
        :type window_end: datetime
        """
        if self.local_vars_configuration.client_side_validation and window_end is None:  # noqa: E501
            raise ValueError("Invalid value for `window_end`, must not be `None`")  # noqa: E501

        self._window_end = window_end

    @property
    def portfolio_entity_ids(self):
        """Gets the portfolio_entity_ids of this QueryCashFlowsRequest.  # noqa: E501

        The set of portfolios and portfolio groups to which the instrument events must belong.  # noqa: E501

        :return: The portfolio_entity_ids of this QueryCashFlowsRequest.  # noqa: E501
        :rtype: list[lusid.PortfolioEntityId]
        """
        return self._portfolio_entity_ids

    @portfolio_entity_ids.setter
    def portfolio_entity_ids(self, portfolio_entity_ids):
        """Sets the portfolio_entity_ids of this QueryCashFlowsRequest.

        The set of portfolios and portfolio groups to which the instrument events must belong.  # noqa: E501

        :param portfolio_entity_ids: The portfolio_entity_ids of this QueryCashFlowsRequest.  # noqa: E501
        :type portfolio_entity_ids: list[lusid.PortfolioEntityId]
        """
        if self.local_vars_configuration.client_side_validation and portfolio_entity_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `portfolio_entity_ids`, must not be `None`")  # noqa: E501

        self._portfolio_entity_ids = portfolio_entity_ids

    @property
    def recipe_id(self):
        """Gets the recipe_id of this QueryCashFlowsRequest.  # noqa: E501


        :return: The recipe_id of this QueryCashFlowsRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        """Sets the recipe_id of this QueryCashFlowsRequest.


        :param recipe_id: The recipe_id of this QueryCashFlowsRequest.  # noqa: E501
        :type recipe_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and recipe_id is None:  # noqa: E501
            raise ValueError("Invalid value for `recipe_id`, must not be `None`")  # noqa: E501

        self._recipe_id = recipe_id

    @property
    def effective_at(self):
        """Gets the effective_at of this QueryCashFlowsRequest.  # noqa: E501

        The Effective date used in the valuation of the cashflows.  # noqa: E501

        :return: The effective_at of this QueryCashFlowsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this QueryCashFlowsRequest.

        The Effective date used in the valuation of the cashflows.  # noqa: E501

        :param effective_at: The effective_at of this QueryCashFlowsRequest.  # noqa: E501
        :type effective_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_at is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

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
        if not isinstance(other, QueryCashFlowsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryCashFlowsRequest):
            return True

        return self.to_dict() != other.to_dict()
