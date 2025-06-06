# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tink/proto/rsa_ssa_pss.proto
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
    'tink/proto/rsa_ssa_pss.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tink.proto import common_pb2 as tink_dot_proto_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ctink/proto/rsa_ssa_pss.proto\x12\x12google.crypto.tink\x1a\x17tink/proto/common.proto\"\x87\x01\n\x0fRsaSsaPssParams\x12.\n\x08sig_hash\x18\x01 \x01(\x0e\x32\x1c.google.crypto.tink.HashType\x12/\n\tmgf1_hash\x18\x02 \x01(\x0e\x32\x1c.google.crypto.tink.HashType\x12\x13\n\x0bsalt_length\x18\x03 \x01(\x05\"p\n\x12RsaSsaPssPublicKey\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x33\n\x06params\x18\x02 \x01(\x0b\x32#.google.crypto.tink.RsaSsaPssParams\x12\t\n\x01n\x18\x03 \x01(\x0c\x12\t\n\x01\x65\x18\x04 \x01(\x0c\"\xa8\x01\n\x13RsaSsaPssPrivateKey\x12\x0f\n\x07version\x18\x01 \x01(\r\x12:\n\npublic_key\x18\x02 \x01(\x0b\x32&.google.crypto.tink.RsaSsaPssPublicKey\x12\t\n\x01\x64\x18\x03 \x01(\x0c\x12\t\n\x01p\x18\x04 \x01(\x0c\x12\t\n\x01q\x18\x05 \x01(\x0c\x12\n\n\x02\x64p\x18\x06 \x01(\x0c\x12\n\n\x02\x64q\x18\x07 \x01(\x0c\x12\x0b\n\x03\x63rt\x18\x08 \x01(\x0c\"\x80\x01\n\x12RsaSsaPssKeyFormat\x12\x33\n\x06params\x18\x01 \x01(\x0b\x32#.google.crypto.tink.RsaSsaPssParams\x12\x1c\n\x14modulus_size_in_bits\x18\x02 \x01(\r\x12\x17\n\x0fpublic_exponent\x18\x03 \x01(\x0c\x42^\n\x1c\x63om.google.crypto.tink.protoP\x01Z<github.com/tink-crypto/tink-go/v2/proto/rsa_ssa_pss_go_protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tink.proto.rsa_ssa_pss_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.google.crypto.tink.protoP\001Z<github.com/tink-crypto/tink-go/v2/proto/rsa_ssa_pss_go_proto'
  _globals['_RSASSAPSSPARAMS']._serialized_start=78
  _globals['_RSASSAPSSPARAMS']._serialized_end=213
  _globals['_RSASSAPSSPUBLICKEY']._serialized_start=215
  _globals['_RSASSAPSSPUBLICKEY']._serialized_end=327
  _globals['_RSASSAPSSPRIVATEKEY']._serialized_start=330
  _globals['_RSASSAPSSPRIVATEKEY']._serialized_end=498
  _globals['_RSASSAPSSKEYFORMAT']._serialized_start=501
  _globals['_RSASSAPSSKEYFORMAT']._serialized_end=629
# @@protoc_insertion_point(module_scope)
