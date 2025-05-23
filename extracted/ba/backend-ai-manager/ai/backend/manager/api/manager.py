from __future__ import annotations

import asyncio
import enum
import functools
import json
import logging
import socket
import textwrap
from collections.abc import Iterable
from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Final, FrozenSet, Optional, Tuple, cast

import aiohttp_cors
import attrs
import graphene
import sqlalchemy as sa
import trafaret as t
from aiohttp import web
from aiotools import aclosing

from ai.backend.common import redis_helper
from ai.backend.common import validators as tx
from ai.backend.common.events.schedule import (
    DoCheckPrecondEvent,
    DoScaleEvent,
    DoScheduleEvent,
    DoStartSessionEvent,
)
from ai.backend.common.types import PromMetric, PromMetricGroup, PromMetricPrimitive
from ai.backend.logging import BraceStyleAdapter

from .. import __version__
from ..defs import DEFAULT_ROLE
from ..errors.exceptions import (
    GenericBadRequest,
    InstanceNotFound,
    InvalidAPIParameters,
    ServerFrozen,
    ServiceUnavailable,
)
from ..models import AGENT_RESOURCE_OCCUPYING_KERNEL_STATUSES, agents, kernels
from ..models.health import (
    SQLAlchemyConnectionInfo,
    get_manager_db_cxn_status,
    report_manager_status,
)
from . import ManagerStatus, SchedulerEvent
from .auth import superadmin_required
from .types import CORSOptions, WebMiddleware
from .utils import (
    check_api_params,
    set_handler_attr,
)

if TYPE_CHECKING:
    from ai.backend.manager.models.gql import GraphQueryContext

    from .context import RootContext

log = BraceStyleAdapter(logging.getLogger(__spec__.name))


class SchedulerOps(enum.Enum):
    INCLUDE_AGENTS = "include-agents"
    EXCLUDE_AGENTS = "exclude-agents"


def server_status_required(allowed_status: FrozenSet[ManagerStatus]):
    def decorator(handler):
        @functools.wraps(handler)
        async def wrapped(request, *args, **kwargs) -> web.StreamResponse:
            root_ctx: RootContext = request.app["_root.context"]
            status = await root_ctx.config_provider.legacy_etcd_config_loader.get_manager_status()
            if status not in allowed_status:
                if status == ManagerStatus.FROZEN:
                    raise ServerFrozen
                msg = f"Server is not in the required status: {allowed_status}"
                raise ServiceUnavailable(msg)
            return await handler(request, *args, **kwargs)

        set_handler_attr(wrapped, "server_status_required", True)
        set_handler_attr(wrapped, "required_server_statuses", allowed_status)

        return wrapped

    return decorator


READ_ALLOWED: Final = frozenset({ManagerStatus.RUNNING, ManagerStatus.FROZEN})
ALL_ALLOWED: Final = frozenset({ManagerStatus.RUNNING})


class GQLMutationUnfrozenRequiredMiddleware:
    def resolve(self, next, root, info: graphene.ResolveInfo, **args) -> Any:
        graph_ctx: GraphQueryContext = info.context
        if (
            info.operation.operation == "mutation"
            and graph_ctx.manager_status == ManagerStatus.FROZEN
        ):
            raise ServerFrozen
        return next(root, info, **args)


async def detect_status_update(root_ctx: RootContext) -> None:
    try:
        async with aclosing(
            root_ctx.config_provider.legacy_etcd_config_loader.watch_manager_status()
        ) as agen:
            async for ev in agen:
                if ev.event == "put":
                    root_ctx.config_provider.legacy_etcd_config_loader.get_manager_status.cache_clear()
                    updated_status = await root_ctx.config_provider.legacy_etcd_config_loader.get_manager_status()
                    log.debug(
                        "Process-{0} detected manager status update: {1}",
                        root_ctx.pidx,
                        updated_status,
                    )
    except asyncio.CancelledError:
        pass


async def report_status_bgtask(root_ctx: RootContext) -> None:
    interval = cast(Optional[float], root_ctx.config_provider.config.manager.status_update_interval)
    if interval is None:
        # Do not run bgtask if interval is not set
        return
    try:
        while True:
            await asyncio.sleep(interval)
            try:
                await report_manager_status(root_ctx)
            except Exception as e:
                log.exception(f"Failed to report manager health status (e:{str(e)})")
    except asyncio.CancelledError:
        pass


async def fetch_manager_status(request: web.Request) -> web.Response:
    root_ctx: RootContext = request.app["_root.context"]
    log.info("MANAGER.FETCH_MANAGER_STATUS ()")
    try:
        status = await root_ctx.config_provider.legacy_etcd_config_loader.get_manager_status()
        # etcd_info = await root_ctx.shared_config.get_manager_nodes_info()
        configs = root_ctx.config_provider.config.manager

        async with root_ctx.db.begin() as conn:
            query = (
                sa.select([sa.func.count()])
                .select_from(kernels)
                .where(
                    (kernels.c.cluster_role == DEFAULT_ROLE)
                    & (kernels.c.status.in_(AGENT_RESOURCE_OCCUPYING_KERNEL_STATUSES)),
                )
            )
            active_sessions_num = await conn.scalar(query)

            _id = configs.id if configs.id else socket.gethostname()
            nodes = [
                {
                    "id": _id,
                    "num_proc": configs.num_proc,
                    "service_addr": str(configs.service_addr),
                    "heartbeat_timeout": configs.heartbeat_timeout,
                    "ssl_enabled": configs.ssl_enabled,
                    "active_sessions": active_sessions_num,
                    "status": status.value,
                    "version": __version__,
                    "api_version": request["api_version"],
                },
            ]
            return web.json_response({
                "nodes": nodes,
                "status": status.value,  # legacy?
                "active_sessions": active_sessions_num,  # legacy?
            })
    except Exception:
        log.exception("GET_MANAGER_STATUS: exception")
        raise


@superadmin_required
@check_api_params(
    t.Dict({
        t.Key("status"): tx.Enum(ManagerStatus),
        t.Key("force_kill", default=False): t.ToBool,
    })
)
async def update_manager_status(request: web.Request, params: Any) -> web.Response:
    root_ctx: RootContext = request.app["_root.context"]
    log.info(
        "MANAGER.UPDATE_MANAGER_STATUS (status:{}, force_kill:{})",
        params["status"],
        params["force_kill"],
    )
    try:
        status = params["status"]
        force_kill = params["force_kill"]
    except json.JSONDecodeError:
        raise InvalidAPIParameters(extra_msg="No request body!")
    except (AssertionError, ValueError) as e:
        raise InvalidAPIParameters(extra_msg=str(e.args[0]))

    if force_kill:
        await root_ctx.registry.kill_all_sessions()
    await root_ctx.config_provider.legacy_etcd_config_loader.update_manager_status(status)

    return web.Response(status=HTTPStatus.NO_CONTENT)


async def get_announcement(request: web.Request) -> web.Response:
    root_ctx: RootContext = request.app["_root.context"]
    data = await root_ctx.etcd.get("manager/announcement")
    if data is None:
        ret = {"enabled": False, "message": ""}
    else:
        ret = {"enabled": True, "message": data}
    return web.json_response(ret)


@superadmin_required
@check_api_params(
    t.Dict({
        t.Key("enabled", default="false"): t.ToBool,
        t.Key("message", default=None): t.Null | t.String,
    })
)
async def update_announcement(request: web.Request, params: Any) -> web.Response:
    root_ctx: RootContext = request.app["_root.context"]

    if params["enabled"]:
        if not params["message"]:
            raise InvalidAPIParameters(extra_msg="Empty message not allowed to enable announcement")
        await root_ctx.etcd.put("manager/announcement", params["message"])
    else:
        await root_ctx.etcd.delete("manager/announcement")
    return web.Response(status=HTTPStatus.NO_CONTENT)


iv_scheduler_ops_args = {
    SchedulerOps.INCLUDE_AGENTS: t.List(t.String),
    SchedulerOps.EXCLUDE_AGENTS: t.List(t.String),
}


@superadmin_required
@check_api_params(
    t.Dict({
        t.Key("op"): tx.Enum(SchedulerOps),
        t.Key("args"): t.Any,
    })
)
async def perform_scheduler_ops(request: web.Request, params: Any) -> web.Response:
    root_ctx: RootContext = request.app["_root.context"]
    try:
        args = iv_scheduler_ops_args[params["op"]].check(params["args"])
    except t.DataError as e:
        raise InvalidAPIParameters(
            f"Input validation failed for args with {params['op']}",
            extra_data=e.as_dict(),
        )
    if params["op"] in (SchedulerOps.INCLUDE_AGENTS, SchedulerOps.EXCLUDE_AGENTS):
        schedulable = params["op"] == SchedulerOps.INCLUDE_AGENTS
        async with root_ctx.db.begin() as conn:
            query = agents.update().values(schedulable=schedulable).where(agents.c.id.in_(args))
            result = await conn.execute(query)
            if result.rowcount < len(args):
                raise InstanceNotFound()
        if schedulable:
            # trigger scheduler
            await root_ctx.event_producer.produce_event(DoScheduleEvent())
    else:
        raise GenericBadRequest("Unknown scheduler operation")
    return web.Response(status=HTTPStatus.NO_CONTENT)


@superadmin_required
@check_api_params(
    t.Dict({
        t.Key("event"): tx.Enum(SchedulerEvent),
    })
)
async def scheduler_trigger(request: web.Request, params: Any) -> web.Response:
    root_ctx: RootContext = request.app["_root.context"]
    match params["event"]:
        case SchedulerEvent.SCHEDULE:
            await root_ctx.event_producer.produce_event(DoScheduleEvent())
        case SchedulerEvent.CHECK_PRECOND:
            await root_ctx.event_producer.produce_event(DoCheckPrecondEvent())
        case SchedulerEvent.START_SESSION:
            await root_ctx.event_producer.produce_event(DoStartSessionEvent())
        case SchedulerEvent.SCALE_SERVICES:
            await root_ctx.event_producer.produce_event(DoScaleEvent())
    return web.Response(status=HTTPStatus.NO_CONTENT)


@superadmin_required
async def scheduler_healthcheck(request: web.Request) -> web.Response:
    root_ctx: RootContext = request.app["_root.context"]
    manager_id = root_ctx.config_provider.config.manager.id

    scheduler_status = {}
    for event in SchedulerEvent:
        scheduler_status[event.value] = await redis_helper.execute(
            root_ctx.redis_live,
            lambda r: r.hgetall(f"manager.{manager_id}.{event.value}"),
            encoding="utf-8",
        )

    return web.json_response(scheduler_status)


class SQLAlchemyConnectionMetric(PromMetric):
    def __init__(self, node_id: str, pid: int, val: int) -> None:
        self.mgr_id = f"{node_id}:{pid}"
        self.val = val

    def metric_value_string(self, metric_name: str, primitive: PromMetricPrimitive) -> str:
        return f"""{metric_name}{{mgr_id="{self.mgr_id}"}} {self.val}"""


class SQLAlchemyTotalConnectionMetricGroup(PromMetricGroup[SQLAlchemyConnectionMetric]):
    @property
    def metric_name(self) -> str:
        return "sqlalchemy_total_connection"

    @property
    def description(self) -> str:
        return "The number of total connections in SQLAlchemy connection pool."

    @property
    def metric_primitive(self) -> PromMetricPrimitive:
        return PromMetricPrimitive.gauge


class SQLAlchemyOpenConnectionMetricGroup(PromMetricGroup[SQLAlchemyConnectionMetric]):
    @property
    def metric_name(self) -> str:
        return "sqlalchemy_open_connection"

    @property
    def description(self) -> str:
        return "The number of open connections in SQLAlchemy connection pool."

    @property
    def metric_primitive(self) -> PromMetricPrimitive:
        return PromMetricPrimitive.gauge


class SQLAlchemyClosedConnectionMetricGroup(PromMetricGroup[SQLAlchemyConnectionMetric]):
    @property
    def metric_name(self) -> str:
        return "sqlalchemy_closed_connection"

    @property
    def description(self) -> str:
        return "The number of closed connections in SQLAlchemy connection pool."

    @property
    def metric_primitive(self) -> PromMetricPrimitive:
        return PromMetricPrimitive.gauge


class RedisConnectionMetric(PromMetric):
    def __init__(self, node_id: str, pid: int, redis_obj_name: str, val: int) -> None:
        self.redis_obj_name = redis_obj_name
        self.mgr_id = f"{node_id}:{pid}"
        self.val = val

    def metric_value_string(self, metric_name: str, primitive: PromMetricPrimitive) -> str:
        return (
            f"""{metric_name}{{mgr_id="{self.mgr_id}",name="{self.redis_obj_name}"}} {self.val}"""
        )


class RedisConnectionMetricGroup(PromMetricGroup[RedisConnectionMetric]):
    @property
    def metric_name(self) -> str:
        return "redis_connection"

    @property
    def description(self) -> str:
        return "The number of connections in Redis Client's connection pool."

    @property
    def metric_primitive(self) -> PromMetricPrimitive:
        return PromMetricPrimitive.gauge


async def get_manager_status_for_prom(request: web.Request) -> web.Response:
    root_ctx: RootContext = request.app["_root.context"]
    status = await get_manager_db_cxn_status(root_ctx)

    total_cxn_metrics = []
    open_cxn_metrics = []
    closed_cxn_metrics = []
    redis_cxn_metrics = []
    for stat in status:
        sqlalchemy_info = cast(SQLAlchemyConnectionInfo, stat.sqlalchemy_info)

        total_cxn_metrics.append(
            SQLAlchemyConnectionMetric(stat.node_id, stat.pid, sqlalchemy_info.total_cxn)
        )
        open_cxn_metrics.append(
            SQLAlchemyConnectionMetric(stat.node_id, stat.pid, sqlalchemy_info.num_checkedout_cxn)
        )
        closed_cxn_metrics.append(
            SQLAlchemyConnectionMetric(stat.node_id, stat.pid, sqlalchemy_info.num_checkedin_cxn)
        )

        for redis_info in stat.redis_connection_info:
            if (num_cxn := redis_info.num_connections) is not None:
                redis_cxn_metrics.append(
                    RedisConnectionMetric(stat.node_id, stat.pid, redis_info.name, num_cxn)
                )

    metric_string = (
        SQLAlchemyTotalConnectionMetricGroup(total_cxn_metrics).metric_string(),
        SQLAlchemyOpenConnectionMetricGroup(open_cxn_metrics).metric_string(),
        SQLAlchemyClosedConnectionMetricGroup(closed_cxn_metrics).metric_string(),
        RedisConnectionMetricGroup(redis_cxn_metrics).metric_string(),
    )

    result = "\n".join(metric_string)
    return web.Response(text=textwrap.dedent(result))


@attrs.define(slots=True, auto_attribs=True, init=False)
class PrivateContext:
    status_watch_task: asyncio.Task
    db_status_report_task: asyncio.Task


async def init(app: web.Application) -> None:
    root_ctx: RootContext = app["_root.context"]
    app_ctx: PrivateContext = app["manager.context"]
    app_ctx.status_watch_task = asyncio.create_task(detect_status_update(root_ctx))
    app_ctx.db_status_report_task = asyncio.create_task(report_status_bgtask(root_ctx))


async def shutdown(app: web.Application) -> None:
    app_ctx: PrivateContext = app["manager.context"]
    if app_ctx.status_watch_task is not None:
        app_ctx.status_watch_task.cancel()
        await asyncio.sleep(0)
        if not app_ctx.status_watch_task.done():
            await app_ctx.status_watch_task
    if app_ctx.db_status_report_task is not None:
        app_ctx.db_status_report_task.cancel()
        await asyncio.sleep(0)
        if not app_ctx.db_status_report_task.done():
            await app_ctx.db_status_report_task


def create_app(
    default_cors_options: CORSOptions,
) -> Tuple[web.Application, Iterable[WebMiddleware]]:
    app = web.Application()
    app["api_versions"] = (2, 3, 4)
    app["manager.context"] = PrivateContext()
    app["prefix"] = "manager"
    cors = aiohttp_cors.setup(app, defaults=default_cors_options)
    status_resource = cors.add(app.router.add_resource("/status"))
    cors.add(status_resource.add_route("GET", fetch_manager_status))
    cors.add(status_resource.add_route("PUT", update_manager_status))
    announcement_resource = cors.add(app.router.add_resource("/announcement"))
    cors.add(announcement_resource.add_route("GET", get_announcement))
    cors.add(announcement_resource.add_route("POST", update_announcement))
    cors.add(app.router.add_route("POST", "/scheduler/operation", perform_scheduler_ops))
    cors.add(app.router.add_route("POST", "/scheduler/trigger", scheduler_trigger))
    cors.add(app.router.add_route("GET", "/scheduler/status", scheduler_healthcheck))
    prom_resource = cors.add(app.router.add_resource("/prom"))
    cors.add(prom_resource.add_route("GET", get_manager_status_for_prom))
    app.on_startup.append(init)
    app.on_shutdown.append(shutdown)
    return app, []
