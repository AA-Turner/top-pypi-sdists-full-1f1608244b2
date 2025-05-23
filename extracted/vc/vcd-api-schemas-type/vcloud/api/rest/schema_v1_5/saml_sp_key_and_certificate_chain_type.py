"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from .resource_type import ResourceType


class SamlSPKeyAndCertificateChainType(ResourceType):
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
        'key': 'str',
        'certificate_chain': 'str'
    }

    attribute_map = {
        'key': 'key',
        'certificate_chain': 'certificateChain'
    }

    def __init__(self, key=None,certificate_chain=None):
        self._key = None
        self._certificate_chain = None

        if key is not None:
            self.key = key
        if certificate_chain is not None:
            self.certificate_chain = certificate_chain

    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, key):
        self._key = key

    @property
    def certificate_chain(self):
        return self._certificate_chain
    
    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        self._certificate_chain = certificate_chain


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
        if not isinstance(other, SamlSPKeyAndCertificateChainType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
