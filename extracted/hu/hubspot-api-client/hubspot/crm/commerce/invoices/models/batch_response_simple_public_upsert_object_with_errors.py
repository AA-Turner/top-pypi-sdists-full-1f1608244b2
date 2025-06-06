# coding: utf-8

"""
    Invoices

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.crm.commerce.invoices.configuration import Configuration


class BatchResponseSimplePublicUpsertObjectWithErrors(object):
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
        "completed_at": "datetime",
        "num_errors": "int",
        "requested_at": "datetime",
        "started_at": "datetime",
        "links": "dict[str, str]",
        "results": "list[SimplePublicUpsertObject]",
        "errors": "list[StandardError]",
        "status": "str",
    }

    attribute_map = {
        "completed_at": "completedAt",
        "num_errors": "numErrors",
        "requested_at": "requestedAt",
        "started_at": "startedAt",
        "links": "links",
        "results": "results",
        "errors": "errors",
        "status": "status",
    }

    def __init__(self, completed_at=None, num_errors=None, requested_at=None, started_at=None, links=None, results=None, errors=None, status=None, local_vars_configuration=None):  # noqa: E501
        """BatchResponseSimplePublicUpsertObjectWithErrors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._completed_at = None
        self._num_errors = None
        self._requested_at = None
        self._started_at = None
        self._links = None
        self._results = None
        self._errors = None
        self._status = None
        self.discriminator = None

        self.completed_at = completed_at
        if num_errors is not None:
            self.num_errors = num_errors
        if requested_at is not None:
            self.requested_at = requested_at
        self.started_at = started_at
        if links is not None:
            self.links = links
        self.results = results
        if errors is not None:
            self.errors = errors
        self.status = status

    @property
    def completed_at(self):
        """Gets the completed_at of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501


        :return: The completed_at of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this BatchResponseSimplePublicUpsertObjectWithErrors.


        :param completed_at: The completed_at of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :type completed_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and completed_at is None:  # noqa: E501
            raise ValueError("Invalid value for `completed_at`, must not be `None`")  # noqa: E501

        self._completed_at = completed_at

    @property
    def num_errors(self):
        """Gets the num_errors of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501


        :return: The num_errors of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :rtype: int
        """
        return self._num_errors

    @num_errors.setter
    def num_errors(self, num_errors):
        """Sets the num_errors of this BatchResponseSimplePublicUpsertObjectWithErrors.


        :param num_errors: The num_errors of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :type num_errors: int
        """

        self._num_errors = num_errors

    @property
    def requested_at(self):
        """Gets the requested_at of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501


        :return: The requested_at of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :rtype: datetime
        """
        return self._requested_at

    @requested_at.setter
    def requested_at(self, requested_at):
        """Sets the requested_at of this BatchResponseSimplePublicUpsertObjectWithErrors.


        :param requested_at: The requested_at of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :type requested_at: datetime
        """

        self._requested_at = requested_at

    @property
    def started_at(self):
        """Gets the started_at of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501


        :return: The started_at of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this BatchResponseSimplePublicUpsertObjectWithErrors.


        :param started_at: The started_at of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :type started_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def links(self):
        """Gets the links of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501


        :return: The links of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this BatchResponseSimplePublicUpsertObjectWithErrors.


        :param links: The links of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :type links: dict[str, str]
        """

        self._links = links

    @property
    def results(self):
        """Gets the results of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501


        :return: The results of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :rtype: list[SimplePublicUpsertObject]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this BatchResponseSimplePublicUpsertObjectWithErrors.


        :param results: The results of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :type results: list[SimplePublicUpsertObject]
        """
        if self.local_vars_configuration.client_side_validation and results is None:  # noqa: E501
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    @property
    def errors(self):
        """Gets the errors of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501


        :return: The errors of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :rtype: list[StandardError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this BatchResponseSimplePublicUpsertObjectWithErrors.


        :param errors: The errors of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :type errors: list[StandardError]
        """

        self._errors = errors

    @property
    def status(self):
        """Gets the status of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501


        :return: The status of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchResponseSimplePublicUpsertObjectWithErrors.


        :param status: The status of this BatchResponseSimplePublicUpsertObjectWithErrors.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `status` ({0}), must be one of {1}".format(status, allowed_values))  # noqa: E501

        self._status = status

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
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
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
        if not isinstance(other, BatchResponseSimplePublicUpsertObjectWithErrors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchResponseSimplePublicUpsertObjectWithErrors):
            return True

        return self.to_dict() != other.to_dict()
