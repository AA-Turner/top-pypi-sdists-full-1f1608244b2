# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nebius/iam/v1/tenant_user_account_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nebius.api.nebius import annotations_pb2 as nebius_dot_annotations__pb2
from nebius.api.nebius.common.v1 import operation_pb2 as nebius_dot_common_dot_v1_dot_operation__pb2
from nebius.api.nebius.iam.v1 import tenant_user_account_pb2 as nebius_dot_iam_dot_v1_dot_tenant__user__account__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/nebius/iam/v1/tenant_user_account_service.proto\x12\rnebius.iam.v1\x1a\x18nebius/annotations.proto\x1a nebius/common/v1/operation.proto\x1a\'nebius/iam/v1/tenant_user_account.proto\"-\n\x1bGetTenantUserAccountRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\xa8\x01\n\x1dListTenantUserAccountsRequest\x12\x1b\n\tparent_id\x18\x01 \x01(\tR\x08parentId\x12 \n\tpage_size\x18\x02 \x01(\x03H\x00R\x08pageSize\x88\x01\x01\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12\x1b\n\x06\x66ilter\x18\x04 \x01(\tB\x03\xc0J\x01R\x06\x66ilterB\x0c\n\n_page_size\"\x80\x01\n\x1eListTenantUserAccountsResponse\x12\x36\n\x05items\x18\x01 \x03(\x0b\x32 .nebius.iam.v1.TenantUserAccountR\x05items\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"/\n\x1d\x42lockTenantUserAccountRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"1\n\x1fUnblockTenantUserAccountRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id2\x8c\x03\n\x18TenantUserAccountService\x12S\n\x03Get\x12*.nebius.iam.v1.GetTenantUserAccountRequest\x1a .nebius.iam.v1.TenantUserAccount\x12\x63\n\x04List\x12,.nebius.iam.v1.ListTenantUserAccountsRequest\x1a-.nebius.iam.v1.ListTenantUserAccountsResponse\x12R\n\x05\x42lock\x12,.nebius.iam.v1.BlockTenantUserAccountRequest\x1a\x1b.nebius.common.v1.Operation\x12V\n\x07Unblock\x12..nebius.iam.v1.UnblockTenantUserAccountRequest\x1a\x1b.nebius.common.v1.Operation\x1a\n\xbaJ\x07\x63pl.iamBd\n\x14\x61i.nebius.pub.iam.v1B\x1dTenantUserAccountServiceProtoP\x01Z+github.com/nebius/gosdk/proto/nebius/iam/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nebius.iam.v1.tenant_user_account_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024ai.nebius.pub.iam.v1B\035TenantUserAccountServiceProtoP\001Z+github.com/nebius/gosdk/proto/nebius/iam/v1'
  _LISTTENANTUSERACCOUNTSREQUEST.fields_by_name['filter']._options = None
  _LISTTENANTUSERACCOUNTSREQUEST.fields_by_name['filter']._serialized_options = b'\300J\001'
  _TENANTUSERACCOUNTSERVICE._options = None
  _TENANTUSERACCOUNTSERVICE._serialized_options = b'\272J\007cpl.iam'
  _globals['_GETTENANTUSERACCOUNTREQUEST']._serialized_start=167
  _globals['_GETTENANTUSERACCOUNTREQUEST']._serialized_end=212
  _globals['_LISTTENANTUSERACCOUNTSREQUEST']._serialized_start=215
  _globals['_LISTTENANTUSERACCOUNTSREQUEST']._serialized_end=383
  _globals['_LISTTENANTUSERACCOUNTSRESPONSE']._serialized_start=386
  _globals['_LISTTENANTUSERACCOUNTSRESPONSE']._serialized_end=514
  _globals['_BLOCKTENANTUSERACCOUNTREQUEST']._serialized_start=516
  _globals['_BLOCKTENANTUSERACCOUNTREQUEST']._serialized_end=563
  _globals['_UNBLOCKTENANTUSERACCOUNTREQUEST']._serialized_start=565
  _globals['_UNBLOCKTENANTUSERACCOUNTREQUEST']._serialized_end=614
  _globals['_TENANTUSERACCOUNTSERVICE']._serialized_start=617
  _globals['_TENANTUSERACCOUNTSERVICE']._serialized_end=1013
# @@protoc_insertion_point(module_scope)
