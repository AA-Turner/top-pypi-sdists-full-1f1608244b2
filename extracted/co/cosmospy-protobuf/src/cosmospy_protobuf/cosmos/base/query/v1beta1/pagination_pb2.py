"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*cosmos/base/query/v1beta1/pagination.proto\x12\x19cosmos.base.query.v1beta1"_\n\x0bPageRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\r\n\x05limit\x18\x03 \x01(\x04\x12\x13\n\x0bcount_total\x18\x04 \x01(\x08\x12\x0f\n\x07reverse\x18\x05 \x01(\x08"/\n\x0cPageResponse\x12\x10\n\x08next_key\x18\x01 \x01(\x0c\x12\r\n\x05total\x18\x02 \x01(\x04B*Z(github.com/cosmos/cosmos-sdk/types/queryb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.query.v1beta1.pagination_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z(github.com/cosmos/cosmos-sdk/types/query'
    _globals['_PAGEREQUEST']._serialized_start = 73
    _globals['_PAGEREQUEST']._serialized_end = 168
    _globals['_PAGERESPONSE']._serialized_start = 170
    _globals['_PAGERESPONSE']._serialized_end = 217