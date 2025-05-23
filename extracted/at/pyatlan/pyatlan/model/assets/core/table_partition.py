# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 Atlan Pte. Ltd.


from __future__ import annotations

from typing import ClassVar, Dict, List, Optional, overload

from pydantic.v1 import Field, validator

from pyatlan.model.enums import AtlanConnectorType
from pyatlan.model.fields.atlan_fields import (
    BooleanField,
    KeywordField,
    NumericField,
    RelationField,
    TextField,
)
from pyatlan.utils import init_guid, validate_required_fields

from .s_q_l import SQL


class TablePartition(SQL):
    """Description"""

    @overload
    @classmethod
    def creator(
        cls,
        *,
        name: str,
        table_qualified_name: str,
    ) -> TablePartition:
        """
        Builds the minimal object necessary to create a table partition.

        :param name: name of the table partition
        :param table_qualified_name: unique name of the table in which this table partition exists
        :returns: the minimal request necessary to create the table partition
        """

    @overload
    @classmethod
    def creator(
        cls,
        *,
        name: str,
        connection_qualified_name: str,
        database_name: str,
        database_qualified_name: str,
        schema_name: str,
        schema_qualified_name: str,
        table_name: str,
        table_qualified_name: str,
    ) -> TablePartition:
        """
        Builds the minimal object necessary to create a table partition.

        :param name: name of the TablePartition
        :param connection_qualified_name: unique name of the connection in which to create the TablePartition
        :param database_name: simple name of the Database in which to create the TablePartition
        :param database_qualified_name: unique name of the Database in which to create the TablePartition
        :param schema_name: simple name of the Schema in which to create the TablePartition
        :param schema_qualified_name: unique name of the Schema in which to create the TablePartition
        :param table_name: simple name of the Table in which to create the TablePartition
        :param table_qualified_name: unique name of the table in which this table partition exists
        :returns: the minimal request necessary to create the table partition
        """

    @classmethod
    @init_guid
    def creator(
        cls,
        *,
        name: str,
        connection_qualified_name: Optional[str] = None,
        database_name: Optional[str] = None,
        database_qualified_name: Optional[str] = None,
        schema_name: Optional[str] = None,
        schema_qualified_name: Optional[str] = None,
        table_name: Optional[str] = None,
        table_qualified_name: str,
    ) -> TablePartition:
        """
        Builds the minimal object necessary to create a table partition.

        :param name: name of the TablePartition
        :param connection_qualified_name: unique name of the connection in which to create the TablePartition
        :param database_name: simple name of the Database in which to create the TablePartition
        :param database_qualified_name: unique name of the Database in which to create the TablePartition
        :param schema_name: simple name of the Schema in which to create the TablePartition
        :param schema_qualified_name: unique name of the Schema in which to create the TablePartition
        :param table_name: simple name of the Table in which to create the TablePartition
        :param table_qualified_name: unique name of the table in which this table partition exists
        :returns: the minimal request necessary to create the table partition
        """
        attributes = TablePartition.Attributes.creator(
            name=name,
            connection_qualified_name=connection_qualified_name,
            database_name=database_name,
            database_qualified_name=database_qualified_name,
            schema_name=schema_name,
            schema_qualified_name=schema_qualified_name,
            table_name=table_name,
            table_qualified_name=table_qualified_name,
        )
        return cls(attributes=attributes)

    type_name: str = Field(default="TablePartition", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "TablePartition":
            raise ValueError("must be TablePartition")
        return v

    def __setattr__(self, name, value):
        if name in TablePartition._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    CONSTRAINT: ClassVar[TextField] = TextField("constraint", "constraint")
    """
    Constraint that defines this table partition.
    """
    COLUMN_COUNT: ClassVar[NumericField] = NumericField("columnCount", "columnCount")
    """
    Number of columns in this partition.
    """
    ROW_COUNT: ClassVar[NumericField] = NumericField("rowCount", "rowCount")
    """
    Number of rows in this partition.
    """
    SIZE_BYTES: ClassVar[NumericField] = NumericField("sizeBytes", "sizeBytes")
    """
    Size of this partition, in bytes.
    """
    ALIAS: ClassVar[TextField] = TextField("alias", "alias")
    """
    Alias for this partition.
    """
    IS_TEMPORARY: ClassVar[BooleanField] = BooleanField("isTemporary", "isTemporary")
    """
    Whether this partition is temporary (true) or not (false).
    """
    IS_QUERY_PREVIEW: ClassVar[BooleanField] = BooleanField(
        "isQueryPreview", "isQueryPreview"
    )
    """
    Whether preview queries for this partition are allowed (true) or not (false).
    """
    QUERY_PREVIEW_CONFIG: ClassVar[KeywordField] = KeywordField(
        "queryPreviewConfig", "queryPreviewConfig"
    )
    """
    Configuration for the preview queries.
    """
    EXTERNAL_LOCATION: ClassVar[TextField] = TextField(
        "externalLocation", "externalLocation"
    )
    """
    External location of this partition, for example: an S3 object location.
    """
    EXTERNAL_LOCATION_REGION: ClassVar[TextField] = TextField(
        "externalLocationRegion", "externalLocationRegion"
    )
    """
    Region of the external location of this partition, for example: S3 region.
    """
    EXTERNAL_LOCATION_FORMAT: ClassVar[KeywordField] = KeywordField(
        "externalLocationFormat", "externalLocationFormat"
    )
    """
    Format of the external location of this partition, for example: JSON, CSV, PARQUET, etc.
    """
    IS_PARTITIONED: ClassVar[BooleanField] = BooleanField(
        "isPartitioned", "isPartitioned"
    )
    """
    Whether this partition is further partitioned (true) or not (false).
    """
    PARTITION_STRATEGY: ClassVar[KeywordField] = KeywordField(
        "partitionStrategy", "partitionStrategy"
    )
    """
    Partition strategy of this partition.
    """
    PARTITION_COUNT: ClassVar[NumericField] = NumericField(
        "partitionCount", "partitionCount"
    )
    """
    Number of sub-partitions of this partition.
    """
    PARTITION_LIST: ClassVar[TextField] = TextField("partitionList", "partitionList")
    """
    List of sub-partitions in this partition.
    """

    COLUMNS: ClassVar[RelationField] = RelationField("columns")
    """
    TBC
    """
    PARENT_TABLE: ClassVar[RelationField] = RelationField("parentTable")
    """
    TBC
    """
    CHILD_TABLE_PARTITIONS: ClassVar[RelationField] = RelationField(
        "childTablePartitions"
    )
    """
    TBC
    """
    PARENT_TABLE_PARTITION: ClassVar[RelationField] = RelationField(
        "parentTablePartition"
    )
    """
    TBC
    """

    _convenience_properties: ClassVar[List[str]] = [
        "constraint",
        "column_count",
        "row_count",
        "size_bytes",
        "alias",
        "is_temporary",
        "is_query_preview",
        "query_preview_config",
        "external_location",
        "external_location_region",
        "external_location_format",
        "is_partitioned",
        "partition_strategy",
        "partition_count",
        "partition_list",
        "columns",
        "parent_table",
        "child_table_partitions",
        "parent_table_partition",
    ]

    @property
    def constraint(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.constraint

    @constraint.setter
    def constraint(self, constraint: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.constraint = constraint

    @property
    def column_count(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.column_count

    @column_count.setter
    def column_count(self, column_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_count = column_count

    @property
    def row_count(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.row_count

    @row_count.setter
    def row_count(self, row_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.row_count = row_count

    @property
    def size_bytes(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.size_bytes = size_bytes

    @property
    def alias(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.alias

    @alias.setter
    def alias(self, alias: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.alias = alias

    @property
    def is_temporary(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_temporary

    @is_temporary.setter
    def is_temporary(self, is_temporary: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_temporary = is_temporary

    @property
    def is_query_preview(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_query_preview

    @is_query_preview.setter
    def is_query_preview(self, is_query_preview: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_query_preview = is_query_preview

    @property
    def query_preview_config(self) -> Optional[Dict[str, str]]:
        return None if self.attributes is None else self.attributes.query_preview_config

    @query_preview_config.setter
    def query_preview_config(self, query_preview_config: Optional[Dict[str, str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.query_preview_config = query_preview_config

    @property
    def external_location(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.external_location

    @external_location.setter
    def external_location(self, external_location: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.external_location = external_location

    @property
    def external_location_region(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.external_location_region
        )

    @external_location_region.setter
    def external_location_region(self, external_location_region: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.external_location_region = external_location_region

    @property
    def external_location_format(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.external_location_format
        )

    @external_location_format.setter
    def external_location_format(self, external_location_format: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.external_location_format = external_location_format

    @property
    def is_partitioned(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_partitioned

    @is_partitioned.setter
    def is_partitioned(self, is_partitioned: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_partitioned = is_partitioned

    @property
    def partition_strategy(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.partition_strategy

    @partition_strategy.setter
    def partition_strategy(self, partition_strategy: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.partition_strategy = partition_strategy

    @property
    def partition_count(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.partition_count

    @partition_count.setter
    def partition_count(self, partition_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.partition_count = partition_count

    @property
    def partition_list(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.partition_list

    @partition_list.setter
    def partition_list(self, partition_list: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.partition_list = partition_list

    @property
    def columns(self) -> Optional[List[Column]]:
        return None if self.attributes is None else self.attributes.columns

    @columns.setter
    def columns(self, columns: Optional[List[Column]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.columns = columns

    @property
    def parent_table(self) -> Optional[Table]:
        return None if self.attributes is None else self.attributes.parent_table

    @parent_table.setter
    def parent_table(self, parent_table: Optional[Table]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.parent_table = parent_table

    @property
    def child_table_partitions(self) -> Optional[List[TablePartition]]:
        return (
            None if self.attributes is None else self.attributes.child_table_partitions
        )

    @child_table_partitions.setter
    def child_table_partitions(
        self, child_table_partitions: Optional[List[TablePartition]]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.child_table_partitions = child_table_partitions

    @property
    def parent_table_partition(self) -> Optional[TablePartition]:
        return (
            None if self.attributes is None else self.attributes.parent_table_partition
        )

    @parent_table_partition.setter
    def parent_table_partition(self, parent_table_partition: Optional[TablePartition]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.parent_table_partition = parent_table_partition

    class Attributes(SQL.Attributes):
        constraint: Optional[str] = Field(default=None, description="")
        column_count: Optional[int] = Field(default=None, description="")
        row_count: Optional[int] = Field(default=None, description="")
        size_bytes: Optional[int] = Field(default=None, description="")
        alias: Optional[str] = Field(default=None, description="")
        is_temporary: Optional[bool] = Field(default=None, description="")
        is_query_preview: Optional[bool] = Field(default=None, description="")
        query_preview_config: Optional[Dict[str, str]] = Field(
            default=None, description=""
        )
        external_location: Optional[str] = Field(default=None, description="")
        external_location_region: Optional[str] = Field(default=None, description="")
        external_location_format: Optional[str] = Field(default=None, description="")
        is_partitioned: Optional[bool] = Field(default=None, description="")
        partition_strategy: Optional[str] = Field(default=None, description="")
        partition_count: Optional[int] = Field(default=None, description="")
        partition_list: Optional[str] = Field(default=None, description="")
        columns: Optional[List[Column]] = Field(
            default=None, description=""
        )  # relationship
        parent_table: Optional[Table] = Field(
            default=None, description=""
        )  # relationship
        child_table_partitions: Optional[List[TablePartition]] = Field(
            default=None, description=""
        )  # relationship
        parent_table_partition: Optional[TablePartition] = Field(
            default=None, description=""
        )  # relationship

        @classmethod
        @init_guid
        def creator(
            cls,
            *,
            name: str,
            connection_qualified_name: Optional[str] = None,
            database_name: Optional[str] = None,
            database_qualified_name: Optional[str] = None,
            schema_name: Optional[str] = None,
            schema_qualified_name: Optional[str] = None,
            table_name: Optional[str] = None,
            table_qualified_name: str,
        ) -> TablePartition.Attributes:
            """
            Builds the minimal object necessary to create a table partition.

            :param name: name of the TablePartition
            :param connection_qualified_name: unique name of the connection in which to create the TablePartition
            :param database_name: simple name of the Database in which to create the TablePartition
            :param database_qualified_name: unique name of the Database in which to create the TablePartition
            :param schema_name: simple name of the Schema in which to create the TablePartition
            :param schema_qualified_name: unique name of the Schema in which to create the TablePartition
            :param table_name: simple name of the Table in which to create the TablePartition
            :param table_qualified_name: unique name of the table in which this table partition exists
            :returns: the minimal request necessary to create the table partition
            """
            validate_required_fields(
                ["name", "table_qualified_name"],
                [name, table_qualified_name],
            )
            assert table_qualified_name  # noqa: S101
            if connection_qualified_name:
                connector_name = AtlanConnectorType.get_connector_name(
                    connection_qualified_name
                )
            else:
                connection_qn, connector_name = AtlanConnectorType.get_connector_name(
                    table_qualified_name, "table_qualified_name", 6
                )

            fields = table_qualified_name.split("/")

            connection_qualified_name = connection_qualified_name or connection_qn
            database_name = database_name or fields[3]
            schema_name = schema_name or fields[4]
            table_name = table_name or fields[5]
            database_qualified_name = (
                database_qualified_name
                or f"{connection_qualified_name}/{database_name}"
            )
            schema_qualified_name = (
                schema_qualified_name or f"{database_qualified_name}/{schema_name}"
            )

            qualified_name = f"{schema_qualified_name}/{name}"

            return TablePartition.Attributes(
                name=name,
                qualified_name=qualified_name,
                database_name=database_name,
                database_qualified_name=database_qualified_name,
                schema_name=schema_name,
                schema_qualified_name=schema_qualified_name,
                connector_name=connector_name,
                connection_qualified_name=connection_qualified_name,
                table_name=table_name,
                table_qualified_name=table_qualified_name,
            )

    attributes: TablePartition.Attributes = Field(
        default_factory=lambda: TablePartition.Attributes(),
        description=(
            "Map of attributes in the instance and their values. "
            "The specific keys of this map will vary by type, "
            "so are described in the sub-types of this schema."
        ),
    )


from .column import Column  # noqa: E402, F401
from .table import Table  # noqa: E402, F401
