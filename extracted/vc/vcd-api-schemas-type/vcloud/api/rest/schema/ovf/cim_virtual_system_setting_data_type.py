"""
 Copyright (c) 2021 VMware, Inc. All rights reserved.
"""
from pprint import pformat
from six import iteritems
import re


class CIMVirtualSystemSettingDataType(object):
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
        'automatic_recovery_action': 'AutomaticRecoveryAction',
        'automatic_shutdown_action': 'AutomaticShutdownAction',
        'automatic_startup_action': 'AutomaticStartupAction',
        'automatic_startup_action_delay': 'CimDateTime',
        'automatic_startup_action_sequence_number': 'CimUnsignedShort',
        'caption': 'VirtualSystemCaption',
        'changeable_type': 'VirtualSystemChangeableType',
        'configuration_data_root': 'CimString',
        'configuration_file': 'CimString',
        'configuration_id': 'CimString',
        'configuration_name': 'VirtualSystemConfigurationName',
        'creation_time': 'CimDateTime',
        'description': 'VirtualSystemDescription',
        'element_name': 'VirtualSystemElementName',
        'generation': 'VirtualSystemGeneration',
        'instance_id': 'VirtualSystemInstanceID',
        'log_data_root': 'CimString',
        'notes': 'list[CimString]',
        'recovery_file': 'CimString',
        'snapshot_data_root': 'CimString',
        'suspend_data_root': 'CimString',
        'swap_file_data_root': 'CimString',
        'virtual_system_identifier': 'CimString',
        'virtual_system_type': 'CimString',
        'any': 'list[object]',
        'other_attributes': 'object'
    }

    attribute_map = {
        'automatic_recovery_action': 'automaticRecoveryAction',
        'automatic_shutdown_action': 'automaticShutdownAction',
        'automatic_startup_action': 'automaticStartupAction',
        'automatic_startup_action_delay': 'automaticStartupActionDelay',
        'automatic_startup_action_sequence_number': 'automaticStartupActionSequenceNumber',
        'caption': 'caption',
        'changeable_type': 'changeableType',
        'configuration_data_root': 'configurationDataRoot',
        'configuration_file': 'configurationFile',
        'configuration_id': 'configurationID',
        'configuration_name': 'configurationName',
        'creation_time': 'creationTime',
        'description': 'description',
        'element_name': 'elementName',
        'generation': 'generation',
        'instance_id': 'instanceID',
        'log_data_root': 'logDataRoot',
        'notes': 'notes',
        'recovery_file': 'recoveryFile',
        'snapshot_data_root': 'snapshotDataRoot',
        'suspend_data_root': 'suspendDataRoot',
        'swap_file_data_root': 'swapFileDataRoot',
        'virtual_system_identifier': 'virtualSystemIdentifier',
        'virtual_system_type': 'virtualSystemType',
        'any': 'any',
        'other_attributes': 'otherAttributes'
    }

    def __init__(self, automatic_recovery_action=None,automatic_shutdown_action=None,automatic_startup_action=None,automatic_startup_action_delay=None,automatic_startup_action_sequence_number=None,caption=None,changeable_type=None,configuration_data_root=None,configuration_file=None,configuration_id=None,configuration_name=None,creation_time=None,description=None,element_name=None,generation=None,instance_id=None,log_data_root=None,notes=None,recovery_file=None,snapshot_data_root=None,suspend_data_root=None,swap_file_data_root=None,virtual_system_identifier=None,virtual_system_type=None,any=None,other_attributes=None):
        self._automatic_recovery_action = None
        self._automatic_shutdown_action = None
        self._automatic_startup_action = None
        self._automatic_startup_action_delay = None
        self._automatic_startup_action_sequence_number = None
        self._caption = None
        self._changeable_type = None
        self._configuration_data_root = None
        self._configuration_file = None
        self._configuration_id = None
        self._configuration_name = None
        self._creation_time = None
        self._description = None
        self._element_name = None
        self._generation = None
        self._instance_id = None
        self._log_data_root = None
        self._notes = None
        self._recovery_file = None
        self._snapshot_data_root = None
        self._suspend_data_root = None
        self._swap_file_data_root = None
        self._virtual_system_identifier = None
        self._virtual_system_type = None
        self._any = None
        self._other_attributes = None

        if automatic_recovery_action is not None:
            self.automatic_recovery_action = automatic_recovery_action
        if automatic_shutdown_action is not None:
            self.automatic_shutdown_action = automatic_shutdown_action
        if automatic_startup_action is not None:
            self.automatic_startup_action = automatic_startup_action
        if automatic_startup_action_delay is not None:
            self.automatic_startup_action_delay = automatic_startup_action_delay
        if automatic_startup_action_sequence_number is not None:
            self.automatic_startup_action_sequence_number = automatic_startup_action_sequence_number
        if caption is not None:
            self.caption = caption
        if changeable_type is not None:
            self.changeable_type = changeable_type
        if configuration_data_root is not None:
            self.configuration_data_root = configuration_data_root
        if configuration_file is not None:
            self.configuration_file = configuration_file
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if configuration_name is not None:
            self.configuration_name = configuration_name
        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if element_name is not None:
            self.element_name = element_name
        if generation is not None:
            self.generation = generation
        if instance_id is not None:
            self.instance_id = instance_id
        if log_data_root is not None:
            self.log_data_root = log_data_root
        if notes is not None:
            self.notes = notes
        if recovery_file is not None:
            self.recovery_file = recovery_file
        if snapshot_data_root is not None:
            self.snapshot_data_root = snapshot_data_root
        if suspend_data_root is not None:
            self.suspend_data_root = suspend_data_root
        if swap_file_data_root is not None:
            self.swap_file_data_root = swap_file_data_root
        if virtual_system_identifier is not None:
            self.virtual_system_identifier = virtual_system_identifier
        if virtual_system_type is not None:
            self.virtual_system_type = virtual_system_type
        if any is not None:
            self.any = any
        if other_attributes is not None:
            self.other_attributes = other_attributes

    @property
    def automatic_recovery_action(self):
        return self._automatic_recovery_action
    
    @automatic_recovery_action.setter
    def automatic_recovery_action(self, automatic_recovery_action):
        self._automatic_recovery_action = automatic_recovery_action

    @property
    def automatic_shutdown_action(self):
        return self._automatic_shutdown_action
    
    @automatic_shutdown_action.setter
    def automatic_shutdown_action(self, automatic_shutdown_action):
        self._automatic_shutdown_action = automatic_shutdown_action

    @property
    def automatic_startup_action(self):
        return self._automatic_startup_action
    
    @automatic_startup_action.setter
    def automatic_startup_action(self, automatic_startup_action):
        self._automatic_startup_action = automatic_startup_action

    @property
    def automatic_startup_action_delay(self):
        return self._automatic_startup_action_delay
    
    @automatic_startup_action_delay.setter
    def automatic_startup_action_delay(self, automatic_startup_action_delay):
        self._automatic_startup_action_delay = automatic_startup_action_delay

    @property
    def automatic_startup_action_sequence_number(self):
        return self._automatic_startup_action_sequence_number
    
    @automatic_startup_action_sequence_number.setter
    def automatic_startup_action_sequence_number(self, automatic_startup_action_sequence_number):
        self._automatic_startup_action_sequence_number = automatic_startup_action_sequence_number

    @property
    def caption(self):
        return self._caption
    
    @caption.setter
    def caption(self, caption):
        self._caption = caption

    @property
    def changeable_type(self):
        return self._changeable_type
    
    @changeable_type.setter
    def changeable_type(self, changeable_type):
        self._changeable_type = changeable_type

    @property
    def configuration_data_root(self):
        return self._configuration_data_root
    
    @configuration_data_root.setter
    def configuration_data_root(self, configuration_data_root):
        self._configuration_data_root = configuration_data_root

    @property
    def configuration_file(self):
        return self._configuration_file
    
    @configuration_file.setter
    def configuration_file(self, configuration_file):
        self._configuration_file = configuration_file

    @property
    def configuration_id(self):
        return self._configuration_id
    
    @configuration_id.setter
    def configuration_id(self, configuration_id):
        self._configuration_id = configuration_id

    @property
    def configuration_name(self):
        return self._configuration_name
    
    @configuration_name.setter
    def configuration_name(self, configuration_name):
        self._configuration_name = configuration_name

    @property
    def creation_time(self):
        return self._creation_time
    
    @creation_time.setter
    def creation_time(self, creation_time):
        self._creation_time = creation_time

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def element_name(self):
        return self._element_name
    
    @element_name.setter
    def element_name(self, element_name):
        self._element_name = element_name

    @property
    def generation(self):
        return self._generation
    
    @generation.setter
    def generation(self, generation):
        self._generation = generation

    @property
    def instance_id(self):
        return self._instance_id
    
    @instance_id.setter
    def instance_id(self, instance_id):
        self._instance_id = instance_id

    @property
    def log_data_root(self):
        return self._log_data_root
    
    @log_data_root.setter
    def log_data_root(self, log_data_root):
        self._log_data_root = log_data_root

    @property
    def notes(self):
        return self._notes
    
    @notes.setter
    def notes(self, notes):
        self._notes = notes

    @property
    def recovery_file(self):
        return self._recovery_file
    
    @recovery_file.setter
    def recovery_file(self, recovery_file):
        self._recovery_file = recovery_file

    @property
    def snapshot_data_root(self):
        return self._snapshot_data_root
    
    @snapshot_data_root.setter
    def snapshot_data_root(self, snapshot_data_root):
        self._snapshot_data_root = snapshot_data_root

    @property
    def suspend_data_root(self):
        return self._suspend_data_root
    
    @suspend_data_root.setter
    def suspend_data_root(self, suspend_data_root):
        self._suspend_data_root = suspend_data_root

    @property
    def swap_file_data_root(self):
        return self._swap_file_data_root
    
    @swap_file_data_root.setter
    def swap_file_data_root(self, swap_file_data_root):
        self._swap_file_data_root = swap_file_data_root

    @property
    def virtual_system_identifier(self):
        return self._virtual_system_identifier
    
    @virtual_system_identifier.setter
    def virtual_system_identifier(self, virtual_system_identifier):
        self._virtual_system_identifier = virtual_system_identifier

    @property
    def virtual_system_type(self):
        return self._virtual_system_type
    
    @virtual_system_type.setter
    def virtual_system_type(self, virtual_system_type):
        self._virtual_system_type = virtual_system_type

    @property
    def any(self):
        return self._any
    
    @any.setter
    def any(self, any):
        self._any = any

    @property
    def other_attributes(self):
        return self._other_attributes
    
    @other_attributes.setter
    def other_attributes(self, other_attributes):
        self._other_attributes = other_attributes


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
        if not isinstance(other, CIMVirtualSystemSettingDataType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
