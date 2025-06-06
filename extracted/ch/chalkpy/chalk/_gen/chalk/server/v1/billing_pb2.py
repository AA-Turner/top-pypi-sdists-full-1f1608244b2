# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chalk/server/v1/billing.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chalk._gen.chalk.auth.v1 import permissions_pb2 as chalk_dot_auth_dot_v1_dot_permissions__pb2
from chalk._gen.chalk.kubernetes.v1 import nodes_pb2 as chalk_dot_kubernetes_dot_v1_dot_nodes__pb2
from chalk._gen.chalk.kubernetes.v1 import pods_pb2 as chalk_dot_kubernetes_dot_v1_dot_pods__pb2
from chalk._gen.chalk.pubsub.v1 import node_status_pb2 as chalk_dot_pubsub_dot_v1_dot_node__status__pb2
from chalk._gen.chalk.pubsub.v1 import pod_status_pb2 as chalk_dot_pubsub_dot_v1_dot_pod__status__pb2
from chalk._gen.chalk.server.v1 import chart_pb2 as chalk_dot_server_dot_v1_dot_chart__pb2
from chalk._gen.chalk.server.v1 import pod_request_pb2 as chalk_dot_server_dot_v1_dot_pod__request__pb2
from chalk._gen.chalk.usage.v1 import rate_pb2 as chalk_dot_usage_dot_v1_dot_rate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1d\x63halk/server/v1/billing.proto\x12\x0f\x63halk.server.v1\x1a\x1f\x63halk/auth/v1/permissions.proto\x1a\x1f\x63halk/kubernetes/v1/nodes.proto\x1a\x1e\x63halk/kubernetes/v1/pods.proto\x1a!chalk/pubsub/v1/node_status.proto\x1a chalk/pubsub/v1/pod_status.proto\x1a\x1b\x63halk/server/v1/chart.proto\x1a!chalk/server/v1/pod_request.proto\x1a\x19\x63halk/usage/v1/rate.proto"\x88\x02\n\x14GetUsageChartRequest\x12\x1e\n\x08start_ms\x18\x01 \x01(\x03H\x00R\x07startMs\x88\x01\x01\x12\x1a\n\x06\x65nd_ms\x18\x02 \x01(\x03H\x01R\x05\x65ndMs\x88\x01\x01\x12>\n\x06period\x18\x03 \x01(\x0e\x32!.chalk.server.v1.UsageChartPeriodH\x02R\x06period\x88\x01\x01\x12\x44\n\x08grouping\x18\x04 \x01(\x0e\x32#.chalk.server.v1.UsageChartGroupingH\x03R\x08grouping\x88\x01\x01\x42\x0b\n\t_start_msB\t\n\x07_end_msB\t\n\x07_periodB\x0b\n\t_grouping"E\n\x15GetUsageChartResponse\x12,\n\x05\x63hart\x18\x01 \x01(\x0b\x32\x16.chalk.server.v1.ChartR\x05\x63hart"\x1c\n\x1aGetUtilizationRatesRequest"P\n\x1bGetUtilizationRatesResponse\x12\x31\n\x05rates\x18\x01 \x03(\x0b\x32\x1b.chalk.usage.v1.MachineRateR\x05rates"\xd2\x01\n\x16GetNodesAndPodsRequest\x12!\n\tnamespace\x18\x01 \x01(\tH\x00R\tnamespace\x88\x01\x01\x12\x31\n\x12pod_label_selector\x18\x02 \x01(\tH\x01R\x10podLabelSelector\x88\x01\x01\x12*\n\x0e\x65nvironment_id\x18\x03 \x01(\tH\x02R\renvironmentId\x88\x01\x01\x42\x0c\n\n_namespaceB\x15\n\x13_pod_label_selectorB\x11\n\x0f_environment_id"\x88\x01\n\x17GetNodesAndPodsResponse\x12\x37\n\x05nodes\x18\x01 \x03(\x0b\x32!.chalk.pubsub.v1.NodeStatusPubSubR\x05nodes\x12\x34\n\x04pods\x18\x02 \x03(\x0b\x32 .chalk.pubsub.v1.PodStatusPubSubR\x04pods"\xd4\x01\n\x18GetNodesAndPodsUIRequest\x12!\n\tnamespace\x18\x01 \x01(\tH\x00R\tnamespace\x88\x01\x01\x12\x31\n\x12pod_label_selector\x18\x02 \x01(\tH\x01R\x10podLabelSelector\x88\x01\x01\x12*\n\x0e\x65nvironment_id\x18\x03 \x01(\tH\x02R\renvironmentId\x88\x01\x01\x42\x0c\n\n_namespaceB\x15\n\x13_pod_label_selectorB\x11\n\x0f_environment_id"\x96\x01\n\x19GetNodesAndPodsUIResponse\x12=\n\x05nodes\x18\x01 \x03(\x0b\x32\'.chalk.kubernetes.v1.KubernetesNodeDataR\x05nodes\x12:\n\x04pods\x18\x02 \x03(\x0b\x32&.chalk.kubernetes.v1.KubernetesPodDataR\x04pods"\x18\n\x16SyncUtilizationRequest"\x19\n\x17SyncUtilizationResponse*t\n\x10UsageChartPeriod\x12"\n\x1eUSAGE_CHART_PERIOD_UNSPECIFIED\x10\x00\x12\x1c\n\x18USAGE_CHART_PERIOD_DAILY\x10\x01\x12\x1e\n\x1aUSAGE_CHART_PERIOD_MONTHLY\x10\x02*\x84\x01\n\x12UsageChartGrouping\x12$\n USAGE_CHART_GROUPING_UNSPECIFIED\x10\x00\x12&\n"USAGE_CHART_GROUPING_INSTANCE_TYPE\x10\x01\x12 \n\x1cUSAGE_CHART_GROUPING_CLUSTER\x10\x02\x32\xbc\x05\n\x0e\x42illingService\x12r\n\x11GetNodesAndPodsUI\x12).chalk.server.v1.GetNodesAndPodsUIRequest\x1a*.chalk.server.v1.GetNodesAndPodsUIResponse"\x06\x90\x02\x01\x80}\x0b\x12l\n\x0fGetNodesAndPods\x12\'.chalk.server.v1.GetNodesAndPodsRequest\x1a(.chalk.server.v1.GetNodesAndPodsResponse"\x06\x90\x02\x01\x80}\x0b\x12\x66\n\rGetUsageChart\x12%.chalk.server.v1.GetUsageChartRequest\x1a&.chalk.server.v1.GetUsageChartResponse"\x06\x90\x02\x01\x80}\x1c\x12x\n\x13GetUtilizationRates\x12+.chalk.server.v1.GetUtilizationRatesRequest\x1a,.chalk.server.v1.GetUtilizationRatesResponse"\x06\x90\x02\x01\x80}\x01\x12x\n\x13GetPodRequestCharts\x12+.chalk.server.v1.GetPodRequestChartsRequest\x1a,.chalk.server.v1.GetPodRequestChartsResponse"\x06\x90\x02\x01\x80}\x06\x12l\n\x0fSyncUtilization\x12\'.chalk.server.v1.SyncUtilizationRequest\x1a(.chalk.server.v1.SyncUtilizationResponse"\x06\x90\x02\x01\x80}\x1b\x42\x95\x01\n\x13\x63om.chalk.server.v1B\x0c\x42illingProtoP\x01Z\x12server/v1;serverv1\xa2\x02\x03\x43SX\xaa\x02\x0f\x43halk.Server.V1\xca\x02\x0f\x43halk\\Server\\V1\xe2\x02\x1b\x43halk\\Server\\V1\\GPBMetadata\xea\x02\x11\x43halk::Server::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "chalk.server.v1.billing_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\023com.chalk.server.v1B\014BillingProtoP\001Z\022server/v1;serverv1\242\002\003CSX\252\002\017Chalk.Server.V1\312\002\017Chalk\\Server\\V1\342\002\033Chalk\\Server\\V1\\GPBMetadata\352\002\021Chalk::Server::V1"
    _globals["_BILLINGSERVICE"].methods_by_name["GetNodesAndPodsUI"]._options = None
    _globals["_BILLINGSERVICE"].methods_by_name["GetNodesAndPodsUI"]._serialized_options = b"\220\002\001\200}\013"
    _globals["_BILLINGSERVICE"].methods_by_name["GetNodesAndPods"]._options = None
    _globals["_BILLINGSERVICE"].methods_by_name["GetNodesAndPods"]._serialized_options = b"\220\002\001\200}\013"
    _globals["_BILLINGSERVICE"].methods_by_name["GetUsageChart"]._options = None
    _globals["_BILLINGSERVICE"].methods_by_name["GetUsageChart"]._serialized_options = b"\220\002\001\200}\034"
    _globals["_BILLINGSERVICE"].methods_by_name["GetUtilizationRates"]._options = None
    _globals["_BILLINGSERVICE"].methods_by_name["GetUtilizationRates"]._serialized_options = b"\220\002\001\200}\001"
    _globals["_BILLINGSERVICE"].methods_by_name["GetPodRequestCharts"]._options = None
    _globals["_BILLINGSERVICE"].methods_by_name["GetPodRequestCharts"]._serialized_options = b"\220\002\001\200}\006"
    _globals["_BILLINGSERVICE"].methods_by_name["SyncUtilization"]._options = None
    _globals["_BILLINGSERVICE"].methods_by_name["SyncUtilization"]._serialized_options = b"\220\002\001\200}\033"
    _globals["_USAGECHARTPERIOD"]._serialized_start = 1531
    _globals["_USAGECHARTPERIOD"]._serialized_end = 1647
    _globals["_USAGECHARTGROUPING"]._serialized_start = 1650
    _globals["_USAGECHARTGROUPING"]._serialized_end = 1782
    _globals["_GETUSAGECHARTREQUEST"]._serialized_start = 309
    _globals["_GETUSAGECHARTREQUEST"]._serialized_end = 573
    _globals["_GETUSAGECHARTRESPONSE"]._serialized_start = 575
    _globals["_GETUSAGECHARTRESPONSE"]._serialized_end = 644
    _globals["_GETUTILIZATIONRATESREQUEST"]._serialized_start = 646
    _globals["_GETUTILIZATIONRATESREQUEST"]._serialized_end = 674
    _globals["_GETUTILIZATIONRATESRESPONSE"]._serialized_start = 676
    _globals["_GETUTILIZATIONRATESRESPONSE"]._serialized_end = 756
    _globals["_GETNODESANDPODSREQUEST"]._serialized_start = 759
    _globals["_GETNODESANDPODSREQUEST"]._serialized_end = 969
    _globals["_GETNODESANDPODSRESPONSE"]._serialized_start = 972
    _globals["_GETNODESANDPODSRESPONSE"]._serialized_end = 1108
    _globals["_GETNODESANDPODSUIREQUEST"]._serialized_start = 1111
    _globals["_GETNODESANDPODSUIREQUEST"]._serialized_end = 1323
    _globals["_GETNODESANDPODSUIRESPONSE"]._serialized_start = 1326
    _globals["_GETNODESANDPODSUIRESPONSE"]._serialized_end = 1476
    _globals["_SYNCUTILIZATIONREQUEST"]._serialized_start = 1478
    _globals["_SYNCUTILIZATIONREQUEST"]._serialized_end = 1502
    _globals["_SYNCUTILIZATIONRESPONSE"]._serialized_start = 1504
    _globals["_SYNCUTILIZATIONRESPONSE"]._serialized_end = 1529
    _globals["_BILLINGSERVICE"]._serialized_start = 1785
    _globals["_BILLINGSERVICE"]._serialized_end = 2485
# @@protoc_insertion_point(module_scope)
