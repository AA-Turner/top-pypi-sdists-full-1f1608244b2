from __future__ import annotations

import asyncio
import base64
import json
import logging
import os
import re
import secrets
import shutil
import signal
import struct
import sys
from collections.abc import Iterable, Mapping, MutableMapping, Sequence
from dataclasses import dataclass
from decimal import Decimal
from functools import partial
from io import StringIO
from pathlib import Path
from subprocess import CalledProcessError
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Final,
    FrozenSet,
    List,
    Optional,
    Set,
    Tuple,
    Union,
    cast,
    override,
)
from uuid import UUID

import aiofiles
import aiohttp
import aiotools
import pkg_resources
import zmq
import zmq.asyncio
from aiodocker.docker import Docker, DockerContainer
from aiodocker.exceptions import DockerError
from aiodocker.types import PortInfo
from aiomonitor.task import preserve_termination_log
from aiotools import TaskGroup
from async_timeout import timeout

from ai.backend.common import redis_helper
from ai.backend.common.cgroup import get_cgroup_mount_point
from ai.backend.common.docker import (
    MAX_KERNELSPEC,
    MIN_KERNELSPEC,
    ImageRef,
    KernelFeatures,
    LabelName,
)
from ai.backend.common.dto.agent.response import PurgeImageResp, PurgeImagesResp
from ai.backend.common.dto.manager.rpc_request import PurgeImagesReq
from ai.backend.common.events.dispatcher import EventProducer
from ai.backend.common.events.kernel import KernelLifecycleEventReason
from ai.backend.common.exception import ImageNotAvailable, InvalidImageName, InvalidImageTag
from ai.backend.common.json import (
    dump_json,
    load_json,
)
from ai.backend.common.plugin.monitor import ErrorPluginContext, StatsPluginContext
from ai.backend.common.types import (
    AgentId,
    AutoPullBehavior,
    BinarySize,
    ClusterInfo,
    ClusterSSHPortMapping,
    ContainerId,
    DeviceId,
    DeviceName,
    ImageConfig,
    ImageRegistry,
    KernelCreationConfig,
    KernelId,
    MountPermission,
    MountTypes,
    ResourceGroupType,
    ResourceSlot,
    Sentinel,
    ServicePort,
    SessionId,
    SlotName,
    current_resource_slots,
)
from ai.backend.common.utils import (
    AsyncFileWriter,
    current_loop,
)
from ai.backend.logging import BraceStyleAdapter
from ai.backend.logging.formatter import pretty

from ..agent import (
    ACTIVE_STATUS_SET,
    AbstractAgent,
    AbstractKernelCreationContext,
    ComputerContext,
    ScanImagesResult,
)
from ..exception import ContainerCreationError, UnsupportedResource
from ..fs import create_scratch_filesystem, destroy_scratch_filesystem
from ..kernel import AbstractKernel
from ..plugin.network import ContainerNetworkCapability, ContainerNetworkInfo, NetworkPluginContext
from ..proxy import DomainSocketProxy, proxy_connection
from ..resources import AbstractComputePlugin, KernelResourceSpec, Mount, known_slot_types
from ..scratch import create_loop_filesystem, destroy_loop_filesystem
from ..server import get_extra_volumes
from ..types import (
    AgentEventData,
    Container,
    ContainerStatus,
    KernelOwnershipData,
    LifecycleEvent,
    MountInfo,
    Port,
)
from ..utils import (
    closing_async,
    container_pid_to_host_pid,
    get_kernel_id_from_container,
    host_pid_to_container_pid,
    update_nested_dict,
)
from .kernel import DockerKernel
from .metadata.server import MetadataServer
from .resources import load_resources, scan_available_resources
from .utils import PersistentServiceContainer

if TYPE_CHECKING:
    from ai.backend.common.auth import PublicKey
    from ai.backend.common.etcd import AsyncEtcd

log = BraceStyleAdapter(logging.getLogger(__spec__.name))
eof_sentinel = Sentinel.TOKEN

LDD_GLIBC_REGEX = re.compile(r"^ldd \([^\)]+\) ([\d\.]+)$")
LDD_MUSL_REGEX = re.compile(r"^musl libc .+$")

known_glibc_distros: Final[dict[float, str]] = {
    2.17: "centos7.6",
    2.27: "ubuntu18.04",
    2.28: "centos8.0",
    2.31: "ubuntu20.04",
    2.34: "centos9.0",
    2.35: "ubuntu22.04",
    2.39: "ubuntu24.04",
}


def container_from_docker_container(src: DockerContainer) -> Container:
    ports = []
    for private_port, host_ports in src["NetworkSettings"]["Ports"].items():
        private_port = int(private_port.split("/")[0])
        if host_ports is None:
            host_ip = "127.0.0.1"
            host_port = 0
        else:
            host_ip = host_ports[0]["HostIp"]
            host_port = int(host_ports[0]["HostPort"])
        ports.append(Port(host_ip, private_port, host_port))
    return Container(
        id=src._id,
        status=src["State"]["Status"],
        image=src["Config"]["Image"],
        labels=src["Config"]["Labels"],
        ports=ports,
        backend_obj=src,
    )


async def _clean_scratch(
    loop: asyncio.AbstractEventLoop,
    scratch_type: str,
    scratch_root: Path,
    kernel_id: KernelId,
) -> None:
    scratch_dir = scratch_root / str(kernel_id)
    tmp_dir = scratch_root / f"{kernel_id}_tmp"
    try:
        if sys.platform.startswith("linux") and scratch_type == "memory":
            await destroy_scratch_filesystem(scratch_dir)
            await destroy_scratch_filesystem(tmp_dir)
            await loop.run_in_executor(None, shutil.rmtree, scratch_dir)
            await loop.run_in_executor(None, shutil.rmtree, tmp_dir)
        elif sys.platform.startswith("linux") and scratch_type == "hostfile":
            await destroy_loop_filesystem(scratch_root, kernel_id)
        else:
            await loop.run_in_executor(None, shutil.rmtree, scratch_dir)
    except CalledProcessError:
        pass
    except FileNotFoundError:
        pass


def _DockerError_reduce(self):
    return (
        type(self),
        (self.status, {"message": self.message}, *self.args),
    )


def _DockerContainerError_reduce(self):
    return (
        type(self),
        (self.status, {"message": self.message}, self.container_id, *self.args),
    )


@dataclass
class DockerPurgeImageReq:
    image: str
    force: bool
    noprune: bool


class DockerKernelCreationContext(AbstractKernelCreationContext[DockerKernel]):
    scratch_dir: Path
    tmp_dir: Path
    config_dir: Path
    work_dir: Path
    container_configs: List[Mapping[str, Any]]
    domain_socket_proxies: List[DomainSocketProxy]
    computer_docker_args: Dict[str, Any]
    port_pool: Set[int]
    agent_sockpath: Path
    resource_lock: asyncio.Lock
    cluster_ssh_port_mapping: Optional[ClusterSSHPortMapping]
    gwbridge_subnet: Optional[str]

    network_plugin_ctx: NetworkPluginContext

    def __init__(
        self,
        ownership_data: KernelOwnershipData,
        event_producer: EventProducer,
        kernel_image: ImageRef,
        kernel_config: KernelCreationConfig,
        distro: str,
        local_config: Mapping[str, Any],
        computers: MutableMapping[DeviceName, ComputerContext],
        port_pool: Set[int],
        agent_sockpath: Path,
        resource_lock: asyncio.Lock,
        network_plugin_ctx: NetworkPluginContext,
        restarting: bool = False,
        cluster_ssh_port_mapping: Optional[ClusterSSHPortMapping] = None,
        gwbridge_subnet: Optional[str] = None,
    ) -> None:
        super().__init__(
            ownership_data,
            event_producer,
            kernel_image,
            kernel_config,
            distro,
            local_config,
            computers,
            restarting=restarting,
        )
        kernel_id = ownership_data.kernel_id
        scratch_dir = (self.local_config["container"]["scratch-root"] / str(kernel_id)).resolve()
        tmp_dir = (self.local_config["container"]["scratch-root"] / f"{kernel_id}_tmp").resolve()

        self.scratch_dir = scratch_dir
        self.tmp_dir = tmp_dir
        self.config_dir = scratch_dir / "config"
        self.work_dir = scratch_dir / "work"
        self.uid = kernel_config["uid"]
        self.main_gid = kernel_config["main_gid"]
        self.supplementary_gids = set(kernel_config["supplementary_gids"])

        self.port_pool = port_pool
        self.agent_sockpath = agent_sockpath
        self.resource_lock = resource_lock

        self.container_configs = []
        self.domain_socket_proxies = []
        self.computer_docker_args = {}

        self.cluster_ssh_port_mapping = cluster_ssh_port_mapping
        self.gwbridge_subnet = gwbridge_subnet

        self.network_plugin_ctx = network_plugin_ctx

    @override
    def get_overriding_uid(self) -> Optional[int]:
        return self.uid

    @override
    def get_overriding_gid(self) -> Optional[int]:
        return self.main_gid

    @override
    def get_supplementary_gids(self) -> set[int]:
        return self.supplementary_gids

    def _kernel_resource_spec_read(self, filename):
        with open(filename, "r") as f:
            resource_spec = KernelResourceSpec.read_from_file(f)
        return resource_spec

    async def get_extra_envs(self) -> Mapping[str, str]:
        return {}

    async def prepare_resource_spec(self) -> Tuple[KernelResourceSpec, Optional[Mapping[str, Any]]]:
        loop = current_loop()
        if self.restarting:
            resource_spec = await loop.run_in_executor(
                None, self._kernel_resource_spec_read, self.config_dir / "resource.txt"
            )
            resource_opts = None
        else:
            slots = ResourceSlot.from_json(self.kernel_config["resource_slots"])
            # Ensure that we have intrinsic slots.
            assert SlotName("cpu") in slots
            assert SlotName("mem") in slots
            # accept unknown slot type with zero values
            # but reject if they have non-zero values.
            for st, sv in slots.items():
                if st not in known_slot_types and sv != Decimal(0):
                    raise UnsupportedResource(st)
            # sanitize the slots
            current_resource_slots.set(known_slot_types)
            slots = slots.normalize_slots(ignore_unknown=True)
            resource_spec = KernelResourceSpec(
                allocations={},
                slots={**slots},  # copy
                mounts=[],
                scratch_disk_size=0,  # TODO: implement (#70)
            )
            resource_opts = self.kernel_config.get("resource_opts", {})
        return resource_spec, resource_opts

    def _chown_paths_if_root(
        self, paths: Iterable[Path], uid: Optional[int], gid: Optional[int]
    ) -> None:
        if os.geteuid() == 0:  # only possible when I am root.
            for p in paths:
                if KernelFeatures.UID_MATCH in self.kernel_features:
                    valid_uid = (
                        uid if uid is not None else self.local_config["container"]["kernel-uid"]
                    )
                    valid_gid = (
                        gid if gid is not None else self.local_config["container"]["kernel-gid"]
                    )
                else:
                    stat = os.stat(p)
                    valid_uid = uid if uid is not None else stat.st_uid
                    valid_gid = gid if gid is not None else stat.st_gid
                os.chown(p, valid_uid, valid_gid)

    async def prepare_scratch(self) -> None:
        loop = current_loop()

        # Create the scratch, config, and work directories.
        scratch_type = self.local_config["container"]["scratch-type"]
        scratch_root = self.local_config["container"]["scratch-root"]
        scratch_size = self.local_config["container"]["scratch-size"]

        if sys.platform.startswith("linux") and scratch_type == "memory":
            await loop.run_in_executor(None, partial(self.tmp_dir.mkdir, exist_ok=True))
            await create_scratch_filesystem(self.scratch_dir, 64)
            await create_scratch_filesystem(self.tmp_dir, 64)
        elif sys.platform.startswith("linux") and scratch_type == "hostfile":
            await create_loop_filesystem(scratch_root, scratch_size, self.kernel_id)
        else:
            await loop.run_in_executor(None, partial(self.scratch_dir.mkdir, exist_ok=True))

        def _create_scratch_dirs():
            self.config_dir.mkdir(parents=True, exist_ok=True)
            self.config_dir.chmod(0o755)
            self.work_dir.mkdir(parents=True, exist_ok=True)
            self.work_dir.chmod(0o755)

        await loop.run_in_executor(None, _create_scratch_dirs)

        if not self.restarting:
            # Since these files are bind-mounted inside a bind-mounted directory,
            # we need to touch them first to avoid their "ghost" files are created
            # as root in the host-side filesystem, which prevents deletion of scratch
            # directories when the agent is running as non-root.
            def _clone_dotfiles():
                jupyter_custom_css_path = Path(
                    pkg_resources.resource_filename("ai.backend.runner", "jupyter-custom.css")
                )
                logo_path = Path(pkg_resources.resource_filename("ai.backend.runner", "logo.svg"))
                font_path = Path(pkg_resources.resource_filename("ai.backend.runner", "roboto.ttf"))
                font_italic_path = Path(
                    pkg_resources.resource_filename("ai.backend.runner", "roboto-italic.ttf")
                )
                bashrc_path = Path(pkg_resources.resource_filename("ai.backend.runner", ".bashrc"))
                bash_profile_path = Path(
                    pkg_resources.resource_filename("ai.backend.runner", ".bash_profile")
                )
                zshrc_path = Path(pkg_resources.resource_filename("ai.backend.runner", ".zshrc"))
                vimrc_path = Path(pkg_resources.resource_filename("ai.backend.runner", ".vimrc"))
                tmux_conf_path = Path(
                    pkg_resources.resource_filename("ai.backend.runner", ".tmux.conf")
                )
                jupyter_custom_dir = self.work_dir / ".jupyter" / "custom"
                jupyter_custom_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy(jupyter_custom_css_path.resolve(), jupyter_custom_dir / "custom.css")
                shutil.copy(logo_path.resolve(), jupyter_custom_dir / "logo.svg")
                shutil.copy(font_path.resolve(), jupyter_custom_dir / "roboto.ttf")
                shutil.copy(font_italic_path.resolve(), jupyter_custom_dir / "roboto-italic.ttf")
                shutil.copy(bashrc_path.resolve(), self.work_dir / ".bashrc")
                shutil.copy(bash_profile_path.resolve(), self.work_dir / ".bash_profile")
                shutil.copy(zshrc_path.resolve(), self.work_dir / ".zshrc")
                shutil.copy(vimrc_path.resolve(), self.work_dir / ".vimrc")
                shutil.copy(tmux_conf_path.resolve(), self.work_dir / ".tmux.conf")

                def chown_scratch(uid: Optional[int], gid: Optional[int]) -> None:
                    paths = [
                        self.work_dir,
                        self.work_dir / ".jupyter",
                        self.work_dir / ".jupyter" / "custom",
                        self.work_dir / ".bashrc",
                        self.work_dir / ".bash_profile",
                        self.work_dir / ".zshrc",
                        self.work_dir / ".vimrc",
                        self.work_dir / ".tmux.conf",
                    ]
                    self._chown_paths_if_root(paths, uid, gid)

                do_override = False
                if (ouid := self.get_overriding_uid()) is not None:
                    do_override = True

                if (ogid := self.get_overriding_gid()) is not None:
                    do_override = True

                if do_override:
                    chown_scratch(ouid, ogid)
                else:
                    if KernelFeatures.UID_MATCH in self.kernel_features:
                        chown_scratch(
                            self.local_config["container"]["kernel-uid"],
                            self.local_config["container"]["kernel-gid"],
                        )

            await loop.run_in_executor(None, _clone_dotfiles)

    async def get_intrinsic_mounts(self) -> Sequence[Mount]:
        loop = current_loop()

        # scratch/config/tmp mounts
        mounts: List[Mount] = [
            Mount(
                MountTypes.BIND, self.config_dir, Path("/home/config"), MountPermission.READ_ONLY
            ),
            Mount(MountTypes.BIND, self.work_dir, Path("/home/work"), MountPermission.READ_WRITE),
        ]
        if (
            sys.platform.startswith("linux")
            and self.local_config["container"]["scratch-type"] == "memory"
        ):
            mounts.append(
                Mount(
                    MountTypes.BIND,
                    self.tmp_dir,
                    Path("/tmp"),
                    MountPermission.READ_WRITE,
                )
            )
        # /etc/localtime and /etc/timezone mounts
        if sys.platform.startswith("linux"):
            localtime_file = Path("/etc/localtime")
            timezone_file = Path("/etc/timezone")
            if localtime_file.exists():
                mounts.append(
                    Mount(
                        type=MountTypes.BIND,
                        source=localtime_file,
                        target=localtime_file,
                        permission=MountPermission.READ_ONLY,
                    )
                )
            if timezone_file.exists():
                mounts.append(
                    Mount(
                        type=MountTypes.BIND,
                        source=timezone_file,
                        target=timezone_file,
                        permission=MountPermission.READ_ONLY,
                    )
                )
        # lxcfs mounts
        lxcfs_root = Path("/var/lib/lxcfs")
        if lxcfs_root.is_dir():
            mounts.extend(
                Mount(
                    MountTypes.BIND,
                    lxcfs_proc_path,
                    "/" / lxcfs_proc_path.relative_to(lxcfs_root),
                    MountPermission.READ_WRITE,
                )
                for lxcfs_proc_path in (lxcfs_root / "proc").iterdir()
                if lxcfs_proc_path.stat().st_size > 0
            )
            mounts.extend(
                Mount(
                    MountTypes.BIND,
                    lxcfs_root / path,
                    "/" / Path(path),
                    MountPermission.READ_WRITE,
                )
                for path in [
                    "sys/devices/system/cpu",
                    "sys/devices/system/cpu/online",
                ]
                if Path(lxcfs_root / path).exists()
            )

        # extra mounts
        async with closing_async(Docker()) as docker:
            extra_mount_list = await get_extra_volumes(docker, self.image_ref.short)
        mounts.extend(
            Mount(MountTypes.VOLUME, v.name, v.container_path, v.mode) for v in extra_mount_list
        )

        # debug mounts
        if self.local_config["debug"]["coredump"]["enabled"]:
            mounts.append(
                Mount(
                    MountTypes.BIND,
                    self.local_config["debug"]["coredump"]["path"],
                    self.local_config["debug"]["coredump"]["core_path"],
                    MountPermission.READ_WRITE,
                )
            )

        # agent-socket mount
        if sys.platform != "darwin":
            mounts.append(
                Mount(
                    MountTypes.BIND,
                    self.agent_sockpath,
                    Path("/opt/kernel/agent.sock"),
                    MountPermission.READ_WRITE,
                )
            )
        ipc_base_path = self.local_config["agent"]["ipc-base-path"]

        # domain-socket proxy mount
        # (used for special service containers such image importer)
        for host_sock_path in self.internal_data.get("domain_socket_proxies", []):
            await loop.run_in_executor(
                None, partial((ipc_base_path / "proxy").mkdir, parents=True, exist_ok=True)
            )
            host_proxy_path = ipc_base_path / "proxy" / f"{secrets.token_hex(12)}.sock"
            proxy_server = await asyncio.start_unix_server(
                aiotools.apartial(proxy_connection, host_sock_path), str(host_proxy_path)
            )
            await loop.run_in_executor(None, host_proxy_path.chmod, 0o666)
            self.domain_socket_proxies.append(
                DomainSocketProxy(
                    Path(host_sock_path),
                    host_proxy_path,
                    proxy_server,
                )
            )
            mounts.append(
                Mount(
                    MountTypes.BIND,
                    host_proxy_path,
                    host_sock_path,
                    MountPermission.READ_WRITE,
                )
            )

        return mounts

    def resolve_krunner_filepath(self, filename) -> Path:
        return Path(
            pkg_resources.resource_filename(
                "ai.backend.runner",
                "../" + filename,
            )
        ).resolve()

    def get_runner_mount(
        self,
        type: MountTypes,
        src: Union[str, Path],
        target: Union[str, Path],
        perm: MountPermission = MountPermission.READ_ONLY,
        opts: Optional[Mapping[str, Any]] = None,
    ) -> Mount:
        return Mount(
            type,
            Path(src),
            Path(target),
            MountPermission(perm),
            opts=opts,
        )

    async def apply_network(self, cluster_info: ClusterInfo) -> None:
        # FIXME: find out way to inect network ID to kernel resource spec
        match cluster_info["network_config"].get("mode"):
            case "bridge":
                self.container_configs.append({
                    "HostConfig": {
                        "NetworkMode": cluster_info["network_config"]["network_name"],
                    },
                    "NetworkingConfig": {
                        "EndpointsConfig": {
                            cluster_info["network_config"]["network_name"]: {
                                "Aliases": [self.kernel_config["cluster_hostname"]],
                            },
                        },
                    },
                })
            case mode if mode:
                try:
                    plugin = self.network_plugin_ctx.plugins[mode]
                except KeyError:
                    raise RuntimeError(f"Network plugin {mode} not loaded!")

                container_config = await plugin.join_network(
                    self.kernel_config, cluster_info, **cluster_info["network_config"]
                )
                self.container_configs.append(container_config)
                if self.gwbridge_subnet is not None:
                    self.container_configs.append({
                        "Env": [f"OMPI_MCA_btl_tcp_if_exclude=127.0.0.1/32,{self.gwbridge_subnet}"],
                    })
        if self.local_config["container"].get("alternative-bridge") is not None:
            self.container_configs.append({
                "HostConfig": {
                    "NetworkMode": self.local_config["container"]["alternative-bridge"],
                },
            })
        # RDMA mounts
        ib_root = Path("/dev/infiniband")
        if ib_root.is_dir() and (ib_root / "uverbs0").exists():
            self.container_configs.append({
                "HostConfig": {
                    "Devices": [
                        {
                            "PathOnHost": "/dev/infiniband",
                            "PathInContainer": "/dev/infiniband",
                            "CgroupPermissions": "rwm",
                        },
                    ],
                },
            })

    async def prepare_ssh(self, cluster_info: ClusterInfo) -> None:
        sshkey = cluster_info["ssh_keypair"]
        if sshkey is None:
            return

        def _write_config():
            try:
                priv_key_path = self.config_dir / "ssh" / "id_cluster"
                pub_key_path = self.config_dir / "ssh" / "id_cluster.pub"
                priv_key_path.parent.mkdir(parents=True, exist_ok=True)
                priv_key_path.write_text(sshkey["private_key"])
                pub_key_path.write_text(sshkey["public_key"])

                def chown_keyfile(uid: Optional[int], gid: Optional[int]) -> None:
                    self._chown_paths_if_root([priv_key_path, pub_key_path], uid, gid)

                do_override = False
                if (ouid := self.get_overriding_uid()) is not None:
                    do_override = True

                if (ogid := self.get_overriding_gid()) is not None:
                    do_override = True

                if do_override:
                    chown_keyfile(ouid, ogid)
                else:
                    if KernelFeatures.UID_MATCH in self.kernel_features:
                        chown_keyfile(
                            self.local_config["container"]["kernel-uid"],
                            self.local_config["container"]["kernel-gid"],
                        )
                priv_key_path.chmod(0o600)
                if cluster_ssh_port_mapping := cluster_info["cluster_ssh_port_mapping"]:
                    port_mapping_json_path = self.config_dir / "ssh" / "port-mapping.json"
                    port_mapping_json_path.write_bytes(dump_json(cluster_ssh_port_mapping))
            except Exception:
                log.exception("error while writing cluster keypair")

        current_loop().run_in_executor(None, _write_config)  # ???

    async def process_mounts(self, mounts: Sequence[Mount]):
        def fix_unsupported_perm(folder_perm: MountPermission) -> MountPermission:
            if folder_perm == MountPermission.RW_DELETE:
                # TODO: enforce readable/writable but not deletable
                # (Currently docker's READ_WRITE includes DELETE)
                return MountPermission.READ_WRITE
            return folder_perm

        container_config = {
            "HostConfig": {
                "Mounts": [
                    {
                        "Target": str(mount.target),
                        "Source": str(mount.source),
                        "Type": mount.type.value,
                        "ReadOnly": (
                            fix_unsupported_perm(mount.permission) == MountPermission.READ_ONLY
                        ),
                        f"{mount.type.value.capitalize()}Options": mount.opts if mount.opts else {},
                    }
                    for mount in mounts
                ],
            },
        }
        self.container_configs.append(container_config)

    async def apply_accelerator_allocation(
        self,
        computer: AbstractComputePlugin,
        device_alloc: Mapping[SlotName, Mapping[DeviceId, Decimal]],
    ) -> None:
        async with closing_async(Docker()) as docker:
            update_nested_dict(
                self.computer_docker_args,
                await computer.generate_docker_args(docker, device_alloc),
            )

    async def generate_accelerator_mounts(
        self,
        computer: AbstractComputePlugin,
        device_alloc: Mapping[SlotName, Mapping[DeviceId, Decimal]],
    ) -> List[MountInfo]:
        src_path = self.config_dir / str(computer.key)
        src_path.mkdir()
        return await computer.generate_mounts(src_path, device_alloc)

    async def prepare_container(
        self,
        resource_spec: KernelResourceSpec,
        environ: Mapping[str, str],
        service_ports: List[ServicePort],
        cluster_info: ClusterInfo,
    ) -> DockerKernel:
        loop = current_loop()
        ouid = self.get_overriding_uid()
        ogid = self.get_overriding_gid()

        if self.restarting:
            pass
        else:
            # Create bootstrap.sh into workdir if needed
            if bootstrap := self.kernel_config.get("bootstrap_script"):

                def _write_user_bootstrap_script():
                    (self.work_dir / "bootstrap.sh").write_text(bootstrap)
                    if ouid is not None or ogid is not None:
                        self._chown_paths_if_root([self.work_dir / "bootstrap.sh"], ouid, ogid)
                    else:
                        if KernelFeatures.UID_MATCH in self.kernel_features:
                            self._chown_paths_if_root(
                                [self.work_dir / "bootstrap.sh"],
                                self.local_config["container"]["kernel-uid"],
                                self.local_config["container"]["kernel-gid"],
                            )

                await loop.run_in_executor(None, _write_user_bootstrap_script)

            with StringIO() as buf:
                for k, v in environ.items():
                    buf.write(f"{k}={v}\n")
                accel_envs = self.computer_docker_args.get("Env", [])
                for env in accel_envs:
                    buf.write(f"{env}\n")
                await loop.run_in_executor(
                    None,
                    (self.config_dir / "environ.txt").write_bytes,
                    buf.getvalue().encode("utf8"),
                )

            with StringIO() as buf:
                resource_spec.write_to_file(buf)
                for dev_type, device_alloc in resource_spec.allocations.items():
                    device_plugin = self.computers[dev_type].instance
                    kvpairs = await device_plugin.generate_resource_data(device_alloc)
                    for k, v in kvpairs.items():
                        buf.write(f"{k}={v}\n")
                await loop.run_in_executor(
                    None,
                    (self.config_dir / "resource.txt").write_bytes,
                    buf.getvalue().encode("utf8"),
                )

        shutil.copyfile(self.config_dir / "environ.txt", self.config_dir / "environ_base.txt")
        shutil.copyfile(self.config_dir / "resource.txt", self.config_dir / "resource_base.txt")

        # TODO: refactor out dotfiles/sshkey initialization to the base agent?
        docker_creds = self.internal_data.get("docker_credentials")
        if docker_creds:
            await loop.run_in_executor(
                None,
                (self.config_dir / "docker-creds.json").write_bytes,
                dump_json(docker_creds),
            )

        # Create SSH keypair only if ssh_keypair internal_data exists and
        # /home/work/.ssh folder is not mounted.
        if self.internal_data.get("ssh_keypair"):
            for mount in resource_spec.mounts:
                container_path = str(mount).split(":")[1]
                if container_path == "/home/work/.ssh":
                    break
            else:
                pubkey = self.internal_data["ssh_keypair"]["public_key"].encode("ascii")
                privkey = self.internal_data["ssh_keypair"]["private_key"].encode("ascii")
                ssh_dir = self.work_dir / ".ssh"

                def _populate_ssh_config():
                    ssh_dir.mkdir(parents=True, exist_ok=True)
                    ssh_dir.chmod(0o700)
                    (ssh_dir / "authorized_keys").write_bytes(pubkey)
                    (ssh_dir / "authorized_keys").chmod(0o600)
                    if not (ssh_dir / "id_rsa").is_file():
                        (ssh_dir / "id_rsa").write_bytes(privkey)
                        (ssh_dir / "id_rsa").chmod(0o600)
                    (self.work_dir / "id_container").write_bytes(privkey)
                    (self.work_dir / "id_container").chmod(0o600)

                    def chown_idfile(uid: Optional[int], gid: Optional[int]) -> None:
                        paths = [
                            ssh_dir,
                            ssh_dir / "authorized_keys",
                            ssh_dir / "id_rsa",
                            self.work_dir / "id_container",
                        ]
                        self._chown_paths_if_root(paths, uid, gid)

                    if ouid is not None or ogid is not None:
                        chown_idfile(ouid, ogid)
                    else:
                        if KernelFeatures.UID_MATCH in self.kernel_features:
                            chown_idfile(
                                self.local_config["container"]["kernel-uid"],
                                self.local_config["container"]["kernel-gid"],
                            )

                await loop.run_in_executor(None, _populate_ssh_config)

        # higher priority dotfiles are stored last to support overwriting
        for dotfile in self.internal_data.get("dotfiles", []):
            if dotfile["path"].startswith("/"):
                if dotfile["path"].startswith("/home/"):
                    path_arr = dotfile["path"].split("/")
                    file_path: Path = self.scratch_dir / "/".join(path_arr[2:])
                else:
                    file_path = Path(dotfile["path"])
            else:
                file_path = self.work_dir / dotfile["path"]
            file_path.parent.mkdir(parents=True, exist_ok=True)

            dotfile_content = dotfile["data"]
            if not dotfile_content.endswith("\n"):
                dotfile_content += "\n"
            await loop.run_in_executor(None, file_path.write_text, dotfile_content)

            tmp = Path(file_path)
            tmp_paths: list[Path] = []
            while tmp != self.work_dir:
                tmp.chmod(int(dotfile["perm"], 8))
                tmp_paths.append(tmp)
                tmp = tmp.parent
            if ouid is not None or ogid is not None:
                self._chown_paths_if_root(tmp_paths, ouid, ogid)
            else:
                if KernelFeatures.UID_MATCH in self.kernel_features:
                    self._chown_paths_if_root(
                        tmp_paths,
                        self.local_config["container"]["kernel-uid"],
                        self.local_config["container"]["kernel-gid"],
                    )

        kernel_obj = DockerKernel(
            self.ownership_data,
            self.kernel_config["network_id"],
            self.image_ref,
            self.kspec_version,
            cluster_info["network_config"].get("mode", "bridge"),
            agent_config=self.local_config,
            service_ports=service_ports,
            resource_spec=resource_spec,
            environ=environ,
            data={},
        )
        return kernel_obj

    @property
    @override
    def repl_ports(self) -> Sequence[int]:
        return (2000, 2001)

    @property
    @override
    def protected_services(self) -> Sequence[str]:
        rgtype: ResourceGroupType = self.local_config["agent"]["scaling-group-type"]
        match rgtype:
            case ResourceGroupType.COMPUTE:
                return ()
            case ResourceGroupType.STORAGE:
                return ("ttyd",)

    async def _apply_seccomp_profile(self, container_config: MutableMapping[str, Any]) -> None:
        default_seccomp_path = self.resolve_krunner_filepath("runner/default-seccomp.json")

        if not default_seccomp_path.exists():
            log.warning(
                "Default seccomp profile file not found in the expected path! Skipped the application of additional syscalls."
            )
            return

        async with aiofiles.open(default_seccomp_path, mode="r") as fp:
            seccomp_profile = load_json(await fp.read())

            additional_allowed_syscalls = self.additional_allowed_syscalls
            additional_allowed_syscall_rule = {
                "names": additional_allowed_syscalls,
                "action": "SCMP_ACT_ALLOW",
                "args": [],
                "comment": "Additionally allowed syscalls by Backend.AI Agent",
            }
            seccomp_profile["syscalls"].append(additional_allowed_syscall_rule)

            container_config["HostConfig"]["SecurityOpt"] = [
                f"seccomp={json.dumps(seccomp_profile)}"
            ]

    async def start_container(
        self,
        kernel_obj: AbstractKernel,
        cmdargs: List[str],
        resource_opts,
        preopen_ports,
        cluster_info: ClusterInfo,
    ) -> Mapping[str, Any]:
        loop = current_loop()
        resource_spec = kernel_obj.resource_spec
        service_ports = kernel_obj.service_ports
        environ = kernel_obj.environ
        image_labels = self.kernel_config["image"]["labels"]

        # PHASE 4: Run!
        container_bind_host = self.local_config["container"]["bind-host"]
        advertised_kernel_host = self.local_config["container"].get("advertised-host")
        if len(service_ports) + len(self.repl_ports) > len(self.port_pool):
            raise RuntimeError(
                f"Container ports are not sufficiently available. (remaining ports: {self.port_pool})"
            )
        exposed_ports = [*self.repl_ports]
        host_ports = [self.port_pool.pop() for _ in self.repl_ports]
        host_ips = []
        for sport in service_ports:
            exposed_ports.extend(sport["container_ports"])
            if (
                sport["name"] == "sshd"
                and self.cluster_ssh_port_mapping
                and (
                    ssh_host_port := self.cluster_ssh_port_mapping.get(
                        self.kernel_config["cluster_hostname"]
                    )
                )
            ):
                host_ports.append(ssh_host_port[1])
            else:
                hport = self.port_pool.pop()
                host_ports.append(hport)
        protected_service_ports: set[int] = set()
        for sport in service_ports:
            if sport["name"] in self.protected_services:
                protected_service_ports.update(sport["container_ports"])
        for eport in exposed_ports:
            if eport in self.repl_ports:  # always protected
                host_ips.append("127.0.0.1")
            elif eport in protected_service_ports:  # check if protected by resource group type
                host_ips.append("127.0.0.1")
            else:
                host_ips.append(str(container_bind_host))
        assert len(host_ips) == len(host_ports) == len(exposed_ports)

        if (mode := cluster_info["network_config"].get("mode")) and mode != "bridge":
            try:
                plugin = self.network_plugin_ctx.plugins[mode]
            except KeyError:
                raise RuntimeError(f"Network plugin {mode} not loaded!")
            if ContainerNetworkCapability.GLOBAL in (await plugin.get_capabilities()):
                await plugin.prepare_port_forward(
                    kernel_obj,
                    str(container_bind_host),
                    [
                        (host_port, container_port)
                        for host_port, container_port in zip(host_ports, exposed_ports)
                    ],
                )

        container_log_size = self.local_config["agent"]["container-logs"]["max-length"]
        container_log_file_count = 5
        container_log_file_size = BinarySize(container_log_size // container_log_file_count)

        if self.image_ref.is_local:
            image = self.image_ref.short
        else:
            image = self.image_ref.canonical

        container_config: MutableMapping[str, Any] = {
            "Image": image,
            "Tty": True,
            "OpenStdin": True,
            "Privileged": False,
            "StopSignal": "SIGINT",
            "ExposedPorts": {f"{port}/tcp": {} for port in exposed_ports},
            "EntryPoint": ["/opt/kernel/entrypoint.sh"],
            "Cmd": cmdargs,
            "Env": [f"{k}={v}" for k, v in environ.items()],
            "WorkingDir": "/home/work",
            "Hostname": self.kernel_config["cluster_hostname"],
            "Labels": {
                LabelName.KERNEL_ID: str(self.kernel_id),
                LabelName.SESSION_ID: str(self.session_id),
                LabelName.OWNER_USER: self.ownership_data.owner_user_id_to_str,
                LabelName.OWNER_PROJECT: self.ownership_data.owner_project_id_to_str,
                LabelName.OWNER_AGENT: str(self.agent_id),
                LabelName.BLOCK_SERVICE_PORTS: (
                    "1" if self.internal_data.get("block_service_ports", False) else "0"
                ),
            },
            "HostConfig": {
                "Init": True,
                "PortBindings": {
                    f"{eport}/tcp": [{"HostPort": str(hport), "HostIp": hip}]
                    for eport, hport, hip in zip(exposed_ports, host_ports, host_ips)
                },
                "PublishAllPorts": False,  # we manage port mapping manually!
                "CapAdd": [
                    "IPC_LOCK",  # for hugepages and RDMA
                    "SYS_NICE",  # for NFS based GPUDirect Storage
                ],
                "Ulimits": [
                    {"Name": "nofile", "Soft": 1048576, "Hard": 1048576},
                    {"Name": "memlock", "Soft": -1, "Hard": -1},
                ],
                "LogConfig": {
                    "Type": "local",  # for efficient docker-specific storage
                    "Config": {
                        # these fields must be str
                        # (ref: https://docs.docker.com/config/containers/logging/local/)
                        "max-size": f"{container_log_file_size:s}",
                        "max-file": str(container_log_file_count),
                        "compress": "false",
                    },
                },
            },
        }

        await self._apply_seccomp_profile(container_config)

        # merge all container configs generated during prior preparation steps
        for c in self.container_configs:
            update_nested_dict(container_config, c)
        if self.local_config["container"]["sandbox-type"] == "jail":
            update_nested_dict(
                container_config,
                {
                    "HostConfig": {
                        "SecurityOpt": ["seccomp=unconfined", "apparmor=unconfined"],
                        "CapAdd": ["SYS_PTRACE"],
                    },
                },
            )

        if resource_opts and resource_opts.get("shmem"):
            shmem = int(resource_opts.get("shmem", "0"))
            self.computer_docker_args["HostConfig"]["ShmSize"] = shmem
            self.computer_docker_args["HostConfig"]["MemorySwap"] -= shmem
            self.computer_docker_args["HostConfig"]["Memory"] -= shmem

        service_ports_label: list[str] = []
        service_ports_label += image_labels.get(LabelName.SERVICE_PORTS, "").split(",")
        service_ports_label += [f"{port_no}:preopen:{port_no}" for port_no in preopen_ports]

        container_config["Labels"][LabelName.SERVICE_PORTS] = ",".join([
            label for label in service_ports_label if label
        ])
        update_nested_dict(container_config, self.computer_docker_args)
        kernel_name = f"kernel.{self.image_ref.name.split('/')[-1]}.{self.kernel_id}"

        # optional local override of docker config
        extra_container_opts_name = "agent-docker-container-opts.json"
        for extra_container_opts_file in [
            Path("/etc/backend.ai") / extra_container_opts_name,
            Path.home() / ".config" / "backend.ai" / extra_container_opts_name,
            Path.cwd() / extra_container_opts_name,
        ]:
            if extra_container_opts_file.is_file():
                try:
                    extra_container_opts = load_json(extra_container_opts_file.read_bytes())
                    update_nested_dict(container_config, extra_container_opts)
                except IOError:
                    pass

        # The final container config is settled down here.
        if self.local_config["debug"]["log-kernel-config"]:
            log.debug("full container config: {!r}", pretty(container_config))

        async def _rollback_container_creation() -> None:
            await _clean_scratch(
                loop,
                self.local_config["container"]["scratch-type"],
                self.local_config["container"]["scratch-root"],
                self.kernel_id,
            )
            self.port_pool.update(host_ports)
            async with self.resource_lock:
                for dev_name, device_alloc in resource_spec.allocations.items():
                    self.computers[dev_name].alloc_map.free(device_alloc)

        # We are all set! Create and start the container.
        async with closing_async(Docker()) as docker:
            container: Optional[DockerContainer] = None
            try:
                container = await docker.containers.create(
                    config=container_config, name=kernel_name
                )
                assert container is not None
                cid = cast(str, container._id)
                async with AsyncFileWriter(
                    target_filename=self.config_dir / "resource.txt",
                    access_mode="a",
                ) as writer:
                    await writer.write(f"CID={cid}\n")

            except asyncio.CancelledError:
                if container is not None:
                    raise ContainerCreationError(
                        container_id=container._id, message="Container creation cancelled"
                    )
                raise
            except Exception as e:
                # Oops, we have to restore the allocated resources!
                await _rollback_container_creation()
                if container is not None:
                    raise ContainerCreationError(
                        container_id=container._id, message=f"unknown. {repr(e)}"
                    )
                raise

            try:
                await container.start()
            except asyncio.CancelledError:
                await _rollback_container_creation()
                raise ContainerCreationError(container_id=cid, message="Container start cancelled")
            except Exception as e:
                await _rollback_container_creation()
                raise ContainerCreationError(container_id=cid, message=f"unknown. {repr(e)}")

            if self.internal_data.get("sudo_session_enabled", False):
                exec = await container.exec(
                    [
                        # file ownership is guaranteed to be set as root:root since command is executed on behalf of root user
                        "sh",
                        "-c",
                        'mkdir -p /etc/sudoers.d && echo "work ALL=(ALL:ALL) NOPASSWD:ALL" > /etc/sudoers.d/01-bai-work',
                    ],
                    user="root",
                )
                shell_response = await exec.start(detach=True)
                if shell_response:
                    await _rollback_container_creation()
                    raise ContainerCreationError(
                        container_id=cid,
                        message=f"sudoers provision failed: {shell_response.decode()}",
                    )

            additional_network_names: Set[str] = set()
            for dev_name, device_alloc in resource_spec.allocations.items():
                n = await self.computers[dev_name].instance.get_docker_networks(device_alloc)
                additional_network_names |= set(n)

            for name in additional_network_names:
                network = await docker.networks.get(name)
                await network.connect({"Container": container._id})

            kernel_obj.container_id = container._id
            container_network_info: ContainerNetworkInfo | None = None
            if (mode := cluster_info["network_config"].get("mode")) and mode != "bridge":
                try:
                    plugin = self.network_plugin_ctx.plugins[mode]
                except KeyError:
                    raise RuntimeError(f"Network plugin {mode} not loaded!")
                if ContainerNetworkCapability.GLOBAL in (await plugin.get_capabilities()):
                    container_network_info = await plugin.expose_ports(
                        kernel_obj,
                        str(container_bind_host),
                        [
                            (host_port, container_port)
                            for host_port, container_port in zip(host_ports, exposed_ports)
                        ],
                    )

            created_host_ports: Tuple[int, ...]
            repl_in_port = 0
            repl_out_port = 0
            if container_network_info:
                kernel_host = container_network_info.container_host
                port_map = container_network_info.services
                assert "replin" in port_map and "replout" in port_map

                repl_in_port = port_map["replin"][2000]
                repl_out_port = port_map["replout"][2001]
                stdin_port = 0  # left for legacy
                stdout_port = 0  # left for legacy

                for sport in service_ports:
                    created_host_ports = tuple(
                        port_map[sport["name"]][cport] for cport in sport["container_ports"]
                    )
                    sport["host_ports"] = created_host_ports
            else:
                kernel_host = advertised_kernel_host or container_bind_host
                ctnr_host_port_map: MutableMapping[int, int] = {}
                stdin_port = 0
                stdout_port = 0
                for idx, port in enumerate(exposed_ports):
                    ports: list[PortInfo] | None = await container.port(port)
                    if ports is None:
                        raise ContainerCreationError(
                            container_id=cid, message="Container port not found"
                        )
                    host_port = int(ports[0]["HostPort"])
                    if host_port != host_ports[idx]:
                        await _rollback_container_creation()
                        raise ContainerCreationError(
                            container_id=cid,
                            message=f"Port mapping mismatch. {host_port = }, {host_ports[idx] = }",
                        )
                    assert host_port == host_ports[idx]
                    if port == 2000:  # intrinsic
                        repl_in_port = host_port
                    elif port == 2001:  # intrinsic
                        repl_out_port = host_port
                    elif port == 2002:  # legacy
                        stdin_port = host_port
                    elif port == 2003:  # legacy
                        stdout_port = host_port
                    else:
                        ctnr_host_port_map[port] = host_port
                for sport in service_ports:
                    created_host_ports = tuple(
                        ctnr_host_port_map[cport] for cport in sport["container_ports"]
                    )
                    sport["host_ports"] = created_host_ports

        assert repl_in_port != 0, "repl_in_port should have been assigned."
        assert repl_out_port != 0, "repl_out_port should have been assigned."
        return {
            "container_id": container._id,
            "kernel_host": kernel_host,
            "repl_in_port": repl_in_port,
            "repl_out_port": repl_out_port,
            "stdin_port": stdin_port,  # legacy
            "stdout_port": stdout_port,  # legacy
            "host_ports": host_ports,
            "domain_socket_proxies": self.domain_socket_proxies,
            "block_service_ports": self.internal_data.get("block_service_ports", False),
        }


class DockerAgent(AbstractAgent[DockerKernel, DockerKernelCreationContext]):
    docker_info: Mapping[str, Any]
    monitor_docker_task: asyncio.Task
    agent_sockpath: Path
    agent_sock_task: asyncio.Task
    metadata_server: MetadataServer
    docker_ptask_group: aiotools.PersistentTaskGroup
    gwbridge_subnet: Optional[str]
    checked_invalid_images: Set[str]

    network_plugin_ctx: NetworkPluginContext

    def __init__(
        self,
        etcd: AsyncEtcd,
        local_config: Mapping[str, Any],
        *,
        stats_monitor: StatsPluginContext,
        error_monitor: ErrorPluginContext,
        skip_initial_scan: bool = False,
        agent_public_key: Optional[PublicKey],
    ) -> None:
        super().__init__(
            etcd,
            local_config,
            stats_monitor=stats_monitor,
            error_monitor=error_monitor,
            skip_initial_scan=skip_initial_scan,
            agent_public_key=agent_public_key,
        )
        self.checked_invalid_images = set()

    async def __ainit__(self) -> None:
        async with closing_async(Docker()) as docker:
            docker_host = ""
            match docker.connector:
                case aiohttp.TCPConnector():
                    assert docker.docker_host is not None
                    docker_host = docker.docker_host
                case aiohttp.NamedPipeConnector() | aiohttp.UnixConnector() as connector:
                    docker_host = connector.path
                case _:
                    docker_host = "(unknown)"
            log.info("accessing the local Docker daemon via {}", docker_host)
            docker_version = await docker.version()
            log.info(
                "running with Docker {0} with API {1}",
                docker_version["Version"],
                docker_version["ApiVersion"],
            )
            kernel_version = docker_version["KernelVersion"]
            if "linuxkit" in kernel_version:
                self.local_config["agent"]["docker-mode"] = "linuxkit"
            else:
                self.local_config["agent"]["docker-mode"] = "native"
            docker_info = await docker.system.info()
            docker_info = dict(docker_info)
            # Assume cgroup v1 if CgroupVersion key is absent
            if "CgroupVersion" not in docker_info:
                docker_info["CgroupVersion"] = "1"
            log.info(
                "Cgroup Driver: {0}, Cgroup Version: {1}",
                docker_info["CgroupDriver"],
                docker_info["CgroupVersion"],
            )
            self.docker_info = docker_info
        await super().__ainit__()
        try:
            async with Docker() as docker:
                gwbridge = await docker.networks.get("docker_gwbridge")
                gwbridge_info = await gwbridge.show()
                self.gwbridge_subnet = gwbridge_info["IPAM"]["Config"][0]["Subnet"]
        except (DockerError, KeyError, IndexError):
            self.gwbridge_subnet = None
        ipc_base_path = self.local_config["agent"]["ipc-base-path"]
        (ipc_base_path / "container").mkdir(parents=True, exist_ok=True)
        self.agent_sockpath = ipc_base_path / "container" / f"agent.{self.local_instance_id}.sock"
        # Workaround for Docker Desktop for Mac's UNIX socket mount failure with virtiofs
        if sys.platform != "darwin":
            socket_relay_name = f"backendai-socket-relay.{self.local_instance_id}"
            socket_relay_container = PersistentServiceContainer(
                "backendai-socket-relay:latest",
                {
                    "Cmd": [
                        f"UNIX-LISTEN:/ipc/{self.agent_sockpath.name},unlink-early,fork,mode=777",
                        f"TCP-CONNECT:127.0.0.1:{self.local_config['agent']['agent-sock-port']}",
                    ],
                    "HostConfig": {
                        "Mounts": [
                            {
                                "Type": "bind",
                                "Source": str(ipc_base_path / "container"),
                                "Target": "/ipc",
                            },
                        ],
                        "NetworkMode": "host",
                    },
                },
                name=socket_relay_name,
            )
            await socket_relay_container.ensure_running_latest()
        self.agent_sock_task = asyncio.create_task(self.handle_agent_socket())
        self.monitor_docker_task = asyncio.create_task(self.monitor_docker_events())
        self.docker_ptask_group = aiotools.PersistentTaskGroup()

        self.metadata_server = await MetadataServer.new(
            self.local_config,
            self.etcd,
            self.kernel_registry,
        )
        await self.metadata_server.start_server()
        # For legacy accelerator plugins
        self.docker = Docker()

        self.network_plugin_ctx = NetworkPluginContext(self.etcd, self.local_config)
        await self.network_plugin_ctx.init(
            context=self,
            allowlist=self.local_config["agent"]["allow-network-plugins"],
            blocklist=self.local_config["agent"]["block-network-plugins"],
        )

    async def shutdown(self, stop_signal: signal.Signals):
        # Stop handling agent sock.
        if self.agent_sock_task is not None:
            self.agent_sock_task.cancel()
            await self.agent_sock_task
        if self.docker_ptask_group is not None:
            await self.docker_ptask_group.shutdown()

        try:
            await super().shutdown(stop_signal)
        finally:
            # Stop docker event monitoring.
            if self.monitor_docker_task is not None:
                self.monitor_docker_task.cancel()
                await self.monitor_docker_task

        await self.metadata_server.cleanup()
        if self.docker:
            await self.docker.close()

    def get_cgroup_path(self, controller: str, container_id: str) -> Path:
        driver = self.docker_info["CgroupDriver"]
        version = self.docker_info["CgroupVersion"]
        mount_point = get_cgroup_mount_point(version, controller)
        # See https://docs.docker.com/config/containers/runmetrics/#find-the-cgroup-for-a-given-container
        match driver:
            case "cgroupfs":
                cgroup = f"docker/{container_id}"
            case "systemd":
                cgroup = f"system.slice/docker-{container_id}.scope"
            case _:
                raise ValueError(f"Unsupported cgroup driver: {driver!r}")
        return mount_point / cgroup

    async def load_resources(self) -> Mapping[DeviceName, AbstractComputePlugin]:
        return await load_resources(self.etcd, self.local_config)

    async def scan_available_resources(self) -> Mapping[SlotName, Decimal]:
        return await scan_available_resources(
            self.local_config, {name: cctx.instance for name, cctx in self.computers.items()}
        )

    async def extract_image_command(self, image: str) -> str | None:
        async with closing_async(Docker()) as docker:
            result = await docker.images.get(image)
            return result["Config"].get("Cmd")

    async def enumerate_containers(
        self,
        status_filter: FrozenSet[ContainerStatus] = ACTIVE_STATUS_SET,
    ) -> Sequence[Tuple[KernelId, Container]]:
        result = []
        fetch_tasks = []
        async with closing_async(Docker()) as docker:
            for container in await docker.containers.list():

                async def _fetch_container_info(container):
                    kernel_id = "(unknown)"
                    try:
                        kernel_id = await get_kernel_id_from_container(container)
                        if kernel_id is None:
                            return
                        if container["State"]["Status"] in status_filter:
                            owner_id = AgentId(
                                container["Config"]["Labels"].get(LabelName.OWNER_AGENT, "")
                            )
                            if self.id == owner_id:
                                await container.show()
                                result.append(
                                    (
                                        kernel_id,
                                        container_from_docker_container(container),
                                    ),
                                )
                    except asyncio.CancelledError:
                        pass
                    except Exception:
                        log.exception(
                            "error while fetching container information (cid:{}, k:{})",
                            container._id,
                            kernel_id,
                        )

                fetch_tasks.append(_fetch_container_info(container))

            await asyncio.gather(*fetch_tasks, return_exceptions=True)
        return result

    async def resolve_image_distro(self, image: ImageConfig) -> str:
        image_labels = image["labels"]
        distro = image_labels.get(LabelName.BASE_DISTRO)
        if distro:
            return distro

        async with Docker() as docker:
            image_id = image["digest"].partition(":")[-1]
            # check if distro data is available on redis cache
            cached_distro = await redis_helper.execute(
                self.redis_stat_pool, lambda r: r.get(f"image:{image_id}:distro")
            )
            if cached_distro:
                return cached_distro.decode()

            container_config: dict[str, Any] = {
                "Image": image["canonical"],
                "Tty": True,
                "Privileged": False,
                "AttachStdin": False,
                "AttachStdout": True,
                "AttachStderr": True,
                "HostConfig": {
                    "Init": True,
                },
                "Entrypoint": [""],
                "Cmd": ["ldd", "--version"],
            }

            container = await docker.containers.create(container_config)
            await container.start()
            await container.wait()  # wait until container finishes to prevent race condition
            container_log = await container.log(stdout=True, stderr=True, follow=False)
            await container.stop()
            await container.delete()
            log.debug("response: {}", container_log)
            version_lines = container_log[0].splitlines()
            if m := LDD_GLIBC_REGEX.search(version_lines[0]):
                version = float(m.group(1))
                if version in known_glibc_distros:
                    distro = known_glibc_distros[version]
                else:
                    for idx, known_version in enumerate(known_glibc_distros.keys()):
                        if version < known_version:
                            distro = list(known_glibc_distros.values())[idx - 1]
                            break
                    else:
                        distro = list(known_glibc_distros.values())[-1]
            elif m := LDD_MUSL_REGEX.search(version_lines[0]):
                distro = "alpine3.8"
            else:
                raise RuntimeError("Could not determine the C library variant.")
            await redis_helper.execute(
                self.redis_stat_pool, lambda r: r.set(f"image:{image_id}:distro", distro)
            )
            return distro

    async def scan_images(self) -> ScanImagesResult:
        async with closing_async(Docker()) as docker:
            all_images = await docker.images.list()
            scanned_images, removed_images = {}, {}
            for image in all_images:
                if image["RepoTags"] is None:
                    continue
                for repo_tag in image["RepoTags"]:
                    if repo_tag.endswith("<none>"):
                        continue
                    try:
                        ImageRef.parse_image_str(repo_tag, "*")
                    except (InvalidImageName, InvalidImageTag) as e:
                        if repo_tag not in self.checked_invalid_images:
                            log.warning(
                                "Image name {} does not conform to Backend.AI's image naming rule. This image will be ignored. Details: {}",
                                repo_tag,
                                e,
                            )
                            self.checked_invalid_images.add(repo_tag)
                        continue

                    img_detail = await docker.images.inspect(repo_tag)
                    labels = img_detail.get("Config", {}).get("Labels")
                    if labels is None:
                        continue
                    kernelspec = int(labels.get(LabelName.KERNEL_SPEC, "1"))
                    if MIN_KERNELSPEC <= kernelspec <= MAX_KERNELSPEC:
                        scanned_images[repo_tag] = img_detail["Id"]
            for added_image in scanned_images.keys() - self.images.keys():
                log.debug("found kernel image: {0}", added_image)

            for removed_image in self.images.keys() - scanned_images.keys():
                log.debug("removed kernel image: {0}", removed_image)
                removed_images[removed_image] = self.images[removed_image]

            return ScanImagesResult(
                scanned_images=scanned_images,
                removed_images=removed_images,
            )

    async def handle_agent_socket(self):
        """
        A simple request-reply socket handler for in-container processes.
        For ease of implementation in low-level languages such as C,
        it uses a simple C-friendly ZeroMQ-based multipart messaging protocol.

        The agent listens on a local TCP port and there is a socat relay
        that proxies this port via a UNIX domain socket mounted inside
        actual containers.  The reason for this is to avoid inode changes
        upon agent restarts by keeping the relay container running persistently,
        so that the mounted UNIX socket files don't get to refere a dangling pointer
        when the agent is restarted.

        Request message:
            The first part is the requested action as string,
            The second part and later are arguments.

        Reply message:
            The first part is a 32-bit integer (int in C)
                (0: success)
                (-1: generic unhandled error)
                (-2: invalid action)
            The second part and later are arguments.

        All strings are UTF-8 encoded.
        """
        terminating = False
        zmq_ctx = zmq.asyncio.Context()
        while True:
            agent_sock = zmq_ctx.socket(zmq.REP)
            try:
                agent_sock.bind(f"tcp://127.0.0.1:{self.local_config['agent']['agent-sock-port']}")
                while True:
                    msg = await agent_sock.recv_multipart()
                    if not msg:
                        break
                    try:
                        if msg[0] == b"host-pid-to-container-pid":
                            container_id = msg[1].decode()
                            host_pid = struct.unpack("i", msg[2])[0]
                            container_pid = await host_pid_to_container_pid(
                                container_id,
                                host_pid,
                            )
                            reply = [
                                struct.pack("i", 0),
                                struct.pack("i", container_pid),
                            ]
                        elif msg[0] == b"container-pid-to-host-pid":
                            container_id = msg[1].decode()
                            container_pid = struct.unpack("i", msg[2])[0]
                            host_pid = await container_pid_to_host_pid(container_id, container_pid)
                            reply = [
                                struct.pack("i", 0),
                                struct.pack("i", host_pid),
                            ]
                        elif msg[0] == b"is-jail-enabled":
                            reply = [
                                struct.pack("i", 0),
                                struct.pack(
                                    "i",
                                    (
                                        1
                                        if self.local_config["container"]["sandbox-type"] == "jail"
                                        else 0
                                    ),
                                ),
                            ]
                        else:
                            reply = [struct.pack("i", -2), b"Invalid action"]
                    except asyncio.CancelledError:
                        terminating = True
                        raise
                    except Exception as e:
                        log.exception("handle_agent_socket(): internal error")
                        reply = [struct.pack("i", -1), f"Error: {e}".encode("utf-8")]
                    await agent_sock.send_multipart(reply)
            except asyncio.CancelledError:
                terminating = True
                return
            except zmq.ZMQError:
                log.exception("handle_agent_socket(): zmq error")
                raise
            finally:
                agent_sock.close()
                if not terminating:
                    log.info("handle_agent_socket(): rebinding the socket")
                else:
                    zmq_ctx.destroy()

    async def push_image(
        self,
        image_ref: ImageRef,
        registry_conf: ImageRegistry,
        *,
        timeout: float | None | Sentinel = Sentinel.TOKEN,
    ) -> None:
        if image_ref.is_local:
            return
        auth_config = None
        reg_user = registry_conf.get("username")
        reg_passwd = registry_conf.get("password")
        log.info("pushing image {} to registry", image_ref.canonical)
        if reg_user and reg_passwd:
            encoded_creds = base64.b64encode(f"{reg_user}:{reg_passwd}".encode("utf-8")).decode(
                "ascii"
            )
            auth_config = {
                "auth": encoded_creds,
            }

        async with closing_async(Docker()) as docker:
            kwargs: dict[str, Any] = {"auth": auth_config}
            if timeout != Sentinel.TOKEN:
                kwargs["timeout"] = timeout
            result = await docker.images.push(image_ref.canonical, **kwargs)

            if not result:
                raise RuntimeError("Failed to push image: unexpected return value from aiodocker")
            elif error := result[-1].get("error"):
                raise RuntimeError(f"Failed to push image: {error}")

    async def pull_image(
        self,
        image_ref: ImageRef,
        registry_conf: ImageRegistry,
        *,
        timeout: float | None,
    ) -> None:
        auth_config = None
        reg_user = registry_conf.get("username")
        reg_passwd = registry_conf.get("password")
        if reg_user and reg_passwd:
            encoded_creds = base64.b64encode(f"{reg_user}:{reg_passwd}".encode("utf-8")).decode(
                "ascii"
            )
            auth_config = {
                "auth": encoded_creds,
            }
        log.info("pulling image {} from registry", image_ref.canonical)
        async with closing_async(Docker()) as docker:
            result = await docker.images.pull(
                image_ref.canonical, auth=auth_config, timeout=timeout
            )

            if not result:
                raise RuntimeError("Failed to pull image: unexpected return value from aiodocker")
            elif error := result[-1].get("error"):
                raise RuntimeError(f"Failed to pull image: {error}")

    async def _purge_image(self, docker: Docker, request: DockerPurgeImageReq) -> PurgeImageResp:
        try:
            await docker.images.delete(request.image, force=request.force, noprune=request.noprune)
            return PurgeImageResp.success(image=request.image)
        except Exception as e:
            log.error(f'Failed to purge image "{request.image}": {e}')
            return PurgeImageResp.failure(image=request.image, error=str(e))

    async def purge_images(self, request: PurgeImagesReq) -> PurgeImagesResp:
        async with closing_async(Docker()) as docker:
            async with TaskGroup() as tg:
                tasks = [
                    tg.create_task(
                        self._purge_image(
                            docker,
                            DockerPurgeImageReq(
                                image=image, force=request.force, noprune=request.noprune
                            ),
                        )
                    )
                    for image in request.images
                ]

        results = []
        for task in tasks:
            deleted_info = task.result()
            results.append(deleted_info)

        return PurgeImagesResp(responses=results)

    async def check_image(
        self, image_ref: ImageRef, image_id: str, auto_pull: AutoPullBehavior
    ) -> bool:
        try:
            async with closing_async(Docker()) as docker:
                image_info = await docker.images.inspect(image_ref.canonical)
                if auto_pull == AutoPullBehavior.DIGEST:
                    if image_info["Id"] != image_id:
                        return True
            log.info("found the local up-to-date image for {}", image_ref.canonical)
        except DockerError as e:
            if e.status == 404:
                if auto_pull == AutoPullBehavior.DIGEST:
                    return True
                elif auto_pull == AutoPullBehavior.TAG:
                    return True
                elif auto_pull == AutoPullBehavior.NONE:
                    raise ImageNotAvailable(image_ref)
            else:
                raise
        return False

    async def init_kernel_context(
        self,
        ownership_data: KernelOwnershipData,
        kernel_image: ImageRef,
        kernel_config: KernelCreationConfig,
        *,
        restarting: bool = False,
        cluster_ssh_port_mapping: Optional[ClusterSSHPortMapping] = None,
    ) -> DockerKernelCreationContext:
        distro = await self.resolve_image_distro(kernel_config["image"])
        return DockerKernelCreationContext(
            ownership_data,
            self.event_producer,
            kernel_image,
            kernel_config,
            distro,
            self.local_config,
            self.computers,
            self.port_pool,
            self.agent_sockpath,
            self.resource_lock,
            self.network_plugin_ctx,
            restarting=restarting,
            cluster_ssh_port_mapping=cluster_ssh_port_mapping,
            gwbridge_subnet=self.gwbridge_subnet,
        )

    async def restart_kernel__load_config(
        self,
        kernel_id: KernelId,
        name: str,
    ) -> bytes:
        loop = current_loop()
        scratch_dir = (self.local_config["container"]["scratch-root"] / str(kernel_id)).resolve()
        config_dir = scratch_dir / "config"
        return await loop.run_in_executor(
            None,
            (config_dir / name).read_bytes,
        )

    async def restart_kernel__store_config(
        self,
        kernel_id: KernelId,
        name: str,
        data: bytes,
    ) -> None:
        loop = current_loop()
        scratch_dir = (self.local_config["container"]["scratch-root"] / str(kernel_id)).resolve()
        config_dir = scratch_dir / "config"
        return await loop.run_in_executor(
            None,
            (config_dir / name).write_bytes,
            data,
        )

    async def destroy_kernel(
        self,
        kernel_id: KernelId,
        container_id: Optional[ContainerId],
    ) -> None:
        if container_id is None:
            return
        try:
            async with closing_async(Docker()) as docker:
                container = docker.containers.container(container_id)
                # The default timeout of the docker stop API is 10 seconds
                # to kill if container does not self-terminate.
                await container.stop()
        except DockerError as e:
            if e.status == 409 and "is not running" in e.message:
                # already dead
                log.warning("destroy_kernel(k:{0}) already dead", kernel_id)
                await self.reconstruct_resource_usage()
            elif e.status == 404:
                # missing
                log.warning(
                    "destroy_kernel(k:{0}) kernel missing, forgetting this kernel", kernel_id
                )
                await self.reconstruct_resource_usage()
            else:
                log.exception("destroy_kernel(k:{0}) kill error", kernel_id)
                await self.error_monitor.capture_exception()

    async def clean_kernel(
        self,
        kernel_id: KernelId,
        container_id: Optional[ContainerId],
        restarting: bool,
    ) -> None:
        loop = current_loop()
        async with closing_async(Docker()) as docker:
            if container_id is not None:
                container = docker.containers.container(container_id)

                async def log_iter():
                    it = container.log(
                        stdout=True,
                        stderr=True,
                        follow=True,
                    )
                    async with aiotools.aclosing(it):
                        async for line in it:
                            yield line.encode("utf-8")

                try:
                    with timeout(60):
                        await self.collect_logs(kernel_id, container_id, log_iter())
                except DockerError as e:
                    if e.status == 404:
                        log.warning(
                            "container is already cleaned or missing (k:{}, cid:{})",
                            kernel_id,
                            container_id,
                        )
                    else:
                        raise
                except asyncio.TimeoutError:
                    log.warning(
                        "timeout for collecting container logs (k:{}, cid:{})",
                        kernel_id,
                        container_id,
                    )
                except Exception as e:
                    log.warning(
                        "error while collecting container logs (k:{}, cid:{})",
                        kernel_id,
                        container_id,
                        exc_info=e,
                    )

            kernel_obj = self.kernel_registry.get(kernel_id)
            if kernel_obj is not None:
                for domain_socket_proxy in kernel_obj.get("domain_socket_proxies", []):
                    if domain_socket_proxy.proxy_server.is_serving():
                        domain_socket_proxy.proxy_server.close()
                        await domain_socket_proxy.proxy_server.wait_closed()
                        try:
                            domain_socket_proxy.host_proxy_path.unlink()
                        except IOError:
                            pass

            if (
                not self.local_config["debug"]["skip-container-deletion"]
                and container_id is not None
            ):
                container = docker.containers.container(container_id)
                try:
                    with timeout(90):
                        await container.delete(force=True, v=True)
                except DockerError as e:
                    if e.status == 409 and "already in progress" in e.message:
                        return
                    elif e.status == 404:
                        return
                    else:
                        log.exception(
                            "unexpected docker error while deleting container (k:{}, c:{})",
                            kernel_id,
                            container_id,
                        )
                except asyncio.TimeoutError:
                    log.warning("container deletion timeout (k:{}, c:{})", kernel_id, container_id)

            if not restarting:
                await _clean_scratch(
                    loop,
                    self.local_config["container"]["scratch-type"],
                    self.local_config["container"]["scratch-root"],
                    kernel_id,
                )
                if kernel_obj:
                    kernel = cast(DockerKernel, kernel_obj)
                    if kernel.network_driver != "bridge":
                        try:
                            plugin = self.network_plugin_ctx.plugins[kernel.network_driver]
                        except KeyError:
                            raise RuntimeError(
                                f"Network plugin {kernel.network_driver} not loaded!"
                            )
                        await plugin.leave_network(kernel)

    async def create_local_network(self, network_name: str) -> None:
        async with closing_async(Docker()) as docker:
            await docker.networks.create({
                "Name": network_name,
                "Driver": "bridge",
                "Labels": {
                    "ai.backend.cluster-network": "1",
                },
            })

    async def destroy_local_network(self, network_name: str) -> None:
        async with closing_async(Docker()) as docker:
            network = await docker.networks.get(network_name)
            await network.delete()

    @preserve_termination_log
    async def monitor_docker_events(self):
        async def handle_action_start(
            session_id: SessionId, kernel_id: KernelId, evdata: Mapping[str, Any]
        ) -> None:
            await self.inject_container_lifecycle_event(
                kernel_id,
                session_id,
                LifecycleEvent.START,
                KernelLifecycleEventReason.NEW_CONTAINER_STARTED,
                container_id=ContainerId(evdata["Actor"]["ID"]),
            )

        async def handle_action_die(
            session_id: SessionId, kernel_id: KernelId, evdata: Mapping[str, Any]
        ) -> None:
            # When containers die, we immediately clean up them.
            reason = None
            kernel_obj = self.kernel_registry.get(kernel_id)
            if kernel_obj is not None:
                reason = kernel_obj.termination_reason
            try:
                exit_code = evdata["Actor"]["Attributes"]["exitCode"]
            except KeyError:
                exit_code = 255
            await self.inject_container_lifecycle_event(
                kernel_id,
                session_id,
                LifecycleEvent.CLEAN,
                reason or KernelLifecycleEventReason.SELF_TERMINATED,
                container_id=ContainerId(evdata["Actor"]["ID"]),
                exit_code=exit_code,
            )

        async def handle_action_oom(
            session_id: SessionId, kernel_id: KernelId, evdata: Mapping[str, Any]
        ) -> None:
            kernel_obj = self.kernel_registry.get(kernel_id, None)
            if kernel_obj is None:
                return
            await kernel_obj.notify_event(
                AgentEventData(
                    type="oom",
                    data={},
                )
            )

        while True:
            async with closing_async(Docker()) as docker:
                subscriber = docker.events.subscribe(create_task=True)
                try:
                    while True:
                        try:
                            # ref: https://docs.docker.com/engine/api/v1.40/#operation/SystemEvents
                            evdata = await subscriber.get()
                            if evdata is None:
                                # Break out to the outermost loop when the connection is closed
                                log.info(
                                    "monitor_docker_events(): "
                                    "restarting aiodocker event subscriber",
                                )
                                break
                            if evdata["Type"] != "container":
                                # Our interest is the container-related events
                                continue
                            container_name = evdata["Actor"]["Attributes"]["name"]
                            kernel_id = await get_kernel_id_from_container(container_name)
                            if kernel_id is None:
                                continue
                            if self.local_config["debug"]["log-docker-events"] and evdata[
                                "Action"
                            ] in ("start", "die", "oom"):
                                log.debug(
                                    "docker-event: action={}, actor={}",
                                    evdata["Action"],
                                    evdata["Actor"],
                                )
                            session_id = SessionId(
                                UUID(evdata["Actor"]["Attributes"][LabelName.SESSION_ID])
                            )
                            match evdata["Action"]:
                                case "start":
                                    await asyncio.shield(
                                        self.docker_ptask_group.create_task(
                                            handle_action_start(session_id, kernel_id, evdata),
                                        )
                                    )
                                case "die":
                                    await asyncio.shield(
                                        self.docker_ptask_group.create_task(
                                            handle_action_die(session_id, kernel_id, evdata),
                                        )
                                    )
                                case "oom":
                                    await asyncio.shield(
                                        self.docker_ptask_group.create_task(
                                            handle_action_oom(session_id, kernel_id, evdata),
                                        )
                                    )
                        except asyncio.CancelledError:
                            # We are shutting down...
                            return
                        except Exception:
                            log.exception("monitor_docker_events(): unexpected error")
                finally:
                    await asyncio.shield(
                        self.docker_ptask_group.create_task(
                            docker.events.stop(),
                        )
                    )
