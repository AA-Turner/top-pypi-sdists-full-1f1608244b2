"""Writer entity."""

from abc import ABC, abstractmethod
from functools import reduce
from typing import Any, Callable, Dict, List, Optional

from pyspark.sql.dataframe import DataFrame

from butterfree.clients import SparkClient
from butterfree.configs.db import AbstractWriteConfig
from butterfree.hooks import HookableComponent
from butterfree.metadata.writer_metadata import WriterMetadata
from butterfree.transform import FeatureSet


class Writer(ABC, HookableComponent):
    """Abstract base class for Writers.

    Args:
        spark_client: client for spark connections with external services.

    """

    def __init__(
        self,
        db_config: AbstractWriteConfig,
        debug_mode: Optional[bool] = False,
        interval_mode: Optional[bool] = False,
        write_to_entity: Optional[bool] = False,
        row_count_validation: Optional[bool] = True,
        merge_on: Optional[list] = None,
    ) -> None:
        super().__init__()
        self.db_config = db_config
        self.transformations: List[Dict[str, Any]] = []
        self.debug_mode = debug_mode
        self.interval_mode = interval_mode
        self.write_to_entity = write_to_entity
        self.row_count_validation = row_count_validation
        self.merge_on = merge_on

    def with_(
        self, transformer: Callable[..., DataFrame], *args: Any, **kwargs: Any
    ) -> "Writer":
        """Define a new transformation for the Writer.

        All the transformations are used when the method consume is called.

        Args:
            transformer: method that receives a dataframe and output a
                dataframe.
            *args: args for the transformer.
            **kwargs: kwargs for the transformer.

        Returns:
            Reader object with new transformation

        """
        new_transformation = {
            "transformer": transformer,
            "args": args if args else (),
            "kwargs": kwargs if kwargs else {},
        }
        self.transformations.append(new_transformation)
        return self

    def _apply_transformations(self, df: DataFrame) -> DataFrame:
        return reduce(
            lambda result_df, transformation: transformation["transformer"](
                result_df, *transformation["args"], **transformation["kwargs"]
            ),
            self.transformations,
            df,
        )

    @abstractmethod
    def write(
        self,
        feature_set: FeatureSet,
        dataframe: DataFrame,
        spark_client: SparkClient,
    ) -> Any:
        """Loads the data from a feature set into the Feature Store.

        Feature Store could be Online or Historical.

        Args:
            feature_set: object processed with feature set metadata.
            dataframe: Spark dataframe containing data from a feature set.
            spark_client: client for Spark connections with external services.

        """

    @abstractmethod
    def check_schema(
        self,
        client: Any,
        dataframe: DataFrame,
        table_name: str,
        database: Optional[str] = None,
    ) -> DataFrame:
        """Instantiate the schema check hook to check schema between dataframe and database.

        Args:
            client: client for Spark or Cassandra connections with external services.
            dataframe: Spark dataframe containing data from a feature set.
            table_name: table name where the dataframe will be saved.
            database: database name where the dataframe will be saved.
        """

    @abstractmethod
    def validate(
        self, feature_set: FeatureSet, dataframe: DataFrame, spark_client: SparkClient
    ) -> Any:
        """Calculate dataframe rows to validate data into Feature Store.

        Args:
            feature_set: object processed with feature set metadata.
            dataframe: Spark dataframe containing data from a feature set.
            spark_client: client for Spark connections with external services.

        Raises:
            AssertionError: if validation fails.

        """

    def build_metadata(self) -> WriterMetadata:
        """Get the writer's metadata as a Pydantic model.

        This method creates a standardized representation of writer metadata
        that can be used for documentation, validation, and serialization purposes.

        Returns:
            A BaseWriterMetadata model containing the writer's metadata
        """

        writer_metadata = WriterMetadata(
            type=self.__class__.__name__,
            interval_mode=self.interval_mode,
            write_to_entity=self.write_to_entity,
            db_config=self.db_config.__class__.__name__,
        )

        return writer_metadata
