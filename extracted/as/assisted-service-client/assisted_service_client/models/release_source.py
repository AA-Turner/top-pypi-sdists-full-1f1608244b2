# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ReleaseSource(object):
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
        'openshift_version': 'str',
        'multi_cpu_architectures': 'list[str]',
        'upgrade_channels': 'list[UpgradeChannel]'
    }

    attribute_map = {
        'openshift_version': 'openshift_version',
        'multi_cpu_architectures': 'multi_cpu_architectures',
        'upgrade_channels': 'upgrade_channels'
    }

    def __init__(self, openshift_version=None, multi_cpu_architectures=None, upgrade_channels=None):  # noqa: E501
        """ReleaseSource - a model defined in Swagger"""  # noqa: E501

        self._openshift_version = None
        self._multi_cpu_architectures = None
        self._upgrade_channels = None
        self.discriminator = None

        self.openshift_version = openshift_version
        self.multi_cpu_architectures = multi_cpu_architectures
        self.upgrade_channels = upgrade_channels

    @property
    def openshift_version(self):
        """Gets the openshift_version of this ReleaseSource.  # noqa: E501

        Version of the OpenShift cluster.  # noqa: E501

        :return: The openshift_version of this ReleaseSource.  # noqa: E501
        :rtype: str
        """
        return self._openshift_version

    @openshift_version.setter
    def openshift_version(self, openshift_version):
        """Sets the openshift_version of this ReleaseSource.

        Version of the OpenShift cluster.  # noqa: E501

        :param openshift_version: The openshift_version of this ReleaseSource.  # noqa: E501
        :type: str
        """
        if openshift_version is None:
            raise ValueError("Invalid value for `openshift_version`, must not be `None`")  # noqa: E501

        self._openshift_version = openshift_version

    @property
    def multi_cpu_architectures(self):
        """Gets the multi_cpu_architectures of this ReleaseSource.  # noqa: E501


        :return: The multi_cpu_architectures of this ReleaseSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._multi_cpu_architectures

    @multi_cpu_architectures.setter
    def multi_cpu_architectures(self, multi_cpu_architectures):
        """Sets the multi_cpu_architectures of this ReleaseSource.


        :param multi_cpu_architectures: The multi_cpu_architectures of this ReleaseSource.  # noqa: E501
        :type: list[str]
        """
        if multi_cpu_architectures is None:
            raise ValueError("Invalid value for `multi_cpu_architectures`, must not be `None`")  # noqa: E501
        allowed_values = ["x86_64", "aarch64", "arm64", "ppc64le", "s390x"]  # noqa: E501
        if not set(multi_cpu_architectures).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `multi_cpu_architectures` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(multi_cpu_architectures) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._multi_cpu_architectures = multi_cpu_architectures

    @property
    def upgrade_channels(self):
        """Gets the upgrade_channels of this ReleaseSource.  # noqa: E501


        :return: The upgrade_channels of this ReleaseSource.  # noqa: E501
        :rtype: list[UpgradeChannel]
        """
        return self._upgrade_channels

    @upgrade_channels.setter
    def upgrade_channels(self, upgrade_channels):
        """Sets the upgrade_channels of this ReleaseSource.


        :param upgrade_channels: The upgrade_channels of this ReleaseSource.  # noqa: E501
        :type: list[UpgradeChannel]
        """
        if upgrade_channels is None:
            raise ValueError("Invalid value for `upgrade_channels`, must not be `None`")  # noqa: E501

        self._upgrade_channels = upgrade_channels

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
        if issubclass(ReleaseSource, dict):
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
        if not isinstance(other, ReleaseSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
