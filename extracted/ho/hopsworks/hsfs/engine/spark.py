#
#   Copyright 2020 Logical Clocks AB
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
from __future__ import annotations

import copy
import json
import os
import re
import shutil
import uuid
import warnings
from datetime import date, datetime, timezone
from typing import TYPE_CHECKING, Any, Dict, List, Optional, TypeVar, Union


if TYPE_CHECKING:
    import great_expectations
    from pyspark.rdd import RDD
    from pyspark.sql import DataFrame

import pandas as pd
import tzlocal
from hopsworks_common.core.constants import HAS_NUMPY, HAS_PANDAS
from hsfs.constructor import query
from hsfs.core import feature_group_api

# in case importing in %%local
from hsfs.core.vector_db_client import VectorDbClient


if HAS_NUMPY:
    import numpy as np


try:
    import pyspark
    from pyspark import SparkFiles
    from pyspark.rdd import RDD
    from pyspark.sql import DataFrame, SparkSession, SQLContext
    from pyspark.sql.avro.functions import from_avro, to_avro
    from pyspark.sql.functions import (
        array,
        col,
        concat,
        from_json,
        lit,
        struct,
        udf,
    )
    from pyspark.sql.types import (
        ArrayType,
        BinaryType,
        BooleanType,
        ByteType,
        DateType,
        DecimalType,
        DoubleType,
        FloatType,
        IntegerType,
        LongType,
        ShortType,
        StringType,
        StructField,
        StructType,
        TimestampType,
    )

    if pd.__version__ >= "2.0.0" and pyspark.__version__ < "3.2.3":

        def iteritems(self):
            return self.items()

        pd.DataFrame.iteritems = iteritems
except ImportError:
    pass

from hopsworks_common import client
from hopsworks_common.client.exceptions import FeatureStoreException
from hsfs import (
    feature,
    feature_view,
    training_dataset,
    training_dataset_feature,
    transformation_function,
    util,
)
from hsfs import feature_group as fg_mod
from hsfs.core import (
    dataset_api,
    delta_engine,
    hudi_engine,
    kafka_engine,
    transformation_function_engine,
)
from hsfs.core.constants import HAS_AVRO, HAS_GREAT_EXPECTATIONS
from hsfs.decorators import uses_great_expectations
from hsfs.storage_connector import StorageConnector
from hsfs.training_dataset_split import TrainingDatasetSplit


if HAS_GREAT_EXPECTATIONS:
    import great_expectations

if HAS_AVRO:
    import avro


class Engine:
    HIVE_FORMAT = "hive"
    KAFKA_FORMAT = "kafka"

    APPEND = "append"
    OVERWRITE = "overwrite"

    def __init__(self):
        self._spark_session = SparkSession.builder.enableHiveSupport().getOrCreate()
        self._spark_context = self._spark_session.sparkContext
        # self._spark_context.setLogLevel("DEBUG")
        self._jvm = self._spark_context._jvm

        self._spark_session.conf.set("hive.exec.dynamic.partition", "true")
        self._spark_session.conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
        self._spark_session.conf.set("spark.sql.hive.convertMetastoreParquet", "false")
        self._spark_session.conf.set("spark.sql.session.timeZone", "UTC")
        self._dataset_api = dataset_api.DatasetApi()

    def sql(
        self,
        sql_query,
        feature_store,
        connector,
        dataframe_type,
        read_options,
        schema=None,
    ):
        if not connector:
            result_df = self._sql_offline(sql_query, feature_store)
        else:
            result_df = connector.read(sql_query, None, {}, None)

        self.set_job_group("", "")
        return self._return_dataframe_type(result_df, dataframe_type)

    def is_flyingduck_query_supported(self, query, read_options=None):
        return False  # we do not support flyingduck on pyspark clients

    def _sql_offline(self, sql_query, feature_store):
        # set feature store
        self._spark_session.sql("USE {}".format(feature_store))
        return self._spark_session.sql(sql_query)

    def show(self, sql_query, feature_store, n, online_conn, read_options=None):
        return self.sql(
            sql_query, feature_store, online_conn, "default", read_options
        ).show(n)

    def read_vector_db(
        self,
        feature_group: fg_mod.FeatureGroup,
        n: int = None,
        dataframe_type: str = "default",
    ) -> Union[
        pd.DataFrame, np.ndarray, List[List[Any]], TypeVar("pyspark.sql.DataFrame")
    ]:
        results = VectorDbClient.read_feature_group(feature_group, n)
        feature_names = [f.name for f in feature_group.features]
        dataframe_type = dataframe_type.lower()
        if dataframe_type in ["default", "spark"]:
            if len(results) == 0:
                return self._spark_session.createDataFrame(
                    self._spark_session.sparkContext.emptyRDD(), StructType()
                )
            else:
                return self._spark_session.createDataFrame(results, feature_names)
        else:
            df = pd.DataFrame(results, columns=feature_names, index=None)
            return self._return_dataframe_type(df, dataframe_type)

    def set_job_group(self, group_id, description):
        self._spark_session.sparkContext.setJobGroup(group_id, description)

    def register_external_temporary_table(self, external_fg, alias):
        if not isinstance(external_fg, fg_mod.SpineGroup):
            external_dataset = external_fg.storage_connector.read(
                external_fg.query,
                external_fg.data_format,
                external_fg.options,
                external_fg.storage_connector._get_path(
                    external_fg.path
                ),  # cant rely on location since this method can be used before FG is saved
            )
        else:
            external_dataset = external_fg.dataframe

        external_dataset.createOrReplaceTempView(alias)
        return external_dataset

    def register_hudi_temporary_table(
        self, hudi_fg_alias, feature_store_id, feature_store_name, read_options
    ):
        hudi_engine_instance = hudi_engine.HudiEngine(
            feature_store_id,
            feature_store_name,
            hudi_fg_alias.feature_group,
            self._spark_context,
            self._spark_session,
        )

        hudi_engine_instance.register_temporary_table(
            hudi_fg_alias,
            read_options,
        )

        self.reconcile_schema(hudi_fg_alias, read_options, hudi_engine_instance)

    def register_delta_temporary_table(
        self, delta_fg_alias, feature_store_id, feature_store_name, read_options
    ):
        delta_engine_instance = delta_engine.DeltaEngine(
            feature_store_id,
            feature_store_name,
            delta_fg_alias.feature_group,
            self._spark_session,
            self._spark_context,
        )

        delta_engine_instance.register_temporary_table(
            delta_fg_alias,
            read_options,
        )

        self.reconcile_schema(delta_fg_alias, read_options, delta_engine_instance)

    def reconcile_schema(self, fg_alias, read_options, engine_instance):
        if sorted(self._spark_session.table(fg_alias.alias).columns) != sorted(
            [feature.name for feature in fg_alias.feature_group._features]
            + hudi_engine.HudiEngine.HUDI_SPEC_FEATURE_NAMES
            if fg_alias.feature_group.time_travel_format == "HUDI"
            else []
        ):
            full_fg = feature_group_api.FeatureGroupApi().get(
                feature_store_id=fg_alias.feature_group._feature_store_id,
                name=fg_alias.feature_group.name,
                version=fg_alias.feature_group.version,
            )

            self.update_table_schema(full_fg)

            engine_instance.register_temporary_table(
                fg_alias,
                read_options,
            )

    def _return_dataframe_type(self, dataframe, dataframe_type):
        if dataframe_type.lower() in ["default", "spark"]:
            return dataframe

        # Converting to pandas dataframe if return type is not spark
        if isinstance(dataframe, DataFrame):
            dataframe = dataframe.toPandas()

        if dataframe_type.lower() == "pandas":
            return dataframe
        if dataframe_type.lower() == "numpy":
            return dataframe.values
        if dataframe_type.lower() == "python":
            return dataframe.values.tolist()

        raise TypeError(
            "Dataframe type `{}` not supported on this platform.".format(dataframe_type)
        )

    def convert_to_default_dataframe(self, dataframe):
        if isinstance(dataframe, list):
            dataframe = self.convert_list_to_spark_dataframe(dataframe)
        elif HAS_NUMPY and isinstance(dataframe, np.ndarray):
            dataframe = self.convert_numpy_to_spark_dataframe(dataframe)
        elif HAS_PANDAS and isinstance(dataframe, pd.DataFrame):
            dataframe = self.convert_pandas_to_spark_dataframe(dataframe)
        elif isinstance(dataframe, RDD):
            dataframe = dataframe.toDF()

        if isinstance(dataframe, DataFrame):
            upper_case_features = [
                c for c in dataframe.columns if util.contains_uppercase(c)
            ]
            space_features = [
                c for c in dataframe.columns if util.contains_whitespace(c)
            ]
            if len(upper_case_features) > 0:
                warnings.warn(
                    "The ingested dataframe contains upper case letters in feature names: `{}`. "
                    "Feature names are sanitized to lower case in the feature store.".format(
                        upper_case_features
                    ),
                    util.FeatureGroupWarning,
                    stacklevel=1,
                )
            if len(space_features) > 0:
                warnings.warn(
                    "The ingested dataframe contains feature names with spaces: `{}`. "
                    "Feature names are sanitized to use underscore '_' in the feature store.".format(
                        space_features
                    ),
                    util.FeatureGroupWarning,
                    stacklevel=1,
                )

            lowercase_dataframe = dataframe.select(
                [col(x).alias(util.autofix_feature_name(x)) for x in dataframe.columns]
            )
            # for streaming dataframes this will be handled in DeltaStreamerTransformer.java class
            if not lowercase_dataframe.isStreaming:
                nullable_schema = copy.deepcopy(lowercase_dataframe.schema)
                for struct_field in nullable_schema:
                    struct_field.nullable = True
                lowercase_dataframe = self._spark_session.createDataFrame(
                    lowercase_dataframe.rdd, nullable_schema
                )

            return lowercase_dataframe
        if dataframe == "spine":
            return None

        raise TypeError(
            "The provided dataframe type is not recognized. Supported types are: spark rdds, spark dataframes, "
            "pandas dataframes, python 2D lists, and numpy 2D arrays. The provided dataframe has type: {}".format(
                type(dataframe)
            )
        )

    @staticmethod
    def utc_disguised_as_local(dt):
        local_tz = tzlocal.get_localzone()
        utc = timezone.utc
        if not dt.tzinfo:
            dt = dt.replace(tzinfo=utc)
        return dt.astimezone(utc).replace(tzinfo=local_tz)

    def convert_list_to_spark_dataframe(self, dataframe):
        if HAS_NUMPY:
            return self.convert_numpy_to_spark_dataframe(np.array(dataframe))
        try:
            dataframe[0][0]
        except TypeError:
            raise TypeError(
                "Cannot convert a list that has less than two dimensions to a dataframe."
            ) from None
        ok = False
        try:
            dataframe[0][0][0]
        except TypeError:
            ok = True
        if not ok:
            raise TypeError(
                "Cannot convert a list that has more than two dimensions to a dataframe."
            ) from None
        num_cols = len(dataframe[0])
        if HAS_PANDAS:
            dataframe_dict = {}
            for n_col in range(num_cols):
                c = "col_" + str(n_col)
                dataframe_dict[c] = [dataframe[i][n_col] for i in range(len(dataframe))]
            return self.convert_pandas_to_spark_dataframe(pd.DataFrame(dataframe_dict))
        for i in range(len(dataframe)):
            dataframe[i] = [
                self.utc_disguised_as_local(d) if isinstance(d, datetime) else d
                for d in dataframe[i]
            ]
        return self._spark_session.createDataFrame(
            dataframe, ["col_" + str(n) for n in range(num_cols)]
        )

    def convert_numpy_to_spark_dataframe(self, dataframe):
        if dataframe.ndim != 2:
            raise TypeError(
                "Cannot convert numpy array that do not have two dimensions to a dataframe. "
                "The number of dimensions are: {}".format(dataframe.ndim)
            )
        num_cols = dataframe.shape[1]
        if HAS_PANDAS:
            dataframe_dict = {}
            for n_col in range(num_cols):
                c = "col_" + str(n_col)
                dataframe_dict[c] = dataframe[:, n_col]
            return self.convert_pandas_to_spark_dataframe(pd.DataFrame(dataframe_dict))
        # convert timestamps to current timezone
        for n_col in range(num_cols):
            if dataframe[:, n_col].dtype == np.dtype("datetime64[ns]"):
                # set the timezone to the client's timezone because that is
                # what spark expects.
                dataframe[:, n_col] = np.array(
                    [self.utc_disguised_as_local(d.item()) for d in dataframe[:, n_col]]
                )
        return self._spark_session.createDataFrame(
            dataframe.tolist(), ["col_" + str(n) for n in range(num_cols)]
        )

    def convert_pandas_to_spark_dataframe(self, dataframe):
        # convert timestamps to current timezone
        local_tz = tzlocal.get_localzone()
        # make shallow copy so the original df does not get changed
        dataframe_copy = dataframe.copy(deep=False)
        for c in dataframe_copy.columns:
            if isinstance(
                dataframe_copy[c].dtype, pd.core.dtypes.dtypes.DatetimeTZDtype
            ):
                # convert to utc timestamp
                dataframe_copy[c] = dataframe_copy[c].dt.tz_convert(None)
            if HAS_NUMPY and dataframe_copy[c].dtype == np.dtype("datetime64[ns]"):
                # set the timezone to the client's timezone because that is
                # what spark expects.
                dataframe_copy[c] = dataframe_copy[c].dt.tz_localize(
                    str(local_tz), ambiguous="infer", nonexistent="shift_forward"
                )
        return self._spark_session.createDataFrame(dataframe_copy)

    def save_dataframe(
        self,
        feature_group,
        dataframe,
        operation,
        online_enabled,
        storage,
        offline_write_options,
        online_write_options,
        validation_id=None,
    ):
        try:
            if (
                isinstance(feature_group, fg_mod.ExternalFeatureGroup)
                and feature_group.online_enabled
            ) or feature_group.stream:
                self._save_online_dataframe(
                    feature_group, dataframe, online_write_options
                )
            else:
                if storage == "offline" or not online_enabled:
                    self._save_offline_dataframe(
                        feature_group,
                        dataframe,
                        operation,
                        offline_write_options,
                        validation_id,
                    )
                elif storage == "online":
                    self._save_online_dataframe(
                        feature_group, dataframe, online_write_options
                    )
                elif online_enabled and storage is None:
                    self._save_offline_dataframe(
                        feature_group,
                        dataframe,
                        operation,
                        offline_write_options,
                    )
                    self._save_online_dataframe(
                        feature_group, dataframe, online_write_options
                    )
        except Exception as e:
            raise FeatureStoreException(e).with_traceback(e.__traceback__) from e

    def save_stream_dataframe(
        self,
        feature_group: Union[fg_mod.FeatureGroup, fg_mod.ExternalFeatureGroup],
        dataframe,
        query_name,
        output_mode,
        await_termination: bool,
        timeout,
        checkpoint_dir: Optional[str],
        write_options: Optional[Dict[str, Any]],
    ):
        write_options = kafka_engine.get_kafka_config(
            feature_group.feature_store_id, write_options, engine="spark"
        )
        serialized_df = self._serialize_to_avro(feature_group, dataframe)

        if query_name is None:
            query_name = (
                f"insert_stream_{feature_group.feature_store.project_id}_{feature_group._id}"
                f"_{feature_group.name}_{feature_group.version}_onlinefs"
            )

        query = (
            serialized_df.withColumn("headers", self._get_headers(feature_group))
            .writeStream.outputMode(output_mode)
            .format(self.KAFKA_FORMAT)
            .option(
                "checkpointLocation",
                "/Projects/"
                + client.get_instance()._project_name
                + "/Resources/"
                + query_name
                + "-checkpoint"
                if checkpoint_dir is None
                else checkpoint_dir,
            )
            .options(**write_options)
            .option("topic", feature_group._online_topic_name)
            .queryName(query_name)
            .start()
        )

        if await_termination:
            query.awaitTermination(timeout)

            # wait for online ingestion
            if feature_group.online_enabled and write_options.get(
                "wait_for_online_ingestion", False
            ):
                feature_group.get_latest_online_ingestion().wait_for_completion(
                    options=write_options.get("online_ingestion_options", {})
                )

        return query

    def _save_offline_dataframe(
        self,
        feature_group,
        dataframe,
        operation,
        write_options,
        validation_id=None,
    ):
        if feature_group.time_travel_format == "HUDI":
            hudi_engine_instance = hudi_engine.HudiEngine(
                feature_group.feature_store_id,
                feature_group.feature_store_name,
                feature_group,
                self._spark_session,
                self._spark_context,
            )

            hudi_engine_instance.save_hudi_fg(
                dataframe, self.APPEND, operation, write_options, validation_id
            )
        elif feature_group.time_travel_format == "DELTA":
            delta_engine_instance = delta_engine.DeltaEngine(
                feature_group.feature_store_id,
                feature_group.feature_store_name,
                feature_group,
                self._spark_session,
                self._spark_context,
            )
            delta_engine_instance.save_delta_fg(dataframe, write_options, validation_id)
        else:
            dataframe.write.format(self.HIVE_FORMAT).mode(self.APPEND).options(
                **write_options
            ).partitionBy(
                feature_group.partition_key if feature_group.partition_key else []
            ).saveAsTable(feature_group._get_table_name())

    def _save_online_dataframe(self, feature_group, dataframe, write_options):
        write_options = kafka_engine.get_kafka_config(
            feature_group.feature_store_id, write_options, engine="spark"
        )

        serialized_df = self._serialize_to_avro(feature_group, dataframe)

        (
            serialized_df.withColumn(
                "headers", self._get_headers(feature_group, dataframe.count())
            )
            .write.format(self.KAFKA_FORMAT)
            .options(**write_options)
            .option("topic", feature_group._online_topic_name)
            .save()
        )

        # wait for online ingestion
        if feature_group.online_enabled and write_options.get(
            "wait_for_online_ingestion", False
        ):
            feature_group.get_latest_online_ingestion().wait_for_completion(
                options=write_options.get("online_ingestion_options", {})
            )

    def _get_headers(
        self,
        feature_group: Union[fg_mod.FeatureGroup, fg_mod.ExternalFeatureGroup],
        num_entries: Optional[int] = None,
    ) -> array:
        return array(
            *[
                struct(lit(key).alias("key"), lit(value).alias("value"))
                for key, value in kafka_engine.get_headers(
                    feature_group, num_entries
                ).items()
            ]
        )

    def _serialize_to_avro(
        self,
        feature_group: Union[fg_mod.FeatureGroup, fg_mod.ExternalFeatureGroup],
        dataframe: Union[RDD, DataFrame],
    ):
        """Encodes all complex type features to binary using their avro type as schema."""
        encoded_dataframe = dataframe.select(
            [
                field["name"]
                if field["name"] not in feature_group.get_complex_features()
                else to_avro(
                    field["name"], feature_group._get_feature_avro_schema(field["name"])
                ).alias(field["name"])
                for field in json.loads(feature_group.avro_schema)["fields"]
            ]
        )

        """Packs all features into named struct to be serialized to single avro/binary
        column. And packs primary key into arry to be serialized for partitioning.
        """
        return encoded_dataframe.select(
            [
                # be aware: primary_key array should always be sorted
                to_avro(
                    concat(
                        *[
                            col(f).cast("string")
                            for f in sorted(feature_group.primary_key)
                        ]
                    )
                ).alias("key"),
                to_avro(
                    struct(
                        [
                            field["name"]
                            for field in json.loads(feature_group.avro_schema)["fields"]
                        ]
                    ),
                    feature_group._get_encoded_avro_schema(),
                ).alias("value"),
            ]
        )

    def _deserialize_from_avro(
        self,
        feature_group: Union[fg_mod.FeatureGroup, fg_mod.ExternalFeatureGroup],
        dataframe: Union[RDD, DataFrame],
    ):
        """
        Deserializes 'value' column from binary using avro schema and unpacks it into columns.
        """
        decoded_dataframe = dataframe.select(
            from_avro("value", feature_group._get_encoded_avro_schema()).alias("value")
        ).select(col("value.*"))

        """Decodes all complex type features from binary using their avro type as schema."""
        return decoded_dataframe.select(
            [
                field["name"]
                if field["name"] not in feature_group.get_complex_features()
                else from_avro(
                    field["name"], feature_group._get_feature_avro_schema(field["name"])
                ).alias(field["name"])
                for field in json.loads(feature_group.avro_schema)["fields"]
            ]
        )

    def get_training_data(
        self,
        training_dataset: training_dataset.TrainingDataset,
        feature_view_obj: feature_view.FeatureView,
        query_obj: query.Query,
        read_options: Dict[str, Any],
        dataframe_type: str,
        training_dataset_version: int = None,
        transformation_context: Dict[str, Any] = None,
    ):
        """
        Function that creates or retrieves already created the training dataset.

        # Arguments
            training_dataset_obj `TrainingDataset`: The training dataset metadata object.
            feature_view_obj `FeatureView`: The feature view object for the which the training data is being created.
            query_obj `Query`: The query object that contains the query used to create the feature view.
            read_options `Dict[str, Any]`: Dictionary that can be used to specify extra parameters for reading data.
            dataframe_type `str`: The type of dataframe returned.
            training_dataset_version `int`: Version of training data to be retrieved.
            transformation_context: `Dict[str, Any]` A dictionary mapping variable names to objects that will be provided as contextual information to the transformation function at runtime.
                These variables must be explicitly defined as parameters in the transformation function to be accessible during execution. If no context variables are provided, this parameter defaults to `None`.
        # Raises
            `ValueError`: If the training dataset statistics could not be retrieved.
        """
        return self.write_training_dataset(
            training_dataset,
            query_obj,
            read_options,
            None,
            read_options=read_options,
            to_df=True,
            feature_view_obj=feature_view_obj,
            training_dataset_version=training_dataset_version,
            transformation_context=transformation_context,
        )

    def split_labels(self, df, labels, dataframe_type):
        if labels:
            if isinstance(df, pd.DataFrame):
                labels_df = df[labels]
                df_new = df.drop(columns=labels)
            else:
                labels_df = df.select(*labels)
                df_new = df.drop(*labels)
            return (
                self._return_dataframe_type(df_new, dataframe_type),
                self._return_dataframe_type(labels_df, dataframe_type),
            )
        else:
            return self._return_dataframe_type(df, dataframe_type), None

    def drop_columns(self, df, drop_cols):
        return df.drop(*drop_cols)

    def write_training_dataset(
        self,
        training_dataset: training_dataset.TrainingDataset,
        query_obj: query.Query,
        user_write_options: Dict[str, Any],
        save_mode: str,
        read_options: Dict[str, Any] = None,
        feature_view_obj: feature_view.FeatureView = None,
        to_df: bool = False,
        training_dataset_version: Optional[int] = None,
        transformation_context: Dict[str, Any] = None,
    ):
        """
        Function that creates or retrieves already created the training dataset.

        # Arguments
            training_dataset `TrainingDataset`: The training dataset metadata object.
            query_obj `Query`: The query object that contains the query used to create the feature view.
            user_write_options `Dict[str, Any]`: Dictionary that can be used to specify extra parameters for writing data using spark.
            save_mode `str`: Spark save mode to be used while writing data.
            read_options `Dict[str, Any]`: Dictionary that can be used to specify extra parameters for reading data.
            feature_view_obj `FeatureView`: The feature view object for the which the training data is being created.
            to_df `bool`: Return dataframe instead of writing the data.
            training_dataset_version `Optional[int]`: Version of training data to be retrieved.
            transformation_context: `Dict[str, Any]` A dictionary mapping variable names to objects that will be provided as contextual information to the transformation function at runtime.
                These variables must be explicitly defined as parameters in the transformation function to be accessible during execution. If no context variables are provided, this parameter defaults to `None`.
        # Raises
            `ValueError`: If the training dataset statistics could not be retrieved.
        """
        write_options = self.write_options(
            training_dataset.data_format, user_write_options
        )
        if read_options is None:
            read_options = {}

        if len(training_dataset.splits) == 0:
            if isinstance(query_obj, query.Query):
                dataset = self.convert_to_default_dataframe(
                    query_obj.read(read_options=read_options)
                )
            else:
                raise ValueError("Dataset should be a query.")

            # if training_dataset_version is None:
            transformation_function_engine.TransformationFunctionEngine.compute_and_set_feature_statistics(
                training_dataset, feature_view_obj, dataset
            )
            # else:
            #    transformation_function_engine.TransformationFunctionEngine.get_and_set_feature_statistics(
            #        training_dataset, feature_view_obj, training_dataset_version
            #    )

            if training_dataset.coalesce:
                dataset = dataset.coalesce(1)
            path = training_dataset.location + "/" + training_dataset.name
            return self._write_training_dataset_single(
                feature_view_obj.transformation_functions,
                dataset,
                training_dataset.storage_connector,
                training_dataset.data_format,
                write_options,
                save_mode,
                path,
                to_df=to_df,
                transformation_context=transformation_context,
            )
        else:
            split_dataset = self._split_df(
                query_obj, training_dataset, read_options=read_options
            )
            for key in split_dataset:
                if training_dataset.coalesce:
                    split_dataset[key] = split_dataset[key].coalesce(1)

                split_dataset[key] = split_dataset[key].cache()

            if training_dataset_version is None:
                transformation_function_engine.TransformationFunctionEngine.compute_and_set_feature_statistics(
                    training_dataset, feature_view_obj, split_dataset
                )
            else:
                transformation_function_engine.TransformationFunctionEngine.get_and_set_feature_statistics(
                    training_dataset, feature_view_obj, training_dataset_version
                )

            return self._write_training_dataset_splits(
                training_dataset,
                split_dataset,
                write_options,
                save_mode,
                to_df=to_df,
                transformation_functions=feature_view_obj.transformation_functions,
                transformation_context=transformation_context,
            )

    def _split_df(self, query_obj, training_dataset, read_options=None):
        if read_options is None:
            read_options = {}
        if (
            training_dataset.splits[0].split_type
            == TrainingDatasetSplit.TIME_SERIES_SPLIT
        ):
            event_time = query_obj._left_feature_group.event_time
            event_time_feature = [
                _feature
                for _feature in query_obj.features
                if (
                    _feature.name == event_time
                    and _feature._feature_group_id == query_obj._left_feature_group.id
                )
            ]

            if not event_time_feature:
                event_time_feature = query_obj._left_feature_group.__getattr__(
                    event_time
                )
                event_time_feature.use_fully_qualified_name = True

                query_obj.append_feature(event_time_feature)
                event_time = event_time_feature._get_fully_qualified_feature_name(
                    feature_group=query_obj._left_feature_group
                )

                return self._time_series_split(
                    training_dataset,
                    query_obj.read(read_options=read_options),
                    event_time,
                    drop_event_time=True,
                )
            else:
                # Use the fully qualified name of the event time feature if required
                event_time = event_time_feature[0]._get_fully_qualified_feature_name(
                    feature_group=query_obj._left_feature_group
                )

                return self._time_series_split(
                    training_dataset,
                    query_obj.read(read_options=read_options),
                    event_time,
                )
        else:
            return self._random_split(
                query_obj.read(read_options=read_options), training_dataset
            )

    def _random_split(self, dataset, training_dataset):
        splits = [(split.name, split.percentage) for split in training_dataset.splits]
        split_weights = [split[1] for split in splits]
        split_dataset = dataset.randomSplit(split_weights, training_dataset.seed)
        return dict([(split[0], split_dataset[i]) for i, split in enumerate(splits)])

    def _time_series_split(
        self, training_dataset, dataset, event_time, drop_event_time=False
    ):
        # duplicate the code from util module to avoid udf errors on windows
        def check_timestamp_format_from_date_string(input_date):
            date_format_patterns = {
                r"^([0-9]{4})([0-9]{2})([0-9]{2})$": "%Y%m%d",
                r"^([0-9]{4})([0-9]{2})([0-9]{2})([0-9]{2})$": "%Y%m%d%H",
                r"^([0-9]{4})([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})$": "%Y%m%d%H%M",
                r"^([0-9]{4})([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})$": "%Y%m%d%H%M%S",
                r"^([0-9]{4})([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{3})$": "%Y%m%d%H%M%S%f",
                r"^([0-9]{4})([0-9]{2})([0-9]{2})T([0-9]{2})([0-9]{2})([0-9]{2})([0-9]{6})Z$": "ISO",
            }
            normalized_date = (
                input_date.replace("/", "")
                .replace("-", "")
                .replace(" ", "")
                .replace(":", "")
                .replace(".", "")
            )

            date_format = None
            for pattern in date_format_patterns:
                date_format_pattern = re.match(pattern, normalized_date)
                if date_format_pattern:
                    date_format = date_format_patterns[pattern]
                    break

            if date_format is None:
                raise ValueError(
                    "Unable to identify format of the provided date value : "
                    + input_date
                )

            return normalized_date, date_format

        def get_timestamp_from_date_string(input_date):
            norm_input_date, date_format = check_timestamp_format_from_date_string(
                input_date
            )
            try:
                if date_format != "ISO":
                    date_time = datetime.strptime(norm_input_date, date_format)
                else:
                    date_time = datetime.fromisoformat(input_date[:-1])
            except ValueError as err:
                raise ValueError(
                    "Unable to parse the normalized input date value : "
                    + norm_input_date
                    + " with format "
                    + date_format
                ) from err
            if date_time.tzinfo is None:
                date_time = date_time.replace(tzinfo=timezone.utc)
            return int(float(date_time.timestamp()) * 1000)

        def convert_event_time_to_timestamp(event_time):
            if not event_time:
                return None
            if isinstance(event_time, str):
                return get_timestamp_from_date_string(event_time)
            elif isinstance(event_time, pd._libs.tslibs.timestamps.Timestamp):
                # convert to unix epoch time in milliseconds.
                event_time = event_time.to_pydatetime()
                # convert to unix epoch time in milliseconds.
                if event_time.tzinfo is None:
                    event_time = event_time.replace(tzinfo=timezone.utc)
                return int(event_time.timestamp() * 1000)
            elif isinstance(event_time, datetime):
                # convert to unix epoch time in milliseconds.
                if event_time.tzinfo is None:
                    event_time = event_time.replace(tzinfo=timezone.utc)
                return int(event_time.timestamp() * 1000)
            elif isinstance(event_time, date):
                # convert to unix epoch time in milliseconds.
                event_time = datetime(*event_time.timetuple()[:7])
                if event_time.tzinfo is None:
                    event_time = event_time.replace(tzinfo=timezone.utc)
                return int(event_time.timestamp() * 1000)
            elif isinstance(event_time, int):
                if event_time == 0:
                    raise ValueError("Event time should be greater than 0.")
                # jdbc supports timestamp precision up to second only.
                if len(str(event_time)) <= 10:
                    event_time = event_time * 1000
                return event_time
            else:
                raise ValueError(
                    "Given event time should be in `datetime`, `date`, `str` or `int` type"
                )

        # registering the UDF
        _convert_event_time_to_timestamp = udf(
            convert_event_time_to_timestamp, LongType()
        )

        result_dfs = {}
        ts_col = _convert_event_time_to_timestamp(col(event_time))
        for split in training_dataset.splits:
            result_df = dataset.filter(ts_col >= split.start_time).filter(
                ts_col < split.end_time
            )
            if drop_event_time:
                result_df = result_df.drop(event_time)
            result_dfs[split.name] = result_df
        return result_dfs

    def _write_training_dataset_splits(
        self,
        training_dataset,
        feature_dataframes,
        write_options,
        save_mode,
        to_df=False,
        transformation_functions: List[
            transformation_function.TransformationFunction
        ] = None,
        transformation_context: Dict[str, Any] = None,
    ):
        for split_name, feature_dataframe in feature_dataframes.items():
            split_path = training_dataset.location + "/" + str(split_name)
            feature_dataframes[split_name] = self._write_training_dataset_single(
                transformation_functions,
                feature_dataframe,
                training_dataset.storage_connector,
                training_dataset.data_format,
                write_options,
                save_mode,
                split_path,
                to_df=to_df,
                transformation_context=transformation_context,
            )

        if to_df:
            return feature_dataframes

    def _write_training_dataset_single(
        self,
        transformation_functions,
        feature_dataframe,
        storage_connector,
        data_format,
        write_options,
        save_mode,
        path,
        to_df=False,
        transformation_context: Dict[str, Any] = None,
    ):
        # apply transformation functions (they are applied separately to each split)
        feature_dataframe = self._apply_transformation_function(
            transformation_functions,
            dataset=feature_dataframe,
            transformation_context=transformation_context,
        )
        if to_df:
            return feature_dataframe
        # TODO: currently not supported petastorm, hdf5 and npy file formats
        if data_format.lower() == "tsv":
            data_format = "csv"

        path = self.setup_storage_connector(storage_connector, path)

        feature_dataframe.write.format(data_format).options(**write_options).mode(
            save_mode
        ).save(path)

        feature_dataframe.unpersist()

    def read(
        self, storage_connector, data_format, read_options, location, dataframe_type
    ):
        if not data_format:
            raise FeatureStoreException("data_format is not specified")

        if isinstance(location, str):
            if data_format.lower() in ["delta", "parquet", "hudi", "orc", "bigquery"]:
                # All the above data format readers can handle partitioning
                # by their own, they don't need /**
                # for bigquery, argument location can be a SQL query
                path = location
            else:
                path = location + "/**"

            if data_format.lower() == "tsv":
                data_format = "csv"

        else:
            path = None

        path = self.setup_storage_connector(storage_connector, path)

        return self._return_dataframe_type(
            self._spark_session.read.format(data_format)
            .options(**(read_options if read_options else {}))
            .load(path),
            dataframe_type=dataframe_type,
        )

    def read_stream(
        self,
        storage_connector,
        message_format,
        schema,
        options,
        include_metadata,
    ):
        # ideally all this logic should be in the storage connector in case we add more
        # streaming storage connectors...
        stream = self._spark_session.readStream.format(
            storage_connector.SPARK_FORMAT
        )  # todo SPARK_FORMAT available only for KAFKA connectors

        # set user options last so that they overwrite any default options
        stream = stream.options(**storage_connector.spark_options(), **options)

        if storage_connector.type == StorageConnector.KAFKA:
            return self._read_stream_kafka(
                stream, message_format, schema, include_metadata
            )

    def _read_stream_kafka(self, stream, message_format, schema, include_metadata):
        kafka_cols = [
            col("key"),
            col("topic"),
            col("partition"),
            col("offset"),
            col("timestamp"),
            col("timestampType"),
        ]

        if message_format == "avro" and schema is not None:
            # check if vallid avro schema
            avro.schema.parse(schema)
            df = stream.load()
            if include_metadata is True:
                return df.select(
                    *kafka_cols, from_avro(df.value, schema).alias("value")
                ).select(*kafka_cols, col("value.*"))
            return df.select(from_avro(df.value, schema).alias("value")).select(
                col("value.*")
            )
        elif message_format == "json" and schema is not None:
            df = stream.load()
            if include_metadata is True:
                return df.select(
                    *kafka_cols,
                    from_json(df.value.cast("string"), schema).alias("value"),
                ).select(*kafka_cols, col("value.*"))
            return df.select(
                from_json(df.value.cast("string"), schema).alias("value")
            ).select(col("value.*"))

        if include_metadata is True:
            return stream.load()
        return stream.load().select("key", "value")

    def add_file(self, file):
        if not file:
            return file

        # This is used for unit testing
        if not file.startswith("file://"):
            file = "hdfs://" + file

        file_name = os.path.basename(file)

        # for external clients, download the file
        if client._is_external():
            tmp_file = os.path.join(SparkFiles.getRootDirectory(), file_name)
            print("Reading key file from storage connector.")
            response = self._dataset_api.read_content(file, util.get_dataset_type(file))

            with open(tmp_file, "wb") as f:
                f.write(response.content)
        else:
            self._spark_context.addFile(file)

            # The file is not added to the driver current working directory
            # We should add it manually by copying from the download location
            # The file will be added to the executors current working directory
            # before the next task is executed
            shutil.copy(SparkFiles.get(file_name), file_name)

        return file_name

    def profile(
        self,
        dataframe,
        relevant_columns,
        correlations,
        histograms,
        exact_uniqueness=True,
    ):
        """Profile a dataframe with Deequ."""
        return self._jvm.com.logicalclocks.hsfs.spark.engine.SparkEngine.getInstance().profile(
            dataframe._jdf,
            relevant_columns,
            correlations,
            histograms,
            exact_uniqueness,
        )

    @uses_great_expectations
    def validate_with_great_expectations(
        self,
        dataframe: DataFrame,  # noqa: F821
        expectation_suite: great_expectations.core.ExpectationSuite,  # noqa: F821
        ge_validate_kwargs: Optional[dict],
    ):
        # NOTE: InMemoryStoreBackendDefaults SHOULD NOT BE USED in normal settings. You
        # may experience data loss as it persists nothing. It is used here for testing.
        # Please refer to docs to learn how to instantiate your DataContext.
        store_backend_defaults = (
            great_expectations.data_context.types.base.InMemoryStoreBackendDefaults()
        )
        data_context_config = (
            great_expectations.data_context.types.base.DataContextConfig(
                store_backend_defaults=store_backend_defaults,
                checkpoint_store_name=store_backend_defaults.checkpoint_store_name,
            )
        )
        context = great_expectations.data_context.BaseDataContext(
            project_config=data_context_config
        )

        datasource = {
            "name": "my_spark_dataframe",
            "class_name": "Datasource",
            "execution_engine": {
                "class_name": "SparkDFExecutionEngine",
                "force_reuse_spark_context": True,
            },
            "data_connectors": {
                "default_runtime_data_connector_name": {
                    "class_name": "RuntimeDataConnector",
                    "batch_identifiers": ["batch_id"],
                }
            },
        }
        context.add_datasource(**datasource)

        # Here is a RuntimeBatchRequest using a dataframe
        batch_request = great_expectations.core.batch.RuntimeBatchRequest(
            datasource_name="my_spark_dataframe",
            data_connector_name="default_runtime_data_connector_name",
            data_asset_name="<YOUR_MEANGINGFUL_NAME>",  # This can be anything that identifies this data_asset for you
            batch_identifiers={"batch_id": "default_identifier"},
            runtime_parameters={"batch_data": dataframe},  # Your dataframe goes here
        )
        context.save_expectation_suite(expectation_suite)
        validator = context.get_validator(
            batch_request=batch_request,
            expectation_suite_name=expectation_suite.expectation_suite_name,
        )
        report = validator.validate(**ge_validate_kwargs)

        return report

    def write_options(self, data_format, provided_options):
        if data_format.lower() == "tfrecords":
            options = dict(recordType="Example")
            options.update(provided_options)
        elif data_format.lower() == "tfrecord":
            options = dict(recordType="Example")
            options.update(provided_options)
        elif data_format.lower() == "csv":
            options = dict(delimiter=",", header="true")
            options.update(provided_options)
        elif data_format.lower() == "tsv":
            options = dict(delimiter="\t", header="true")
            options.update(provided_options)
        else:
            options = {}
            options.update(provided_options)
        return options

    def read_options(self, data_format, provided_options):
        if provided_options is None:
            provided_options = {}
        if data_format.lower() == "tfrecords":
            options = dict(recordType="Example", **provided_options)
            options.update(provided_options)
        elif data_format.lower() == "tfrecord":
            options = dict(recordType="Example")
            options.update(provided_options)
        elif data_format.lower() == "csv":
            options = dict(delimiter=",", header="true", inferSchema="true")
            options.update(provided_options)
        elif data_format.lower() == "tsv":
            options = dict(delimiter="\t", header="true", inferSchema="true")
            options.update(provided_options)
        else:
            options = {}
            options.update(provided_options)
        return options

    def parse_schema_feature_group(
        self,
        dataframe,
        time_travel_format=None,
        **kwargs,
    ):
        features = []

        using_hudi = time_travel_format == "HUDI"
        for feat in dataframe.schema:
            name = util.autofix_feature_name(feat.name)
            try:
                converted_type = Engine._convert_spark_type_to_offline_type(
                    feat.dataType, using_hudi
                )
            except ValueError as e:
                raise FeatureStoreException(f"Feature '{feat.name}': {str(e)}") from e
            features.append(
                feature.Feature(
                    name, converted_type, feat.metadata.get("description", None)
                )
            )
        return features

    def parse_schema_training_dataset(self, dataframe):
        return [
            training_dataset_feature.TrainingDatasetFeature(
                util.autofix_feature_name(feat.name), feat.dataType.simpleString()
            )
            for feat in dataframe.schema
        ]

    def setup_storage_connector(self, storage_connector, path=None):
        if storage_connector.type == StorageConnector.S3:
            return self._setup_s3_hadoop_conf(storage_connector, path)
        elif storage_connector.type == StorageConnector.ADLS:
            return self._setup_adls_hadoop_conf(storage_connector, path)
        elif storage_connector.type == StorageConnector.GCS:
            return self._setup_gcp_hadoop_conf(storage_connector, path)
        else:
            return path

    def _setup_s3_hadoop_conf(self, storage_connector, path):
        FS_S3_GLOBAL_CONF = "fs.s3a.global-conf"

        # The argument arrive here as strings
        if storage_connector.arguments.get(FS_S3_GLOBAL_CONF, "True").lower() == "true":
            # For legacy behaviour set the S3 values at global level
            self._set_s3_hadoop_conf(storage_connector, "fs.s3a")

        # Set credentials at bucket level as well to allow users to use multiple
        # storage connector in the same application.
        self._set_s3_hadoop_conf(
            storage_connector, f"fs.s3a.bucket.{storage_connector.bucket}"
        )
        return path.replace("s3://", "s3a://", 1) if path is not None else None

    def _set_s3_hadoop_conf(self, storage_connector, prefix):
        if storage_connector.access_key:
            self._spark_context._jsc.hadoopConfiguration().set(
                f"{prefix}.access.key", storage_connector.access_key
            )
        if storage_connector.secret_key:
            self._spark_context._jsc.hadoopConfiguration().set(
                f"{prefix}.secret.key", storage_connector.secret_key
            )
        if storage_connector.server_encryption_algorithm:
            self._spark_context._jsc.hadoopConfiguration().set(
                f"{prefix}.server-side-encryption-algorithm",
                storage_connector.server_encryption_algorithm,
            )
        if storage_connector.server_encryption_key:
            self._spark_context._jsc.hadoopConfiguration().set(
                f"{prefix}.server-side-encryption-key",
                storage_connector.server_encryption_key,
            )
        if storage_connector.session_token:
            print(f"session token set for {prefix}")
            self._spark_context._jsc.hadoopConfiguration().set(
                f"{prefix}.aws.credentials.provider",
                "org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider",
            )
            self._spark_context._jsc.hadoopConfiguration().set(
                f"{prefix}.session.token",
                storage_connector.session_token,
            )

        # This is the name of the property as expected from the user, without the bucket name.
        FS_S3_ENDPOINT = "fs.s3a.endpoint"
        if FS_S3_ENDPOINT in storage_connector.arguments:
            self._spark_context._jsc.hadoopConfiguration().set(
                f"{prefix}.endpoint",
                storage_connector.spark_options().get(FS_S3_ENDPOINT),
            )

    def _setup_adls_hadoop_conf(self, storage_connector, path):
        for k, v in storage_connector.spark_options().items():
            self._spark_context._jsc.hadoopConfiguration().set(k, v)

        return path

    def is_spark_dataframe(self, dataframe):
        if isinstance(dataframe, DataFrame):
            return True
        return False

    def update_table_schema(self, feature_group):
        if feature_group.time_travel_format == "DELTA":
            self._add_cols_to_delta_table(feature_group)
        else:
            self._save_empty_dataframe(feature_group)

    def _save_empty_dataframe(self, feature_group):
        location = feature_group.prepare_spark_location()

        dataframe = self._spark_session.read.format("hudi").load(location)

        for _feature in feature_group.features:
            if _feature.name not in dataframe.columns:
                dataframe = dataframe.withColumn(
                    _feature.name, lit(None).cast(_feature.type)
                )

        self.save_dataframe(
            feature_group,
            dataframe.limit(0),
            "upsert",
            feature_group.online_enabled,
            "offline",
            {},
            {},
        )

    def _add_cols_to_delta_table(self, feature_group):
        location = feature_group.prepare_spark_location()

        dataframe = self._spark_session.read.format("delta").load(location)

        for _feature in feature_group.features:
            if _feature.name not in dataframe.columns:
                dataframe = dataframe.withColumn(
                    _feature.name, lit(None).cast(_feature.type)
                )

        dataframe.limit(0).write.format("delta").mode("append").option(
            "mergeSchema", "true"
        ).option("spark.databricks.delta.schema.autoMerge.enabled", "true").save(
            location
        )

    def _apply_transformation_function(
        self,
        transformation_functions: List[transformation_function.TransformationFunction],
        dataset: DataFrame,
        transformation_context: Dict[str, Any] = None,
    ):
        """
        Apply transformation function to the dataframe.

        # Arguments
            transformation_functions `List[TransformationFunction]` : List of transformation functions.
            dataset `Union[DataFrame]`: A spark dataframe.
            transformation_context: `Dict[str, Any]` A dictionary mapping variable names to objects that will be provided as contextual information to the transformation function at runtime.
                These variables must be explicitly defined as parameters in the transformation function to be accessible during execution. If no context variables are provided, this parameter defaults to `None`.
        # Returns
            `DataFrame`: A spark dataframe with the transformed data.
        # Raises
            `hopsworks.client.exceptions.FeatureStoreException`: If any of the features mentioned in the transformation function is not present in the Feature View.
        """
        dropped_features = set()
        transformations = []
        transformation_features = []
        output_col_names = []
        explode_name = []
        for tf in transformation_functions:
            hopsworks_udf = tf.hopsworks_udf

            # Setting transformation function context variables.
            hopsworks_udf.transformation_context = transformation_context

            missing_features = set(hopsworks_udf.transformation_features) - set(
                dataset.columns
            )

            if missing_features:
                if (
                    tf.transformation_type
                    == transformation_function.TransformationType.ON_DEMAND
                ):
                    # On-demand transformation are applied using the python/spark engine during insertion, the transformation while retrieving feature vectors are performed in the vector_server.
                    raise FeatureStoreException(
                        f"The following feature(s): `{'`, '.join(missing_features)}`, specified in the on-demand transformation function '{hopsworks_udf.function_name}' are not present in the dataframe being inserted into the feature group. "
                        + "Please verify that the correct feature names are used in the transformation function and that these features exist in the dataframe being inserted."
                    )
                else:
                    raise FeatureStoreException(
                        f"The following feature(s): `{'`, '.join(missing_features)}`, specified in the model-dependent transformation function '{hopsworks_udf.function_name}' are not present in the feature view. Please verify that the correct features are specified in the transformation function."
                    )
            if tf.hopsworks_udf.dropped_features:
                dropped_features.update(hopsworks_udf.dropped_features)

            # Add to dropped features if the feature need to overwritten to avoid ambiguous columns.
            if len(hopsworks_udf.return_types) == 1 and (
                hopsworks_udf.function_name == hopsworks_udf.output_column_names[0]
            ):
                dropped_features.update(hopsworks_udf.output_column_names)

            pandas_udf = hopsworks_udf.get_udf()
            output_col_name = hopsworks_udf.output_column_names[0]

            transformations.append(pandas_udf)
            output_col_names.append(output_col_name)
            transformation_features.append(hopsworks_udf.transformation_features)

            if len(hopsworks_udf.return_types) > 1:
                explode_name.append(f"{output_col_name}.*")
            else:
                explode_name.append(output_col_name)

        untransformed_columns = []  # Untransformed column maintained as a list since order is imported while selecting features.
        for column in dataset.columns:
            if column not in dropped_features:
                untransformed_columns.append(column)
        # Applying transformations
        transformed_dataset = dataset.select(
            *untransformed_columns,
            *[
                fun(*feature).alias(output_col_name)
                for fun, feature, output_col_name in zip(
                    transformations, transformation_features, output_col_names
                )
            ],
        ).select(*untransformed_columns, *explode_name)

        return transformed_dataset

    def _setup_gcp_hadoop_conf(self, storage_connector, path):
        PROPERTY_ENCRYPTION_KEY = "fs.gs.encryption.key"
        PROPERTY_ENCRYPTION_HASH = "fs.gs.encryption.key.hash"
        PROPERTY_ALGORITHM = "fs.gs.encryption.algorithm"
        PROPERTY_GCS_FS_KEY = "fs.AbstractFileSystem.gs.impl"
        PROPERTY_GCS_FS_VALUE = "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS"
        PROPERTY_GCS_ACCOUNT_ENABLE = "google.cloud.auth.service.account.enable"
        PROPERTY_ACCT_EMAIL = "fs.gs.auth.service.account.email"
        PROPERTY_ACCT_KEY_ID = "fs.gs.auth.service.account.private.key.id"
        PROPERTY_ACCT_KEY = "fs.gs.auth.service.account.private.key"
        # The AbstractFileSystem for 'gs:' URIs
        self._spark_context._jsc.hadoopConfiguration().setIfUnset(
            PROPERTY_GCS_FS_KEY, PROPERTY_GCS_FS_VALUE
        )
        # Whether to use a service account for GCS authorization. Setting this
        # property to `false` will disable use of service accounts for authentication.
        self._spark_context._jsc.hadoopConfiguration().setIfUnset(
            PROPERTY_GCS_ACCOUNT_ENABLE, "true"
        )

        # The JSON key file of the service account used for GCS
        # access when google.cloud.auth.service.account.enable is true.
        local_path = self.add_file(storage_connector.key_path)
        with open(local_path, "r") as f_in:
            jsondata = json.load(f_in)
        self._spark_context._jsc.hadoopConfiguration().set(
            PROPERTY_ACCT_EMAIL, jsondata["client_email"]
        )
        self._spark_context._jsc.hadoopConfiguration().set(
            PROPERTY_ACCT_KEY_ID, jsondata["private_key_id"]
        )
        self._spark_context._jsc.hadoopConfiguration().set(
            PROPERTY_ACCT_KEY, jsondata["private_key"]
        )

        if storage_connector.algorithm:
            # if encryption fields present
            self._spark_context._jsc.hadoopConfiguration().set(
                PROPERTY_ALGORITHM, storage_connector.algorithm
            )
            self._spark_context._jsc.hadoopConfiguration().set(
                PROPERTY_ENCRYPTION_KEY, storage_connector.encryption_key
            )
            self._spark_context._jsc.hadoopConfiguration().set(
                PROPERTY_ENCRYPTION_HASH, storage_connector.encryption_key_hash
            )
        else:
            # unset if already set
            self._spark_context._jsc.hadoopConfiguration().unset(PROPERTY_ALGORITHM)
            self._spark_context._jsc.hadoopConfiguration().unset(
                PROPERTY_ENCRYPTION_HASH
            )
            self._spark_context._jsc.hadoopConfiguration().unset(
                PROPERTY_ENCRYPTION_KEY
            )

        return path

    def create_empty_df(self, streaming_df):
        return SQLContext(self._spark_context).createDataFrame(
            self._spark_context.emptyRDD(), streaming_df.schema
        )

    @staticmethod
    def get_unique_values(feature_dataframe, feature_name):
        unique_values = feature_dataframe.select(feature_name).distinct().collect()
        return [field[feature_name] for field in unique_values]

    @staticmethod
    def _convert_spark_type_to_offline_type(spark_type, using_hudi):
        # The HiveSyncTool is strict and does not support schema evolution from tinyint/short to
        # int. Avro, on the other hand, does not support tinyint/short and delivers them as int
        # to Hive. Therefore, we need to force Hive to create int-typed columns in the first place.

        if not using_hudi:
            return spark_type.simpleString()
        elif type(spark_type) is ByteType:
            return "int"
        elif type(spark_type) is ShortType:
            return "int"
        elif type(spark_type) in [
            BooleanType,
            IntegerType,
            LongType,
            FloatType,
            DoubleType,
            DecimalType,
            TimestampType,
            DateType,
            StringType,
            ArrayType,
            StructType,
            BinaryType,
        ]:
            return spark_type.simpleString()

        raise ValueError(f"spark type {str(type(spark_type))} not supported")

    @staticmethod
    def _convert_offline_type_to_spark_type(offline_type):
        if "array<" == offline_type[:6]:
            return ArrayType(
                Engine._convert_offline_type_to_spark_type(offline_type[6:-1])
            )
        elif "struct<label:string,index:int>" in offline_type:
            return StructType(
                [
                    StructField("label", StringType(), True),
                    StructField("index", IntegerType(), True),
                ]
            )
        elif offline_type.startswith("decimal"):
            return DecimalType()
        else:
            offline_type_spark_type_mapping = {
                "string": StringType(),
                "bigint": LongType(),
                "int": IntegerType(),
                "smallint": ShortType(),
                "tinyint": ByteType(),
                "float": FloatType(),
                "double": DoubleType(),
                "timestamp": TimestampType(),
                "boolean": BooleanType(),
                "date": DateType(),
                "binary": BinaryType(),
            }
            if offline_type in offline_type_spark_type_mapping:
                return offline_type_spark_type_mapping[offline_type]
            else:
                raise FeatureStoreException(
                    f"Offline type {offline_type} cannot be converted to a spark type."
                )

    @staticmethod
    def cast_columns(df, schema, online=False):
        pyspark_schema = dict(
            [
                (_feat.name, Engine._convert_offline_type_to_spark_type(_feat.type))
                for _feat in schema
            ]
        )
        for _feat in pyspark_schema:
            df = df.withColumn(_feat, col(_feat).cast(pyspark_schema[_feat]))
        return df

    @staticmethod
    def is_connector_type_supported(type):
        return True

    def get_feature_logging_df(
        self,
        features: Union[
            pd.DataFrame, list[list], np.ndarray, TypeVar("pyspark.sql.DataFrame")
        ],
        fg: fg_mod.FeatureGroup = None,
        td_features: List[str] = None,
        td_predictions: List[training_dataset_feature.TrainingDatasetFeature] = None,
        td_col_name: Optional[str] = None,
        time_col_name: Optional[str] = None,
        model_col_name: Optional[str] = None,
        predictions: Optional[Union[pd.DataFrame, list[list], np.ndarray]] = None,
        training_dataset_version: Optional[int] = None,
        hsml_model: str = None,
        **kwargs,
    ):
        # do not take prediction separately because spark ml framework usually return feature together with the prediction
        # and it is costly to join them back
        df = self.convert_to_default_dataframe(features)
        if td_predictions:
            for f in td_predictions:
                if f.name not in df.columns:
                    df = df.withColumn(
                        f.name,
                        lit(None).cast(
                            Engine._convert_offline_type_to_spark_type(f.type)
                        ),
                    )

        uuid_udf = udf(lambda: str(uuid.uuid4()), StringType())

        # Add new columns to the DataFrame
        df = df.withColumn(td_col_name, lit(training_dataset_version).cast(LongType()))
        df = df.withColumn(model_col_name, lit(hsml_model).cast(StringType()))
        now = datetime.now()
        df = df.withColumn(time_col_name, lit(now).cast(TimestampType()))
        df = df.withColumn("log_id", uuid_udf())

        # Select the required columns
        return df.select(*[feat.name for feat in fg.features])

    @staticmethod
    def read_feature_log(query, time_col):
        df = query.read()
        return df.drop("log_id", time_col)


class SchemaError(Exception):
    """Thrown when schemas don't match"""
