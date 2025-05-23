from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from enum import IntEnum
from graphlib import CycleError, TopologicalSorter
from multiprocessing import cpu_count
from typing import TYPE_CHECKING, Callable, Iterator, Optional

from gevent.pool import Pool
from paramiko import PKey

from pyinfra import logger

from .config import Config
from .exceptions import PyinfraError

if TYPE_CHECKING:
    from pyinfra.api.arguments import AllArguments
    from pyinfra.api.command import PyinfraCommand
    from pyinfra.api.host import Host
    from pyinfra.api.inventory import Inventory
    from pyinfra.api.operation import OperationMeta


# Work out the max parallel we can achieve with the open files limit of the user/process,
# take 10 for opening Python files and /3 for ~3 files per host during op runs.
# See: https://github.com/Fizzadar/pyinfra/issues/44
try:
    from resource import RLIMIT_NOFILE, getrlimit

    nofile_limit, _ = getrlimit(RLIMIT_NOFILE)
    MAX_PARALLEL = round((nofile_limit - 10) / 3)

# Resource isn't available on Windows
except ImportError:
    nofile_limit = 0
    MAX_PARALLEL = 100000


class BaseStateCallback:
    # Host callbacks
    #

    @staticmethod
    def host_before_connect(state: "State", host: "Host"):
        pass

    @staticmethod
    def host_connect(state: "State", host: "Host"):
        pass

    @staticmethod
    def host_connect_error(state: "State", host: "Host", error):
        pass

    @staticmethod
    def host_disconnect(state: "State", host: "Host"):
        pass

    # Operation callbacks
    #

    @staticmethod
    def operation_start(state: "State", op_hash):
        pass

    @staticmethod
    def operation_host_start(state: "State", host: "Host", op_hash):
        pass

    @staticmethod
    def operation_host_success(state: "State", host: "Host", op_hash):
        pass

    @staticmethod
    def operation_host_error(state: "State", host: "Host", op_hash):
        pass

    @staticmethod
    def operation_end(state: "State", op_hash):
        pass


class StateStage(IntEnum):
    # Setup - collect inventory & data
    Setup = 1
    # Connect - connect to the inventory
    Connect = 2
    # Prepare - detect operation changes
    Prepare = 3
    # Execute - execute operations
    Execute = 4
    # Disconnect - disconnect from the inventory
    Disconnect = 5


class StateOperationMeta:
    names: set[str]
    args: list[str]
    op_order: tuple[int, ...]
    global_arguments: "AllArguments"

    def __init__(self, op_order: tuple[int, ...]):
        self.op_order = op_order
        self.names = set()
        self.args = []
        self.global_arguments = {}  # type: ignore


@dataclass
class StateOperationHostData:
    command_generator: Callable[[], Iterator["PyinfraCommand"]]
    global_arguments: "AllArguments"
    operation_meta: "OperationMeta"
    parent_op_hash: Optional[str] = None


class StateHostMeta:
    ops = 0
    ops_change = 0
    ops_no_change = 0
    op_hashes: set[str]

    def __init__(self) -> None:
        self.op_hashes = set()


class StateHostResults:
    ops = 0
    success_ops = 0
    error_ops = 0
    ignored_error_ops = 0
    partial_ops = 0


class State:
    """
    Manages state for a pyinfra deploy.
    """

    initialised: bool = False

    # A pyinfra.api.Inventory which stores all our pyinfra.api.Host's
    inventory: "Inventory"

    # A pyinfra.api.Config
    config: "Config"

    # Main gevent pool
    pool: "Pool"

    # Current stage this state is in
    current_stage: StateStage = StateStage.Setup
    # Warning counters by stage
    stage_warnings: dict[StateStage, int] = defaultdict(int)

    # Whether we are executing operations (ie hosts are all ready)
    is_executing: bool = False

    # Whether we should check for operation changes as part of the operation ordering phase, this
    # allows us to guesstimate which ops will result in changes on which hosts.
    check_for_changes: bool = True

    print_noop_info: bool = False  # print "[host] noop: reason for noop"
    print_fact_info: bool = False  # print "loaded fact X"
    print_input: bool = False
    print_fact_input: bool = False
    print_output: bool = False
    print_fact_output: bool = False

    # Used in CLI
    cwd: Optional[str] = None  # base directory for locating files/templates/etc
    current_deploy_filename: Optional[str] = None
    current_exec_filename: Optional[str] = None
    current_op_file_number: int = 0
    should_raise_failed_hosts: Optional[Callable[["State"], bool]] = None

    def __init__(
        self,
        inventory: Optional["Inventory"] = None,
        config: Optional["Config"] = None,
        check_for_changes: bool = True,
        **kwargs,
    ):
        """
        Initializes the state, the main Pyinfra

        Args:
            inventory (Optional[Inventory], optional): The inventory. Defaults to None.
            config (Optional[Config], optional): The config object. Defaults to None.
        """
        self.check_for_changes = check_for_changes

        if inventory:
            self.init(inventory, config, **kwargs)

    def init(
        self,
        inventory: "Inventory",
        config: Optional["Config"],
        initial_limit=None,
    ):
        # Config validation
        #

        # If no config, create one using the defaults
        if config is None:
            config = Config()

        if not config.PARALLEL:
            # TODO: benchmark this
            # In my own tests the optimum number of parallel SSH processes is
            # ~20 per CPU core - no science here yet, needs benchmarking!
            cpus = cpu_count()
            ideal_parallel = cpus * 20

            config.PARALLEL = min(ideal_parallel, len(inventory), MAX_PARALLEL)

        # If explicitly set, just issue a warning
        elif config.PARALLEL > MAX_PARALLEL:
            logger.warning(
                (
                    "Parallel set to {0}, but this may hit the open files limit of {1}.\n"
                    "    Max recommended value: {2}"
                ).format(config.PARALLEL, nofile_limit, MAX_PARALLEL),
            )

        # Actually initialise the state object
        #

        self.callback_handlers: list[BaseStateCallback] = []

        # Setup greenlet pools
        self.pool = Pool(config.PARALLEL)
        self.fact_pool = Pool(config.PARALLEL)

        # Private keys
        self.private_keys: dict[str, PKey] = {}

        # Assign inventory/config
        self.inventory = inventory
        self.config = config

        # Hosts we've activated at any time
        self.activated_hosts: set["Host"] = set()
        # Active hosts that *haven't* failed yet
        self.active_hosts: set["Host"] = set()
        # Hosts that have failed
        self.failed_hosts: set["Host"] = set()

        # Limit hosts changes dynamically to limit operations to a subset of hosts
        self.limit_hosts: list["Host"] = initial_limit

        # Op basics
        self.op_meta: dict[str, StateOperationMeta] = {}  # maps operation hash -> names/etc

        # Op dict for each host
        self.ops: dict["Host", dict[str, StateOperationHostData]] = {host: {} for host in inventory}

        # Meta dict for each host
        self.meta: dict["Host", StateHostMeta] = {host: StateHostMeta() for host in inventory}

        # Results dict for each host
        self.results: dict["Host", StateHostResults] = {
            host: StateHostResults() for host in inventory
        }

        # Assign state back references to inventory & config
        inventory.state = config.state = self
        for host in inventory:
            host.init(self)

        self.initialised = True

    def set_stage(self, stage: StateStage) -> None:
        if stage < self.current_stage:
            raise Exception("State stage cannot go backwards!")
        self.current_stage = stage

    def increment_warning_counter(self) -> None:
        self.stage_warnings[self.current_stage] += 1

    def get_warning_counter(self) -> int:
        return self.stage_warnings[self.current_stage]

    def should_check_for_changes(self):
        return self.check_for_changes

    def add_callback_handler(self, handler):
        if not isinstance(handler, BaseStateCallback):
            raise TypeError(
                ("{0} is not a valid callback handler (use `BaseStateCallback`)").format(handler),
            )
        self.callback_handlers.append(handler)

    def trigger_callbacks(self, method_name: str, *args, **kwargs):
        for handler in self.callback_handlers:
            func = getattr(handler, method_name)
            func(self, *args, **kwargs)

    def get_op_order(self):
        ts: TopologicalSorter = TopologicalSorter()

        for host in self.inventory:
            for i, op_hash in enumerate(host.op_hash_order):
                if not i:
                    ts.add(op_hash)
                else:
                    ts.add(op_hash, host.op_hash_order[i - 1])

        final_op_order = []

        try:
            ts.prepare()
        except CycleError as e:
            raise PyinfraError(
                (
                    "Cycle detected in operation ordering DAG.\n"
                    f"    Error: {e}\n\n"
                    "    This can happen when using loops in operation code, "
                    "please see: https://docs.pyinfra.com/en/latest/deploy-process.html#loops-cycle-errors"  # noqa: E501
                ),
            )

        while ts.is_active():
            # Ensure that where we have multiple different operations that can be executed in any
            # dependency order we order them by line numbers.
            node_group = sorted(
                ts.get_ready(),
                key=lambda op_hash: self.op_meta[op_hash].op_order,
            )
            ts.done(*node_group)
            final_op_order.extend(node_group)

        return final_op_order

    def get_op_meta(self, op_hash: str) -> StateOperationMeta:
        return self.op_meta[op_hash]

    def get_meta_for_host(self, host: "Host") -> StateHostMeta:
        return self.meta[host]

    def get_results_for_host(self, host: "Host") -> StateHostResults:
        return self.results[host]

    def get_op_data_for_host(
        self,
        host: "Host",
        op_hash: str,
    ) -> StateOperationHostData:
        return self.ops[host][op_hash]

    def set_op_data_for_host(
        self,
        host: "Host",
        op_hash: str,
        op_data: StateOperationHostData,
    ):
        self.ops[host][op_hash] = op_data

    def activate_host(self, host: "Host"):
        """
        Flag a host as active.
        """

        logger.debug("Activating host: %s", host)

        # Add to *both* activated and active - active will reduce as hosts fail
        # but connected will not, enabling us to track failed %.
        self.activated_hosts.add(host)
        self.active_hosts.add(host)

    def fail_hosts(self, hosts_to_fail, activated_count=None):
        """
        Flag a ``set`` of hosts as failed, error for ``config.FAIL_PERCENT``.
        """

        if not hosts_to_fail:
            return

        activated_count = activated_count or len(self.activated_hosts)

        logger.debug(
            "Failing hosts: {0}".format(
                ", ".join(
                    (host.name for host in hosts_to_fail),
                ),
            ),
        )

        self.failed_hosts.update(hosts_to_fail)

        self.active_hosts -= hosts_to_fail

        # Check we're not above the fail percent
        active_hosts = self.active_hosts

        # No hosts left!
        if not active_hosts:
            raise PyinfraError("No hosts remaining!")

        if self.config.FAIL_PERCENT is not None:
            percent_failed = (1 - len(active_hosts) / activated_count) * 100

            if percent_failed > self.config.FAIL_PERCENT:
                if self.should_raise_failed_hosts and self.should_raise_failed_hosts(self) is False:
                    return

                raise PyinfraError(
                    "Over {0}% of hosts failed ({1}%)".format(
                        self.config.FAIL_PERCENT,
                        int(round(percent_failed)),
                    ),
                )

    def is_host_in_limit(self, host: "Host"):
        """
        Returns a boolean indicating if the host is within the current state limit.
        """

        limit_hosts = self.limit_hosts

        if not isinstance(limit_hosts, list):
            return True
        return host in limit_hosts
