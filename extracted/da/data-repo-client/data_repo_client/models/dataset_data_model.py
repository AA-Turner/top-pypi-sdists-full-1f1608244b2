# coding: utf-8

"""
    Data Repository API

    <details><summary>This document defines the REST API for the Terra Data Repository.</summary> <p> **Status: design in progress** There are a few top-level endpoints (besides some used by swagger):  * / - generated by swagger: swagger API page that provides this documentation and a live UI for submitting REST requests  * /status - provides the operational status of the service  * /configuration - provides the basic configuration and information about the service  * /api - is the authenticated and authorized Data Repository API  * /ga4gh/drs/v1 - is a transcription of the Data Repository Service API  The API endpoints are organized by interface. Each interface is separately versioned. <p> **Notes on Naming** <p> All of the reference items are suffixed with \\\"Model\\\". Those names are used as the class names in the generated Java code. It is helpful to distinguish these model classes from other related classes, like the DAO classes and the operation classes. </details>   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from data_repo_client.configuration import Configuration


class DatasetDataModel(object):
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
        'result': 'list[object]',
        'total_row_count': 'int',
        'filtered_row_count': 'int'
    }

    attribute_map = {
        'result': 'result',
        'total_row_count': 'totalRowCount',
        'filtered_row_count': 'filteredRowCount'
    }

    def __init__(self, result=None, total_row_count=None, filtered_row_count=None, local_vars_configuration=None):  # noqa: E501
        """DatasetDataModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._total_row_count = None
        self._filtered_row_count = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if total_row_count is not None:
            self.total_row_count = total_row_count
        if filtered_row_count is not None:
            self.filtered_row_count = filtered_row_count

    @property
    def result(self):
        """Gets the result of this DatasetDataModel.  # noqa: E501

        Data from a dataset table  # noqa: E501

        :return: The result of this DatasetDataModel.  # noqa: E501
        :rtype: list[object]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DatasetDataModel.

        Data from a dataset table  # noqa: E501

        :param result: The result of this DatasetDataModel.  # noqa: E501
        :type: list[object]
        """

        self._result = result

    @property
    def total_row_count(self):
        """Gets the total_row_count of this DatasetDataModel.  # noqa: E501


        :return: The total_row_count of this DatasetDataModel.  # noqa: E501
        :rtype: int
        """
        return self._total_row_count

    @total_row_count.setter
    def total_row_count(self, total_row_count):
        """Sets the total_row_count of this DatasetDataModel.


        :param total_row_count: The total_row_count of this DatasetDataModel.  # noqa: E501
        :type: int
        """

        self._total_row_count = total_row_count

    @property
    def filtered_row_count(self):
        """Gets the filtered_row_count of this DatasetDataModel.  # noqa: E501


        :return: The filtered_row_count of this DatasetDataModel.  # noqa: E501
        :rtype: int
        """
        return self._filtered_row_count

    @filtered_row_count.setter
    def filtered_row_count(self, filtered_row_count):
        """Sets the filtered_row_count of this DatasetDataModel.


        :param filtered_row_count: The filtered_row_count of this DatasetDataModel.  # noqa: E501
        :type: int
        """

        self._filtered_row_count = filtered_row_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DatasetDataModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatasetDataModel):
            return True

        return self.to_dict() != other.to_dict()
