# coding: utf-8

"""
    clb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateLoadBalancerRequest(object):
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
        'address_ip_version': 'str',
        'allowed_ports': 'list[str]',
        'bypass_security_group_enabled': 'str',
        'client_token': 'str',
        'description': 'str',
        'eip_billing_config': 'EipBillingConfigForCreateLoadBalancerInput',
        'eni_address': 'str',
        'eni_address_num': 'int',
        'eni_ipv6_address': 'str',
        'load_balancer_billing_type': 'int',
        'load_balancer_name': 'str',
        'load_balancer_spec': 'str',
        'master_zone_id': 'str',
        'modification_protection_reason': 'str',
        'modification_protection_status': 'str',
        'period': 'int',
        'period_unit': 'str',
        'project_name': 'str',
        'region_id': 'str',
        'slave_zone_id': 'str',
        'subnet_id': 'str',
        'tags': 'list[TagForCreateLoadBalancerInput]',
        'type': 'str',
        'vpc_id': 'str',
        'zone_type': 'str'
    }

    attribute_map = {
        'address_ip_version': 'AddressIpVersion',
        'allowed_ports': 'AllowedPorts',
        'bypass_security_group_enabled': 'BypassSecurityGroupEnabled',
        'client_token': 'ClientToken',
        'description': 'Description',
        'eip_billing_config': 'EipBillingConfig',
        'eni_address': 'EniAddress',
        'eni_address_num': 'EniAddressNum',
        'eni_ipv6_address': 'EniIpv6Address',
        'load_balancer_billing_type': 'LoadBalancerBillingType',
        'load_balancer_name': 'LoadBalancerName',
        'load_balancer_spec': 'LoadBalancerSpec',
        'master_zone_id': 'MasterZoneId',
        'modification_protection_reason': 'ModificationProtectionReason',
        'modification_protection_status': 'ModificationProtectionStatus',
        'period': 'Period',
        'period_unit': 'PeriodUnit',
        'project_name': 'ProjectName',
        'region_id': 'RegionId',
        'slave_zone_id': 'SlaveZoneId',
        'subnet_id': 'SubnetId',
        'tags': 'Tags',
        'type': 'Type',
        'vpc_id': 'VpcId',
        'zone_type': 'ZoneType'
    }

    def __init__(self, address_ip_version=None, allowed_ports=None, bypass_security_group_enabled=None, client_token=None, description=None, eip_billing_config=None, eni_address=None, eni_address_num=None, eni_ipv6_address=None, load_balancer_billing_type=None, load_balancer_name=None, load_balancer_spec=None, master_zone_id=None, modification_protection_reason=None, modification_protection_status=None, period=None, period_unit=None, project_name=None, region_id=None, slave_zone_id=None, subnet_id=None, tags=None, type=None, vpc_id=None, zone_type=None, _configuration=None):  # noqa: E501
        """CreateLoadBalancerRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address_ip_version = None
        self._allowed_ports = None
        self._bypass_security_group_enabled = None
        self._client_token = None
        self._description = None
        self._eip_billing_config = None
        self._eni_address = None
        self._eni_address_num = None
        self._eni_ipv6_address = None
        self._load_balancer_billing_type = None
        self._load_balancer_name = None
        self._load_balancer_spec = None
        self._master_zone_id = None
        self._modification_protection_reason = None
        self._modification_protection_status = None
        self._period = None
        self._period_unit = None
        self._project_name = None
        self._region_id = None
        self._slave_zone_id = None
        self._subnet_id = None
        self._tags = None
        self._type = None
        self._vpc_id = None
        self._zone_type = None
        self.discriminator = None

        if address_ip_version is not None:
            self.address_ip_version = address_ip_version
        if allowed_ports is not None:
            self.allowed_ports = allowed_ports
        if bypass_security_group_enabled is not None:
            self.bypass_security_group_enabled = bypass_security_group_enabled
        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        if eip_billing_config is not None:
            self.eip_billing_config = eip_billing_config
        if eni_address is not None:
            self.eni_address = eni_address
        if eni_address_num is not None:
            self.eni_address_num = eni_address_num
        if eni_ipv6_address is not None:
            self.eni_ipv6_address = eni_ipv6_address
        if load_balancer_billing_type is not None:
            self.load_balancer_billing_type = load_balancer_billing_type
        if load_balancer_name is not None:
            self.load_balancer_name = load_balancer_name
        if load_balancer_spec is not None:
            self.load_balancer_spec = load_balancer_spec
        if master_zone_id is not None:
            self.master_zone_id = master_zone_id
        if modification_protection_reason is not None:
            self.modification_protection_reason = modification_protection_reason
        if modification_protection_status is not None:
            self.modification_protection_status = modification_protection_status
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit
        if project_name is not None:
            self.project_name = project_name
        self.region_id = region_id
        if slave_zone_id is not None:
            self.slave_zone_id = slave_zone_id
        self.subnet_id = subnet_id
        if tags is not None:
            self.tags = tags
        self.type = type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if zone_type is not None:
            self.zone_type = zone_type

    @property
    def address_ip_version(self):
        """Gets the address_ip_version of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The address_ip_version of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._address_ip_version

    @address_ip_version.setter
    def address_ip_version(self, address_ip_version):
        """Sets the address_ip_version of this CreateLoadBalancerRequest.


        :param address_ip_version: The address_ip_version of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._address_ip_version = address_ip_version

    @property
    def allowed_ports(self):
        """Gets the allowed_ports of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The allowed_ports of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_ports

    @allowed_ports.setter
    def allowed_ports(self, allowed_ports):
        """Sets the allowed_ports of this CreateLoadBalancerRequest.


        :param allowed_ports: The allowed_ports of this CreateLoadBalancerRequest.  # noqa: E501
        :type: list[str]
        """

        self._allowed_ports = allowed_ports

    @property
    def bypass_security_group_enabled(self):
        """Gets the bypass_security_group_enabled of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The bypass_security_group_enabled of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._bypass_security_group_enabled

    @bypass_security_group_enabled.setter
    def bypass_security_group_enabled(self, bypass_security_group_enabled):
        """Sets the bypass_security_group_enabled of this CreateLoadBalancerRequest.


        :param bypass_security_group_enabled: The bypass_security_group_enabled of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._bypass_security_group_enabled = bypass_security_group_enabled

    @property
    def client_token(self):
        """Gets the client_token of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The client_token of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateLoadBalancerRequest.


        :param client_token: The client_token of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The description of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateLoadBalancerRequest.


        :param description: The description of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def eip_billing_config(self):
        """Gets the eip_billing_config of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The eip_billing_config of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: EipBillingConfigForCreateLoadBalancerInput
        """
        return self._eip_billing_config

    @eip_billing_config.setter
    def eip_billing_config(self, eip_billing_config):
        """Sets the eip_billing_config of this CreateLoadBalancerRequest.


        :param eip_billing_config: The eip_billing_config of this CreateLoadBalancerRequest.  # noqa: E501
        :type: EipBillingConfigForCreateLoadBalancerInput
        """

        self._eip_billing_config = eip_billing_config

    @property
    def eni_address(self):
        """Gets the eni_address of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The eni_address of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._eni_address

    @eni_address.setter
    def eni_address(self, eni_address):
        """Sets the eni_address of this CreateLoadBalancerRequest.


        :param eni_address: The eni_address of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._eni_address = eni_address

    @property
    def eni_address_num(self):
        """Gets the eni_address_num of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The eni_address_num of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: int
        """
        return self._eni_address_num

    @eni_address_num.setter
    def eni_address_num(self, eni_address_num):
        """Sets the eni_address_num of this CreateLoadBalancerRequest.


        :param eni_address_num: The eni_address_num of this CreateLoadBalancerRequest.  # noqa: E501
        :type: int
        """

        self._eni_address_num = eni_address_num

    @property
    def eni_ipv6_address(self):
        """Gets the eni_ipv6_address of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The eni_ipv6_address of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._eni_ipv6_address

    @eni_ipv6_address.setter
    def eni_ipv6_address(self, eni_ipv6_address):
        """Sets the eni_ipv6_address of this CreateLoadBalancerRequest.


        :param eni_ipv6_address: The eni_ipv6_address of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._eni_ipv6_address = eni_ipv6_address

    @property
    def load_balancer_billing_type(self):
        """Gets the load_balancer_billing_type of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The load_balancer_billing_type of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: int
        """
        return self._load_balancer_billing_type

    @load_balancer_billing_type.setter
    def load_balancer_billing_type(self, load_balancer_billing_type):
        """Sets the load_balancer_billing_type of this CreateLoadBalancerRequest.


        :param load_balancer_billing_type: The load_balancer_billing_type of this CreateLoadBalancerRequest.  # noqa: E501
        :type: int
        """

        self._load_balancer_billing_type = load_balancer_billing_type

    @property
    def load_balancer_name(self):
        """Gets the load_balancer_name of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The load_balancer_name of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_name

    @load_balancer_name.setter
    def load_balancer_name(self, load_balancer_name):
        """Sets the load_balancer_name of this CreateLoadBalancerRequest.


        :param load_balancer_name: The load_balancer_name of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._load_balancer_name = load_balancer_name

    @property
    def load_balancer_spec(self):
        """Gets the load_balancer_spec of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The load_balancer_spec of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_spec

    @load_balancer_spec.setter
    def load_balancer_spec(self, load_balancer_spec):
        """Sets the load_balancer_spec of this CreateLoadBalancerRequest.


        :param load_balancer_spec: The load_balancer_spec of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._load_balancer_spec = load_balancer_spec

    @property
    def master_zone_id(self):
        """Gets the master_zone_id of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The master_zone_id of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._master_zone_id

    @master_zone_id.setter
    def master_zone_id(self, master_zone_id):
        """Sets the master_zone_id of this CreateLoadBalancerRequest.


        :param master_zone_id: The master_zone_id of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._master_zone_id = master_zone_id

    @property
    def modification_protection_reason(self):
        """Gets the modification_protection_reason of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The modification_protection_reason of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._modification_protection_reason

    @modification_protection_reason.setter
    def modification_protection_reason(self, modification_protection_reason):
        """Sets the modification_protection_reason of this CreateLoadBalancerRequest.


        :param modification_protection_reason: The modification_protection_reason of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._modification_protection_reason = modification_protection_reason

    @property
    def modification_protection_status(self):
        """Gets the modification_protection_status of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The modification_protection_status of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._modification_protection_status

    @modification_protection_status.setter
    def modification_protection_status(self, modification_protection_status):
        """Sets the modification_protection_status of this CreateLoadBalancerRequest.


        :param modification_protection_status: The modification_protection_status of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._modification_protection_status = modification_protection_status

    @property
    def period(self):
        """Gets the period of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The period of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CreateLoadBalancerRequest.


        :param period: The period of this CreateLoadBalancerRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The period_unit of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this CreateLoadBalancerRequest.


        :param period_unit: The period_unit of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._period_unit = period_unit

    @property
    def project_name(self):
        """Gets the project_name of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The project_name of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CreateLoadBalancerRequest.


        :param project_name: The project_name of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The region_id of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateLoadBalancerRequest.


        :param region_id: The region_id of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

    @property
    def slave_zone_id(self):
        """Gets the slave_zone_id of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The slave_zone_id of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._slave_zone_id

    @slave_zone_id.setter
    def slave_zone_id(self, slave_zone_id):
        """Sets the slave_zone_id of this CreateLoadBalancerRequest.


        :param slave_zone_id: The slave_zone_id of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._slave_zone_id = slave_zone_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The subnet_id of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateLoadBalancerRequest.


        :param subnet_id: The subnet_id of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and subnet_id is None:
            raise ValueError("Invalid value for `subnet_id`, must not be `None`")  # noqa: E501

        self._subnet_id = subnet_id

    @property
    def tags(self):
        """Gets the tags of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The tags of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: list[TagForCreateLoadBalancerInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateLoadBalancerRequest.


        :param tags: The tags of this CreateLoadBalancerRequest.  # noqa: E501
        :type: list[TagForCreateLoadBalancerInput]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The type of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateLoadBalancerRequest.


        :param type: The type of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The vpc_id of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateLoadBalancerRequest.


        :param vpc_id: The vpc_id of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def zone_type(self):
        """Gets the zone_type of this CreateLoadBalancerRequest.  # noqa: E501


        :return: The zone_type of this CreateLoadBalancerRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        """Sets the zone_type of this CreateLoadBalancerRequest.


        :param zone_type: The zone_type of this CreateLoadBalancerRequest.  # noqa: E501
        :type: str
        """

        self._zone_type = zone_type

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
        if issubclass(CreateLoadBalancerRequest, dict):
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
        if not isinstance(other, CreateLoadBalancerRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateLoadBalancerRequest):
            return True

        return self.to_dict() != other.to_dict()
