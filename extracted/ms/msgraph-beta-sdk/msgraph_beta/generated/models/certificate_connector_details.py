from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class CertificateConnectorDetails(Entity, Parsable):
    """
    Entity used to retrieve information about Intune Certificate Connectors.
    """
    # Connector name (set during enrollment).
    connector_name: Optional[str] = None
    # Version of the connector installed.
    connector_version: Optional[str] = None
    # Date/time when this connector was enrolled.
    enrollment_date_time: Optional[datetime.datetime] = None
    # Date/time when this connector last connected to the service.
    last_checkin_date_time: Optional[datetime.datetime] = None
    # Name of the machine hosting this connector service.
    machine_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CertificateConnectorDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CertificateConnectorDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CertificateConnectorDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "connectorName": lambda n : setattr(self, 'connector_name', n.get_str_value()),
            "connectorVersion": lambda n : setattr(self, 'connector_version', n.get_str_value()),
            "enrollmentDateTime": lambda n : setattr(self, 'enrollment_date_time', n.get_datetime_value()),
            "lastCheckinDateTime": lambda n : setattr(self, 'last_checkin_date_time', n.get_datetime_value()),
            "machineName": lambda n : setattr(self, 'machine_name', n.get_str_value()),
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
        writer.write_str_value("connectorName", self.connector_name)
        writer.write_str_value("connectorVersion", self.connector_version)
        writer.write_datetime_value("enrollmentDateTime", self.enrollment_date_time)
        writer.write_datetime_value("lastCheckinDateTime", self.last_checkin_date_time)
        writer.write_str_value("machineName", self.machine_name)
    

