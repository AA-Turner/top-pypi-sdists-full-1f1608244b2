# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admobilize/billing/v1alpha1/billing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)admobilize/billing/v1alpha1/billing.proto\x12\x1b\x61\x64mobilize.billing.v1alpha1\"B\n\x0e\x42illingAccount\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04open\x18\x02 \x01(\x08\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\"T\n\x12ProjectBillingInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x1c\n\x14\x62illing_account_name\x18\x03 \x01(\tB\x98\x01\n\x1f\x63om.admobilize.billing.v1alpha1B\x0c\x42illingProtoP\x01Z?bitbucket.org/admobilize/admobilizeapis-go/pkg/billing/v1alpha1\xa2\x02\x05\x41\x44MBL\xaa\x02\x1b\x41\x64Mobilize.Billing.V1Alpha1b\x06proto3')



_BILLINGACCOUNT = DESCRIPTOR.message_types_by_name['BillingAccount']
_PROJECTBILLINGINFO = DESCRIPTOR.message_types_by_name['ProjectBillingInfo']
BillingAccount = _reflection.GeneratedProtocolMessageType('BillingAccount', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGACCOUNT,
  '__module__' : 'admobilize.billing.v1alpha1.billing_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.billing.v1alpha1.BillingAccount)
  })
_sym_db.RegisterMessage(BillingAccount)

ProjectBillingInfo = _reflection.GeneratedProtocolMessageType('ProjectBillingInfo', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTBILLINGINFO,
  '__module__' : 'admobilize.billing.v1alpha1.billing_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.billing.v1alpha1.ProjectBillingInfo)
  })
_sym_db.RegisterMessage(ProjectBillingInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.admobilize.billing.v1alpha1B\014BillingProtoP\001Z?bitbucket.org/admobilize/admobilizeapis-go/pkg/billing/v1alpha1\242\002\005ADMBL\252\002\033AdMobilize.Billing.V1Alpha1'
  _BILLINGACCOUNT._serialized_start=74
  _BILLINGACCOUNT._serialized_end=140
  _PROJECTBILLINGINFO._serialized_start=142
  _PROJECTBILLINGINFO._serialized_end=226
# @@protoc_insertion_point(module_scope)
