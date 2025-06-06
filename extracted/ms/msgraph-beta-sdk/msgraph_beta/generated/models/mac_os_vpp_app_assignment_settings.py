from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_assignment_settings import MobileAppAssignmentSettings

from .mobile_app_assignment_settings import MobileAppAssignmentSettings

@dataclass
class MacOsVppAppAssignmentSettings(MobileAppAssignmentSettings, Parsable):
    """
    Contains properties used to assign an Mac VPP mobile app to a group.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOsVppAppAssignmentSettings"
    # When TRUE, indicates that the app should not be automatically updated with the latest version from Apple app store. When FALSE, indicates that the app may be auto updated. By default, this property is set to null which internally is treated as FALSE.
    prevent_auto_app_update: Optional[bool] = None
    # When TRUE, indicates that the app should not be backed up to iCloud. When FALSE, indicates that the app may be backed up to iCloud. By default, this property is set to null which internally is treated as FALSE.
    prevent_managed_app_backup: Optional[bool] = None
    # Whether or not to uninstall the app when device is removed from Intune.
    uninstall_on_device_removal: Optional[bool] = None
    # Whether or not to use device licensing.
    use_device_licensing: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOsVppAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOsVppAppAssignmentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOsVppAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        fields: dict[str, Callable[[Any], None]] = {
            "preventAutoAppUpdate": lambda n : setattr(self, 'prevent_auto_app_update', n.get_bool_value()),
            "preventManagedAppBackup": lambda n : setattr(self, 'prevent_managed_app_backup', n.get_bool_value()),
            "uninstallOnDeviceRemoval": lambda n : setattr(self, 'uninstall_on_device_removal', n.get_bool_value()),
            "useDeviceLicensing": lambda n : setattr(self, 'use_device_licensing', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("preventAutoAppUpdate", self.prevent_auto_app_update)
        writer.write_bool_value("preventManagedAppBackup", self.prevent_managed_app_backup)
        writer.write_bool_value("uninstallOnDeviceRemoval", self.uninstall_on_device_removal)
        writer.write_bool_value("useDeviceLicensing", self.use_device_licensing)
    

