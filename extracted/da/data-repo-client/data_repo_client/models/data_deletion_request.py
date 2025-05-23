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


class DataDeletionRequest(object):
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
        'delete_type': 'str',
        'transaction_id': 'str',
        'spec_type': 'str',
        'tables': 'list[DataDeletionTableModel]'
    }

    attribute_map = {
        'delete_type': 'deleteType',
        'transaction_id': 'transactionId',
        'spec_type': 'specType',
        'tables': 'tables'
    }

    def __init__(self, delete_type=None, transaction_id=None, spec_type=None, tables=None, local_vars_configuration=None):  # noqa: E501
        """DataDeletionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._delete_type = None
        self._transaction_id = None
        self._spec_type = None
        self._tables = None
        self.discriminator = None

        self.delete_type = delete_type
        if transaction_id is not None:
            self.transaction_id = transaction_id
        self.spec_type = spec_type
        if tables is not None:
            self.tables = tables

    @property
    def delete_type(self):
        """Gets the delete_type of this DataDeletionRequest.  # noqa: E501


        :return: The delete_type of this DataDeletionRequest.  # noqa: E501
        :rtype: str
        """
        return self._delete_type

    @delete_type.setter
    def delete_type(self, delete_type):
        """Sets the delete_type of this DataDeletionRequest.


        :param delete_type: The delete_type of this DataDeletionRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and delete_type is None:  # noqa: E501
            raise ValueError("Invalid value for `delete_type`, must not be `None`")  # noqa: E501
        allowed_values = ["soft"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and delete_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `delete_type` ({0}), must be one of {1}"  # noqa: E501
                .format(delete_type, allowed_values)
            )

        self._delete_type = delete_type

    @property
    def transaction_id(self):
        """Gets the transaction_id of this DataDeletionRequest.  # noqa: E501

        If specified, the deleted data will remain visible to users and snapshot creation until the transaction in question is committed. If the transaction is rolled back, then the changes from this delete and any other operations using this transaction will be undone.   # noqa: E501

        :return: The transaction_id of this DataDeletionRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this DataDeletionRequest.

        If specified, the deleted data will remain visible to users and snapshot creation until the transaction in question is committed. If the transaction is rolled back, then the changes from this delete and any other operations using this transaction will be undone.   # noqa: E501

        :param transaction_id: The transaction_id of this DataDeletionRequest.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def spec_type(self):
        """Gets the spec_type of this DataDeletionRequest.  # noqa: E501


        :return: The spec_type of this DataDeletionRequest.  # noqa: E501
        :rtype: str
        """
        return self._spec_type

    @spec_type.setter
    def spec_type(self, spec_type):
        """Sets the spec_type of this DataDeletionRequest.


        :param spec_type: The spec_type of this DataDeletionRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and spec_type is None:  # noqa: E501
            raise ValueError("Invalid value for `spec_type`, must not be `None`")  # noqa: E501
        allowed_values = ["gcsFile", "jsonArray"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and spec_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `spec_type` ({0}), must be one of {1}"  # noqa: E501
                .format(spec_type, allowed_values)
            )

        self._spec_type = spec_type

    @property
    def tables(self):
        """Gets the tables of this DataDeletionRequest.  # noqa: E501


        :return: The tables of this DataDeletionRequest.  # noqa: E501
        :rtype: list[DataDeletionTableModel]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this DataDeletionRequest.


        :param tables: The tables of this DataDeletionRequest.  # noqa: E501
        :type: list[DataDeletionTableModel]
        """

        self._tables = tables

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
        if not isinstance(other, DataDeletionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataDeletionRequest):
            return True

        return self.to_dict() != other.to_dict()
