"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.distribution.v1beta1 import distribution_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)cosmos/distribution/v1beta1/genesis.proto\x12\x1bcosmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a.cosmos/distribution/v1beta1/distribution.proto"\x91\x01\n\x15DelegatorWithdrawInfo\x127\n\x11delegator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x125\n\x10withdraw_address\x18\x02 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"withdraw_address":\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xf5\x01\n!ValidatorOutstandingRewardsRecord\x127\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address"\x12\x8c\x01\n\x13outstanding_rewards\x18\x02 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinBQ\xc8\xde\x1f\x00\xf2\xde\x1f\x1ayaml:"outstanding_rewards"\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xd7\x01\n$ValidatorAccumulatedCommissionRecord\x127\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address"\x12l\n\x0baccumulated\x18\x02 \x01(\x0b2;.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionB\x1a\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"accumulated":\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xd7\x01\n ValidatorHistoricalRewardsRecord\x127\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address"\x12\x0e\n\x06period\x18\x02 \x01(\x04\x12`\n\x07rewards\x18\x03 \x01(\x0b27.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsB\x16\xc8\xde\x1f\x00\xf2\xde\x1f\x0eyaml:"rewards":\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xc1\x01\n\x1dValidatorCurrentRewardsRecord\x127\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address"\x12]\n\x07rewards\x18\x02 \x01(\x0b24.cosmos.distribution.v1beta1.ValidatorCurrentRewardsB\x16\xc8\xde\x1f\x00\xf2\xde\x1f\x0eyaml:"rewards":\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x82\x02\n\x1bDelegatorStartingInfoRecord\x127\n\x11delegator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"delegator_address"\x127\n\x11validator_address\x18\x02 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address"\x12g\n\rstarting_info\x18\x03 \x01(\x0b22.cosmos.distribution.v1beta1.DelegatorStartingInfoB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"starting_info":\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xe5\x01\n\x19ValidatorSlashEventRecord\x127\n\x11validator_address\x18\x01 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"validator_address"\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12\x0e\n\x06period\x18\x03 \x01(\x04\x12e\n\x15validator_slash_event\x18\x04 \x01(\x0b20.cosmos.distribution.v1beta1.ValidatorSlashEventB\x14\xc8\xde\x1f\x00\xf2\xde\x1f\x0cyaml:"event":\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xb1\t\n\x0cGenesisState\x12J\n\x06params\x18\x01 \x01(\x0b2#.cosmos.distribution.v1beta1.ParamsB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"params"\x12O\n\x08fee_pool\x18\x02 \x01(\x0b2$.cosmos.distribution.v1beta1.FeePoolB\x17\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"fee_pool"\x12}\n\x18delegator_withdraw_infos\x18\x03 \x03(\x0b22.cosmos.distribution.v1beta1.DelegatorWithdrawInfoB\'\xc8\xde\x1f\x00\xf2\xde\x1f\x1fyaml:"delegator_withdraw_infos"\x127\n\x11previous_proposer\x18\x04 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"previous_proposer"\x12\x7f\n\x13outstanding_rewards\x18\x05 \x03(\x0b2>.cosmos.distribution.v1beta1.ValidatorOutstandingRewardsRecordB"\xc8\xde\x1f\x00\xf2\xde\x1f\x1ayaml:"outstanding_rewards"\x12\x9e\x01\n!validator_accumulated_commissions\x18\x06 \x03(\x0b2A.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionRecordB0\xc8\xde\x1f\x00\xf2\xde\x1f(yaml:"validator_accumulated_commissions"\x12\x90\x01\n\x1cvalidator_historical_rewards\x18\x07 \x03(\x0b2=.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsRecordB+\xc8\xde\x1f\x00\xf2\xde\x1f#yaml:"validator_historical_rewards"\x12\x87\x01\n\x19validator_current_rewards\x18\x08 \x03(\x0b2:.cosmos.distribution.v1beta1.ValidatorCurrentRewardsRecordB(\xc8\xde\x1f\x00\xf2\xde\x1f yaml:"validator_current_rewards"\x12\x83\x01\n\x18delegator_starting_infos\x18\t \x03(\x0b28.cosmos.distribution.v1beta1.DelegatorStartingInfoRecordB\'\xc8\xde\x1f\x00\xf2\xde\x1f\x1fyaml:"delegator_starting_infos"\x12}\n\x16validator_slash_events\x18\n \x03(\x0b26.cosmos.distribution.v1beta1.ValidatorSlashEventRecordB%\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:"validator_slash_events":\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00B7Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.distribution.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01'
    _DELEGATORWITHDRAWINFO.fields_by_name['delegator_address']._options = None
    _DELEGATORWITHDRAWINFO.fields_by_name['delegator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"delegator_address"'
    _DELEGATORWITHDRAWINFO.fields_by_name['withdraw_address']._options = None
    _DELEGATORWITHDRAWINFO.fields_by_name['withdraw_address']._serialized_options = b'\xf2\xde\x1f\x17yaml:"withdraw_address"'
    _DELEGATORWITHDRAWINFO._options = None
    _DELEGATORWITHDRAWINFO._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['validator_address']._options = None
    _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['outstanding_rewards']._options = None
    _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['outstanding_rewards']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1ayaml:"outstanding_rewards"\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _VALIDATOROUTSTANDINGREWARDSRECORD._options = None
    _VALIDATOROUTSTANDINGREWARDSRECORD._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['validator_address']._options = None
    _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['accumulated']._options = None
    _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['accumulated']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"accumulated"'
    _VALIDATORACCUMULATEDCOMMISSIONRECORD._options = None
    _VALIDATORACCUMULATEDCOMMISSIONRECORD._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['validator_address']._options = None
    _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['rewards']._options = None
    _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0eyaml:"rewards"'
    _VALIDATORHISTORICALREWARDSRECORD._options = None
    _VALIDATORHISTORICALREWARDSRECORD._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _VALIDATORCURRENTREWARDSRECORD.fields_by_name['validator_address']._options = None
    _VALIDATORCURRENTREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _VALIDATORCURRENTREWARDSRECORD.fields_by_name['rewards']._options = None
    _VALIDATORCURRENTREWARDSRECORD.fields_by_name['rewards']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0eyaml:"rewards"'
    _VALIDATORCURRENTREWARDSRECORD._options = None
    _VALIDATORCURRENTREWARDSRECORD._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _DELEGATORSTARTINGINFORECORD.fields_by_name['delegator_address']._options = None
    _DELEGATORSTARTINGINFORECORD.fields_by_name['delegator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"delegator_address"'
    _DELEGATORSTARTINGINFORECORD.fields_by_name['validator_address']._options = None
    _DELEGATORSTARTINGINFORECORD.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _DELEGATORSTARTINGINFORECORD.fields_by_name['starting_info']._options = None
    _DELEGATORSTARTINGINFORECORD.fields_by_name['starting_info']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"starting_info"'
    _DELEGATORSTARTINGINFORECORD._options = None
    _DELEGATORSTARTINGINFORECORD._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_address']._options = None
    _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_address']._serialized_options = b'\xf2\xde\x1f\x18yaml:"validator_address"'
    _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_slash_event']._options = None
    _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_slash_event']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0cyaml:"event"'
    _VALIDATORSLASHEVENTRECORD._options = None
    _VALIDATORSLASHEVENTRECORD._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"params"'
    _GENESISSTATE.fields_by_name['fee_pool']._options = None
    _GENESISSTATE.fields_by_name['fee_pool']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"fee_pool"'
    _GENESISSTATE.fields_by_name['delegator_withdraw_infos']._options = None
    _GENESISSTATE.fields_by_name['delegator_withdraw_infos']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1fyaml:"delegator_withdraw_infos"'
    _GENESISSTATE.fields_by_name['previous_proposer']._options = None
    _GENESISSTATE.fields_by_name['previous_proposer']._serialized_options = b'\xf2\xde\x1f\x18yaml:"previous_proposer"'
    _GENESISSTATE.fields_by_name['outstanding_rewards']._options = None
    _GENESISSTATE.fields_by_name['outstanding_rewards']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1ayaml:"outstanding_rewards"'
    _GENESISSTATE.fields_by_name['validator_accumulated_commissions']._options = None
    _GENESISSTATE.fields_by_name['validator_accumulated_commissions']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f(yaml:"validator_accumulated_commissions"'
    _GENESISSTATE.fields_by_name['validator_historical_rewards']._options = None
    _GENESISSTATE.fields_by_name['validator_historical_rewards']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f#yaml:"validator_historical_rewards"'
    _GENESISSTATE.fields_by_name['validator_current_rewards']._options = None
    _GENESISSTATE.fields_by_name['validator_current_rewards']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f yaml:"validator_current_rewards"'
    _GENESISSTATE.fields_by_name['delegator_starting_infos']._options = None
    _GENESISSTATE.fields_by_name['delegator_starting_infos']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1fyaml:"delegator_starting_infos"'
    _GENESISSTATE.fields_by_name['validator_slash_events']._options = None
    _GENESISSTATE.fields_by_name['validator_slash_events']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:"validator_slash_events"'
    _GENESISSTATE._options = None
    _GENESISSTATE._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_DELEGATORWITHDRAWINFO']._serialized_start = 177
    _globals['_DELEGATORWITHDRAWINFO']._serialized_end = 322
    _globals['_VALIDATOROUTSTANDINGREWARDSRECORD']._serialized_start = 325
    _globals['_VALIDATOROUTSTANDINGREWARDSRECORD']._serialized_end = 570
    _globals['_VALIDATORACCUMULATEDCOMMISSIONRECORD']._serialized_start = 573
    _globals['_VALIDATORACCUMULATEDCOMMISSIONRECORD']._serialized_end = 788
    _globals['_VALIDATORHISTORICALREWARDSRECORD']._serialized_start = 791
    _globals['_VALIDATORHISTORICALREWARDSRECORD']._serialized_end = 1006
    _globals['_VALIDATORCURRENTREWARDSRECORD']._serialized_start = 1009
    _globals['_VALIDATORCURRENTREWARDSRECORD']._serialized_end = 1202
    _globals['_DELEGATORSTARTINGINFORECORD']._serialized_start = 1205
    _globals['_DELEGATORSTARTINGINFORECORD']._serialized_end = 1463
    _globals['_VALIDATORSLASHEVENTRECORD']._serialized_start = 1466
    _globals['_VALIDATORSLASHEVENTRECORD']._serialized_end = 1695
    _globals['_GENESISSTATE']._serialized_start = 1698
    _globals['_GENESISSTATE']._serialized_end = 2899