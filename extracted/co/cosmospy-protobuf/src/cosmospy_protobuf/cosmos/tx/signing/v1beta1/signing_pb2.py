"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....cosmos.crypto.multisig.v1beta1 import multisig_pb2 as cosmos_dot_crypto_dot_multisig_dot_v1beta1_dot_multisig__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'cosmos/tx/signing/v1beta1/signing.proto\x12\x19cosmos.tx.signing.v1beta1\x1a-cosmos/crypto/multisig/v1beta1/multisig.proto\x1a\x19google/protobuf/any.proto"Z\n\x14SignatureDescriptors\x12B\n\nsignatures\x18\x01 \x03(\x0b2..cosmos.tx.signing.v1beta1.SignatureDescriptor"\xa4\x04\n\x13SignatureDescriptor\x12(\n\npublic_key\x18\x01 \x01(\x0b2\x14.google.protobuf.Any\x12A\n\x04data\x18\x02 \x01(\x0b23.cosmos.tx.signing.v1beta1.SignatureDescriptor.Data\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x1a\x8d\x03\n\x04Data\x12L\n\x06single\x18\x01 \x01(\x0b2:.cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.SingleH\x00\x12J\n\x05multi\x18\x02 \x01(\x0b29.cosmos.tx.signing.v1beta1.SignatureDescriptor.Data.MultiH\x00\x1aN\n\x06Single\x121\n\x04mode\x18\x01 \x01(\x0e2#.cosmos.tx.signing.v1beta1.SignMode\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x1a\x93\x01\n\x05Multi\x12A\n\x08bitarray\x18\x01 \x01(\x0b2/.cosmos.crypto.multisig.v1beta1.CompactBitArray\x12G\n\nsignatures\x18\x02 \x03(\x0b23.cosmos.tx.signing.v1beta1.SignatureDescriptor.DataB\x05\n\x03sum*\x8b\x01\n\x08SignMode\x12\x19\n\x15SIGN_MODE_UNSPECIFIED\x10\x00\x12\x14\n\x10SIGN_MODE_DIRECT\x10\x01\x12\x15\n\x11SIGN_MODE_TEXTUAL\x10\x02\x12\x1f\n\x1bSIGN_MODE_LEGACY_AMINO_JSON\x10\x7f\x12\x16\n\x11SIGN_MODE_EIP_191\x10\xbf\x01B/Z-github.com/cosmos/cosmos-sdk/types/tx/signingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.tx.signing.v1beta1.signing_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/types/tx/signing'
    _globals['_SIGNMODE']._serialized_start = 788
    _globals['_SIGNMODE']._serialized_end = 927
    _globals['_SIGNATUREDESCRIPTORS']._serialized_start = 144
    _globals['_SIGNATUREDESCRIPTORS']._serialized_end = 234
    _globals['_SIGNATUREDESCRIPTOR']._serialized_start = 237
    _globals['_SIGNATUREDESCRIPTOR']._serialized_end = 785
    _globals['_SIGNATUREDESCRIPTOR_DATA']._serialized_start = 388
    _globals['_SIGNATUREDESCRIPTOR_DATA']._serialized_end = 785
    _globals['_SIGNATUREDESCRIPTOR_DATA_SINGLE']._serialized_start = 550
    _globals['_SIGNATUREDESCRIPTOR_DATA_SINGLE']._serialized_end = 628
    _globals['_SIGNATUREDESCRIPTOR_DATA_MULTI']._serialized_start = 631
    _globals['_SIGNATUREDESCRIPTOR_DATA_MULTI']._serialized_end = 778