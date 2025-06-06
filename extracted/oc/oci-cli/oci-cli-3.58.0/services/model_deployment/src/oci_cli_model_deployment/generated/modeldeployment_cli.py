# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240424

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('model_deployment.model_deployment_root_group.command_name', 'model-deployment'), cls=CommandGroupWithAlias, help=cli_util.override('model_deployment.model_deployment_root_group.help', """Model deployments are a managed resource in the OCI Data Science service to use to deploy machine learning models as HTTP endpoints in OCI. Deploying machine learning models as web applications (HTTP API endpoints) serving predictions in real time is the most common way that models are productionized. HTTP endpoints are flexible and can serve requests for model predictions.

For more information, see [Model Deployments]"""), short_help=cli_util.override('model_deployment.model_deployment_root_group.short_help', """Model Deployment Data Plane API"""))
@cli_util.help_option_group
def model_deployment_root_group():
    pass


@click.command(cli_util.override('model_deployment.inference_result_group.command_name', 'inference-result'), cls=CommandGroupWithAlias, help="""A model used in x-related-resource for grouping actions with no returned body.""")
@cli_util.help_option_group
def inference_result_group():
    pass


model_deployment_root_group.add_command(inference_result_group)


@inference_result_group.command(name=cli_util.override('model_deployment.predict.command_name', 'predict'), help=u"""Invoking a model deployment calls the predict endpoint of the model deployment URI. This endpoint takes sample data as input and is processed using the predict() function in score.py model artifact file \n[Command Reference](predict)""")
@cli_util.option('--model-deployment-id', required=True, help=u"""The [OCID] of the model deployment.""")
@cli_util.option('--request-body', required=True, help=u"""Input data details for making a prediction call""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def predict(ctx, from_json, model_deployment_id, request_body):

    if isinstance(model_deployment_id, six.string_types) and len(model_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --model-deployment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('model_deployment', 'model_deployment', ctx)
    result = client.predict(
        model_deployment_id=model_deployment_id,
        request_body=request_body,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@inference_result_group.command(name=cli_util.override('model_deployment.predict_with_response_stream.command_name', 'predict-with-response-stream'), help=u"""Invoking a model deployment calls the predictWithResponseStream endpoint of the model deployment URI to get the streaming result. This endpoint takes sample data as input and is processed using the predict() function in score.py model artifact file \n[Command Reference](predictWithResponseStream)""")
@cli_util.option('--model-deployment-id', required=True, help=u"""The [OCID] of the model deployment.""")
@cli_util.option('--request-body', required=True, help=u"""Input data details for making a prediction call""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def predict_with_response_stream(ctx, from_json, file, model_deployment_id, request_body):

    if isinstance(model_deployment_id, six.string_types) and len(model_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --model-deployment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('model_deployment', 'model_deployment', ctx)
    result = client.predict_with_response_stream(
        model_deployment_id=model_deployment_id,
        request_body=request_body,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()
