"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!ibc/core/channel/v1/channel.proto\x12\x13ibc.core.channel.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fibc/core/client/v1/client.proto"\xed\x01\n\x07Channel\x12)\n\x05state\x18\x01 \x01(\x0e2\x1a.ibc.core.channel.v1.State\x12,\n\x08ordering\x18\x02 \x01(\x0e2\x1a.ibc.core.channel.v1.Order\x12=\n\x0ccounterparty\x18\x03 \x01(\x0b2!.ibc.core.channel.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x123\n\x0fconnection_hops\x18\x04 \x03(\tB\x1a\xf2\xde\x1f\x16yaml:"connection_hops"\x12\x0f\n\x07version\x18\x05 \x01(\t:\x04\x88\xa0\x1f\x00"\x9c\x02\n\x11IdentifiedChannel\x12)\n\x05state\x18\x01 \x01(\x0e2\x1a.ibc.core.channel.v1.State\x12,\n\x08ordering\x18\x02 \x01(\x0e2\x1a.ibc.core.channel.v1.Order\x12=\n\x0ccounterparty\x18\x03 \x01(\x0b2!.ibc.core.channel.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x123\n\x0fconnection_hops\x18\x04 \x03(\tB\x1a\xf2\xde\x1f\x16yaml:"connection_hops"\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x0f\n\x07port_id\x18\x06 \x01(\t\x12\x12\n\nchannel_id\x18\x07 \x01(\t:\x04\x88\xa0\x1f\x00"d\n\x0cCounterparty\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"port_id"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id":\x04\x88\xa0\x1f\x00"\x8e\x03\n\x06Packet\x12\x10\n\x08sequence\x18\x01 \x01(\x04\x12+\n\x0bsource_port\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:"source_port"\x121\n\x0esource_channel\x18\x03 \x01(\tB\x19\xf2\xde\x1f\x15yaml:"source_channel"\x125\n\x10destination_port\x18\x04 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"destination_port"\x12;\n\x13destination_channel\x18\x05 \x01(\tB\x1e\xf2\xde\x1f\x1ayaml:"destination_channel"\x12\x0c\n\x04data\x18\x06 \x01(\x0c\x12Q\n\x0etimeout_height\x18\x07 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"timeout_height"\x127\n\x11timeout_timestamp\x18\x08 \x01(\x04B\x1c\xf2\xde\x1f\x18yaml:"timeout_timestamp":\x04\x88\xa0\x1f\x00"\x83\x01\n\x0bPacketState\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"port_id"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id"\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x12\x0c\n\x04data\x18\x04 \x01(\x0c:\x04\x88\xa0\x1f\x00"r\n\x08PacketId\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"port_id"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id"\x12\x10\n\x08sequence\x18\x03 \x01(\x04:\x04\x88\xa0\x1f\x00"@\n\x0fAcknowledgement\x12\x10\n\x06result\x18\x15 \x01(\x0cH\x00\x12\x0f\n\x05error\x18\x16 \x01(\tH\x00B\n\n\x08response*\xb7\x01\n\x05State\x126\n\x1fSTATE_UNINITIALIZED_UNSPECIFIED\x10\x00\x1a\x11\x8a\x9d \rUNINITIALIZED\x12\x18\n\nSTATE_INIT\x10\x01\x1a\x08\x8a\x9d \x04INIT\x12\x1e\n\rSTATE_TRYOPEN\x10\x02\x1a\x0b\x8a\x9d \x07TRYOPEN\x12\x18\n\nSTATE_OPEN\x10\x03\x1a\x08\x8a\x9d \x04OPEN\x12\x1c\n\x0cSTATE_CLOSED\x10\x04\x1a\n\x8a\x9d \x06CLOSED\x1a\x04\x88\xa3\x1e\x00*w\n\x05Order\x12$\n\x16ORDER_NONE_UNSPECIFIED\x10\x00\x1a\x08\x8a\x9d \x04NONE\x12"\n\x0fORDER_UNORDERED\x10\x01\x1a\r\x8a\x9d \tUNORDERED\x12\x1e\n\rORDER_ORDERED\x10\x02\x1a\x0b\x8a\x9d \x07ORDERED\x1a\x04\x88\xa3\x1e\x00B;Z9github.com/cosmos/ibc-go/v4/modules/core/04-channel/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.channel.v1.channel_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z9github.com/cosmos/ibc-go/v4/modules/core/04-channel/types'
    _STATE._options = None
    _STATE._serialized_options = b'\x88\xa3\x1e\x00'
    _STATE.values_by_name['STATE_UNINITIALIZED_UNSPECIFIED']._options = None
    _STATE.values_by_name['STATE_UNINITIALIZED_UNSPECIFIED']._serialized_options = b'\x8a\x9d \rUNINITIALIZED'
    _STATE.values_by_name['STATE_INIT']._options = None
    _STATE.values_by_name['STATE_INIT']._serialized_options = b'\x8a\x9d \x04INIT'
    _STATE.values_by_name['STATE_TRYOPEN']._options = None
    _STATE.values_by_name['STATE_TRYOPEN']._serialized_options = b'\x8a\x9d \x07TRYOPEN'
    _STATE.values_by_name['STATE_OPEN']._options = None
    _STATE.values_by_name['STATE_OPEN']._serialized_options = b'\x8a\x9d \x04OPEN'
    _STATE.values_by_name['STATE_CLOSED']._options = None
    _STATE.values_by_name['STATE_CLOSED']._serialized_options = b'\x8a\x9d \x06CLOSED'
    _ORDER._options = None
    _ORDER._serialized_options = b'\x88\xa3\x1e\x00'
    _ORDER.values_by_name['ORDER_NONE_UNSPECIFIED']._options = None
    _ORDER.values_by_name['ORDER_NONE_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x04NONE'
    _ORDER.values_by_name['ORDER_UNORDERED']._options = None
    _ORDER.values_by_name['ORDER_UNORDERED']._serialized_options = b'\x8a\x9d \tUNORDERED'
    _ORDER.values_by_name['ORDER_ORDERED']._options = None
    _ORDER.values_by_name['ORDER_ORDERED']._serialized_options = b'\x8a\x9d \x07ORDERED'
    _CHANNEL.fields_by_name['counterparty']._options = None
    _CHANNEL.fields_by_name['counterparty']._serialized_options = b'\xc8\xde\x1f\x00'
    _CHANNEL.fields_by_name['connection_hops']._options = None
    _CHANNEL.fields_by_name['connection_hops']._serialized_options = b'\xf2\xde\x1f\x16yaml:"connection_hops"'
    _CHANNEL._options = None
    _CHANNEL._serialized_options = b'\x88\xa0\x1f\x00'
    _IDENTIFIEDCHANNEL.fields_by_name['counterparty']._options = None
    _IDENTIFIEDCHANNEL.fields_by_name['counterparty']._serialized_options = b'\xc8\xde\x1f\x00'
    _IDENTIFIEDCHANNEL.fields_by_name['connection_hops']._options = None
    _IDENTIFIEDCHANNEL.fields_by_name['connection_hops']._serialized_options = b'\xf2\xde\x1f\x16yaml:"connection_hops"'
    _IDENTIFIEDCHANNEL._options = None
    _IDENTIFIEDCHANNEL._serialized_options = b'\x88\xa0\x1f\x00'
    _COUNTERPARTY.fields_by_name['port_id']._options = None
    _COUNTERPARTY.fields_by_name['port_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"port_id"'
    _COUNTERPARTY.fields_by_name['channel_id']._options = None
    _COUNTERPARTY.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _COUNTERPARTY._options = None
    _COUNTERPARTY._serialized_options = b'\x88\xa0\x1f\x00'
    _PACKET.fields_by_name['source_port']._options = None
    _PACKET.fields_by_name['source_port']._serialized_options = b'\xf2\xde\x1f\x12yaml:"source_port"'
    _PACKET.fields_by_name['source_channel']._options = None
    _PACKET.fields_by_name['source_channel']._serialized_options = b'\xf2\xde\x1f\x15yaml:"source_channel"'
    _PACKET.fields_by_name['destination_port']._options = None
    _PACKET.fields_by_name['destination_port']._serialized_options = b'\xf2\xde\x1f\x17yaml:"destination_port"'
    _PACKET.fields_by_name['destination_channel']._options = None
    _PACKET.fields_by_name['destination_channel']._serialized_options = b'\xf2\xde\x1f\x1ayaml:"destination_channel"'
    _PACKET.fields_by_name['timeout_height']._options = None
    _PACKET.fields_by_name['timeout_height']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"timeout_height"'
    _PACKET.fields_by_name['timeout_timestamp']._options = None
    _PACKET.fields_by_name['timeout_timestamp']._serialized_options = b'\xf2\xde\x1f\x18yaml:"timeout_timestamp"'
    _PACKET._options = None
    _PACKET._serialized_options = b'\x88\xa0\x1f\x00'
    _PACKETSTATE.fields_by_name['port_id']._options = None
    _PACKETSTATE.fields_by_name['port_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"port_id"'
    _PACKETSTATE.fields_by_name['channel_id']._options = None
    _PACKETSTATE.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _PACKETSTATE._options = None
    _PACKETSTATE._serialized_options = b'\x88\xa0\x1f\x00'
    _PACKETID.fields_by_name['port_id']._options = None
    _PACKETID.fields_by_name['port_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"port_id"'
    _PACKETID.fields_by_name['channel_id']._options = None
    _PACKETID.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _PACKETID._options = None
    _PACKETID._serialized_options = b'\x88\xa0\x1f\x00'
    _globals['_STATE']._serialized_start = 1460
    _globals['_STATE']._serialized_end = 1643
    _globals['_ORDER']._serialized_start = 1645
    _globals['_ORDER']._serialized_end = 1764
    _globals['_CHANNEL']._serialized_start = 114
    _globals['_CHANNEL']._serialized_end = 351
    _globals['_IDENTIFIEDCHANNEL']._serialized_start = 354
    _globals['_IDENTIFIEDCHANNEL']._serialized_end = 638
    _globals['_COUNTERPARTY']._serialized_start = 640
    _globals['_COUNTERPARTY']._serialized_end = 740
    _globals['_PACKET']._serialized_start = 743
    _globals['_PACKET']._serialized_end = 1141
    _globals['_PACKETSTATE']._serialized_start = 1144
    _globals['_PACKETSTATE']._serialized_end = 1275
    _globals['_PACKETID']._serialized_start = 1277
    _globals['_PACKETID']._serialized_end = 1391
    _globals['_ACKNOWLEDGEMENT']._serialized_start = 1393
    _globals['_ACKNOWLEDGEMENT']._serialized_end = 1457