# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/google/fhir/proto/r4/core/profiles/actual_group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from proto.google.fhir.proto import annotations_pb2 as proto_dot_google_dot_fhir_dot_proto_dot_annotations__pb2
from proto.google.fhir.proto.r4.core import codes_pb2 as proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_codes__pb2
from proto.google.fhir.proto.r4.core import datatypes_pb2 as proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/google/fhir/proto/r4/core/profiles/actual_group.proto',
  package='google.fhir.r4.core',
  syntax='proto3',
  serialized_options=b'\n\027com.google.fhir.r4.coreP\001\230\306\260\265\007\004',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;proto/google/fhir/proto/r4/core/profiles/actual_group.proto\x12\x13google.fhir.r4.core\x1a\x19google/protobuf/any.proto\x1a)proto/google/fhir/proto/annotations.proto\x1a+proto/google/fhir/proto/r4/core/codes.proto\x1a/proto/google/fhir/proto/r4/core/datatypes.proto\"\xd0\x11\n\x0b\x41\x63tualGroup\x12#\n\x02id\x18\x01 \x01(\x0b\x32\x17.google.fhir.r4.core.Id\x12\'\n\x04meta\x18\x02 \x01(\x0b\x32\x19.google.fhir.r4.core.Meta\x12\x30\n\x0eimplicit_rules\x18\x03 \x01(\x0b\x32\x18.google.fhir.r4.core.Uri\x12+\n\x08language\x18\x04 \x01(\x0b\x32\x19.google.fhir.r4.core.Code\x12,\n\x04text\x18\x05 \x01(\x0b\x32\x1e.google.fhir.r4.core.Narrative\x12\'\n\tcontained\x18\x06 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x31\n\textension\x18\x08 \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12:\n\x12modifier_extension\x18\t \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12\x33\n\nidentifier\x18\n \x03(\x0b\x32\x1f.google.fhir.r4.core.Identifier\x12,\n\x06\x61\x63tive\x18\x0b \x01(\x0b\x32\x1c.google.fhir.r4.core.Boolean\x12?\n\x04type\x18\x0c \x01(\x0b\x32).google.fhir.r4.core.ActualGroup.TypeCodeB\x06\xf0\xd0\x87\xeb\x04\x01\x12\x34\n\x06\x61\x63tual\x18\r \x01(\x0b\x32\x1c.google.fhir.r4.core.BooleanB\x06\xf0\xd0\x87\xeb\x04\x01\x12\x32\n\x04\x63ode\x18\x0e \x01(\x0b\x32$.google.fhir.r4.core.CodeableConcept\x12)\n\x04name\x18\x0f \x01(\x0b\x32\x1b.google.fhir.r4.core.String\x12\x32\n\x08quantity\x18\x10 \x01(\x0b\x32 .google.fhir.r4.core.UnsignedInt\x12\x86\x01\n\x0fmanaging_entity\x18\x11 \x01(\x0b\x32\x1e.google.fhir.r4.core.ReferenceBM\xf2\xff\xfc\xc2\x06\x0cOrganization\xf2\xff\xfc\xc2\x06\rRelatedPerson\xf2\xff\xfc\xc2\x06\x0cPractitioner\xf2\xff\xfc\xc2\x06\x10PractitionerRole\x12\x37\n\x06member\x18\x13 \x03(\x0b\x32\'.google.fhir.r4.core.ActualGroup.Member\x1a\x86\x02\n\x08TypeCode\x12\x37\n\x05value\x18\x01 \x01(\x0e\x32(.google.fhir.r4.core.GroupTypeCode.Value\x12\'\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.fhir.r4.core.String\x12\x31\n\textension\x18\x03 \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension:e\xc0\x9f\xe3\xb6\x05\x01\x8a\xf9\x83\xb2\x05\'http://hl7.org/fhir/ValueSet/group-type\x9a\xb5\x8e\x93\x06,http://hl7.org/fhir/StructureDefinition/code\x1a\xa1\x03\n\x06Member\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.google.fhir.r4.core.String\x12\x31\n\textension\x18\x02 \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12:\n\x12modifier_extension\x18\x03 \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12\xa1\x01\n\x06\x65ntity\x18\x04 \x01(\x0b\x32\x1e.google.fhir.r4.core.ReferenceBq\xf0\xd0\x87\xeb\x04\x01\xf2\xff\xfc\xc2\x06\x07Patient\xf2\xff\xfc\xc2\x06\x0cPractitioner\xf2\xff\xfc\xc2\x06\x10PractitionerRole\xf2\xff\xfc\xc2\x06\x06\x44\x65vice\xf2\xff\xfc\xc2\x06\nMedication\xf2\xff\xfc\xc2\x06\tSubstance\xf2\xff\xfc\xc2\x06\x05Group\x12+\n\x06period\x18\x05 \x01(\x0b\x32\x1b.google.fhir.r4.core.Period\x12.\n\x08inactive\x18\x06 \x01(\x0b\x32\x1c.google.fhir.r4.core.Boolean:\xe5\x04\xc0\x9f\xe3\xb6\x05\x03\x9a\xb5\x8e\x93\x06-http://hl7.org/fhir/StructureDefinition/Group\xb2\xfe\xe4\x97\x06\x33http://hl7.org/fhir/StructureDefinition/actualgroup\x9a\x86\x93\xa0\x08!member.empty() or (actual = true)\xb2\xf5\xf5\xd7\t\x18\n\x06\x61\x63tual\x10\x04\x1a\x0cGroup.actual\xb2\xf5\xf5\xd7\t-\n\x0e\x63haracteristic\x10\x04\x1a\x19Group.characteristic.code\xb2\xf5\xf5\xd7\t.\n\x14\x63haracteristic-value\x10\x06\x1a\x14Group.characteristic\xb2\xf5\xf5\xd7\t\x14\n\x04\x63ode\x10\x04\x1a\nGroup.code\xb2\xf5\xf5\xd7\t)\n\x07\x65xclude\x10\x04\x1a\x1cGroup.characteristic.exclude\xb2\xf5\xf5\xd7\t \n\nidentifier\x10\x04\x1a\x10Group.identifier\xb2\xf5\xf5\xd7\t)\n\x0fmanaging-entity\x10\x05\x1a\x14Group.managingEntity\xb2\xf5\xf5\xd7\t\x1f\n\x06member\x10\x05\x1a\x13Group.member.entity\xb2\xf5\xf5\xd7\t\x14\n\x04type\x10\x04\x1a\nGroup.type\xb2\xf5\xf5\xd7\td\n\x05value\x10\x04\x1aY(Group.characteristic.value as CodeableConcept) | (Group.characteristic.value as boolean)J\x04\x08\x07\x10\x08J\x04\x08\x12\x10\x13\x42!\n\x17\x63om.google.fhir.r4.coreP\x01\x98\xc6\xb0\xb5\x07\x04\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_annotations__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_codes__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2.DESCRIPTOR,])




_ACTUALGROUP_TYPECODE = _descriptor.Descriptor(
  name='TypeCode',
  full_name='google.fhir.r4.core.ActualGroup.TypeCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='google.fhir.r4.core.ActualGroup.TypeCode.value', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.r4.core.ActualGroup.TypeCode.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.r4.core.ActualGroup.TypeCode.extension', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\300\237\343\266\005\001\212\371\203\262\005\'http://hl7.org/fhir/ValueSet/group-type\232\265\216\223\006,http://hl7.org/fhir/StructureDefinition/code',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1195,
  serialized_end=1457,
)

_ACTUALGROUP_MEMBER = _descriptor.Descriptor(
  name='Member',
  full_name='google.fhir.r4.core.ActualGroup.Member',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.r4.core.ActualGroup.Member.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.r4.core.ActualGroup.Member.extension', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modifier_extension', full_name='google.fhir.r4.core.ActualGroup.Member.modifier_extension', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity', full_name='google.fhir.r4.core.ActualGroup.Member.entity', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001\362\377\374\302\006\007Patient\362\377\374\302\006\014Practitioner\362\377\374\302\006\020PractitionerRole\362\377\374\302\006\006Device\362\377\374\302\006\nMedication\362\377\374\302\006\tSubstance\362\377\374\302\006\005Group', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period', full_name='google.fhir.r4.core.ActualGroup.Member.period', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inactive', full_name='google.fhir.r4.core.ActualGroup.Member.inactive', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1460,
  serialized_end=1877,
)

_ACTUALGROUP = _descriptor.Descriptor(
  name='ActualGroup',
  full_name='google.fhir.r4.core.ActualGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.r4.core.ActualGroup.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='google.fhir.r4.core.ActualGroup.meta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='implicit_rules', full_name='google.fhir.r4.core.ActualGroup.implicit_rules', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='google.fhir.r4.core.ActualGroup.language', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='google.fhir.r4.core.ActualGroup.text', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contained', full_name='google.fhir.r4.core.ActualGroup.contained', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.r4.core.ActualGroup.extension', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modifier_extension', full_name='google.fhir.r4.core.ActualGroup.modifier_extension', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='google.fhir.r4.core.ActualGroup.identifier', index=8,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active', full_name='google.fhir.r4.core.ActualGroup.active', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.fhir.r4.core.ActualGroup.type', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actual', full_name='google.fhir.r4.core.ActualGroup.actual', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\360\320\207\353\004\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='google.fhir.r4.core.ActualGroup.code', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.fhir.r4.core.ActualGroup.name', index=13,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='google.fhir.r4.core.ActualGroup.quantity', index=14,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='managing_entity', full_name='google.fhir.r4.core.ActualGroup.managing_entity', index=15,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\377\374\302\006\014Organization\362\377\374\302\006\rRelatedPerson\362\377\374\302\006\014Practitioner\362\377\374\302\006\020PractitionerRole', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='member', full_name='google.fhir.r4.core.ActualGroup.member', index=16,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ACTUALGROUP_TYPECODE, _ACTUALGROUP_MEMBER, ],
  enum_types=[
  ],
  serialized_options=b'\300\237\343\266\005\003\232\265\216\223\006-http://hl7.org/fhir/StructureDefinition/Group\262\376\344\227\0063http://hl7.org/fhir/StructureDefinition/actualgroup\232\206\223\240\010!member.empty() or (actual = true)\262\365\365\327\t\030\n\006actual\020\004\032\014Group.actual\262\365\365\327\t-\n\016characteristic\020\004\032\031Group.characteristic.code\262\365\365\327\t.\n\024characteristic-value\020\006\032\024Group.characteristic\262\365\365\327\t\024\n\004code\020\004\032\nGroup.code\262\365\365\327\t)\n\007exclude\020\004\032\034Group.characteristic.exclude\262\365\365\327\t \n\nidentifier\020\004\032\020Group.identifier\262\365\365\327\t)\n\017managing-entity\020\005\032\024Group.managingEntity\262\365\365\327\t\037\n\006member\020\005\032\023Group.member.entity\262\365\365\327\t\024\n\004type\020\004\032\nGroup.type\262\365\365\327\td\n\005value\020\004\032Y(Group.characteristic.value as CodeableConcept) | (Group.characteristic.value as boolean)',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=2505,
)

_ACTUALGROUP_TYPECODE.fields_by_name['value'].enum_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_codes__pb2._GROUPTYPECODE_VALUE
_ACTUALGROUP_TYPECODE.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_ACTUALGROUP_TYPECODE.fields_by_name['extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_ACTUALGROUP_TYPECODE.containing_type = _ACTUALGROUP
_ACTUALGROUP_MEMBER.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_ACTUALGROUP_MEMBER.fields_by_name['extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_ACTUALGROUP_MEMBER.fields_by_name['modifier_extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_ACTUALGROUP_MEMBER.fields_by_name['entity'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
_ACTUALGROUP_MEMBER.fields_by_name['period'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._PERIOD
_ACTUALGROUP_MEMBER.fields_by_name['inactive'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._BOOLEAN
_ACTUALGROUP_MEMBER.containing_type = _ACTUALGROUP
_ACTUALGROUP.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._ID
_ACTUALGROUP.fields_by_name['meta'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._META
_ACTUALGROUP.fields_by_name['implicit_rules'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._URI
_ACTUALGROUP.fields_by_name['language'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODE
_ACTUALGROUP.fields_by_name['text'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._NARRATIVE
_ACTUALGROUP.fields_by_name['contained'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_ACTUALGROUP.fields_by_name['extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_ACTUALGROUP.fields_by_name['modifier_extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_ACTUALGROUP.fields_by_name['identifier'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._IDENTIFIER
_ACTUALGROUP.fields_by_name['active'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._BOOLEAN
_ACTUALGROUP.fields_by_name['type'].message_type = _ACTUALGROUP_TYPECODE
_ACTUALGROUP.fields_by_name['actual'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._BOOLEAN
_ACTUALGROUP.fields_by_name['code'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODEABLECONCEPT
_ACTUALGROUP.fields_by_name['name'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_ACTUALGROUP.fields_by_name['quantity'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._UNSIGNEDINT
_ACTUALGROUP.fields_by_name['managing_entity'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
_ACTUALGROUP.fields_by_name['member'].message_type = _ACTUALGROUP_MEMBER
DESCRIPTOR.message_types_by_name['ActualGroup'] = _ACTUALGROUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActualGroup = _reflection.GeneratedProtocolMessageType('ActualGroup', (_message.Message,), {

  'TypeCode' : _reflection.GeneratedProtocolMessageType('TypeCode', (_message.Message,), {
    'DESCRIPTOR' : _ACTUALGROUP_TYPECODE,
    '__module__' : 'proto.google.fhir.proto.r4.core.profiles.actual_group_pb2'
    # @@protoc_insertion_point(class_scope:google.fhir.r4.core.ActualGroup.TypeCode)
    })
  ,

  'Member' : _reflection.GeneratedProtocolMessageType('Member', (_message.Message,), {
    'DESCRIPTOR' : _ACTUALGROUP_MEMBER,
    '__module__' : 'proto.google.fhir.proto.r4.core.profiles.actual_group_pb2'
    # @@protoc_insertion_point(class_scope:google.fhir.r4.core.ActualGroup.Member)
    })
  ,
  'DESCRIPTOR' : _ACTUALGROUP,
  '__module__' : 'proto.google.fhir.proto.r4.core.profiles.actual_group_pb2'
  # @@protoc_insertion_point(class_scope:google.fhir.r4.core.ActualGroup)
  })
_sym_db.RegisterMessage(ActualGroup)
_sym_db.RegisterMessage(ActualGroup.TypeCode)
_sym_db.RegisterMessage(ActualGroup.Member)


DESCRIPTOR._options = None
_ACTUALGROUP_TYPECODE._options = None
_ACTUALGROUP_MEMBER.fields_by_name['entity']._options = None
_ACTUALGROUP.fields_by_name['type']._options = None
_ACTUALGROUP.fields_by_name['actual']._options = None
_ACTUALGROUP.fields_by_name['managing_entity']._options = None
_ACTUALGROUP._options = None
# @@protoc_insertion_point(module_scope)
