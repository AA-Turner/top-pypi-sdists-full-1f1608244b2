# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/feature_store/sources/data_source_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from _qwak_proto.qwak.feature_store.sources import data_source_pb2 as qwak_dot_feature__store_dot_sources_dot_data__source__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4qwak/feature_store/sources/data_source_service.proto\x12\x1aqwak.feature.store.sources\x1a,qwak/feature_store/sources/data_source.proto\"_\n\x17\x43reateDataSourceRequest\x12\x44\n\x10\x64\x61ta_source_spec\x18\x01 \x01(\x0b\x32*.qwak.feature.store.sources.DataSourceSpec\"W\n\x18\x43reateDataSourceResponse\x12;\n\x0b\x64\x61ta_source\x18\x01 \x01(\x0b\x32&.qwak.feature.store.sources.DataSource\"w\n\x17UpdateDataSourceRequest\x12\x16\n\x0e\x64\x61ta_source_id\x18\x01 \x01(\t\x12\x44\n\x10\x64\x61ta_source_spec\x18\x02 \x01(\x0b\x32*.qwak.feature.store.sources.DataSourceSpec\"W\n\x18UpdateDataSourceResponse\x12;\n\x0b\x64\x61ta_source\x18\x01 \x01(\x0b\x32&.qwak.feature.store.sources.DataSource\"1\n\x17\x44\x65leteDataSourceRequest\x12\x16\n\x0e\x64\x61ta_source_id\x18\x01 \x01(\t\"\x1a\n\x18\x44\x65leteDataSourceResponse\"2\n\x18GetDataSourceByIdRequest\x12\x16\n\x0e\x64\x61ta_source_id\x18\x01 \x01(\t\"X\n\x19GetDataSourceByIdResponse\x12;\n\x0b\x64\x61ta_source\x18\x01 \x01(\x0b\x32&.qwak.feature.store.sources.DataSource\"6\n\x1aGetDataSourceByNameRequest\x12\x18\n\x10\x64\x61ta_source_name\x18\x01 \x01(\t\"Z\n\x1bGetDataSourceByNameResponse\x12;\n\x0b\x64\x61ta_source\x18\x01 \x01(\x0b\x32&.qwak.feature.store.sources.DataSource\"\x18\n\x16ListDataSourcesRequest\"W\n\x17ListDataSourcesResponse\x12<\n\x0c\x64\x61ta_sources\x18\x01 \x03(\x0b\x32&.qwak.feature.store.sources.DataSource\"Q\n CreateDataSourceUploadURLRequest\x12\x18\n\x10\x64\x61ta_source_name\x18\x01 \x01(\t\x12\x13\n\x0bobject_name\x18\x02 \x01(\t\"7\n!CreateDataSourceUploadURLResponse\x12\x12\n\nupload_url\x18\x01 \x01(\t2\xd5\x08\n\x11\x44\x61taSourceService\x12}\n\x10\x43reateDataSource\x12\x33.qwak.feature.store.sources.CreateDataSourceRequest\x1a\x34.qwak.feature.store.sources.CreateDataSourceResponse\x12}\n\x10UpdateDataSource\x12\x33.qwak.feature.store.sources.UpdateDataSourceRequest\x1a\x34.qwak.feature.store.sources.UpdateDataSourceResponse\x12}\n\x10\x44\x65leteDataSource\x12\x33.qwak.feature.store.sources.DeleteDataSourceRequest\x1a\x34.qwak.feature.store.sources.DeleteDataSourceResponse\x12\x80\x01\n\x11GetDataSourceById\x12\x34.qwak.feature.store.sources.GetDataSourceByIdRequest\x1a\x35.qwak.feature.store.sources.GetDataSourceByIdResponse\x12\x86\x01\n\x13GetDataSourceByName\x12\x36.qwak.feature.store.sources.GetDataSourceByNameRequest\x1a\x37.qwak.feature.store.sources.GetDataSourceByNameResponse\x12z\n\x0fListDataSources\x12\x32.qwak.feature.store.sources.ListDataSourcesRequest\x1a\x33.qwak.feature.store.sources.ListDataSourcesResponse\x12\x9d\x01\n\x19\x43reateDataSourceUploadURL\x12<.qwak.feature.store.sources.CreateDataSourceUploadURLRequest\x1a=.qwak.feature.store.sources.CreateDataSourceUploadURLResponse\"\x03\x88\x02\x01\x12\x9a\x01\n\x1b\x43reateDataSourceUploadURLV1\x12<.qwak.feature.store.sources.CreateDataSourceUploadURLRequest\x1a=.qwak.feature.store.sources.CreateDataSourceUploadURLResponseB[\n(com.qwak.ai.feature.store.management.apiP\x01Z-qwak/featurestore/sources;featurestoresourcesb\x06proto3')



_CREATEDATASOURCEREQUEST = DESCRIPTOR.message_types_by_name['CreateDataSourceRequest']
_CREATEDATASOURCERESPONSE = DESCRIPTOR.message_types_by_name['CreateDataSourceResponse']
_UPDATEDATASOURCEREQUEST = DESCRIPTOR.message_types_by_name['UpdateDataSourceRequest']
_UPDATEDATASOURCERESPONSE = DESCRIPTOR.message_types_by_name['UpdateDataSourceResponse']
_DELETEDATASOURCEREQUEST = DESCRIPTOR.message_types_by_name['DeleteDataSourceRequest']
_DELETEDATASOURCERESPONSE = DESCRIPTOR.message_types_by_name['DeleteDataSourceResponse']
_GETDATASOURCEBYIDREQUEST = DESCRIPTOR.message_types_by_name['GetDataSourceByIdRequest']
_GETDATASOURCEBYIDRESPONSE = DESCRIPTOR.message_types_by_name['GetDataSourceByIdResponse']
_GETDATASOURCEBYNAMEREQUEST = DESCRIPTOR.message_types_by_name['GetDataSourceByNameRequest']
_GETDATASOURCEBYNAMERESPONSE = DESCRIPTOR.message_types_by_name['GetDataSourceByNameResponse']
_LISTDATASOURCESREQUEST = DESCRIPTOR.message_types_by_name['ListDataSourcesRequest']
_LISTDATASOURCESRESPONSE = DESCRIPTOR.message_types_by_name['ListDataSourcesResponse']
_CREATEDATASOURCEUPLOADURLREQUEST = DESCRIPTOR.message_types_by_name['CreateDataSourceUploadURLRequest']
_CREATEDATASOURCEUPLOADURLRESPONSE = DESCRIPTOR.message_types_by_name['CreateDataSourceUploadURLResponse']
CreateDataSourceRequest = _reflection.GeneratedProtocolMessageType('CreateDataSourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATASOURCEREQUEST,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.CreateDataSourceRequest)
  })
_sym_db.RegisterMessage(CreateDataSourceRequest)

CreateDataSourceResponse = _reflection.GeneratedProtocolMessageType('CreateDataSourceResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATASOURCERESPONSE,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.CreateDataSourceResponse)
  })
_sym_db.RegisterMessage(CreateDataSourceResponse)

UpdateDataSourceRequest = _reflection.GeneratedProtocolMessageType('UpdateDataSourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATASOURCEREQUEST,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.UpdateDataSourceRequest)
  })
_sym_db.RegisterMessage(UpdateDataSourceRequest)

UpdateDataSourceResponse = _reflection.GeneratedProtocolMessageType('UpdateDataSourceResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATASOURCERESPONSE,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.UpdateDataSourceResponse)
  })
_sym_db.RegisterMessage(UpdateDataSourceResponse)

DeleteDataSourceRequest = _reflection.GeneratedProtocolMessageType('DeleteDataSourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASOURCEREQUEST,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.DeleteDataSourceRequest)
  })
_sym_db.RegisterMessage(DeleteDataSourceRequest)

DeleteDataSourceResponse = _reflection.GeneratedProtocolMessageType('DeleteDataSourceResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASOURCERESPONSE,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.DeleteDataSourceResponse)
  })
_sym_db.RegisterMessage(DeleteDataSourceResponse)

GetDataSourceByIdRequest = _reflection.GeneratedProtocolMessageType('GetDataSourceByIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASOURCEBYIDREQUEST,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.GetDataSourceByIdRequest)
  })
_sym_db.RegisterMessage(GetDataSourceByIdRequest)

GetDataSourceByIdResponse = _reflection.GeneratedProtocolMessageType('GetDataSourceByIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASOURCEBYIDRESPONSE,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.GetDataSourceByIdResponse)
  })
_sym_db.RegisterMessage(GetDataSourceByIdResponse)

GetDataSourceByNameRequest = _reflection.GeneratedProtocolMessageType('GetDataSourceByNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASOURCEBYNAMEREQUEST,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.GetDataSourceByNameRequest)
  })
_sym_db.RegisterMessage(GetDataSourceByNameRequest)

GetDataSourceByNameResponse = _reflection.GeneratedProtocolMessageType('GetDataSourceByNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASOURCEBYNAMERESPONSE,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.GetDataSourceByNameResponse)
  })
_sym_db.RegisterMessage(GetDataSourceByNameResponse)

ListDataSourcesRequest = _reflection.GeneratedProtocolMessageType('ListDataSourcesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATASOURCESREQUEST,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.ListDataSourcesRequest)
  })
_sym_db.RegisterMessage(ListDataSourcesRequest)

ListDataSourcesResponse = _reflection.GeneratedProtocolMessageType('ListDataSourcesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATASOURCESRESPONSE,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.ListDataSourcesResponse)
  })
_sym_db.RegisterMessage(ListDataSourcesResponse)

CreateDataSourceUploadURLRequest = _reflection.GeneratedProtocolMessageType('CreateDataSourceUploadURLRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATASOURCEUPLOADURLREQUEST,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.CreateDataSourceUploadURLRequest)
  })
_sym_db.RegisterMessage(CreateDataSourceUploadURLRequest)

CreateDataSourceUploadURLResponse = _reflection.GeneratedProtocolMessageType('CreateDataSourceUploadURLResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATASOURCEUPLOADURLRESPONSE,
  '__module__' : 'qwak.feature_store.sources.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.sources.CreateDataSourceUploadURLResponse)
  })
_sym_db.RegisterMessage(CreateDataSourceUploadURLResponse)

_DATASOURCESERVICE = DESCRIPTOR.services_by_name['DataSourceService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(com.qwak.ai.feature.store.management.apiP\001Z-qwak/featurestore/sources;featurestoresources'
  _DATASOURCESERVICE.methods_by_name['CreateDataSourceUploadURL']._options = None
  _DATASOURCESERVICE.methods_by_name['CreateDataSourceUploadURL']._serialized_options = b'\210\002\001'
  _CREATEDATASOURCEREQUEST._serialized_start=130
  _CREATEDATASOURCEREQUEST._serialized_end=225
  _CREATEDATASOURCERESPONSE._serialized_start=227
  _CREATEDATASOURCERESPONSE._serialized_end=314
  _UPDATEDATASOURCEREQUEST._serialized_start=316
  _UPDATEDATASOURCEREQUEST._serialized_end=435
  _UPDATEDATASOURCERESPONSE._serialized_start=437
  _UPDATEDATASOURCERESPONSE._serialized_end=524
  _DELETEDATASOURCEREQUEST._serialized_start=526
  _DELETEDATASOURCEREQUEST._serialized_end=575
  _DELETEDATASOURCERESPONSE._serialized_start=577
  _DELETEDATASOURCERESPONSE._serialized_end=603
  _GETDATASOURCEBYIDREQUEST._serialized_start=605
  _GETDATASOURCEBYIDREQUEST._serialized_end=655
  _GETDATASOURCEBYIDRESPONSE._serialized_start=657
  _GETDATASOURCEBYIDRESPONSE._serialized_end=745
  _GETDATASOURCEBYNAMEREQUEST._serialized_start=747
  _GETDATASOURCEBYNAMEREQUEST._serialized_end=801
  _GETDATASOURCEBYNAMERESPONSE._serialized_start=803
  _GETDATASOURCEBYNAMERESPONSE._serialized_end=893
  _LISTDATASOURCESREQUEST._serialized_start=895
  _LISTDATASOURCESREQUEST._serialized_end=919
  _LISTDATASOURCESRESPONSE._serialized_start=921
  _LISTDATASOURCESRESPONSE._serialized_end=1008
  _CREATEDATASOURCEUPLOADURLREQUEST._serialized_start=1010
  _CREATEDATASOURCEUPLOADURLREQUEST._serialized_end=1091
  _CREATEDATASOURCEUPLOADURLRESPONSE._serialized_start=1093
  _CREATEDATASOURCEUPLOADURLRESPONSE._serialized_end=1148
  _DATASOURCESERVICE._serialized_start=1151
  _DATASOURCESERVICE._serialized_end=2260
# @@protoc_insertion_point(module_scope)
