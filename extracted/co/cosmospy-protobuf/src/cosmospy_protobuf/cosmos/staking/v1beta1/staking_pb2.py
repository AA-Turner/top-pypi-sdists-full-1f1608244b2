"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from ....tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/staking/v1beta1/staking.proto\x12\x16cosmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ctendermint/types/types.proto\x1a\x1btendermint/abci/types.proto"y\n\x0eHistoricalInfo\x12.\n\x06header\x18\x01 \x01(\x0b2\x18.tendermint.types.HeaderB\x04\xc8\xde\x1f\x00\x127\n\x06valset\x18\x02 \x03(\x0b2!.cosmos.staking.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00"\x91\x02\n\x0fCommissionRates\x12<\n\x04rate\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12S\n\x08max_rate\x18\x02 \x01(\tBA\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x0fyaml:"max_rate"\x12a\n\x0fmax_change_rate\x18\x03 \x01(\tBH\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x16yaml:"max_change_rate":\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01"\xb4\x01\n\nCommission\x12K\n\x10commission_rates\x18\x01 \x01(\x0b2\'.cosmos.staking.v1beta1.CommissionRatesB\x08\xc8\xde\x1f\x00\xd0\xde\x1f\x01\x12O\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1e\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"update_time"\x90\xdf\x1f\x01:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01"\x93\x01\n\x0bDescription\x12\x0f\n\x07moniker\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\x12\x0f\n\x07website\x18\x03 \x01(\t\x125\n\x10security_contact\x18\x04 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"security_contact"\x12\x0f\n\x07details\x18\x05 \x01(\t:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01"\xa1\x08\n\tValidator\x125\n\x10operator_address\x18\x01 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"operator_address"\x12c\n\x10consensus_pubkey\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyB3\xf2\xde\x1f\x17yaml:"consensus_pubkey"\xca\xb4-\x14cosmos.crypto.PubKey\x12\x0e\n\x06jailed\x18\x03 \x01(\x08\x122\n\x06status\x18\x04 \x01(\x0e2".cosmos.staking.v1beta1.BondStatus\x12>\n\x06tokens\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12c\n\x10delegator_shares\x18\x06 \x01(\tBI\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x17yaml:"delegator_shares"\x12>\n\x0bdescription\x18\x07 \x01(\x0b2#.cosmos.staking.v1beta1.DescriptionB\x04\xc8\xde\x1f\x00\x125\n\x10unbonding_height\x18\x08 \x01(\x03B\x1b\xf2\xde\x1f\x17yaml:"unbonding_height"\x12U\n\x0eunbonding_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB!\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"unbonding_time"\x90\xdf\x1f\x01\x12<\n\ncommission\x18\n \x01(\x0b2".cosmos.staking.v1beta1.CommissionB\x04\xc8\xde\x1f\x00\x12k\n\x13min_self_delegation\x18\x0b \x01(\tBN\x18\x01\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"min_self_delegation"\x12#\n\x1bunbonding_on_hold_ref_count\x18\x0c \x01(\x03\x12\x15\n\runbonding_ids\x18\r \x03(\x04\x12m\n\x15validator_bond_shares\x18\x0e \x01(\tBN\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x1cyaml:"validator_bond_shares"\x12]\n\rliquid_shares\x18\x0f \x01(\tBF\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x14yaml:"liquid_shares":\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00"+\n\x0cValAddresses\x12\x11\n\taddresses\x18\x01 \x03(\t:\x08\x98\xa0\x1f\x00\x80\xdc \x01"\x88\x01\n\x06DVPair\x127\n\x11delegator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x127\n\x11validator_address\x18\x02 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address":\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00">\n\x07DVPairs\x123\n\x05pairs\x18\x01 \x03(\x0b2\x1e.cosmos.staking.v1beta1.DVPairB\x04\xc8\xde\x1f\x00"\xd5\x01\n\nDVVTriplet\x127\n\x11delegator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x12?\n\x15validator_src_address\x18\x02 \x01(\tB \xf2\xde\x1f\x1cyaml:"validator_src_address"\x12?\n\x15validator_dst_address\x18\x03 \x01(\tB \xf2\xde\x1f\x1cyaml:"validator_dst_address":\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00"I\n\x0bDVVTriplets\x12:\n\x08triplets\x18\x01 \x03(\x0b2".cosmos.staking.v1beta1.DVVTripletB\x04\xc8\xde\x1f\x00"\xe4\x01\n\nDelegation\x127\n\x11delegator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x127\n\x11validator_address\x18\x02 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address"\x12>\n\x06shares\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x16\n\x0evalidator_bond\x18\x04 \x01(\x08:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00"\xde\x01\n\x13UnbondingDelegation\x127\n\x11delegator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x127\n\x11validator_address\x18\x02 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address"\x12G\n\x07entries\x18\x03 \x03(\x0b20.cosmos.staking.v1beta1.UnbondingDelegationEntryB\x04\xc8\xde\x1f\x00:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00"\x91\x03\n\x18UnbondingDelegationEntry\x123\n\x0fcreation_height\x18\x01 \x01(\x03B\x1a\xf2\xde\x1f\x16yaml:"creation_height"\x12W\n\x0fcompletion_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB"\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"completion_time"\x90\xdf\x1f\x01\x12a\n\x0finitial_balance\x18\x03 \x01(\tBH\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"initial_balance"\x12?\n\x07balance\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12\x14\n\x0cunbonding_id\x18\x05 \x01(\x04\x12#\n\x1bunbonding_on_hold_ref_count\x18\x06 \x01(\x03:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01"\x8d\x03\n\x11RedelegationEntry\x123\n\x0fcreation_height\x18\x01 \x01(\x03B\x1a\xf2\xde\x1f\x16yaml:"creation_height"\x12W\n\x0fcompletion_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB"\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"completion_time"\x90\xdf\x1f\x01\x12a\n\x0finitial_balance\x18\x03 \x01(\tBH\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"initial_balance"\x12B\n\nshares_dst\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x14\n\x0cunbonding_id\x18\x05 \x01(\x04\x12#\n\x1bunbonding_on_hold_ref_count\x18\x06 \x01(\x03:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01"\x99\x02\n\x0cRedelegation\x127\n\x11delegator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x12?\n\x15validator_src_address\x18\x02 \x01(\tB \xf2\xde\x1f\x1cyaml:"validator_src_address"\x12?\n\x15validator_dst_address\x18\x03 \x01(\tB \xf2\xde\x1f\x1cyaml:"validator_dst_address"\x12@\n\x07entries\x18\x04 \x03(\x0b2).cosmos.staking.v1beta1.RedelegationEntryB\x04\xc8\xde\x1f\x00:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00"\x97\x05\n\x06Params\x12T\n\x0eunbonding_time\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB!\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"unbonding_time"\x98\xdf\x1f\x01\x121\n\x0emax_validators\x18\x02 \x01(\rB\x19\xf2\xde\x1f\x15yaml:"max_validators"\x12+\n\x0bmax_entries\x18\x03 \x01(\rB\x16\xf2\xde\x1f\x12yaml:"max_entries"\x129\n\x12historical_entries\x18\x04 \x01(\rB\x1d\xf2\xde\x1f\x19yaml:"historical_entries"\x12)\n\nbond_denom\x18\x05 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"bond_denom"\x12m\n\x15validator_bond_factor\x18\x07 \x01(\tBN\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x1cyaml:"validator_bond_factor"\x12u\n\x19global_liquid_staking_cap\x18\x08 \x01(\tBR\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f yaml:"global_liquid_staking_cap"\x12{\n\x1cvalidator_liquid_staking_cap\x18\t \x01(\tBU\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f#yaml:"validator_liquid_staking_cap":\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01J\x04\x08\x06\x10\x07"\x8e\x01\n\x12DelegationResponse\x12<\n\ndelegation\x18\x01 \x01(\x0b2".cosmos.staking.v1beta1.DelegationB\x04\xc8\xde\x1f\x00\x120\n\x07balance\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x00"\xaf\x01\n\x19RedelegationEntryResponse\x12K\n\x12redelegation_entry\x18\x01 \x01(\x0b2).cosmos.staking.v1beta1.RedelegationEntryB\x04\xc8\xde\x1f\x00\x12?\n\x07balance\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int:\x04\xe8\xa0\x1f\x01"\xa8\x01\n\x14RedelegationResponse\x12@\n\x0credelegation\x18\x01 \x01(\x0b2$.cosmos.staking.v1beta1.RedelegationB\x04\xc8\xde\x1f\x00\x12H\n\x07entries\x18\x02 \x03(\x0b21.cosmos.staking.v1beta1.RedelegationEntryResponseB\x04\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x00"\xe0\x01\n\x04Pool\x12^\n\x11not_bonded_tokens\x18\x01 \x01(\tBC\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xea\xde\x1f\x11not_bonded_tokens\x12n\n\rbonded_tokens\x18\x02 \x01(\tBW\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xea\xde\x1f\rbonded_tokens\xf2\xde\x1f\x14yaml:"bonded_tokens":\x08\xe8\xa0\x1f\x01\xf0\xa0\x1f\x01"K\n\x10ValidatorUpdates\x127\n\x07updates\x18\x01 \x03(\x0b2 .tendermint.abci.ValidatorUpdateB\x04\xc8\xde\x1f\x00"a\n\x13TokenizeShareRecord\x12\n\n\x02id\x18\x01 \x01(\x04\x12\r\n\x05owner\x18\x02 \x01(\t\x12\x16\n\x0emodule_account\x18\x03 \x01(\t\x12\x11\n\tvalidator\x18\x04 \x01(\t:\x04\xe8\xa0\x1f\x01"7\n"PendingTokenizeShareAuthorizations\x12\x11\n\taddresses\x18\x01 \x03(\t*\xb6\x01\n\nBondStatus\x12,\n\x17BOND_STATUS_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bUnspecified\x12&\n\x14BOND_STATUS_UNBONDED\x10\x01\x1a\x0c\x8a\x9d \x08Unbonded\x12(\n\x15BOND_STATUS_UNBONDING\x10\x02\x1a\r\x8a\x9d \tUnbonding\x12"\n\x12BOND_STATUS_BONDED\x10\x03\x1a\n\x8a\x9d \x06Bonded\x1a\x04\x88\xa3\x1e\x00*\xa9\x01\n\x0eInfractionType\x124\n\x1bINFRACTION_TYPE_UNSPECIFIED\x10\x00\x1a\x13\x8a\x9d \x0fInfractionEmpty\x12/\n\x1bINFRACTION_TYPE_DOUBLE_SIGN\x10\x01\x1a\x0e\x8a\x9d \nDoubleSign\x12*\n\x18INFRACTION_TYPE_DOWNTIME\x10\x02\x1a\x0c\x8a\x9d \x08Downtime\x1a\x04\x88\xa3\x1e\x00*\xc9\x01\n\x17TokenizeShareLockStatus\x12*\n&TOKENIZE_SHARE_LOCK_STATUS_UNSPECIFIED\x10\x00\x12%\n!TOKENIZE_SHARE_LOCK_STATUS_LOCKED\x10\x01\x12\'\n#TOKENIZE_SHARE_LOCK_STATUS_UNLOCKED\x10\x02\x12,\n(TOKENIZE_SHARE_LOCK_STATUS_LOCK_EXPIRING\x10\x03\x1a\x04\x88\xa3\x1e\x00B.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.staking_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
    _BONDSTATUS._options = None
    _BONDSTATUS._serialized_options = b'\x88\xa3\x1e\x00'
    _BONDSTATUS.values_by_name['BOND_STATUS_UNSPECIFIED']._options = None
    _BONDSTATUS.values_by_name['BOND_STATUS_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x0bUnspecified'
    _BONDSTATUS.values_by_name['BOND_STATUS_UNBONDED']._options = None
    _BONDSTATUS.values_by_name['BOND_STATUS_UNBONDED']._serialized_options = b'\x8a\x9d \x08Unbonded'
    _BONDSTATUS.values_by_name['BOND_STATUS_UNBONDING']._options = None
    _BONDSTATUS.values_by_name['BOND_STATUS_UNBONDING']._serialized_options = b'\x8a\x9d \tUnbonding'
    _BONDSTATUS.values_by_name['BOND_STATUS_BONDED']._options = None
    _BONDSTATUS.values_by_name['BOND_STATUS_BONDED']._serialized_options = b'\x8a\x9d \x06Bonded'
    _INFRACTIONTYPE._options = None
    _INFRACTIONTYPE._serialized_options = b'\x88\xa3\x1e\x00'
    _INFRACTIONTYPE.values_by_name['INFRACTION_TYPE_UNSPECIFIED']._options = None
    _INFRACTIONTYPE.values_by_name['INFRACTION_TYPE_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x0fInfractionEmpty'
    _INFRACTIONTYPE.values_by_name['INFRACTION_TYPE_DOUBLE_SIGN']._options = None
    _INFRACTIONTYPE.values_by_name['INFRACTION_TYPE_DOUBLE_SIGN']._serialized_options = b'\x8a\x9d \nDoubleSign'
    _INFRACTIONTYPE.values_by_name['INFRACTION_TYPE_DOWNTIME']._options = None
    _INFRACTIONTYPE.values_by_name['INFRACTION_TYPE_DOWNTIME']._serialized_options = b'\x8a\x9d \x08Downtime'
    _TOKENIZESHARELOCKSTATUS._options = None
    _TOKENIZESHARELOCKSTATUS._serialized_options = b'\x88\xa3\x1e\x00'
    _HISTORICALINFO.fields_by_name['header']._options = None
    _HISTORICALINFO.fields_by_name['header']._serialized_options = b'\xc8\xde\x1f\x00'
    _HISTORICALINFO.fields_by_name['valset']._options = None
    _HISTORICALINFO.fields_by_name['valset']._serialized_options = b'\xc8\xde\x1f\x00'
    _COMMISSIONRATES.fields_by_name['rate']._options = None
    _COMMISSIONRATES.fields_by_name['rate']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _COMMISSIONRATES.fields_by_name['max_rate']._options = None
    _COMMISSIONRATES.fields_by_name['max_rate']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x0fyaml:"max_rate"'
    _COMMISSIONRATES.fields_by_name['max_change_rate']._options = None
    _COMMISSIONRATES.fields_by_name['max_change_rate']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x16yaml:"max_change_rate"'
    _COMMISSIONRATES._options = None
    _COMMISSIONRATES._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _COMMISSION.fields_by_name['commission_rates']._options = None
    _COMMISSION.fields_by_name['commission_rates']._serialized_options = b'\xc8\xde\x1f\x00\xd0\xde\x1f\x01'
    _COMMISSION.fields_by_name['update_time']._options = None
    _COMMISSION.fields_by_name['update_time']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"update_time"\x90\xdf\x1f\x01'
    _COMMISSION._options = None
    _COMMISSION._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _DESCRIPTION.fields_by_name['security_contact']._options = None
    _DESCRIPTION.fields_by_name['security_contact']._serialized_options = b'\xf2\xde\x1f\x17yaml:"security_contact"'
    _DESCRIPTION._options = None
    _DESCRIPTION._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _VALIDATOR.fields_by_name['operator_address']._options = None
    _VALIDATOR.fields_by_name['operator_address']._serialized_options = b'\xf2\xde\x1f\x17yaml:"operator_address"'
    _VALIDATOR.fields_by_name['consensus_pubkey']._options = None
    _VALIDATOR.fields_by_name['consensus_pubkey']._serialized_options = b'\xf2\xde\x1f\x17yaml:"consensus_pubkey"\xca\xb4-\x14cosmos.crypto.PubKey'
    _VALIDATOR.fields_by_name['tokens']._options = None
    _VALIDATOR.fields_by_name['tokens']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _VALIDATOR.fields_by_name['delegator_shares']._options = None
    _VALIDATOR.fields_by_name['delegator_shares']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x17yaml:"delegator_shares"'
    _VALIDATOR.fields_by_name['description']._options = None
    _VALIDATOR.fields_by_name['description']._serialized_options = b'\xc8\xde\x1f\x00'
    _VALIDATOR.fields_by_name['unbonding_height']._options = None
    _VALIDATOR.fields_by_name['unbonding_height']._serialized_options = b'\xf2\xde\x1f\x17yaml:"unbonding_height"'
    _VALIDATOR.fields_by_name['unbonding_time']._options = None
    _VALIDATOR.fields_by_name['unbonding_time']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"unbonding_time"\x90\xdf\x1f\x01'
    _VALIDATOR.fields_by_name['commission']._options = None
    _VALIDATOR.fields_by_name['commission']._serialized_options = b'\xc8\xde\x1f\x00'
    _VALIDATOR.fields_by_name['min_self_delegation']._options = None
    _VALIDATOR.fields_by_name['min_self_delegation']._serialized_options = b'\x18\x01\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x1ayaml:"min_self_delegation"'
    _VALIDATOR.fields_by_name['validator_bond_shares']._options = None
    _VALIDATOR.fields_by_name['validator_bond_shares']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x1cyaml:"validator_bond_shares"'
    _VALIDATOR.fields_by_name['liquid_shares']._options = None
    _VALIDATOR.fields_by_name['liquid_shares']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x14yaml:"liquid_shares"'
    _VALIDATOR._options = None
    _VALIDATOR._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _VALADDRESSES._options = None
    _VALADDRESSES._serialized_options = b'\x98\xa0\x1f\x00\x80\xdc \x01'
    _DVPAIR.fields_by_name['delegator_address']._options = None
    _DVPAIR.fields_by_name['delegator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"delegator_address"'
    _DVPAIR.fields_by_name['validator_address']._options = None
    _DVPAIR.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _DVPAIR._options = None
    _DVPAIR._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _DVPAIRS.fields_by_name['pairs']._options = None
    _DVPAIRS.fields_by_name['pairs']._serialized_options = b'\xc8\xde\x1f\x00'
    _DVVTRIPLET.fields_by_name['delegator_address']._options = None
    _DVVTRIPLET.fields_by_name['delegator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"delegator_address"'
    _DVVTRIPLET.fields_by_name['validator_src_address']._options = None
    _DVVTRIPLET.fields_by_name['validator_src_address']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"validator_src_address"'
    _DVVTRIPLET.fields_by_name['validator_dst_address']._options = None
    _DVVTRIPLET.fields_by_name['validator_dst_address']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"validator_dst_address"'
    _DVVTRIPLET._options = None
    _DVVTRIPLET._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _DVVTRIPLETS.fields_by_name['triplets']._options = None
    _DVVTRIPLETS.fields_by_name['triplets']._serialized_options = b'\xc8\xde\x1f\x00'
    _DELEGATION.fields_by_name['delegator_address']._options = None
    _DELEGATION.fields_by_name['delegator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"delegator_address"'
    _DELEGATION.fields_by_name['validator_address']._options = None
    _DELEGATION.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _DELEGATION.fields_by_name['shares']._options = None
    _DELEGATION.fields_by_name['shares']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _DELEGATION._options = None
    _DELEGATION._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _UNBONDINGDELEGATION.fields_by_name['delegator_address']._options = None
    _UNBONDINGDELEGATION.fields_by_name['delegator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"delegator_address"'
    _UNBONDINGDELEGATION.fields_by_name['validator_address']._options = None
    _UNBONDINGDELEGATION.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _UNBONDINGDELEGATION.fields_by_name['entries']._options = None
    _UNBONDINGDELEGATION.fields_by_name['entries']._serialized_options = b'\xc8\xde\x1f\x00'
    _UNBONDINGDELEGATION._options = None
    _UNBONDINGDELEGATION._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _UNBONDINGDELEGATIONENTRY.fields_by_name['creation_height']._options = None
    _UNBONDINGDELEGATIONENTRY.fields_by_name['creation_height']._serialized_options = b'\xf2\xde\x1f\x16yaml:"creation_height"'
    _UNBONDINGDELEGATIONENTRY.fields_by_name['completion_time']._options = None
    _UNBONDINGDELEGATIONENTRY.fields_by_name['completion_time']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"completion_time"\x90\xdf\x1f\x01'
    _UNBONDINGDELEGATIONENTRY.fields_by_name['initial_balance']._options = None
    _UNBONDINGDELEGATIONENTRY.fields_by_name['initial_balance']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"initial_balance"'
    _UNBONDINGDELEGATIONENTRY.fields_by_name['balance']._options = None
    _UNBONDINGDELEGATIONENTRY.fields_by_name['balance']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _UNBONDINGDELEGATIONENTRY._options = None
    _UNBONDINGDELEGATIONENTRY._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _REDELEGATIONENTRY.fields_by_name['creation_height']._options = None
    _REDELEGATIONENTRY.fields_by_name['creation_height']._serialized_options = b'\xf2\xde\x1f\x16yaml:"creation_height"'
    _REDELEGATIONENTRY.fields_by_name['completion_time']._options = None
    _REDELEGATIONENTRY.fields_by_name['completion_time']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"completion_time"\x90\xdf\x1f\x01'
    _REDELEGATIONENTRY.fields_by_name['initial_balance']._options = None
    _REDELEGATIONENTRY.fields_by_name['initial_balance']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x16yaml:"initial_balance"'
    _REDELEGATIONENTRY.fields_by_name['shares_dst']._options = None
    _REDELEGATIONENTRY.fields_by_name['shares_dst']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _REDELEGATIONENTRY._options = None
    _REDELEGATIONENTRY._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _REDELEGATION.fields_by_name['delegator_address']._options = None
    _REDELEGATION.fields_by_name['delegator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"delegator_address"'
    _REDELEGATION.fields_by_name['validator_src_address']._options = None
    _REDELEGATION.fields_by_name['validator_src_address']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"validator_src_address"'
    _REDELEGATION.fields_by_name['validator_dst_address']._options = None
    _REDELEGATION.fields_by_name['validator_dst_address']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"validator_dst_address"'
    _REDELEGATION.fields_by_name['entries']._options = None
    _REDELEGATION.fields_by_name['entries']._serialized_options = b'\xc8\xde\x1f\x00'
    _REDELEGATION._options = None
    _REDELEGATION._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _PARAMS.fields_by_name['unbonding_time']._options = None
    _PARAMS.fields_by_name['unbonding_time']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"unbonding_time"\x98\xdf\x1f\x01'
    _PARAMS.fields_by_name['max_validators']._options = None
    _PARAMS.fields_by_name['max_validators']._serialized_options = b'\xf2\xde\x1f\x15yaml:"max_validators"'
    _PARAMS.fields_by_name['max_entries']._options = None
    _PARAMS.fields_by_name['max_entries']._serialized_options = b'\xf2\xde\x1f\x12yaml:"max_entries"'
    _PARAMS.fields_by_name['historical_entries']._options = None
    _PARAMS.fields_by_name['historical_entries']._serialized_options = b'\xf2\xde\x1f\x19yaml:"historical_entries"'
    _PARAMS.fields_by_name['bond_denom']._options = None
    _PARAMS.fields_by_name['bond_denom']._serialized_options = b'\xf2\xde\x1f\x11yaml:"bond_denom"'
    _PARAMS.fields_by_name['validator_bond_factor']._options = None
    _PARAMS.fields_by_name['validator_bond_factor']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x1cyaml:"validator_bond_factor"'
    _PARAMS.fields_by_name['global_liquid_staking_cap']._options = None
    _PARAMS.fields_by_name['global_liquid_staking_cap']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f yaml:"global_liquid_staking_cap"'
    _PARAMS.fields_by_name['validator_liquid_staking_cap']._options = None
    _PARAMS.fields_by_name['validator_liquid_staking_cap']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f#yaml:"validator_liquid_staking_cap"'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _DELEGATIONRESPONSE.fields_by_name['delegation']._options = None
    _DELEGATIONRESPONSE.fields_by_name['delegation']._serialized_options = b'\xc8\xde\x1f\x00'
    _DELEGATIONRESPONSE.fields_by_name['balance']._options = None
    _DELEGATIONRESPONSE.fields_by_name['balance']._serialized_options = b'\xc8\xde\x1f\x00'
    _DELEGATIONRESPONSE._options = None
    _DELEGATIONRESPONSE._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _REDELEGATIONENTRYRESPONSE.fields_by_name['redelegation_entry']._options = None
    _REDELEGATIONENTRYRESPONSE.fields_by_name['redelegation_entry']._serialized_options = b'\xc8\xde\x1f\x00'
    _REDELEGATIONENTRYRESPONSE.fields_by_name['balance']._options = None
    _REDELEGATIONENTRYRESPONSE.fields_by_name['balance']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _REDELEGATIONENTRYRESPONSE._options = None
    _REDELEGATIONENTRYRESPONSE._serialized_options = b'\xe8\xa0\x1f\x01'
    _REDELEGATIONRESPONSE.fields_by_name['redelegation']._options = None
    _REDELEGATIONRESPONSE.fields_by_name['redelegation']._serialized_options = b'\xc8\xde\x1f\x00'
    _REDELEGATIONRESPONSE.fields_by_name['entries']._options = None
    _REDELEGATIONRESPONSE.fields_by_name['entries']._serialized_options = b'\xc8\xde\x1f\x00'
    _REDELEGATIONRESPONSE._options = None
    _REDELEGATIONRESPONSE._serialized_options = b'\xe8\xa0\x1f\x00'
    _POOL.fields_by_name['not_bonded_tokens']._options = None
    _POOL.fields_by_name['not_bonded_tokens']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xea\xde\x1f\x11not_bonded_tokens'
    _POOL.fields_by_name['bonded_tokens']._options = None
    _POOL.fields_by_name['bonded_tokens']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xea\xde\x1f\rbonded_tokens\xf2\xde\x1f\x14yaml:"bonded_tokens"'
    _POOL._options = None
    _POOL._serialized_options = b'\xe8\xa0\x1f\x01\xf0\xa0\x1f\x01'
    _VALIDATORUPDATES.fields_by_name['updates']._options = None
    _VALIDATORUPDATES.fields_by_name['updates']._serialized_options = b'\xc8\xde\x1f\x00'
    _TOKENIZESHARERECORD._options = None
    _TOKENIZESHARERECORD._serialized_options = b'\xe8\xa0\x1f\x01'
    _globals['_BONDSTATUS']._serialized_start = 5792
    _globals['_BONDSTATUS']._serialized_end = 5974
    _globals['_INFRACTIONTYPE']._serialized_start = 5977
    _globals['_INFRACTIONTYPE']._serialized_end = 6146
    _globals['_TOKENIZESHARELOCKSTATUS']._serialized_start = 6149
    _globals['_TOKENIZESHARELOCKSTATUS']._serialized_end = 6350
    _globals['_HISTORICALINFO']._serialized_start = 296
    _globals['_HISTORICALINFO']._serialized_end = 417
    _globals['_COMMISSIONRATES']._serialized_start = 420
    _globals['_COMMISSIONRATES']._serialized_end = 693
    _globals['_COMMISSION']._serialized_start = 696
    _globals['_COMMISSION']._serialized_end = 876
    _globals['_DESCRIPTION']._serialized_start = 879
    _globals['_DESCRIPTION']._serialized_end = 1026
    _globals['_VALIDATOR']._serialized_start = 1029
    _globals['_VALIDATOR']._serialized_end = 2086
    _globals['_VALADDRESSES']._serialized_start = 2088
    _globals['_VALADDRESSES']._serialized_end = 2131
    _globals['_DVPAIR']._serialized_start = 2134
    _globals['_DVPAIR']._serialized_end = 2270
    _globals['_DVPAIRS']._serialized_start = 2272
    _globals['_DVPAIRS']._serialized_end = 2334
    _globals['_DVVTRIPLET']._serialized_start = 2337
    _globals['_DVVTRIPLET']._serialized_end = 2550
    _globals['_DVVTRIPLETS']._serialized_start = 2552
    _globals['_DVVTRIPLETS']._serialized_end = 2625
    _globals['_DELEGATION']._serialized_start = 2628
    _globals['_DELEGATION']._serialized_end = 2856
    _globals['_UNBONDINGDELEGATION']._serialized_start = 2859
    _globals['_UNBONDINGDELEGATION']._serialized_end = 3081
    _globals['_UNBONDINGDELEGATIONENTRY']._serialized_start = 3084
    _globals['_UNBONDINGDELEGATIONENTRY']._serialized_end = 3485
    _globals['_REDELEGATIONENTRY']._serialized_start = 3488
    _globals['_REDELEGATIONENTRY']._serialized_end = 3885
    _globals['_REDELEGATION']._serialized_start = 3888
    _globals['_REDELEGATION']._serialized_end = 4169
    _globals['_PARAMS']._serialized_start = 4172
    _globals['_PARAMS']._serialized_end = 4835
    _globals['_DELEGATIONRESPONSE']._serialized_start = 4838
    _globals['_DELEGATIONRESPONSE']._serialized_end = 4980
    _globals['_REDELEGATIONENTRYRESPONSE']._serialized_start = 4983
    _globals['_REDELEGATIONENTRYRESPONSE']._serialized_end = 5158
    _globals['_REDELEGATIONRESPONSE']._serialized_start = 5161
    _globals['_REDELEGATIONRESPONSE']._serialized_end = 5329
    _globals['_POOL']._serialized_start = 5332
    _globals['_POOL']._serialized_end = 5556
    _globals['_VALIDATORUPDATES']._serialized_start = 5558
    _globals['_VALIDATORUPDATES']._serialized_end = 5633
    _globals['_TOKENIZESHARERECORD']._serialized_start = 5635
    _globals['_TOKENIZESHARERECORD']._serialized_end = 5732
    _globals['_PENDINGTOKENIZESHAREAUTHORIZATIONS']._serialized_start = 5734
    _globals['_PENDINGTOKENIZESHAREAUTHORIZATIONS']._serialized_end = 5789