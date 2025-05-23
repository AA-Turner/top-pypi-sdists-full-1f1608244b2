"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from ...tendermint.libs.bits import types_pb2 as tendermint_dot_libs_dot_bits_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n tendermint/consensus/types.proto\x12\x14tendermint.consensus\x1a\x14gogoproto/gogo.proto\x1a\x1ctendermint/types/types.proto\x1a tendermint/libs/bits/types.proto"x\n\x0cNewRoundStep\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12\x0c\n\x04step\x18\x03 \x01(\r\x12 \n\x18seconds_since_start_time\x18\x04 \x01(\x03\x12\x19\n\x11last_commit_round\x18\x05 \x01(\x05"\xbc\x01\n\rNewValidBlock\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12D\n\x15block_part_set_header\x18\x03 \x01(\x0b2\x1f.tendermint.types.PartSetHeaderB\x04\xc8\xde\x1f\x00\x123\n\x0bblock_parts\x18\x04 \x01(\x0b2\x1e.tendermint.libs.bits.BitArray\x12\x11\n\tis_commit\x18\x05 \x01(\x08">\n\x08Proposal\x122\n\x08proposal\x18\x01 \x01(\x0b2\x1a.tendermint.types.ProposalB\x04\xc8\xde\x1f\x00"u\n\x0bProposalPOL\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\x1a\n\x12proposal_pol_round\x18\x02 \x01(\x05\x12:\n\x0cproposal_pol\x18\x03 \x01(\x0b2\x1e.tendermint.libs.bits.BitArrayB\x04\xc8\xde\x1f\x00"V\n\tBlockPart\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12*\n\x04part\x18\x03 \x01(\x0b2\x16.tendermint.types.PartB\x04\xc8\xde\x1f\x00",\n\x04Vote\x12$\n\x04vote\x18\x01 \x01(\x0b2\x16.tendermint.types.Vote"f\n\x07HasVote\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12-\n\x04type\x18\x03 \x01(\x0e2\x1f.tendermint.types.SignedMsgType\x12\r\n\x05index\x18\x04 \x01(\x05"\x9a\x01\n\x0cVoteSetMaj23\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12-\n\x04type\x18\x03 \x01(\x0e2\x1f.tendermint.types.SignedMsgType\x12<\n\x08block_id\x18\x04 \x01(\x0b2\x19.tendermint.types.BlockIDB\x0f\xc8\xde\x1f\x00\xe2\xde\x1f\x07BlockID"\xce\x01\n\x0bVoteSetBits\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12-\n\x04type\x18\x03 \x01(\x0e2\x1f.tendermint.types.SignedMsgType\x12<\n\x08block_id\x18\x04 \x01(\x0b2\x19.tendermint.types.BlockIDB\x0f\xc8\xde\x1f\x00\xe2\xde\x1f\x07BlockID\x123\n\x05votes\x18\x05 \x01(\x0b2\x1e.tendermint.libs.bits.BitArrayB\x04\xc8\xde\x1f\x00"\x8d\x04\n\x07Message\x12<\n\x0enew_round_step\x18\x01 \x01(\x0b2".tendermint.consensus.NewRoundStepH\x00\x12>\n\x0fnew_valid_block\x18\x02 \x01(\x0b2#.tendermint.consensus.NewValidBlockH\x00\x122\n\x08proposal\x18\x03 \x01(\x0b2\x1e.tendermint.consensus.ProposalH\x00\x129\n\x0cproposal_pol\x18\x04 \x01(\x0b2!.tendermint.consensus.ProposalPOLH\x00\x125\n\nblock_part\x18\x05 \x01(\x0b2\x1f.tendermint.consensus.BlockPartH\x00\x12*\n\x04vote\x18\x06 \x01(\x0b2\x1a.tendermint.consensus.VoteH\x00\x121\n\x08has_vote\x18\x07 \x01(\x0b2\x1d.tendermint.consensus.HasVoteH\x00\x12<\n\x0evote_set_maj23\x18\x08 \x01(\x0b2".tendermint.consensus.VoteSetMaj23H\x00\x12:\n\rvote_set_bits\x18\t \x01(\x0b2!.tendermint.consensus.VoteSetBitsH\x00B\x05\n\x03sumB=Z;github.com/tendermint/tendermint/proto/tendermint/consensusb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.consensus.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z;github.com/tendermint/tendermint/proto/tendermint/consensus'
    _NEWVALIDBLOCK.fields_by_name['block_part_set_header']._options = None
    _NEWVALIDBLOCK.fields_by_name['block_part_set_header']._serialized_options = b'\xc8\xde\x1f\x00'
    _PROPOSAL.fields_by_name['proposal']._options = None
    _PROPOSAL.fields_by_name['proposal']._serialized_options = b'\xc8\xde\x1f\x00'
    _PROPOSALPOL.fields_by_name['proposal_pol']._options = None
    _PROPOSALPOL.fields_by_name['proposal_pol']._serialized_options = b'\xc8\xde\x1f\x00'
    _BLOCKPART.fields_by_name['part']._options = None
    _BLOCKPART.fields_by_name['part']._serialized_options = b'\xc8\xde\x1f\x00'
    _VOTESETMAJ23.fields_by_name['block_id']._options = None
    _VOTESETMAJ23.fields_by_name['block_id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x07BlockID'
    _VOTESETBITS.fields_by_name['block_id']._options = None
    _VOTESETBITS.fields_by_name['block_id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x07BlockID'
    _VOTESETBITS.fields_by_name['votes']._options = None
    _VOTESETBITS.fields_by_name['votes']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_NEWROUNDSTEP']._serialized_start = 144
    _globals['_NEWROUNDSTEP']._serialized_end = 264
    _globals['_NEWVALIDBLOCK']._serialized_start = 267
    _globals['_NEWVALIDBLOCK']._serialized_end = 455
    _globals['_PROPOSAL']._serialized_start = 457
    _globals['_PROPOSAL']._serialized_end = 519
    _globals['_PROPOSALPOL']._serialized_start = 521
    _globals['_PROPOSALPOL']._serialized_end = 638
    _globals['_BLOCKPART']._serialized_start = 640
    _globals['_BLOCKPART']._serialized_end = 726
    _globals['_VOTE']._serialized_start = 728
    _globals['_VOTE']._serialized_end = 772
    _globals['_HASVOTE']._serialized_start = 774
    _globals['_HASVOTE']._serialized_end = 876
    _globals['_VOTESETMAJ23']._serialized_start = 879
    _globals['_VOTESETMAJ23']._serialized_end = 1033
    _globals['_VOTESETBITS']._serialized_start = 1036
    _globals['_VOTESETBITS']._serialized_end = 1242
    _globals['_MESSAGE']._serialized_start = 1245
    _globals['_MESSAGE']._serialized_end = 1770