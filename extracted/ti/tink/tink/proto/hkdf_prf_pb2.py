# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tink/proto/hkdf_prf.proto
# Protobuf Python Version: 5.29.3
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
    3,
    '',
    'tink/proto/hkdf_prf.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tink.proto import common_pb2 as tink_dot_proto_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19tink/proto/hkdf_prf.proto\x12\x12google.crypto.tink\x1a\x17tink/proto/common.proto\"I\n\rHkdfPrfParams\x12*\n\x04hash\x18\x01 \x01(\x0e\x32\x1c.google.crypto.tink.HashType\x12\x0c\n\x04salt\x18\x02 \x01(\x0c\"c\n\nHkdfPrfKey\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x31\n\x06params\x18\x02 \x01(\x0b\x32!.google.crypto.tink.HkdfPrfParams\x12\x11\n\tkey_value\x18\x03 \x01(\x0c\"h\n\x10HkdfPrfKeyFormat\x12\x31\n\x06params\x18\x01 \x01(\x0b\x32!.google.crypto.tink.HkdfPrfParams\x12\x10\n\x08key_size\x18\x02 \x01(\r\x12\x0f\n\x07version\x18\x03 \x01(\rBX\n\x1c\x63om.google.crypto.tink.protoP\x01Z6github.com/tink-crypto/tink-go/v2/proto/hkdf_prf_protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tink.proto.hkdf_prf_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.google.crypto.tink.protoP\001Z6github.com/tink-crypto/tink-go/v2/proto/hkdf_prf_proto'
  _globals['_HKDFPRFPARAMS']._serialized_start=74
  _globals['_HKDFPRFPARAMS']._serialized_end=147
  _globals['_HKDFPRFKEY']._serialized_start=149
  _globals['_HKDFPRFKEY']._serialized_end=248
  _globals['_HKDFPRFKEYFORMAT']._serialized_start=250
  _globals['_HKDFPRFKEYFORMAT']._serialized_end=354
# @@protoc_insertion_point(module_scope)
