# coding: utf-8

"""
    Akeyless API

    The purpose of this application is to provide access to Akeyless API.  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: support@akeyless.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from akeyless.configuration import Configuration


class SyslogLogForwardingConfig(object):
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
        'syslog_enable_tls': 'bool',
        'syslog_formatter': 'str',
        'syslog_host': 'str',
        'syslog_network': 'str',
        'syslog_target_tag': 'str',
        'syslog_tls_certificate': 'str'
    }

    attribute_map = {
        'syslog_enable_tls': 'syslog_enable_tls',
        'syslog_formatter': 'syslog_formatter',
        'syslog_host': 'syslog_host',
        'syslog_network': 'syslog_network',
        'syslog_target_tag': 'syslog_target_tag',
        'syslog_tls_certificate': 'syslog_tls_certificate'
    }

    def __init__(self, syslog_enable_tls=None, syslog_formatter=None, syslog_host=None, syslog_network=None, syslog_target_tag=None, syslog_tls_certificate=None, local_vars_configuration=None):  # noqa: E501
        """SyslogLogForwardingConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._syslog_enable_tls = None
        self._syslog_formatter = None
        self._syslog_host = None
        self._syslog_network = None
        self._syslog_target_tag = None
        self._syslog_tls_certificate = None
        self.discriminator = None

        if syslog_enable_tls is not None:
            self.syslog_enable_tls = syslog_enable_tls
        if syslog_formatter is not None:
            self.syslog_formatter = syslog_formatter
        if syslog_host is not None:
            self.syslog_host = syslog_host
        if syslog_network is not None:
            self.syslog_network = syslog_network
        if syslog_target_tag is not None:
            self.syslog_target_tag = syslog_target_tag
        if syslog_tls_certificate is not None:
            self.syslog_tls_certificate = syslog_tls_certificate

    @property
    def syslog_enable_tls(self):
        """Gets the syslog_enable_tls of this SyslogLogForwardingConfig.  # noqa: E501


        :return: The syslog_enable_tls of this SyslogLogForwardingConfig.  # noqa: E501
        :rtype: bool
        """
        return self._syslog_enable_tls

    @syslog_enable_tls.setter
    def syslog_enable_tls(self, syslog_enable_tls):
        """Sets the syslog_enable_tls of this SyslogLogForwardingConfig.


        :param syslog_enable_tls: The syslog_enable_tls of this SyslogLogForwardingConfig.  # noqa: E501
        :type: bool
        """

        self._syslog_enable_tls = syslog_enable_tls

    @property
    def syslog_formatter(self):
        """Gets the syslog_formatter of this SyslogLogForwardingConfig.  # noqa: E501


        :return: The syslog_formatter of this SyslogLogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._syslog_formatter

    @syslog_formatter.setter
    def syslog_formatter(self, syslog_formatter):
        """Sets the syslog_formatter of this SyslogLogForwardingConfig.


        :param syslog_formatter: The syslog_formatter of this SyslogLogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._syslog_formatter = syslog_formatter

    @property
    def syslog_host(self):
        """Gets the syslog_host of this SyslogLogForwardingConfig.  # noqa: E501


        :return: The syslog_host of this SyslogLogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._syslog_host

    @syslog_host.setter
    def syslog_host(self, syslog_host):
        """Sets the syslog_host of this SyslogLogForwardingConfig.


        :param syslog_host: The syslog_host of this SyslogLogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._syslog_host = syslog_host

    @property
    def syslog_network(self):
        """Gets the syslog_network of this SyslogLogForwardingConfig.  # noqa: E501


        :return: The syslog_network of this SyslogLogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._syslog_network

    @syslog_network.setter
    def syslog_network(self, syslog_network):
        """Sets the syslog_network of this SyslogLogForwardingConfig.


        :param syslog_network: The syslog_network of this SyslogLogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._syslog_network = syslog_network

    @property
    def syslog_target_tag(self):
        """Gets the syslog_target_tag of this SyslogLogForwardingConfig.  # noqa: E501


        :return: The syslog_target_tag of this SyslogLogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._syslog_target_tag

    @syslog_target_tag.setter
    def syslog_target_tag(self, syslog_target_tag):
        """Sets the syslog_target_tag of this SyslogLogForwardingConfig.


        :param syslog_target_tag: The syslog_target_tag of this SyslogLogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._syslog_target_tag = syslog_target_tag

    @property
    def syslog_tls_certificate(self):
        """Gets the syslog_tls_certificate of this SyslogLogForwardingConfig.  # noqa: E501


        :return: The syslog_tls_certificate of this SyslogLogForwardingConfig.  # noqa: E501
        :rtype: str
        """
        return self._syslog_tls_certificate

    @syslog_tls_certificate.setter
    def syslog_tls_certificate(self, syslog_tls_certificate):
        """Sets the syslog_tls_certificate of this SyslogLogForwardingConfig.


        :param syslog_tls_certificate: The syslog_tls_certificate of this SyslogLogForwardingConfig.  # noqa: E501
        :type: str
        """

        self._syslog_tls_certificate = syslog_tls_certificate

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
        if not isinstance(other, SyslogLogForwardingConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SyslogLogForwardingConfig):
            return True

        return self.to_dict() != other.to_dict()
