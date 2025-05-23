# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/logging/log_source.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dqwak/logging/log_source.proto\x12\x14qwak.logging.service\"\xca\x04\n\tLogSource\x12\x41\n\rmodel_runtime\x18\x01 \x01(\x0b\x32(.qwak.logging.service.ModelRuntimeSourceH\x00\x12?\n\x0cremote_build\x18\x02 \x01(\x0b\x32\'.qwak.logging.service.RemoteBuildSourceH\x00\x12M\n\x13inference_execution\x18\x03 \x01(\x0b\x32..qwak.logging.service.InferenceExecutionSourceH\x00\x12P\n\x15streaming_feature_set\x18\x04 \x01(\x0b\x32/.qwak.logging.service.StreamingFeatureSetSourceH\x00\x12g\n!streaming_aggregation_feature_set\x18\x05 \x01(\x0b\x32:.qwak.logging.service.StreamingAggregationFeatureSetSourceH\x00\x12H\n\x11\x62\x61tch_feature_set\x18\x06 \x01(\x0b\x32+.qwak.logging.service.BatchFeatureSetSourceH\x00\x12[\n\x1breal_time_feature_extractor\x18\x07 \x01(\x0b\x32\x34.qwak.logging.service.RealTimeFeatureExtractorSourceH\x00\x42\x08\n\x06source\"8\n\x11RemoteBuildSource\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\x12\x11\n\tphase_ids\x18\x02 \x03(\t\"N\n\x12ModelRuntimeSource\x12\x17\n\rdeployment_id\x18\x01 \x01(\tH\x00\x12\x12\n\x08\x62uild_id\x18\x02 \x01(\tH\x00\x42\x0b\n\tsearch_by\"`\n\x18InferenceExecutionSource\x12\x1a\n\x10inference_job_id\x18\x01 \x01(\tH\x00\x12\x1b\n\x11inference_task_id\x18\x02 \x01(\tH\x00\x42\x0b\n\tsearch_by\"\xbf\x01\n\x19StreamingFeatureSetSource\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x01 \x01(\t\x12\x18\n\x10\x66\x65\x61ture_set_name\x18\x02 \x01(\t\x12\x34\n\x07offline\x18\x03 \x01(\x0b\x32!.qwak.logging.service.OfflineTypeH\x00\x12\x32\n\x06online\x18\x04 \x01(\x0b\x32 .qwak.logging.service.OnlineTypeH\x00\x42\x06\n\x04type\"W\n\x15\x42\x61tchFeatureSetSource\x12\x15\n\rfeatureset_id\x18\x01 \x01(\t\x12\x17\n\x0f\x66\x65\x61tureset_name\x18\x02 \x01(\t\x12\x0e\n\x06run_id\x18\x03 \x01(\t\"\xdb\x01\n$StreamingAggregationFeatureSetSource\x12\x37\n\trow_level\x18\x01 \x01(\x0b\x32\".qwak.logging.service.RowLevelTypeH\x00\x12:\n\ncompaction\x18\x02 \x01(\x0b\x32$.qwak.logging.service.CompactionTypeH\x00\x12\x36\n\x08\x62\x61\x63kfill\x18\x03 \x01(\x0b\x32\".qwak.logging.service.BackfillTypeH\x00\x42\x06\n\x04type\">\n\nOnlineType\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x01 \x01(\t\x12\x18\n\x10\x66\x65\x61ture_set_name\x18\x02 \x01(\t\"O\n\x0bOfflineType\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x01 \x01(\t\x12\x18\n\x10\x66\x65\x61ture_set_name\x18\x02 \x01(\t\x12\x0e\n\x06run_id\x18\x03 \x01(\t\"@\n\x0cRowLevelType\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x01 \x01(\t\x12\x18\n\x10\x66\x65\x61ture_set_name\x18\x02 \x01(\t\"R\n\x0e\x43ompactionType\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x01 \x01(\t\x12\x18\n\x10\x66\x65\x61ture_set_name\x18\x02 \x01(\t\x12\x0e\n\x06run_id\x18\x03 \x01(\t\"@\n\x0c\x42\x61\x63kfillType\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x01 \x01(\t\x12\x18\n\x10\x66\x65\x61ture_set_name\x18\x02 \x01(\t\"H\n\x1eRealTimeFeatureExtractorSource\x12&\n\x1ereal_time_feature_extractor_id\x18\x01 \x01(\tB\"\n\x1e\x63om.qwak.ai.logging.reader.apiP\x01\x62\x06proto3')



_LOGSOURCE = DESCRIPTOR.message_types_by_name['LogSource']
_REMOTEBUILDSOURCE = DESCRIPTOR.message_types_by_name['RemoteBuildSource']
_MODELRUNTIMESOURCE = DESCRIPTOR.message_types_by_name['ModelRuntimeSource']
_INFERENCEEXECUTIONSOURCE = DESCRIPTOR.message_types_by_name['InferenceExecutionSource']
_STREAMINGFEATURESETSOURCE = DESCRIPTOR.message_types_by_name['StreamingFeatureSetSource']
_BATCHFEATURESETSOURCE = DESCRIPTOR.message_types_by_name['BatchFeatureSetSource']
_STREAMINGAGGREGATIONFEATURESETSOURCE = DESCRIPTOR.message_types_by_name['StreamingAggregationFeatureSetSource']
_ONLINETYPE = DESCRIPTOR.message_types_by_name['OnlineType']
_OFFLINETYPE = DESCRIPTOR.message_types_by_name['OfflineType']
_ROWLEVELTYPE = DESCRIPTOR.message_types_by_name['RowLevelType']
_COMPACTIONTYPE = DESCRIPTOR.message_types_by_name['CompactionType']
_BACKFILLTYPE = DESCRIPTOR.message_types_by_name['BackfillType']
_REALTIMEFEATUREEXTRACTORSOURCE = DESCRIPTOR.message_types_by_name['RealTimeFeatureExtractorSource']
LogSource = _reflection.GeneratedProtocolMessageType('LogSource', (_message.Message,), {
  'DESCRIPTOR' : _LOGSOURCE,
  '__module__' : 'qwak.logging.log_source_pb2'
  # @@protoc_insertion_point(class_scope:qwak.logging.service.LogSource)
  })
_sym_db.RegisterMessage(LogSource)

RemoteBuildSource = _reflection.GeneratedProtocolMessageType('RemoteBuildSource', (_message.Message,), {
  'DESCRIPTOR' : _REMOTEBUILDSOURCE,
  '__module__' : 'qwak.logging.log_source_pb2'
  # @@protoc_insertion_point(class_scope:qwak.logging.service.RemoteBuildSource)
  })
_sym_db.RegisterMessage(RemoteBuildSource)

ModelRuntimeSource = _reflection.GeneratedProtocolMessageType('ModelRuntimeSource', (_message.Message,), {
  'DESCRIPTOR' : _MODELRUNTIMESOURCE,
  '__module__' : 'qwak.logging.log_source_pb2'
  # @@protoc_insertion_point(class_scope:qwak.logging.service.ModelRuntimeSource)
  })
_sym_db.RegisterMessage(ModelRuntimeSource)

InferenceExecutionSource = _reflection.GeneratedProtocolMessageType('InferenceExecutionSource', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCEEXECUTIONSOURCE,
  '__module__' : 'qwak.logging.log_source_pb2'
  # @@protoc_insertion_point(class_scope:qwak.logging.service.InferenceExecutionSource)
  })
_sym_db.RegisterMessage(InferenceExecutionSource)

StreamingFeatureSetSource = _reflection.GeneratedProtocolMessageType('StreamingFeatureSetSource', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGFEATURESETSOURCE,
  '__module__' : 'qwak.logging.log_source_pb2'
  # @@protoc_insertion_point(class_scope:qwak.logging.service.StreamingFeatureSetSource)
  })
_sym_db.RegisterMessage(StreamingFeatureSetSource)

BatchFeatureSetSource = _reflection.GeneratedProtocolMessageType('BatchFeatureSetSource', (_message.Message,), {
  'DESCRIPTOR' : _BATCHFEATURESETSOURCE,
  '__module__' : 'qwak.logging.log_source_pb2'
  # @@protoc_insertion_point(class_scope:qwak.logging.service.BatchFeatureSetSource)
  })
_sym_db.RegisterMessage(BatchFeatureSetSource)

StreamingAggregationFeatureSetSource = _reflection.GeneratedProtocolMessageType('StreamingAggregationFeatureSetSource', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGAGGREGATIONFEATURESETSOURCE,
  '__module__' : 'qwak.logging.log_source_pb2'
  # @@protoc_insertion_point(class_scope:qwak.logging.service.StreamingAggregationFeatureSetSource)
  })
_sym_db.RegisterMessage(StreamingAggregationFeatureSetSource)

OnlineType = _reflection.GeneratedProtocolMessageType('OnlineType', (_message.Message,), {
  'DESCRIPTOR' : _ONLINETYPE,
  '__module__' : 'qwak.logging.log_source_pb2'
  # @@protoc_insertion_point(class_scope:qwak.logging.service.OnlineType)
  })
_sym_db.RegisterMessage(OnlineType)

OfflineType = _reflection.GeneratedProtocolMessageType('OfflineType', (_message.Message,), {
  'DESCRIPTOR' : _OFFLINETYPE,
  '__module__' : 'qwak.logging.log_source_pb2'
  # @@protoc_insertion_point(class_scope:qwak.logging.service.OfflineType)
  })
_sym_db.RegisterMessage(OfflineType)

RowLevelType = _reflection.GeneratedProtocolMessageType('RowLevelType', (_message.Message,), {
  'DESCRIPTOR' : _ROWLEVELTYPE,
  '__module__' : 'qwak.logging.log_source_pb2'
  # @@protoc_insertion_point(class_scope:qwak.logging.service.RowLevelType)
  })
_sym_db.RegisterMessage(RowLevelType)

CompactionType = _reflection.GeneratedProtocolMessageType('CompactionType', (_message.Message,), {
  'DESCRIPTOR' : _COMPACTIONTYPE,
  '__module__' : 'qwak.logging.log_source_pb2'
  # @@protoc_insertion_point(class_scope:qwak.logging.service.CompactionType)
  })
_sym_db.RegisterMessage(CompactionType)

BackfillType = _reflection.GeneratedProtocolMessageType('BackfillType', (_message.Message,), {
  'DESCRIPTOR' : _BACKFILLTYPE,
  '__module__' : 'qwak.logging.log_source_pb2'
  # @@protoc_insertion_point(class_scope:qwak.logging.service.BackfillType)
  })
_sym_db.RegisterMessage(BackfillType)

RealTimeFeatureExtractorSource = _reflection.GeneratedProtocolMessageType('RealTimeFeatureExtractorSource', (_message.Message,), {
  'DESCRIPTOR' : _REALTIMEFEATUREEXTRACTORSOURCE,
  '__module__' : 'qwak.logging.log_source_pb2'
  # @@protoc_insertion_point(class_scope:qwak.logging.service.RealTimeFeatureExtractorSource)
  })
_sym_db.RegisterMessage(RealTimeFeatureExtractorSource)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.qwak.ai.logging.reader.apiP\001'
  _LOGSOURCE._serialized_start=56
  _LOGSOURCE._serialized_end=642
  _REMOTEBUILDSOURCE._serialized_start=644
  _REMOTEBUILDSOURCE._serialized_end=700
  _MODELRUNTIMESOURCE._serialized_start=702
  _MODELRUNTIMESOURCE._serialized_end=780
  _INFERENCEEXECUTIONSOURCE._serialized_start=782
  _INFERENCEEXECUTIONSOURCE._serialized_end=878
  _STREAMINGFEATURESETSOURCE._serialized_start=881
  _STREAMINGFEATURESETSOURCE._serialized_end=1072
  _BATCHFEATURESETSOURCE._serialized_start=1074
  _BATCHFEATURESETSOURCE._serialized_end=1161
  _STREAMINGAGGREGATIONFEATURESETSOURCE._serialized_start=1164
  _STREAMINGAGGREGATIONFEATURESETSOURCE._serialized_end=1383
  _ONLINETYPE._serialized_start=1385
  _ONLINETYPE._serialized_end=1447
  _OFFLINETYPE._serialized_start=1449
  _OFFLINETYPE._serialized_end=1528
  _ROWLEVELTYPE._serialized_start=1530
  _ROWLEVELTYPE._serialized_end=1594
  _COMPACTIONTYPE._serialized_start=1596
  _COMPACTIONTYPE._serialized_end=1678
  _BACKFILLTYPE._serialized_start=1680
  _BACKFILLTYPE._serialized_end=1744
  _REALTIMEFEATUREEXTRACTORSOURCE._serialized_start=1746
  _REALTIMEFEATUREEXTRACTORSOURCE._serialized_end=1818
# @@protoc_insertion_point(module_scope)
