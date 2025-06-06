# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigParams(object):
    """
    Database configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigParams object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_key:
            The value to assign to the config_key property of this ConfigParams.
        :type config_key: str

        :param default_config_value:
            The value to assign to the default_config_value property of this ConfigParams.
        :type default_config_value: str

        :param overriden_config_value:
            The value to assign to the overriden_config_value property of this ConfigParams.
        :type overriden_config_value: str

        :param allowed_values:
            The value to assign to the allowed_values property of this ConfigParams.
        :type allowed_values: str

        :param is_restart_required:
            The value to assign to the is_restart_required property of this ConfigParams.
        :type is_restart_required: bool

        :param data_type:
            The value to assign to the data_type property of this ConfigParams.
        :type data_type: str

        :param is_overridable:
            The value to assign to the is_overridable property of this ConfigParams.
        :type is_overridable: bool

        :param description:
            The value to assign to the description property of this ConfigParams.
        :type description: str

        """
        self.swagger_types = {
            'config_key': 'str',
            'default_config_value': 'str',
            'overriden_config_value': 'str',
            'allowed_values': 'str',
            'is_restart_required': 'bool',
            'data_type': 'str',
            'is_overridable': 'bool',
            'description': 'str'
        }
        self.attribute_map = {
            'config_key': 'configKey',
            'default_config_value': 'defaultConfigValue',
            'overriden_config_value': 'overridenConfigValue',
            'allowed_values': 'allowedValues',
            'is_restart_required': 'isRestartRequired',
            'data_type': 'dataType',
            'is_overridable': 'isOverridable',
            'description': 'description'
        }
        self._config_key = None
        self._default_config_value = None
        self._overriden_config_value = None
        self._allowed_values = None
        self._is_restart_required = None
        self._data_type = None
        self._is_overridable = None
        self._description = None

    @property
    def config_key(self):
        """
        **[Required]** Gets the config_key of this ConfigParams.
        The configuration variable name.


        :return: The config_key of this ConfigParams.
        :rtype: str
        """
        return self._config_key

    @config_key.setter
    def config_key(self, config_key):
        """
        Sets the config_key of this ConfigParams.
        The configuration variable name.


        :param config_key: The config_key of this ConfigParams.
        :type: str
        """
        self._config_key = config_key

    @property
    def default_config_value(self):
        """
        **[Required]** Gets the default_config_value of this ConfigParams.
        Default value for the configuration variable.


        :return: The default_config_value of this ConfigParams.
        :rtype: str
        """
        return self._default_config_value

    @default_config_value.setter
    def default_config_value(self, default_config_value):
        """
        Sets the default_config_value of this ConfigParams.
        Default value for the configuration variable.


        :param default_config_value: The default_config_value of this ConfigParams.
        :type: str
        """
        self._default_config_value = default_config_value

    @property
    def overriden_config_value(self):
        """
        Gets the overriden_config_value of this ConfigParams.
        User-selected configuration variable value.


        :return: The overriden_config_value of this ConfigParams.
        :rtype: str
        """
        return self._overriden_config_value

    @overriden_config_value.setter
    def overriden_config_value(self, overriden_config_value):
        """
        Sets the overriden_config_value of this ConfigParams.
        User-selected configuration variable value.


        :param overriden_config_value: The overriden_config_value of this ConfigParams.
        :type: str
        """
        self._overriden_config_value = overriden_config_value

    @property
    def allowed_values(self):
        """
        **[Required]** Gets the allowed_values of this ConfigParams.
        Range or list of allowed values.


        :return: The allowed_values of this ConfigParams.
        :rtype: str
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """
        Sets the allowed_values of this ConfigParams.
        Range or list of allowed values.


        :param allowed_values: The allowed_values of this ConfigParams.
        :type: str
        """
        self._allowed_values = allowed_values

    @property
    def is_restart_required(self):
        """
        **[Required]** Gets the is_restart_required of this ConfigParams.
        If true, modifying this configuration value will require a restart of the database.


        :return: The is_restart_required of this ConfigParams.
        :rtype: bool
        """
        return self._is_restart_required

    @is_restart_required.setter
    def is_restart_required(self, is_restart_required):
        """
        Sets the is_restart_required of this ConfigParams.
        If true, modifying this configuration value will require a restart of the database.


        :param is_restart_required: The is_restart_required of this ConfigParams.
        :type: bool
        """
        self._is_restart_required = is_restart_required

    @property
    def data_type(self):
        """
        **[Required]** Gets the data_type of this ConfigParams.
        Data type of the variable.


        :return: The data_type of this ConfigParams.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this ConfigParams.
        Data type of the variable.


        :param data_type: The data_type of this ConfigParams.
        :type: str
        """
        self._data_type = data_type

    @property
    def is_overridable(self):
        """
        **[Required]** Gets the is_overridable of this ConfigParams.
        Whether the value can be overridden or not.


        :return: The is_overridable of this ConfigParams.
        :rtype: bool
        """
        return self._is_overridable

    @is_overridable.setter
    def is_overridable(self, is_overridable):
        """
        Sets the is_overridable of this ConfigParams.
        Whether the value can be overridden or not.


        :param is_overridable: The is_overridable of this ConfigParams.
        :type: bool
        """
        self._is_overridable = is_overridable

    @property
    def description(self):
        """
        **[Required]** Gets the description of this ConfigParams.
        Details about the PostgreSQL parameter.


        :return: The description of this ConfigParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConfigParams.
        Details about the PostgreSQL parameter.


        :param description: The description of this ConfigParams.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
