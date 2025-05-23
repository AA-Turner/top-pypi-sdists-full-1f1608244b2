# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/traffic/v1/traffic_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from _qwak_proto.qwak.traffic.v1 import traffic_pb2 as qwak_dot_traffic_dot_v1_dot_traffic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!qwak/traffic/v1/traffic_api.proto\x12\x0fqwak.traffic.v1\x1a\x1dqwak/traffic/v1/traffic.proto\"e\n\x1eResetAndSetTrafficStateRequest\x12\x43\n\x15multiple_http_traffic\x18\x01 \x01(\x0b\x32$.qwak.traffic.v1.MultipleHttpTraffic\"!\n\x1fResetAndSetTrafficStateResponse\"\x8f\x01\n\x1a\x41pplyGroupedTrafficRequest\x12\x45\n\x15multiple_http_traffic\x18\x01 \x01(\x0b\x32$.qwak.traffic.v1.MultipleHttpTrafficH\x00\x12\x10\n\x08group_id\x18\x02 \x01(\t\x12\r\n\x05hosts\x18\x03 \x03(\tB\t\n\x07traffic\"\x1d\n\x1b\x41pplyGroupedTrafficResponse\"~\n\x15\x43reateEndpointRequest\x12\x10\n\x08group_id\x18\x01 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x02 \x01(\t\x12\x11\n\tvariation\x18\x03 \x01(\t\x12\x1f\n\x17http_request_timeout_ms\x18\x04 \x01(\x05\x12\r\n\x05hosts\x18\x05 \x03(\t\"\x18\n\x16\x43reateEndpointResponse\")\n\x15\x44\x65leteEndpointRequest\x12\x10\n\x08group_id\x18\x01 \x01(\t\"\x18\n\x16\x44\x65leteEndpointResponse2\xc2\x03\n\nTrafficAPI\x12|\n\x17ResetAndSetTrafficState\x12/.qwak.traffic.v1.ResetAndSetTrafficStateRequest\x1a\x30.qwak.traffic.v1.ResetAndSetTrafficStateResponse\x12p\n\x13\x41pplyGroupedTraffic\x12+.qwak.traffic.v1.ApplyGroupedTrafficRequest\x1a,.qwak.traffic.v1.ApplyGroupedTrafficResponse\x12\x61\n\x0e\x43reateEndpoint\x12&.qwak.traffic.v1.CreateEndpointRequest\x1a\'.qwak.traffic.v1.CreateEndpointResponse\x12\x61\n\x0e\x44\x65leteEndpoint\x12&.qwak.traffic.v1.DeleteEndpointRequest\x1a\'.qwak.traffic.v1.DeleteEndpointResponseB\x17\n\x13\x63om.qwak.traffic.v1P\x01\x62\x06proto3')



_RESETANDSETTRAFFICSTATEREQUEST = DESCRIPTOR.message_types_by_name['ResetAndSetTrafficStateRequest']
_RESETANDSETTRAFFICSTATERESPONSE = DESCRIPTOR.message_types_by_name['ResetAndSetTrafficStateResponse']
_APPLYGROUPEDTRAFFICREQUEST = DESCRIPTOR.message_types_by_name['ApplyGroupedTrafficRequest']
_APPLYGROUPEDTRAFFICRESPONSE = DESCRIPTOR.message_types_by_name['ApplyGroupedTrafficResponse']
_CREATEENDPOINTREQUEST = DESCRIPTOR.message_types_by_name['CreateEndpointRequest']
_CREATEENDPOINTRESPONSE = DESCRIPTOR.message_types_by_name['CreateEndpointResponse']
_DELETEENDPOINTREQUEST = DESCRIPTOR.message_types_by_name['DeleteEndpointRequest']
_DELETEENDPOINTRESPONSE = DESCRIPTOR.message_types_by_name['DeleteEndpointResponse']
ResetAndSetTrafficStateRequest = _reflection.GeneratedProtocolMessageType('ResetAndSetTrafficStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETANDSETTRAFFICSTATEREQUEST,
  '__module__' : 'qwak.traffic.v1.traffic_api_pb2'
  # @@protoc_insertion_point(class_scope:qwak.traffic.v1.ResetAndSetTrafficStateRequest)
  })
_sym_db.RegisterMessage(ResetAndSetTrafficStateRequest)

ResetAndSetTrafficStateResponse = _reflection.GeneratedProtocolMessageType('ResetAndSetTrafficStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESETANDSETTRAFFICSTATERESPONSE,
  '__module__' : 'qwak.traffic.v1.traffic_api_pb2'
  # @@protoc_insertion_point(class_scope:qwak.traffic.v1.ResetAndSetTrafficStateResponse)
  })
_sym_db.RegisterMessage(ResetAndSetTrafficStateResponse)

ApplyGroupedTrafficRequest = _reflection.GeneratedProtocolMessageType('ApplyGroupedTrafficRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPLYGROUPEDTRAFFICREQUEST,
  '__module__' : 'qwak.traffic.v1.traffic_api_pb2'
  # @@protoc_insertion_point(class_scope:qwak.traffic.v1.ApplyGroupedTrafficRequest)
  })
_sym_db.RegisterMessage(ApplyGroupedTrafficRequest)

ApplyGroupedTrafficResponse = _reflection.GeneratedProtocolMessageType('ApplyGroupedTrafficResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPLYGROUPEDTRAFFICRESPONSE,
  '__module__' : 'qwak.traffic.v1.traffic_api_pb2'
  # @@protoc_insertion_point(class_scope:qwak.traffic.v1.ApplyGroupedTrafficResponse)
  })
_sym_db.RegisterMessage(ApplyGroupedTrafficResponse)

CreateEndpointRequest = _reflection.GeneratedProtocolMessageType('CreateEndpointRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEENDPOINTREQUEST,
  '__module__' : 'qwak.traffic.v1.traffic_api_pb2'
  # @@protoc_insertion_point(class_scope:qwak.traffic.v1.CreateEndpointRequest)
  })
_sym_db.RegisterMessage(CreateEndpointRequest)

CreateEndpointResponse = _reflection.GeneratedProtocolMessageType('CreateEndpointResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEENDPOINTRESPONSE,
  '__module__' : 'qwak.traffic.v1.traffic_api_pb2'
  # @@protoc_insertion_point(class_scope:qwak.traffic.v1.CreateEndpointResponse)
  })
_sym_db.RegisterMessage(CreateEndpointResponse)

DeleteEndpointRequest = _reflection.GeneratedProtocolMessageType('DeleteEndpointRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEENDPOINTREQUEST,
  '__module__' : 'qwak.traffic.v1.traffic_api_pb2'
  # @@protoc_insertion_point(class_scope:qwak.traffic.v1.DeleteEndpointRequest)
  })
_sym_db.RegisterMessage(DeleteEndpointRequest)

DeleteEndpointResponse = _reflection.GeneratedProtocolMessageType('DeleteEndpointResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEENDPOINTRESPONSE,
  '__module__' : 'qwak.traffic.v1.traffic_api_pb2'
  # @@protoc_insertion_point(class_scope:qwak.traffic.v1.DeleteEndpointResponse)
  })
_sym_db.RegisterMessage(DeleteEndpointResponse)

_TRAFFICAPI = DESCRIPTOR.services_by_name['TrafficAPI']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.qwak.traffic.v1P\001'
  _RESETANDSETTRAFFICSTATEREQUEST._serialized_start=85
  _RESETANDSETTRAFFICSTATEREQUEST._serialized_end=186
  _RESETANDSETTRAFFICSTATERESPONSE._serialized_start=188
  _RESETANDSETTRAFFICSTATERESPONSE._serialized_end=221
  _APPLYGROUPEDTRAFFICREQUEST._serialized_start=224
  _APPLYGROUPEDTRAFFICREQUEST._serialized_end=367
  _APPLYGROUPEDTRAFFICRESPONSE._serialized_start=369
  _APPLYGROUPEDTRAFFICRESPONSE._serialized_end=398
  _CREATEENDPOINTREQUEST._serialized_start=400
  _CREATEENDPOINTREQUEST._serialized_end=526
  _CREATEENDPOINTRESPONSE._serialized_start=528
  _CREATEENDPOINTRESPONSE._serialized_end=552
  _DELETEENDPOINTREQUEST._serialized_start=554
  _DELETEENDPOINTREQUEST._serialized_end=595
  _DELETEENDPOINTRESPONSE._serialized_start=597
  _DELETEENDPOINTRESPONSE._serialized_end=621
  _TRAFFICAPI._serialized_start=624
  _TRAFFICAPI._serialized_end=1074
# @@protoc_insertion_point(module_scope)
