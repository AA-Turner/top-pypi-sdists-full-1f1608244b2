from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.cloud_p_c_performance_report_name import CloudPCPerformanceReportName

@dataclass
class GetCloudPcPerformanceReportPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The filter property
    filter: Optional[str] = None
    # The groupBy property
    group_by: Optional[list[str]] = None
    # The orderBy property
    order_by: Optional[list[str]] = None
    # The reportName property
    report_name: Optional[CloudPCPerformanceReportName] = None
    # The search property
    search: Optional[str] = None
    # The select property
    select: Optional[list[str]] = None
    # The skip property
    skip: Optional[int] = None
    # The top property
    top: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetCloudPcPerformanceReportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetCloudPcPerformanceReportPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetCloudPcPerformanceReportPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.cloud_p_c_performance_report_name import CloudPCPerformanceReportName

        from .....models.cloud_p_c_performance_report_name import CloudPCPerformanceReportName

        fields: dict[str, Callable[[Any], None]] = {
            "filter": lambda n : setattr(self, 'filter', n.get_str_value()),
            "groupBy": lambda n : setattr(self, 'group_by', n.get_collection_of_primitive_values(str)),
            "orderBy": lambda n : setattr(self, 'order_by', n.get_collection_of_primitive_values(str)),
            "reportName": lambda n : setattr(self, 'report_name', n.get_enum_value(CloudPCPerformanceReportName)),
            "search": lambda n : setattr(self, 'search', n.get_str_value()),
            "select": lambda n : setattr(self, 'select', n.get_collection_of_primitive_values(str)),
            "skip": lambda n : setattr(self, 'skip', n.get_int_value()),
            "top": lambda n : setattr(self, 'top', n.get_int_value()),
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
        writer.write_str_value("filter", self.filter)
        writer.write_collection_of_primitive_values("groupBy", self.group_by)
        writer.write_collection_of_primitive_values("orderBy", self.order_by)
        writer.write_enum_value("reportName", self.report_name)
        writer.write_str_value("search", self.search)
        writer.write_collection_of_primitive_values("select", self.select)
        writer.write_int_value("skip", self.skip)
        writer.write_int_value("top", self.top)
        writer.write_additional_data_value(self.additional_data)
    

