# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/common/v1/operation_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nebius.api.buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from nebius.api.nebius.common.v1 import operation_pb2 as nebius_dot_common_dot_v1_dot_operation__pb2
from nebius.api.nebius import annotations_pb2 as nebius_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(nebius/common/v1/operation_service.proto\x12\x10nebius.common.v1\x1a\x1b\x62uf/validate/validate.proto\x1a nebius/common/v1/operation.proto\x1a\x18nebius/annotations.proto\"-\n\x13GetOperationRequest\x12\x16\n\x02id\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01R\x02id\"|\n\x15ListOperationsRequest\x12\'\n\x0bresource_id\x18\x01 \x01(\tB\x06\xbaH\x03\xc8\x01\x01R\nresourceId\x12\x1b\n\tpage_size\x18\x02 \x01(\x03R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"}\n\x16ListOperationsResponse\x12;\n\noperations\x18\x01 \x03(\x0b\x32\x1b.nebius.common.v1.OperationR\noperations\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken2\xcb\x01\n\x10OperationService\x12I\n\x03Get\x12%.nebius.common.v1.GetOperationRequest\x1a\x1b.nebius.common.v1.Operation\x12l\n\x04List\x12\'.nebius.common.v1.ListOperationsRequest\x1a(.nebius.common.v1.ListOperationsResponse\"\x11\x9a\xb5\x18\r\n\x0bresource_idBb\n\x17\x61i.nebius.pub.common.v1B\x15OperationServiceProtoP\x01Z.github.com/nebius/gosdk/proto/nebius/common/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.common.v1.operation_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027ai.nebius.pub.common.v1B\025OperationServiceProtoP\001Z.github.com/nebius/gosdk/proto/nebius/common/v1'
  _GETOPERATIONREQUEST.fields_by_name['id']._options = None
  _GETOPERATIONREQUEST.fields_by_name['id']._serialized_options = b'\272H\003\310\001\001'
  _LISTOPERATIONSREQUEST.fields_by_name['resource_id']._options = None
  _LISTOPERATIONSREQUEST.fields_by_name['resource_id']._serialized_options = b'\272H\003\310\001\001'
  _OPERATIONSERVICE.methods_by_name['List']._options = None
  _OPERATIONSERVICE.methods_by_name['List']._serialized_options = b'\232\265\030\r\n\013resource_id'
  _globals['_GETOPERATIONREQUEST']._serialized_start=151
  _globals['_GETOPERATIONREQUEST']._serialized_end=196
  _globals['_LISTOPERATIONSREQUEST']._serialized_start=198
  _globals['_LISTOPERATIONSREQUEST']._serialized_end=322
  _globals['_LISTOPERATIONSRESPONSE']._serialized_start=324
  _globals['_LISTOPERATIONSRESPONSE']._serialized_end=449
  _globals['_OPERATIONSERVICE']._serialized_start=452
  _globals['_OPERATIONSERVICE']._serialized_end=655
# @@protoc_insertion_point(module_scope)
