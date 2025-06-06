# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/google/fhir/proto/r4/core/resources/care_team.proto
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
  name='proto/google/fhir/proto/r4/core/resources/care_team.proto',
  package='google.fhir.r4.core',
  syntax='proto3',
  serialized_options=b'\n\027com.google.fhir.r4.coreP\001\230\306\260\265\007\004',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9proto/google/fhir/proto/r4/core/resources/care_team.proto\x12\x13google.fhir.r4.core\x1a\x19google/protobuf/any.proto\x1a)proto/google/fhir/proto/annotations.proto\x1a+proto/google/fhir/proto/r4/core/codes.proto\x1a/proto/google/fhir/proto/r4/core/datatypes.proto\"\xa3\'\n\x08\x43\x61reTeam\x12#\n\x02id\x18\x01 \x01(\x0b\x32\x17.google.fhir.r4.core.Id\x12\'\n\x04meta\x18\x02 \x01(\x0b\x32\x19.google.fhir.r4.core.Meta\x12\x30\n\x0eimplicit_rules\x18\x03 \x01(\x0b\x32\x18.google.fhir.r4.core.Uri\x12+\n\x08language\x18\x04 \x01(\x0b\x32\x19.google.fhir.r4.core.Code\x12,\n\x04text\x18\x05 \x01(\x0b\x32\x1e.google.fhir.r4.core.Narrative\x12\'\n\tcontained\x18\x06 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x31\n\textension\x18\x08 \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12:\n\x12modifier_extension\x18\t \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12\x33\n\nidentifier\x18\n \x03(\x0b\x32\x1f.google.fhir.r4.core.Identifier\x12\x38\n\x06status\x18\x0b \x01(\x0b\x32(.google.fhir.r4.core.CareTeam.StatusCode\x12\x36\n\x08\x63\x61tegory\x18\x0c \x03(\x0b\x32$.google.fhir.r4.core.CodeableConcept\x12)\n\x04name\x18\r \x01(\x0b\x32\x1b.google.fhir.r4.core.String\x12I\n\x07subject\x18\x0e \x01(\x0b\x32\x1e.google.fhir.r4.core.ReferenceB\x18\xf2\xff\xfc\xc2\x06\x07Patient\xf2\xff\xfc\xc2\x06\x05Group\x12\x42\n\tencounter\x18\x0f \x01(\x0b\x32\x1e.google.fhir.r4.core.ReferenceB\x0f\xf2\xff\xfc\xc2\x06\tEncounter\x12+\n\x06period\x18\x10 \x01(\x0b\x32\x1b.google.fhir.r4.core.Period\x12>\n\x0bparticipant\x18\x11 \x03(\x0b\x32).google.fhir.r4.core.CareTeam.Participant\x12\x39\n\x0breason_code\x18\x12 \x03(\x0b\x32$.google.fhir.r4.core.CodeableConcept\x12I\n\x10reason_reference\x18\x13 \x03(\x0b\x32\x1e.google.fhir.r4.core.ReferenceB\x0f\xf2\xff\xfc\xc2\x06\tCondition\x12Q\n\x15managing_organization\x18\x14 \x03(\x0b\x32\x1e.google.fhir.r4.core.ReferenceB\x12\xf2\xff\xfc\xc2\x06\x0cOrganization\x12\x32\n\x07telecom\x18\x15 \x03(\x0b\x32!.google.fhir.r4.core.ContactPoint\x12-\n\x04note\x18\x16 \x03(\x0b\x32\x1f.google.fhir.r4.core.Annotation\x1a\x93\x02\n\nStatusCode\x12<\n\x05value\x18\x01 \x01(\x0e\x32-.google.fhir.r4.core.CareTeamStatusCode.Value\x12\'\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.fhir.r4.core.String\x12\x31\n\textension\x18\x03 \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension:k\xc0\x9f\xe3\xb6\x05\x01\x8a\xf9\x83\xb2\x05-http://hl7.org/fhir/ValueSet/care-team-status\x9a\xb5\x8e\x93\x06,http://hl7.org/fhir/StructureDefinition/code\x1a\xd3\x04\n\x0bParticipant\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.google.fhir.r4.core.String\x12\x31\n\textension\x18\x02 \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12:\n\x12modifier_extension\x18\x03 \x03(\x0b\x32\x1e.google.fhir.r4.core.Extension\x12\x32\n\x04role\x18\x04 \x03(\x0b\x32$.google.fhir.r4.core.CodeableConcept\x12\x98\x01\n\x06member\x18\x05 \x01(\x0b\x32\x1e.google.fhir.r4.core.ReferenceBh\xf2\xff\xfc\xc2\x06\x0cPractitioner\xf2\xff\xfc\xc2\x06\x10PractitionerRole\xf2\xff\xfc\xc2\x06\rRelatedPerson\xf2\xff\xfc\xc2\x06\x07Patient\xf2\xff\xfc\xc2\x06\x0cOrganization\xf2\xff\xfc\xc2\x06\x08\x43\x61reTeam\x12H\n\x0con_behalf_of\x18\x06 \x01(\x0b\x32\x1e.google.fhir.r4.core.ReferenceB\x12\xf2\xff\xfc\xc2\x06\x0cOrganization\x12+\n\x06period\x18\x07 \x01(\x0b\x32\x1b.google.fhir.r4.core.Period:f\x9a\x86\x93\xa0\x08`onBehalfOf.exists() implies (member.resolve().iif(empty(), true, ofType(Practitioner).exists())):\xa7\x17\xc0\x9f\xe3\xb6\x05\x03\xb2\xfe\xe4\x97\x06\x30http://hl7.org/fhir/StructureDefinition/CareTeam\xb2\xf5\xf5\xd7\t\x1f\n\x08\x63\x61tegory\x10\x04\x1a\x11\x43\x61reTeam.category\xb2\xf5\xf5\xd7\t\x97\x03\n\x04\x64\x61te\x10\x02\x1a\x8c\x03\x41llergyIntolerance.recordedDate | CarePlan.period | CareTeam.period | ClinicalImpression.date | Composition.date | Consent.dateTime | DiagnosticReport.effective | Encounter.period | EpisodeOfCare.period | FamilyMemberHistory.date | Flag.period | Immunization.occurrence | List.date | Observation.effective | Procedure.performed | (RiskAssessment.occurrence as dateTime) | SupplyRequest.authoredOn\xb2\xf5\xf5\xd7\t!\n\tencounter\x10\x05\x1a\x12\x43\x61reTeam.encounter\xb2\xf5\xf5\xd7\t\x85\x07\n\nidentifier\x10\x04\x1a\xf4\x06\x41llergyIntolerance.identifier | CarePlan.identifier | CareTeam.identifier | Composition.identifier | Condition.identifier | Consent.identifier | DetectedIssue.identifier | DeviceRequest.identifier | DiagnosticReport.identifier | DocumentManifest.masterIdentifier | DocumentManifest.identifier | DocumentReference.masterIdentifier | DocumentReference.identifier | Encounter.identifier | EpisodeOfCare.identifier | FamilyMemberHistory.identifier | Goal.identifier | ImagingStudy.identifier | Immunization.identifier | List.identifier | MedicationAdministration.identifier | MedicationDispense.identifier | MedicationRequest.identifier | MedicationStatement.identifier | NutritionOrder.identifier | Observation.identifier | Procedure.identifier | RiskAssessment.identifier | ServiceRequest.identifier | SupplyDelivery.identifier | SupplyRequest.identifier | VisionPrescription.identifier\xb2\xf5\xf5\xd7\t,\n\x0bparticipant\x10\x05\x1a\x1b\x43\x61reTeam.participant.member\xb2\xf5\xf5\xd7\t\xf8\n\n\x07patient\x10\x05\x1a\xea\nAllergyIntolerance.patient | CarePlan.subject.where(resolve() is Patient) | CareTeam.subject.where(resolve() is Patient) | ClinicalImpression.subject.where(resolve() is Patient) | Composition.subject.where(resolve() is Patient) | Condition.subject.where(resolve() is Patient) | Consent.patient | DetectedIssue.patient | DeviceRequest.subject.where(resolve() is Patient) | DeviceUseStatement.subject | DiagnosticReport.subject.where(resolve() is Patient) | DocumentManifest.subject.where(resolve() is Patient) | DocumentReference.subject.where(resolve() is Patient) | Encounter.subject.where(resolve() is Patient) | EpisodeOfCare.patient | FamilyMemberHistory.patient | Flag.subject.where(resolve() is Patient) | Goal.subject.where(resolve() is Patient) | ImagingStudy.subject.where(resolve() is Patient) | Immunization.patient | List.subject.where(resolve() is Patient) | MedicationAdministration.subject.where(resolve() is Patient) | MedicationDispense.subject.where(resolve() is Patient) | MedicationRequest.subject.where(resolve() is Patient) | MedicationStatement.subject.where(resolve() is Patient) | NutritionOrder.patient | Observation.subject.where(resolve() is Patient) | Procedure.subject.where(resolve() is Patient) | RiskAssessment.subject.where(resolve() is Patient) | ServiceRequest.subject.where(resolve() is Patient) | SupplyDelivery.patient | VisionPrescription.patient\xb2\xf5\xf5\xd7\t\x1b\n\x06status\x10\x04\x1a\x0f\x43\x61reTeam.status\xb2\xf5\xf5\xd7\t\x1d\n\x07subject\x10\x05\x1a\x10\x43\x61reTeam.subjectJ\x04\x08\x07\x10\x08\x42!\n\x17\x63om.google.fhir.r4.coreP\x01\x98\xc6\xb0\xb5\x07\x04\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_annotations__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_codes__pb2.DESCRIPTOR,proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2.DESCRIPTOR,])




_CARETEAM_STATUSCODE = _descriptor.Descriptor(
  name='StatusCode',
  full_name='google.fhir.r4.core.CareTeam.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='google.fhir.r4.core.CareTeam.StatusCode.value', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.r4.core.CareTeam.StatusCode.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.r4.core.CareTeam.StatusCode.extension', index=2,
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
  serialized_options=b'\300\237\343\266\005\001\212\371\203\262\005-http://hl7.org/fhir/ValueSet/care-team-status\232\265\216\223\006,http://hl7.org/fhir/StructureDefinition/code',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1409,
  serialized_end=1684,
)

_CARETEAM_PARTICIPANT = _descriptor.Descriptor(
  name='Participant',
  full_name='google.fhir.r4.core.CareTeam.Participant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.r4.core.CareTeam.Participant.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.r4.core.CareTeam.Participant.extension', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modifier_extension', full_name='google.fhir.r4.core.CareTeam.Participant.modifier_extension', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='google.fhir.r4.core.CareTeam.Participant.role', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='member', full_name='google.fhir.r4.core.CareTeam.Participant.member', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\377\374\302\006\014Practitioner\362\377\374\302\006\020PractitionerRole\362\377\374\302\006\rRelatedPerson\362\377\374\302\006\007Patient\362\377\374\302\006\014Organization\362\377\374\302\006\010CareTeam', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='on_behalf_of', full_name='google.fhir.r4.core.CareTeam.Participant.on_behalf_of', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\377\374\302\006\014Organization', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period', full_name='google.fhir.r4.core.CareTeam.Participant.period', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\232\206\223\240\010`onBehalfOf.exists() implies (member.resolve().iif(empty(), true, ofType(Practitioner).exists()))',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1687,
  serialized_end=2282,
)

_CARETEAM = _descriptor.Descriptor(
  name='CareTeam',
  full_name='google.fhir.r4.core.CareTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.fhir.r4.core.CareTeam.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='google.fhir.r4.core.CareTeam.meta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='implicit_rules', full_name='google.fhir.r4.core.CareTeam.implicit_rules', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='google.fhir.r4.core.CareTeam.language', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='google.fhir.r4.core.CareTeam.text', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contained', full_name='google.fhir.r4.core.CareTeam.contained', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension', full_name='google.fhir.r4.core.CareTeam.extension', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modifier_extension', full_name='google.fhir.r4.core.CareTeam.modifier_extension', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='google.fhir.r4.core.CareTeam.identifier', index=8,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.fhir.r4.core.CareTeam.status', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='google.fhir.r4.core.CareTeam.category', index=10,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.fhir.r4.core.CareTeam.name', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subject', full_name='google.fhir.r4.core.CareTeam.subject', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\377\374\302\006\007Patient\362\377\374\302\006\005Group', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='encounter', full_name='google.fhir.r4.core.CareTeam.encounter', index=13,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\377\374\302\006\tEncounter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period', full_name='google.fhir.r4.core.CareTeam.period', index=14,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='participant', full_name='google.fhir.r4.core.CareTeam.participant', index=15,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason_code', full_name='google.fhir.r4.core.CareTeam.reason_code', index=16,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason_reference', full_name='google.fhir.r4.core.CareTeam.reason_reference', index=17,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\377\374\302\006\tCondition', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='managing_organization', full_name='google.fhir.r4.core.CareTeam.managing_organization', index=18,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\377\374\302\006\014Organization', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='telecom', full_name='google.fhir.r4.core.CareTeam.telecom', index=19,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='note', full_name='google.fhir.r4.core.CareTeam.note', index=20,
      number=22, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CARETEAM_STATUSCODE, _CARETEAM_PARTICIPANT, ],
  enum_types=[
  ],
  serialized_options=b'\300\237\343\266\005\003\262\376\344\227\0060http://hl7.org/fhir/StructureDefinition/CareTeam\262\365\365\327\t\037\n\010category\020\004\032\021CareTeam.category\262\365\365\327\t\227\003\n\004date\020\002\032\214\003AllergyIntolerance.recordedDate | CarePlan.period | CareTeam.period | ClinicalImpression.date | Composition.date | Consent.dateTime | DiagnosticReport.effective | Encounter.period | EpisodeOfCare.period | FamilyMemberHistory.date | Flag.period | Immunization.occurrence | List.date | Observation.effective | Procedure.performed | (RiskAssessment.occurrence as dateTime) | SupplyRequest.authoredOn\262\365\365\327\t!\n\tencounter\020\005\032\022CareTeam.encounter\262\365\365\327\t\205\007\n\nidentifier\020\004\032\364\006AllergyIntolerance.identifier | CarePlan.identifier | CareTeam.identifier | Composition.identifier | Condition.identifier | Consent.identifier | DetectedIssue.identifier | DeviceRequest.identifier | DiagnosticReport.identifier | DocumentManifest.masterIdentifier | DocumentManifest.identifier | DocumentReference.masterIdentifier | DocumentReference.identifier | Encounter.identifier | EpisodeOfCare.identifier | FamilyMemberHistory.identifier | Goal.identifier | ImagingStudy.identifier | Immunization.identifier | List.identifier | MedicationAdministration.identifier | MedicationDispense.identifier | MedicationRequest.identifier | MedicationStatement.identifier | NutritionOrder.identifier | Observation.identifier | Procedure.identifier | RiskAssessment.identifier | ServiceRequest.identifier | SupplyDelivery.identifier | SupplyRequest.identifier | VisionPrescription.identifier\262\365\365\327\t,\n\013participant\020\005\032\033CareTeam.participant.member\262\365\365\327\t\370\n\n\007patient\020\005\032\352\nAllergyIntolerance.patient | CarePlan.subject.where(resolve() is Patient) | CareTeam.subject.where(resolve() is Patient) | ClinicalImpression.subject.where(resolve() is Patient) | Composition.subject.where(resolve() is Patient) | Condition.subject.where(resolve() is Patient) | Consent.patient | DetectedIssue.patient | DeviceRequest.subject.where(resolve() is Patient) | DeviceUseStatement.subject | DiagnosticReport.subject.where(resolve() is Patient) | DocumentManifest.subject.where(resolve() is Patient) | DocumentReference.subject.where(resolve() is Patient) | Encounter.subject.where(resolve() is Patient) | EpisodeOfCare.patient | FamilyMemberHistory.patient | Flag.subject.where(resolve() is Patient) | Goal.subject.where(resolve() is Patient) | ImagingStudy.subject.where(resolve() is Patient) | Immunization.patient | List.subject.where(resolve() is Patient) | MedicationAdministration.subject.where(resolve() is Patient) | MedicationDispense.subject.where(resolve() is Patient) | MedicationRequest.subject.where(resolve() is Patient) | MedicationStatement.subject.where(resolve() is Patient) | NutritionOrder.patient | Observation.subject.where(resolve() is Patient) | Procedure.subject.where(resolve() is Patient) | RiskAssessment.subject.where(resolve() is Patient) | ServiceRequest.subject.where(resolve() is Patient) | SupplyDelivery.patient | VisionPrescription.patient\262\365\365\327\t\033\n\006status\020\004\032\017CareTeam.status\262\365\365\327\t\035\n\007subject\020\005\032\020CareTeam.subject',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=5274,
)

_CARETEAM_STATUSCODE.fields_by_name['value'].enum_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_codes__pb2._CARETEAMSTATUSCODE_VALUE
_CARETEAM_STATUSCODE.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_CARETEAM_STATUSCODE.fields_by_name['extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_CARETEAM_STATUSCODE.containing_type = _CARETEAM
_CARETEAM_PARTICIPANT.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_CARETEAM_PARTICIPANT.fields_by_name['extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_CARETEAM_PARTICIPANT.fields_by_name['modifier_extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_CARETEAM_PARTICIPANT.fields_by_name['role'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODEABLECONCEPT
_CARETEAM_PARTICIPANT.fields_by_name['member'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
_CARETEAM_PARTICIPANT.fields_by_name['on_behalf_of'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
_CARETEAM_PARTICIPANT.fields_by_name['period'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._PERIOD
_CARETEAM_PARTICIPANT.containing_type = _CARETEAM
_CARETEAM.fields_by_name['id'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._ID
_CARETEAM.fields_by_name['meta'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._META
_CARETEAM.fields_by_name['implicit_rules'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._URI
_CARETEAM.fields_by_name['language'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODE
_CARETEAM.fields_by_name['text'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._NARRATIVE
_CARETEAM.fields_by_name['contained'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CARETEAM.fields_by_name['extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_CARETEAM.fields_by_name['modifier_extension'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._EXTENSION
_CARETEAM.fields_by_name['identifier'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._IDENTIFIER
_CARETEAM.fields_by_name['status'].message_type = _CARETEAM_STATUSCODE
_CARETEAM.fields_by_name['category'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODEABLECONCEPT
_CARETEAM.fields_by_name['name'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._STRING
_CARETEAM.fields_by_name['subject'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
_CARETEAM.fields_by_name['encounter'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
_CARETEAM.fields_by_name['period'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._PERIOD
_CARETEAM.fields_by_name['participant'].message_type = _CARETEAM_PARTICIPANT
_CARETEAM.fields_by_name['reason_code'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CODEABLECONCEPT
_CARETEAM.fields_by_name['reason_reference'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
_CARETEAM.fields_by_name['managing_organization'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._REFERENCE
_CARETEAM.fields_by_name['telecom'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._CONTACTPOINT
_CARETEAM.fields_by_name['note'].message_type = proto_dot_google_dot_fhir_dot_proto_dot_r4_dot_core_dot_datatypes__pb2._ANNOTATION
DESCRIPTOR.message_types_by_name['CareTeam'] = _CARETEAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CareTeam = _reflection.GeneratedProtocolMessageType('CareTeam', (_message.Message,), {

  'StatusCode' : _reflection.GeneratedProtocolMessageType('StatusCode', (_message.Message,), {
    'DESCRIPTOR' : _CARETEAM_STATUSCODE,
    '__module__' : 'proto.google.fhir.proto.r4.core.resources.care_team_pb2'
    # @@protoc_insertion_point(class_scope:google.fhir.r4.core.CareTeam.StatusCode)
    })
  ,

  'Participant' : _reflection.GeneratedProtocolMessageType('Participant', (_message.Message,), {
    'DESCRIPTOR' : _CARETEAM_PARTICIPANT,
    '__module__' : 'proto.google.fhir.proto.r4.core.resources.care_team_pb2'
    # @@protoc_insertion_point(class_scope:google.fhir.r4.core.CareTeam.Participant)
    })
  ,
  'DESCRIPTOR' : _CARETEAM,
  '__module__' : 'proto.google.fhir.proto.r4.core.resources.care_team_pb2'
  # @@protoc_insertion_point(class_scope:google.fhir.r4.core.CareTeam)
  })
_sym_db.RegisterMessage(CareTeam)
_sym_db.RegisterMessage(CareTeam.StatusCode)
_sym_db.RegisterMessage(CareTeam.Participant)


DESCRIPTOR._options = None
_CARETEAM_STATUSCODE._options = None
_CARETEAM_PARTICIPANT.fields_by_name['member']._options = None
_CARETEAM_PARTICIPANT.fields_by_name['on_behalf_of']._options = None
_CARETEAM_PARTICIPANT._options = None
_CARETEAM.fields_by_name['subject']._options = None
_CARETEAM.fields_by_name['encounter']._options = None
_CARETEAM.fields_by_name['reason_reference']._options = None
_CARETEAM.fields_by_name['managing_organization']._options = None
_CARETEAM._options = None
# @@protoc_insertion_point(module_scope)
