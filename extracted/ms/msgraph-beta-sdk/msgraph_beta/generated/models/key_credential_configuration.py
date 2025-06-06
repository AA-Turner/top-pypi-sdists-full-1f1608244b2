from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_key_credential_restriction_type import AppKeyCredentialRestrictionType
    from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
    from .app_management_restriction_state import AppManagementRestrictionState

@dataclass
class KeyCredentialConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Collection of GUIDs that represent certificateBasedApplicationConfiguration that is allowed as root and intermediate certificate authorities.
    certificate_based_application_configuration_ids: Optional[list[str]] = None
    # Collection of custom security attribute exemptions. If an actor user or service principal has the custom security attribute defined in this section, they're exempted from the restriction.  This means that calls the user or service principal makes to create or update apps are exempt from this policy enforcement.
    exclude_actors: Optional[AppManagementPolicyActorExemptions] = None
    # String value that indicates the maximum lifetime for key expiration, defined as an ISO 8601 duration. For example, P4DT12H30M5S represents four days, 12 hours, 30 minutes, and five seconds. This property is required when restrictionType is set to keyLifetime.
    max_lifetime: Optional[datetime.timedelta] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the date from which the policy restriction applies to newly created applications. For existing applications, the enforcement date can be retroactively applied.
    restrict_for_apps_created_after_date_time: Optional[datetime.datetime] = None
    # The restrictionType property
    restriction_type: Optional[AppKeyCredentialRestrictionType] = None
    # Indicates whether the restriction is evaluated. The possible values are: enabled, disabled, unknownFutureValue. If enabled, the restriction is evaluated. If disabled, the restriction isn't evaluated or enforced.
    state: Optional[AppManagementRestrictionState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KeyCredentialConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KeyCredentialConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KeyCredentialConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_key_credential_restriction_type import AppKeyCredentialRestrictionType
        from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
        from .app_management_restriction_state import AppManagementRestrictionState

        from .app_key_credential_restriction_type import AppKeyCredentialRestrictionType
        from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
        from .app_management_restriction_state import AppManagementRestrictionState

        fields: dict[str, Callable[[Any], None]] = {
            "certificateBasedApplicationConfigurationIds": lambda n : setattr(self, 'certificate_based_application_configuration_ids', n.get_collection_of_primitive_values(str)),
            "excludeActors": lambda n : setattr(self, 'exclude_actors', n.get_object_value(AppManagementPolicyActorExemptions)),
            "maxLifetime": lambda n : setattr(self, 'max_lifetime', n.get_timedelta_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restrictForAppsCreatedAfterDateTime": lambda n : setattr(self, 'restrict_for_apps_created_after_date_time', n.get_datetime_value()),
            "restrictionType": lambda n : setattr(self, 'restriction_type', n.get_enum_value(AppKeyCredentialRestrictionType)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AppManagementRestrictionState)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("certificateBasedApplicationConfigurationIds", self.certificate_based_application_configuration_ids)
        writer.write_object_value("excludeActors", self.exclude_actors)
        writer.write_timedelta_value("maxLifetime", self.max_lifetime)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("restrictForAppsCreatedAfterDateTime", self.restrict_for_apps_created_after_date_time)
        writer.write_enum_value("restrictionType", self.restriction_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

