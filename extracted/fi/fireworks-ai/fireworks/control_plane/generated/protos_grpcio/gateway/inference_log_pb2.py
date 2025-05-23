# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gateway/inference_log.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'gateway/inference_log.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as gateway_dot_options__pb2
from ..google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ..google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bgateway/inference_log.proto\x12\x07gateway\x1a\x15gateway/options.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xab\x04\n\x0cInferenceLog\x12\x13\n\x04name\x18\x01 \x01(\tB\x05\xe2\x41\x02\x03\x05\x12\x36\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x05\xe2\x41\x02\x03\x05\x12\x13\n\x05model\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03\x12\x1a\n\x0crequest_type\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03\x12\x1b\n\rinput_content\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03\x12\x1c\n\x0eoutput_content\x18\x06 \x01(\tB\x04\xe2\x41\x01\x03\x12\x19\n\x0b\x64uration_ms\x18\x07 \x01(\x03\x42\x04\xe2\x41\x01\x03\x12\x19\n\x0bstatus_code\x18\x08 \x01(\x05\x42\x04\xe2\x41\x01\x03\x12;\n\x08metadata\x18\t \x03(\x0b\x32#.gateway.InferenceLog.MetadataEntryB\x04\xe2\x41\x01\x03\x12\x35\n\x0bupdate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:\x86\x01\xea\x41t\n\x1d\x61pi.fireworks.ai/InferenceLog\x12\x34\x61\x63\x63ounts/{AccountId}/inference-logs/{InferenceLogId}*\x0einference-logs2\rinference-log\x82\xf1\x04\x0b\n\x07\x41\x63\x63ount\x10\x01\"a\n\x16GetInferenceLogRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x33\n\tread_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01\"/\n\x19\x44\x65leteInferenceLogRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"\xc6\x01\n\x18ListInferenceLogsRequest\x12\x14\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x17\n\tpage_size\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x01\x12\x18\n\npage_token\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01\x12\x14\n\x06\x66ilter\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01\x12\x16\n\x08order_by\x18\x05 \x01(\tB\x04\xe2\x41\x01\x01\x12\x33\n\tread_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01\"w\n\x19ListInferenceLogsResponse\x12-\n\x0einference_logs\x18\x01 \x03(\x0b\x32\x15.gateway.InferenceLog\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05\x42\x43ZAgithub.com/fw-ai/fireworks/control_plane/protos/generated/gatewayb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gateway.inference_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/fw-ai/fireworks/control_plane/protos/generated/gateway'
  _globals['_INFERENCELOG_METADATAENTRY']._loaded_options = None
  _globals['_INFERENCELOG_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_INFERENCELOG'].fields_by_name['name']._loaded_options = None
  _globals['_INFERENCELOG'].fields_by_name['name']._serialized_options = b'\342A\002\003\005'
  _globals['_INFERENCELOG'].fields_by_name['create_time']._loaded_options = None
  _globals['_INFERENCELOG'].fields_by_name['create_time']._serialized_options = b'\342A\002\003\005'
  _globals['_INFERENCELOG'].fields_by_name['model']._loaded_options = None
  _globals['_INFERENCELOG'].fields_by_name['model']._serialized_options = b'\342A\001\003'
  _globals['_INFERENCELOG'].fields_by_name['request_type']._loaded_options = None
  _globals['_INFERENCELOG'].fields_by_name['request_type']._serialized_options = b'\342A\001\003'
  _globals['_INFERENCELOG'].fields_by_name['input_content']._loaded_options = None
  _globals['_INFERENCELOG'].fields_by_name['input_content']._serialized_options = b'\342A\001\003'
  _globals['_INFERENCELOG'].fields_by_name['output_content']._loaded_options = None
  _globals['_INFERENCELOG'].fields_by_name['output_content']._serialized_options = b'\342A\001\003'
  _globals['_INFERENCELOG'].fields_by_name['duration_ms']._loaded_options = None
  _globals['_INFERENCELOG'].fields_by_name['duration_ms']._serialized_options = b'\342A\001\003'
  _globals['_INFERENCELOG'].fields_by_name['status_code']._loaded_options = None
  _globals['_INFERENCELOG'].fields_by_name['status_code']._serialized_options = b'\342A\001\003'
  _globals['_INFERENCELOG'].fields_by_name['metadata']._loaded_options = None
  _globals['_INFERENCELOG'].fields_by_name['metadata']._serialized_options = b'\342A\001\003'
  _globals['_INFERENCELOG'].fields_by_name['update_time']._loaded_options = None
  _globals['_INFERENCELOG'].fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _globals['_INFERENCELOG']._loaded_options = None
  _globals['_INFERENCELOG']._serialized_options = b'\352At\n\035api.fireworks.ai/InferenceLog\0224accounts/{AccountId}/inference-logs/{InferenceLogId}*\016inference-logs2\rinference-log\202\361\004\013\n\007Account\020\001'
  _globals['_GETINFERENCELOGREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_GETINFERENCELOGREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002'
  _globals['_GETINFERENCELOGREQUEST'].fields_by_name['read_mask']._loaded_options = None
  _globals['_GETINFERENCELOGREQUEST'].fields_by_name['read_mask']._serialized_options = b'\342A\001\001'
  _globals['_DELETEINFERENCELOGREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_DELETEINFERENCELOGREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002'
  _globals['_LISTINFERENCELOGSREQUEST'].fields_by_name['parent']._loaded_options = None
  _globals['_LISTINFERENCELOGSREQUEST'].fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _globals['_LISTINFERENCELOGSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTINFERENCELOGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _globals['_LISTINFERENCELOGSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTINFERENCELOGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _globals['_LISTINFERENCELOGSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTINFERENCELOGSREQUEST'].fields_by_name['filter']._serialized_options = b'\342A\001\001'
  _globals['_LISTINFERENCELOGSREQUEST'].fields_by_name['order_by']._loaded_options = None
  _globals['_LISTINFERENCELOGSREQUEST'].fields_by_name['order_by']._serialized_options = b'\342A\001\001'
  _globals['_LISTINFERENCELOGSREQUEST'].fields_by_name['read_mask']._loaded_options = None
  _globals['_LISTINFERENCELOGSREQUEST'].fields_by_name['read_mask']._serialized_options = b'\342A\001\001'
  _globals['_INFERENCELOG']._serialized_start=191
  _globals['_INFERENCELOG']._serialized_end=746
  _globals['_INFERENCELOG_METADATAENTRY']._serialized_start=562
  _globals['_INFERENCELOG_METADATAENTRY']._serialized_end=609
  _globals['_GETINFERENCELOGREQUEST']._serialized_start=748
  _globals['_GETINFERENCELOGREQUEST']._serialized_end=845
  _globals['_DELETEINFERENCELOGREQUEST']._serialized_start=847
  _globals['_DELETEINFERENCELOGREQUEST']._serialized_end=894
  _globals['_LISTINFERENCELOGSREQUEST']._serialized_start=897
  _globals['_LISTINFERENCELOGSREQUEST']._serialized_end=1095
  _globals['_LISTINFERENCELOGSRESPONSE']._serialized_start=1097
  _globals['_LISTINFERENCELOGSRESPONSE']._serialized_end=1216
# @@protoc_insertion_point(module_scope)
