import ast
import functools
import graphlib
import importlib
import os
import re
import sys
from pathlib import Path

import click
import rich
from loguru import logger

from ..cli.config import get_config_value, log_options
from ..cli.decorators import async_command
from ..utils import combined_env
from .load import (WorkflowType, find_unreferenced_workflows, get_entries,
                   load_workflow, make_graph)
from .registry import Registry, set_config_api
from .schedule import CalibrationFailedError
from .schedule import maintain as maintain_workflow
from .schedule import run as run_workflow
from .utils import workflow_template


@logger.catch(reraise=True)
def run_script(script_path, extra_paths=None):
    """Run a script in a new process, inheriting current PYTHONPATH plus any extra paths."""
    import subprocess
    import sys

    # Launch the new process with the modified environment
    proc = subprocess.Popen([sys.executable, script_path],
                            env=combined_env(extra_paths))
    proc.communicate()


@logger.catch(reraise=True)
def check_toplogy(workflow: WorkflowType,
                  code_path: str | Path,
                  veryfy_source_code: bool = True) -> dict:
    graph = {}
    try:
        graphlib.TopologicalSorter(
            make_graph(workflow,
                       graph,
                       code_path,
                       veryfy_source_code=veryfy_source_code)).static_order()
    except graphlib.CycleError as e:
        logger.error(
            f"Workflow {workflow.__workflow_id__} has a circular dependency: {e}"
        )
        raise e
    return graph


def command_option(command_name):
    """命令专属配置装饰器工厂"""

    def decorator(func):

        @click.option(
            '--code',
            '-c',
            default=lambda: get_config_value("code", str, command_name),
            help='The path of the code.')
        @click.option(
            '--data',
            '-d',
            default=lambda: get_config_value("data", str, command_name),
            help='The path of the data.')
        @click.option(
            '--api',
            '-a',
            default=lambda: get_config_value("api", str, command_name),
            help='The modlule name of the api.')
        @click.option(
            '--bootstrap',
            '-b',
            default=lambda: get_config_value("bootstrap", Path, command_name),
            help='The path of the bootstrap.')
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if 'code' in kwargs and kwargs['code'] is not None:
                code = os.path.expanduser(kwargs['code'])
                if code not in sys.path:
                    sys.path.insert(0, code)
            bootstrap = kwargs.pop('bootstrap')
            if bootstrap is not None:
                run_script(bootstrap)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@click.command()
@click.argument('workflow')
@click.option('--code',
              '-c',
              default=lambda: get_config_value("code", str, 'create'),
              help='The path of the code.')
@log_options('create')
def create(workflow, code):
    """
    Create a new workflow file.
    """
    logger.info(f'[CMD]: create {workflow} --code {code}')
    if code is None:
        code = Path.cwd()

    fname = Path(code) / f'{workflow}'
    fname = Path(os.path.expanduser(fname))
    if fname.exists():
        click.echo(f'{workflow} already exists')
        return

    fname.parent.mkdir(parents=True, exist_ok=True)
    deps = find_unreferenced_workflows(code)

    with open(fname, 'w') as f:
        f.write(workflow_template(workflow, list(deps)))
    click.echo(f'{workflow} created')


@click.command()
@click.argument('key')
@click.argument('value', type=str)
@click.option('--api',
              '-a',
              default=lambda: get_config_value("api", str, 'set'),
              help='The modlule name of the api.')
@log_options('set')
def set(key, value, api):
    """
    Set a config.
    """
    logger.info(f'[CMD]: reg set {key} {value} --api {api}')
    reg = Registry()
    if api is not None:
        api = importlib.import_module(api)
        set_config_api(api.query_config, api.update_config, api.delete_config,
                       api.export_config, api.clear_config)
    try:
        value = eval(value)
    except:
        pass
    reg.set(key, value)


@click.command()
@click.argument('key')
@click.option('--api',
              '-a',
              default=lambda: get_config_value("api", str, 'get'),
              help='The modlule name of the api.')
@log_options('get')
def get(key, api):
    """
    Get a config.
    """
    logger.info(f'[CMD]: reg get {key} --api {api}')
    reg = Registry()
    if api is not None:
        api = importlib.import_module(api)
        set_config_api(api.query_config, api.update_config, api.delete_config,
                       api.export_config, api.clear_config)
    rich.print(reg.get(key))


@click.command()
@click.argument('key')
@click.option('--api',
              '-a',
              default=lambda: get_config_value("api", str, 'get'),
              help='The modlule name of the api.')
@log_options('delete')
def delete(key, api):
    """
    Delete a config key.
    """
    logger.info(f'[CMD]: reg delete {key} --api {api}')
    reg = Registry()
    if api is not None:
        api = importlib.import_module(api)
        set_config_api(api.query_config, api.update_config, api.delete_config,
                       api.export_config, api.clear_config)
    reg.delete(key)


@click.command()
@click.argument('file')
@click.option('--api',
              '-a',
              default=lambda: get_config_value("api", str, 'get'),
              help='The modlule name of the api.')
@click.option('--format',
              '-f',
              default='pickle',
              help='The format of the config.')
@log_options('export')
def export(file, api, format):
    """
    Export a config.
    """
    logger.info(f'[CMD]: reg export {file} --api {api}')
    reg = Registry()
    if api is not None:
        api = importlib.import_module(api)
        set_config_api(api.query_config, api.update_config, api.delete_config,
                       api.export_config, api.clear_config)
    cfg = reg.export()
    if format == 'json':
        import json
        with open(file, 'w') as f:
            json.dump(cfg, f, indent=4)
    elif format == 'yaml':
        import yaml
        with open(file, 'w') as f:
            yaml.dump(cfg, f)
    elif format == 'pickle':
        import pickle
        with open(file, 'wb') as f:
            pickle.dump(cfg, f)
    else:
        raise ValueError(f'Unknown format: {format}')


@click.command()
@click.argument('file')
@click.option('--api',
              '-a',
              default=lambda: get_config_value("api", str, 'get'),
              help='The modlule name of the api.')
@click.option('--format',
              '-f',
              default='pickle',
              help='The format of the config.')
@log_options('load')
def load(file, api, format):
    """
    Load a config.
    """
    logger.info(f'[CMD]: reg load {file} --api {api}')
    reg = Registry()
    if api is not None:
        api = importlib.import_module(api)
        set_config_api(api.query_config, api.update_config, api.delete_config,
                       api.export_config, api.clear_config)
    if format == 'json':
        import json
        with open(file, 'r') as f:
            cfg = json.load(f)
    elif format == 'yaml':
        import yaml
        with open(file, 'r') as f:
            cfg = yaml.load(f, Loader=yaml.FullLoader)
    elif format == 'pickle':
        import pickle
        with open(file, 'rb') as f:
            cfg = pickle.load(f)
    elif format == 'report':
        from .storage import get_report_by_index
        report = get_report_by_index(int(file))
        cfg = report.config
        if cfg is None:
            raise ValueError(f'No config found for report {file}')
    else:
        raise ValueError(f'Unknown format: {format}')
    reg.clear()
    reg.update(cfg)


@click.command()
@click.option('--bootstrap',
              '-b',
              default=lambda: get_config_value("bootstrap", Path),
              help='The path of the bootstrap.')
def boot(bootstrap):
    """
    Run a bootstrap script.
    """
    if bootstrap is not None:
        run_script(bootstrap)


def parse_dynamic_option_value(value):
    """解析动态参数值"""
    try:
        parsed_value = ast.literal_eval(value)
    except (ValueError, SyntaxError):
        # 如果解析失败，返回原始字符串
        parsed_value = value
    return parsed_value


def parse_dynamic_options(args):
    """解析格式为 key=value 的未知参数列表"""
    pattern = re.compile(r'^([a-zA-Z_][\w\-]*)=(.+)$')
    result = {}
    for arg in args:
        match = pattern.match(arg)
        if match:
            key, value = match.groups()
            result[key] = parse_dynamic_option_value(value)
        else:
            raise ValueError(
                f"Invalid argument format: {arg}. Expected format is key=value."
            )
    return result


help_doc = """
Run a workflow.

If the workflow has entries, run all entries.
If `--no-dependents` is set, only run the workflow itself.
If `--retry` is set, retry the workflow when calibration failed.
If `--freeze` is set, freeze the config table.
If `--plot` is set, plot the report.
If `--api` is set, use the api to get and update the config table.
If `--code` is not set, use the current working directory.
If `--data` is not set, use the `logs` directory in the code path.
"""


@click.command(context_settings=dict(ignore_unknown_options=True,
                                     allow_extra_args=True),
               help=help_doc)
@click.argument('workflow')
@click.option('--plot', '-p', is_flag=True, help='Plot the report.')
@click.option('--no-dependents',
              '-n',
              is_flag=True,
              help='Do not run dependents.')
@click.option('--retry', '-r', default=1, type=int, help='Retry times.')
@click.option('--freeze', is_flag=True, help='Freeze the config table.')
@click.option('--fail-fast',
              '-f',
              is_flag=True,
              help='Fail immediately on first error.')
@click.option('--veryfy-source-code',
              is_flag=True,
              help='Veryfy the source code.')
@log_options('run')
@command_option('run')
@click.pass_context
@async_command
async def run(ctx,
              workflow,
              code,
              data,
              api,
              plot,
              no_dependents,
              retry,
              freeze,
              fail_fast,
              veryfy_source_code=True):
    logger.info(
        f'[CMD]: run {workflow} --code {code} --data {data} --api {api}'
        f'{" --plot" if plot else ""}'
        f'{" --no-dependents" if no_dependents else ""}'
        f' --retry {retry}'
        f'{" --freeze " if freeze else ""}')
    if api is not None:
        api = importlib.import_module(api)
        set_config_api(api.query_config, api.update_config, api.delete_config,
                       api.export_config, api.clear_config)
    if code is None:
        code = Path.cwd()
    if data is None:
        data = Path(code) / 'logs'

    code = Path(os.path.expanduser(code))
    data = Path(os.path.expanduser(data))

    extra_args = ctx.args
    params = parse_dynamic_options(extra_args)

    if params:
        workflow = (workflow, params)
        rich.print(workflow)

    wf = load_workflow(workflow, code, veryfy_source_code=veryfy_source_code)
    check_toplogy(wf, code, veryfy_source_code=veryfy_source_code)

    for i in range(retry):
        try:
            if no_dependents:
                if hasattr(wf, 'entries'):
                    exceptions = []
                    for entry in get_entries(
                            wf, code, veryfy_source_code=veryfy_source_code):
                        try:
                            await run_workflow(
                                entry,
                                code,
                                data,
                                plot=plot,
                                freeze=freeze,
                            )
                        except Exception as e:
                            if fail_fast:
                                raise e
                            exceptions.append(e)
                    if any(exceptions):
                        raise exceptions[0]
                else:
                    await run_workflow(
                        wf,
                        code,
                        data,
                        plot=plot,
                        freeze=freeze,
                    )
            else:
                if hasattr(wf, 'entries'):
                    exceptions = []
                    for entry in get_entries(
                            wf, code, veryfy_source_code=veryfy_source_code):
                        try:
                            await maintain_workflow(
                                entry,
                                code,
                                data,
                                run=True,
                                plot=plot,
                                freeze=freeze,
                                fail_fast=fail_fast,
                                veryfy_source_code=veryfy_source_code,
                            )
                        except Exception as e:
                            if fail_fast:
                                raise e
                            exceptions.append(e)
                    if any(exceptions):
                        raise exceptions[0]
                else:
                    await maintain_workflow(
                        wf,
                        code,
                        data,
                        run=True,
                        plot=plot,
                        freeze=freeze,
                        fail_fast=fail_fast,
                        veryfy_source_code=veryfy_source_code,
                    )
            break
        except CalibrationFailedError as e:
            if i == retry - 1:
                raise e
            logger.warning(f'Calibration failed, retrying ({i + 1}/{retry})')
            continue


@click.command()
@click.argument('workflow')
@click.option('--retry', '-r', default=1, type=int, help='Retry times.')
@click.option('--plot', '-p', is_flag=True, help='Plot the report.')
@click.option('--fail-fast',
              '-f',
              is_flag=True,
              help='Fail immediately on first error.')
@click.option('--veryfy-source-code',
              is_flag=True,
              help='Veryfy the source code.')
@log_options('maintain')
@command_option('maintain')
@async_command
async def maintain(workflow,
                   code,
                   data,
                   api,
                   retry,
                   plot,
                   fail_fast,
                   veryfy_source_code=True):
    """
    Maintain a workflow.

    If the workflow has entries, run all entries.
    If `--retry` is set, retry the workflow when calibration failed.
    If `--plot` is set, plot the report.
    If `--api` is set, use the api to get and update the config table.
    If `--code` is not set, use the current working directory.
    If `--data` is not set, use the `logs` directory in the code path.
    """
    logger.info(
        f'[CMD]: maintain {workflow} --code {code} --data {data} --api {api}'
        f' --retry {retry}'
        f'{" --plot" if plot else ""}')
    if api is not None:
        api = importlib.import_module(api)
        set_config_api(api.query_config, api.update_config, api.delete_config,
                       api.export_config, api.clear_config)
    if code is None:
        code = Path.cwd()
    if data is None:
        data = Path(code) / 'logs'

    code = Path(os.path.expanduser(code))
    data = Path(os.path.expanduser(data))

    wf = load_workflow(workflow, code, veryfy_source_code=veryfy_source_code)
    check_toplogy(wf, code, veryfy_source_code=veryfy_source_code)

    for i in range(retry):
        try:
            if hasattr(wf, 'entries'):
                exceptions = []
                for entry in get_entries(
                        wf, code, veryfy_source_code=veryfy_source_code):
                    try:
                        await maintain_workflow(
                            entry,
                            code,
                            data,
                            run=False,
                            plot=plot,
                            freeze=False,
                            fail_fast=fail_fast,
                            veryfy_source_code=veryfy_source_code,
                        )
                    except Exception as e:
                        if fail_fast:
                            raise e
                        exceptions.append(e)
                if any(exceptions):
                    raise exceptions[0]
            else:
                await maintain_workflow(
                    wf,
                    code,
                    data,
                    run=False,
                    plot=plot,
                    freeze=False,
                    fail_fast=fail_fast,
                    veryfy_source_code=veryfy_source_code,
                )
            break
        except CalibrationFailedError as e:
            if i == retry - 1:
                raise e
            logger.warning(f'Calibration failed, retrying ({i + 1}/{retry})')
            continue


@click.command()
@click.argument('report_id')
@click.option('--plot', '-p', is_flag=True, help='Plot the report.')
@log_options('reproduce')
@command_option('reproduce')
@async_command
async def reproduce(report_id, code, data, api, plot):
    """
    Reproduce a report.

    If `--plot` is set, plot the report.
    If `--api` is set, use the api to get and update the config table.
    If `--code` is not set, use the current working directory.
    If `--data` is not set, use the `logs` directory in the code path.
    """
    logger.info(
        f'[CMD]: reproduce {report_id} --code {code} --data {data} --api {api}'
        f'{" --plot" if plot else ""}')
    if api is not None:
        api = importlib.import_module(api)
        set_config_api(api.query_config, api.update_config, api.delete_config,
                       api.export_config, api.clear_config)
    if code is None:
        code = Path.cwd()
    if data is None:
        data = Path(code) / 'logs'

    code = Path(os.path.expanduser(code))
    data = Path(os.path.expanduser(data))

    from .load import load_workflow_from_source_code
    from .storage import get_report_by_index

    reg = Registry()

    r = get_report_by_index(int(report_id), data)

    wf = load_workflow_from_source_code(r.workflow, r.script)
    cfg = reg.export()
    reg.clear()
    reg.update(r.config)
    await run_workflow(wf, code, data, plot=plot, freeze=True)
    reg.clear()
    reg.update(cfg)
