"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .v_cloud_extensible_type import VCloudExtensibleType


class SmtpServerSettingsType(VCloudExtensibleType):
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
        'is_use_authentication': 'bool',
        'host': 'str',
        'port': 'int',
        'username': 'str',
        'password': 'str',
        'smtp_secure_mode': 'SmtpSecureModeType',
        'ssl_trust_store': 'str'
    }

    attribute_map = {
        'is_use_authentication': 'isUseAuthentication',
        'host': 'host',
        'port': 'port',
        'username': 'username',
        'password': 'password',
        'smtp_secure_mode': 'smtpSecureMode',
        'ssl_trust_store': 'sslTrustStore'
    }

    def __init__(self, is_use_authentication=None,host=None,port=None,username=None,password=None,smtp_secure_mode=None,ssl_trust_store=None):
        self._is_use_authentication = None
        self._host = None
        self._port = None
        self._username = None
        self._password = None
        self._smtp_secure_mode = None
        self._ssl_trust_store = None

        if is_use_authentication is not None:
            self.is_use_authentication = is_use_authentication
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if smtp_secure_mode is not None:
            self.smtp_secure_mode = smtp_secure_mode
        if ssl_trust_store is not None:
            self.ssl_trust_store = ssl_trust_store

    @property
    def is_use_authentication(self):
        return self._is_use_authentication
    
    @is_use_authentication.setter
    def is_use_authentication(self, is_use_authentication):
        self._is_use_authentication = is_use_authentication

    @property
    def host(self):
        return self._host
    
    @host.setter
    def host(self, host):
        self._host = host

    @property
    def port(self):
        return self._port
    
    @port.setter
    def port(self, port):
        self._port = port

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password

    @property
    def smtp_secure_mode(self):
        return self._smtp_secure_mode
    
    @smtp_secure_mode.setter
    def smtp_secure_mode(self, smtp_secure_mode):
        self._smtp_secure_mode = smtp_secure_mode

    @property
    def ssl_trust_store(self):
        return self._ssl_trust_store
    
    @ssl_trust_store.setter
    def ssl_trust_store(self, ssl_trust_store):
        self._ssl_trust_store = ssl_trust_store


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
        if not isinstance(other, SmtpServerSettingsType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
