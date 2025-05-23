from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .drive_protection_rule import DriveProtectionRule
    from .drive_protection_unit import DriveProtectionUnit
    from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob
    from .protection_policy_base import ProtectionPolicyBase

from .protection_policy_base import ProtectionPolicyBase

@dataclass
class OneDriveForBusinessProtectionPolicy(ProtectionPolicyBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.oneDriveForBusinessProtectionPolicy"
    # Contains the details of the Onedrive for Business protection rule.
    drive_inclusion_rules: Optional[list[DriveProtectionRule]] = None
    # Contains the protection units associated with a  OneDrive for Business protection policy.
    drive_protection_units: Optional[list[DriveProtectionUnit]] = None
    # The driveProtectionUnitsBulkAdditionJobs property
    drive_protection_units_bulk_addition_jobs: Optional[list[DriveProtectionUnitsBulkAdditionJob]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OneDriveForBusinessProtectionPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OneDriveForBusinessProtectionPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OneDriveForBusinessProtectionPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .drive_protection_rule import DriveProtectionRule
        from .drive_protection_unit import DriveProtectionUnit
        from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob
        from .protection_policy_base import ProtectionPolicyBase

        from .drive_protection_rule import DriveProtectionRule
        from .drive_protection_unit import DriveProtectionUnit
        from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob
        from .protection_policy_base import ProtectionPolicyBase

        fields: dict[str, Callable[[Any], None]] = {
            "driveInclusionRules": lambda n : setattr(self, 'drive_inclusion_rules', n.get_collection_of_object_values(DriveProtectionRule)),
            "driveProtectionUnits": lambda n : setattr(self, 'drive_protection_units', n.get_collection_of_object_values(DriveProtectionUnit)),
            "driveProtectionUnitsBulkAdditionJobs": lambda n : setattr(self, 'drive_protection_units_bulk_addition_jobs', n.get_collection_of_object_values(DriveProtectionUnitsBulkAdditionJob)),
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
        writer.write_collection_of_object_values("driveInclusionRules", self.drive_inclusion_rules)
        writer.write_collection_of_object_values("driveProtectionUnits", self.drive_protection_units)
        writer.write_collection_of_object_values("driveProtectionUnitsBulkAdditionJobs", self.drive_protection_units_bulk_addition_jobs)
    

