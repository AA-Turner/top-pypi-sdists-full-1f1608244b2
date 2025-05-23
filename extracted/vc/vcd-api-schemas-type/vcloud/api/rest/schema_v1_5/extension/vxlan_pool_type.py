"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .vmw_network_pool_type import VMWNetworkPoolType


class VxlanPoolType(VMWNetworkPoolType):
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
        'vim_switch_ref': 'VimObjectRefType',
        'transport_zone_ref': 'VimObjectRefType',
        'used_networks_count': 'int',
        'promiscuous_mode': 'bool',
        'vds_contexts': 'list[VdsContextType]'
    }

    attribute_map = {
        'vim_switch_ref': 'vimSwitchRef',
        'transport_zone_ref': 'transportZoneRef',
        'used_networks_count': 'usedNetworksCount',
        'promiscuous_mode': 'promiscuousMode',
        'vds_contexts': 'vdsContexts'
    }

    def __init__(self, vim_switch_ref=None,transport_zone_ref=None,used_networks_count=None,promiscuous_mode=None,vds_contexts=None):
        self._vim_switch_ref = None
        self._transport_zone_ref = None
        self._used_networks_count = None
        self._promiscuous_mode = None
        self._vds_contexts = None

        if vim_switch_ref is not None:
            self.vim_switch_ref = vim_switch_ref
        if transport_zone_ref is not None:
            self.transport_zone_ref = transport_zone_ref
        if used_networks_count is not None:
            self.used_networks_count = used_networks_count
        if promiscuous_mode is not None:
            self.promiscuous_mode = promiscuous_mode
        if vds_contexts is not None:
            self.vds_contexts = vds_contexts

    @property
    def vim_switch_ref(self):
        return self._vim_switch_ref
    
    @vim_switch_ref.setter
    def vim_switch_ref(self, vim_switch_ref):
        self._vim_switch_ref = vim_switch_ref

    @property
    def transport_zone_ref(self):
        return self._transport_zone_ref
    
    @transport_zone_ref.setter
    def transport_zone_ref(self, transport_zone_ref):
        self._transport_zone_ref = transport_zone_ref

    @property
    def used_networks_count(self):
        return self._used_networks_count
    
    @used_networks_count.setter
    def used_networks_count(self, used_networks_count):
        self._used_networks_count = used_networks_count

    @property
    def promiscuous_mode(self):
        return self._promiscuous_mode
    
    @promiscuous_mode.setter
    def promiscuous_mode(self, promiscuous_mode):
        self._promiscuous_mode = promiscuous_mode

    @property
    def vds_contexts(self):
        return self._vds_contexts
    
    @vds_contexts.setter
    def vds_contexts(self, vds_contexts):
        self._vds_contexts = vds_contexts


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
        if not isinstance(other, VxlanPoolType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
