# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Atlan Pte. Ltd.
import time
from datetime import datetime, timedelta, timezone
from typing import Generator

import pytest

from pyatlan import utils
from pyatlan.client.atlan import AtlanClient
from pyatlan.client.workflow import WorkflowClient
from pyatlan.model.assets import Connection
from pyatlan.model.credential import Credential, CredentialResponse
from pyatlan.model.enums import AtlanConnectorType, AtlanWorkflowPhase, WorkflowPackage
from pyatlan.model.packages.snowflake_miner import SnowflakeMiner
from pyatlan.model.workflow import WorkflowResponse, WorkflowSchedule
from tests.integration.client import TestId, delete_asset
from tests.integration.connection_test import create_connection

MODULE_NAME = TestId.make_unique("WorfklowClient")
WORKFLOW_TEMPLATE_REF = "workflowTemplateRef"
WORKFLOW_SCHEDULE_SCHEDULE = "45 4 * * *"
WORKFLOW_SCHEDULE_TIMEZONE = "Asia/Kolkata"
WORKFLOW_SCHEDULE_UPDATED_1 = "45 5 * * *"
WORKFLOW_SCHEDULE_TIMEZONE_UPDATED_1 = "Europe/Paris"
WORKFLOW_SCHEDULE_UPDATED_2 = "45 6 * * *"
WORKFLOW_SCHEDULE_TIMEZONE_UPDATED_2 = "Europe/London"
WORKFLOW_SCHEDULE_UPDATED_3 = "45 7 * * *"
WORKFLOW_SCHEDULE_TIMEZONE_UPDATED_3 = "Europe/Dublin"


@pytest.fixture(scope="module")
def create_credentials(
    client: AtlanClient,
) -> Generator[CredentialResponse, None, None]:
    """Creates a new credential using the Atlan API."""
    credentials_name = f"default-spark-{int(utils.get_epoch_timestamp())}-0"

    credentials = Credential(
        name=credentials_name,
        auth_type="atlan_api_key",
        connector_config_name="atlan-connectors-spark",
        connector="spark",
        username="test-username",
        password="12345",
        connector_type="event",
        host="test-host",
        port=123,
    )

    create_credentials = client.credentials.creator(credentials)
    guid = create_credentials.id
    if guid is None:
        raise ValueError("Failed to retrieve GUID from created credentials.")

    yield create_credentials

    response = delete_credentials(client, guid=guid)
    assert response is None


def delete_credentials(client: AtlanClient, guid: str):
    response = client.credentials.purge_by_guid(guid=guid)
    return response


@pytest.fixture(scope="module")
def connection(client: AtlanClient) -> Generator[Connection, None, None]:
    connection = create_connection(
        client=client, name=MODULE_NAME, connector_type=AtlanConnectorType.SNOWFLAKE
    )
    yield connection
    delete_asset(client, guid=connection.guid, asset_type=Connection)


def delete_workflow(client: AtlanClient, workflow_name: str) -> None:
    client.workflow.delete(workflow_name=workflow_name)


@pytest.fixture(scope="module")
def workflow(
    client: AtlanClient, connection: Connection
) -> Generator[WorkflowResponse, None, None]:
    assert connection and connection.qualified_name
    miner = (
        SnowflakeMiner(connection_qualified_name=connection.qualified_name)
        .s3(
            s3_bucket="test-s3-bucket",
            s3_prefix="test-s3-prefix",
            s3_bucket_region="test-s3-bucket-region",
            sql_query_key="TEST_QUERY",
            default_database_key="TEST_SNOWFLAKE",
            default_schema_key="TEST_SCHEMA",
            session_id_key="TEST_SESSION_ID",
        )
        .popularity_window(days=15)
        .native_lineage(enabled=True)
        .custom_config(config={"test": True, "feature": 1234})
        .to_workflow()
    )
    schedule = WorkflowSchedule(
        cron_schedule=WORKFLOW_SCHEDULE_SCHEDULE, timezone=WORKFLOW_SCHEDULE_TIMEZONE
    )
    workflow = client.workflow.run(miner, workflow_schedule=schedule)
    assert workflow
    # Adding some delay to make sure
    # the workflow run is indexed in ES.
    time.sleep(30)
    yield workflow
    assert workflow.metadata and workflow.metadata.name
    delete_workflow(client, workflow.metadata.name)


def test_workflow_find_by_methods(client: AtlanClient):
    results = client.workflow.find_by_type(
        prefix=WorkflowPackage.SNOWFLAKE, max_results=10
    )
    assert results
    assert len(results) >= 1

    workflow_id = results[0].id
    assert workflow_id
    workflow = client.workflow.find_by_id(id=workflow_id)
    assert workflow
    assert workflow.id and workflow.id == workflow_id

    workflow = client.workflow.find_by_id(id="invalid-id")
    assert workflow is None


def test_workflow_get_runs_and_stop(client: AtlanClient, workflow: WorkflowResponse):
    # Retrieve the lastest workflow run
    assert workflow and workflow.metadata and workflow.metadata.name
    runs = client.workflow.get_runs(
        workflow_name=workflow.metadata.name, workflow_phase=AtlanWorkflowPhase.RUNNING
    )
    assert runs and runs.count == 1
    current_page = runs.current_page()
    assert current_page is not None and len(current_page) == 1
    run = current_page[0]
    assert run and run.id
    assert workflow.metadata.name and (workflow.metadata.name in run.id)

    # Stop the running workflow
    run_response = client.workflow.stop(workflow_run_id=run.id)
    assert run_response
    assert (
        run_response.status and run_response.status.phase == AtlanWorkflowPhase.RUNNING
    )
    assert (
        run_response.status.stored_workflow_template_spec
        and run_response.status.stored_workflow_template_spec.get(
            WORKFLOW_TEMPLATE_REF
        ).get("name")
        == workflow.metadata.name
    )

    # Test workflow monitoring
    workflow_status = client.workflow.monitor(workflow_response=workflow)
    assert workflow_status == AtlanWorkflowPhase.FAILED

    # Test workflow monitoring by providing workflow name directly
    workflow_name = workflow.metadata.name
    workflow_status = client.workflow.monitor(workflow_name=workflow_name)
    assert workflow_status == AtlanWorkflowPhase.FAILED

    # Test find run by id
    workflow_run = client.workflow.find_run_by_id(id=run.id)
    assert (
        workflow_run
        and workflow_run.source
        and workflow_run.source.status
        and workflow_run.source.status.phase == AtlanWorkflowPhase.FAILED
    )

    # Test find run by status and time range
    runs_status = client.workflow.find_runs_by_status_and_time_range(
        [AtlanWorkflowPhase.FAILED], started_at="now-1h"
    )
    assert runs_status
    workflow_run_status = runs_status.current_page()[0]  # type: ignore
    start_time = workflow_run_status.source.status.startedAt  # type: ignore
    start_datetime = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")  # type: ignore
    start_datetime = start_datetime.replace(tzinfo=timezone.utc)
    current_time = datetime.now(timezone.utc)
    time_diff = current_time - start_datetime
    assert (
        workflow_run_status
        and workflow_run_status.source
        and workflow_run_status.source.status
        and workflow_run_status.source.status.phase == AtlanWorkflowPhase.FAILED
        and time_diff < timedelta(hours=1)
    )


def test_workflow_get_all_scheduled_runs(
    client: AtlanClient, workflow: WorkflowResponse
):
    runs = client.workflow.get_all_scheduled_runs()

    assert workflow and workflow.metadata and workflow.metadata.name
    scheduled_workflow_name = f"{workflow.metadata.name}-cron"
    assert runs and len(runs) >= 1

    found = any(
        run.metadata and run.metadata.name == scheduled_workflow_name for run in runs
    )

    if not found:
        pytest.fail(
            f"Unable to find scheduled run for workflow: {workflow.metadata.name}"
        )


def _assert_scheduled_run(client: AtlanClient, workflow: WorkflowResponse):
    assert workflow and workflow.metadata and workflow.metadata.name
    scheduled_workflow = client.workflow.get_scheduled_run(
        workflow_name=workflow.metadata.name
    )
    scheduled_workflow_name = f"{workflow.metadata.name}-cron"
    assert (
        scheduled_workflow
        and scheduled_workflow.metadata
        and scheduled_workflow.metadata.name == scheduled_workflow_name
    )


def test_workflow_get_scheduled_run(client: AtlanClient, workflow: WorkflowResponse):
    _assert_scheduled_run(client, workflow)


def _assert_add_schedule(workflow, scheduled_workflow, schedule, timezone):
    assert scheduled_workflow
    assert scheduled_workflow.metadata
    assert scheduled_workflow.metadata.name == workflow.metadata.name
    assert scheduled_workflow.metadata.annotations
    assert (
        scheduled_workflow.metadata.annotations.get(
            WorkflowClient._WORKFLOW_RUN_SCHEDULE
        )
        == schedule
    )
    assert (
        scheduled_workflow.metadata.annotations.get(
            WorkflowClient._WORKFLOW_RUN_TIMEZONE
        )
        == timezone
    )


def _assert_remove_schedule(response, workflow):
    assert response
    assert response.metadata.annotations
    assert response.metadata.name == workflow.metadata.name
    assert WorkflowClient._WORKFLOW_RUN_TIMEZONE in response.metadata.annotations
    assert WorkflowClient._WORKFLOW_RUN_SCHEDULE not in response.metadata.annotations


def test_workflow_add_remove_schedule(client: AtlanClient, workflow: WorkflowResponse):
    schedule = WorkflowSchedule(
        cron_schedule=WORKFLOW_SCHEDULE_UPDATED_1,
        timezone=WORKFLOW_SCHEDULE_TIMEZONE_UPDATED_1,
    )

    # NOTE: This method will overwrite existing workflow run schedule
    # Try to update schedule again, with `Workflow` object
    scheduled_workflow = client.workflow.add_schedule(
        workflow=workflow, workflow_schedule=schedule
    )

    _assert_add_schedule(
        workflow,
        scheduled_workflow,
        WORKFLOW_SCHEDULE_UPDATED_1,
        WORKFLOW_SCHEDULE_TIMEZONE_UPDATED_1,
    )
    # Make sure scheduled run exists
    _assert_scheduled_run(client, workflow)
    # Now remove the scheduled run
    response = client.workflow.remove_schedule(workflow)
    _assert_remove_schedule(response, workflow)

    # Try to update schedule again, with `WorkflowSearchResult` object
    existing_workflow = client.workflow.find_by_type(
        prefix=WorkflowPackage.SNOWFLAKE_MINER
    )[0]
    assert (
        existing_workflow
        and existing_workflow.source
        and existing_workflow.source.metadata
    )
    assert workflow and workflow.metadata
    assert existing_workflow.source.metadata.name == workflow.metadata.name

    schedule = WorkflowSchedule(
        cron_schedule=WORKFLOW_SCHEDULE_UPDATED_2,
        timezone=WORKFLOW_SCHEDULE_TIMEZONE_UPDATED_2,
    )
    scheduled_workflow = client.workflow.add_schedule(
        workflow=existing_workflow, workflow_schedule=schedule
    )

    _assert_add_schedule(
        workflow,
        scheduled_workflow,
        WORKFLOW_SCHEDULE_UPDATED_2,
        WORKFLOW_SCHEDULE_TIMEZONE_UPDATED_2,
    )
    # Make sure scheduled run exists
    _assert_scheduled_run(client, workflow)
    # Now remove the scheduled run
    response = client.workflow.remove_schedule(workflow)
    _assert_remove_schedule(response, workflow)

    # Try to update schedule again, with `WorkflowPackage` object
    schedule = WorkflowSchedule(
        cron_schedule=WORKFLOW_SCHEDULE_UPDATED_3,
        timezone=WORKFLOW_SCHEDULE_TIMEZONE_UPDATED_3,
    )
    scheduled_workflow = client.workflow.add_schedule(
        workflow=WorkflowPackage.SNOWFLAKE_MINER, workflow_schedule=schedule
    )

    _assert_add_schedule(
        workflow,
        scheduled_workflow,
        WORKFLOW_SCHEDULE_UPDATED_3,
        WORKFLOW_SCHEDULE_TIMEZONE_UPDATED_3,
    )
    # Make sure scheduled run exists
    _assert_scheduled_run(client, workflow)
    # Now remove the scheduled run
    response = client.workflow.remove_schedule(workflow)
    _assert_remove_schedule(response, workflow)


def test_credentials(client: AtlanClient, create_credentials: Credential):
    credentials = create_credentials
    assert credentials
    assert credentials.id
    reterieved_creds = client.credentials.get(guid=credentials.id)
    assert reterieved_creds.auth_type == "atlan_api_key"
    assert reterieved_creds.connector_config_name == "atlan-connectors-spark"
    assert reterieved_creds.connector == "spark"
    assert reterieved_creds.username == "test-username"
    assert create_credentials.connector_type == "event"
    assert create_credentials.host == "test-host"
    assert create_credentials.port == 123
    assert create_credentials.extras is None
    assert create_credentials.level is None
    assert create_credentials.metadata is None


def test_get_all_credentials(client: AtlanClient):
    credentials = client.credentials.get_all()
    assert credentials, "Expected credentials but found None"
    assert credentials.records is not None, "Expected records but found None"
    assert len(credentials.records or []) > 0, (
        "Expected at least one record but found none"
    )


def test_get_all_credentials_with_filter_limit_offset(client: AtlanClient):
    filter_criteria = {"connectorType": "jdbc"}
    limit = 1
    offset = 1
    credentials = client.credentials.get_all(
        filter=filter_criteria, limit=limit, offset=offset
    )
    assert len(credentials.records or []) <= limit, "Exceeded limit in results"
    for cred in credentials.records or []:
        assert cred.connector_type == "jdbc", (
            f"Expected 'jdbc', got {cred.connector_type}"
        )


def test_get_all_credentials_with_multiple_filters(client: AtlanClient):
    filter_criteria = {"connectorType": "jdbc", "isActive": True}

    credentials = client.credentials.get_all(filter=filter_criteria)
    assert credentials, "Expected credentials but found None"
    assert credentials.records is not None, "Expected records but found None"
    assert len(credentials.records or []) > 0, (
        "Expected at least one record but found none"
    )

    for record in credentials.records or []:
        assert record.connector_type == "jdbc", (
            f"Expected 'jdbc', got {record.connector_type}"
        )
        assert record.is_active, f"Expected active record, but got inactive: {record}"


def test_get_all_credentials_with_invalid_filter_key(client: AtlanClient):
    filter_criteria = {"invalidKey": "someValue"}
    try:
        client.credentials.get_all(filter=filter_criteria)
        pytest.fail("Expected an error due to invalid filter key, but none occurred.")
    except Exception as e:
        assert "400" in str(e), f"Expected a 400 error, but got: {e}"


def test_get_all_credentials_with_invalid_filter_value(client: AtlanClient):
    filter_criteria = {"connector_type": 123}

    try:
        client.credentials.get_all(filter=filter_criteria)
        pytest.fail("Expected an error due to invalid filter value, but none occurred.")
    except Exception as e:
        assert "400" in str(e), f"Expected a 400 error, but got: {e}"
