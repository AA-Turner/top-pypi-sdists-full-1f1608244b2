# coding: utf-8

"""
    external/v1/auth_service.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    NOTE
    ----
    standard swagger-codegen-cli for this python client has been modified
    by custom templates. The purpose of these templates is to include
    typing information in the API and Model code. Please refer to the
    main grid repository for more info
"""

import pprint
import re  # noqa: F401

from typing import TYPE_CHECKING

import six

if TYPE_CHECKING:
    from datetime import datetime
    from lightning_cloud.openapi.models import *

class Validate(object):
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
        'aws': 'V1AwsDataConnection',
        'check_is_public': 'bool',
        'cluster_ids': 'list[str]',
        'gcp': 'V1GcpDataConnection'
    }

    attribute_map = {
        'aws': 'aws',
        'check_is_public': 'checkIsPublic',
        'cluster_ids': 'clusterIds',
        'gcp': 'gcp'
    }

    def __init__(self, aws: 'V1AwsDataConnection' =None, check_is_public: 'bool' =None, cluster_ids: 'list[str]' =None, gcp: 'V1GcpDataConnection' =None):  # noqa: E501
        """Validate - a model defined in Swagger"""  # noqa: E501
        self._aws = None
        self._check_is_public = None
        self._cluster_ids = None
        self._gcp = None
        self.discriminator = None
        if aws is not None:
            self.aws = aws
        if check_is_public is not None:
            self.check_is_public = check_is_public
        if cluster_ids is not None:
            self.cluster_ids = cluster_ids
        if gcp is not None:
            self.gcp = gcp

    @property
    def aws(self) -> 'V1AwsDataConnection':
        """Gets the aws of this Validate.  # noqa: E501


        :return: The aws of this Validate.  # noqa: E501
        :rtype: V1AwsDataConnection
        """
        return self._aws

    @aws.setter
    def aws(self, aws: 'V1AwsDataConnection'):
        """Sets the aws of this Validate.


        :param aws: The aws of this Validate.  # noqa: E501
        :type: V1AwsDataConnection
        """

        self._aws = aws

    @property
    def check_is_public(self) -> 'bool':
        """Gets the check_is_public of this Validate.  # noqa: E501


        :return: The check_is_public of this Validate.  # noqa: E501
        :rtype: bool
        """
        return self._check_is_public

    @check_is_public.setter
    def check_is_public(self, check_is_public: 'bool'):
        """Sets the check_is_public of this Validate.


        :param check_is_public: The check_is_public of this Validate.  # noqa: E501
        :type: bool
        """

        self._check_is_public = check_is_public

    @property
    def cluster_ids(self) -> 'list[str]':
        """Gets the cluster_ids of this Validate.  # noqa: E501


        :return: The cluster_ids of this Validate.  # noqa: E501
        :rtype: list[str]
        """
        return self._cluster_ids

    @cluster_ids.setter
    def cluster_ids(self, cluster_ids: 'list[str]'):
        """Sets the cluster_ids of this Validate.


        :param cluster_ids: The cluster_ids of this Validate.  # noqa: E501
        :type: list[str]
        """

        self._cluster_ids = cluster_ids

    @property
    def gcp(self) -> 'V1GcpDataConnection':
        """Gets the gcp of this Validate.  # noqa: E501


        :return: The gcp of this Validate.  # noqa: E501
        :rtype: V1GcpDataConnection
        """
        return self._gcp

    @gcp.setter
    def gcp(self, gcp: 'V1GcpDataConnection'):
        """Sets the gcp of this Validate.


        :param gcp: The gcp of this Validate.  # noqa: E501
        :type: V1GcpDataConnection
        """

        self._gcp = gcp

    def to_dict(self) -> dict:
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
        if issubclass(Validate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'Validate') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, Validate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Validate') -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
