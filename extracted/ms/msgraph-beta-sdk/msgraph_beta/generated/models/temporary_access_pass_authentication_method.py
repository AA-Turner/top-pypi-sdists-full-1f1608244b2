from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method import AuthenticationMethod

from .authentication_method import AuthenticationMethod

@dataclass
class TemporaryAccessPassAuthenticationMethod(AuthenticationMethod, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.temporaryAccessPassAuthenticationMethod"
    # Determines whether the pass is limited to a one-time use. If true, the pass can be used once; if false, the pass can be used multiple times within the Temporary Access Pass lifetime.
    is_usable_once: Optional[bool] = None
    # The lifetime of the Temporary Access Pass in minutes starting at startDateTime. Must be between 10 and 43200 inclusive (equivalent to 30 days).
    lifetime_in_minutes: Optional[int] = None
    # The date and time when the Temporary Access Pass becomes available to use and when isUsable is true is enforced.
    start_date_time: Optional[datetime.datetime] = None
    # The Temporary Access Pass used to authenticate. Returned only on creation of a new temporaryAccessPassAuthenticationMethod object; Hidden in subsequent read operations and returned as null with GET.
    temporary_access_pass: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TemporaryAccessPassAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TemporaryAccessPassAuthenticationMethod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TemporaryAccessPassAuthenticationMethod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method import AuthenticationMethod

        from .authentication_method import AuthenticationMethod

        fields: dict[str, Callable[[Any], None]] = {
            "isUsableOnce": lambda n : setattr(self, 'is_usable_once', n.get_bool_value()),
            "lifetimeInMinutes": lambda n : setattr(self, 'lifetime_in_minutes', n.get_int_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "temporaryAccessPass": lambda n : setattr(self, 'temporary_access_pass', n.get_str_value()),
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
        writer.write_bool_value("isUsableOnce", self.is_usable_once)
        writer.write_int_value("lifetimeInMinutes", self.lifetime_in_minutes)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("temporaryAccessPass", self.temporary_access_pass)
    

