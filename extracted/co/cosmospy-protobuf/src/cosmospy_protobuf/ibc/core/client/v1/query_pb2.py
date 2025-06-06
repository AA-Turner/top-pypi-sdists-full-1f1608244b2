"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from .....ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eibc/core/client/v1/query.proto\x12\x12ibc.core.client.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1fibc/core/client/v1/client.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x14gogoproto/gogo.proto",\n\x17QueryClientStateRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t"\x8d\x01\n\x18QueryClientStateResponse\x12*\n\x0cclient_state\x18\x01 \x01(\x0b2\x14.google.protobuf.Any\x12\r\n\x05proof\x18\x02 \x01(\x0c\x126\n\x0cproof_height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"V\n\x18QueryClientStatesRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xba\x01\n\x19QueryClientStatesResponse\x12`\n\rclient_states\x18\x01 \x03(\x0b2).ibc.core.client.v1.IdentifiedClientStateB\x1e\xc8\xde\x1f\x00\xaa\xdf\x1f\x16IdentifiedClientStates\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"x\n\x1aQueryConsensusStateRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x17\n\x0frevision_number\x18\x02 \x01(\x04\x12\x17\n\x0frevision_height\x18\x03 \x01(\x04\x12\x15\n\rlatest_height\x18\x04 \x01(\x08"\x93\x01\n\x1bQueryConsensusStateResponse\x12-\n\x0fconsensus_state\x18\x01 \x01(\x0b2\x14.google.protobuf.Any\x12\r\n\x05proof\x18\x02 \x01(\x0c\x126\n\x0cproof_height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00"l\n\x1bQueryConsensusStatesRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xa9\x01\n\x1cQueryConsensusStatesResponse\x12L\n\x10consensus_states\x18\x01 \x03(\x0b2,.ibc.core.client.v1.ConsensusStateWithHeightB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"r\n!QueryConsensusStateHeightsRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xa4\x01\n"QueryConsensusStateHeightsResponse\x12A\n\x17consensus_state_heights\x18\x01 \x03(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"-\n\x18QueryClientStatusRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t"+\n\x19QueryClientStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\t"\x1a\n\x18QueryClientParamsRequest"G\n\x19QueryClientParamsResponse\x12*\n\x06params\x18\x01 \x01(\x0b2\x1a.ibc.core.client.v1.Params"!\n\x1fQueryUpgradedClientStateRequest"W\n QueryUpgradedClientStateResponse\x123\n\x15upgraded_client_state\x18\x01 \x01(\x0b2\x14.google.protobuf.Any"$\n"QueryUpgradedConsensusStateRequest"]\n#QueryUpgradedConsensusStateResponse\x126\n\x18upgraded_consensus_state\x18\x01 \x01(\x0b2\x14.google.protobuf.Any2\xcc\x0c\n\x05Query\x12\x9f\x01\n\x0bClientState\x12+.ibc.core.client.v1.QueryClientStateRequest\x1a,.ibc.core.client.v1.QueryClientStateResponse"5\x82\xd3\xe4\x93\x02/\x12-/ibc/core/client/v1/client_states/{client_id}\x12\x96\x01\n\x0cClientStates\x12,.ibc.core.client.v1.QueryClientStatesRequest\x1a-.ibc.core.client.v1.QueryClientStatesResponse")\x82\xd3\xe4\x93\x02#\x12!/ibc/core/client/v1/client_states\x12\xdf\x01\n\x0eConsensusState\x12..ibc.core.client.v1.QueryConsensusStateRequest\x1a/.ibc.core.client.v1.QueryConsensusStateResponse"l\x82\xd3\xe4\x93\x02f\x12d/ibc/core/client/v1/consensus_states/{client_id}/revision/{revision_number}/height/{revision_height}\x12\xae\x01\n\x0fConsensusStates\x12/.ibc.core.client.v1.QueryConsensusStatesRequest\x1a0.ibc.core.client.v1.QueryConsensusStatesResponse"8\x82\xd3\xe4\x93\x022\x120/ibc/core/client/v1/consensus_states/{client_id}\x12\xc8\x01\n\x15ConsensusStateHeights\x125.ibc.core.client.v1.QueryConsensusStateHeightsRequest\x1a6.ibc.core.client.v1.QueryConsensusStateHeightsResponse"@\x82\xd3\xe4\x93\x02:\x128/ibc/core/client/v1/consensus_states/{client_id}/heights\x12\xa2\x01\n\x0cClientStatus\x12,.ibc.core.client.v1.QueryClientStatusRequest\x1a-.ibc.core.client.v1.QueryClientStatusResponse"5\x82\xd3\xe4\x93\x02/\x12-/ibc/core/client/v1/client_status/{client_id}\x12\x8a\x01\n\x0cClientParams\x12,.ibc.core.client.v1.QueryClientParamsRequest\x1a-.ibc.core.client.v1.QueryClientParamsResponse"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/ibc/client/v1/params\x12\xb4\x01\n\x13UpgradedClientState\x123.ibc.core.client.v1.QueryUpgradedClientStateRequest\x1a4.ibc.core.client.v1.QueryUpgradedClientStateResponse"2\x82\xd3\xe4\x93\x02,\x12*/ibc/core/client/v1/upgraded_client_states\x12\xc0\x01\n\x16UpgradedConsensusState\x126.ibc.core.client.v1.QueryUpgradedConsensusStateRequest\x1a7.ibc.core.client.v1.QueryUpgradedConsensusStateResponse"5\x82\xd3\xe4\x93\x02/\x12-/ibc/core/client/v1/upgraded_consensus_statesB:Z8github.com/cosmos/ibc-go/v4/modules/core/02-client/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.client.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/cosmos/ibc-go/v4/modules/core/02-client/types'
    _QUERYCLIENTSTATERESPONSE.fields_by_name['proof_height']._options = None
    _QUERYCLIENTSTATERESPONSE.fields_by_name['proof_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYCLIENTSTATESRESPONSE.fields_by_name['client_states']._options = None
    _QUERYCLIENTSTATESRESPONSE.fields_by_name['client_states']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\x16IdentifiedClientStates'
    _QUERYCONSENSUSSTATERESPONSE.fields_by_name['proof_height']._options = None
    _QUERYCONSENSUSSTATERESPONSE.fields_by_name['proof_height']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYCONSENSUSSTATESRESPONSE.fields_by_name['consensus_states']._options = None
    _QUERYCONSENSUSSTATESRESPONSE.fields_by_name['consensus_states']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYCONSENSUSSTATEHEIGHTSRESPONSE.fields_by_name['consensus_state_heights']._options = None
    _QUERYCONSENSUSSTATEHEIGHTSRESPONSE.fields_by_name['consensus_state_heights']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['ClientState']._options = None
    _QUERY.methods_by_name['ClientState']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/ibc/core/client/v1/client_states/{client_id}'
    _QUERY.methods_by_name['ClientStates']._options = None
    _QUERY.methods_by_name['ClientStates']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/ibc/core/client/v1/client_states'
    _QUERY.methods_by_name['ConsensusState']._options = None
    _QUERY.methods_by_name['ConsensusState']._serialized_options = b'\x82\xd3\xe4\x93\x02f\x12d/ibc/core/client/v1/consensus_states/{client_id}/revision/{revision_number}/height/{revision_height}'
    _QUERY.methods_by_name['ConsensusStates']._options = None
    _QUERY.methods_by_name['ConsensusStates']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/ibc/core/client/v1/consensus_states/{client_id}'
    _QUERY.methods_by_name['ConsensusStateHeights']._options = None
    _QUERY.methods_by_name['ConsensusStateHeights']._serialized_options = b'\x82\xd3\xe4\x93\x02:\x128/ibc/core/client/v1/consensus_states/{client_id}/heights'
    _QUERY.methods_by_name['ClientStatus']._options = None
    _QUERY.methods_by_name['ClientStatus']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/ibc/core/client/v1/client_status/{client_id}'
    _QUERY.methods_by_name['ClientParams']._options = None
    _QUERY.methods_by_name['ClientParams']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17\x12\x15/ibc/client/v1/params'
    _QUERY.methods_by_name['UpgradedClientState']._options = None
    _QUERY.methods_by_name['UpgradedClientState']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/ibc/core/client/v1/upgraded_client_states'
    _QUERY.methods_by_name['UpgradedConsensusState']._options = None
    _QUERY.methods_by_name['UpgradedConsensusState']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/ibc/core/client/v1/upgraded_consensus_states'
    _globals['_QUERYCLIENTSTATEREQUEST']._serialized_start = 210
    _globals['_QUERYCLIENTSTATEREQUEST']._serialized_end = 254
    _globals['_QUERYCLIENTSTATERESPONSE']._serialized_start = 257
    _globals['_QUERYCLIENTSTATERESPONSE']._serialized_end = 398
    _globals['_QUERYCLIENTSTATESREQUEST']._serialized_start = 400
    _globals['_QUERYCLIENTSTATESREQUEST']._serialized_end = 486
    _globals['_QUERYCLIENTSTATESRESPONSE']._serialized_start = 489
    _globals['_QUERYCLIENTSTATESRESPONSE']._serialized_end = 675
    _globals['_QUERYCONSENSUSSTATEREQUEST']._serialized_start = 677
    _globals['_QUERYCONSENSUSSTATEREQUEST']._serialized_end = 797
    _globals['_QUERYCONSENSUSSTATERESPONSE']._serialized_start = 800
    _globals['_QUERYCONSENSUSSTATERESPONSE']._serialized_end = 947
    _globals['_QUERYCONSENSUSSTATESREQUEST']._serialized_start = 949
    _globals['_QUERYCONSENSUSSTATESREQUEST']._serialized_end = 1057
    _globals['_QUERYCONSENSUSSTATESRESPONSE']._serialized_start = 1060
    _globals['_QUERYCONSENSUSSTATESRESPONSE']._serialized_end = 1229
    _globals['_QUERYCONSENSUSSTATEHEIGHTSREQUEST']._serialized_start = 1231
    _globals['_QUERYCONSENSUSSTATEHEIGHTSREQUEST']._serialized_end = 1345
    _globals['_QUERYCONSENSUSSTATEHEIGHTSRESPONSE']._serialized_start = 1348
    _globals['_QUERYCONSENSUSSTATEHEIGHTSRESPONSE']._serialized_end = 1512
    _globals['_QUERYCLIENTSTATUSREQUEST']._serialized_start = 1514
    _globals['_QUERYCLIENTSTATUSREQUEST']._serialized_end = 1559
    _globals['_QUERYCLIENTSTATUSRESPONSE']._serialized_start = 1561
    _globals['_QUERYCLIENTSTATUSRESPONSE']._serialized_end = 1604
    _globals['_QUERYCLIENTPARAMSREQUEST']._serialized_start = 1606
    _globals['_QUERYCLIENTPARAMSREQUEST']._serialized_end = 1632
    _globals['_QUERYCLIENTPARAMSRESPONSE']._serialized_start = 1634
    _globals['_QUERYCLIENTPARAMSRESPONSE']._serialized_end = 1705
    _globals['_QUERYUPGRADEDCLIENTSTATEREQUEST']._serialized_start = 1707
    _globals['_QUERYUPGRADEDCLIENTSTATEREQUEST']._serialized_end = 1740
    _globals['_QUERYUPGRADEDCLIENTSTATERESPONSE']._serialized_start = 1742
    _globals['_QUERYUPGRADEDCLIENTSTATERESPONSE']._serialized_end = 1829
    _globals['_QUERYUPGRADEDCONSENSUSSTATEREQUEST']._serialized_start = 1831
    _globals['_QUERYUPGRADEDCONSENSUSSTATEREQUEST']._serialized_end = 1867
    _globals['_QUERYUPGRADEDCONSENSUSSTATERESPONSE']._serialized_start = 1869
    _globals['_QUERYUPGRADEDCONSENSUSSTATERESPONSE']._serialized_end = 1962
    _globals['_QUERY']._serialized_start = 1965
    _globals['_QUERY']._serialized_end = 3577