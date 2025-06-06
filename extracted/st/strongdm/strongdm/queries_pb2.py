# Copyright 2020 StrongDM Inc
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: queries.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2
from . import tags_pb2 as tags__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rqueries.proto\x12\x02v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\roptions.proto\x1a\nspec.proto\x1a\ntags.proto\"\x7f\n\x10QueryListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:(\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\xe6\x01\n\x11QueryListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12&\n\x07queries\x18\x02 \x03(\x0b\x32\t.v1.QueryB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12W\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB,\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x06\xb2\xf4\xb3\x07\x01*\xf2\xf8\xb3\x07\x12\xb2\xf4\xb3\x07\r!json_gateway:(\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\xd3\n\n\x05Query\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1e\n\naccount_id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1f\n\x0bresource_id\x18\x03 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1e\n\nquery_body\x18\x04 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x37\n\x08\x64uration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\tencrypted\x18\x06 \x01(\x08\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1e\n\nquery_hash\x18\x07 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12.\n\x18remote_identity_username\x18\x08 \x01(\tB\x0c\x18\x01\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x39\n\ttimestamp\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x0e\x65gress_node_id\x18\n \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1e\n\nreplayable\x18\x0b \x01(\x08\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12 \n\x0crecord_count\x18\x0c \x01(\x03\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12!\n\rresource_type\x18\r \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x0equery_category\x18\x0e \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\tquery_key\x18\x0f \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12!\n\rresource_name\x18\x10 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12+\n\rresource_tags\x18\x11 \x01(\x0b\x32\x08.v1.TagsB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12&\n\x12\x61\x63\x63ount_first_name\x18\x12 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12%\n\x11\x61\x63\x63ount_last_name\x18\x13 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12!\n\raccount_email\x18\x14 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12*\n\x0c\x61\x63\x63ount_tags\x18\x15 \x01(\x0b\x32\x08.v1.TagsB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12/\n\x0cquery_key_id\x18\x16 \x01(\tB\x19\xf2\xf8\xb3\x07\x14\xb0\xf3\xb3\x07\x01\xb2\xf4\xb3\x07\ngo_private\x12<\n\x0c\x63ompleted_at\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12-\n\x07\x63\x61pture\x18\x18 \x01(\x0b\x32\x10.v1.QueryCaptureB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\tsource_ip\x18\x19 \x01(\tB\"\xf2\xf8\xb3\x07\x1d\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x13\xc2\xf4\xb3\x07\x0e\n\x02go\x12\x08SourceIP\x12\x34\n\x11\x61uthentication_id\x18\x1a \x01(\tB\x19\xf2\xf8\xb3\x07\x14\xb0\xf3\xb3\x07\x01\xb2\xf4\xb3\x07\ngo_private\x12\x1a\n\x06target\x18\x1b \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x36\n\tauthzJson\x18\x1c \x01(\tB#\xf2\xf8\xb3\x07\x1e\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x14\xc2\xf4\xb3\x07\x0f\n\x02go\x12\tAuthzJSON\x12\x35\n\tclient_ip\x18\x1d \x01(\tB\"\xf2\xf8\xb3\x07\x1d\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x13\xc2\xf4\xb3\x07\x0e\n\x02go\x12\x08\x43lientIP\x12+\n\x17identity_alias_username\x18\x1e \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12=\n\rmetadata_json\x18\x1f \x01(\tB&\xf2\xf8\xb3\x07!\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x17\xc2\xf4\xb3\x07\x12\n\x02go\x12\x0cMetadataJSON:2\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider\"\xa3\x05\n\x0cQueryCapture\x12\x19\n\x05width\x18\x01 \x01(\x05\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1a\n\x06height\x18\x02 \x01(\x05\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1b\n\x07\x63ommand\x18\x03 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x32\n\x03\x65nv\x18\x04 \x03(\x0b\x32\x19.v1.QueryCapture.EnvEntryB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x18\n\x04type\x18\x05 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\tfile_name\x18\x06 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\tfile_size\x18\x07 \x01(\x03\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x0e\x63lient_command\x18\x08 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x17\n\x03pod\x18\t \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\tcontainer\x18\n \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\"\n\x0erequest_method\x18\x0b \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x39\n\x0brequest_uri\x18\x0c \x01(\tB$\xf2\xf8\xb3\x07\x1f\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x15\xc2\xf4\xb3\x07\x10\n\x02go\x12\nRequestURI\x12 \n\x0crequest_body\x18\r \x01(\x0c\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12&\n\x12impersonation_user\x18\x0e \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12(\n\x14impersonation_groups\x18\x0f \x03(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12$\n\x10privilege_groups\x18\x10 \x03(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x1a*\n\x08\x45nvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:2\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\xfa\xf8\xb3\x07\x06\xd2\xf3\xb3\x07\x01*\xfa\xf8\xb3\x07\x18\xd2\xf3\xb3\x07\x13!terraform-provider2\xa5\x01\n\x07Queries\x12W\n\x04List\x12\x14.v1.QueryListRequest\x1a\x15.v1.QueryListResponse\"\"\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x10\xaa\xf3\xb3\x07\x0b/v1/queries\x1a\x41\xca\xf9\xb3\x07\n\xc2\xf9\xb3\x07\x05Query\xca\xf9\xb3\x07\x05\xd8\xf9\xb3\x07\x01\xca\xf9\xb3\x07\x06\xca\xf9\xb3\x07\x01*\xca\xf9\xb3\x07\x18\xca\xf9\xb3\x07\x13!terraform-providerB\x8b\x01\n\x19\x63om.strongdm.api.plumbingB\x0fQueriesPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1\xc2\x92\xb4\x07\x06\xa2\x8c\xb4\x07\x01*\xc2\x92\xb4\x07\x18\xa2\x8c\xb4\x07\x13!terraform-providerb\x06proto3')



_QUERYLISTREQUEST = DESCRIPTOR.message_types_by_name['QueryListRequest']
_QUERYLISTRESPONSE = DESCRIPTOR.message_types_by_name['QueryListResponse']
_QUERY = DESCRIPTOR.message_types_by_name['Query']
_QUERYCAPTURE = DESCRIPTOR.message_types_by_name['QueryCapture']
_QUERYCAPTURE_ENVENTRY = _QUERYCAPTURE.nested_types_by_name['EnvEntry']
QueryListRequest = _reflection.GeneratedProtocolMessageType('QueryListRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYLISTREQUEST,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:v1.QueryListRequest)
  })
_sym_db.RegisterMessage(QueryListRequest)

QueryListResponse = _reflection.GeneratedProtocolMessageType('QueryListResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYLISTRESPONSE,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:v1.QueryListResponse)
  })
_sym_db.RegisterMessage(QueryListResponse)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:v1.Query)
  })
_sym_db.RegisterMessage(Query)

QueryCapture = _reflection.GeneratedProtocolMessageType('QueryCapture', (_message.Message,), {

  'EnvEntry' : _reflection.GeneratedProtocolMessageType('EnvEntry', (_message.Message,), {
    'DESCRIPTOR' : _QUERYCAPTURE_ENVENTRY,
    '__module__' : 'queries_pb2'
    # @@protoc_insertion_point(class_scope:v1.QueryCapture.EnvEntry)
    })
  ,
  'DESCRIPTOR' : _QUERYCAPTURE,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:v1.QueryCapture)
  })
_sym_db.RegisterMessage(QueryCapture)
_sym_db.RegisterMessage(QueryCapture.EnvEntry)

_QUERIES = DESCRIPTOR.services_by_name['Queries']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.strongdm.api.plumbingB\017QueriesPlumbingZ5github.com/strongdm/strongdm-sdk-go/v3/internal/v1;v1\302\222\264\007\006\242\214\264\007\001*\302\222\264\007\030\242\214\264\007\023!terraform-provider'
  _QUERYLISTREQUEST.fields_by_name['filter']._options = None
  _QUERYLISTREQUEST.fields_by_name['filter']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYLISTREQUEST._options = None
  _QUERYLISTREQUEST._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _QUERYLISTRESPONSE.fields_by_name['queries']._options = None
  _QUERYLISTRESPONSE.fields_by_name['queries']._serialized_options = b'\362\370\263\007\005\270\363\263\007\001'
  _QUERYLISTRESPONSE.fields_by_name['rate_limit']._options = None
  _QUERYLISTRESPONSE.fields_by_name['rate_limit']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\006\262\364\263\007\001*\362\370\263\007\022\262\364\263\007\r!json_gateway'
  _QUERYLISTRESPONSE._options = None
  _QUERYLISTRESPONSE._serialized_options = b'\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _QUERY.fields_by_name['id']._options = None
  _QUERY.fields_by_name['id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['account_id']._options = None
  _QUERY.fields_by_name['account_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['resource_id']._options = None
  _QUERY.fields_by_name['resource_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['query_body']._options = None
  _QUERY.fields_by_name['query_body']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['duration']._options = None
  _QUERY.fields_by_name['duration']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['encrypted']._options = None
  _QUERY.fields_by_name['encrypted']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['query_hash']._options = None
  _QUERY.fields_by_name['query_hash']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['remote_identity_username']._options = None
  _QUERY.fields_by_name['remote_identity_username']._serialized_options = b'\030\001\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['timestamp']._options = None
  _QUERY.fields_by_name['timestamp']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['egress_node_id']._options = None
  _QUERY.fields_by_name['egress_node_id']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['replayable']._options = None
  _QUERY.fields_by_name['replayable']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['record_count']._options = None
  _QUERY.fields_by_name['record_count']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['resource_type']._options = None
  _QUERY.fields_by_name['resource_type']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['query_category']._options = None
  _QUERY.fields_by_name['query_category']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['query_key']._options = None
  _QUERY.fields_by_name['query_key']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['resource_name']._options = None
  _QUERY.fields_by_name['resource_name']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['resource_tags']._options = None
  _QUERY.fields_by_name['resource_tags']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['account_first_name']._options = None
  _QUERY.fields_by_name['account_first_name']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['account_last_name']._options = None
  _QUERY.fields_by_name['account_last_name']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['account_email']._options = None
  _QUERY.fields_by_name['account_email']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['account_tags']._options = None
  _QUERY.fields_by_name['account_tags']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['query_key_id']._options = None
  _QUERY.fields_by_name['query_key_id']._serialized_options = b'\362\370\263\007\024\260\363\263\007\001\262\364\263\007\ngo_private'
  _QUERY.fields_by_name['completed_at']._options = None
  _QUERY.fields_by_name['completed_at']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['capture']._options = None
  _QUERY.fields_by_name['capture']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['source_ip']._options = None
  _QUERY.fields_by_name['source_ip']._serialized_options = b'\362\370\263\007\035\260\363\263\007\001\312\363\263\007\023\302\364\263\007\016\n\002go\022\010SourceIP'
  _QUERY.fields_by_name['authentication_id']._options = None
  _QUERY.fields_by_name['authentication_id']._serialized_options = b'\362\370\263\007\024\260\363\263\007\001\262\364\263\007\ngo_private'
  _QUERY.fields_by_name['target']._options = None
  _QUERY.fields_by_name['target']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['authzJson']._options = None
  _QUERY.fields_by_name['authzJson']._serialized_options = b'\362\370\263\007\036\260\363\263\007\001\312\363\263\007\024\302\364\263\007\017\n\002go\022\tAuthzJSON'
  _QUERY.fields_by_name['client_ip']._options = None
  _QUERY.fields_by_name['client_ip']._serialized_options = b'\362\370\263\007\035\260\363\263\007\001\312\363\263\007\023\302\364\263\007\016\n\002go\022\010ClientIP'
  _QUERY.fields_by_name['identity_alias_username']._options = None
  _QUERY.fields_by_name['identity_alias_username']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERY.fields_by_name['metadata_json']._options = None
  _QUERY.fields_by_name['metadata_json']._serialized_options = b'\362\370\263\007!\260\363\263\007\001\312\363\263\007\027\302\364\263\007\022\n\002go\022\014MetadataJSON'
  _QUERY._options = None
  _QUERY._serialized_options = b'\372\370\263\007\005\250\363\263\007\001\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _QUERYCAPTURE_ENVENTRY._options = None
  _QUERYCAPTURE_ENVENTRY._serialized_options = b'8\001'
  _QUERYCAPTURE.fields_by_name['width']._options = None
  _QUERYCAPTURE.fields_by_name['width']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['height']._options = None
  _QUERYCAPTURE.fields_by_name['height']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['command']._options = None
  _QUERYCAPTURE.fields_by_name['command']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['env']._options = None
  _QUERYCAPTURE.fields_by_name['env']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['type']._options = None
  _QUERYCAPTURE.fields_by_name['type']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['file_name']._options = None
  _QUERYCAPTURE.fields_by_name['file_name']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['file_size']._options = None
  _QUERYCAPTURE.fields_by_name['file_size']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['client_command']._options = None
  _QUERYCAPTURE.fields_by_name['client_command']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['pod']._options = None
  _QUERYCAPTURE.fields_by_name['pod']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['container']._options = None
  _QUERYCAPTURE.fields_by_name['container']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['request_method']._options = None
  _QUERYCAPTURE.fields_by_name['request_method']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['request_uri']._options = None
  _QUERYCAPTURE.fields_by_name['request_uri']._serialized_options = b'\362\370\263\007\037\260\363\263\007\001\312\363\263\007\025\302\364\263\007\020\n\002go\022\nRequestURI'
  _QUERYCAPTURE.fields_by_name['request_body']._options = None
  _QUERYCAPTURE.fields_by_name['request_body']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['impersonation_user']._options = None
  _QUERYCAPTURE.fields_by_name['impersonation_user']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['impersonation_groups']._options = None
  _QUERYCAPTURE.fields_by_name['impersonation_groups']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE.fields_by_name['privilege_groups']._options = None
  _QUERYCAPTURE.fields_by_name['privilege_groups']._serialized_options = b'\362\370\263\007\005\260\363\263\007\001'
  _QUERYCAPTURE._options = None
  _QUERYCAPTURE._serialized_options = b'\372\370\263\007\005\250\363\263\007\001\372\370\263\007\006\322\363\263\007\001*\372\370\263\007\030\322\363\263\007\023!terraform-provider'
  _QUERIES._options = None
  _QUERIES._serialized_options = b'\312\371\263\007\n\302\371\263\007\005Query\312\371\263\007\005\330\371\263\007\001\312\371\263\007\006\312\371\263\007\001*\312\371\263\007\030\312\371\263\007\023!terraform-provider'
  _QUERIES.methods_by_name['List']._options = None
  _QUERIES.methods_by_name['List']._serialized_options = b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\020\252\363\263\007\013/v1/queries'
  _QUERYLISTREQUEST._serialized_start=125
  _QUERYLISTREQUEST._serialized_end=252
  _QUERYLISTRESPONSE._serialized_start=255
  _QUERYLISTRESPONSE._serialized_end=485
  _QUERY._serialized_start=488
  _QUERY._serialized_end=1851
  _QUERYCAPTURE._serialized_start=1854
  _QUERYCAPTURE._serialized_end=2529
  _QUERYCAPTURE_ENVENTRY._serialized_start=2435
  _QUERYCAPTURE_ENVENTRY._serialized_end=2477
  _QUERIES._serialized_start=2532
  _QUERIES._serialized_end=2697
# @@protoc_insertion_point(module_scope)
