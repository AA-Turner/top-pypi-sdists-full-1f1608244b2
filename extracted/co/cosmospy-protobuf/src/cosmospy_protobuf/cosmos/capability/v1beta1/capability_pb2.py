"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*cosmos/capability/v1beta1/capability.proto\x12\x19cosmos.capability.v1beta1\x1a\x14gogoproto/gogo.proto"3\n\nCapability\x12\x1f\n\x05index\x18\x01 \x01(\x04B\x10\xf2\xde\x1f\x0cyaml:"index":\x04\x98\xa0\x1f\x00"S\n\x05Owner\x12!\n\x06module\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"module"\x12\x1d\n\x04name\x18\x02 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:"name":\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00"J\n\x10CapabilityOwners\x126\n\x06owners\x18\x01 \x03(\x0b2 .cosmos.capability.v1beta1.OwnerB\x04\xc8\xde\x1f\x00B1Z/github.com/cosmos/cosmos-sdk/x/capability/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.capability.v1beta1.capability_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z/github.com/cosmos/cosmos-sdk/x/capability/types'
    _CAPABILITY.fields_by_name['index']._options = None
    _CAPABILITY.fields_by_name['index']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"index"'
    _CAPABILITY._options = None
    _CAPABILITY._serialized_options = b'\x98\xa0\x1f\x00'
    _OWNER.fields_by_name['module']._options = None
    _OWNER.fields_by_name['module']._serialized_options = b'\xf2\xde\x1f\ryaml:"module"'
    _OWNER.fields_by_name['name']._options = None
    _OWNER.fields_by_name['name']._serialized_options = b'\xf2\xde\x1f\x0byaml:"name"'
    _OWNER._options = None
    _OWNER._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _CAPABILITYOWNERS.fields_by_name['owners']._options = None
    _CAPABILITYOWNERS.fields_by_name['owners']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_CAPABILITY']._serialized_start = 95
    _globals['_CAPABILITY']._serialized_end = 146
    _globals['_OWNER']._serialized_start = 148
    _globals['_OWNER']._serialized_end = 231
    _globals['_CAPABILITYOWNERS']._serialized_start = 233
    _globals['_CAPABILITYOWNERS']._serialized_end = 307