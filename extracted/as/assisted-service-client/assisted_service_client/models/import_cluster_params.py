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


class ImportClusterParams(object):
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
        'name': 'str',
        'api_vip_dnsname': 'str',
        'openshift_version': 'str',
        'openshift_cluster_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'api_vip_dnsname': 'api_vip_dnsname',
        'openshift_version': 'openshift_version',
        'openshift_cluster_id': 'openshift_cluster_id'
    }

    def __init__(self, name=None, api_vip_dnsname=None, openshift_version=None, openshift_cluster_id=None):  # noqa: E501
        """ImportClusterParams - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._api_vip_dnsname = None
        self._openshift_version = None
        self._openshift_cluster_id = None
        self.discriminator = None

        self.name = name
        self.api_vip_dnsname = api_vip_dnsname
        if openshift_version is not None:
            self.openshift_version = openshift_version
        self.openshift_cluster_id = openshift_cluster_id

    @property
    def name(self):
        """Gets the name of this ImportClusterParams.  # noqa: E501

        OpenShift cluster name.  # noqa: E501

        :return: The name of this ImportClusterParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportClusterParams.

        OpenShift cluster name.  # noqa: E501

        :param name: The name of this ImportClusterParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def api_vip_dnsname(self):
        """Gets the api_vip_dnsname of this ImportClusterParams.  # noqa: E501

        The domain name used to reach the OpenShift cluster API.  # noqa: E501

        :return: The api_vip_dnsname of this ImportClusterParams.  # noqa: E501
        :rtype: str
        """
        return self._api_vip_dnsname

    @api_vip_dnsname.setter
    def api_vip_dnsname(self, api_vip_dnsname):
        """Sets the api_vip_dnsname of this ImportClusterParams.

        The domain name used to reach the OpenShift cluster API.  # noqa: E501

        :param api_vip_dnsname: The api_vip_dnsname of this ImportClusterParams.  # noqa: E501
        :type: str
        """
        if api_vip_dnsname is None:
            raise ValueError("Invalid value for `api_vip_dnsname`, must not be `None`")  # noqa: E501

        self._api_vip_dnsname = api_vip_dnsname

    @property
    def openshift_version(self):
        """Gets the openshift_version of this ImportClusterParams.  # noqa: E501

        Version of the OpenShift cluster.  # noqa: E501

        :return: The openshift_version of this ImportClusterParams.  # noqa: E501
        :rtype: str
        """
        return self._openshift_version

    @openshift_version.setter
    def openshift_version(self, openshift_version):
        """Sets the openshift_version of this ImportClusterParams.

        Version of the OpenShift cluster.  # noqa: E501

        :param openshift_version: The openshift_version of this ImportClusterParams.  # noqa: E501
        :type: str
        """

        self._openshift_version = openshift_version

    @property
    def openshift_cluster_id(self):
        """Gets the openshift_cluster_id of this ImportClusterParams.  # noqa: E501

        The id of the OCP cluster, that hosts will be added to  # noqa: E501

        :return: The openshift_cluster_id of this ImportClusterParams.  # noqa: E501
        :rtype: str
        """
        return self._openshift_cluster_id

    @openshift_cluster_id.setter
    def openshift_cluster_id(self, openshift_cluster_id):
        """Sets the openshift_cluster_id of this ImportClusterParams.

        The id of the OCP cluster, that hosts will be added to  # noqa: E501

        :param openshift_cluster_id: The openshift_cluster_id of this ImportClusterParams.  # noqa: E501
        :type: str
        """
        if openshift_cluster_id is None:
            raise ValueError("Invalid value for `openshift_cluster_id`, must not be `None`")  # noqa: E501

        self._openshift_cluster_id = openshift_cluster_id

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
        if issubclass(ImportClusterParams, dict):
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
        if not isinstance(other, ImportClusterParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
