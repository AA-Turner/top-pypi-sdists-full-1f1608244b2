"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .query_result_record_type import QueryResultRecordType


class QueryResultOrgRecordType(QueryResultRecordType):
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
        'name': 'str',
        'is_read_only': 'bool',
        'is_enabled': 'bool',
        'deployed_vm_quota': 'int',
        'stored_vm_quota': 'int',
        'display_name': 'str',
        'can_publish_catalogs': 'bool',
        'number_of_catalogs': 'int',
        'number_of_vdcs': 'int',
        'number_of_v_apps': 'int',
        'number_of_groups': 'int',
        'number_of_disks': 'int',
        'can_publish_externally': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'is_read_only': 'isReadOnly',
        'is_enabled': 'isEnabled',
        'deployed_vm_quota': 'deployedVMQuota',
        'stored_vm_quota': 'storedVMQuota',
        'display_name': 'displayName',
        'can_publish_catalogs': 'canPublishCatalogs',
        'number_of_catalogs': 'numberOfCatalogs',
        'number_of_vdcs': 'numberOfVdcs',
        'number_of_v_apps': 'numberOfVApps',
        'number_of_groups': 'numberOfGroups',
        'number_of_disks': 'numberOfDisks',
        'can_publish_externally': 'canPublishExternally'
    }

    def __init__(self, name=None,is_read_only=None,is_enabled=None,deployed_vm_quota=None,stored_vm_quota=None,display_name=None,can_publish_catalogs=None,number_of_catalogs=None,number_of_vdcs=None,number_of_v_apps=None,number_of_groups=None,number_of_disks=None,can_publish_externally=None):
        self._name = None
        self._is_read_only = None
        self._is_enabled = None
        self._deployed_vm_quota = None
        self._stored_vm_quota = None
        self._display_name = None
        self._can_publish_catalogs = None
        self._number_of_catalogs = None
        self._number_of_vdcs = None
        self._number_of_v_apps = None
        self._number_of_groups = None
        self._number_of_disks = None
        self._can_publish_externally = None

        if name is not None:
            self.name = name
        if is_read_only is not None:
            self.is_read_only = is_read_only
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if deployed_vm_quota is not None:
            self.deployed_vm_quota = deployed_vm_quota
        if stored_vm_quota is not None:
            self.stored_vm_quota = stored_vm_quota
        if display_name is not None:
            self.display_name = display_name
        if can_publish_catalogs is not None:
            self.can_publish_catalogs = can_publish_catalogs
        if number_of_catalogs is not None:
            self.number_of_catalogs = number_of_catalogs
        if number_of_vdcs is not None:
            self.number_of_vdcs = number_of_vdcs
        if number_of_v_apps is not None:
            self.number_of_v_apps = number_of_v_apps
        if number_of_groups is not None:
            self.number_of_groups = number_of_groups
        if number_of_disks is not None:
            self.number_of_disks = number_of_disks
        if can_publish_externally is not None:
            self.can_publish_externally = can_publish_externally

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def is_read_only(self):
        return self._is_read_only
    
    @is_read_only.setter
    def is_read_only(self, is_read_only):
        self._is_read_only = is_read_only

    @property
    def is_enabled(self):
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self, is_enabled):
        self._is_enabled = is_enabled

    @property
    def deployed_vm_quota(self):
        return self._deployed_vm_quota
    
    @deployed_vm_quota.setter
    def deployed_vm_quota(self, deployed_vm_quota):
        self._deployed_vm_quota = deployed_vm_quota

    @property
    def stored_vm_quota(self):
        return self._stored_vm_quota
    
    @stored_vm_quota.setter
    def stored_vm_quota(self, stored_vm_quota):
        self._stored_vm_quota = stored_vm_quota

    @property
    def display_name(self):
        return self._display_name
    
    @display_name.setter
    def display_name(self, display_name):
        self._display_name = display_name

    @property
    def can_publish_catalogs(self):
        return self._can_publish_catalogs
    
    @can_publish_catalogs.setter
    def can_publish_catalogs(self, can_publish_catalogs):
        self._can_publish_catalogs = can_publish_catalogs

    @property
    def number_of_catalogs(self):
        return self._number_of_catalogs
    
    @number_of_catalogs.setter
    def number_of_catalogs(self, number_of_catalogs):
        self._number_of_catalogs = number_of_catalogs

    @property
    def number_of_vdcs(self):
        return self._number_of_vdcs
    
    @number_of_vdcs.setter
    def number_of_vdcs(self, number_of_vdcs):
        self._number_of_vdcs = number_of_vdcs

    @property
    def number_of_v_apps(self):
        return self._number_of_v_apps
    
    @number_of_v_apps.setter
    def number_of_v_apps(self, number_of_v_apps):
        self._number_of_v_apps = number_of_v_apps

    @property
    def number_of_groups(self):
        return self._number_of_groups
    
    @number_of_groups.setter
    def number_of_groups(self, number_of_groups):
        self._number_of_groups = number_of_groups

    @property
    def number_of_disks(self):
        return self._number_of_disks
    
    @number_of_disks.setter
    def number_of_disks(self, number_of_disks):
        self._number_of_disks = number_of_disks

    @property
    def can_publish_externally(self):
        return self._can_publish_externally
    
    @can_publish_externally.setter
    def can_publish_externally(self, can_publish_externally):
        self._can_publish_externally = can_publish_externally


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
        if not isinstance(other, QueryResultOrgRecordType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
