"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re
from ..entity_type import EntityType


class StrandedItemType(EntityType):
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
        'entity_type': 'str',
        'deletion_date': 'str',
        'error_message': 'str',
        'parent': 'ReferenceType',
        'stranded_item_vim_objects': 'StrandedItemVimObjectsType'
    }

    attribute_map = {
        'entity_type': 'entityType',
        'deletion_date': 'deletionDate',
        'error_message': 'errorMessage',
        'parent': 'parent',
        'stranded_item_vim_objects': 'strandedItemVimObjects'
    }

    def __init__(self, entity_type=None,deletion_date=None,error_message=None,parent=None,stranded_item_vim_objects=None):
        self._entity_type = None
        self._deletion_date = None
        self._error_message = None
        self._parent = None
        self._stranded_item_vim_objects = None

        if entity_type is not None:
            self.entity_type = entity_type
        if deletion_date is not None:
            self.deletion_date = deletion_date
        if error_message is not None:
            self.error_message = error_message
        if parent is not None:
            self.parent = parent
        if stranded_item_vim_objects is not None:
            self.stranded_item_vim_objects = stranded_item_vim_objects

    @property
    def entity_type(self):
        return self._entity_type
    
    @entity_type.setter
    def entity_type(self, entity_type):
        self._entity_type = entity_type

    @property
    def deletion_date(self):
        return self._deletion_date
    
    @deletion_date.setter
    def deletion_date(self, deletion_date):
        self._deletion_date = deletion_date

    @property
    def error_message(self):
        return self._error_message
    
    @error_message.setter
    def error_message(self, error_message):
        self._error_message = error_message

    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def stranded_item_vim_objects(self):
        return self._stranded_item_vim_objects
    
    @stranded_item_vim_objects.setter
    def stranded_item_vim_objects(self, stranded_item_vim_objects):
        self._stranded_item_vim_objects = stranded_item_vim_objects


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
        if not isinstance(other, StrandedItemType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
