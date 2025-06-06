"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .resource_type import ResourceType


class OrgOperationLimitsSettingsType(ResourceType):
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
        'consoles_per_vm_limit': 'int',
        'operations_per_user': 'int',
        'operations_per_org': 'int',
        'queued_operations_per_user': 'int',
        'queued_operations_per_org': 'int'
    }

    attribute_map = {
        'consoles_per_vm_limit': 'consolesPerVmLimit',
        'operations_per_user': 'operationsPerUser',
        'operations_per_org': 'operationsPerOrg',
        'queued_operations_per_user': 'queuedOperationsPerUser',
        'queued_operations_per_org': 'queuedOperationsPerOrg'
    }

    def __init__(self, consoles_per_vm_limit=None,operations_per_user=None,operations_per_org=None,queued_operations_per_user=None,queued_operations_per_org=None):
        self._consoles_per_vm_limit = None
        self._operations_per_user = None
        self._operations_per_org = None
        self._queued_operations_per_user = None
        self._queued_operations_per_org = None

        if consoles_per_vm_limit is not None:
            self.consoles_per_vm_limit = consoles_per_vm_limit
        if operations_per_user is not None:
            self.operations_per_user = operations_per_user
        if operations_per_org is not None:
            self.operations_per_org = operations_per_org
        if queued_operations_per_user is not None:
            self.queued_operations_per_user = queued_operations_per_user
        if queued_operations_per_org is not None:
            self.queued_operations_per_org = queued_operations_per_org

    @property
    def consoles_per_vm_limit(self):
        return self._consoles_per_vm_limit
    
    @consoles_per_vm_limit.setter
    def consoles_per_vm_limit(self, consoles_per_vm_limit):
        self._consoles_per_vm_limit = consoles_per_vm_limit

    @property
    def operations_per_user(self):
        return self._operations_per_user
    
    @operations_per_user.setter
    def operations_per_user(self, operations_per_user):
        self._operations_per_user = operations_per_user

    @property
    def operations_per_org(self):
        return self._operations_per_org
    
    @operations_per_org.setter
    def operations_per_org(self, operations_per_org):
        self._operations_per_org = operations_per_org

    @property
    def queued_operations_per_user(self):
        return self._queued_operations_per_user
    
    @queued_operations_per_user.setter
    def queued_operations_per_user(self, queued_operations_per_user):
        self._queued_operations_per_user = queued_operations_per_user

    @property
    def queued_operations_per_org(self):
        return self._queued_operations_per_org
    
    @queued_operations_per_org.setter
    def queued_operations_per_org(self, queued_operations_per_org):
        self._queued_operations_per_org = queued_operations_per_org


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
        if not isinstance(other, OrgOperationLimitsSettingsType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
