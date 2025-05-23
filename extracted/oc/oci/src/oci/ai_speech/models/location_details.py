# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LocationDetails(object):
    """
    Possible object storage location types
    """

    #: A constant which can be used with the location_type property of a LocationDetails.
    #: This constant has a value of "OBJECT_LIST"
    LOCATION_TYPE_OBJECT_LIST = "OBJECT_LIST"

    def __init__(self, **kwargs):
        """
        Initializes a new LocationDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_speech.models.ObjectListDataset`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param location_type:
            The value to assign to the location_type property of this LocationDetails.
            Allowed values for this property are: "OBJECT_LIST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type location_type: str

        """
        self.swagger_types = {
            'location_type': 'str'
        }
        self.attribute_map = {
            'location_type': 'locationType'
        }
        self._location_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['locationType']

        if type == 'OBJECT_LIST':
            return 'ObjectListDataset'
        else:
            return 'LocationDetails'

    @property
    def location_type(self):
        """
        **[Required]** Gets the location_type of this LocationDetails.
        Possible object storage location types

        Allowed values for this property are: "OBJECT_LIST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The location_type of this LocationDetails.
        :rtype: str
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """
        Sets the location_type of this LocationDetails.
        Possible object storage location types


        :param location_type: The location_type of this LocationDetails.
        :type: str
        """
        allowed_values = ["OBJECT_LIST"]
        if not value_allowed_none_or_none_sentinel(location_type, allowed_values):
            location_type = 'UNKNOWN_ENUM_VALUE'
        self._location_type = location_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
