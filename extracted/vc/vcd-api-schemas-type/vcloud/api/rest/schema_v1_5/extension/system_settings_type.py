"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from ..resource_type import ResourceType


class SystemSettingsType(ResourceType):
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
        'general_settings': 'GeneralSettingsType',
        'notifications_settings': 'NotificationsSettingsType',
        'ldap_settings': 'LdapSettingsType',
        'amqp_settings': 'AmqpSettingsType',
        'email_settings': 'EmailSettingsType',
        'license': 'LicenseType',
        'branding_settings': 'BrandingSettingsType',
        'blocking_task_settings': 'BlockingTaskSettingsType',
        'password_policy_settings': 'SystemPasswordPolicySettingsType',
        'kerberos_settings': 'KerberosSettingsType',
        'lookup_service_settings': 'LookupServiceSettingsType',
        'catalog_settings': 'CatalogSettingsType',
        'operation_limits_settings': 'OperationLimitsSettingsType',
        'cpom_settings': 'CpomSettingsType'
    }

    attribute_map = {
        'general_settings': 'generalSettings',
        'notifications_settings': 'notificationsSettings',
        'ldap_settings': 'ldapSettings',
        'amqp_settings': 'amqpSettings',
        'email_settings': 'emailSettings',
        'license': 'license',
        'branding_settings': 'brandingSettings',
        'blocking_task_settings': 'blockingTaskSettings',
        'password_policy_settings': 'passwordPolicySettings',
        'kerberos_settings': 'kerberosSettings',
        'lookup_service_settings': 'lookupServiceSettings',
        'catalog_settings': 'catalogSettings',
        'operation_limits_settings': 'operationLimitsSettings',
        'cpom_settings': 'cpomSettings'
    }

    def __init__(self, general_settings=None,notifications_settings=None,ldap_settings=None,amqp_settings=None,email_settings=None,license=None,branding_settings=None,blocking_task_settings=None,password_policy_settings=None,kerberos_settings=None,lookup_service_settings=None,catalog_settings=None,operation_limits_settings=None,cpom_settings=None):
        self._general_settings = None
        self._notifications_settings = None
        self._ldap_settings = None
        self._amqp_settings = None
        self._email_settings = None
        self._license = None
        self._branding_settings = None
        self._blocking_task_settings = None
        self._password_policy_settings = None
        self._kerberos_settings = None
        self._lookup_service_settings = None
        self._catalog_settings = None
        self._operation_limits_settings = None
        self._cpom_settings = None

        if general_settings is not None:
            self.general_settings = general_settings
        if notifications_settings is not None:
            self.notifications_settings = notifications_settings
        if ldap_settings is not None:
            self.ldap_settings = ldap_settings
        if amqp_settings is not None:
            self.amqp_settings = amqp_settings
        if email_settings is not None:
            self.email_settings = email_settings
        if license is not None:
            self.license = license
        if branding_settings is not None:
            self.branding_settings = branding_settings
        if blocking_task_settings is not None:
            self.blocking_task_settings = blocking_task_settings
        if password_policy_settings is not None:
            self.password_policy_settings = password_policy_settings
        if kerberos_settings is not None:
            self.kerberos_settings = kerberos_settings
        if lookup_service_settings is not None:
            self.lookup_service_settings = lookup_service_settings
        if catalog_settings is not None:
            self.catalog_settings = catalog_settings
        if operation_limits_settings is not None:
            self.operation_limits_settings = operation_limits_settings
        if cpom_settings is not None:
            self.cpom_settings = cpom_settings

    @property
    def general_settings(self):
        return self._general_settings
    
    @general_settings.setter
    def general_settings(self, general_settings):
        self._general_settings = general_settings

    @property
    def notifications_settings(self):
        return self._notifications_settings
    
    @notifications_settings.setter
    def notifications_settings(self, notifications_settings):
        self._notifications_settings = notifications_settings

    @property
    def ldap_settings(self):
        return self._ldap_settings
    
    @ldap_settings.setter
    def ldap_settings(self, ldap_settings):
        self._ldap_settings = ldap_settings

    @property
    def amqp_settings(self):
        return self._amqp_settings
    
    @amqp_settings.setter
    def amqp_settings(self, amqp_settings):
        self._amqp_settings = amqp_settings

    @property
    def email_settings(self):
        return self._email_settings
    
    @email_settings.setter
    def email_settings(self, email_settings):
        self._email_settings = email_settings

    @property
    def license(self):
        return self._license
    
    @license.setter
    def license(self, license):
        self._license = license

    @property
    def branding_settings(self):
        return self._branding_settings
    
    @branding_settings.setter
    def branding_settings(self, branding_settings):
        self._branding_settings = branding_settings

    @property
    def blocking_task_settings(self):
        return self._blocking_task_settings
    
    @blocking_task_settings.setter
    def blocking_task_settings(self, blocking_task_settings):
        self._blocking_task_settings = blocking_task_settings

    @property
    def password_policy_settings(self):
        return self._password_policy_settings
    
    @password_policy_settings.setter
    def password_policy_settings(self, password_policy_settings):
        self._password_policy_settings = password_policy_settings

    @property
    def kerberos_settings(self):
        return self._kerberos_settings
    
    @kerberos_settings.setter
    def kerberos_settings(self, kerberos_settings):
        self._kerberos_settings = kerberos_settings

    @property
    def lookup_service_settings(self):
        return self._lookup_service_settings
    
    @lookup_service_settings.setter
    def lookup_service_settings(self, lookup_service_settings):
        self._lookup_service_settings = lookup_service_settings

    @property
    def catalog_settings(self):
        return self._catalog_settings
    
    @catalog_settings.setter
    def catalog_settings(self, catalog_settings):
        self._catalog_settings = catalog_settings

    @property
    def operation_limits_settings(self):
        return self._operation_limits_settings
    
    @operation_limits_settings.setter
    def operation_limits_settings(self, operation_limits_settings):
        self._operation_limits_settings = operation_limits_settings

    @property
    def cpom_settings(self):
        return self._cpom_settings
    
    @cpom_settings.setter
    def cpom_settings(self, cpom_settings):
        self._cpom_settings = cpom_settings


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
        if not isinstance(other, SystemSettingsType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
