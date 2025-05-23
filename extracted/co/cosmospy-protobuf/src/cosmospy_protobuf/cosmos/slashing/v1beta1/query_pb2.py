"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.slashing.v1beta1 import slashing_pb2 as cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cosmos/slashing/v1beta1/query.proto\x12\x17cosmos.slashing.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a&cosmos/slashing/v1beta1/slashing.proto"\x14\n\x12QueryParamsRequest"L\n\x13QueryParamsResponse\x125\n\x06params\x18\x01 \x01(\x0b2\x1f.cosmos.slashing.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"/\n\x17QuerySigningInfoRequest\x12\x14\n\x0ccons_address\x18\x01 \x01(\t"i\n\x18QuerySigningInfoResponse\x12M\n\x10val_signing_info\x18\x01 \x01(\x0b2-.cosmos.slashing.v1beta1.ValidatorSigningInfoB\x04\xc8\xde\x1f\x00"V\n\x18QuerySigningInfosRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x9b\x01\n\x19QuerySigningInfosResponse\x12A\n\x04info\x18\x01 \x03(\x0b2-.cosmos.slashing.v1beta1.ValidatorSigningInfoB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse2\xf2\x03\n\x05Query\x12\x8c\x01\n\x06Params\x12+.cosmos.slashing.v1beta1.QueryParamsRequest\x1a,.cosmos.slashing.v1beta1.QueryParamsResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/cosmos/slashing/v1beta1/params\x12\xb1\x01\n\x0bSigningInfo\x120.cosmos.slashing.v1beta1.QuerySigningInfoRequest\x1a1.cosmos.slashing.v1beta1.QuerySigningInfoResponse"=\x82\xd3\xe4\x93\x027\x125/cosmos/slashing/v1beta1/signing_infos/{cons_address}\x12\xa5\x01\n\x0cSigningInfos\x121.cosmos.slashing.v1beta1.QuerySigningInfosRequest\x1a2.cosmos.slashing.v1beta1.QuerySigningInfosResponse".\x82\xd3\xe4\x93\x02(\x12&/cosmos/slashing/v1beta1/signing_infosB/Z-github.com/cosmos/cosmos-sdk/x/slashing/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.slashing.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYSIGNINGINFORESPONSE.fields_by_name['val_signing_info']._options = None
    _QUERYSIGNINGINFORESPONSE.fields_by_name['val_signing_info']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYSIGNINGINFOSRESPONSE.fields_by_name['info']._options = None
    _QUERYSIGNINGINFOSRESPONSE.fields_by_name['info']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/cosmos/slashing/v1beta1/params'
    _QUERY.methods_by_name['SigningInfo']._options = None
    _QUERY.methods_by_name['SigningInfo']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/cosmos/slashing/v1beta1/signing_infos/{cons_address}'
    _QUERY.methods_by_name['SigningInfos']._options = None
    _QUERY.methods_by_name['SigningInfos']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/cosmos/slashing/v1beta1/signing_infos'
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 200
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 220
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 222
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 298
    _globals['_QUERYSIGNINGINFOREQUEST']._serialized_start = 300
    _globals['_QUERYSIGNINGINFOREQUEST']._serialized_end = 347
    _globals['_QUERYSIGNINGINFORESPONSE']._serialized_start = 349
    _globals['_QUERYSIGNINGINFORESPONSE']._serialized_end = 454
    _globals['_QUERYSIGNINGINFOSREQUEST']._serialized_start = 456
    _globals['_QUERYSIGNINGINFOSREQUEST']._serialized_end = 542
    _globals['_QUERYSIGNINGINFOSRESPONSE']._serialized_start = 545
    _globals['_QUERYSIGNINGINFOSRESPONSE']._serialized_end = 700
    _globals['_QUERY']._serialized_start = 703
    _globals['_QUERY']._serialized_end = 1201