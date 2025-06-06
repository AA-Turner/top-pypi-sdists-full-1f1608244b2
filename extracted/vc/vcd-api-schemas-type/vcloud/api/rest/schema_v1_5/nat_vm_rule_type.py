"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .v_cloud_extensible_type import VCloudExtensibleType


class NatVmRuleType(VCloudExtensibleType):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'external_ip_address': 'str',
        'external_port': 'int',
        'v_app_scoped_vm_id': 'str',
        'vm_nic_id': 'int',
        'internal_port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'external_ip_address': 'externalIpAddress',
        'external_port': 'externalPort',
        'v_app_scoped_vm_id': 'vAppScopedVmId',
        'vm_nic_id': 'vmNicId',
        'internal_port': 'internalPort',
        'protocol': 'protocol'
    }

    def __init__(self, external_ip_address=None,external_port=None,v_app_scoped_vm_id=None,vm_nic_id=None,internal_port=None,protocol=None):
        self._external_ip_address = None
        self._external_port = None
        self._v_app_scoped_vm_id = None
        self._vm_nic_id = None
        self._internal_port = None
        self._protocol = None

        if external_ip_address is not None:
            self.external_ip_address = external_ip_address
        if external_port is not None:
            self.external_port = external_port
        if v_app_scoped_vm_id is not None:
            self.v_app_scoped_vm_id = v_app_scoped_vm_id
        if vm_nic_id is not None:
            self.vm_nic_id = vm_nic_id
        if internal_port is not None:
            self.internal_port = internal_port
        if protocol is not None:
            self.protocol = protocol

    @property
    def external_ip_address(self):
        return self._external_ip_address
    
    @external_ip_address.setter
    def external_ip_address(self, external_ip_address):
        self._external_ip_address = external_ip_address

    @property
    def external_port(self):
        return self._external_port
    
    @external_port.setter
    def external_port(self, external_port):
        self._external_port = external_port

    @property
    def v_app_scoped_vm_id(self):
        return self._v_app_scoped_vm_id
    
    @v_app_scoped_vm_id.setter
    def v_app_scoped_vm_id(self, v_app_scoped_vm_id):
        self._v_app_scoped_vm_id = v_app_scoped_vm_id

    @property
    def vm_nic_id(self):
        return self._vm_nic_id
    
    @vm_nic_id.setter
    def vm_nic_id(self, vm_nic_id):
        self._vm_nic_id = vm_nic_id

    @property
    def internal_port(self):
        return self._internal_port
    
    @internal_port.setter
    def internal_port(self, internal_port):
        self._internal_port = internal_port

    @property
    def protocol(self):
        return self._protocol
    
    @protocol.setter
    def protocol(self, protocol):
        self._protocol = protocol


    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        return pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NatVmRuleType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
