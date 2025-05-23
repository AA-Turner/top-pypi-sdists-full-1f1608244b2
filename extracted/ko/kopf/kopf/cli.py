import asyncio
import dataclasses
import functools
import os
from collections.abc import Collection
from typing import Any, Callable, Optional

import click

from kopf._cogs.aiokits import aioadapters
from kopf._cogs.configs import configuration
from kopf._cogs.helpers import loaders
from kopf._cogs.structs import credentials, references
from kopf._core.actions import loggers
from kopf._core.engines import peering
from kopf._core.intents import registries
from kopf._core.reactor import running
from kopf._kits import loops


@dataclasses.dataclass()
class CLIControls:
    """ `KopfRunner` controls, which are impossible to pass via CLI. """
    ready_flag: Optional[aioadapters.Flag] = None
    stop_flag: Optional[aioadapters.Flag] = None
    vault: Optional[credentials.Vault] = None
    registry: Optional[registries.OperatorRegistry] = None
    settings: Optional[configuration.OperatorSettings] = None
    loop: Optional[asyncio.AbstractEventLoop] = None


# With Click>=8.2.0, that should be `click.Choice[LogFormat]`, but it is good for now, too.
# TODO: when Python 3.9 is dropped, upgrade dependencies to click>=8.2.0, and remake the class here.
#       see: https://github.com/nolar/kopf/pull/1174
class LogFormatParamType(click.Choice):  # type: ignore

    def __init__(self) -> None:
        super().__init__(choices=[v.name.lower() for v in loggers.LogFormat])

    def convert(self, value: Any, param: Any, ctx: Any) -> loggers.LogFormat:
        if isinstance(value, loggers.LogFormat):
            return value
        else:
            name: str = super().convert(value, param, ctx)
            return loggers.LogFormat[name.upper()]


def logging_options(fn: Callable[..., Any]) -> Callable[..., Any]:
    """ A decorator to configure logging in all commands the same way."""
    @click.option('-v', '--verbose', is_flag=True)
    @click.option('-d', '--debug', is_flag=True)
    @click.option('-q', '--quiet', is_flag=True)
    @click.option('--log-format', type=LogFormatParamType(), default='full')
    @click.option('--log-refkey', type=str)
    @click.option('--log-prefix/--no-log-prefix', default=None)
    @functools.wraps(fn)  # to preserve other opts/args
    def wrapper(verbose: bool, quiet: bool, debug: bool,
                log_format: loggers.LogFormat = loggers.LogFormat.FULL,
                log_prefix: Optional[bool] = False,
                log_refkey: Optional[str] = None,
                *args: Any, **kwargs: Any) -> Any:
        loggers.configure(debug=debug, verbose=verbose, quiet=quiet,
                          log_format=log_format, log_refkey=log_refkey, log_prefix=log_prefix)
        return fn(*args, **kwargs)

    return wrapper


@click.group(name='kopf', context_settings=dict(
    auto_envvar_prefix='KOPF',
))
@click.version_option(prog_name='kopf')
@click.make_pass_decorator(CLIControls, ensure=True)
def main(__controls: CLIControls) -> None:
    pass


@main.command()
@logging_options
@click.option('-A', '--all-namespaces', 'clusterwide', is_flag=True)
@click.option('-n', '--namespace', 'namespaces', multiple=True)
@click.option('--standalone', is_flag=True, default=None)
@click.option('--dev', 'priority', type=int, is_flag=True, flag_value=666)
@click.option('-L', '--liveness', 'liveness_endpoint', type=str)
@click.option('-P', '--peering', 'peering_name', type=str, envvar='KOPF_RUN_PEERING')
@click.option('-p', '--priority', type=int)
@click.option('-m', '--module', 'modules', multiple=True)
@click.argument('paths', nargs=-1)
@click.make_pass_decorator(CLIControls, ensure=True)
def run(
        __controls: CLIControls,
        paths: list[str],
        modules: list[str],
        peering_name: Optional[str],
        priority: Optional[int],
        standalone: Optional[bool],
        namespaces: Collection[references.NamespacePattern],
        clusterwide: bool,
        liveness_endpoint: Optional[str],
) -> None:
    """ Start an operator process and handle all the requests. """
    if os.environ.get('KOPF_RUN_NAMESPACE'):  # legacy for single-namespace mode
        namespaces = tuple(namespaces) + (os.environ.get('KOPF_RUN_NAMESPACE', ''),)
    if namespaces and clusterwide:
        raise click.UsageError("Either --namespace or --all-namespaces can be used, not both.")
    if __controls.registry is not None:
        registries.set_default_registry(__controls.registry)
    loaders.preload(
        paths=paths,
        modules=modules,
    )
    with loops.proper_loop(__controls.loop):
        return running.run(
            standalone=standalone,
            namespaces=namespaces,
            clusterwide=clusterwide,
            priority=priority,
            peering_name=peering_name,
            liveness_endpoint=liveness_endpoint,
            registry=__controls.registry,
            settings=__controls.settings,
            stop_flag=__controls.stop_flag,
            ready_flag=__controls.ready_flag,
            vault=__controls.vault,
            loop=__controls.loop,
        )


@main.command()
@logging_options
@click.option('-n', '--namespace', 'namespaces', multiple=True)
@click.option('-A', '--all-namespaces', 'clusterwide', is_flag=True)
@click.option('-i', '--id', type=str, default=None)
@click.option('--dev', 'priority', flag_value=666)
@click.option('-P', '--peering', 'peering_name', required=True, envvar='KOPF_FREEZE_PEERING')
@click.option('-p', '--priority', type=int, default=100, required=True)
@click.option('-t', '--lifetime', type=int, required=True)
@click.option('-m', '--message', type=str)
@click.make_pass_decorator(CLIControls, ensure=True)
def freeze(
        __controls: CLIControls,
        id: Optional[str],
        message: Optional[str],
        lifetime: int,
        namespaces: Collection[references.NamespacePattern],
        clusterwide: bool,
        peering_name: str,
        priority: int,
) -> None:
    """ Pause the resource handling in the operator(s). """
    identity = peering.Identity(id) if id else peering.detect_own_id(manual=True)
    insights = references.Insights()
    settings = configuration.OperatorSettings()
    settings.peering.name = peering_name
    settings.peering.priority = priority
    with loops.proper_loop(__controls.loop):
        return running.run(
            clusterwide=clusterwide,
            namespaces=namespaces,
            insights=insights,
            identity=identity,
            settings=settings,
            _command=peering.touch_command(
                insights=insights,
                identity=identity,
                settings=settings,
                lifetime=lifetime))


@main.command()
@logging_options
@click.option('-n', '--namespace', 'namespaces', multiple=True)
@click.option('-A', '--all-namespaces', 'clusterwide', is_flag=True)
@click.option('-i', '--id', type=str, default=None)
@click.option('-P', '--peering', 'peering_name', required=True, envvar='KOPF_RESUME_PEERING')
@click.make_pass_decorator(CLIControls, ensure=True)
def resume(
        __controls: CLIControls,
        id: Optional[str],
        namespaces: Collection[references.NamespacePattern],
        clusterwide: bool,
        peering_name: str,
) -> None:
    """ Resume the resource handling in the operator(s). """
    identity = peering.Identity(id) if id else peering.detect_own_id(manual=True)
    insights = references.Insights()
    settings = configuration.OperatorSettings()
    settings.peering.name = peering_name
    with loops.proper_loop(__controls.loop):
        return running.run(
            clusterwide=clusterwide,
            namespaces=namespaces,
            insights=insights,
            identity=identity,
            settings=settings,
            _command=peering.touch_command(
                insights=insights,
                identity=identity,
                settings=settings,
                lifetime=0))
