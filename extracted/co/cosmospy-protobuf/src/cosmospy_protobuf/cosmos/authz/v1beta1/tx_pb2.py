"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos.base.abci.v1beta1 import abci_pb2 as cosmos_dot_base_dot_abci_dot_v1beta1_dot_abci__pb2
from ....cosmos.authz.v1beta1 import authz_pb2 as cosmos_dot_authz_dot_v1beta1_dot_authz__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dcosmos/authz/v1beta1/tx.proto\x12\x14cosmos.authz.v1beta1\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\x1a#cosmos/base/abci/v1beta1/abci.proto\x1a cosmos/authz/v1beta1/authz.proto"^\n\x08MsgGrant\x12\x0f\n\x07granter\x18\x01 \x01(\t\x12\x0f\n\x07grantee\x18\x02 \x01(\t\x120\n\x05grant\x18\x03 \x01(\x0b2\x1b.cosmos.authz.v1beta1.GrantB\x04\xc8\xde\x1f\x00""\n\x0fMsgExecResponse\x12\x0f\n\x07results\x18\x01 \x03(\x0c"`\n\x07MsgExec\x12\x0f\n\x07grantee\x18\x01 \x01(\t\x12D\n\x04msgs\x18\x02 \x03(\x0b2\x14.google.protobuf.AnyB \xca\xb4-\x1csdk.Msg, authz.Authorization"\x12\n\x10MsgGrantResponse"C\n\tMsgRevoke\x12\x0f\n\x07granter\x18\x01 \x01(\t\x12\x0f\n\x07grantee\x18\x02 \x01(\t\x12\x14\n\x0cmsg_type_url\x18\x03 \x01(\t"\x13\n\x11MsgRevokeResponse2\xf8\x01\n\x03Msg\x12O\n\x05Grant\x12\x1e.cosmos.authz.v1beta1.MsgGrant\x1a&.cosmos.authz.v1beta1.MsgGrantResponse\x12L\n\x04Exec\x12\x1d.cosmos.authz.v1beta1.MsgExec\x1a%.cosmos.authz.v1beta1.MsgExecResponse\x12R\n\x06Revoke\x12\x1f.cosmos.authz.v1beta1.MsgRevoke\x1a\'.cosmos.authz.v1beta1.MsgRevokeResponseB*Z$github.com/cosmos/cosmos-sdk/x/authz\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.authz.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/authz\xc8\xe1\x1e\x00'
    _MSGGRANT.fields_by_name['grant']._options = None
    _MSGGRANT.fields_by_name['grant']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGEXEC.fields_by_name['msgs']._options = None
    _MSGEXEC.fields_by_name['msgs']._serialized_options = b'\xca\xb4-\x1csdk.Msg, authz.Authorization'
    _globals['_MSGGRANT']._serialized_start = 235
    _globals['_MSGGRANT']._serialized_end = 329
    _globals['_MSGEXECRESPONSE']._serialized_start = 331
    _globals['_MSGEXECRESPONSE']._serialized_end = 365
    _globals['_MSGEXEC']._serialized_start = 367
    _globals['_MSGEXEC']._serialized_end = 463
    _globals['_MSGGRANTRESPONSE']._serialized_start = 465
    _globals['_MSGGRANTRESPONSE']._serialized_end = 483
    _globals['_MSGREVOKE']._serialized_start = 485
    _globals['_MSGREVOKE']._serialized_end = 552
    _globals['_MSGREVOKERESPONSE']._serialized_start = 554
    _globals['_MSGREVOKERESPONSE']._serialized_end = 573
    _globals['_MSG']._serialized_start = 576
    _globals['_MSG']._serialized_end = 824