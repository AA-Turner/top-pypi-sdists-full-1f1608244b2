"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from ..schema.ovf.section_type import SectionType


class CustomizationSectionType(SectionType):
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
        'customize_on_instantiate': 'bool',
        'link': 'list[LinkType]',
        'any': 'list[object]',
        'gold_master': 'bool',
        'href': 'str',
        'type': 'str'
    }

    attribute_map = {
        'customize_on_instantiate': 'customizeOnInstantiate',
        'link': 'link',
        'any': 'any',
        'gold_master': 'goldMaster',
        'href': 'href',
        'type': 'type'
    }

    def __init__(self, customize_on_instantiate=None,link=None,any=None,gold_master=None,href=None,type=None):
        self._customize_on_instantiate = None
        self._link = None
        self._any = None
        self._gold_master = None
        self._href = None
        self._type = None

        if customize_on_instantiate is not None:
            self.customize_on_instantiate = customize_on_instantiate
        if link is not None:
            self.link = link
        if any is not None:
            self.any = any
        if gold_master is not None:
            self.gold_master = gold_master
        if href is not None:
            self.href = href
        if type is not None:
            self.type = type

    @property
    def customize_on_instantiate(self):
        return self._customize_on_instantiate
    
    @customize_on_instantiate.setter
    def customize_on_instantiate(self, customize_on_instantiate):
        self._customize_on_instantiate = customize_on_instantiate

    @property
    def link(self):
        return self._link
    
    @link.setter
    def link(self, link):
        self._link = link

    @property
    def any(self):
        return self._any
    
    @any.setter
    def any(self, any):
        self._any = any

    @property
    def gold_master(self):
        return self._gold_master
    
    @gold_master.setter
    def gold_master(self, gold_master):
        self._gold_master = gold_master

    @property
    def href(self):
        return self._href
    
    @href.setter
    def href(self, href):
        self._href = href

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        self._type = type


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
        if not isinstance(other, CustomizationSectionType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
