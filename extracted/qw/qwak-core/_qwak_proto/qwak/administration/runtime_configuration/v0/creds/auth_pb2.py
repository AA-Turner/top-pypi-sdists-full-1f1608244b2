# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/administration/runtime_configuration/v0/creds/auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from _qwak_proto.qwak.administration.runtime_configuration.v0.creds import secret_pb2 as qwak_dot_administration_dot_runtime__configuration_dot_v0_dot_creds_dot_secret__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=qwak/administration/runtime_configuration/v0/creds/auth.proto\x12\x37qwak.administration.runtime_configuration.v0.creds.auth\x1a?qwak/administration/runtime_configuration/v0/creds/secret.proto\"\xc1\x01\n\tBasicAuth\x12Y\n\x08username\x18\x01 \x01(\x0b\x32G.qwak.administration.runtime_configuration.v0.creds.secret.SecretKeyRef\x12Y\n\x08password\x18\x02 \x01(\x0b\x32G.qwak.administration.runtime_configuration.v0.creds.secret.SecretKeyRefB\xe3\x01\n0com.jfrog.ml.runtime_configuration.v0.creds.authP\x01Z\xac\x01github.com/qwak-ai/qwak-platform/services/core/java/user-management/user-management-api/pb/qwak/administration/runtime_configuration/v0/creds;runtime_configuration_v0_credsb\x06proto3')



_BASICAUTH = DESCRIPTOR.message_types_by_name['BasicAuth']
BasicAuth = _reflection.GeneratedProtocolMessageType('BasicAuth', (_message.Message,), {
  'DESCRIPTOR' : _BASICAUTH,
  '__module__' : 'qwak.administration.runtime_configuration.v0.creds.auth_pb2'
  # @@protoc_insertion_point(class_scope:qwak.administration.runtime_configuration.v0.creds.auth.BasicAuth)
  })
_sym_db.RegisterMessage(BasicAuth)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n0com.jfrog.ml.runtime_configuration.v0.creds.authP\001Z\254\001github.com/qwak-ai/qwak-platform/services/core/java/user-management/user-management-api/pb/qwak/administration/runtime_configuration/v0/creds;runtime_configuration_v0_creds'
  _BASICAUTH._serialized_start=188
  _BASICAUTH._serialized_end=381
# @@protoc_insertion_point(module_scope)
