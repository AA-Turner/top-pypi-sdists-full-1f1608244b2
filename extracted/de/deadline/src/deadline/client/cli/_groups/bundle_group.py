# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

"""
All the `deadline bundle` commands.
"""

from __future__ import annotations

import json
import logging
import re
from typing import Any, Optional

import click
from botocore.exceptions import ClientError

from deadline.client import api
from deadline.client.config import config_file, get_setting, set_setting
from deadline.job_attachments.exceptions import (
    AssetSyncError,
    AssetSyncCancelledError,
    MisconfiguredInputsError,
)
from deadline.job_attachments.models import AssetUploadGroup, JobAttachmentsFileSystem
from deadline.job_attachments._utils import _human_readable_file_size

from ...exceptions import DeadlineOperationError, CreateJobWaiterCanceled
from .._common import _apply_cli_options_to_config, _handle_error, _ProgressBarCallbackManager
from ._sigint_handler import SigIntHandler

logger = logging.getLogger(__name__)

# Set up the signal handler for handling Ctrl + C interruptions.
sigint_handler = SigIntHandler()


@click.group(name="bundle")
@_handle_error
def cli_bundle():
    """
    Commands to work with Open Job Description job bundles.
    """


# Latin alphanumeric, starting with a letter
_openjd_identifier_regex = r"(?-m:^[A-Za-z_][A-Za-z0-9_]*\Z)"


def validate_parameters(ctx, param, value):
    """
    Validate provided --parameter values, ensuring that they are in the format "ParamName=Value", and convert them to a dict with the
    following format:
        [{"name": "<name>", "value": "<value>"}, ...]
    """
    parameters_split = []
    for parameter in value:
        regex_match = re.match("([^=]+)=(.*)", parameter)
        if not regex_match:
            raise click.BadParameter(
                f'Parameters must be provided in the format "ParamName=Value". Invalid parameter: {parameter}'
            )

        if not re.match(_openjd_identifier_regex, regex_match[1]):
            raise click.BadParameter(
                f"Parameter names must be alphanumeric Open Job Description identifiers. Invalid parameter name: {regex_match[1]}"
            )

        parameters_split.append({"name": regex_match[1], "value": regex_match[2]})

    return parameters_split


@cli_bundle.command(name="submit")
@click.option(
    "-p",
    "--parameter",
    multiple=True,
    callback=validate_parameters,
    help='The values for the job template\'s parameters. Can be provided as key-value pairs, inline JSON strings, or as paths to a JSON or YAML document. If provided more than once, the values are combined in the order that they appear. Examples: --parameter MyParam=5 -p file://parameter_file.json -p \'{"MyParam": "5"}\'',
)
@click.option("--profile", help="The AWS profile to use.")
@click.option("--farm-id", help="The farm to use.")
@click.option("--queue-id", help="The queue to use.")
@click.option("--storage-profile-id", help="The storage profile to use.")
@click.option("--name", help="The job name to use in place of the one in the job bundle.")
@click.option(
    "--priority",
    type=int,
    default=50,
    help="The priority of the job. Jobs with a higher priority run first.",
)
@click.option(
    "--max-failed-tasks-count",
    type=int,
    help="The maximum number of failed tasks before the job is marked as failed.",
)
@click.option(
    "--max-retries-per-task",
    type=int,
    help="The maximum number of times to retry a task before it is marked as failed.",
)
@click.option(
    "--max-worker-count",
    type=int,
    help="The max worker count of the job.",
)
@click.option(
    "--job-attachments-file-system",
    help="The method workers use to access job attachments. "
    "COPIED means to copy files to the worker and VIRTUAL means to load "
    "files as needed from a virtual file system. If VIRTUAL is selected "
    "but not supported by a worker, it will fallback to COPIED.",
    type=click.Choice([e.value for e in JobAttachmentsFileSystem]),
)
@click.option(
    "--yes",
    is_flag=True,
    help="Skip any confirmation prompts",
)
@click.option(
    "--require-paths-exist",
    is_flag=True,
    help="Return an error if any input files are missing.",
)
@click.option(
    "--submitter-name",
    type=click.STRING,
    help="Name of the application submitting the bundle.",
)
@click.argument("job_bundle_dir")
@_handle_error
def bundle_submit(
    job_bundle_dir,
    job_attachments_file_system,
    parameter,
    yes,
    name,
    priority,
    max_failed_tasks_count,
    max_retries_per_task,
    max_worker_count,
    require_paths_exist,
    submitter_name,
    **args,
):
    """
    Submits an Open Job Description job bundle.
    """
    # Apply the CLI args to the config
    config = _apply_cli_options_to_config(required_options={"farm_id", "queue_id"}, **args)

    hash_callback_manager = _ProgressBarCallbackManager(length=100, label="Hashing Attachments")
    upload_callback_manager = _ProgressBarCallbackManager(length=100, label="Uploading Attachments")

    def _check_create_job_wait_canceled() -> bool:
        return sigint_handler.continue_operation

    def _decide_cancel_submission(upload_group: AssetUploadGroup) -> bool:
        """
        Callback to decide if submission should be cancelled or not. Return 'True' to cancel.
        Prints a warning that requires confirmation if paths are found outside of configured storage profile locations.
        """
        warning_message = ""
        for group in upload_group.asset_groups:
            if not group.file_system_location_name:
                warning_message += f"\n\nUnder the directory '{group.root_path}':"
                warning_message += (
                    f"\n\t{len(group.inputs)} input file{'' if len(group.inputs) == 1 else 's'}"
                    if len(group.inputs) > 0
                    else ""
                )
                warning_message += (
                    f"\n\t{len(group.outputs)} output director{'y' if len(group.outputs) == 1 else 'ies'}"
                    if len(group.outputs) > 0
                    else ""
                )
                warning_message += (
                    f"\n\t{len(group.references)} referenced file{'' if len(group.references) == 1 else 's'} and/or director{'y' if len(group.outputs) == 1 else 'ies'}"
                    if len(group.references) > 0
                    else ""
                )

        # Exit early if there are no warnings and we've either set auto accept or there's no files to confirm
        if not warning_message and (
            yes
            or config_file.str2bool(get_setting("settings.auto_accept", config=config))
            or upload_group.total_input_files == 0
        ):
            return False

        message_text = (
            f"Job submission contains {upload_group.total_input_files} input files totaling {_human_readable_file_size(upload_group.total_input_bytes)}. "
            " All input files will be uploaded to S3 if they are not already present in the job attachments bucket."
        )
        if warning_message:
            message_text += (
                f"\n\nFiles were specified outside of the configured storage profile location(s). "
                " Please confirm that you intend to submit a job that uses files from the following directories:"
                f"{warning_message}\n\n"
                "To permanently remove this warning you must only use files located within a storage profile location."
            )
        message_text += "\n\nDo you wish to proceed?"
        return not click.confirm(
            message_text,
            default=not warning_message,
        )

    try:
        job_id = api.create_job_from_job_bundle(
            job_bundle_dir=job_bundle_dir,
            job_parameters=parameter,
            name=name,
            job_attachments_file_system=job_attachments_file_system,
            config=config,
            priority=priority,
            max_failed_tasks_count=max_failed_tasks_count,
            max_retries_per_task=max_retries_per_task,
            max_worker_count=max_worker_count,
            hashing_progress_callback=hash_callback_manager.callback,
            upload_progress_callback=upload_callback_manager.callback,
            create_job_result_callback=_check_create_job_wait_canceled,
            print_function_callback=click.echo,
            decide_cancel_submission_callback=_decide_cancel_submission,
            require_paths_exist=require_paths_exist,
            submitter_name=submitter_name,
        )

        # Check Whether the CLI options are modifying any of the default settings that affect
        # the job id. If not, we'll save the job id submitted as the default job id.
        # If the submission is canceled by the user job_id will be None, so ignore this case as well.
        if (
            job_id is not None
            and args.get("profile") is None
            and args.get("farm_id") is None
            and args.get("queue_id") is None
            and args.get("storage_profile_id") is None
        ):
            set_setting("defaults.job_id", job_id)

    except AssetSyncCancelledError as exc:
        if sigint_handler.continue_operation:
            raise DeadlineOperationError(f"Job submission unexpectedly canceled:\n{exc}") from exc
        else:
            click.echo("Job submission canceled.")
            return
    except AssetSyncError as exc:
        raise DeadlineOperationError(f"Failed to upload job attachments:\n{exc}") from exc
    except CreateJobWaiterCanceled as exc:
        if sigint_handler.continue_operation:
            raise DeadlineOperationError(
                f"Unexpectedly canceled during wait for final status of CreateJob:\n{exc}"
            ) from exc
        else:
            click.echo("Canceled waiting for final status of CreateJob.")
            return
    except ClientError as exc:
        raise DeadlineOperationError(
            f"Failed to submit the job bundle to AWS Deadline Cloud:\n{exc}"
        ) from exc
    except MisconfiguredInputsError as exc:
        click.echo(str(exc))
        click.echo("Job submission canceled.")
        return
    except Exception as exc:
        api.get_deadline_cloud_library_telemetry_client().record_error(
            event_details={"exception_scope": "on_submit"},
            exception_type=str(type(exc)),
        )
        raise


@cli_bundle.command(name="gui-submit")
@click.argument("job_bundle_dir", required=False)
@click.option(
    "--browse",
    is_flag=True,
    help="Opens a folder browser to select a bundle.",
)
@click.option(
    "--install-gui",
    is_flag=True,
    help="Installs GUI dependencies if they are not installed already",
)
@click.option(
    "--submitter-name",
    type=click.STRING,
    help="Name of the application submitting the bundle. If a name is specified, the GUI will automatically close after submitting the job.",
)
@click.option(
    "--output",
    type=click.Choice(
        ["verbose", "json"],
        case_sensitive=False,
    ),
    default="verbose",
    help="Specifies the output format of the messages printed to stdout.\n"
    "VERBOSE: Displays messages in a human-readable text format.\n"
    "JSON: Displays messages in JSON line format, so that the info can be easily "
    "parsed/consumed by custom scripts.",
)
@_handle_error
def bundle_gui_submit(job_bundle_dir, browse, output, install_gui, submitter_name, **args):
    """
    Opens a GUI to submit an Open Job Description job bundle.
    """
    from ...ui import gui_context_for_cli

    with gui_context_for_cli(automatically_install_dependencies=install_gui) as app:
        from ...ui.job_bundle_submitter import show_job_bundle_submitter

        if not job_bundle_dir and not browse:
            raise DeadlineOperationError(
                "Specify a job bundle directory or run the bundle command with the --browse flag"
            )
        output = output.lower()

        submitter = show_job_bundle_submitter(
            input_job_bundle_dir=job_bundle_dir, browse=browse, submitter_name=submitter_name
        )

        if not submitter:
            return

        submitter.show()

        app.exec()

        response = None
        if submitter:
            response = submitter.create_job_response

        _print_response(
            output=output,
            submitted=True if response else False,
            job_bundle_dir=job_bundle_dir,
            job_history_bundle_dir=submitter.job_history_bundle_dir,
            job_id=response["jobId"] if response else None,
        )


def _print_response(
    output: str,
    submitted: bool,
    job_bundle_dir: str,
    job_history_bundle_dir: Optional[str],
    job_id: Optional[str],
):
    if output == "json":
        if submitted:
            response: dict[str, Any] = {
                "status": "SUBMITTED",
                "jobId": job_id,
                "jobHistoryBundleDirectory": job_history_bundle_dir,
            }
            click.echo(json.dumps(response))
        else:
            click.echo(json.dumps({"status": "CANCELED"}))
    else:
        if submitted:
            click.echo("Submitted job bundle:")
            click.echo(f"   {job_bundle_dir}")
            click.echo(f"Job ID: {job_id}")
        else:
            click.echo("Job submission canceled.")
