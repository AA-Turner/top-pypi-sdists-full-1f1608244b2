# coding: utf-8

"""
    ark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RequestCountsForListBatchInferenceJobsOutput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'completed': 'int',
        'failed': 'int',
        'total': 'int'
    }

    attribute_map = {
        'completed': 'Completed',
        'failed': 'Failed',
        'total': 'Total'
    }

    def __init__(self, completed=None, failed=None, total=None, _configuration=None):  # noqa: E501
        """RequestCountsForListBatchInferenceJobsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._completed = None
        self._failed = None
        self._total = None
        self.discriminator = None

        if completed is not None:
            self.completed = completed
        if failed is not None:
            self.failed = failed
        if total is not None:
            self.total = total

    @property
    def completed(self):
        """Gets the completed of this RequestCountsForListBatchInferenceJobsOutput.  # noqa: E501


        :return: The completed of this RequestCountsForListBatchInferenceJobsOutput.  # noqa: E501
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this RequestCountsForListBatchInferenceJobsOutput.


        :param completed: The completed of this RequestCountsForListBatchInferenceJobsOutput.  # noqa: E501
        :type: int
        """

        self._completed = completed

    @property
    def failed(self):
        """Gets the failed of this RequestCountsForListBatchInferenceJobsOutput.  # noqa: E501


        :return: The failed of this RequestCountsForListBatchInferenceJobsOutput.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this RequestCountsForListBatchInferenceJobsOutput.


        :param failed: The failed of this RequestCountsForListBatchInferenceJobsOutput.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def total(self):
        """Gets the total of this RequestCountsForListBatchInferenceJobsOutput.  # noqa: E501


        :return: The total of this RequestCountsForListBatchInferenceJobsOutput.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this RequestCountsForListBatchInferenceJobsOutput.


        :param total: The total of this RequestCountsForListBatchInferenceJobsOutput.  # noqa: E501
        :type: int
        """

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(RequestCountsForListBatchInferenceJobsOutput, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RequestCountsForListBatchInferenceJobsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestCountsForListBatchInferenceJobsOutput):
            return True

        return self.to_dict() != other.to_dict()
