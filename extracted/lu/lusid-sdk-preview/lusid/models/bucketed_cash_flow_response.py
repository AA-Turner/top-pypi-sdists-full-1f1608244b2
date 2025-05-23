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


class BucketedCashFlowResponse(object):
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
        'href': 'str',
        'data': 'list[dict(str, object)]',
        'report_currency': 'str',
        'data_schema': 'ResultDataSchema',
        'failed': 'dict(str, ErrorDetail)',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'data': 'data',
        'report_currency': 'reportCurrency',
        'data_schema': 'dataSchema',
        'failed': 'failed',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'data': 'optional',
        'report_currency': 'optional',
        'data_schema': 'optional',
        'failed': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, data=None, report_currency=None, data_schema=None, failed=None, links=None, local_vars_configuration=None):  # noqa: E501
        """BucketedCashFlowResponse - a model defined in OpenAPI"
        
        :param href: 
        :type href: str
        :param data:  List of dictionary bucketed cash flow result set.  Each dictionary represent a bucketed cashflow result set keyed by AddressKeys.  e.g. dictionary[\"Valuation/CashFlowAmount\"] for the aggregated cash flow amount for the bucket.  e.g. suppose \"RoundUp\" method, then dictionary[\"Valuation/CashFlowDate/RoundUp\"] returns the bucketed cashflow date.
        :type data: list[dict(str, object)]
        :param report_currency:  Three letter ISO currency string indicating what currency to report in for ReportCcy denominated queries.  If not present then the currency of the relevant portfolio will be used in its place where relevant.
        :type report_currency: str
        :param data_schema: 
        :type data_schema: lusid.ResultDataSchema
        :param failed:  Information about where instruments have failed to return cashflows in so far as it is available.  e.g., failure to retrieve a market quote for a floating rate instrument.
        :type failed: dict[str, lusid.ErrorDetail]
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._data = None
        self._report_currency = None
        self._data_schema = None
        self._failed = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.data = data
        self.report_currency = report_currency
        if data_schema is not None:
            self.data_schema = data_schema
        self.failed = failed
        self.links = links

    @property
    def href(self):
        """Gets the href of this BucketedCashFlowResponse.  # noqa: E501


        :return: The href of this BucketedCashFlowResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BucketedCashFlowResponse.


        :param href: The href of this BucketedCashFlowResponse.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def data(self):
        """Gets the data of this BucketedCashFlowResponse.  # noqa: E501

        List of dictionary bucketed cash flow result set.  Each dictionary represent a bucketed cashflow result set keyed by AddressKeys.  e.g. dictionary[\"Valuation/CashFlowAmount\"] for the aggregated cash flow amount for the bucket.  e.g. suppose \"RoundUp\" method, then dictionary[\"Valuation/CashFlowDate/RoundUp\"] returns the bucketed cashflow date.  # noqa: E501

        :return: The data of this BucketedCashFlowResponse.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this BucketedCashFlowResponse.

        List of dictionary bucketed cash flow result set.  Each dictionary represent a bucketed cashflow result set keyed by AddressKeys.  e.g. dictionary[\"Valuation/CashFlowAmount\"] for the aggregated cash flow amount for the bucket.  e.g. suppose \"RoundUp\" method, then dictionary[\"Valuation/CashFlowDate/RoundUp\"] returns the bucketed cashflow date.  # noqa: E501

        :param data: The data of this BucketedCashFlowResponse.  # noqa: E501
        :type data: list[dict(str, object)]
        """

        self._data = data

    @property
    def report_currency(self):
        """Gets the report_currency of this BucketedCashFlowResponse.  # noqa: E501

        Three letter ISO currency string indicating what currency to report in for ReportCcy denominated queries.  If not present then the currency of the relevant portfolio will be used in its place where relevant.  # noqa: E501

        :return: The report_currency of this BucketedCashFlowResponse.  # noqa: E501
        :rtype: str
        """
        return self._report_currency

    @report_currency.setter
    def report_currency(self, report_currency):
        """Sets the report_currency of this BucketedCashFlowResponse.

        Three letter ISO currency string indicating what currency to report in for ReportCcy denominated queries.  If not present then the currency of the relevant portfolio will be used in its place where relevant.  # noqa: E501

        :param report_currency: The report_currency of this BucketedCashFlowResponse.  # noqa: E501
        :type report_currency: str
        """

        self._report_currency = report_currency

    @property
    def data_schema(self):
        """Gets the data_schema of this BucketedCashFlowResponse.  # noqa: E501


        :return: The data_schema of this BucketedCashFlowResponse.  # noqa: E501
        :rtype: lusid.ResultDataSchema
        """
        return self._data_schema

    @data_schema.setter
    def data_schema(self, data_schema):
        """Sets the data_schema of this BucketedCashFlowResponse.


        :param data_schema: The data_schema of this BucketedCashFlowResponse.  # noqa: E501
        :type data_schema: lusid.ResultDataSchema
        """

        self._data_schema = data_schema

    @property
    def failed(self):
        """Gets the failed of this BucketedCashFlowResponse.  # noqa: E501

        Information about where instruments have failed to return cashflows in so far as it is available.  e.g., failure to retrieve a market quote for a floating rate instrument.  # noqa: E501

        :return: The failed of this BucketedCashFlowResponse.  # noqa: E501
        :rtype: dict[str, lusid.ErrorDetail]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this BucketedCashFlowResponse.

        Information about where instruments have failed to return cashflows in so far as it is available.  e.g., failure to retrieve a market quote for a floating rate instrument.  # noqa: E501

        :param failed: The failed of this BucketedCashFlowResponse.  # noqa: E501
        :type failed: dict[str, lusid.ErrorDetail]
        """

        self._failed = failed

    @property
    def links(self):
        """Gets the links of this BucketedCashFlowResponse.  # noqa: E501


        :return: The links of this BucketedCashFlowResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this BucketedCashFlowResponse.


        :param links: The links of this BucketedCashFlowResponse.  # noqa: E501
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
        if not isinstance(other, BucketedCashFlowResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BucketedCashFlowResponse):
            return True

        return self.to_dict() != other.to_dict()
