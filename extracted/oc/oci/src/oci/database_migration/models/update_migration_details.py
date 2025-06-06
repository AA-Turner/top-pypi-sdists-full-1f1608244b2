# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMigrationDetails(object):
    """
    Common Update Migration details.
    """

    #: A constant which can be used with the database_combination property of a UpdateMigrationDetails.
    #: This constant has a value of "MYSQL"
    DATABASE_COMBINATION_MYSQL = "MYSQL"

    #: A constant which can be used with the database_combination property of a UpdateMigrationDetails.
    #: This constant has a value of "ORACLE"
    DATABASE_COMBINATION_ORACLE = "ORACLE"

    #: A constant which can be used with the type property of a UpdateMigrationDetails.
    #: This constant has a value of "ONLINE"
    TYPE_ONLINE = "ONLINE"

    #: A constant which can be used with the type property of a UpdateMigrationDetails.
    #: This constant has a value of "OFFLINE"
    TYPE_OFFLINE = "OFFLINE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMigrationDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_migration.models.UpdateMySqlMigrationDetails`
        * :class:`~oci.database_migration.models.UpdateOracleMigrationDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateMigrationDetails.
        :type description: str

        :param database_combination:
            The value to assign to the database_combination property of this UpdateMigrationDetails.
            Allowed values for this property are: "MYSQL", "ORACLE"
        :type database_combination: str

        :param type:
            The value to assign to the type property of this UpdateMigrationDetails.
            Allowed values for this property are: "ONLINE", "OFFLINE"
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateMigrationDetails.
        :type display_name: str

        :param source_database_connection_id:
            The value to assign to the source_database_connection_id property of this UpdateMigrationDetails.
        :type source_database_connection_id: str

        :param target_database_connection_id:
            The value to assign to the target_database_connection_id property of this UpdateMigrationDetails.
        :type target_database_connection_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateMigrationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateMigrationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'database_combination': 'str',
            'type': 'str',
            'display_name': 'str',
            'source_database_connection_id': 'str',
            'target_database_connection_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'description': 'description',
            'database_combination': 'databaseCombination',
            'type': 'type',
            'display_name': 'displayName',
            'source_database_connection_id': 'sourceDatabaseConnectionId',
            'target_database_connection_id': 'targetDatabaseConnectionId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._description = None
        self._database_combination = None
        self._type = None
        self._display_name = None
        self._source_database_connection_id = None
        self._target_database_connection_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['databaseCombination']

        if type == 'MYSQL':
            return 'UpdateMySqlMigrationDetails'

        if type == 'ORACLE':
            return 'UpdateOracleMigrationDetails'
        else:
            return 'UpdateMigrationDetails'

    @property
    def description(self):
        """
        Gets the description of this UpdateMigrationDetails.
        A user-friendly description. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The description of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateMigrationDetails.
        A user-friendly description. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param description: The description of this UpdateMigrationDetails.
        :type: str
        """
        self._description = description

    @property
    def database_combination(self):
        """
        **[Required]** Gets the database_combination of this UpdateMigrationDetails.
        The combination of source and target databases participating in a migration.
        Example: ORACLE means the migration is meant for migrating Oracle source and target databases.

        Allowed values for this property are: "MYSQL", "ORACLE"


        :return: The database_combination of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._database_combination

    @database_combination.setter
    def database_combination(self, database_combination):
        """
        Sets the database_combination of this UpdateMigrationDetails.
        The combination of source and target databases participating in a migration.
        Example: ORACLE means the migration is meant for migrating Oracle source and target databases.


        :param database_combination: The database_combination of this UpdateMigrationDetails.
        :type: str
        """
        allowed_values = ["MYSQL", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(database_combination, allowed_values):
            raise ValueError(
                f"Invalid value for `database_combination`, must be None or one of {allowed_values}"
            )
        self._database_combination = database_combination

    @property
    def type(self):
        """
        Gets the type of this UpdateMigrationDetails.
        The type of the migration to be performed.
        Example: ONLINE if no downtime is preferred for a migration. This method uses Oracle GoldenGate for replication.

        Allowed values for this property are: "ONLINE", "OFFLINE"


        :return: The type of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UpdateMigrationDetails.
        The type of the migration to be performed.
        Example: ONLINE if no downtime is preferred for a migration. This method uses Oracle GoldenGate for replication.


        :param type: The type of this UpdateMigrationDetails.
        :type: str
        """
        allowed_values = ["ONLINE", "OFFLINE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateMigrationDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateMigrationDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateMigrationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def source_database_connection_id(self):
        """
        Gets the source_database_connection_id of this UpdateMigrationDetails.
        The OCID of the resource being referenced.


        :return: The source_database_connection_id of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._source_database_connection_id

    @source_database_connection_id.setter
    def source_database_connection_id(self, source_database_connection_id):
        """
        Sets the source_database_connection_id of this UpdateMigrationDetails.
        The OCID of the resource being referenced.


        :param source_database_connection_id: The source_database_connection_id of this UpdateMigrationDetails.
        :type: str
        """
        self._source_database_connection_id = source_database_connection_id

    @property
    def target_database_connection_id(self):
        """
        Gets the target_database_connection_id of this UpdateMigrationDetails.
        The OCID of the resource being referenced.


        :return: The target_database_connection_id of this UpdateMigrationDetails.
        :rtype: str
        """
        return self._target_database_connection_id

    @target_database_connection_id.setter
    def target_database_connection_id(self, target_database_connection_id):
        """
        Sets the target_database_connection_id of this UpdateMigrationDetails.
        The OCID of the resource being referenced.


        :param target_database_connection_id: The target_database_connection_id of this UpdateMigrationDetails.
        :type: str
        """
        self._target_database_connection_id = target_database_connection_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateMigrationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see Resource Tags. Example: {\"Department\": \"Finance\"}


        :return: The freeform_tags of this UpdateMigrationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateMigrationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see Resource Tags. Example: {\"Department\": \"Finance\"}


        :param freeform_tags: The freeform_tags of this UpdateMigrationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateMigrationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateMigrationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateMigrationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateMigrationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
