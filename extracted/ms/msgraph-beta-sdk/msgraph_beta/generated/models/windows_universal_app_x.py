from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_contained_app import MobileContainedApp
    from .mobile_lob_app import MobileLobApp
    from .windows_architecture import WindowsArchitecture
    from .windows_device_type import WindowsDeviceType
    from .windows_minimum_operating_system import WindowsMinimumOperatingSystem

from .mobile_lob_app import MobileLobApp

@dataclass
class WindowsUniversalAppX(MobileLobApp, Parsable):
    """
    Contains properties and inherited properties for Windows Universal AppX Line Of Business apps. Inherits from `mobileLobApp`.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUniversalAppX"
    # Contains properties for Windows architecture.
    applicable_architectures: Optional[WindowsArchitecture] = None
    # Contains properties for Windows device type. Multiple values can be selected. Default value is `none`.
    applicable_device_types: Optional[WindowsDeviceType] = None
    # The collection of contained apps in the committed mobileAppContent of a windowsUniversalAppX app. This property is read-only.
    committed_contained_apps: Optional[list[MobileContainedApp]] = None
    # The Identity Name of the app, parsed from the appx file when it is uploaded through the Intune MEM console. For example: 'Contoso.DemoApp'.
    identity_name: Optional[str] = None
    # The Identity Publisher Hash of the app, parsed from the appx file when it is uploaded through the Intune MEM console. For example: 'AB82CD0XYZ'.
    identity_publisher_hash: Optional[str] = None
    # The Identity Resource Identifier of the app, parsed from the appx file when it is uploaded through the Intune MEM console. For example: 'TestResourceId'.
    identity_resource_identifier: Optional[str] = None
    # The Identity Version of the app, parsed from the appx file when it is uploaded through the Intune MEM console.  For example: '1.0.0.0'.
    identity_version: Optional[str] = None
    # Whether or not the app is a bundle. If TRUE, app is a bundle; if FALSE, app is not a bundle.
    is_bundle: Optional[bool] = None
    # The minimum operating system required for a Windows mobile app.
    minimum_supported_operating_system: Optional[WindowsMinimumOperatingSystem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsUniversalAppX:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUniversalAppX
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsUniversalAppX()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_contained_app import MobileContainedApp
        from .mobile_lob_app import MobileLobApp
        from .windows_architecture import WindowsArchitecture
        from .windows_device_type import WindowsDeviceType
        from .windows_minimum_operating_system import WindowsMinimumOperatingSystem

        from .mobile_contained_app import MobileContainedApp
        from .mobile_lob_app import MobileLobApp
        from .windows_architecture import WindowsArchitecture
        from .windows_device_type import WindowsDeviceType
        from .windows_minimum_operating_system import WindowsMinimumOperatingSystem

        fields: dict[str, Callable[[Any], None]] = {
            "applicableArchitectures": lambda n : setattr(self, 'applicable_architectures', n.get_collection_of_enum_values(WindowsArchitecture)),
            "applicableDeviceTypes": lambda n : setattr(self, 'applicable_device_types', n.get_collection_of_enum_values(WindowsDeviceType)),
            "committedContainedApps": lambda n : setattr(self, 'committed_contained_apps', n.get_collection_of_object_values(MobileContainedApp)),
            "identityName": lambda n : setattr(self, 'identity_name', n.get_str_value()),
            "identityPublisherHash": lambda n : setattr(self, 'identity_publisher_hash', n.get_str_value()),
            "identityResourceIdentifier": lambda n : setattr(self, 'identity_resource_identifier', n.get_str_value()),
            "identityVersion": lambda n : setattr(self, 'identity_version', n.get_str_value()),
            "isBundle": lambda n : setattr(self, 'is_bundle', n.get_bool_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(WindowsMinimumOperatingSystem)),
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
        writer.write_enum_value("applicableArchitectures", self.applicable_architectures)
        writer.write_enum_value("applicableDeviceTypes", self.applicable_device_types)
        writer.write_collection_of_object_values("committedContainedApps", self.committed_contained_apps)
        writer.write_str_value("identityName", self.identity_name)
        writer.write_str_value("identityPublisherHash", self.identity_publisher_hash)
        writer.write_str_value("identityResourceIdentifier", self.identity_resource_identifier)
        writer.write_str_value("identityVersion", self.identity_version)
        writer.write_bool_value("isBundle", self.is_bundle)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
    

