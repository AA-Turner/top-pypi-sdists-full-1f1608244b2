# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/google/fhir/proto/r4/core/resources/medicinal_product_undesirable_effect.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from proto.google.fhir.proto import annotations_pb2 as proto_dot_google_dot_fhir_dot_proto_dot_annotations__pb2
from proto.google.fhir.proto.r4.core import datatypes_pb2 as proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/google/fhir/proto/r4/core/resources/medicinal_product_undesirable_effect.proto',
  package='google.fhir.r4.core',
  syntax='proto3',
  serialized_options=b'\n\027com.google.fhir.r4.coreP\001\230\306\260\265\007\004',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nTproto/google/fhir/proto/r4/core/resources/medicinal_product_undesirable_effect.proto\x12\x13google.fhir.r4.core\x1a\x19google/protobuf/any.proto\x1a)proto/google/fhir/proto/annotations.proto\x1a/proto/google/fhir/proto/r4/core/datatypes.proto\"\x8b\x07\n!MedicinalProductUndesirableEffect\x12#\n\x02id\x18\x01 \x01(\x0b\x32\x17.google.fhir.r4.core.Id\x12\'\n\x04meta\x18\x02 \x01(\x0b\x32\x19.google.fhir.r4.core.Meta\x12\x30\n\x0eimplicit_rules\x18\x03 \x01(\x0b\x32\x18.google.fhir.r4.core.Uri\x12+\n\x08language\x18\x04 \x01(\x0b\x32\x19.google.fhir.r4.core.Code\x12,\n\x04text\x18\x05 \x01(\x0b\x32\x1e.google.fhir.r4.core.Narrative\x12\'\n\tcontained\x18\x06 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x31\n\textension\x18\x08 \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12:\n\x12modifier_extension\x18\t \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12W\n\x07subject\x18\n \x03(\x0b\x32\x1e.google.fhir.r4.core.ReferenceB&\xf2\xff\xfc\xc2\x06\x10MedicinalProduct\xf2\xff\xfc\xc2\x06\nMedication\x12\x46\n\x18symptom_condition_effect\x18\x0b \x01(\x0b\x32$.google.fhir.r4.core.CodeableConcept\x12<\n\x0e\x63lassification\x18\x0c \x01(\x0b\x32$.google.fhir.r4.core.CodeableConcept\x12\x45\n\x17\x66requency_of_occurrence\x18\r \x01(\x0b\x32$.google.fhir.r4.core.CodeableConcept\x12\x33\n\npopulation\x18\x0e \x03(\x0b\x32\x1f.google.fhir.r4.core.Population:\x91\x01\xc0\x9f\xe3\xb6\x05\x03\xb2\xfe\xe4\x97\x06Ihttp://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect\xb2\xf5\xf5\xd7\t6\n\x07subject\x10\x05\x1a)MedicinalProductUndesirableEffect.subjectJ\x04\x08\x07\x10\x08\x42!\n\x17\x63om.google.fhir.r4.coreP\x01\x98\xc6\xb0\xb5\x07\x04\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_annotations__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2.DESCRIPTOR,])




_MEDICINALPRODUCTUNDESIRABLEEFFECT = _descriptor.Descriptor(
  name='MedicinalProductUndesirableEffect',
  full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect.meta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='implicit_rules', full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect.implicit_rules', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect.language', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect.text', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contained', full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect.contained', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect.extension', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modifier_extension', full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect.modifier_extension', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subject', full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect.subject', index=8,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\377\374\302\006\020MedicinalProduct\362\377\374\302\006\nMedication', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='symptom_condition_effect', full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect.symptom_condition_effect', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classification', full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect.classification', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frequency_of_occurrence', full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect.frequency_of_occurrence', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='population', full_name='google.fhir.r4.core.MedicinalProductUndesirableEffect.population', index=12,
      number=14, type=11, cpp_type=10, label=3,
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
  serialized_options=b'\300\237\343\266\005\003\262\376\344\227\006Ihttp://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect\262\365\365\327\t6\n\007subject\020\005\032)MedicinalProductUndesirableEffect.subject',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=1136,
)

_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._ID
_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['meta'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._META
_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['implicit_rules'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._URI
_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['language'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODE
_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['text'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._NARRATIVE
_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['contained'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['modifier_extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['subject'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['symptom_condition_effect'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODEABLECONCEPT
_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['classification'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODEABLECONCEPT
_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['frequency_of_occurrence'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODEABLECONCEPT
_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['population'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._POPULATION
DESCRIPTOR.message_types_by_name['MedicinalProductUndesirableEffect'] = _MEDICINALPRODUCTUNDESIRABLEEFFECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MedicinalProductUndesirableEffect = _reflection.GeneratedProtocolMessageType('MedicinalProductUndesirableEffect', (_message.Message,), {
  'DESCRIPTOR' : _MEDICINALPRODUCTUNDESIRABLEEFFECT,
  '__module__' : 'proto.google.fhir.proto.r4.core.resources.medicinal_product_undesirable_effect_pb2'
  # @@protoc_insertion_point(class_scope:google.fhir.r4.core.MedicinalProductUndesirableEffect)
  })
_sym_db.RegisterMessage(MedicinalProductUndesirableEffect)


DESCRIPTOR._options = None
_MEDICINALPRODUCTUNDESIRABLEEFFECT.fields_by_name['subject']._options = None
_MEDICINALPRODUCTUNDESIRABLEEFFECT._options = None
# @@protoc_insertion_point(module_scope)
