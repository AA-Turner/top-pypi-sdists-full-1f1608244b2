# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/feature_store/features/feature_set_types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from _qwak_proto.qwak.feature_store.sources import batch_pb2 as qwak_dot_feature__store_dot_sources_dot_batch__pb2
from _qwak_proto.qwak.feature_store.sources import streaming_pb2 as qwak_dot_feature__store_dot_sources_dot_streaming__pb2
from _qwak_proto.qwak.feature_store.features import execution_pb2 as qwak_dot_feature__store_dot_features_dot_execution__pb2
from _qwak_proto.qwak.feature_store.features import aggregation_pb2 as qwak_dot_feature__store_dot_features_dot_aggregation__pb2
from _qwak_proto.qwak.feature_store.features import monitoring_pb2 as qwak_dot_feature__store_dot_features_dot_monitoring__pb2
from _qwak_proto.qwak.feature_store.features import real_time_feature_extractor_pb2 as qwak_dot_feature__store_dot_features_dot_real__time__feature__extractor__pb2
from _qwak_proto.qwak.feature_store.sinks import sink_pb2 as qwak_dot_feature__store_dot_sinks_dot_sink__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3qwak/feature_store/features/feature_set_types.proto\x12\x1bqwak.feature.store.features\x1a\x1fgoogle/protobuf/timestamp.proto\x1a&qwak/feature_store/sources/batch.proto\x1a*qwak/feature_store/sources/streaming.proto\x1a+qwak/feature_store/features/execution.proto\x1a-qwak/feature_store/features/aggregation.proto\x1a,qwak/feature_store/features/monitoring.proto\x1a=qwak/feature_store/features/real_time_feature_extractor.proto\x1a#qwak/feature_store/sinks/sink.proto\"\x9f\x04\n\x0e\x46\x65\x61tureSetType\x12I\n\x11\x62\x61tch_feature_set\x18\x05 \x01(\x0b\x32,.qwak.feature.store.features.BatchFeatureSetH\x00\x12Q\n\x16on_the_fly_feature_set\x18\x06 \x01(\x0b\x32/.qwak.feature.store.features.OnTheFlyFeatureSetH\x00\x12Q\n\x15streaming_feature_set\x18\x07 \x01(\x0b\x32\x30.qwak.feature.store.features.StreamingFeatureSetH\x00\x12V\n\x18streaming_feature_set_v1\x18\x08 \x01(\x0b\x32\x32.qwak.feature.store.features.StreamingFeatureSetV1H\x00\x12N\n\x14\x62\x61tch_feature_set_v1\x18\t \x01(\x0b\x32..qwak.feature.store.features.BatchFeatureSetV1H\x00\x12h\n!streaming_aggregation_feature_set\x18\n \x01(\x0b\x32;.qwak.feature.store.features.StreamingAggregationFeatureSetH\x00\x42\n\n\x08set_type\"\x9d\x03\n\x0f\x42\x61tchFeatureSet\x12\x19\n\x11scheduling_policy\x18\x01 \x01(\t\x12\x41\n\x0c\x64\x61ta_sources\x18\x02 \x03(\x0b\x32\'.qwak.feature.store.sources.BatchSourceB\x02\x18\x01\x12\x37\n\x08\x62\x61\x63kfill\x18\x03 \x01(\x0b\x32%.qwak.feature.store.features.Backfill\x12\x37\n\x08\x66unction\x18\x04 \x01(\x0b\x32%.qwak.feature.store.features.Function\x12U\n\x19\x66\x65\x61ture_set_batch_sources\x18\x05 \x03(\x0b\x32\x32.qwak.feature.store.features.FeatureSetBatchSource\x12\x63\n\x19monitoring_configurations\x18\x06 \x01(\x0b\x32@.qwak.feature.store.features.monitoring.MonitoringConfigurations\"\xd8\x05\n\x11\x42\x61tchFeatureSetV1\x12\x19\n\x11scheduling_policy\x18\x01 \x01(\t\x12\x37\n\x08\x62\x61\x63kfill\x18\x02 \x01(\x0b\x32%.qwak.feature.store.features.Backfill\x12;\n\x08\x66unction\x18\x03 \x01(\x0b\x32%.qwak.feature.store.features.FunctionB\x02\x18\x01\x12U\n\x19\x66\x65\x61ture_set_batch_sources\x18\x04 \x03(\x0b\x32\x32.qwak.feature.store.features.FeatureSetBatchSource\x12L\n\x0e\x65xecution_spec\x18\x05 \x01(\x0b\x32\x34.qwak.feature.store.features.execution.ExecutionSpec\x12\x14\n\x0coffline_sink\x18\x06 \x01(\x08\x12\x13\n\x0bonline_sink\x18\x07 \x01(\x08\x12\x63\n\x19monitoring_configurations\x18\x08 \x01(\x0b\x32@.qwak.feature.store.features.monitoring.MonitoringConfigurations\x12\x1d\n\x15timestamp_column_name\x18\t \x01(\t\x12\x43\n\x0etransformation\x18\n \x01(\x0b\x32+.qwak.feature.store.features.Transformation\x12&\n\x1eqwak_internal_protocol_version\x18\x0b \x01(\x05\x12\\\n\x1breal_time_feature_extractor\x18\x0c \x01(\x0b\x32\x35.qwak.feature.store.features.RealTimeFeatureExtractorH\x00\x42\x13\n\x11\x66\x65\x61ture_extractor\"\x9d\x01\n\x15\x46\x65\x61tureSetBatchSource\x12<\n\x0b\x64\x61ta_source\x18\x01 \x01(\x0b\x32\'.qwak.feature.store.sources.BatchSource\x12\x46\n\x0bread_policy\x18\x02 \x01(\x0b\x32\x31.qwak.feature.store.features.DataSourceReadPolicy\"X\n\x13StreamingFeatureSet\x12\x41\n\x0c\x64\x61ta_sources\x18\x01 \x03(\x0b\x32+.qwak.feature.store.sources.StreamingSource\"\xc3\x03\n\x15StreamingFeatureSetV1\x12\x41\n\x0c\x64\x61ta_sources\x18\x01 \x03(\x0b\x32+.qwak.feature.store.sources.StreamingSource\x12\x43\n\x0etransformation\x18\x02 \x01(\x0b\x32+.qwak.feature.store.features.Transformation\x12U\n\x0e\x65xecution_spec\x18\x03 \x01(\x0b\x32=.qwak.feature.store.features.execution.StreamingExecutionSpec\x12\x1d\n\x15timestamp_column_name\x18\x04 \x01(\t\x12\x1f\n\x17online_trigger_interval\x18\x05 \x01(\x05\x12!\n\x19offline_scheduling_policy\x18\x06 \x01(\t\x12&\n\x1eqwak_internal_protocol_version\x18\x07 \x01(\x05\x12@\n\x0f\x61uxiliary_sinks\x18\x08 \x03(\x0b\x32\'.qwak.feature.store.sinks.StreamingSink\"\x97\x04\n\x1eStreamingAggregationFeatureSet\x12\x41\n\x0c\x64\x61ta_sources\x18\x01 \x03(\x0b\x32+.qwak.feature.store.sources.StreamingSource\x12\x43\n\x0etransformation\x18\x02 \x01(\x0b\x32+.qwak.feature.store.features.Transformation\x12U\n\x0e\x65xecution_spec\x18\x03 \x01(\x0b\x32=.qwak.feature.store.features.execution.StreamingExecutionSpec\x12\x1d\n\x15timestamp_column_name\x18\x04 \x01(\t\x12\x1f\n\x17online_trigger_interval\x18\x05 \x01(\x05\x12$\n\x1c\x63ompaction_scheduling_policy\x18\x06 \x01(\t\x12\x46\n\x10\x61ggregation_spec\x18\x07 \x01(\x0b\x32,.qwak.feature.store.features.AggregationSpec\x12@\n\rbackfill_spec\x18\x08 \x01(\x0b\x32).qwak.feature.store.features.BackfillSpec\x12&\n\x1eqwak_internal_protocol_version\x18\t \x01(\x05\"\xc3\x01\n\x1b\x42\x61\x63kfillBatchDataSourceSpec\x12<\n\x0b\x64\x61ta_source\x18\x01 \x01(\x0b\x32\'.qwak.feature.store.sources.BatchSource\x12\x33\n\x0fstart_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"|\n\x16\x42\x61\x63kfillDataSourceSpec\x12Z\n\x16\x62\x61tch_data_source_spec\x18\x01 \x01(\x0b\x32\x38.qwak.feature.store.features.BackfillBatchDataSourceSpecH\x00\x42\x06\n\x04type\"\xe1\x02\n\x0c\x42\x61\x63kfillSpec\x12T\n\x0e\x65xecution_spec\x18\x01 \x01(\x0b\x32<.qwak.feature.store.features.execution.BackfillExecutionSpec\x12\x33\n\x0fstart_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x43\n\x0etransformation\x18\x04 \x01(\x0b\x32+.qwak.feature.store.features.Transformation\x12N\n\x11\x64\x61ta_source_specs\x18\x05 \x03(\x0b\x32\x33.qwak.feature.store.features.BackfillDataSourceSpec\"\x9f\x01\n\x0f\x41ggregationSpec\x12O\n\x0c\x61ggregations\x18\x01 \x03(\x0b\x32\x39.qwak.feature.store.features.aggregation.AggregationField\x12\x15\n\rslide_seconds\x18\x02 \x01(\x05\x12$\n\x1c\x61llowed_late_arrival_seconds\x18\x03 \x01(\x05\"\xdd\x03\n\x0eTransformation\x12L\n\x12udf_transformation\x18\x01 \x01(\x0b\x32..qwak.feature.store.features.UdfTransformationH\x00\x12L\n\x12sql_transformation\x18\x02 \x01(\x0b\x32..qwak.feature.store.features.SqlTransformationH\x00\x12V\n\x15koalas_transformation\x18\x03 \x01(\x0b\x32\x31.qwak.feature.store.features.KoalasTransformationB\x02\x18\x01H\x00\x12T\n\x16pyspark_transformation\x18\x05 \x01(\x0b\x32\x32.qwak.feature.store.features.PySparkTransformationH\x00\x12\x62\n\x1epandas_on_spark_transformation\x18\x06 \x01(\x0b\x32\x38.qwak.feature.store.features.PandasOnSparkTransformationH\x00\x12\x15\n\rartifact_path\x18\x04 \x01(\tB\x06\n\x04type\"*\n\x11UdfTransformation\x12\x15\n\rfunction_name\x18\x01 \x01(\t\"8\n\x11SqlTransformation\x12\x0b\n\x03sql\x18\x01 \x01(\t\x12\x16\n\x0e\x66unction_names\x18\x02 \x03(\t\"\x83\x01\n\x14KoalasTransformation\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12\x41\n\x06qwargs\x18\x02 \x01(\x0b\x32/.qwak.feature.store.features.TransformArgumentsH\x00:\x02\x18\x01\x42\r\n\x0b\x61rgs_option\"\x80\x01\n\x15PySparkTransformation\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12\x41\n\x06qwargs\x18\x02 \x01(\x0b\x32/.qwak.feature.store.features.TransformArgumentsH\x00\x42\r\n\x0b\x61rgs_option\"\x86\x01\n\x1bPandasOnSparkTransformation\x12\x15\n\rfunction_name\x18\x01 \x01(\t\x12\x41\n\x06qwargs\x18\x02 \x01(\x0b\x32/.qwak.feature.store.features.TransformArgumentsH\x00\x42\r\n\x0b\x61rgs_option\"\x90\x01\n\x12TransformArguments\x12K\n\x06qwargs\x18\x01 \x03(\x0b\x32;.qwak.feature.store.features.TransformArguments.QwargsEntry\x1a-\n\x0bQwargsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"f\n\x12OnTheFlyFeatureSet\x12:\n\x08\x66unction\x18\x01 \x01(\x0b\x32(.qwak.feature.store.features.UdfFunction\x12\x14\n\x0crequirements\x18\x02 \x01(\x0c\"\x96\x01\n\x08\x46unction\x12@\n\x0csql_function\x18\x01 \x01(\x0b\x32(.qwak.feature.store.features.SqlFunctionH\x00\x12@\n\x0cudf_function\x18\x02 \x01(\x0b\x32(.qwak.feature.store.features.UdfFunctionH\x00\x42\x06\n\x04type\"\xb5\x01\n\x08\x42\x61\x63kfill\x12.\n\nstart_date\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12I\n\rfillup_method\x18\x02 \x01(\x0e\x32\x32.qwak.feature.store.features.Backfill.FillUpMethod\".\n\x0c\x46illUpMethod\x12\x10\n\x0c\x41S_SCHEDULED\x10\x00\x12\x0c\n\x08SNAPSHOT\x10\x01\"\x1a\n\x0bSqlFunction\x12\x0b\n\x03sql\x18\x01 \x01(\t\"\x1b\n\x0bUdfFunction\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x0c\"\t\n\x07NewOnly\"\xa0\x01\n\tTimeFrame\x12\x0f\n\x07minutes\x18\x01 \x01(\x05\x12\x37\n\x07vanilla\x18\x02 \x01(\x0b\x32$.qwak.feature.store.features.VanillaH\x00\x12?\n\x0b\x61ggregation\x18\x03 \x01(\x0b\x32(.qwak.feature.store.features.AggregationH\x00\x42\x08\n\x06\x66lavor\"k\n\x0b\x41ggregation\x12T\n\x16\x61ggregation_population\x18\x01 \x01(\x0b\x32\x32.qwak.feature.store.features.AggregationPopulationH\x00\x42\x06\n\x04type\"\x17\n\x15\x41ggregationPopulation\"\x1c\n\x1aPopulationTimeframeNewOnly\"j\n\x13PopulationTimeframe\x12K\n\x08new_only\x18\x01 \x01(\x0b\x32\x37.qwak.feature.store.features.PopulationTimeframeNewOnlyH\x00\x42\x06\n\x04type\"\t\n\x07Vanilla\"\x9f\x01\n\x08\x46ullRead\x12\x37\n\x07\x64\x65\x66\x61ult\x18\x01 \x01(\x0b\x32$.qwak.feature.store.features.VanillaH\x00\x12P\n\x14population_timeframe\x18\x02 \x01(\x0b\x32\x30.qwak.feature.store.features.PopulationTimeframeH\x00\x42\x08\n\x06\x66lavor\"\xd2\x01\n\x14\x44\x61taSourceReadPolicy\x12\x38\n\x08new_only\x18\x01 \x01(\x0b\x32$.qwak.feature.store.features.NewOnlyH\x00\x12<\n\ntime_frame\x18\x02 \x01(\x0b\x32&.qwak.feature.store.features.TimeFrameH\x00\x12:\n\tfull_read\x18\x03 \x01(\x0b\x32%.qwak.feature.store.features.FullReadH\x00\x42\x06\n\x04type*}\n\x12\x46\x65\x61tureSetTypeView\x12!\n\x1d\x46\x45\x41TURE_SET_TYPE_VIEW_INVALID\x10\x00\x12\x1f\n\x1b\x46\x45\x41TURE_SET_TYPE_VIEW_BATCH\x10\x01\x12#\n\x1f\x46\x45\x41TURE_SET_TYPE_VIEW_STREAMING\x10\x02\x42[\n&com.qwak.ai.feature.store.features.apiP\x01Z/qwak/featurestore/features;featurestorefeaturesb\x06proto3')

_FEATURESETTYPEVIEW = DESCRIPTOR.enum_types_by_name['FeatureSetTypeView']
FeatureSetTypeView = enum_type_wrapper.EnumTypeWrapper(_FEATURESETTYPEVIEW)
FEATURE_SET_TYPE_VIEW_INVALID = 0
FEATURE_SET_TYPE_VIEW_BATCH = 1
FEATURE_SET_TYPE_VIEW_STREAMING = 2


_FEATURESETTYPE = DESCRIPTOR.message_types_by_name['FeatureSetType']
_BATCHFEATURESET = DESCRIPTOR.message_types_by_name['BatchFeatureSet']
_BATCHFEATURESETV1 = DESCRIPTOR.message_types_by_name['BatchFeatureSetV1']
_FEATURESETBATCHSOURCE = DESCRIPTOR.message_types_by_name['FeatureSetBatchSource']
_STREAMINGFEATURESET = DESCRIPTOR.message_types_by_name['StreamingFeatureSet']
_STREAMINGFEATURESETV1 = DESCRIPTOR.message_types_by_name['StreamingFeatureSetV1']
_STREAMINGAGGREGATIONFEATURESET = DESCRIPTOR.message_types_by_name['StreamingAggregationFeatureSet']
_BACKFILLBATCHDATASOURCESPEC = DESCRIPTOR.message_types_by_name['BackfillBatchDataSourceSpec']
_BACKFILLDATASOURCESPEC = DESCRIPTOR.message_types_by_name['BackfillDataSourceSpec']
_BACKFILLSPEC = DESCRIPTOR.message_types_by_name['BackfillSpec']
_AGGREGATIONSPEC = DESCRIPTOR.message_types_by_name['AggregationSpec']
_TRANSFORMATION = DESCRIPTOR.message_types_by_name['Transformation']
_UDFTRANSFORMATION = DESCRIPTOR.message_types_by_name['UdfTransformation']
_SQLTRANSFORMATION = DESCRIPTOR.message_types_by_name['SqlTransformation']
_KOALASTRANSFORMATION = DESCRIPTOR.message_types_by_name['KoalasTransformation']
_PYSPARKTRANSFORMATION = DESCRIPTOR.message_types_by_name['PySparkTransformation']
_PANDASONSPARKTRANSFORMATION = DESCRIPTOR.message_types_by_name['PandasOnSparkTransformation']
_TRANSFORMARGUMENTS = DESCRIPTOR.message_types_by_name['TransformArguments']
_TRANSFORMARGUMENTS_QWARGSENTRY = _TRANSFORMARGUMENTS.nested_types_by_name['QwargsEntry']
_ONTHEFLYFEATURESET = DESCRIPTOR.message_types_by_name['OnTheFlyFeatureSet']
_FUNCTION = DESCRIPTOR.message_types_by_name['Function']
_BACKFILL = DESCRIPTOR.message_types_by_name['Backfill']
_SQLFUNCTION = DESCRIPTOR.message_types_by_name['SqlFunction']
_UDFFUNCTION = DESCRIPTOR.message_types_by_name['UdfFunction']
_NEWONLY = DESCRIPTOR.message_types_by_name['NewOnly']
_TIMEFRAME = DESCRIPTOR.message_types_by_name['TimeFrame']
_AGGREGATION = DESCRIPTOR.message_types_by_name['Aggregation']
_AGGREGATIONPOPULATION = DESCRIPTOR.message_types_by_name['AggregationPopulation']
_POPULATIONTIMEFRAMENEWONLY = DESCRIPTOR.message_types_by_name['PopulationTimeframeNewOnly']
_POPULATIONTIMEFRAME = DESCRIPTOR.message_types_by_name['PopulationTimeframe']
_VANILLA = DESCRIPTOR.message_types_by_name['Vanilla']
_FULLREAD = DESCRIPTOR.message_types_by_name['FullRead']
_DATASOURCEREADPOLICY = DESCRIPTOR.message_types_by_name['DataSourceReadPolicy']
_BACKFILL_FILLUPMETHOD = _BACKFILL.enum_types_by_name['FillUpMethod']
FeatureSetType = _reflection.GeneratedProtocolMessageType('FeatureSetType', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESETTYPE,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.FeatureSetType)
  })
_sym_db.RegisterMessage(FeatureSetType)

BatchFeatureSet = _reflection.GeneratedProtocolMessageType('BatchFeatureSet', (_message.Message,), {
  'DESCRIPTOR' : _BATCHFEATURESET,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.BatchFeatureSet)
  })
_sym_db.RegisterMessage(BatchFeatureSet)

BatchFeatureSetV1 = _reflection.GeneratedProtocolMessageType('BatchFeatureSetV1', (_message.Message,), {
  'DESCRIPTOR' : _BATCHFEATURESETV1,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.BatchFeatureSetV1)
  })
_sym_db.RegisterMessage(BatchFeatureSetV1)

FeatureSetBatchSource = _reflection.GeneratedProtocolMessageType('FeatureSetBatchSource', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESETBATCHSOURCE,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.FeatureSetBatchSource)
  })
_sym_db.RegisterMessage(FeatureSetBatchSource)

StreamingFeatureSet = _reflection.GeneratedProtocolMessageType('StreamingFeatureSet', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGFEATURESET,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.StreamingFeatureSet)
  })
_sym_db.RegisterMessage(StreamingFeatureSet)

StreamingFeatureSetV1 = _reflection.GeneratedProtocolMessageType('StreamingFeatureSetV1', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGFEATURESETV1,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.StreamingFeatureSetV1)
  })
_sym_db.RegisterMessage(StreamingFeatureSetV1)

StreamingAggregationFeatureSet = _reflection.GeneratedProtocolMessageType('StreamingAggregationFeatureSet', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGAGGREGATIONFEATURESET,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.StreamingAggregationFeatureSet)
  })
_sym_db.RegisterMessage(StreamingAggregationFeatureSet)

BackfillBatchDataSourceSpec = _reflection.GeneratedProtocolMessageType('BackfillBatchDataSourceSpec', (_message.Message,), {
  'DESCRIPTOR' : _BACKFILLBATCHDATASOURCESPEC,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.BackfillBatchDataSourceSpec)
  })
_sym_db.RegisterMessage(BackfillBatchDataSourceSpec)

BackfillDataSourceSpec = _reflection.GeneratedProtocolMessageType('BackfillDataSourceSpec', (_message.Message,), {
  'DESCRIPTOR' : _BACKFILLDATASOURCESPEC,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.BackfillDataSourceSpec)
  })
_sym_db.RegisterMessage(BackfillDataSourceSpec)

BackfillSpec = _reflection.GeneratedProtocolMessageType('BackfillSpec', (_message.Message,), {
  'DESCRIPTOR' : _BACKFILLSPEC,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.BackfillSpec)
  })
_sym_db.RegisterMessage(BackfillSpec)

AggregationSpec = _reflection.GeneratedProtocolMessageType('AggregationSpec', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATIONSPEC,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.AggregationSpec)
  })
_sym_db.RegisterMessage(AggregationSpec)

Transformation = _reflection.GeneratedProtocolMessageType('Transformation', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMATION,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.Transformation)
  })
_sym_db.RegisterMessage(Transformation)

UdfTransformation = _reflection.GeneratedProtocolMessageType('UdfTransformation', (_message.Message,), {
  'DESCRIPTOR' : _UDFTRANSFORMATION,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.UdfTransformation)
  })
_sym_db.RegisterMessage(UdfTransformation)

SqlTransformation = _reflection.GeneratedProtocolMessageType('SqlTransformation', (_message.Message,), {
  'DESCRIPTOR' : _SQLTRANSFORMATION,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.SqlTransformation)
  })
_sym_db.RegisterMessage(SqlTransformation)

KoalasTransformation = _reflection.GeneratedProtocolMessageType('KoalasTransformation', (_message.Message,), {
  'DESCRIPTOR' : _KOALASTRANSFORMATION,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.KoalasTransformation)
  })
_sym_db.RegisterMessage(KoalasTransformation)

PySparkTransformation = _reflection.GeneratedProtocolMessageType('PySparkTransformation', (_message.Message,), {
  'DESCRIPTOR' : _PYSPARKTRANSFORMATION,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.PySparkTransformation)
  })
_sym_db.RegisterMessage(PySparkTransformation)

PandasOnSparkTransformation = _reflection.GeneratedProtocolMessageType('PandasOnSparkTransformation', (_message.Message,), {
  'DESCRIPTOR' : _PANDASONSPARKTRANSFORMATION,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.PandasOnSparkTransformation)
  })
_sym_db.RegisterMessage(PandasOnSparkTransformation)

TransformArguments = _reflection.GeneratedProtocolMessageType('TransformArguments', (_message.Message,), {

  'QwargsEntry' : _reflection.GeneratedProtocolMessageType('QwargsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRANSFORMARGUMENTS_QWARGSENTRY,
    '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
    # @@protoc_insertion_point(class_scope:qwak.feature.store.features.TransformArguments.QwargsEntry)
    })
  ,
  'DESCRIPTOR' : _TRANSFORMARGUMENTS,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.TransformArguments)
  })
_sym_db.RegisterMessage(TransformArguments)
_sym_db.RegisterMessage(TransformArguments.QwargsEntry)

OnTheFlyFeatureSet = _reflection.GeneratedProtocolMessageType('OnTheFlyFeatureSet', (_message.Message,), {
  'DESCRIPTOR' : _ONTHEFLYFEATURESET,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.OnTheFlyFeatureSet)
  })
_sym_db.RegisterMessage(OnTheFlyFeatureSet)

Function = _reflection.GeneratedProtocolMessageType('Function', (_message.Message,), {
  'DESCRIPTOR' : _FUNCTION,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.Function)
  })
_sym_db.RegisterMessage(Function)

Backfill = _reflection.GeneratedProtocolMessageType('Backfill', (_message.Message,), {
  'DESCRIPTOR' : _BACKFILL,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.Backfill)
  })
_sym_db.RegisterMessage(Backfill)

SqlFunction = _reflection.GeneratedProtocolMessageType('SqlFunction', (_message.Message,), {
  'DESCRIPTOR' : _SQLFUNCTION,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.SqlFunction)
  })
_sym_db.RegisterMessage(SqlFunction)

UdfFunction = _reflection.GeneratedProtocolMessageType('UdfFunction', (_message.Message,), {
  'DESCRIPTOR' : _UDFFUNCTION,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.UdfFunction)
  })
_sym_db.RegisterMessage(UdfFunction)

NewOnly = _reflection.GeneratedProtocolMessageType('NewOnly', (_message.Message,), {
  'DESCRIPTOR' : _NEWONLY,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.NewOnly)
  })
_sym_db.RegisterMessage(NewOnly)

TimeFrame = _reflection.GeneratedProtocolMessageType('TimeFrame', (_message.Message,), {
  'DESCRIPTOR' : _TIMEFRAME,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.TimeFrame)
  })
_sym_db.RegisterMessage(TimeFrame)

Aggregation = _reflection.GeneratedProtocolMessageType('Aggregation', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATION,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.Aggregation)
  })
_sym_db.RegisterMessage(Aggregation)

AggregationPopulation = _reflection.GeneratedProtocolMessageType('AggregationPopulation', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATIONPOPULATION,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.AggregationPopulation)
  })
_sym_db.RegisterMessage(AggregationPopulation)

PopulationTimeframeNewOnly = _reflection.GeneratedProtocolMessageType('PopulationTimeframeNewOnly', (_message.Message,), {
  'DESCRIPTOR' : _POPULATIONTIMEFRAMENEWONLY,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.PopulationTimeframeNewOnly)
  })
_sym_db.RegisterMessage(PopulationTimeframeNewOnly)

PopulationTimeframe = _reflection.GeneratedProtocolMessageType('PopulationTimeframe', (_message.Message,), {
  'DESCRIPTOR' : _POPULATIONTIMEFRAME,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.PopulationTimeframe)
  })
_sym_db.RegisterMessage(PopulationTimeframe)

Vanilla = _reflection.GeneratedProtocolMessageType('Vanilla', (_message.Message,), {
  'DESCRIPTOR' : _VANILLA,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.Vanilla)
  })
_sym_db.RegisterMessage(Vanilla)

FullRead = _reflection.GeneratedProtocolMessageType('FullRead', (_message.Message,), {
  'DESCRIPTOR' : _FULLREAD,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.FullRead)
  })
_sym_db.RegisterMessage(FullRead)

DataSourceReadPolicy = _reflection.GeneratedProtocolMessageType('DataSourceReadPolicy', (_message.Message,), {
  'DESCRIPTOR' : _DATASOURCEREADPOLICY,
  '__module__' : 'qwak.feature_store.features.feature_set_types_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.DataSourceReadPolicy)
  })
_sym_db.RegisterMessage(DataSourceReadPolicy)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&com.qwak.ai.feature.store.features.apiP\001Z/qwak/featurestore/features;featurestorefeatures'
  _BATCHFEATURESET.fields_by_name['data_sources']._options = None
  _BATCHFEATURESET.fields_by_name['data_sources']._serialized_options = b'\030\001'
  _BATCHFEATURESETV1.fields_by_name['function']._options = None
  _BATCHFEATURESETV1.fields_by_name['function']._serialized_options = b'\030\001'
  _TRANSFORMATION.fields_by_name['koalas_transformation']._options = None
  _TRANSFORMATION.fields_by_name['koalas_transformation']._serialized_options = b'\030\001'
  _KOALASTRANSFORMATION._options = None
  _KOALASTRANSFORMATION._serialized_options = b'\030\001'
  _TRANSFORMARGUMENTS_QWARGSENTRY._options = None
  _TRANSFORMARGUMENTS_QWARGSENTRY._serialized_options = b'8\001'
  _FEATURESETTYPEVIEW._serialized_start=6677
  _FEATURESETTYPEVIEW._serialized_end=6802
  _FEATURESETTYPE._serialized_start=440
  _FEATURESETTYPE._serialized_end=983
  _BATCHFEATURESET._serialized_start=986
  _BATCHFEATURESET._serialized_end=1399
  _BATCHFEATURESETV1._serialized_start=1402
  _BATCHFEATURESETV1._serialized_end=2130
  _FEATURESETBATCHSOURCE._serialized_start=2133
  _FEATURESETBATCHSOURCE._serialized_end=2290
  _STREAMINGFEATURESET._serialized_start=2292
  _STREAMINGFEATURESET._serialized_end=2380
  _STREAMINGFEATURESETV1._serialized_start=2383
  _STREAMINGFEATURESETV1._serialized_end=2834
  _STREAMINGAGGREGATIONFEATURESET._serialized_start=2837
  _STREAMINGAGGREGATIONFEATURESET._serialized_end=3372
  _BACKFILLBATCHDATASOURCESPEC._serialized_start=3375
  _BACKFILLBATCHDATASOURCESPEC._serialized_end=3570
  _BACKFILLDATASOURCESPEC._serialized_start=3572
  _BACKFILLDATASOURCESPEC._serialized_end=3696
  _BACKFILLSPEC._serialized_start=3699
  _BACKFILLSPEC._serialized_end=4052
  _AGGREGATIONSPEC._serialized_start=4055
  _AGGREGATIONSPEC._serialized_end=4214
  _TRANSFORMATION._serialized_start=4217
  _TRANSFORMATION._serialized_end=4694
  _UDFTRANSFORMATION._serialized_start=4696
  _UDFTRANSFORMATION._serialized_end=4738
  _SQLTRANSFORMATION._serialized_start=4740
  _SQLTRANSFORMATION._serialized_end=4796
  _KOALASTRANSFORMATION._serialized_start=4799
  _KOALASTRANSFORMATION._serialized_end=4930
  _PYSPARKTRANSFORMATION._serialized_start=4933
  _PYSPARKTRANSFORMATION._serialized_end=5061
  _PANDASONSPARKTRANSFORMATION._serialized_start=5064
  _PANDASONSPARKTRANSFORMATION._serialized_end=5198
  _TRANSFORMARGUMENTS._serialized_start=5201
  _TRANSFORMARGUMENTS._serialized_end=5345
  _TRANSFORMARGUMENTS_QWARGSENTRY._serialized_start=5300
  _TRANSFORMARGUMENTS_QWARGSENTRY._serialized_end=5345
  _ONTHEFLYFEATURESET._serialized_start=5347
  _ONTHEFLYFEATURESET._serialized_end=5449
  _FUNCTION._serialized_start=5452
  _FUNCTION._serialized_end=5602
  _BACKFILL._serialized_start=5605
  _BACKFILL._serialized_end=5786
  _BACKFILL_FILLUPMETHOD._serialized_start=5740
  _BACKFILL_FILLUPMETHOD._serialized_end=5786
  _SQLFUNCTION._serialized_start=5788
  _SQLFUNCTION._serialized_end=5814
  _UDFFUNCTION._serialized_start=5816
  _UDFFUNCTION._serialized_end=5843
  _NEWONLY._serialized_start=5845
  _NEWONLY._serialized_end=5854
  _TIMEFRAME._serialized_start=5857
  _TIMEFRAME._serialized_end=6017
  _AGGREGATION._serialized_start=6019
  _AGGREGATION._serialized_end=6126
  _AGGREGATIONPOPULATION._serialized_start=6128
  _AGGREGATIONPOPULATION._serialized_end=6151
  _POPULATIONTIMEFRAMENEWONLY._serialized_start=6153
  _POPULATIONTIMEFRAMENEWONLY._serialized_end=6181
  _POPULATIONTIMEFRAME._serialized_start=6183
  _POPULATIONTIMEFRAME._serialized_end=6289
  _VANILLA._serialized_start=6291
  _VANILLA._serialized_end=6300
  _FULLREAD._serialized_start=6303
  _FULLREAD._serialized_end=6462
  _DATASOURCEREADPOLICY._serialized_start=6465
  _DATASOURCEREADPOLICY._serialized_end=6675
# @@protoc_insertion_point(module_scope)
