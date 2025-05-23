"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .resource_type import ResourceType


class OrgLdapSettingsType(ResourceType):
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
        'org_ldap_mode': 'str',
        'custom_users_ou': 'str',
        'custom_org_ldap_settings': 'CustomOrgLdapSettingsType'
    }

    attribute_map = {
        'org_ldap_mode': 'orgLdapMode',
        'custom_users_ou': 'customUsersOu',
        'custom_org_ldap_settings': 'customOrgLdapSettings'
    }

    def __init__(self, org_ldap_mode=None,custom_users_ou=None,custom_org_ldap_settings=None):
        self._org_ldap_mode = None
        self._custom_users_ou = None
        self._custom_org_ldap_settings = None

        if org_ldap_mode is not None:
            self.org_ldap_mode = org_ldap_mode
        if custom_users_ou is not None:
            self.custom_users_ou = custom_users_ou
        if custom_org_ldap_settings is not None:
            self.custom_org_ldap_settings = custom_org_ldap_settings

    @property
    def org_ldap_mode(self):
        return self._org_ldap_mode
    
    @org_ldap_mode.setter
    def org_ldap_mode(self, org_ldap_mode):
        self._org_ldap_mode = org_ldap_mode

    @property
    def custom_users_ou(self):
        return self._custom_users_ou
    
    @custom_users_ou.setter
    def custom_users_ou(self, custom_users_ou):
        self._custom_users_ou = custom_users_ou

    @property
    def custom_org_ldap_settings(self):
        return self._custom_org_ldap_settings
    
    @custom_org_ldap_settings.setter
    def custom_org_ldap_settings(self, custom_org_ldap_settings):
        self._custom_org_ldap_settings = custom_org_ldap_settings


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
        if not isinstance(other, OrgLdapSettingsType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
