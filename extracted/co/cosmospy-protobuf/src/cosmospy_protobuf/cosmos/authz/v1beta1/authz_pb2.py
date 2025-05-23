"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/authz/v1beta1/authz.proto\x12\x14cosmos.authz.v1beta1\x1a\x19cosmos_proto/cosmos.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto"6\n\x14GenericAuthorization\x12\x0b\n\x03msg\x18\x01 \x01(\t:\x11\xca\xb4-\rAuthorization"\x81\x01\n\x05Grant\x12>\n\rauthorization\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB\x11\xca\xb4-\rAuthorization\x128\n\nexpiration\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01"\xb0\x01\n\x12GrantAuthorization\x12\x0f\n\x07granter\x18\x01 \x01(\t\x12\x0f\n\x07grantee\x18\x02 \x01(\t\x12>\n\rauthorization\x18\x03 \x01(\x0b2\x14.google.protobuf.AnyB\x11\xca\xb4-\rAuthorization\x128\n\nexpiration\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01B*Z$github.com/cosmos/cosmos-sdk/x/authz\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.authz.v1beta1.authz_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/authz\xc8\xe1\x1e\x00'
    _GENERICAUTHORIZATION._options = None
    _GENERICAUTHORIZATION._serialized_options = b'\xca\xb4-\rAuthorization'
    _GRANT.fields_by_name['authorization']._options = None
    _GRANT.fields_by_name['authorization']._serialized_options = b'\xca\xb4-\rAuthorization'
    _GRANT.fields_by_name['expiration']._options = None
    _GRANT.fields_by_name['expiration']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _GRANTAUTHORIZATION.fields_by_name['authorization']._options = None
    _GRANTAUTHORIZATION.fields_by_name['authorization']._serialized_options = b'\xca\xb4-\rAuthorization'
    _GRANTAUTHORIZATION.fields_by_name['expiration']._options = None
    _GRANTAUTHORIZATION.fields_by_name['expiration']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _globals['_GENERICAUTHORIZATION']._serialized_start = 167
    _globals['_GENERICAUTHORIZATION']._serialized_end = 221
    _globals['_GRANT']._serialized_start = 224
    _globals['_GRANT']._serialized_end = 353
    _globals['_GRANTAUTHORIZATION']._serialized_start = 356
    _globals['_GRANTAUTHORIZATION']._serialized_end = 532