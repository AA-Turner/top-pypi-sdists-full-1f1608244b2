# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Endpoint(object):
    """
    Information about the database instance node endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Endpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param fqdn:
            The value to assign to the fqdn property of this Endpoint.
        :type fqdn: str

        :param ip_address:
            The value to assign to the ip_address property of this Endpoint.
        :type ip_address: str

        :param port:
            The value to assign to the port property of this Endpoint.
        :type port: int

        """
        self.swagger_types = {
            'fqdn': 'str',
            'ip_address': 'str',
            'port': 'int'
        }
        self.attribute_map = {
            'fqdn': 'fqdn',
            'ip_address': 'ipAddress',
            'port': 'port'
        }
        self._fqdn = None
        self._ip_address = None
        self._port = None

    @property
    def fqdn(self):
        """
        **[Required]** Gets the fqdn of this Endpoint.
        The FQDN of the endpoint.


        :return: The fqdn of this Endpoint.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this Endpoint.
        The FQDN of the endpoint.


        :param fqdn: The fqdn of this Endpoint.
        :type: str
        """
        self._fqdn = fqdn

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Endpoint.
        The IP address of the endpoint.


        :return: The ip_address of this Endpoint.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Endpoint.
        The IP address of the endpoint.


        :param ip_address: The ip_address of this Endpoint.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def port(self):
        """
        **[Required]** Gets the port of this Endpoint.
        The port address of the endpoint.


        :return: The port of this Endpoint.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this Endpoint.
        The port address of the endpoint.


        :param port: The port of this Endpoint.
        :type: int
        """
        self._port = port

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
