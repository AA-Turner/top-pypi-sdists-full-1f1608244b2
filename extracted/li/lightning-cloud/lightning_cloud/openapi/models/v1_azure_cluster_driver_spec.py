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

class V1AzureClusterDriverSpec(object):
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
        'instance_types': 'list[V1InstanceSpec]',
        'internal_test_cluster': 'bool',
        'kubernetes_version': 'str',
        'region': 'str',
        'subscription_id': 'str'
    }

    attribute_map = {
        'instance_types': 'instanceTypes',
        'internal_test_cluster': 'internalTestCluster',
        'kubernetes_version': 'kubernetesVersion',
        'region': 'region',
        'subscription_id': 'subscriptionId'
    }

    def __init__(self, instance_types: 'list[V1InstanceSpec]' =None, internal_test_cluster: 'bool' =None, kubernetes_version: 'str' =None, region: 'str' =None, subscription_id: 'str' =None):  # noqa: E501
        """V1AzureClusterDriverSpec - a model defined in Swagger"""  # noqa: E501
        self._instance_types = None
        self._internal_test_cluster = None
        self._kubernetes_version = None
        self._region = None
        self._subscription_id = None
        self.discriminator = None
        if instance_types is not None:
            self.instance_types = instance_types
        if internal_test_cluster is not None:
            self.internal_test_cluster = internal_test_cluster
        if kubernetes_version is not None:
            self.kubernetes_version = kubernetes_version
        if region is not None:
            self.region = region
        if subscription_id is not None:
            self.subscription_id = subscription_id

    @property
    def instance_types(self) -> 'list[V1InstanceSpec]':
        """Gets the instance_types of this V1AzureClusterDriverSpec.  # noqa: E501


        :return: The instance_types of this V1AzureClusterDriverSpec.  # noqa: E501
        :rtype: list[V1InstanceSpec]
        """
        return self._instance_types

    @instance_types.setter
    def instance_types(self, instance_types: 'list[V1InstanceSpec]'):
        """Sets the instance_types of this V1AzureClusterDriverSpec.


        :param instance_types: The instance_types of this V1AzureClusterDriverSpec.  # noqa: E501
        :type: list[V1InstanceSpec]
        """

        self._instance_types = instance_types

    @property
    def internal_test_cluster(self) -> 'bool':
        """Gets the internal_test_cluster of this V1AzureClusterDriverSpec.  # noqa: E501


        :return: The internal_test_cluster of this V1AzureClusterDriverSpec.  # noqa: E501
        :rtype: bool
        """
        return self._internal_test_cluster

    @internal_test_cluster.setter
    def internal_test_cluster(self, internal_test_cluster: 'bool'):
        """Sets the internal_test_cluster of this V1AzureClusterDriverSpec.


        :param internal_test_cluster: The internal_test_cluster of this V1AzureClusterDriverSpec.  # noqa: E501
        :type: bool
        """

        self._internal_test_cluster = internal_test_cluster

    @property
    def kubernetes_version(self) -> 'str':
        """Gets the kubernetes_version of this V1AzureClusterDriverSpec.  # noqa: E501


        :return: The kubernetes_version of this V1AzureClusterDriverSpec.  # noqa: E501
        :rtype: str
        """
        return self._kubernetes_version

    @kubernetes_version.setter
    def kubernetes_version(self, kubernetes_version: 'str'):
        """Sets the kubernetes_version of this V1AzureClusterDriverSpec.


        :param kubernetes_version: The kubernetes_version of this V1AzureClusterDriverSpec.  # noqa: E501
        :type: str
        """

        self._kubernetes_version = kubernetes_version

    @property
    def region(self) -> 'str':
        """Gets the region of this V1AzureClusterDriverSpec.  # noqa: E501


        :return: The region of this V1AzureClusterDriverSpec.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region: 'str'):
        """Sets the region of this V1AzureClusterDriverSpec.


        :param region: The region of this V1AzureClusterDriverSpec.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def subscription_id(self) -> 'str':
        """Gets the subscription_id of this V1AzureClusterDriverSpec.  # noqa: E501


        :return: The subscription_id of this V1AzureClusterDriverSpec.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id: 'str'):
        """Sets the subscription_id of this V1AzureClusterDriverSpec.


        :param subscription_id: The subscription_id of this V1AzureClusterDriverSpec.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

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
        if issubclass(V1AzureClusterDriverSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1AzureClusterDriverSpec') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1AzureClusterDriverSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'V1AzureClusterDriverSpec') -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
