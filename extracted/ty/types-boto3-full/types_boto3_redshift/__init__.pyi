"""
Main interface for redshift service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_redshift/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from types_boto3_redshift import (
        Client,
        ClusterAvailableWaiter,
        ClusterDeletedWaiter,
        ClusterRestoredWaiter,
        DescribeClusterDbRevisionsPaginator,
        DescribeClusterParameterGroupsPaginator,
        DescribeClusterParametersPaginator,
        DescribeClusterSecurityGroupsPaginator,
        DescribeClusterSnapshotsPaginator,
        DescribeClusterSubnetGroupsPaginator,
        DescribeClusterTracksPaginator,
        DescribeClusterVersionsPaginator,
        DescribeClustersPaginator,
        DescribeCustomDomainAssociationsPaginator,
        DescribeDataSharesForConsumerPaginator,
        DescribeDataSharesForProducerPaginator,
        DescribeDataSharesPaginator,
        DescribeDefaultClusterParametersPaginator,
        DescribeEndpointAccessPaginator,
        DescribeEndpointAuthorizationPaginator,
        DescribeEventSubscriptionsPaginator,
        DescribeEventsPaginator,
        DescribeHsmClientCertificatesPaginator,
        DescribeHsmConfigurationsPaginator,
        DescribeInboundIntegrationsPaginator,
        DescribeIntegrationsPaginator,
        DescribeNodeConfigurationOptionsPaginator,
        DescribeOrderableClusterOptionsPaginator,
        DescribeRedshiftIdcApplicationsPaginator,
        DescribeReservedNodeExchangeStatusPaginator,
        DescribeReservedNodeOfferingsPaginator,
        DescribeReservedNodesPaginator,
        DescribeScheduledActionsPaginator,
        DescribeSnapshotCopyGrantsPaginator,
        DescribeSnapshotSchedulesPaginator,
        DescribeTableRestoreStatusPaginator,
        DescribeTagsPaginator,
        DescribeUsageLimitsPaginator,
        GetReservedNodeExchangeConfigurationOptionsPaginator,
        GetReservedNodeExchangeOfferingsPaginator,
        ListRecommendationsPaginator,
        RedshiftClient,
        SnapshotAvailableWaiter,
    )

    session = Session()
    client: RedshiftClient = session.client("redshift")

    cluster_available_waiter: ClusterAvailableWaiter = client.get_waiter("cluster_available")
    cluster_deleted_waiter: ClusterDeletedWaiter = client.get_waiter("cluster_deleted")
    cluster_restored_waiter: ClusterRestoredWaiter = client.get_waiter("cluster_restored")
    snapshot_available_waiter: SnapshotAvailableWaiter = client.get_waiter("snapshot_available")

    describe_cluster_db_revisions_paginator: DescribeClusterDbRevisionsPaginator = client.get_paginator("describe_cluster_db_revisions")
    describe_cluster_parameter_groups_paginator: DescribeClusterParameterGroupsPaginator = client.get_paginator("describe_cluster_parameter_groups")
    describe_cluster_parameters_paginator: DescribeClusterParametersPaginator = client.get_paginator("describe_cluster_parameters")
    describe_cluster_security_groups_paginator: DescribeClusterSecurityGroupsPaginator = client.get_paginator("describe_cluster_security_groups")
    describe_cluster_snapshots_paginator: DescribeClusterSnapshotsPaginator = client.get_paginator("describe_cluster_snapshots")
    describe_cluster_subnet_groups_paginator: DescribeClusterSubnetGroupsPaginator = client.get_paginator("describe_cluster_subnet_groups")
    describe_cluster_tracks_paginator: DescribeClusterTracksPaginator = client.get_paginator("describe_cluster_tracks")
    describe_cluster_versions_paginator: DescribeClusterVersionsPaginator = client.get_paginator("describe_cluster_versions")
    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    describe_custom_domain_associations_paginator: DescribeCustomDomainAssociationsPaginator = client.get_paginator("describe_custom_domain_associations")
    describe_data_shares_for_consumer_paginator: DescribeDataSharesForConsumerPaginator = client.get_paginator("describe_data_shares_for_consumer")
    describe_data_shares_for_producer_paginator: DescribeDataSharesForProducerPaginator = client.get_paginator("describe_data_shares_for_producer")
    describe_data_shares_paginator: DescribeDataSharesPaginator = client.get_paginator("describe_data_shares")
    describe_default_cluster_parameters_paginator: DescribeDefaultClusterParametersPaginator = client.get_paginator("describe_default_cluster_parameters")
    describe_endpoint_access_paginator: DescribeEndpointAccessPaginator = client.get_paginator("describe_endpoint_access")
    describe_endpoint_authorization_paginator: DescribeEndpointAuthorizationPaginator = client.get_paginator("describe_endpoint_authorization")
    describe_event_subscriptions_paginator: DescribeEventSubscriptionsPaginator = client.get_paginator("describe_event_subscriptions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_hsm_client_certificates_paginator: DescribeHsmClientCertificatesPaginator = client.get_paginator("describe_hsm_client_certificates")
    describe_hsm_configurations_paginator: DescribeHsmConfigurationsPaginator = client.get_paginator("describe_hsm_configurations")
    describe_inbound_integrations_paginator: DescribeInboundIntegrationsPaginator = client.get_paginator("describe_inbound_integrations")
    describe_integrations_paginator: DescribeIntegrationsPaginator = client.get_paginator("describe_integrations")
    describe_node_configuration_options_paginator: DescribeNodeConfigurationOptionsPaginator = client.get_paginator("describe_node_configuration_options")
    describe_orderable_cluster_options_paginator: DescribeOrderableClusterOptionsPaginator = client.get_paginator("describe_orderable_cluster_options")
    describe_redshift_idc_applications_paginator: DescribeRedshiftIdcApplicationsPaginator = client.get_paginator("describe_redshift_idc_applications")
    describe_reserved_node_exchange_status_paginator: DescribeReservedNodeExchangeStatusPaginator = client.get_paginator("describe_reserved_node_exchange_status")
    describe_reserved_node_offerings_paginator: DescribeReservedNodeOfferingsPaginator = client.get_paginator("describe_reserved_node_offerings")
    describe_reserved_nodes_paginator: DescribeReservedNodesPaginator = client.get_paginator("describe_reserved_nodes")
    describe_scheduled_actions_paginator: DescribeScheduledActionsPaginator = client.get_paginator("describe_scheduled_actions")
    describe_snapshot_copy_grants_paginator: DescribeSnapshotCopyGrantsPaginator = client.get_paginator("describe_snapshot_copy_grants")
    describe_snapshot_schedules_paginator: DescribeSnapshotSchedulesPaginator = client.get_paginator("describe_snapshot_schedules")
    describe_table_restore_status_paginator: DescribeTableRestoreStatusPaginator = client.get_paginator("describe_table_restore_status")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    describe_usage_limits_paginator: DescribeUsageLimitsPaginator = client.get_paginator("describe_usage_limits")
    get_reserved_node_exchange_configuration_options_paginator: GetReservedNodeExchangeConfigurationOptionsPaginator = client.get_paginator("get_reserved_node_exchange_configuration_options")
    get_reserved_node_exchange_offerings_paginator: GetReservedNodeExchangeOfferingsPaginator = client.get_paginator("get_reserved_node_exchange_offerings")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    ```
"""

from .client import RedshiftClient
from .paginator import (
    DescribeClusterDbRevisionsPaginator,
    DescribeClusterParameterGroupsPaginator,
    DescribeClusterParametersPaginator,
    DescribeClusterSecurityGroupsPaginator,
    DescribeClusterSnapshotsPaginator,
    DescribeClustersPaginator,
    DescribeClusterSubnetGroupsPaginator,
    DescribeClusterTracksPaginator,
    DescribeClusterVersionsPaginator,
    DescribeCustomDomainAssociationsPaginator,
    DescribeDataSharesForConsumerPaginator,
    DescribeDataSharesForProducerPaginator,
    DescribeDataSharesPaginator,
    DescribeDefaultClusterParametersPaginator,
    DescribeEndpointAccessPaginator,
    DescribeEndpointAuthorizationPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeHsmClientCertificatesPaginator,
    DescribeHsmConfigurationsPaginator,
    DescribeInboundIntegrationsPaginator,
    DescribeIntegrationsPaginator,
    DescribeNodeConfigurationOptionsPaginator,
    DescribeOrderableClusterOptionsPaginator,
    DescribeRedshiftIdcApplicationsPaginator,
    DescribeReservedNodeExchangeStatusPaginator,
    DescribeReservedNodeOfferingsPaginator,
    DescribeReservedNodesPaginator,
    DescribeScheduledActionsPaginator,
    DescribeSnapshotCopyGrantsPaginator,
    DescribeSnapshotSchedulesPaginator,
    DescribeTableRestoreStatusPaginator,
    DescribeTagsPaginator,
    DescribeUsageLimitsPaginator,
    GetReservedNodeExchangeConfigurationOptionsPaginator,
    GetReservedNodeExchangeOfferingsPaginator,
    ListRecommendationsPaginator,
)
from .waiter import (
    ClusterAvailableWaiter,
    ClusterDeletedWaiter,
    ClusterRestoredWaiter,
    SnapshotAvailableWaiter,
)

Client = RedshiftClient

__all__ = (
    "Client",
    "ClusterAvailableWaiter",
    "ClusterDeletedWaiter",
    "ClusterRestoredWaiter",
    "DescribeClusterDbRevisionsPaginator",
    "DescribeClusterParameterGroupsPaginator",
    "DescribeClusterParametersPaginator",
    "DescribeClusterSecurityGroupsPaginator",
    "DescribeClusterSnapshotsPaginator",
    "DescribeClusterSubnetGroupsPaginator",
    "DescribeClusterTracksPaginator",
    "DescribeClusterVersionsPaginator",
    "DescribeClustersPaginator",
    "DescribeCustomDomainAssociationsPaginator",
    "DescribeDataSharesForConsumerPaginator",
    "DescribeDataSharesForProducerPaginator",
    "DescribeDataSharesPaginator",
    "DescribeDefaultClusterParametersPaginator",
    "DescribeEndpointAccessPaginator",
    "DescribeEndpointAuthorizationPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeHsmClientCertificatesPaginator",
    "DescribeHsmConfigurationsPaginator",
    "DescribeInboundIntegrationsPaginator",
    "DescribeIntegrationsPaginator",
    "DescribeNodeConfigurationOptionsPaginator",
    "DescribeOrderableClusterOptionsPaginator",
    "DescribeRedshiftIdcApplicationsPaginator",
    "DescribeReservedNodeExchangeStatusPaginator",
    "DescribeReservedNodeOfferingsPaginator",
    "DescribeReservedNodesPaginator",
    "DescribeScheduledActionsPaginator",
    "DescribeSnapshotCopyGrantsPaginator",
    "DescribeSnapshotSchedulesPaginator",
    "DescribeTableRestoreStatusPaginator",
    "DescribeTagsPaginator",
    "DescribeUsageLimitsPaginator",
    "GetReservedNodeExchangeConfigurationOptionsPaginator",
    "GetReservedNodeExchangeOfferingsPaginator",
    "ListRecommendationsPaginator",
    "RedshiftClient",
    "SnapshotAvailableWaiter",
)
