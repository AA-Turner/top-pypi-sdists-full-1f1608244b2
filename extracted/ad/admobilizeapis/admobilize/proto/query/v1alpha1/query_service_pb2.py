# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admobilize/query/v1alpha1/query_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from admobilize.proto.query.v1alpha1 import resources_pb2 as admobilize_dot_query_dot_v1alpha1_dot_resources__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-admobilize/query/v1alpha1/query_service.proto\x12\x19\x61\x64mobilize.query.v1alpha1\x1a)admobilize/query/v1alpha1/resources.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\".\n\x1b\x43reateProjectDatasetRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\"\xdc\x07\n\x0cQueryRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x32\n\x07metrics\x18\x03 \x03(\x0b\x32!.admobilize.query.v1alpha1.Metric\x12\x12\n\ndimensions\x18\x04 \x03(\t\x12\r\n\x05\x65poch\x18\x05 \x01(\t\x12\x16\n\x0ehas_comparison\x18\x06 \x01(\x08\x12\x44\n\x10\x61ggregate_result\x18\x0b \x01(\x0b\x32*.admobilize.query.v1alpha1.AggregateResult\x12\x45\n\x11query_from_result\x18( \x01(\x0b\x32*.admobilize.query.v1alpha1.QueryFromResult\x12:\n\x0b\x63lassifiers\x18\x0c \x03(\x0b\x32%.admobilize.query.v1alpha1.Classifier\x12\x0f\n\x07timeout\x18\t \x01(\r\x12\r\n\x05limit\x18\n \x01(\r\x12\x1a\n\x12\x64imensions_encoder\x18\r \x01(\x08\x12@\n\x0e\x65ncoder_params\x18* \x01(\x0b\x32(.admobilize.query.v1alpha1.EncoderParams\x12\x37\n\x08order_by\x18\x0f \x03(\x0b\x32%.admobilize.query.v1alpha1.OrderField\x12\x16\n\x0e\x66ilter_by_hour\x18\x10 \x03(\r\x12\x19\n\x11\x66ilter_by_weekday\x18\x11 \x03(\r\x12?\n\x0e\x66ilter_by_time\x18\x12 \x01(\x0b\x32\'.admobilize.query.v1alpha1.FilterByTime\x12\x36\n\x0b\x63ms_metrics\x18\x13 \x03(\x0b\x32!.admobilize.query.v1alpha1.Metric\x12>\n\rcms_dimension\x18\x14 \x01(\x0b\x32\'.admobilize.query.v1alpha1.CMSDimension\x12@\n\x0e\x63ms_descriptor\x18\x1e \x01(\x0b\x32(.admobilize.query.v1alpha1.CMSDescriptor\x12.\n\nstart_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08timezone\x18\x0e \x01(\t\x12\x0c\n\x03wid\x18\xe6\x07 \x01(\t\x12\x11\n\x08previous\x18\xe7\x07 \x01(\x08\"R\n\rQueryResponse\x12\x34\n\x08\x64\x61tasets\x18\x01 \x03(\x0b\x32\".admobilize.query.v1alpha1.Dataset\x12\x0b\n\x03tid\x18\x02 \x01(\t\"$\n\x11ListTablesRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\"$\n\x12ListTablesResponse\x12\x0e\n\x06tables\x18\x01 \x03(\t\"7\n\x15GetTableSchemaRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\"\x91\x01\n\x16GetTableSchemaResponse\x12\x36\n\x06schema\x18\x01 \x03(\x0b\x32&.admobilize.query.v1alpha1.SchemaField\x12\x10\n\x08num_rows\x18\x02 \x01(\x04\x12\x11\n\tnum_bytes\x18\x03 \x01(\x03\x12\x1a\n\x12last_modified_time\x18\x04 \x01(\x06\"\x9c\x03\n\x12GetReportRequestV2\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x11\n\tsolutions\x18\x02 \x03(\t\x12\x10\n\x03\x63ms\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12N\n\x15timestamp_granularity\x18\x05 \x01(\x0e\x32/.admobilize.query.v1alpha1.TimestampGranularity\x12.\n\nstart_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08timezone\x18\x08 \x01(\t\x12\x0e\n\x06\x66ields\x18\t \x03(\t\x12\x12\n\ndevice_ids\x18\n \x03(\t\x12\x13\n\x0b\x61\x64vertisers\x18\x0b \x03(\t\x12\x0e\n\x06medias\x18\x0c \x03(\t\x12\x10\n\x08weekdays\x18\r \x03(\r\x12\r\n\x05hours\x18\x0e \x03(\r\x12\x0f\n\x07\x64ry_run\x18\x0f \x01(\x08\x42\x06\n\x04_cms\"\x83\x04\n\x10GetReportRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\r\n\x05\x65poch\x18\x03 \x01(\t\x12\x10\n\x08timezone\x18\t \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x0e\n\x06\x66ormat\x18\n \x01(\t\x12\x12\n\nspeed_unit\x18\x0b \x01(\t\x12\x19\n\x11\x66ilter_by_weekday\x18\x0c \x03(\r\x12?\n\x0e\x66ilter_by_time\x18\r \x01(\x0b\x32\'.admobilize.query.v1alpha1.FilterByTime\x12\x0e\n\x06\x66ields\x18\x0e \x03(\t\x12.\n\nstart_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x07\x64\x65vices\x18\x08 \x03(\x0b\x32$.admobilize.query.v1alpha1.DeviceMap\x12\x13\n\x0b\x61\x64vertisers\x18\x10 \x03(\t\x12\x0e\n\x06medias\x18\x11 \x03(\t\x12:\n\x08solution\x18\x12 \x01(\x0e\x32#.admobilize.query.v1alpha1.SolutionH\x00\x88\x01\x01\x42\x0b\n\t_solution\"Z\n\x11GetReportResponse\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32!.admobilize.query.v1alpha1.Status\x12\x12\n\nreport_url\x18\x02 \x01(\t\"\xdf\x01\n\x10\x43reateJobRequest\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\x12\n\nproduct_id\x18\x04 \x01(\t\x12\x10\n\x08timezone\x18\x07 \x01(\t\x12\x12\n\nspeed_unit\x18\x08 \x01(\t\x12\x12\n\ndevice_ids\x18\x05 \x03(\t\x12\x0b\n\x03\x63ms\x18\x06 \x01(\t\"G\n\rGetJobRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12*\n\x06\x66ields\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"I\n\x14GetJobResultRequests\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"2\n\x14\x45xportResultsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\"j\n\x15GetDatapointsResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x14\n\x0cjob_complete\x18\x02 \x01(\x08\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12\x12\n\ndatapoints\x18\x04 \x01(\t\"K\n\x15\x45xportResultsResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x14\n\x0cjob_complete\x18\x02 \x01(\x08\x12\x0c\n\x04urls\x18\x03 \x03(\t\"\xca\x03\n\x13GetTableDataRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x0e\n\x06layout\x18\x03 \x01(\t\x12\x13\n\x0bmax_results\x18\x04 \x01(\r\x12\x12\n\npage_token\x18\x05 \x01(\t\x12\r\n\x05\x65poch\x18\x06 \x01(\t\x12\x35\n\x07\x64\x65vices\x18\x07 \x03(\x0b\x32$.admobilize.query.v1alpha1.DeviceMap\x12\x19\n\x11\x66ilter_by_weekday\x18\x08 \x03(\r\x12?\n\x0e\x66ilter_by_time\x18\t \x01(\x0b\x32\'.admobilize.query.v1alpha1.FilterByTime\x12\x10\n\x08group_by\x18\n \x03(\t\x12\x36\n\tfilter_by\x18\x0b \x01(\x0b\x32#.admobilize.query.v1alpha1.FilterBy\x12.\n\nstart_time\x18\x61 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x62 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08timezone\x18\x63 \x01(\t\"T\n\x14GetTableDataResponse\x12\x12\n\npage_token\x18\x02 \x01(\t\x12(\n\x04rows\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.ListValue\"4\n\x12ListReportsRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\"I\n\x13ListReportsResponse\x12\x32\n\x07reports\x18\x01 \x03(\x0b\x32!.admobilize.query.v1alpha1.Report\"\xc6\x03\n\x13\x43reateReportRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x10\n\x08interval\x18\x03 \x01(\t\x12\x10\n\x08timezone\x18\t \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x0e\n\x06\x66ormat\x18\n \x01(\t\x12\x12\n\nspeed_unit\x18\x0b \x01(\t\x12\x11\n\tfrequency\x18\x0c \x01(\t\x12\x14\n\x0c\x64\x61ys_to_send\x18\r \x03(\t\x12\x19\n\x11\x66ilter_by_weekday\x18\x0e \x03(\r\x12?\n\x0e\x66ilter_by_time\x18\x0f \x01(\x0b\x32\'.admobilize.query.v1alpha1.FilterByTime\x12.\n\nstart_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x64\x65vices\x18\x08 \x03(\t\x12\x13\n\x0b\x61\x64vertisers\x18\x10 \x03(\t\x12\x0e\n\x06medias\x18\x11 \x03(\t\x12\x11\n\tsolutions\x18\x12 \x03(\t\"\xdc\x02\n\x13UpdateReportRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0e\n\x06report\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x0c \x01(\t\x12\x10\n\x08interval\x18\x03 \x01(\t\x12\x10\n\x08timezone\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x03(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x07 \x01(\t\x12\x12\n\nspeed_unit\x18\x08 \x01(\t\x12\x11\n\tfrequency\x18\t \x01(\t\x12\x14\n\x0c\x64\x61ys_to_send\x18\n \x03(\t\x12\x19\n\x11\x66ilter_by_weekday\x18\r \x03(\r\x12?\n\x0e\x66ilter_by_time\x18\x0e \x01(\x0b\x32\'.admobilize.query.v1alpha1.FilterByTime\x12,\n\x08\x65nd_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"D\n\x12PauseReportRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x0e\n\x06report\x18\x03 \x01(\t\"F\n\x14RestartReportRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x0e\n\x06report\x18\x03 \x01(\t\"E\n\x13\x43\x61ncelReportRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x0e\n\x06report\x18\x03 \x01(\t\"\xb7\x01\n\x17GetDeviceHeatmapRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x03 \x01(\t\x12.\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66ilter\x18\x06 \x01(\t\"Q\n\x15ListDashboardResponse\x12\x38\n\ndashboards\x18\x01 \x03(\x0b\x32$.admobilize.query.v1alpha1.Dashboard\"(\n\x13GetDashboardRequest\x12\x11\n\tdashboard\x18\x01 \x01(\t\"\x96\x01\n\x14GetMobileDataRequest\x12\r\n\x05sites\x18\x01 \x03(\t\x12\x11\n\tdimension\x18\x02 \x01(\t\x12.\n\nstart_time\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"]\n\x15GetMobileDataResponse\x12\x37\n\x08\x64\x61tasets\x18\x01 \x03(\x0b\x32%.admobilize.query.v1alpha1.MobileData\x12\x0b\n\x03tid\x18\x02 \x01(\t\"*\n\nMobileData\x12\r\n\x05label\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"I\n\x16GetReportFieldsRequest\x12\x11\n\tsolutions\x18\x01 \x03(\t\x12\x0b\n\x03\x63ms\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\"\x1e\n\x0cReportFields\x12\x0e\n\x06\x66ields\x18\x01 \x03(\t2\xda\x1b\n\x0cQueryService\x12\x91\x01\n\x14\x43reateProjectDataset\x12\x36.admobilize.query.v1alpha1.CreateProjectDatasetRequest\x1a\".admobilize.query.v1alpha1.Project\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v1alpha1/projects:\x01*\x12\x9c\x01\n\x05Query\x12\'.admobilize.query.v1alpha1.QueryRequest\x1a(.admobilize.query.v1alpha1.QueryResponse\"@\x82\xd3\xe4\x93\x02:\"5/v1alpha1/projects/{project=*}/tables/{table=*}/query:\x01*\x12\x98\x01\n\nListTables\x12,.admobilize.query.v1alpha1.ListTablesRequest\x1a-.admobilize.query.v1alpha1.ListTablesResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/v1alpha1/projects/{project=*}/tables\x12\xae\x01\n\x0eGetTableSchema\x12\x30.admobilize.query.v1alpha1.GetTableSchemaRequest\x1a\x31.admobilize.query.v1alpha1.GetTableSchemaResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//v1alpha1/projects/{project=*}/tables/{table=*}\x12x\n\x0eListDashboards\x12\x16.google.protobuf.Empty\x1a\x30.admobilize.query.v1alpha1.ListDashboardResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v1alpha1/dashboards\x12\x90\x01\n\x0cGetDashboard\x12..admobilize.query.v1alpha1.GetDashboardRequest\x1a$.admobilize.query.v1alpha1.Dashboard\"*\x82\xd3\xe4\x93\x02$\x12\"/v1alpha1/dashboards/{dashboard=*}\x12\xa9\x01\n\tGetReport\x12+.admobilize.query.v1alpha1.GetReportRequest\x1a,.admobilize.query.v1alpha1.GetReportResponse\"A\x82\xd3\xe4\x93\x02;\"6/v1alpha1/projects/{project=*}/tables/{table=*}/report:\x01*\x12\xad\x01\n\x0bGetReportV2\x12-.admobilize.query.v1alpha1.GetReportRequestV2\x1a,.admobilize.query.v1alpha1.GetReportResponse\"A\x82\xd3\xe4\x93\x02;\"6/v1alpha2/projects/{project=*}/tables/{table=*}/report:\x01*\x12\xb2\x01\n\x11GetReportFieldsV2\x12\x31.admobilize.query.v1alpha1.GetReportFieldsRequest\x1a\'.admobilize.query.v1alpha1.ReportFields\"A\x82\xd3\xe4\x93\x02;\"6/v1alpha2/projects/{project=*}/tables/{table=*}/fields:\x01*\x12\xa5\x01\n\x0c\x43reateReport\x12..admobilize.query.v1alpha1.CreateReportRequest\x1a!.admobilize.query.v1alpha1.Report\"B\x82\xd3\xe4\x93\x02<\"7/v1alpha1/projects/{project=*}/tables/{table=*}/reports:\x01*\x12\x9f\x01\n\x0cUpdateReport\x12..admobilize.query.v1alpha1.UpdateReportRequest\x1a!.admobilize.query.v1alpha1.Report\"<\x82\xd3\xe4\x93\x02\x36\x1a\x31/v1alpha1/projects/{project=*}/reports/{report=*}:\x01*\x12\x9c\x01\n\x0bListReports\x12-.admobilize.query.v1alpha1.ListReportsRequest\x1a..admobilize.query.v1alpha1.ListReportsResponse\".\x82\xd3\xe4\x93\x02(\x12&/v1alpha1/projects/{project=*}/reports\x12\xb4\x01\n\x0bPauseReport\x12-.admobilize.query.v1alpha1.PauseReportRequest\x1a!.admobilize.query.v1alpha1.Report\"S\x82\xd3\xe4\x93\x02M\"H/v1alpha1/projects/{project=*}/tables/{table=*}/reports/{report=*}:pause:\x01*\x12\xba\x01\n\rRestartReport\x12/.admobilize.query.v1alpha1.RestartReportRequest\x1a!.admobilize.query.v1alpha1.Report\"U\x82\xd3\xe4\x93\x02O\"J/v1alpha1/projects/{project=*}/tables/{table=*}/reports/{report=*}:restart:\x01*\x12\xb0\x01\n\x0c\x43\x61ncelReport\x12..admobilize.query.v1alpha1.CancelReportRequest\x1a!.admobilize.query.v1alpha1.Report\"M\x82\xd3\xe4\x93\x02G*B/v1alpha1/projects/{project=*}/tables/{table=*}/reports/{report=*}:\x01*\x12\xb0\x01\n\x0cGetTableData\x12..admobilize.query.v1alpha1.GetTableDataRequest\x1a/.admobilize.query.v1alpha1.GetTableDataResponse\"?\x82\xd3\xe4\x93\x02\x39\"4/v1alpha1/projects/{project=*}/tables/{table=*}/data:\x01*\x12\xbe\x01\n\x10GetDeviceHeatmap\x12\x32.admobilize.query.v1alpha1.GetDeviceHeatmapRequest\x1a\".admobilize.query.v1alpha1.Heatmap\"R\x82\xd3\xe4\x93\x02L\x12J/v1alpha1/projects/{project=*}/tables/{table=*}/devices/{device=*}/heatmap\x12\x8c\x01\n\rGetMobileData\x12/.admobilize.query.v1alpha1.GetMobileDataRequest\x1a\x30.admobilize.query.v1alpha1.GetMobileDataResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1alpha1/mobile\x12p\n\tCreateJob\x12+.admobilize.query.v1alpha1.CreateJobRequest\x1a\x1e.admobilize.query.v1alpha1.Job\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0e/v1alpha1/jobs\x12q\n\x06GetJob\x12(.admobilize.query.v1alpha1.GetJobRequest\x1a\x1e.admobilize.query.v1alpha1.Job\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1alpha1/{id=jobs/*}\x12\x99\x01\n\rGetJobResults\x12/.admobilize.query.v1alpha1.GetJobResultRequests\x1a\x30.admobilize.query.v1alpha1.GetDatapointsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1alpha1/{id=jobs/*}/results\x12\x98\x01\n\rExportResults\x12/.admobilize.query.v1alpha1.ExportResultsRequest\x1a\x30.admobilize.query.v1alpha1.ExportResultsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1alpha1/{id=jobs/*}/exportB\x9c\x01\n\x1d\x63om.admobilize.query.v1alpha1B\x13QueryResourcesProtoP\x01Z@bitbucket.org/admobilize/admobilizeapis-go/pkg/queryapi/v1alpha1\xa2\x02\x05\x41\x44MQY\xaa\x02\x19\x41\x64Mobilize.Query.V1Alpha1b\x06proto3')



_CREATEPROJECTDATASETREQUEST = DESCRIPTOR.message_types_by_name['CreateProjectDatasetRequest']
_QUERYREQUEST = DESCRIPTOR.message_types_by_name['QueryRequest']
_QUERYRESPONSE = DESCRIPTOR.message_types_by_name['QueryResponse']
_LISTTABLESREQUEST = DESCRIPTOR.message_types_by_name['ListTablesRequest']
_LISTTABLESRESPONSE = DESCRIPTOR.message_types_by_name['ListTablesResponse']
_GETTABLESCHEMAREQUEST = DESCRIPTOR.message_types_by_name['GetTableSchemaRequest']
_GETTABLESCHEMARESPONSE = DESCRIPTOR.message_types_by_name['GetTableSchemaResponse']
_GETREPORTREQUESTV2 = DESCRIPTOR.message_types_by_name['GetReportRequestV2']
_GETREPORTREQUEST = DESCRIPTOR.message_types_by_name['GetReportRequest']
_GETREPORTRESPONSE = DESCRIPTOR.message_types_by_name['GetReportResponse']
_CREATEJOBREQUEST = DESCRIPTOR.message_types_by_name['CreateJobRequest']
_GETJOBREQUEST = DESCRIPTOR.message_types_by_name['GetJobRequest']
_GETJOBRESULTREQUESTS = DESCRIPTOR.message_types_by_name['GetJobResultRequests']
_EXPORTRESULTSREQUEST = DESCRIPTOR.message_types_by_name['ExportResultsRequest']
_GETDATAPOINTSRESPONSE = DESCRIPTOR.message_types_by_name['GetDatapointsResponse']
_EXPORTRESULTSRESPONSE = DESCRIPTOR.message_types_by_name['ExportResultsResponse']
_GETTABLEDATAREQUEST = DESCRIPTOR.message_types_by_name['GetTableDataRequest']
_GETTABLEDATARESPONSE = DESCRIPTOR.message_types_by_name['GetTableDataResponse']
_LISTREPORTSREQUEST = DESCRIPTOR.message_types_by_name['ListReportsRequest']
_LISTREPORTSRESPONSE = DESCRIPTOR.message_types_by_name['ListReportsResponse']
_CREATEREPORTREQUEST = DESCRIPTOR.message_types_by_name['CreateReportRequest']
_UPDATEREPORTREQUEST = DESCRIPTOR.message_types_by_name['UpdateReportRequest']
_PAUSEREPORTREQUEST = DESCRIPTOR.message_types_by_name['PauseReportRequest']
_RESTARTREPORTREQUEST = DESCRIPTOR.message_types_by_name['RestartReportRequest']
_CANCELREPORTREQUEST = DESCRIPTOR.message_types_by_name['CancelReportRequest']
_GETDEVICEHEATMAPREQUEST = DESCRIPTOR.message_types_by_name['GetDeviceHeatmapRequest']
_LISTDASHBOARDRESPONSE = DESCRIPTOR.message_types_by_name['ListDashboardResponse']
_GETDASHBOARDREQUEST = DESCRIPTOR.message_types_by_name['GetDashboardRequest']
_GETMOBILEDATAREQUEST = DESCRIPTOR.message_types_by_name['GetMobileDataRequest']
_GETMOBILEDATARESPONSE = DESCRIPTOR.message_types_by_name['GetMobileDataResponse']
_MOBILEDATA = DESCRIPTOR.message_types_by_name['MobileData']
_GETREPORTFIELDSREQUEST = DESCRIPTOR.message_types_by_name['GetReportFieldsRequest']
_REPORTFIELDS = DESCRIPTOR.message_types_by_name['ReportFields']
CreateProjectDatasetRequest = _reflection.GeneratedProtocolMessageType('CreateProjectDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPROJECTDATASETREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.CreateProjectDatasetRequest)
  })
_sym_db.RegisterMessage(CreateProjectDatasetRequest)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.QueryRequest)
  })
_sym_db.RegisterMessage(QueryRequest)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSE,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.QueryResponse)
  })
_sym_db.RegisterMessage(QueryResponse)

ListTablesRequest = _reflection.GeneratedProtocolMessageType('ListTablesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTABLESREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.ListTablesRequest)
  })
_sym_db.RegisterMessage(ListTablesRequest)

ListTablesResponse = _reflection.GeneratedProtocolMessageType('ListTablesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTABLESRESPONSE,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.ListTablesResponse)
  })
_sym_db.RegisterMessage(ListTablesResponse)

GetTableSchemaRequest = _reflection.GeneratedProtocolMessageType('GetTableSchemaRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTABLESCHEMAREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetTableSchemaRequest)
  })
_sym_db.RegisterMessage(GetTableSchemaRequest)

GetTableSchemaResponse = _reflection.GeneratedProtocolMessageType('GetTableSchemaResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTABLESCHEMARESPONSE,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetTableSchemaResponse)
  })
_sym_db.RegisterMessage(GetTableSchemaResponse)

GetReportRequestV2 = _reflection.GeneratedProtocolMessageType('GetReportRequestV2', (_message.Message,), {
  'DESCRIPTOR' : _GETREPORTREQUESTV2,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetReportRequestV2)
  })
_sym_db.RegisterMessage(GetReportRequestV2)

GetReportRequest = _reflection.GeneratedProtocolMessageType('GetReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREPORTREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetReportRequest)
  })
_sym_db.RegisterMessage(GetReportRequest)

GetReportResponse = _reflection.GeneratedProtocolMessageType('GetReportResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETREPORTRESPONSE,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetReportResponse)
  })
_sym_db.RegisterMessage(GetReportResponse)

CreateJobRequest = _reflection.GeneratedProtocolMessageType('CreateJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEJOBREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.CreateJobRequest)
  })
_sym_db.RegisterMessage(CreateJobRequest)

GetJobRequest = _reflection.GeneratedProtocolMessageType('GetJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetJobRequest)
  })
_sym_db.RegisterMessage(GetJobRequest)

GetJobResultRequests = _reflection.GeneratedProtocolMessageType('GetJobResultRequests', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBRESULTREQUESTS,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetJobResultRequests)
  })
_sym_db.RegisterMessage(GetJobResultRequests)

ExportResultsRequest = _reflection.GeneratedProtocolMessageType('ExportResultsRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTRESULTSREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.ExportResultsRequest)
  })
_sym_db.RegisterMessage(ExportResultsRequest)

GetDatapointsResponse = _reflection.GeneratedProtocolMessageType('GetDatapointsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATAPOINTSRESPONSE,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetDatapointsResponse)
  })
_sym_db.RegisterMessage(GetDatapointsResponse)

ExportResultsResponse = _reflection.GeneratedProtocolMessageType('ExportResultsResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTRESULTSRESPONSE,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.ExportResultsResponse)
  })
_sym_db.RegisterMessage(ExportResultsResponse)

GetTableDataRequest = _reflection.GeneratedProtocolMessageType('GetTableDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTABLEDATAREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetTableDataRequest)
  })
_sym_db.RegisterMessage(GetTableDataRequest)

GetTableDataResponse = _reflection.GeneratedProtocolMessageType('GetTableDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTABLEDATARESPONSE,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetTableDataResponse)
  })
_sym_db.RegisterMessage(GetTableDataResponse)

ListReportsRequest = _reflection.GeneratedProtocolMessageType('ListReportsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTREPORTSREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.ListReportsRequest)
  })
_sym_db.RegisterMessage(ListReportsRequest)

ListReportsResponse = _reflection.GeneratedProtocolMessageType('ListReportsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTREPORTSRESPONSE,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.ListReportsResponse)
  })
_sym_db.RegisterMessage(ListReportsResponse)

CreateReportRequest = _reflection.GeneratedProtocolMessageType('CreateReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREPORTREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.CreateReportRequest)
  })
_sym_db.RegisterMessage(CreateReportRequest)

UpdateReportRequest = _reflection.GeneratedProtocolMessageType('UpdateReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREPORTREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.UpdateReportRequest)
  })
_sym_db.RegisterMessage(UpdateReportRequest)

PauseReportRequest = _reflection.GeneratedProtocolMessageType('PauseReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAUSEREPORTREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.PauseReportRequest)
  })
_sym_db.RegisterMessage(PauseReportRequest)

RestartReportRequest = _reflection.GeneratedProtocolMessageType('RestartReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESTARTREPORTREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.RestartReportRequest)
  })
_sym_db.RegisterMessage(RestartReportRequest)

CancelReportRequest = _reflection.GeneratedProtocolMessageType('CancelReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELREPORTREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.CancelReportRequest)
  })
_sym_db.RegisterMessage(CancelReportRequest)

GetDeviceHeatmapRequest = _reflection.GeneratedProtocolMessageType('GetDeviceHeatmapRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDEVICEHEATMAPREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetDeviceHeatmapRequest)
  })
_sym_db.RegisterMessage(GetDeviceHeatmapRequest)

ListDashboardResponse = _reflection.GeneratedProtocolMessageType('ListDashboardResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDASHBOARDRESPONSE,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.ListDashboardResponse)
  })
_sym_db.RegisterMessage(ListDashboardResponse)

GetDashboardRequest = _reflection.GeneratedProtocolMessageType('GetDashboardRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDASHBOARDREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetDashboardRequest)
  })
_sym_db.RegisterMessage(GetDashboardRequest)

GetMobileDataRequest = _reflection.GeneratedProtocolMessageType('GetMobileDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMOBILEDATAREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetMobileDataRequest)
  })
_sym_db.RegisterMessage(GetMobileDataRequest)

GetMobileDataResponse = _reflection.GeneratedProtocolMessageType('GetMobileDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMOBILEDATARESPONSE,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetMobileDataResponse)
  })
_sym_db.RegisterMessage(GetMobileDataResponse)

MobileData = _reflection.GeneratedProtocolMessageType('MobileData', (_message.Message,), {
  'DESCRIPTOR' : _MOBILEDATA,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.MobileData)
  })
_sym_db.RegisterMessage(MobileData)

GetReportFieldsRequest = _reflection.GeneratedProtocolMessageType('GetReportFieldsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREPORTFIELDSREQUEST,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.GetReportFieldsRequest)
  })
_sym_db.RegisterMessage(GetReportFieldsRequest)

ReportFields = _reflection.GeneratedProtocolMessageType('ReportFields', (_message.Message,), {
  'DESCRIPTOR' : _REPORTFIELDS,
  '__module__' : 'admobilize.query.v1alpha1.query_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.query.v1alpha1.ReportFields)
  })
_sym_db.RegisterMessage(ReportFields)

_QUERYSERVICE = DESCRIPTOR.services_by_name['QueryService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.admobilize.query.v1alpha1B\023QueryResourcesProtoP\001Z@bitbucket.org/admobilize/admobilizeapis-go/pkg/queryapi/v1alpha1\242\002\005ADMQY\252\002\031AdMobilize.Query.V1Alpha1'
  _QUERYSERVICE.methods_by_name['CreateProjectDataset']._options = None
  _QUERYSERVICE.methods_by_name['CreateProjectDataset']._serialized_options = b'\202\323\344\223\002\027\"\022/v1alpha1/projects:\001*'
  _QUERYSERVICE.methods_by_name['Query']._options = None
  _QUERYSERVICE.methods_by_name['Query']._serialized_options = b'\202\323\344\223\002:\"5/v1alpha1/projects/{project=*}/tables/{table=*}/query:\001*'
  _QUERYSERVICE.methods_by_name['ListTables']._options = None
  _QUERYSERVICE.methods_by_name['ListTables']._serialized_options = b'\202\323\344\223\002\'\022%/v1alpha1/projects/{project=*}/tables'
  _QUERYSERVICE.methods_by_name['GetTableSchema']._options = None
  _QUERYSERVICE.methods_by_name['GetTableSchema']._serialized_options = b'\202\323\344\223\0021\022//v1alpha1/projects/{project=*}/tables/{table=*}'
  _QUERYSERVICE.methods_by_name['ListDashboards']._options = None
  _QUERYSERVICE.methods_by_name['ListDashboards']._serialized_options = b'\202\323\344\223\002\026\022\024/v1alpha1/dashboards'
  _QUERYSERVICE.methods_by_name['GetDashboard']._options = None
  _QUERYSERVICE.methods_by_name['GetDashboard']._serialized_options = b'\202\323\344\223\002$\022\"/v1alpha1/dashboards/{dashboard=*}'
  _QUERYSERVICE.methods_by_name['GetReport']._options = None
  _QUERYSERVICE.methods_by_name['GetReport']._serialized_options = b'\202\323\344\223\002;\"6/v1alpha1/projects/{project=*}/tables/{table=*}/report:\001*'
  _QUERYSERVICE.methods_by_name['GetReportV2']._options = None
  _QUERYSERVICE.methods_by_name['GetReportV2']._serialized_options = b'\202\323\344\223\002;\"6/v1alpha2/projects/{project=*}/tables/{table=*}/report:\001*'
  _QUERYSERVICE.methods_by_name['GetReportFieldsV2']._options = None
  _QUERYSERVICE.methods_by_name['GetReportFieldsV2']._serialized_options = b'\202\323\344\223\002;\"6/v1alpha2/projects/{project=*}/tables/{table=*}/fields:\001*'
  _QUERYSERVICE.methods_by_name['CreateReport']._options = None
  _QUERYSERVICE.methods_by_name['CreateReport']._serialized_options = b'\202\323\344\223\002<\"7/v1alpha1/projects/{project=*}/tables/{table=*}/reports:\001*'
  _QUERYSERVICE.methods_by_name['UpdateReport']._options = None
  _QUERYSERVICE.methods_by_name['UpdateReport']._serialized_options = b'\202\323\344\223\0026\0321/v1alpha1/projects/{project=*}/reports/{report=*}:\001*'
  _QUERYSERVICE.methods_by_name['ListReports']._options = None
  _QUERYSERVICE.methods_by_name['ListReports']._serialized_options = b'\202\323\344\223\002(\022&/v1alpha1/projects/{project=*}/reports'
  _QUERYSERVICE.methods_by_name['PauseReport']._options = None
  _QUERYSERVICE.methods_by_name['PauseReport']._serialized_options = b'\202\323\344\223\002M\"H/v1alpha1/projects/{project=*}/tables/{table=*}/reports/{report=*}:pause:\001*'
  _QUERYSERVICE.methods_by_name['RestartReport']._options = None
  _QUERYSERVICE.methods_by_name['RestartReport']._serialized_options = b'\202\323\344\223\002O\"J/v1alpha1/projects/{project=*}/tables/{table=*}/reports/{report=*}:restart:\001*'
  _QUERYSERVICE.methods_by_name['CancelReport']._options = None
  _QUERYSERVICE.methods_by_name['CancelReport']._serialized_options = b'\202\323\344\223\002G*B/v1alpha1/projects/{project=*}/tables/{table=*}/reports/{report=*}:\001*'
  _QUERYSERVICE.methods_by_name['GetTableData']._options = None
  _QUERYSERVICE.methods_by_name['GetTableData']._serialized_options = b'\202\323\344\223\0029\"4/v1alpha1/projects/{project=*}/tables/{table=*}/data:\001*'
  _QUERYSERVICE.methods_by_name['GetDeviceHeatmap']._options = None
  _QUERYSERVICE.methods_by_name['GetDeviceHeatmap']._serialized_options = b'\202\323\344\223\002L\022J/v1alpha1/projects/{project=*}/tables/{table=*}/devices/{device=*}/heatmap'
  _QUERYSERVICE.methods_by_name['GetMobileData']._options = None
  _QUERYSERVICE.methods_by_name['GetMobileData']._serialized_options = b'\202\323\344\223\002\022\022\020/v1alpha1/mobile'
  _QUERYSERVICE.methods_by_name['CreateJob']._options = None
  _QUERYSERVICE.methods_by_name['CreateJob']._serialized_options = b'\202\323\344\223\002\020\"\016/v1alpha1/jobs'
  _QUERYSERVICE.methods_by_name['GetJob']._options = None
  _QUERYSERVICE.methods_by_name['GetJob']._serialized_options = b'\202\323\344\223\002\027\022\025/v1alpha1/{id=jobs/*}'
  _QUERYSERVICE.methods_by_name['GetJobResults']._options = None
  _QUERYSERVICE.methods_by_name['GetJobResults']._serialized_options = b'\202\323\344\223\002\037\022\035/v1alpha1/{id=jobs/*}/results'
  _QUERYSERVICE.methods_by_name['ExportResults']._options = None
  _QUERYSERVICE.methods_by_name['ExportResults']._serialized_options = b'\202\323\344\223\002\036\022\034/v1alpha1/{id=jobs/*}/export'
  _CREATEPROJECTDATASETREQUEST._serialized_start=275
  _CREATEPROJECTDATASETREQUEST._serialized_end=321
  _QUERYREQUEST._serialized_start=324
  _QUERYREQUEST._serialized_end=1312
  _QUERYRESPONSE._serialized_start=1314
  _QUERYRESPONSE._serialized_end=1396
  _LISTTABLESREQUEST._serialized_start=1398
  _LISTTABLESREQUEST._serialized_end=1434
  _LISTTABLESRESPONSE._serialized_start=1436
  _LISTTABLESRESPONSE._serialized_end=1472
  _GETTABLESCHEMAREQUEST._serialized_start=1474
  _GETTABLESCHEMAREQUEST._serialized_end=1529
  _GETTABLESCHEMARESPONSE._serialized_start=1532
  _GETTABLESCHEMARESPONSE._serialized_end=1677
  _GETREPORTREQUESTV2._serialized_start=1680
  _GETREPORTREQUESTV2._serialized_end=2092
  _GETREPORTREQUEST._serialized_start=2095
  _GETREPORTREQUEST._serialized_end=2610
  _GETREPORTRESPONSE._serialized_start=2612
  _GETREPORTRESPONSE._serialized_end=2702
  _CREATEJOBREQUEST._serialized_start=2705
  _CREATEJOBREQUEST._serialized_end=2928
  _GETJOBREQUEST._serialized_start=2930
  _GETJOBREQUEST._serialized_end=3001
  _GETJOBRESULTREQUESTS._serialized_start=3003
  _GETJOBRESULTREQUESTS._serialized_end=3076
  _EXPORTRESULTSREQUEST._serialized_start=3078
  _EXPORTRESULTSREQUEST._serialized_end=3128
  _GETDATAPOINTSRESPONSE._serialized_start=3130
  _GETDATAPOINTSRESPONSE._serialized_end=3236
  _EXPORTRESULTSRESPONSE._serialized_start=3238
  _EXPORTRESULTSRESPONSE._serialized_end=3313
  _GETTABLEDATAREQUEST._serialized_start=3316
  _GETTABLEDATAREQUEST._serialized_end=3774
  _GETTABLEDATARESPONSE._serialized_start=3776
  _GETTABLEDATARESPONSE._serialized_end=3860
  _LISTREPORTSREQUEST._serialized_start=3862
  _LISTREPORTSREQUEST._serialized_end=3914
  _LISTREPORTSRESPONSE._serialized_start=3916
  _LISTREPORTSRESPONSE._serialized_end=3989
  _CREATEREPORTREQUEST._serialized_start=3992
  _CREATEREPORTREQUEST._serialized_end=4446
  _UPDATEREPORTREQUEST._serialized_start=4449
  _UPDATEREPORTREQUEST._serialized_end=4797
  _PAUSEREPORTREQUEST._serialized_start=4799
  _PAUSEREPORTREQUEST._serialized_end=4867
  _RESTARTREPORTREQUEST._serialized_start=4869
  _RESTARTREPORTREQUEST._serialized_end=4939
  _CANCELREPORTREQUEST._serialized_start=4941
  _CANCELREPORTREQUEST._serialized_end=5010
  _GETDEVICEHEATMAPREQUEST._serialized_start=5013
  _GETDEVICEHEATMAPREQUEST._serialized_end=5196
  _LISTDASHBOARDRESPONSE._serialized_start=5198
  _LISTDASHBOARDRESPONSE._serialized_end=5279
  _GETDASHBOARDREQUEST._serialized_start=5281
  _GETDASHBOARDREQUEST._serialized_end=5321
  _GETMOBILEDATAREQUEST._serialized_start=5324
  _GETMOBILEDATAREQUEST._serialized_end=5474
  _GETMOBILEDATARESPONSE._serialized_start=5476
  _GETMOBILEDATARESPONSE._serialized_end=5569
  _MOBILEDATA._serialized_start=5571
  _MOBILEDATA._serialized_end=5613
  _GETREPORTFIELDSREQUEST._serialized_start=5615
  _GETREPORTFIELDSREQUEST._serialized_end=5688
  _REPORTFIELDS._serialized_start=5690
  _REPORTFIELDS._serialized_end=5720
  _QUERYSERVICE._serialized_start=5723
  _QUERYSERVICE._serialized_end=9269
# @@protoc_insertion_point(module_scope)
