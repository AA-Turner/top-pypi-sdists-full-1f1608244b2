# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/mdb/mysql/v1alpha/resource_preset_service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'yandex/cloud/mdb/mysql/v1alpha/resource_preset_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.mdb.mysql.v1alpha import resource_preset_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1alpha_dot_resource__preset__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<yandex/cloud/mdb/mysql/v1alpha/resource_preset_service.proto\x12\x1eyandex.cloud.mdb.mysql.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x34yandex/cloud/mdb/mysql/v1alpha/resource_preset.proto\x1a\x1dyandex/cloud/validation.proto\"<\n\x18GetResourcePresetRequest\x12 \n\x12resource_preset_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"Z\n\x1aListResourcePresetsRequest\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x8b\x01\n\x1bListResourcePresetsResponse\x12H\n\x10resource_presets\x18\x01 \x03(\x0b\x32..yandex.cloud.mdb.mysql.v1alpha.ResourcePreset\x12\"\n\x0fnext_page_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=1002\x80\x03\n\x15ResourcePresetService\x12\xb4\x01\n\x03Get\x12\x38.yandex.cloud.mdb.mysql.v1alpha.GetResourcePresetRequest\x1a..yandex.cloud.mdb.mysql.v1alpha.ResourcePreset\"C\x82\xd3\xe4\x93\x02=\x12;/managed-mysql/v1alpha/resourcePresets/{resource_preset_id}\x12\xaf\x01\n\x04List\x12:.yandex.cloud.mdb.mysql.v1alpha.ListResourcePresetsRequest\x1a;.yandex.cloud.mdb.mysql.v1alpha.ListResourcePresetsResponse\".\x82\xd3\xe4\x93\x02(\x12&/managed-mysql/v1alpha/resourcePresetsBn\n\"yandex.cloud.api.mdb.mysql.v1alphaZHgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1alpha;mysqlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.mysql.v1alpha.resource_preset_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"yandex.cloud.api.mdb.mysql.v1alphaZHgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1alpha;mysql'
  _globals['_GETRESOURCEPRESETREQUEST'].fields_by_name['resource_preset_id']._loaded_options = None
  _globals['_GETRESOURCEPRESETREQUEST'].fields_by_name['resource_preset_id']._serialized_options = b'\350\3071\001'
  _globals['_LISTRESOURCEPRESETSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTRESOURCEPRESETSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _globals['_LISTRESOURCEPRESETSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTRESOURCEPRESETSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTRESOURCEPRESETSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
  _globals['_LISTRESOURCEPRESETSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_RESOURCEPRESETSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_RESOURCEPRESETSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002=\022;/managed-mysql/v1alpha/resourcePresets/{resource_preset_id}'
  _globals['_RESOURCEPRESETSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_RESOURCEPRESETSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002(\022&/managed-mysql/v1alpha/resourcePresets'
  _globals['_GETRESOURCEPRESETREQUEST']._serialized_start=211
  _globals['_GETRESOURCEPRESETREQUEST']._serialized_end=271
  _globals['_LISTRESOURCEPRESETSREQUEST']._serialized_start=273
  _globals['_LISTRESOURCEPRESETSREQUEST']._serialized_end=363
  _globals['_LISTRESOURCEPRESETSRESPONSE']._serialized_start=366
  _globals['_LISTRESOURCEPRESETSRESPONSE']._serialized_end=505
  _globals['_RESOURCEPRESETSERVICE']._serialized_start=508
  _globals['_RESOURCEPRESETSERVICE']._serialized_end=892
# @@protoc_insertion_point(module_scope)
