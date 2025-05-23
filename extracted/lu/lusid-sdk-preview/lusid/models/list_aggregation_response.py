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


class ListAggregationResponse(object):
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
        'aggregation_effective_at': 'datetime',
        'aggregation_as_at': 'datetime',
        'href': 'str',
        'data': 'list[dict(str, object)]',
        'aggregation_currency': 'str',
        'data_schema': 'ResultDataSchema',
        'aggregation_failures': 'list[AggregationMeasureFailureDetail]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'aggregation_effective_at': 'aggregationEffectiveAt',
        'aggregation_as_at': 'aggregationAsAt',
        'href': 'href',
        'data': 'data',
        'aggregation_currency': 'aggregationCurrency',
        'data_schema': 'dataSchema',
        'aggregation_failures': 'aggregationFailures',
        'links': 'links'
    }

    required_map = {
        'aggregation_effective_at': 'optional',
        'aggregation_as_at': 'optional',
        'href': 'optional',
        'data': 'optional',
        'aggregation_currency': 'optional',
        'data_schema': 'optional',
        'aggregation_failures': 'optional',
        'links': 'optional'
    }

    def __init__(self, aggregation_effective_at=None, aggregation_as_at=None, href=None, data=None, aggregation_currency=None, data_schema=None, aggregation_failures=None, links=None, local_vars_configuration=None):  # noqa: E501
        """ListAggregationResponse - a model defined in OpenAPI"
        
        :param aggregation_effective_at: 
        :type aggregation_effective_at: datetime
        :param aggregation_as_at: 
        :type aggregation_as_at: datetime
        :param href: 
        :type href: str
        :param data: 
        :type data: list[dict(str, object)]
        :param aggregation_currency: 
        :type aggregation_currency: str
        :param data_schema: 
        :type data_schema: lusid.ResultDataSchema
        :param aggregation_failures: 
        :type aggregation_failures: list[lusid.AggregationMeasureFailureDetail]
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._aggregation_effective_at = None
        self._aggregation_as_at = None
        self._href = None
        self._data = None
        self._aggregation_currency = None
        self._data_schema = None
        self._aggregation_failures = None
        self._links = None
        self.discriminator = None

        if aggregation_effective_at is not None:
            self.aggregation_effective_at = aggregation_effective_at
        if aggregation_as_at is not None:
            self.aggregation_as_at = aggregation_as_at
        self.href = href
        self.data = data
        self.aggregation_currency = aggregation_currency
        if data_schema is not None:
            self.data_schema = data_schema
        self.aggregation_failures = aggregation_failures
        self.links = links

    @property
    def aggregation_effective_at(self):
        """Gets the aggregation_effective_at of this ListAggregationResponse.  # noqa: E501


        :return: The aggregation_effective_at of this ListAggregationResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._aggregation_effective_at

    @aggregation_effective_at.setter
    def aggregation_effective_at(self, aggregation_effective_at):
        """Sets the aggregation_effective_at of this ListAggregationResponse.


        :param aggregation_effective_at: The aggregation_effective_at of this ListAggregationResponse.  # noqa: E501
        :type aggregation_effective_at: datetime
        """

        self._aggregation_effective_at = aggregation_effective_at

    @property
    def aggregation_as_at(self):
        """Gets the aggregation_as_at of this ListAggregationResponse.  # noqa: E501


        :return: The aggregation_as_at of this ListAggregationResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._aggregation_as_at

    @aggregation_as_at.setter
    def aggregation_as_at(self, aggregation_as_at):
        """Sets the aggregation_as_at of this ListAggregationResponse.


        :param aggregation_as_at: The aggregation_as_at of this ListAggregationResponse.  # noqa: E501
        :type aggregation_as_at: datetime
        """

        self._aggregation_as_at = aggregation_as_at

    @property
    def href(self):
        """Gets the href of this ListAggregationResponse.  # noqa: E501


        :return: The href of this ListAggregationResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ListAggregationResponse.


        :param href: The href of this ListAggregationResponse.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def data(self):
        """Gets the data of this ListAggregationResponse.  # noqa: E501


        :return: The data of this ListAggregationResponse.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListAggregationResponse.


        :param data: The data of this ListAggregationResponse.  # noqa: E501
        :type data: list[dict(str, object)]
        """

        self._data = data

    @property
    def aggregation_currency(self):
        """Gets the aggregation_currency of this ListAggregationResponse.  # noqa: E501


        :return: The aggregation_currency of this ListAggregationResponse.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_currency

    @aggregation_currency.setter
    def aggregation_currency(self, aggregation_currency):
        """Sets the aggregation_currency of this ListAggregationResponse.


        :param aggregation_currency: The aggregation_currency of this ListAggregationResponse.  # noqa: E501
        :type aggregation_currency: str
        """

        self._aggregation_currency = aggregation_currency

    @property
    def data_schema(self):
        """Gets the data_schema of this ListAggregationResponse.  # noqa: E501


        :return: The data_schema of this ListAggregationResponse.  # noqa: E501
        :rtype: lusid.ResultDataSchema
        """
        return self._data_schema

    @data_schema.setter
    def data_schema(self, data_schema):
        """Sets the data_schema of this ListAggregationResponse.


        :param data_schema: The data_schema of this ListAggregationResponse.  # noqa: E501
        :type data_schema: lusid.ResultDataSchema
        """

        self._data_schema = data_schema

    @property
    def aggregation_failures(self):
        """Gets the aggregation_failures of this ListAggregationResponse.  # noqa: E501


        :return: The aggregation_failures of this ListAggregationResponse.  # noqa: E501
        :rtype: list[lusid.AggregationMeasureFailureDetail]
        """
        return self._aggregation_failures

    @aggregation_failures.setter
    def aggregation_failures(self, aggregation_failures):
        """Sets the aggregation_failures of this ListAggregationResponse.


        :param aggregation_failures: The aggregation_failures of this ListAggregationResponse.  # noqa: E501
        :type aggregation_failures: list[lusid.AggregationMeasureFailureDetail]
        """

        self._aggregation_failures = aggregation_failures

    @property
    def links(self):
        """Gets the links of this ListAggregationResponse.  # noqa: E501


        :return: The links of this ListAggregationResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ListAggregationResponse.


        :param links: The links of this ListAggregationResponse.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, ListAggregationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListAggregationResponse):
            return True

        return self.to_dict() != other.to_dict()
