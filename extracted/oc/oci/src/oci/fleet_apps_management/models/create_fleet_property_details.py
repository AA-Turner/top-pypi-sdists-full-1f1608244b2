# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFleetPropertyDetails(object):
    """
    The information about new Property to manage fleet metadata details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFleetPropertyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this CreateFleetPropertyDetails.
        :type value: str

        :param property_id:
            The value to assign to the property_id property of this CreateFleetPropertyDetails.
        :type property_id: str

        """
        self.swagger_types = {
            'value': 'str',
            'property_id': 'str'
        }
        self.attribute_map = {
            'value': 'value',
            'property_id': 'propertyId'
        }
        self._value = None
        self._property_id = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this CreateFleetPropertyDetails.
        Value of the Property.


        :return: The value of this CreateFleetPropertyDetails.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CreateFleetPropertyDetails.
        Value of the Property.


        :param value: The value of this CreateFleetPropertyDetails.
        :type: str
        """
        self._value = value

    @property
    def property_id(self):
        """
        **[Required]** Gets the property_id of this CreateFleetPropertyDetails.
        OCID referring to global level metadata property.


        :return: The property_id of this CreateFleetPropertyDetails.
        :rtype: str
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """
        Sets the property_id of this CreateFleetPropertyDetails.
        OCID referring to global level metadata property.


        :param property_id: The property_id of this CreateFleetPropertyDetails.
        :type: str
        """
        self._property_id = property_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
