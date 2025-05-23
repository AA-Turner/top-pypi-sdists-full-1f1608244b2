# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20170115


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IpMaxConnections(object):
    """
    An object that species the maximum number of connections the listed IPs can make to a listener.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IpMaxConnections object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ip_addresses:
            The value to assign to the ip_addresses property of this IpMaxConnections.
        :type ip_addresses: list[str]

        :param max_connections:
            The value to assign to the max_connections property of this IpMaxConnections.
        :type max_connections: int

        """
        self.swagger_types = {
            'ip_addresses': 'list[str]',
            'max_connections': 'int'
        }
        self.attribute_map = {
            'ip_addresses': 'ipAddresses',
            'max_connections': 'maxConnections'
        }
        self._ip_addresses = None
        self._max_connections = None

    @property
    def ip_addresses(self):
        """
        **[Required]** Gets the ip_addresses of this IpMaxConnections.
        Each element in the list should be valid IPv4 or IPv6 CIDR Block address.
        Example: '[\"129.213.176.0/24\", \"150.136.187.0/24\", \"2002::1234:abcd:ffff:c0a8:101/64\"]'


        :return: The ip_addresses of this IpMaxConnections.
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """
        Sets the ip_addresses of this IpMaxConnections.
        Each element in the list should be valid IPv4 or IPv6 CIDR Block address.
        Example: '[\"129.213.176.0/24\", \"150.136.187.0/24\", \"2002::1234:abcd:ffff:c0a8:101/64\"]'


        :param ip_addresses: The ip_addresses of this IpMaxConnections.
        :type: list[str]
        """
        self._ip_addresses = ip_addresses

    @property
    def max_connections(self):
        """
        **[Required]** Gets the max_connections of this IpMaxConnections.
        The maximum number of simultaneous connections that the specified IPs can make to the
        Listener. IPs without a maxConnections setting can make either defaultMaxConnections
        simultaneous connections to a listener or, if no defaultMaxConnections is specified, an
        unlimited number of simultaneous connections to a listener.


        :return: The max_connections of this IpMaxConnections.
        :rtype: int
        """
        return self._max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        """
        Sets the max_connections of this IpMaxConnections.
        The maximum number of simultaneous connections that the specified IPs can make to the
        Listener. IPs without a maxConnections setting can make either defaultMaxConnections
        simultaneous connections to a listener or, if no defaultMaxConnections is specified, an
        unlimited number of simultaneous connections to a listener.


        :param max_connections: The max_connections of this IpMaxConnections.
        :type: int
        """
        self._max_connections = max_connections

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
