# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chalk/server/v1/flag.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chalk._gen.chalk.auth.v1 import permissions_pb2 as chalk_dot_auth_dot_v1_dot_permissions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1a\x63halk/server/v1/flag.proto\x12\x0f\x63halk.server.v1\x1a\x1f\x63halk/auth/v1/permissions.proto"<\n\x10\x46\x65\x61tureFlagValue\x12\x12\n\x04\x66lag\x18\x01 \x01(\tR\x04\x66lag\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value"\x18\n\x16GetFeatureFlagsRequest"R\n\x17GetFeatureFlagsResponse\x12\x37\n\x05\x66lags\x18\x01 \x03(\x0b\x32!.chalk.server.v1.FeatureFlagValueR\x05\x66lags"s\n\x15SetFeatureFlagRequest\x12\x12\n\x04\x66lag\x18\x01 \x01(\tR\x04\x66lag\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value\x12\x30\n\x05scope\x18\x03 \x01(\x0e\x32\x1a.chalk.server.v1.FlagScopeR\x05scope"\x18\n\x16SetFeatureFlagResponse*X\n\tFlagScope\x12\x1a\n\x16\x46LAG_SCOPE_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x46LAG_SCOPE_TEAM\x10\x01\x12\x1a\n\x16\x46LAG_SCOPE_ENVIRONMENT\x10\x02\x32\xed\x01\n\x12\x46\x65\x61tureFlagService\x12l\n\x0fGetFeatureFlags\x12\'.chalk.server.v1.GetFeatureFlagsRequest\x1a(.chalk.server.v1.GetFeatureFlagsResponse"\x06\x90\x02\x01\x80}\x02\x12i\n\x0eSetFeatureFlag\x12&.chalk.server.v1.SetFeatureFlagRequest\x1a\'.chalk.server.v1.SetFeatureFlagResponse"\x06\x90\x02\x02\x80}\x1b\x42\x92\x01\n\x13\x63om.chalk.server.v1B\tFlagProtoP\x01Z\x12server/v1;serverv1\xa2\x02\x03\x43SX\xaa\x02\x0f\x43halk.Server.V1\xca\x02\x0f\x43halk\\Server\\V1\xe2\x02\x1b\x43halk\\Server\\V1\\GPBMetadata\xea\x02\x11\x43halk::Server::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "chalk.server.v1.flag_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\023com.chalk.server.v1B\tFlagProtoP\001Z\022server/v1;serverv1\242\002\003CSX\252\002\017Chalk.Server.V1\312\002\017Chalk\\Server\\V1\342\002\033Chalk\\Server\\V1\\GPBMetadata\352\002\021Chalk::Server::V1"
    _globals["_FEATUREFLAGSERVICE"].methods_by_name["GetFeatureFlags"]._options = None
    _globals["_FEATUREFLAGSERVICE"].methods_by_name["GetFeatureFlags"]._serialized_options = b"\220\002\001\200}\002"
    _globals["_FEATUREFLAGSERVICE"].methods_by_name["SetFeatureFlag"]._options = None
    _globals["_FEATUREFLAGSERVICE"].methods_by_name["SetFeatureFlag"]._serialized_options = b"\220\002\002\200}\033"
    _globals["_FLAGSCOPE"]._serialized_start = 395
    _globals["_FLAGSCOPE"]._serialized_end = 483
    _globals["_FEATUREFLAGVALUE"]._serialized_start = 80
    _globals["_FEATUREFLAGVALUE"]._serialized_end = 140
    _globals["_GETFEATUREFLAGSREQUEST"]._serialized_start = 142
    _globals["_GETFEATUREFLAGSREQUEST"]._serialized_end = 166
    _globals["_GETFEATUREFLAGSRESPONSE"]._serialized_start = 168
    _globals["_GETFEATUREFLAGSRESPONSE"]._serialized_end = 250
    _globals["_SETFEATUREFLAGREQUEST"]._serialized_start = 252
    _globals["_SETFEATUREFLAGREQUEST"]._serialized_end = 367
    _globals["_SETFEATUREFLAGRESPONSE"]._serialized_start = 369
    _globals["_SETFEATUREFLAGRESPONSE"]._serialized_end = 393
    _globals["_FEATUREFLAGSERVICE"]._serialized_start = 486
    _globals["_FEATUREFLAGSERVICE"]._serialized_end = 723
# @@protoc_insertion_point(module_scope)
