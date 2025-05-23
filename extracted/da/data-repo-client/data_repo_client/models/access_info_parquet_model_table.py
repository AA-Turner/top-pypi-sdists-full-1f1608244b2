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


class AccessInfoParquetModelTable(object):
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
        'name': 'str',
        'url': 'str',
        'sas_token': 'str'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url',
        'sas_token': 'sasToken'
    }

    def __init__(self, name=None, url=None, sas_token=None, local_vars_configuration=None):  # noqa: E501
        """AccessInfoParquetModelTable - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._url = None
        self._sas_token = None
        self.discriminator = None

        self.name = name
        self.url = url
        self.sas_token = sas_token

    @property
    def name(self):
        """Gets the name of this AccessInfoParquetModelTable.  # noqa: E501

        The name of the dataset table   # noqa: E501

        :return: The name of this AccessInfoParquetModelTable.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessInfoParquetModelTable.

        The name of the dataset table   # noqa: E501

        :param name: The name of this AccessInfoParquetModelTable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this AccessInfoParquetModelTable.  # noqa: E501

        The link to access the container that stores parquet files for this table   # noqa: E501

        :return: The url of this AccessInfoParquetModelTable.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AccessInfoParquetModelTable.

        The link to access the container that stores parquet files for this table   # noqa: E501

        :param url: The url of this AccessInfoParquetModelTable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def sas_token(self):
        """Gets the sas_token of this AccessInfoParquetModelTable.  # noqa: E501

        A short lived SAS token to access the parquet files for this table   # noqa: E501

        :return: The sas_token of this AccessInfoParquetModelTable.  # noqa: E501
        :rtype: str
        """
        return self._sas_token

    @sas_token.setter
    def sas_token(self, sas_token):
        """Sets the sas_token of this AccessInfoParquetModelTable.

        A short lived SAS token to access the parquet files for this table   # noqa: E501

        :param sas_token: The sas_token of this AccessInfoParquetModelTable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sas_token is None:  # noqa: E501
            raise ValueError("Invalid value for `sas_token`, must not be `None`")  # noqa: E501

        self._sas_token = sas_token

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
        if not isinstance(other, AccessInfoParquetModelTable):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessInfoParquetModelTable):
            return True

        return self.to_dict() != other.to_dict()
