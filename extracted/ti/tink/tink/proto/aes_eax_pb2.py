# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tink/proto/aes_eax.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'tink/proto/aes_eax.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18tink/proto/aes_eax.proto\x12\x12google.crypto.tink\"\x1f\n\x0c\x41\x65sEaxParams\x12\x0f\n\x07iv_size\x18\x01 \x01(\r\"U\n\x0f\x41\x65sEaxKeyFormat\x12\x30\n\x06params\x18\x01 \x01(\x0b\x32 .google.crypto.tink.AesEaxParams\x12\x10\n\x08key_size\x18\x02 \x01(\r\"a\n\tAesEaxKey\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x30\n\x06params\x18\x02 \x01(\x0b\x32 .google.crypto.tink.AesEaxParams\x12\x11\n\tkey_value\x18\x03 \x01(\x0c\x42Z\n\x1c\x63om.google.crypto.tink.protoP\x01Z8github.com/tink-crypto/tink-go/v2/proto/aes_eax_go_protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tink.proto.aes_eax_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.google.crypto.tink.protoP\001Z8github.com/tink-crypto/tink-go/v2/proto/aes_eax_go_proto'
  _globals['_AESEAXPARAMS']._serialized_start=48
  _globals['_AESEAXPARAMS']._serialized_end=79
  _globals['_AESEAXKEYFORMAT']._serialized_start=81
  _globals['_AESEAXKEYFORMAT']._serialized_end=166
  _globals['_AESEAXKEY']._serialized_start=168
  _globals['_AESEAXKEY']._serialized_end=265
# @@protoc_insertion_point(module_scope)
