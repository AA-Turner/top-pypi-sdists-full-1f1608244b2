"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from ..resource_type import ResourceType


class EmailSettingsType(ResourceType):
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
        'sender_email_address': 'str',
        'email_subject_prefix': 'str',
        'alert_email_to_all_admins': 'bool',
        'alert_email_to': 'str',
        'smtp_settings': 'SmtpSettingsType'
    }

    attribute_map = {
        'sender_email_address': 'senderEmailAddress',
        'email_subject_prefix': 'emailSubjectPrefix',
        'alert_email_to_all_admins': 'alertEmailToAllAdmins',
        'alert_email_to': 'alertEmailTo',
        'smtp_settings': 'smtpSettings'
    }

    def __init__(self, sender_email_address=None,email_subject_prefix=None,alert_email_to_all_admins=None,alert_email_to=None,smtp_settings=None):
        self._sender_email_address = None
        self._email_subject_prefix = None
        self._alert_email_to_all_admins = None
        self._alert_email_to = None
        self._smtp_settings = None

        if sender_email_address is not None:
            self.sender_email_address = sender_email_address
        if email_subject_prefix is not None:
            self.email_subject_prefix = email_subject_prefix
        if alert_email_to_all_admins is not None:
            self.alert_email_to_all_admins = alert_email_to_all_admins
        if alert_email_to is not None:
            self.alert_email_to = alert_email_to
        if smtp_settings is not None:
            self.smtp_settings = smtp_settings

    @property
    def sender_email_address(self):
        return self._sender_email_address
    
    @sender_email_address.setter
    def sender_email_address(self, sender_email_address):
        self._sender_email_address = sender_email_address

    @property
    def email_subject_prefix(self):
        return self._email_subject_prefix
    
    @email_subject_prefix.setter
    def email_subject_prefix(self, email_subject_prefix):
        self._email_subject_prefix = email_subject_prefix

    @property
    def alert_email_to_all_admins(self):
        return self._alert_email_to_all_admins
    
    @alert_email_to_all_admins.setter
    def alert_email_to_all_admins(self, alert_email_to_all_admins):
        self._alert_email_to_all_admins = alert_email_to_all_admins

    @property
    def alert_email_to(self):
        return self._alert_email_to
    
    @alert_email_to.setter
    def alert_email_to(self, alert_email_to):
        self._alert_email_to = alert_email_to

    @property
    def smtp_settings(self):
        return self._smtp_settings
    
    @smtp_settings.setter
    def smtp_settings(self, smtp_settings):
        self._smtp_settings = smtp_settings


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
        if not isinstance(other, EmailSettingsType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
