"""
Main interface for gamelift service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gamelift/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_gamelift import (
        Client,
        DescribeFleetAttributesPaginator,
        DescribeFleetCapacityPaginator,
        DescribeFleetEventsPaginator,
        DescribeFleetUtilizationPaginator,
        DescribeGameServerInstancesPaginator,
        DescribeGameSessionDetailsPaginator,
        DescribeGameSessionQueuesPaginator,
        DescribeGameSessionsPaginator,
        DescribeInstancesPaginator,
        DescribeMatchmakingConfigurationsPaginator,
        DescribeMatchmakingRuleSetsPaginator,
        DescribePlayerSessionsPaginator,
        DescribeScalingPoliciesPaginator,
        GameLiftClient,
        ListAliasesPaginator,
        ListBuildsPaginator,
        ListComputePaginator,
        ListContainerFleetsPaginator,
        ListContainerGroupDefinitionVersionsPaginator,
        ListContainerGroupDefinitionsPaginator,
        ListFleetDeploymentsPaginator,
        ListFleetsPaginator,
        ListGameServerGroupsPaginator,
        ListGameServersPaginator,
        ListLocationsPaginator,
        ListScriptsPaginator,
        SearchGameSessionsPaginator,
    )

    session = Session()
    client: GameLiftClient = session.client("gamelift")

    describe_fleet_attributes_paginator: DescribeFleetAttributesPaginator = client.get_paginator("describe_fleet_attributes")
    describe_fleet_capacity_paginator: DescribeFleetCapacityPaginator = client.get_paginator("describe_fleet_capacity")
    describe_fleet_events_paginator: DescribeFleetEventsPaginator = client.get_paginator("describe_fleet_events")
    describe_fleet_utilization_paginator: DescribeFleetUtilizationPaginator = client.get_paginator("describe_fleet_utilization")
    describe_game_server_instances_paginator: DescribeGameServerInstancesPaginator = client.get_paginator("describe_game_server_instances")
    describe_game_session_details_paginator: DescribeGameSessionDetailsPaginator = client.get_paginator("describe_game_session_details")
    describe_game_session_queues_paginator: DescribeGameSessionQueuesPaginator = client.get_paginator("describe_game_session_queues")
    describe_game_sessions_paginator: DescribeGameSessionsPaginator = client.get_paginator("describe_game_sessions")
    describe_instances_paginator: DescribeInstancesPaginator = client.get_paginator("describe_instances")
    describe_matchmaking_configurations_paginator: DescribeMatchmakingConfigurationsPaginator = client.get_paginator("describe_matchmaking_configurations")
    describe_matchmaking_rule_sets_paginator: DescribeMatchmakingRuleSetsPaginator = client.get_paginator("describe_matchmaking_rule_sets")
    describe_player_sessions_paginator: DescribePlayerSessionsPaginator = client.get_paginator("describe_player_sessions")
    describe_scaling_policies_paginator: DescribeScalingPoliciesPaginator = client.get_paginator("describe_scaling_policies")
    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_builds_paginator: ListBuildsPaginator = client.get_paginator("list_builds")
    list_compute_paginator: ListComputePaginator = client.get_paginator("list_compute")
    list_container_fleets_paginator: ListContainerFleetsPaginator = client.get_paginator("list_container_fleets")
    list_container_group_definition_versions_paginator: ListContainerGroupDefinitionVersionsPaginator = client.get_paginator("list_container_group_definition_versions")
    list_container_group_definitions_paginator: ListContainerGroupDefinitionsPaginator = client.get_paginator("list_container_group_definitions")
    list_fleet_deployments_paginator: ListFleetDeploymentsPaginator = client.get_paginator("list_fleet_deployments")
    list_fleets_paginator: ListFleetsPaginator = client.get_paginator("list_fleets")
    list_game_server_groups_paginator: ListGameServerGroupsPaginator = client.get_paginator("list_game_server_groups")
    list_game_servers_paginator: ListGameServersPaginator = client.get_paginator("list_game_servers")
    list_locations_paginator: ListLocationsPaginator = client.get_paginator("list_locations")
    list_scripts_paginator: ListScriptsPaginator = client.get_paginator("list_scripts")
    search_game_sessions_paginator: SearchGameSessionsPaginator = client.get_paginator("search_game_sessions")
    ```
"""

from .client import GameLiftClient
from .paginator import (
    DescribeFleetAttributesPaginator,
    DescribeFleetCapacityPaginator,
    DescribeFleetEventsPaginator,
    DescribeFleetUtilizationPaginator,
    DescribeGameServerInstancesPaginator,
    DescribeGameSessionDetailsPaginator,
    DescribeGameSessionQueuesPaginator,
    DescribeGameSessionsPaginator,
    DescribeInstancesPaginator,
    DescribeMatchmakingConfigurationsPaginator,
    DescribeMatchmakingRuleSetsPaginator,
    DescribePlayerSessionsPaginator,
    DescribeScalingPoliciesPaginator,
    ListAliasesPaginator,
    ListBuildsPaginator,
    ListComputePaginator,
    ListContainerFleetsPaginator,
    ListContainerGroupDefinitionsPaginator,
    ListContainerGroupDefinitionVersionsPaginator,
    ListFleetDeploymentsPaginator,
    ListFleetsPaginator,
    ListGameServerGroupsPaginator,
    ListGameServersPaginator,
    ListLocationsPaginator,
    ListScriptsPaginator,
    SearchGameSessionsPaginator,
)

Client = GameLiftClient


__all__ = (
    "Client",
    "DescribeFleetAttributesPaginator",
    "DescribeFleetCapacityPaginator",
    "DescribeFleetEventsPaginator",
    "DescribeFleetUtilizationPaginator",
    "DescribeGameServerInstancesPaginator",
    "DescribeGameSessionDetailsPaginator",
    "DescribeGameSessionQueuesPaginator",
    "DescribeGameSessionsPaginator",
    "DescribeInstancesPaginator",
    "DescribeMatchmakingConfigurationsPaginator",
    "DescribeMatchmakingRuleSetsPaginator",
    "DescribePlayerSessionsPaginator",
    "DescribeScalingPoliciesPaginator",
    "GameLiftClient",
    "ListAliasesPaginator",
    "ListBuildsPaginator",
    "ListComputePaginator",
    "ListContainerFleetsPaginator",
    "ListContainerGroupDefinitionVersionsPaginator",
    "ListContainerGroupDefinitionsPaginator",
    "ListFleetDeploymentsPaginator",
    "ListFleetsPaginator",
    "ListGameServerGroupsPaginator",
    "ListGameServersPaginator",
    "ListLocationsPaginator",
    "ListScriptsPaginator",
    "SearchGameSessionsPaginator",
)
