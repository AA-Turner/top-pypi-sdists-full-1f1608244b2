# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/databricks_api/secrets__client.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1tecton_proto/databricks_api/secrets__client.proto\x12\x1btecton_proto.databricks_api\"*\n\x12ScopeCreateRequest\x12\x14\n\x05scope\x18\x01 \x01(\tR\x05scope\"`\n\x18ListSecretScopesResponse\x12\x44\n\x06scopes\x18\x01 \x03(\x0b\x32,.tecton_proto.databricks_api.SecretScopeInfoR\x06scopes\"H\n\x0fSecretScopeInfo\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12!\n\x0c\x62\x61\x63kend_type\x18\x02 \x01(\tR\x0b\x62\x61\x63kendType\"]\n\x10SecretPutRequest\x12\x14\n\x05scope\x18\x01 \x01(\tR\x05scope\x12\x10\n\x03key\x18\x02 \x01(\tR\x03key\x12!\n\x0cstring_value\x18\x03 \x01(\tR\x0bstringValue\"i\n\x13SecretAclPutRequest\x12\x14\n\x05scope\x18\x01 \x01(\tR\x05scope\x12\x1c\n\tprincipal\x18\x02 \x01(\tR\tprincipal\x12\x1e\n\npermission\x18\x03 \x01(\tR\npermission\"Z\n\nPutRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12\x1a\n\x08\x63ontents\x18\x02 \x01(\x0cR\x08\x63ontents\x12\x1c\n\toverwrite\x18\x03 \x01(\x08R\toverwriteB\x1d\n\x19\x63om.tecton.databricks_apiP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.databricks_api.secrets__client_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.tecton.databricks_apiP\001'
  _SCOPECREATEREQUEST._serialized_start=82
  _SCOPECREATEREQUEST._serialized_end=124
  _LISTSECRETSCOPESRESPONSE._serialized_start=126
  _LISTSECRETSCOPESRESPONSE._serialized_end=222
  _SECRETSCOPEINFO._serialized_start=224
  _SECRETSCOPEINFO._serialized_end=296
  _SECRETPUTREQUEST._serialized_start=298
  _SECRETPUTREQUEST._serialized_end=391
  _SECRETACLPUTREQUEST._serialized_start=393
  _SECRETACLPUTREQUEST._serialized_end=498
  _PUTREQUEST._serialized_start=500
  _PUTREQUEST._serialized_end=590
# @@protoc_insertion_point(module_scope)
