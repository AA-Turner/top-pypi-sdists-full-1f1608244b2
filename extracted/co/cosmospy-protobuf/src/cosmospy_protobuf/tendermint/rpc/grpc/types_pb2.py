"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ftendermint/rpc/grpc/types.proto\x12\x13tendermint.rpc.grpc\x1a\x1btendermint/abci/types.proto"\r\n\x0bRequestPing" \n\x12RequestBroadcastTx\x12\n\n\x02tx\x18\x01 \x01(\x0c"\x0e\n\x0cResponsePing"\x81\x01\n\x13ResponseBroadcastTx\x122\n\x08check_tx\x18\x01 \x01(\x0b2 .tendermint.abci.ResponseCheckTx\x126\n\ndeliver_tx\x18\x02 \x01(\x0b2".tendermint.abci.ResponseDeliverTx2\xbd\x01\n\x0cBroadcastAPI\x12K\n\x04Ping\x12 .tendermint.rpc.grpc.RequestPing\x1a!.tendermint.rpc.grpc.ResponsePing\x12`\n\x0bBroadcastTx\x12\'.tendermint.rpc.grpc.RequestBroadcastTx\x1a(.tendermint.rpc.grpc.ResponseBroadcastTxB4Z2github.com/tendermint/tendermint/rpc/grpc;coregrpcb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.rpc.grpc.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/tendermint/tendermint/rpc/grpc;coregrpc'
    _globals['_REQUESTPING']._serialized_start = 85
    _globals['_REQUESTPING']._serialized_end = 98
    _globals['_REQUESTBROADCASTTX']._serialized_start = 100
    _globals['_REQUESTBROADCASTTX']._serialized_end = 132
    _globals['_RESPONSEPING']._serialized_start = 134
    _globals['_RESPONSEPING']._serialized_end = 148
    _globals['_RESPONSEBROADCASTTX']._serialized_start = 151
    _globals['_RESPONSEBROADCASTTX']._serialized_end = 280
    _globals['_BROADCASTAPI']._serialized_start = 283
    _globals['_BROADCASTAPI']._serialized_end = 472