# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20211001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TextSpan(object):
    """
    A wrapper class for offset and length, which together, represent a span of text in a text document.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TextSpan object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param offset:
            The value to assign to the offset property of this TextSpan.
        :type offset: float

        :param length:
            The value to assign to the length property of this TextSpan.
        :type length: float

        """
        self.swagger_types = {
            'offset': 'float',
            'length': 'float'
        }
        self.attribute_map = {
            'offset': 'offset',
            'length': 'length'
        }
        self._offset = None
        self._length = None

    @property
    def offset(self):
        """
        Gets the offset of this TextSpan.
        The offset of the selected text within the entire text.


        :return: The offset of this TextSpan.
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this TextSpan.
        The offset of the selected text within the entire text.


        :param offset: The offset of this TextSpan.
        :type: float
        """
        self._offset = offset

    @property
    def length(self):
        """
        Gets the length of this TextSpan.
        The length of the selected text.


        :return: The length of this TextSpan.
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this TextSpan.
        The length of the selected text.


        :param length: The length of this TextSpan.
        :type: float
        """
        self._length = length

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
