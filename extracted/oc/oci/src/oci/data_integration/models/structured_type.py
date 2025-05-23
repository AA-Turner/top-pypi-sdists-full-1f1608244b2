# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StructuredType(object):
    """
    A `StructuredType` object represents a data type that exists in a physical data asset object such as a table column, but is more complex. For example, an Oracle database `OBJECT` type. It can be composed of multiple `DataType` objects.
    """

    #: A constant which can be used with the dt_type property of a StructuredType.
    #: This constant has a value of "PRIMITIVE"
    DT_TYPE_PRIMITIVE = "PRIMITIVE"

    #: A constant which can be used with the dt_type property of a StructuredType.
    #: This constant has a value of "STRUCTURED"
    DT_TYPE_STRUCTURED = "STRUCTURED"

    def __init__(self, **kwargs):
        """
        Initializes a new StructuredType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param schema:
            The value to assign to the schema property of this StructuredType.
        :type schema: oci.data_integration.models.BaseType

        :param dt_type:
            The value to assign to the dt_type property of this StructuredType.
            Allowed values for this property are: "PRIMITIVE", "STRUCTURED"
        :type dt_type: str

        :param type_system_name:
            The value to assign to the type_system_name property of this StructuredType.
        :type type_system_name: str

        :param config_definition:
            The value to assign to the config_definition property of this StructuredType.
        :type config_definition: oci.data_integration.models.ConfigDefinition

        """
        self.swagger_types = {
            'schema': 'BaseType',
            'dt_type': 'str',
            'type_system_name': 'str',
            'config_definition': 'ConfigDefinition'
        }
        self.attribute_map = {
            'schema': 'schema',
            'dt_type': 'dtType',
            'type_system_name': 'typeSystemName',
            'config_definition': 'configDefinition'
        }
        self._schema = None
        self._dt_type = None
        self._type_system_name = None
        self._config_definition = None

    @property
    def schema(self):
        """
        Gets the schema of this StructuredType.

        :return: The schema of this StructuredType.
        :rtype: oci.data_integration.models.BaseType
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this StructuredType.

        :param schema: The schema of this StructuredType.
        :type: oci.data_integration.models.BaseType
        """
        self._schema = schema

    @property
    def dt_type(self):
        """
        Gets the dt_type of this StructuredType.
        The data type.

        Allowed values for this property are: "PRIMITIVE", "STRUCTURED"


        :return: The dt_type of this StructuredType.
        :rtype: str
        """
        return self._dt_type

    @dt_type.setter
    def dt_type(self, dt_type):
        """
        Sets the dt_type of this StructuredType.
        The data type.


        :param dt_type: The dt_type of this StructuredType.
        :type: str
        """
        allowed_values = ["PRIMITIVE", "STRUCTURED"]
        if not value_allowed_none_or_none_sentinel(dt_type, allowed_values):
            raise ValueError(
                f"Invalid value for `dt_type`, must be None or one of {allowed_values}"
            )
        self._dt_type = dt_type

    @property
    def type_system_name(self):
        """
        Gets the type_system_name of this StructuredType.
        The data type system name.


        :return: The type_system_name of this StructuredType.
        :rtype: str
        """
        return self._type_system_name

    @type_system_name.setter
    def type_system_name(self, type_system_name):
        """
        Sets the type_system_name of this StructuredType.
        The data type system name.


        :param type_system_name: The type_system_name of this StructuredType.
        :type: str
        """
        self._type_system_name = type_system_name

    @property
    def config_definition(self):
        """
        Gets the config_definition of this StructuredType.

        :return: The config_definition of this StructuredType.
        :rtype: oci.data_integration.models.ConfigDefinition
        """
        return self._config_definition

    @config_definition.setter
    def config_definition(self, config_definition):
        """
        Sets the config_definition of this StructuredType.

        :param config_definition: The config_definition of this StructuredType.
        :type: oci.data_integration.models.ConfigDefinition
        """
        self._config_definition = config_definition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
