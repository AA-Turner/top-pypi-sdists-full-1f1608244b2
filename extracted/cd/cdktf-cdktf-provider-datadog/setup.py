import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-datadog",
    "version": "12.0.0",
    "description": "Prebuilt datadog Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-provider-datadog.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-provider-datadog.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_datadog",
        "cdktf_cdktf_provider_datadog._jsii",
        "cdktf_cdktf_provider_datadog.action_connection",
        "cdktf_cdktf_provider_datadog.api_key",
        "cdktf_cdktf_provider_datadog.apm_retention_filter",
        "cdktf_cdktf_provider_datadog.apm_retention_filter_order",
        "cdktf_cdktf_provider_datadog.app_builder_app",
        "cdktf_cdktf_provider_datadog.application_key",
        "cdktf_cdktf_provider_datadog.appsec_waf_custom_rule",
        "cdktf_cdktf_provider_datadog.appsec_waf_exclusion_filter",
        "cdktf_cdktf_provider_datadog.authn_mapping",
        "cdktf_cdktf_provider_datadog.child_organization",
        "cdktf_cdktf_provider_datadog.cloud_configuration_rule",
        "cdktf_cdktf_provider_datadog.cloud_workload_security_agent_rule",
        "cdktf_cdktf_provider_datadog.compliance_custom_framework",
        "cdktf_cdktf_provider_datadog.csm_threats_agent_rule",
        "cdktf_cdktf_provider_datadog.dashboard",
        "cdktf_cdktf_provider_datadog.dashboard_json",
        "cdktf_cdktf_provider_datadog.dashboard_list",
        "cdktf_cdktf_provider_datadog.data_datadog_action_connection",
        "cdktf_cdktf_provider_datadog.data_datadog_api_key",
        "cdktf_cdktf_provider_datadog.data_datadog_apm_retention_filters_order",
        "cdktf_cdktf_provider_datadog.data_datadog_app_builder_app",
        "cdktf_cdktf_provider_datadog.data_datadog_application_key",
        "cdktf_cdktf_provider_datadog.data_datadog_cloud_workload_security_agent_rules",
        "cdktf_cdktf_provider_datadog.data_datadog_csm_threats_agent_rules",
        "cdktf_cdktf_provider_datadog.data_datadog_dashboard",
        "cdktf_cdktf_provider_datadog.data_datadog_dashboard_list",
        "cdktf_cdktf_provider_datadog.data_datadog_hosts",
        "cdktf_cdktf_provider_datadog.data_datadog_integration_aws_available_logs_services",
        "cdktf_cdktf_provider_datadog.data_datadog_integration_aws_available_namespaces",
        "cdktf_cdktf_provider_datadog.data_datadog_integration_aws_logs_services",
        "cdktf_cdktf_provider_datadog.data_datadog_integration_aws_namespace_rules",
        "cdktf_cdktf_provider_datadog.data_datadog_ip_ranges",
        "cdktf_cdktf_provider_datadog.data_datadog_logs_archives_order",
        "cdktf_cdktf_provider_datadog.data_datadog_logs_indexes",
        "cdktf_cdktf_provider_datadog.data_datadog_logs_indexes_order",
        "cdktf_cdktf_provider_datadog.data_datadog_logs_pipelines",
        "cdktf_cdktf_provider_datadog.data_datadog_logs_pipelines_order",
        "cdktf_cdktf_provider_datadog.data_datadog_metric_tags",
        "cdktf_cdktf_provider_datadog.data_datadog_monitor",
        "cdktf_cdktf_provider_datadog.data_datadog_monitor_config_policies",
        "cdktf_cdktf_provider_datadog.data_datadog_monitors",
        "cdktf_cdktf_provider_datadog.data_datadog_permissions",
        "cdktf_cdktf_provider_datadog.data_datadog_powerpack",
        "cdktf_cdktf_provider_datadog.data_datadog_role",
        "cdktf_cdktf_provider_datadog.data_datadog_role_users",
        "cdktf_cdktf_provider_datadog.data_datadog_roles",
        "cdktf_cdktf_provider_datadog.data_datadog_rum_application",
        "cdktf_cdktf_provider_datadog.data_datadog_rum_retention_filters",
        "cdktf_cdktf_provider_datadog.data_datadog_security_monitoring_filters",
        "cdktf_cdktf_provider_datadog.data_datadog_security_monitoring_rules",
        "cdktf_cdktf_provider_datadog.data_datadog_security_monitoring_suppressions",
        "cdktf_cdktf_provider_datadog.data_datadog_sensitive_data_scanner_group_order",
        "cdktf_cdktf_provider_datadog.data_datadog_sensitive_data_scanner_standard_pattern",
        "cdktf_cdktf_provider_datadog.data_datadog_service_account",
        "cdktf_cdktf_provider_datadog.data_datadog_service_level_objective",
        "cdktf_cdktf_provider_datadog.data_datadog_service_level_objectives",
        "cdktf_cdktf_provider_datadog.data_datadog_software_catalog",
        "cdktf_cdktf_provider_datadog.data_datadog_synthetics_global_variable",
        "cdktf_cdktf_provider_datadog.data_datadog_synthetics_locations",
        "cdktf_cdktf_provider_datadog.data_datadog_synthetics_test",
        "cdktf_cdktf_provider_datadog.data_datadog_team",
        "cdktf_cdktf_provider_datadog.data_datadog_team_memberships",
        "cdktf_cdktf_provider_datadog.data_datadog_teams",
        "cdktf_cdktf_provider_datadog.data_datadog_user",
        "cdktf_cdktf_provider_datadog.data_datadog_users",
        "cdktf_cdktf_provider_datadog.data_datadog_workflow_automation",
        "cdktf_cdktf_provider_datadog.domain_allowlist",
        "cdktf_cdktf_provider_datadog.downtime",
        "cdktf_cdktf_provider_datadog.downtime_schedule",
        "cdktf_cdktf_provider_datadog.integration_aws",
        "cdktf_cdktf_provider_datadog.integration_aws_account",
        "cdktf_cdktf_provider_datadog.integration_aws_event_bridge",
        "cdktf_cdktf_provider_datadog.integration_aws_external_id",
        "cdktf_cdktf_provider_datadog.integration_aws_lambda_arn",
        "cdktf_cdktf_provider_datadog.integration_aws_log_collection",
        "cdktf_cdktf_provider_datadog.integration_aws_tag_filter",
        "cdktf_cdktf_provider_datadog.integration_azure",
        "cdktf_cdktf_provider_datadog.integration_cloudflare_account",
        "cdktf_cdktf_provider_datadog.integration_confluent_account",
        "cdktf_cdktf_provider_datadog.integration_confluent_resource",
        "cdktf_cdktf_provider_datadog.integration_fastly_account",
        "cdktf_cdktf_provider_datadog.integration_fastly_service",
        "cdktf_cdktf_provider_datadog.integration_gcp",
        "cdktf_cdktf_provider_datadog.integration_gcp_sts",
        "cdktf_cdktf_provider_datadog.integration_ms_teams_tenant_based_handle",
        "cdktf_cdktf_provider_datadog.integration_ms_teams_workflows_webhook_handle",
        "cdktf_cdktf_provider_datadog.integration_opsgenie_service_object",
        "cdktf_cdktf_provider_datadog.integration_pagerduty",
        "cdktf_cdktf_provider_datadog.integration_pagerduty_service_object",
        "cdktf_cdktf_provider_datadog.integration_slack_channel",
        "cdktf_cdktf_provider_datadog.ip_allowlist",
        "cdktf_cdktf_provider_datadog.logs_archive",
        "cdktf_cdktf_provider_datadog.logs_archive_order",
        "cdktf_cdktf_provider_datadog.logs_custom_destination",
        "cdktf_cdktf_provider_datadog.logs_custom_pipeline",
        "cdktf_cdktf_provider_datadog.logs_index",
        "cdktf_cdktf_provider_datadog.logs_index_order",
        "cdktf_cdktf_provider_datadog.logs_integration_pipeline",
        "cdktf_cdktf_provider_datadog.logs_metric",
        "cdktf_cdktf_provider_datadog.logs_pipeline_order",
        "cdktf_cdktf_provider_datadog.metric_metadata",
        "cdktf_cdktf_provider_datadog.metric_tag_configuration",
        "cdktf_cdktf_provider_datadog.monitor",
        "cdktf_cdktf_provider_datadog.monitor_config_policy",
        "cdktf_cdktf_provider_datadog.monitor_json",
        "cdktf_cdktf_provider_datadog.monitor_notification_rule",
        "cdktf_cdktf_provider_datadog.observability_pipeline",
        "cdktf_cdktf_provider_datadog.on_call_escalation_policy",
        "cdktf_cdktf_provider_datadog.on_call_schedule",
        "cdktf_cdktf_provider_datadog.on_call_team_routing_rules",
        "cdktf_cdktf_provider_datadog.openapi_api",
        "cdktf_cdktf_provider_datadog.organization_settings",
        "cdktf_cdktf_provider_datadog.powerpack",
        "cdktf_cdktf_provider_datadog.provider",
        "cdktf_cdktf_provider_datadog.restriction_policy",
        "cdktf_cdktf_provider_datadog.role",
        "cdktf_cdktf_provider_datadog.rum_application",
        "cdktf_cdktf_provider_datadog.rum_metric",
        "cdktf_cdktf_provider_datadog.rum_retention_filter",
        "cdktf_cdktf_provider_datadog.rum_retention_filters_order",
        "cdktf_cdktf_provider_datadog.security_monitoring_default_rule",
        "cdktf_cdktf_provider_datadog.security_monitoring_filter",
        "cdktf_cdktf_provider_datadog.security_monitoring_rule",
        "cdktf_cdktf_provider_datadog.security_monitoring_rule_json",
        "cdktf_cdktf_provider_datadog.security_monitoring_suppression",
        "cdktf_cdktf_provider_datadog.security_notification_rule",
        "cdktf_cdktf_provider_datadog.sensitive_data_scanner_group",
        "cdktf_cdktf_provider_datadog.sensitive_data_scanner_group_order",
        "cdktf_cdktf_provider_datadog.sensitive_data_scanner_rule",
        "cdktf_cdktf_provider_datadog.service_account",
        "cdktf_cdktf_provider_datadog.service_account_application_key",
        "cdktf_cdktf_provider_datadog.service_definition_yaml",
        "cdktf_cdktf_provider_datadog.service_level_objective",
        "cdktf_cdktf_provider_datadog.slo_correction",
        "cdktf_cdktf_provider_datadog.software_catalog",
        "cdktf_cdktf_provider_datadog.spans_metric",
        "cdktf_cdktf_provider_datadog.synthetics_concurrency_cap",
        "cdktf_cdktf_provider_datadog.synthetics_global_variable",
        "cdktf_cdktf_provider_datadog.synthetics_private_location",
        "cdktf_cdktf_provider_datadog.synthetics_test",
        "cdktf_cdktf_provider_datadog.team",
        "cdktf_cdktf_provider_datadog.team_link",
        "cdktf_cdktf_provider_datadog.team_membership",
        "cdktf_cdktf_provider_datadog.team_permission_setting",
        "cdktf_cdktf_provider_datadog.user",
        "cdktf_cdktf_provider_datadog.user_role",
        "cdktf_cdktf_provider_datadog.webhook",
        "cdktf_cdktf_provider_datadog.webhook_custom_variable",
        "cdktf_cdktf_provider_datadog.workflow_automation"
    ],
    "package_data": {
        "cdktf_cdktf_provider_datadog._jsii": [
            "provider-datadog@12.0.0.jsii.tgz"
        ],
        "cdktf_cdktf_provider_datadog": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.9",
    "install_requires": [
        "cdktf>=0.21.0, <0.22.0",
        "constructs>=10.4.2, <11.0.0",
        "jsii>=1.111.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard>=2.13.3,<4.3.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
