# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cognite/seismic/protos/v1/seismic_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cognite.seismic.protos import types_pb2 as cognite_dot_seismic_dot_protos_dot_types__pb2
from cognite.seismic.protos.v1 import seismic_service_datatypes_pb2 as cognite_dot_seismic_dot_protos_dot_v1_dot_seismic__service__datatypes__pb2
from cognite.seismic.protos.v1 import seismic_service_messages_pb2 as cognite_dot_seismic_dot_protos_dot_v1_dot_seismic__service__messages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/cognite/seismic/protos/v1/seismic_service.proto\x12\x16\x63om.cognite.seismic.v1\x1a\"cognite/seismic/protos/types.proto\x1a\x39\x63ognite/seismic/protos/v1/seismic_service_datatypes.proto\x1a\x38\x63ognite/seismic/protos/v1/seismic_service_messages.proto2\xab\x17\n\nSeismicAPI\x12]\n\x0c\x43reateSurvey\x12+.com.cognite.seismic.v1.CreateSurveyRequest\x1a\x1e.com.cognite.seismic.v1.Survey\"\x00\x12o\n\rSearchSurveys\x12,.com.cognite.seismic.v1.SearchSurveysRequest\x1a,.com.cognite.seismic.v1.SearchSurveyResponse\"\x00\x30\x01\x12Y\n\nEditSurvey\x12).com.cognite.seismic.v1.EditSurveyRequest\x1a\x1e.com.cognite.seismic.v1.Survey\"\x00\x12k\n\x0c\x44\x65leteSurvey\x12+.com.cognite.seismic.v1.DeleteSurveyRequest\x1a,.com.cognite.seismic.v1.DeleteSurveyResponse\"\x00\x12\x89\x01\n\x16RegisterSourceSegyFile\x12\x35.com.cognite.seismic.v1.RegisterSourceSegyFileRequest\x1a\x36.com.cognite.seismic.v1.RegisterSourceSegyFileResponse\"\x00\x12}\n\x12\x45\x64itSourceSegyFile\x12\x31.com.cognite.seismic.v1.EditSourceSegyFileRequest\x1a\x32.com.cognite.seismic.v1.EditSourceSegyFileResponse\"\x00\x12\x8f\x01\n\x18UnregisterSourceSegyFile\x12\x37.com.cognite.seismic.v1.UnregisterSourceSegyFileRequest\x1a\x38.com.cognite.seismic.v1.UnregisterSourceSegyFileResponse\"\x00\x12\x83\x01\n\x14IngestSourceSegyFile\x12\x33.com.cognite.seismic.v1.IngestSourceSegyFileRequest\x1a\x34.com.cognite.seismic.v1.IngestSourceSegyFileResponse\"\x00\x12`\n\rCreateSeismic\x12,.com.cognite.seismic.v1.CreateSeismicRequest\x1a\x1f.com.cognite.seismic.v1.Seismic\"\x00\x12\x64\n\x0eSearchSeismics\x12-.com.cognite.seismic.v1.SearchSeismicsRequest\x1a\x1f.com.cognite.seismic.v1.Seismic\"\x00\x30\x01\x12\\\n\x0b\x45\x64itSeismic\x12*.com.cognite.seismic.v1.EditSeismicRequest\x1a\x1f.com.cognite.seismic.v1.Seismic\"\x00\x12n\n\rDeleteSeismic\x12,.com.cognite.seismic.v1.DeleteSeismicRequest\x1a-.com.cognite.seismic.v1.DeleteSeismicResponse\"\x00\x12s\n\x13SearchSeismicStores\x12\x32.com.cognite.seismic.v1.SearchSeismicStoresRequest\x1a$.com.cognite.seismic.v1.SeismicStore\"\x00\x30\x01\x12w\n\x10InspectIngestion\x12/.com.cognite.seismic.v1.InspectIngestionRequest\x1a\x30.com.cognite.seismic.v1.InspectIngestionResponse\"\x00\x12k\n\x10\x45\x64itSeismicStore\x12/.com.cognite.seismic.v1.EditSeismicStoreRequest\x1a$.com.cognite.seismic.v1.SeismicStore\"\x00\x12}\n\x12\x44\x65leteSeismicStore\x12\x31.com.cognite.seismic.v1.DeleteSeismicStoreRequest\x1a\x32.com.cognite.seismic.v1.DeleteSeismicStoreResponse\"\x00\x12\x66\n\x0f\x43reatePartition\x12..com.cognite.seismic.v1.CreatePartitionRequest\x1a!.com.cognite.seismic.v1.Partition\"\x00\x12j\n\x10SearchPartitions\x12/.com.cognite.seismic.v1.SearchPartitionsRequest\x1a!.com.cognite.seismic.v1.Partition\"\x00\x30\x01\x12\x62\n\rEditPartition\x12,.com.cognite.seismic.v1.EditPartitionRequest\x1a!.com.cognite.seismic.v1.Partition\"\x00\x12t\n\x0f\x44\x65letePartition\x12..com.cognite.seismic.v1.DeletePartitionRequest\x1a/.com.cognite.seismic.v1.DeletePartitionResponse\"\x00\x12R\n\tGetVolume\x12%.com.cognite.seismic.v1.VolumeRequest\x1a\x1a.com.cognite.seismic.Trace\"\x00\x30\x01\x12h\n\x0fGetVolumeBounds\x12%.com.cognite.seismic.v1.VolumeRequest\x1a,.com.cognite.seismic.v1.VolumeBoundsResponse\"\x00\x12[\n\x0cStreamTraces\x12+.com.cognite.seismic.v1.StreamTracesRequest\x1a\x1a.com.cognite.seismic.Trace\"\x00\x30\x01\x12\x64\n\x0eGetTraceBounds\x12+.com.cognite.seismic.v1.StreamTracesRequest\x1a#.com.cognite.seismic.v1.TraceBounds\"\x00\x12j\n\x0bGetSegYFile\x12*.com.cognite.seismic.v1.SegYSeismicRequest\x1a+.com.cognite.seismic.v1.SegYSeismicResponse\"\x00\x30\x01\x12\x65\n\x0bSearchFiles\x12*.com.cognite.seismic.v1.SearchFilesRequest\x1a&.com.cognite.seismic.v1.SourceSegyFile\"\x00\x30\x01\x12p\n\x0fSearchJobStatus\x12..com.cognite.seismic.v1.SearchJobStatusRequest\x1a).com.cognite.seismic.v1.JobStatusResponse\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cognite.seismic.protos.v1.seismic_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_SEISMICAPI']._serialized_start=229
  _globals['_SEISMICAPI']._serialized_end=3216
# @@protoc_insertion_point(module_scope)
