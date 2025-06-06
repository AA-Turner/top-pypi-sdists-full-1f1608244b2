# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VtapCaptureFilterRuleDetails(object):
    """
    This resource contains the rules governing what traffic a VTAP mirrors.
    """

    #: A constant which can be used with the traffic_direction property of a VtapCaptureFilterRuleDetails.
    #: This constant has a value of "INGRESS"
    TRAFFIC_DIRECTION_INGRESS = "INGRESS"

    #: A constant which can be used with the traffic_direction property of a VtapCaptureFilterRuleDetails.
    #: This constant has a value of "EGRESS"
    TRAFFIC_DIRECTION_EGRESS = "EGRESS"

    #: A constant which can be used with the rule_action property of a VtapCaptureFilterRuleDetails.
    #: This constant has a value of "INCLUDE"
    RULE_ACTION_INCLUDE = "INCLUDE"

    #: A constant which can be used with the rule_action property of a VtapCaptureFilterRuleDetails.
    #: This constant has a value of "EXCLUDE"
    RULE_ACTION_EXCLUDE = "EXCLUDE"

    def __init__(self, **kwargs):
        """
        Initializes a new VtapCaptureFilterRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param traffic_direction:
            The value to assign to the traffic_direction property of this VtapCaptureFilterRuleDetails.
            Allowed values for this property are: "INGRESS", "EGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type traffic_direction: str

        :param rule_action:
            The value to assign to the rule_action property of this VtapCaptureFilterRuleDetails.
            Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type rule_action: str

        :param source_cidr:
            The value to assign to the source_cidr property of this VtapCaptureFilterRuleDetails.
        :type source_cidr: str

        :param destination_cidr:
            The value to assign to the destination_cidr property of this VtapCaptureFilterRuleDetails.
        :type destination_cidr: str

        :param protocol:
            The value to assign to the protocol property of this VtapCaptureFilterRuleDetails.
        :type protocol: str

        :param icmp_options:
            The value to assign to the icmp_options property of this VtapCaptureFilterRuleDetails.
        :type icmp_options: oci.core.models.IcmpOptions

        :param tcp_options:
            The value to assign to the tcp_options property of this VtapCaptureFilterRuleDetails.
        :type tcp_options: oci.core.models.TcpOptions

        :param udp_options:
            The value to assign to the udp_options property of this VtapCaptureFilterRuleDetails.
        :type udp_options: oci.core.models.UdpOptions

        """
        self.swagger_types = {
            'traffic_direction': 'str',
            'rule_action': 'str',
            'source_cidr': 'str',
            'destination_cidr': 'str',
            'protocol': 'str',
            'icmp_options': 'IcmpOptions',
            'tcp_options': 'TcpOptions',
            'udp_options': 'UdpOptions'
        }
        self.attribute_map = {
            'traffic_direction': 'trafficDirection',
            'rule_action': 'ruleAction',
            'source_cidr': 'sourceCidr',
            'destination_cidr': 'destinationCidr',
            'protocol': 'protocol',
            'icmp_options': 'icmpOptions',
            'tcp_options': 'tcpOptions',
            'udp_options': 'udpOptions'
        }
        self._traffic_direction = None
        self._rule_action = None
        self._source_cidr = None
        self._destination_cidr = None
        self._protocol = None
        self._icmp_options = None
        self._tcp_options = None
        self._udp_options = None

    @property
    def traffic_direction(self):
        """
        **[Required]** Gets the traffic_direction of this VtapCaptureFilterRuleDetails.
        The traffic direction the VTAP is configured to mirror.

        Allowed values for this property are: "INGRESS", "EGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The traffic_direction of this VtapCaptureFilterRuleDetails.
        :rtype: str
        """
        return self._traffic_direction

    @traffic_direction.setter
    def traffic_direction(self, traffic_direction):
        """
        Sets the traffic_direction of this VtapCaptureFilterRuleDetails.
        The traffic direction the VTAP is configured to mirror.


        :param traffic_direction: The traffic_direction of this VtapCaptureFilterRuleDetails.
        :type: str
        """
        allowed_values = ["INGRESS", "EGRESS"]
        if not value_allowed_none_or_none_sentinel(traffic_direction, allowed_values):
            traffic_direction = 'UNKNOWN_ENUM_VALUE'
        self._traffic_direction = traffic_direction

    @property
    def rule_action(self):
        """
        Gets the rule_action of this VtapCaptureFilterRuleDetails.
        Include or exclude packets meeting this definition from mirrored traffic.

        Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The rule_action of this VtapCaptureFilterRuleDetails.
        :rtype: str
        """
        return self._rule_action

    @rule_action.setter
    def rule_action(self, rule_action):
        """
        Sets the rule_action of this VtapCaptureFilterRuleDetails.
        Include or exclude packets meeting this definition from mirrored traffic.


        :param rule_action: The rule_action of this VtapCaptureFilterRuleDetails.
        :type: str
        """
        allowed_values = ["INCLUDE", "EXCLUDE"]
        if not value_allowed_none_or_none_sentinel(rule_action, allowed_values):
            rule_action = 'UNKNOWN_ENUM_VALUE'
        self._rule_action = rule_action

    @property
    def source_cidr(self):
        """
        Gets the source_cidr of this VtapCaptureFilterRuleDetails.
        Traffic from this CIDR block to the VTAP source will be mirrored to the VTAP target.


        :return: The source_cidr of this VtapCaptureFilterRuleDetails.
        :rtype: str
        """
        return self._source_cidr

    @source_cidr.setter
    def source_cidr(self, source_cidr):
        """
        Sets the source_cidr of this VtapCaptureFilterRuleDetails.
        Traffic from this CIDR block to the VTAP source will be mirrored to the VTAP target.


        :param source_cidr: The source_cidr of this VtapCaptureFilterRuleDetails.
        :type: str
        """
        self._source_cidr = source_cidr

    @property
    def destination_cidr(self):
        """
        Gets the destination_cidr of this VtapCaptureFilterRuleDetails.
        Traffic sent to this CIDR block through the VTAP source will be mirrored to the VTAP target.


        :return: The destination_cidr of this VtapCaptureFilterRuleDetails.
        :rtype: str
        """
        return self._destination_cidr

    @destination_cidr.setter
    def destination_cidr(self, destination_cidr):
        """
        Sets the destination_cidr of this VtapCaptureFilterRuleDetails.
        Traffic sent to this CIDR block through the VTAP source will be mirrored to the VTAP target.


        :param destination_cidr: The destination_cidr of this VtapCaptureFilterRuleDetails.
        :type: str
        """
        self._destination_cidr = destination_cidr

    @property
    def protocol(self):
        """
        Gets the protocol of this VtapCaptureFilterRuleDetails.
        The transport protocol used in the filter. If do not choose a protocol, all protocols will be used in the filter.
        Supported options are:
          * 1 = ICMP
          * 6 = TCP
          * 17 = UDP


        :return: The protocol of this VtapCaptureFilterRuleDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this VtapCaptureFilterRuleDetails.
        The transport protocol used in the filter. If do not choose a protocol, all protocols will be used in the filter.
        Supported options are:
          * 1 = ICMP
          * 6 = TCP
          * 17 = UDP


        :param protocol: The protocol of this VtapCaptureFilterRuleDetails.
        :type: str
        """
        self._protocol = protocol

    @property
    def icmp_options(self):
        """
        Gets the icmp_options of this VtapCaptureFilterRuleDetails.

        :return: The icmp_options of this VtapCaptureFilterRuleDetails.
        :rtype: oci.core.models.IcmpOptions
        """
        return self._icmp_options

    @icmp_options.setter
    def icmp_options(self, icmp_options):
        """
        Sets the icmp_options of this VtapCaptureFilterRuleDetails.

        :param icmp_options: The icmp_options of this VtapCaptureFilterRuleDetails.
        :type: oci.core.models.IcmpOptions
        """
        self._icmp_options = icmp_options

    @property
    def tcp_options(self):
        """
        Gets the tcp_options of this VtapCaptureFilterRuleDetails.

        :return: The tcp_options of this VtapCaptureFilterRuleDetails.
        :rtype: oci.core.models.TcpOptions
        """
        return self._tcp_options

    @tcp_options.setter
    def tcp_options(self, tcp_options):
        """
        Sets the tcp_options of this VtapCaptureFilterRuleDetails.

        :param tcp_options: The tcp_options of this VtapCaptureFilterRuleDetails.
        :type: oci.core.models.TcpOptions
        """
        self._tcp_options = tcp_options

    @property
    def udp_options(self):
        """
        Gets the udp_options of this VtapCaptureFilterRuleDetails.

        :return: The udp_options of this VtapCaptureFilterRuleDetails.
        :rtype: oci.core.models.UdpOptions
        """
        return self._udp_options

    @udp_options.setter
    def udp_options(self, udp_options):
        """
        Sets the udp_options of this VtapCaptureFilterRuleDetails.

        :param udp_options: The udp_options of this VtapCaptureFilterRuleDetails.
        :type: oci.core.models.UdpOptions
        """
        self._udp_options = udp_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
