from __future__ import annotations

import asyncio
import enum
import logging
import math
from abc import ABCMeta, abstractmethod
from collections import UserDict, defaultdict
from collections.abc import (
    Mapping,
    Sequence,
)
from datetime import datetime, timedelta
from decimal import Decimal
from typing import (
    TYPE_CHECKING,
    Annotated,
    Any,
    ClassVar,
    Final,
    List,
    NamedTuple,
    Optional,
    Self,
    Type,
    TypedDict,
    cast,
)

import aiotools
import sqlalchemy as sa
import trafaret as t
from aiotools import TaskGroupError
from dateutil.relativedelta import relativedelta
from pydantic import (
    BaseModel,
    Field,
    GetCoreSchemaHandler,
)
from pydantic_core import core_schema
from redis.asyncio import Redis
from sqlalchemy.engine import Row

import ai.backend.common.validators as tx
from ai.backend.common import msgpack, redis_helper
from ai.backend.common import typed_validators as tv
from ai.backend.common.config import BaseSchema, config_key_to_snake_case
from ai.backend.common.defs import REDIS_LIVE_DB, REDIS_STATISTICS_DB, RedisRole
from ai.backend.common.distributed import GlobalTimer
from ai.backend.common.events.dispatcher import (
    AbstractEvent,
    EventDispatcher,
    EventHandler,
    EventProducer,
)
from ai.backend.common.events.idle import (
    DoIdleCheckEvent,
)
from ai.backend.common.events.session import (
    DoTerminateSessionEvent,
    ExecutionCancelledEvent,
    ExecutionFinishedEvent,
    ExecutionStartedEvent,
    ExecutionTimeoutEvent,
    KernelLifecycleEventReason,
    SessionStartedEvent,
)
from ai.backend.common.types import (
    AccessKey,
    BinarySize,
    RedisConnectionInfo,
    RedisProfileTarget,
    ResourceSlot,
    SessionTypes,
)
from ai.backend.common.utils import nmget
from ai.backend.logging import BraceStyleAdapter
from ai.backend.manager.config.provider import ManagerConfigProvider

from .defs import DEFAULT_ROLE, LockID
from .event_dispatcher.reporters import EventLogger
from .models.kernel import LIVE_STATUS, kernels
from .models.keypair import keypairs
from .models.resource_policy import keypair_resource_policies
from .models.user import users
from .types import DistributedLockFactory

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncConnection as SAConnection

    from ai.backend.common.types import AgentId, KernelId, SessionId

    from .models.utils import ExtendedAsyncSAEngine as SAEngine

log = BraceStyleAdapter(logging.getLogger(__spec__.name))

DEFAULT_CHECK_INTERVAL: Final = 15.0
# idle checker's remaining time should be -1 when the remaining time is negative
IDLE_TIMEOUT_VALUE: Final = -1


class IdleCheckerError(TaskGroupError):
    """
    An exception that is a collection of multiple idle checkers.
    """


def parse_unit(resource_name: str, value: float | int) -> float | int:
    if resource_name.find("mem") == -1:
        return value
    return BinarySize(int(value))


def calculate_remaining_time(
    now: datetime,
    idle_baseline: datetime,
    timeout_period: timedelta,
    grace_period_end: Optional[datetime] = None,
) -> float:
    if grace_period_end is None:
        baseline = idle_baseline
    else:
        baseline = max(idle_baseline, grace_period_end)
    remaining = baseline - now + timeout_period
    return remaining.total_seconds()


async def get_redis_now(redis_obj: RedisConnectionInfo) -> float:
    t = await redis_helper.execute(redis_obj, lambda r: r.time())
    return t[0] + (t[1] / (10**6))


async def get_db_now(dbconn: SAConnection) -> datetime:
    return await dbconn.scalar(sa.select(sa.func.now()))


class UtilizationExtraInfo(NamedTuple):
    avg_util: float
    threshold: float


class UtilizationResourceReport(UserDict):
    __slots__ = ("data",)

    data: dict[str, UtilizationExtraInfo]

    @classmethod
    def from_avg_threshold(
        cls,
        avg_utils: Mapping[str, float],
        thresholds: ResourceThresholds,
        exclusions: set[str],
    ) -> UtilizationResourceReport:
        data: dict[str, UtilizationExtraInfo] = {}
        for metric_key, val in thresholds.items():
            if val.average is None or metric_key in exclusions:
                continue
            avg_util = avg_utils.get(metric_key, 0)
            data[metric_key] = UtilizationExtraInfo(float(avg_util), float(val.average))
        return cls(data)

    def to_dict(self, apply_unit: bool = True) -> dict[str, UtilizationExtraInfo]:
        if apply_unit:
            return {
                k: UtilizationExtraInfo(parse_unit(k, v[0]), parse_unit(k, v[1]))
                for k, v in self.data.items()
            }
        return {**self.data}

    @property
    def utilization_result(self) -> dict[str, bool]:
        return {k: v.avg_util >= v.threshold for k, v in self.data.items()}


class AppStreamingStatus(enum.Enum):
    NO_ACTIVE_CONNECTIONS = 0
    HAS_ACTIVE_CONNECTIONS = 1


class ThresholdOperator(enum.StrEnum):
    AND = "and"
    OR = "or"


class RemainingTimeType(enum.StrEnum):
    GRACE_PERIOD = "grace_period"
    EXPIRE_AFTER = "expire_after"


class ReportInfo(TypedDict):
    remaining: float | None
    remaining_time_type: str
    extra: dict[str, Any] | None


class IdleCheckerHost:
    check_interval: ClassVar[float] = DEFAULT_CHECK_INTERVAL

    def __init__(
        self,
        db: SAEngine,
        config_provider: ManagerConfigProvider,
        event_dispatcher: EventDispatcher,
        event_producer: EventProducer,
        lock_factory: DistributedLockFactory,
    ) -> None:
        self._checkers: list[BaseIdleChecker] = []
        self._frozen = False
        self._db = db
        self._config_provider = config_provider
        self._event_dispatcher = event_dispatcher
        self._event_producer = event_producer
        self._lock_factory = lock_factory
        redis_profile_target: RedisProfileTarget = RedisProfileTarget.from_dict(
            self._config_provider.config.redis.model_dump()
        )
        self._redis_live = redis_helper.get_redis_object(
            redis_profile_target.profile_target(RedisRole.LIVE),
            name="idle.live",
            db=REDIS_LIVE_DB,
        )
        self._redis_stat = redis_helper.get_redis_object(
            redis_profile_target.profile_target(RedisRole.STATISTICS),
            name="idle.stat",
            db=REDIS_STATISTICS_DB,
        )
        self._grace_period_checker: NewUserGracePeriodChecker = NewUserGracePeriodChecker()

    def add_checker(self, checker: BaseIdleChecker):
        if self._frozen:
            raise RuntimeError(
                "Cannot add a new idle checker after the idle checker host is frozen."
            )
        self._checkers.append(checker)

    async def start(self) -> None:
        self._frozen = True
        raw_config = self._config_provider.config.idle.checkers
        await self._grace_period_checker.populate_config(
            raw_config.get(self._grace_period_checker.name) or {}
        )
        for checker in self._checkers:
            await checker.populate_config(raw_config.get(checker.name) or {})
        self.timer = GlobalTimer(
            self._lock_factory(LockID.LOCKID_IDLE_CHECK_TIMER, self.check_interval),
            self._event_producer,
            lambda: DoIdleCheckEvent(),
            self.check_interval,
            task_name="idle_checker",
        )
        self._evh_idle_check = self._event_dispatcher.consume(
            DoIdleCheckEvent,
            None,
            self._do_idle_check,
        )
        await self.timer.join()

    async def shutdown(self) -> None:
        for checker in self._checkers:
            await checker.aclose()
        await self.timer.leave()
        self._event_dispatcher.unconsume(self._evh_idle_check)
        await self._redis_stat.close()
        await self._redis_live.close()

    async def update_app_streaming_status(
        self,
        session_id: SessionId,
        status: AppStreamingStatus,
    ) -> None:
        for checker in self._checkers:
            await checker.update_app_streaming_status(session_id, status)

    async def _do_idle_check(
        self,
        context: None,
        source: AgentId,
        event: DoIdleCheckEvent,
    ) -> None:
        log.debug("do_idle_check(): triggered")
        policy_cache: dict[AccessKey, Row] = {}
        async with self._db.begin_readonly() as conn:
            j = sa.join(kernels, users, kernels.c.user_uuid == users.c.uuid)
            query = (
                sa.select([
                    kernels.c.id,
                    kernels.c.access_key,
                    kernels.c.session_id,
                    kernels.c.session_type,
                    kernels.c.created_at,
                    kernels.c.occupied_slots,
                    kernels.c.requested_slots,
                    kernels.c.cluster_size,
                    users.c.created_at.label("user_created_at"),
                ])
                .select_from(j)
                .where(
                    (kernels.c.status.in_(LIVE_STATUS))
                    & (kernels.c.cluster_role == DEFAULT_ROLE)
                    & (kernels.c.session_type != SessionTypes.INFERENCE),
                )
            )
            result = await conn.execute(query)
            rows = result.fetchall()
            for kernel in rows:
                grace_period_end = await self._grace_period_checker.get_grace_period_end(kernel)
                policy = policy_cache.get(kernel["access_key"], None)
                if policy is None:
                    query = (
                        sa.select([
                            keypair_resource_policies.c.max_session_lifetime,
                            keypair_resource_policies.c.idle_timeout,
                        ])
                        .select_from(
                            sa.join(
                                keypairs,
                                keypair_resource_policies,
                                keypair_resource_policies.c.name == keypairs.c.resource_policy,
                            ),
                        )
                        .where(keypairs.c.access_key == kernel["access_key"])
                    )
                    result = await conn.execute(query)
                    policy = result.first()
                    assert policy is not None
                    policy_cache[kernel["access_key"]] = policy

                check_task = [
                    checker.check_idleness(
                        kernel, conn, policy, self._redis_live, grace_period_end=grace_period_end
                    )
                    for checker in self._checkers
                ]
                check_results = await asyncio.gather(*check_task, return_exceptions=True)
                terminated = False
                errors = []
                for checker, result in zip(self._checkers, check_results):
                    if isinstance(result, aiotools.TaskGroupError):
                        errors.extend(result.__errors__)
                        continue
                    elif isinstance(result, Exception):
                        # mark to be destroyed afterwards
                        errors.append(result)
                        continue
                    if not result:
                        log.info(
                            "The {} idle checker triggered termination of s:{}",
                            checker.name,
                            kernel["session_id"],
                        )
                        if not terminated:
                            terminated = True
                            await self._event_producer.produce_event(
                                DoTerminateSessionEvent(
                                    kernel["session_id"],
                                    checker.terminate_reason,
                                ),
                            )
                if errors:
                    raise IdleCheckerError("idle checker(s) raise errors", errors)

    async def get_idle_check_report(
        self,
        session_id: SessionId,
    ) -> dict[str, Any]:
        return {
            checker.name: {
                "remaining": await checker.get_checker_result(self._redis_live, session_id),
                "remaining_time_type": checker.remaining_time_type.value,
                "extra": await checker.get_extra_info(self._redis_live, session_id),
            }
            for checker in self._checkers
        }

    async def get_batch_idle_check_report(
        self,
        session_ids: Sequence[SessionId],
    ) -> dict[SessionId, dict[str, ReportInfo]]:
        class _ReportDataType(enum.StrEnum):
            REMAINING_TIME = "remaining"
            EXTRA_INFO = "extra"

        key_session_report_map: dict[str, tuple[SessionId, BaseIdleChecker, _ReportDataType]] = {}
        for sid in session_ids:
            for checker in self._checkers:
                _report_key = checker.get_report_key(sid)
                key_session_report_map[_report_key] = (sid, checker, _ReportDataType.REMAINING_TIME)
                if (_extra_key := checker.get_extra_info_key(sid)) is not None:
                    key_session_report_map[_extra_key] = (sid, checker, _ReportDataType.EXTRA_INFO)

        key_list = list(key_session_report_map.keys())

        async def _pipe_builder(r: Redis):
            pipe = r.pipeline()
            for key in key_list:
                await pipe.get(key)
            return pipe

        ret: dict[SessionId, dict[str, ReportInfo]] = {}
        for key, report in zip(
            key_list, await redis_helper.execute(self._redis_live, _pipe_builder)
        ):
            session_id, checker, report_type = key_session_report_map[key]
            if session_id not in ret:
                ret[session_id] = {}
            if checker.name not in ret[session_id]:
                ret[session_id][checker.name] = ReportInfo(
                    remaining=None,
                    remaining_time_type=checker.remaining_time_type.value,
                    extra=None,
                )
            raw_report = cast(bytes | None, report)
            if raw_report is None:
                continue

            ret[session_id][checker.name][report_type.value] = msgpack.unpackb(raw_report)
        return ret


class AbstractIdleCheckReporter(metaclass=ABCMeta):
    remaining_time_type: RemainingTimeType
    name: ClassVar[str] = "base"
    report_key: ClassVar[str] = "base"
    extra_info_key: ClassVar[str] = "base_extra"

    async def aclose(self) -> None:
        pass

    @abstractmethod
    async def populate_config(self, config: Mapping[str, Any]) -> None:
        raise NotImplementedError

    async def update_app_streaming_status(
        self,
        session_id: SessionId,
        status: AppStreamingStatus,
    ) -> None:
        pass

    @classmethod
    def get_report_key(cls, session_id: SessionId) -> str:
        return f"session.{session_id}.{cls.name}.report"

    @classmethod
    def get_extra_info_key(cls, session_id: SessionId) -> str | None:
        return None

    @abstractmethod
    async def get_extra_info(
        self, redis_obj: RedisConnectionInfo, session_id: SessionId
    ) -> Optional[dict[str, Any]]:
        return None

    @abstractmethod
    async def get_checker_result(
        self,
        redis_obj: RedisConnectionInfo,
        session_id: SessionId,
    ) -> Optional[float]:
        """
        Get check result of the given session.
        """
        pass

    async def set_remaining_time_report(
        self, redis_obj: RedisConnectionInfo, session_id: SessionId, remaining: float
    ) -> None:
        await redis_helper.execute(
            redis_obj,
            lambda r: r.set(
                self.get_report_key(session_id),
                msgpack.packb(remaining),
                ex=int(DEFAULT_CHECK_INTERVAL) * 10,
            ),
        )


class AbstractIdleChecker(metaclass=ABCMeta):
    terminate_reason: KernelLifecycleEventReason

    @abstractmethod
    async def check_idleness(
        self,
        kernel: Row,
        dbconn: SAConnection,
        policy: Row,
        redis_obj: RedisConnectionInfo,
        *,
        grace_period_end: Optional[datetime] = None,
    ) -> bool:
        """
        Check the kernel is whether idle or not.
        And report the result to Redis.
        """
        return True


class NewUserGracePeriodChecker(AbstractIdleCheckReporter):
    remaining_time_type: RemainingTimeType = RemainingTimeType.GRACE_PERIOD
    name: ClassVar[str] = "user_grace_period"
    report_key: ClassVar[str] = "user_grace_period"
    user_initial_grace_period: Optional[timedelta] = None

    _config_iv = t.Dict(
        {
            t.Key("user_initial_grace_period", default=None): t.Null | tx.TimeDuration(),
        },
    ).allow_extra("*")

    def __init__(self) -> None:
        pass

    async def populate_config(self, raw_config: Mapping[str, Any]) -> None:
        config = self._config_iv.check(raw_config)
        self.user_initial_grace_period = config["user_initial_grace_period"]
        _grace_period = (
            self.user_initial_grace_period.total_seconds()
            if self.user_initial_grace_period is not None
            else None
        )

        log.info(
            f"NewUserGracePeriodChecker: default period = {_grace_period} seconds",
        )

    async def get_extra_info(
        self, redis_obj: RedisConnectionInfo, session_id: SessionId
    ) -> Optional[dict[str, Any]]:
        return None

    async def del_remaining_time_report(
        self, redis_obj: RedisConnectionInfo, session_id: SessionId
    ) -> None:
        await redis_helper.execute(
            redis_obj,
            lambda r: r.delete(
                self.get_report_key(session_id),
            ),
        )

    async def get_grace_period_end(
        self,
        kernel: Row,
    ) -> Optional[datetime]:
        """
        Calculate the user's initial grace period for idle checkers.
        During the user's initial grace period, the checker does not calculate the time remaining until expiration
        and does not yield any extra information such as average utilization.
        """
        if self.user_initial_grace_period is None:
            return None
        user_created_at: datetime = kernel["user_created_at"]
        return user_created_at + self.user_initial_grace_period

    @property
    def grace_period_const(self) -> float:
        return (
            self.user_initial_grace_period.total_seconds()
            if self.user_initial_grace_period is not None
            else 0
        )

    async def get_checker_result(
        self,
        redis_obj: RedisConnectionInfo,
        session_id: SessionId,
    ) -> Optional[float]:
        key = self.get_report_key(session_id)
        data = await redis_helper.execute(redis_obj, lambda r: r.get(key))
        return msgpack.unpackb(data) if data is not None else None


class BaseIdleChecker(AbstractIdleChecker, AbstractIdleCheckReporter):
    _event_dispatcher: EventDispatcher
    _redis_live: RedisConnectionInfo
    _redis_stat: RedisConnectionInfo
    _db: SAEngine

    def __init__(
        self,
        event_dispatcher: EventDispatcher,
        redis_live: RedisConnectionInfo,
        redis_stat: RedisConnectionInfo,
        db: SAEngine,
    ) -> None:
        self._event_dispatcher = event_dispatcher
        self._redis_live = redis_live
        self._redis_stat = redis_stat
        self._db = db


class NetworkTimeoutIdleChecker(BaseIdleChecker):
    """
    Checks the idleness of a session by the elapsed time since last used.
    The usage means processing of any computation requests, such as
    query/batch-mode code execution and having active service-port connections.
    """

    terminate_reason: KernelLifecycleEventReason = KernelLifecycleEventReason.IDLE_TIMEOUT
    remaining_time_type: RemainingTimeType = RemainingTimeType.EXPIRE_AFTER
    name: ClassVar[str] = "network_timeout"
    report_key: ClassVar[str] = "network_timeout"
    extra_info_key: ClassVar[str] = "network_timeout_timeout_extra"

    _config_iv = t.Dict(
        {
            t.Key("threshold", default="10m"): tx.TimeDuration(),
        },
    ).allow_extra("*")

    idle_timeout: timedelta
    _evhandlers: List[EventHandler[None, AbstractEvent]]

    def __init__(
        self,
        event_dispatcher: EventDispatcher,
        redis_live: RedisConnectionInfo,
        redis_stat: RedisConnectionInfo,
        db: SAEngine,
    ) -> None:
        super().__init__(event_dispatcher, redis_live, redis_stat, db)
        self._event_dispatcher.subscribe(SessionStartedEvent, None, self._session_started_cb)  # type: ignore

        evd = self._event_dispatcher.with_reporters([EventLogger(self._db)])
        self._evhandlers = [
            evd.consume(ExecutionStartedEvent, None, self._execution_started_cb),  # type: ignore
            evd.consume(ExecutionFinishedEvent, None, self._execution_exited_cb),  # type: ignore
            evd.consume(ExecutionTimeoutEvent, None, self._execution_exited_cb),  # type: ignore
            evd.consume(ExecutionCancelledEvent, None, self._execution_exited_cb),  # type: ignore
        ]

    async def aclose(self) -> None:
        for _evh in self._evhandlers:
            self._event_dispatcher.unconsume(_evh)

    async def populate_config(self, raw_config: Mapping[str, Any]) -> None:
        config = self._config_iv.check(raw_config)
        self.idle_timeout = config["threshold"]
        log.info(
            "NetworkTimeoutIdleChecker: default idle_timeout = {0:,} seconds",
            self.idle_timeout.total_seconds(),
        )

    async def update_app_streaming_status(
        self,
        session_id: SessionId,
        status: AppStreamingStatus,
    ) -> None:
        if status == AppStreamingStatus.HAS_ACTIVE_CONNECTIONS:
            await self._disable_timeout(session_id)
        elif status == AppStreamingStatus.NO_ACTIVE_CONNECTIONS:
            await self._update_timeout(session_id)

    async def _disable_timeout(self, session_id: SessionId) -> None:
        log.debug(f"NetworkTimeoutIdleChecker._disable_timeout({session_id})")
        await redis_helper.execute(
            self._redis_live,
            lambda r: r.set(
                f"session.{session_id}.last_access",
                "0",
                xx=True,
            ),
        )

    async def _update_timeout(self, session_id: SessionId) -> None:
        log.debug(f"NetworkTimeoutIdleChecker._update_timeout({session_id})")
        t = await redis_helper.execute(self._redis_live, lambda r: r.time())
        t = t[0] + (t[1] / (10**6))
        await redis_helper.execute(
            self._redis_live,
            lambda r: r.set(
                f"session.{session_id}.last_access",
                f"{t:.06f}",
                ex=max(86400, int(self.idle_timeout.total_seconds() * 2)),
            ),
        )

    async def _session_started_cb(
        self,
        context: None,
        source: AgentId,
        event: SessionStartedEvent,
    ) -> None:
        log.debug("Got SessionStartedEvent")
        await self._update_timeout(event.session_id)

    async def _execution_started_cb(
        self,
        context: None,
        source: AgentId,
        event: ExecutionStartedEvent,
    ) -> None:
        await self._disable_timeout(event.session_id)

    async def _execution_exited_cb(
        self,
        context: None,
        source: AgentId,
        event: ExecutionFinishedEvent | ExecutionTimeoutEvent | ExecutionCancelledEvent,
    ) -> None:
        await self._update_timeout(event.session_id)

    async def get_extra_info(
        self, redis_obj: RedisConnectionInfo, session_id: SessionId
    ) -> Optional[dict[str, Any]]:
        return None

    async def check_idleness(
        self,
        kernel: Row,
        dbconn: SAConnection,
        policy: Row,
        redis_obj: RedisConnectionInfo,
        *,
        grace_period_end: Optional[datetime] = None,
    ) -> bool:
        """
        Check the kernel is timeout or not.
        And save remaining time until timeout of kernel to Redis.
        """
        session_id = kernel["session_id"]

        if SessionTypes(kernel["session_type"]) == SessionTypes.BATCH:
            return True

        active_streams = await redis_helper.execute(
            self._redis_live,
            lambda r: r.zcount(
                f"session.{session_id}.active_app_connections",
                float("-inf"),
                float("+inf"),
            ),
        )
        if active_streams is not None and active_streams > 0:
            return True
        now: float = await get_redis_now(self._redis_live)
        raw_last_access = await redis_helper.execute(
            self._redis_live,
            lambda r: r.get(f"session.{session_id}.last_access"),
        )
        if raw_last_access is None or raw_last_access == "0":
            return True
        last_access = float(raw_last_access)
        # serves as the default fallback if keypair resource policy's idle_timeout is "undefined"
        idle_timeout: float = self.idle_timeout.total_seconds()
        # setting idle_timeout:
        # - zero/inf means "infinite"
        # - negative means "undefined"
        if policy["idle_timeout"] >= 0:
            idle_timeout = float(policy["idle_timeout"])
        if (idle_timeout <= 0) or (math.isinf(idle_timeout) and idle_timeout > 0):
            return True
        tz = grace_period_end.tzinfo if grace_period_end is not None else None
        remaining = calculate_remaining_time(
            datetime.fromtimestamp(now, tz=tz),
            datetime.fromtimestamp(last_access, tz=tz),
            timedelta(seconds=idle_timeout),
            grace_period_end,
        )
        await self.set_remaining_time_report(
            redis_obj, session_id, remaining if remaining > 0 else IDLE_TIMEOUT_VALUE
        )
        return remaining >= 0

    async def get_checker_result(
        self,
        redis_obj: RedisConnectionInfo,
        session_id: SessionId,
    ) -> Optional[float]:
        key = self.get_report_key(session_id)
        data = await redis_helper.execute(redis_obj, lambda r: r.get(key))
        return msgpack.unpackb(data) if data is not None else None


class SessionLifetimeChecker(BaseIdleChecker):
    terminate_reason: KernelLifecycleEventReason = KernelLifecycleEventReason.IDLE_SESSION_LIFETIME
    remaining_time_type: RemainingTimeType = RemainingTimeType.EXPIRE_AFTER
    name: ClassVar[str] = "session_lifetime"
    report_key: ClassVar[str] = "session_lifetime"
    extra_info_key: ClassVar[str] = "session_lifetime_extra"

    async def populate_config(self, raw_config: Mapping[str, Any]) -> None:
        pass

    async def get_extra_info(
        self, redis_obj: RedisConnectionInfo, session_id: SessionId
    ) -> Optional[dict[str, Any]]:
        return None

    async def check_idleness(
        self,
        kernel: Row,
        dbconn: SAConnection,
        policy: Row,
        redis_obj: RedisConnectionInfo,
        *,
        grace_period_end: Optional[datetime] = None,
    ) -> bool:
        """
        Check the kernel has been living longer than resource policy's `max_session_lifetime`.
        And save remaining time until `max_session_lifetime` of kernel to Redis.
        """

        session_id = kernel["session_id"]
        if (max_session_lifetime := policy["max_session_lifetime"]) > 0:
            # TODO: once per-status time tracking is implemented, let's change created_at
            #       to the timestamp when the session entered PREPARING status.
            idle_timeout = timedelta(seconds=max_session_lifetime)
            now: datetime = await get_db_now(dbconn)
            kernel_created_at: datetime = kernel["created_at"]
            remaining = calculate_remaining_time(
                now, kernel_created_at, idle_timeout, grace_period_end
            )
            await self.set_remaining_time_report(
                redis_obj, session_id, remaining if remaining > 0 else IDLE_TIMEOUT_VALUE
            )
            return remaining > 0
        return True

    async def get_checker_result(
        self,
        redis_obj: RedisConnectionInfo,
        session_id: SessionId,
    ) -> Optional[float]:
        key = self.get_report_key(session_id)
        data = await redis_helper.execute(redis_obj, lambda r: r.get(key))
        return msgpack.unpackb(data) if data is not None else None


_metric_name_postfix = ("_util", "_mem", "_used")


def _get_resource_name_from_metric_key(name: str) -> str:
    for p in _metric_name_postfix:
        if name.endswith(p):
            return name.removesuffix(p)
    return name


class ResourceThresholdValue(BaseModel):
    average: Annotated[
        int | float | Decimal | None,
        Field(
            default=None,
            description="Threshold value. Default is 'null', which means the idle checker does not take into account the resource.",
        ),
    ]
    name: Annotated[
        str | None,
        Field(
            default=None,
            description=(
                f"Unique resource name that does not have any {_metric_name_postfix} postfix. "
                f"Default is 'null'. If this value is 'null', any of {_metric_name_postfix} postfix of the resource name is removed."
            ),
        ),
    ]


class ResourceThresholds(dict[str, ResourceThresholdValue]):
    @classmethod
    def default_factory(cls) -> Self:
        return cls(
            cpu_util=ResourceThresholdValue(average=None, name=None),
            mem=ResourceThresholdValue(average=None, name=None),
            cuda_util=ResourceThresholdValue(average=None, name=None),
            cuda_mem=ResourceThresholdValue(average=None, name=None),
        )

    @classmethod
    def threshold_validator(cls, value: dict[str, Any]) -> Self:
        return cls({k: ResourceThresholdValue(**v) for k, v in value.items()})

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: type[Any],
        _handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        schema = core_schema.chain_schema([
            core_schema.dict_schema(
                keys_schema=core_schema.str_schema(), values_schema=core_schema.any_schema()
            ),
            core_schema.no_info_plain_validator_function(cls.threshold_validator),
        ])

        return core_schema.json_or_python_schema(
            json_schema=schema,
            python_schema=schema,
        )


class UtilizationConfig(BaseSchema):
    time_window: tv.TimeDuration
    initial_grace_period: tv.TimeDuration
    thresholds_check_operator: Annotated[
        ThresholdOperator,
        Field(
            default=ThresholdOperator.AND,
            description=f"One of {[v.value for v in ThresholdOperator]}. Default is `and`.",
        ),
    ]
    resource_thresholds: Annotated[
        ResourceThresholds,
        Field(
            default_factory=ResourceThresholds.default_factory,
            description="Resource thresholds used to check utilization idleness.",
        ),
    ]


class UtilizationIdleChecker(BaseIdleChecker):
    """
    Checks the idleness of a session by the average utilization of compute devices.
    """

    terminate_reason: KernelLifecycleEventReason = KernelLifecycleEventReason.IDLE_UTILIZATION
    remaining_time_type: RemainingTimeType = RemainingTimeType.GRACE_PERIOD
    name: ClassVar[str] = "utilization"
    report_key: ClassVar[str] = "utilization"
    extra_info_key: ClassVar[str] = "utilization_extra"

    resource_thresholds: ResourceThresholds
    resource_names_to_check: set[str]
    thresholds_check_operator: ThresholdOperator
    time_window: timedelta
    initial_grace_period: timedelta
    _evhandlers: List[EventHandler[None, AbstractEvent]]

    async def populate_config(self, raw_config: Mapping[str, Any]) -> None:
        config = UtilizationConfig(**config_key_to_snake_case(raw_config))
        self.resource_thresholds = config.resource_thresholds
        self.resource_names_to_check: set[str] = set(self.resource_thresholds.keys())
        self.thresholds_check_operator = ThresholdOperator(config.thresholds_check_operator)

        def _to_timedelta(val: tv.TVariousDelta) -> timedelta:
            match val:
                case timedelta():
                    return val
                case relativedelta():
                    raise ValueError("Should not use 'yr' or 'mo' unit.")

        self.time_window = _to_timedelta(config.time_window)
        self.initial_grace_period = _to_timedelta(config.initial_grace_period)

        thresholds_log = " ".join([
            f"{k}({threshold.average})," for k, threshold in self.resource_thresholds.items()
        ])
        log.info(
            f"UtilizationIdleChecker(%): {thresholds_log} "
            f'thresholds-check-operator("{self.thresholds_check_operator}"), '
            f"time-window({self.time_window.total_seconds()}s)"
        )

    @classmethod
    def get_extra_info_key(cls, session_id: SessionId) -> str | None:
        return f"session.{session_id}.{cls.extra_info_key}"

    async def get_extra_info(
        self, redis_obj: RedisConnectionInfo, session_id: SessionId
    ) -> Optional[dict[str, Any]]:
        key = self.get_extra_info_key(session_id)
        assert key is not None
        data = await redis_helper.execute(
            redis_obj,
            lambda r: r.get(key),
        )
        return msgpack.unpackb(data) if data is not None else None

    def get_time_window(self, policy: Row) -> timedelta:
        # Respect idle_timeout, from keypair resource policy, over time_window.
        if (idle_timeout := policy["idle_timeout"]) >= 0:
            return timedelta(seconds=idle_timeout)
        return self.time_window

    def _get_last_collected_key(self, session_id: SessionId) -> str:
        return f"session.{session_id}.util_last_collected"

    def _get_first_collected_key(self, session_id: SessionId) -> str:
        return f"session.{session_id}.util_first_collected"

    async def check_idleness(
        self,
        kernel: Row,
        dbconn: SAConnection,
        policy: Row,
        redis_obj: RedisConnectionInfo,
        *,
        grace_period_end: Optional[datetime] = None,
    ) -> bool:
        """
        Check the the average utilization of kernel and whether it exceeds the threshold or not.
        And save the average utilization of kernel to Redis.
        """
        session_id = kernel["session_id"]

        interval = IdleCheckerHost.check_interval
        # time_window: Utilization is calculated within this window.
        time_window: timedelta = self.get_time_window(policy)
        occupied_slots = cast(ResourceSlot, kernel["occupied_slots"])
        requested_slots = cast(ResourceSlot, kernel["requested_slots"])
        excluded_resources: set[str] = set()

        util_series_key = f"session.{session_id}.util_series"
        util_first_collected_key = self._get_first_collected_key(session_id)
        util_last_collected_key = self._get_last_collected_key(session_id)

        # window_size: the length of utilization reports.
        window_size = int(time_window.total_seconds() / interval)
        if (window_size <= 0) or (math.isinf(window_size) and window_size > 0):
            return True

        # Wait until the time "interval" is passed after the last udpated time.
        t = await redis_helper.execute(self._redis_live, lambda r: r.time())
        util_now: float = t[0] + (t[1] / (10**6))
        raw_util_last_collected = cast(
            bytes | None,
            await redis_helper.execute(
                self._redis_live,
                lambda r: r.get(util_last_collected_key),
            ),
        )
        util_last_collected: float = (
            float(raw_util_last_collected) if raw_util_last_collected else 0.0
        )
        if util_now - util_last_collected < interval:
            return True

        raw_util_first_collected = cast(
            bytes | None,
            await redis_helper.execute(
                self._redis_live,
                lambda r: r.get(util_first_collected_key),
            ),
        )
        if raw_util_first_collected is None:
            util_first_collected = util_now
            await redis_helper.execute(
                self._redis_live,
                lambda r: r.set(
                    util_first_collected_key,
                    f"{util_now:.06f}",
                    ex=max(86400, int(self.time_window.total_seconds() * 2)),
                ),
            )
        else:
            util_first_collected = float(raw_util_first_collected)

        # Report time remaining until the first time window is full as expire time
        db_now: datetime = await get_db_now(dbconn)
        kernel_created_at: datetime = kernel["created_at"]
        if grace_period_end is not None:
            start_from = max(grace_period_end, kernel_created_at)
        else:
            start_from = kernel_created_at
        total_initial_grace_period_end = start_from + self.initial_grace_period
        remaining = calculate_remaining_time(
            db_now, kernel_created_at, time_window, total_initial_grace_period_end
        )
        await self.set_remaining_time_report(
            redis_obj, session_id, remaining if remaining > 0 else IDLE_TIMEOUT_VALUE
        )

        # Respect initial grace period (no calculation of utilization and no termination of the session)
        if db_now <= total_initial_grace_period_end:
            return True

        # Register requested resources.
        requested_resource_names: set[str] = set()
        for slot_name, val in requested_slots.items():
            if Decimal(val) == 0:
                # The resource is not allocated to this session.
                continue
            _slot_name = cast(str, slot_name)
            resource_name, _, _ = _slot_name.partition(".")
            if resource_name:
                requested_resource_names.add(resource_name)

        # Do not take into account unallocated resources. For example, do not garbage collect
        # a session without GPU even if cuda_util is configured in resource-thresholds.
        for resource_key in self.resource_thresholds.keys():
            if _get_resource_name_from_metric_key(resource_key) not in requested_resource_names:
                excluded_resources.add(resource_key)

        # Get current utilization data from all containers of the session.
        if kernel["cluster_size"] > 1:
            query = sa.select([kernels.c.id]).where(
                (kernels.c.session_id == session_id) & (kernels.c.status.in_(LIVE_STATUS)),
            )
            rows = (await dbconn.execute(query)).fetchall()
            kernel_ids = [k["id"] for k in rows]
        else:
            kernel_ids = [kernel["id"]]
        current_utilizations = await self.get_current_utilization(kernel_ids, occupied_slots)
        if current_utilizations is None:
            return True

        # Update utilization time-series data.
        raw_util_series = cast(
            Optional[bytes],
            await redis_helper.execute(self._redis_live, lambda r: r.get(util_series_key)),
        )

        def default_util_series() -> dict[str, list[float]]:
            return {resource: [] for resource in current_utilizations.keys()}

        if raw_util_series is not None:
            try:
                raw_data: dict[str, list[float]] = msgpack.unpackb(raw_util_series, use_list=True)
                util_series: dict[str, list[float]] = {
                    metric_key: v for metric_key, v in raw_data.items()
                }
            except TypeError:
                util_series = default_util_series()
        else:
            util_series = default_util_series()

        do_idle_check: bool = True

        for metric_key, val in current_utilizations.items():
            if metric_key not in util_series:
                util_series[metric_key] = []
            util_series[metric_key].append(val)
            if len(util_series[metric_key]) > window_size:
                util_series[metric_key].pop(0)
            else:
                do_idle_check = False

        # Do not skip idleness-check if the current time passed the time window
        if util_now - util_first_collected >= time_window.total_seconds():
            do_idle_check = True

        await redis_helper.execute(
            self._redis_live,
            lambda r: r.set(
                util_series_key,
                msgpack.packb(util_series),
                ex=max(86400, int(self.time_window.total_seconds() * 2)),
            ),
        )
        await redis_helper.execute(
            self._redis_live,
            lambda r: r.set(
                util_last_collected_key,
                f"{util_now:.06f}",
                ex=max(86400, int(self.time_window.total_seconds() * 2)),
            ),
        )

        def _avg(util_list: list[float]) -> float:
            try:
                return sum(util_list) / len(util_list)
            except ZeroDivisionError:
                return 0.0

        avg_utils: Mapping[str, float] = {k: _avg(v) for k, v in util_series.items()}

        util_avg_thresholds = UtilizationResourceReport.from_avg_threshold(
            avg_utils, self.resource_thresholds, excluded_resources
        )
        report = {
            "thresholds_check_operator": self.thresholds_check_operator.value,
            "resources": util_avg_thresholds.to_dict(),
        }
        _key = self.get_extra_info_key(session_id)
        assert _key is not None
        await redis_helper.execute(
            redis_obj,
            lambda r: r.set(
                _key,
                msgpack.packb(report),
                ex=int(DEFAULT_CHECK_INTERVAL) * 10,
            ),
        )

        if not do_idle_check:
            return True

        # Check over-utilized (not to be collected) resources.
        sufficiently_utilized = util_avg_thresholds.utilization_result
        check_result = True
        if len(sufficiently_utilized) < 1:
            check_result = True
        elif self.thresholds_check_operator == ThresholdOperator.OR:
            check_result = all(sufficiently_utilized.values())
        else:  # "and" operation is the default
            check_result = any(sufficiently_utilized.values())
        if not check_result:
            log.info(
                "utilization timeout: {} ({}, {})",
                session_id,
                avg_utils,
                self.thresholds_check_operator,
            )
        return check_result

    async def get_current_utilization(
        self,
        kernel_ids: Sequence[KernelId],
        occupied_slots: Mapping[str, Any],
    ) -> Mapping[str, float] | None:
        """
        Return the current utilization key-value pairs of multiple kernels, possibly the
        components of a cluster session. If there are multiple kernel_ids, this method
        will return the averaged values over the kernels for each utilization.
        """
        try:
            utilizations: defaultdict[str, float] = defaultdict(float)
            live_stat = {}
            kernel_counter = 0
            for kernel_id in kernel_ids:
                raw_live_stat = cast(
                    bytes | None,
                    await redis_helper.execute(
                        self._redis_stat,
                        lambda r: r.get(str(kernel_id)),
                    ),
                )
                if raw_live_stat is None:
                    log.warning(
                        f"Utilization data not found or failed to fetch utilization data. Skip idle check (k:{kernel_id})"
                    )
                    continue
                live_stat = cast(dict[str, Any], msgpack.unpackb(raw_live_stat))
                kernel_utils = {
                    k: float(nmget(live_stat, f"{k}.pct", 0.0))
                    for k in self.resource_names_to_check
                }

                for resource, val in kernel_utils.items():
                    utilizations[resource] = utilizations[resource] + val

                # NOTE: Manual calculation of mem utilization.
                # mem.capacity does not report total amount of memory allocated to
                # the container, and mem.pct always report >90% even when nothing is
                # executing. So, we just replace it with the value of occupied slot.
                mem_slots = float(occupied_slots.get("mem", 0))
                mem_current = float(nmget(live_stat, "mem.current", 0.0))
                utilizations["mem"] = (
                    utilizations["mem"] + mem_current / mem_slots * 100 if mem_slots > 0 else 0
                )

                kernel_counter += 1
            if kernel_counter == 0:
                return None
            divider = kernel_counter
            total_utilizations = {k: v / divider for k, v in utilizations.items()}
            return total_utilizations
        except Exception as e:
            _msg = f"Unable to collect utilization for idleness check (kernels:{kernel_ids})"
            log.warning(_msg, exc_info=e)
            return None

    async def get_checker_result(
        self,
        redis_obj: RedisConnectionInfo,
        session_id: SessionId,
    ) -> Optional[float]:
        key = self.get_report_key(session_id)
        data = await redis_helper.execute(redis_obj, lambda r: r.get(key))
        return msgpack.unpackb(data) if data is not None else None


checker_registry: Mapping[str, Type[BaseIdleChecker]] = {
    NetworkTimeoutIdleChecker.name: NetworkTimeoutIdleChecker,
    UtilizationIdleChecker.name: UtilizationIdleChecker,
}


async def init_idle_checkers(
    db: SAEngine,
    config_provider: ManagerConfigProvider,
    event_dispatcher: EventDispatcher,
    event_producer: EventProducer,
    lock_factory: DistributedLockFactory,
) -> IdleCheckerHost:
    """
    Create an instance of session idleness checker
    from the given configuration and using the given event dispatcher.
    """
    checker_host = IdleCheckerHost(
        db,
        config_provider,
        event_dispatcher,
        event_producer,
        lock_factory,
    )
    checker_init_args = (event_dispatcher, checker_host._redis_live, checker_host._redis_stat, db)
    log.info("Initializing idle checker: user_initial_grace_period, session_lifetime")
    checker_host.add_checker(SessionLifetimeChecker(*checker_init_args))  # enabled by default
    enabled_checkers = config_provider.config.idle.enabled
    if enabled_checkers:
        for checker_name in enabled_checkers.split(","):
            checker_name = checker_name.strip()
            checker_cls = checker_registry.get(checker_name, None)
            if checker_cls is None:
                log.warning("ignoring an unknown idle checker name: {}", checker_name)
                continue
            log.info("Initializing idle checker: {}", checker_name)
            checker_instance = checker_cls(*checker_init_args)
            checker_host.add_checker(checker_instance)
    return checker_host
