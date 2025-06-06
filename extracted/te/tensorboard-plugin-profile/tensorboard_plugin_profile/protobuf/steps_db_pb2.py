# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plugin/tensorboard_plugin_profile/protobuf/steps_db.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from tensorboard_plugin_profile.protobuf import op_metrics_pb2 as plugin_dot_tensorboard__plugin__profile_dot_protobuf_dot_op__metrics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9plugin/tensorboard_plugin_profile/protobuf/steps_db.proto\x12\x13tensorflow.profiler\x1a\x19google/protobuf/any.proto\x1a;plugin/tensorboard_plugin_profile/protobuf/op_metrics.proto\"\x90\x02\n\x14GenericStepBreakdown\x12\x46\n\x07type_ps\x18\x01 \x03(\x0b\x32\x35.tensorflow.profiler.GenericStepBreakdown.TypePsEntry\x12N\n\x0b\x63\x61tegory_ps\x18\x02 \x03(\x0b\x32\x39.tensorflow.profiler.GenericStepBreakdown.CategoryPsEntry\x1a-\n\x0bTypePsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a\x31\n\x0f\x43\x61tegoryPsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\"\x9b\x04\n\x10TpuStepBreakdown\x12\x1a\n\x12infeed_duration_ps\x18\x01 \x01(\x04\x12\x17\n\x0fhost_outfeed_ps\x18\x02 \x01(\x04\x12!\n\x19wait_for_scv0_duration_ps\x18\x03 \x01(\x04\x12 \n\x18scv0_infeed_transform_ps\x18\x04 \x01(\x04\x12\x17\n\x0fscv0_outfeed_ps\x18\x05 \x01(\x04\x12\x17\n\x0f\x63rs_duration_ps\x18\x06 \x01(\x04\x12\x1b\n\x13scv0_infeed_percent\x18\x07 \x01(\x01\x12\x18\n\x10send_duration_ps\x18\x08 \x01(\x04\x12\x18\n\x10recv_duration_ps\x18\t \x01(\x04\x12\x1d\n\x15host_send_duration_ps\x18\x0f \x01(\x04\x12\x1d\n\x15host_recv_duration_ps\x18\x10 \x01(\x04\x12\x31\n)wait_for_megacore_fusion_peer_duration_ps\x18\x0e \x01(\x04\x12 \n\x18overlay_wait_duration_ps\x18\x0b \x01(\x04\x12\x1d\n\x15high_flops_compute_ps\x18\x0c \x01(\x04\x12\x12\n\ntc_idle_ps\x18\r \x01(\x04\x12\x12\n\ntc_busy_ps\x18\x11 \x01(\x04\x12\x14\n\x0cscv0_busy_ps\x18\x12 \x01(\x04\x12\x14\n\x0cscv0_step_ps\x18\x13 \x01(\x04J\x04\x08\n\x10\x0b\"\x85\x01\n\x17SparseCoreStepBreakdown\x12\x15\n\rsc_compute_ps\x18\x01 \x01(\x04\x12\x14\n\x0csc_infeed_ps\x18\x02 \x01(\x04\x12\x15\n\rsc_outfeed_ps\x18\x03 \x01(\x04\x12\x12\n\nsc_idle_ps\x18\x04 \x01(\x04\x12\x12\n\nsc_busy_ps\x18\x05 \x01(\x04\"V\n\x14\x44\x65viceMemoryTransfer\x12\x12\n\noccurrence\x18\x01 \x01(\x04\x12\x0f\n\x07time_us\x18\x02 \x01(\x01\x12\x19\n\x11\x62ytes_transferred\x18\x03 \x01(\x04\"\xca\x01\n\x0eStepInfoResult\x12\x10\n\x08step_num\x18\x01 \x01(\r\x12\x11\n\tstep_name\x18\x05 \x01(\t\x12\x13\n\x0b\x64uration_ps\x18\x02 \x01(\x04\x12\x10\n\x08\x62\x65gin_ps\x18\x03 \x01(\x04\x12,\n\x0estep_breakdown\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\x12>\n\x0b\x63ollectives\x18\x06 \x01(\x0b\x32).tensorflow.profiler.DeviceMemoryTransfer\"\x83\x01\n\rAllReduceInfo\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x10\n\x04name\x18\x02 \x01(\tB\x02\x18\x01\x12\x15\n\rall_reduce_id\x18\x03 \x01(\x04\x12\x15\n\rstart_time_ps\x18\x04 \x01(\x04\x12\x13\n\x0b\x65nd_time_ps\x18\x05 \x01(\x04\x12\x11\n\tbyte_size\x18\x06 \x01(\x04\"P\n\x11\x41llReduceDbResult\x12;\n\x0f\x61ll_reduce_info\x18\x01 \x03(\x0b\x32\".tensorflow.profiler.AllReduceInfo\"\xc4\x05\n\x0fPerCoreStepInfo\x12\x10\n\x08step_num\x18\x01 \x01(\r\x12U\n\x12step_info_per_core\x18\x02 \x03(\x0b\x32\x39.tensorflow.profiler.PerCoreStepInfo.StepInfoPerCoreEntry\x12\x38\n\x0ehlo_metrics_db\x18\x03 \x01(\x0b\x32 .tensorflow.profiler.OpMetricsDb\x12\x61\n\x19\x63ore_id_to_replica_id_map\x18\x05 \x03(\x0b\x32>.tensorflow.profiler.PerCoreStepInfo.CoreIdToReplicaIdMapEntry\x12\\\n\x16\x61ll_reduce_db_per_core\x18\x06 \x03(\x0b\x32<.tensorflow.profiler.PerCoreStepInfo.AllReduceDbPerCoreEntry\x12J\n\x17\x64\x65vice_memory_transfers\x18\x07 \x03(\x0b\x32).tensorflow.profiler.DeviceMemoryTransfer\x1a[\n\x14StepInfoPerCoreEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x32\n\x05value\x18\x02 \x01(\x0b\x32#.tensorflow.profiler.StepInfoResult:\x02\x38\x01\x1a;\n\x19\x43oreIdToReplicaIdMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x61\n\x17\x41llReduceDbPerCoreEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.tensorflow.profiler.AllReduceDbResult:\x02\x38\x01J\x04\x08\x04\x10\x05\"\xa2\x01\n\x12StepDatabaseResult\x12;\n\rstep_sequence\x18\x01 \x03(\x0b\x32$.tensorflow.profiler.PerCoreStepInfo\x12\x1b\n\x13use_incomplete_step\x18\x02 \x01(\x08\x12\x19\n\x11num_steps_dropped\x18\x03 \x01(\r\x12\x17\n\x0f\x65mpty_intersect\x18\x04 \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plugin.tensorboard_plugin_profile.protobuf.steps_db_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENERICSTEPBREAKDOWN_TYPEPSENTRY._options = None
  _GENERICSTEPBREAKDOWN_TYPEPSENTRY._serialized_options = b'8\001'
  _GENERICSTEPBREAKDOWN_CATEGORYPSENTRY._options = None
  _GENERICSTEPBREAKDOWN_CATEGORYPSENTRY._serialized_options = b'8\001'
  _ALLREDUCEINFO.fields_by_name['name']._options = None
  _ALLREDUCEINFO.fields_by_name['name']._serialized_options = b'\030\001'
  _PERCORESTEPINFO_STEPINFOPERCOREENTRY._options = None
  _PERCORESTEPINFO_STEPINFOPERCOREENTRY._serialized_options = b'8\001'
  _PERCORESTEPINFO_COREIDTOREPLICAIDMAPENTRY._options = None
  _PERCORESTEPINFO_COREIDTOREPLICAIDMAPENTRY._serialized_options = b'8\001'
  _PERCORESTEPINFO_ALLREDUCEDBPERCOREENTRY._options = None
  _PERCORESTEPINFO_ALLREDUCEDBPERCOREENTRY._serialized_options = b'8\001'
  _GENERICSTEPBREAKDOWN._serialized_start=171
  _GENERICSTEPBREAKDOWN._serialized_end=443
  _GENERICSTEPBREAKDOWN_TYPEPSENTRY._serialized_start=347
  _GENERICSTEPBREAKDOWN_TYPEPSENTRY._serialized_end=392
  _GENERICSTEPBREAKDOWN_CATEGORYPSENTRY._serialized_start=394
  _GENERICSTEPBREAKDOWN_CATEGORYPSENTRY._serialized_end=443
  _TPUSTEPBREAKDOWN._serialized_start=446
  _TPUSTEPBREAKDOWN._serialized_end=985
  _SPARSECORESTEPBREAKDOWN._serialized_start=988
  _SPARSECORESTEPBREAKDOWN._serialized_end=1121
  _DEVICEMEMORYTRANSFER._serialized_start=1123
  _DEVICEMEMORYTRANSFER._serialized_end=1209
  _STEPINFORESULT._serialized_start=1212
  _STEPINFORESULT._serialized_end=1414
  _ALLREDUCEINFO._serialized_start=1417
  _ALLREDUCEINFO._serialized_end=1548
  _ALLREDUCEDBRESULT._serialized_start=1550
  _ALLREDUCEDBRESULT._serialized_end=1630
  _PERCORESTEPINFO._serialized_start=1633
  _PERCORESTEPINFO._serialized_end=2341
  _PERCORESTEPINFO_STEPINFOPERCOREENTRY._serialized_start=2084
  _PERCORESTEPINFO_STEPINFOPERCOREENTRY._serialized_end=2175
  _PERCORESTEPINFO_COREIDTOREPLICAIDMAPENTRY._serialized_start=2177
  _PERCORESTEPINFO_COREIDTOREPLICAIDMAPENTRY._serialized_end=2236
  _PERCORESTEPINFO_ALLREDUCEDBPERCOREENTRY._serialized_start=2238
  _PERCORESTEPINFO_ALLREDUCEDBPERCOREENTRY._serialized_end=2335
  _STEPDATABASERESULT._serialized_start=2344
  _STEPDATABASERESULT._serialized_end=2506
# @@protoc_insertion_point(module_scope)
