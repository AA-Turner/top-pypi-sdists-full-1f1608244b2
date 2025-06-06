"""Provides a hook to interact with a dbt project."""

from __future__ import annotations

import json
import logging
import sys
from abc import ABC
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Iterable,
    Iterator,
    NamedTuple,
    Optional,
    Tuple,
)
from urllib.parse import urlparse

from airflow.exceptions import AirflowException
from airflow.utils.log.logging_mixin import LoggingMixin

if sys.version_info >= (3, 11):
    from contextlib import chdir as chdir_ctx
else:
    from contextlib_chdir import chdir as chdir_ctx

if TYPE_CHECKING:
    from dbt.contracts.results import RunResult

    from airflow_dbt_python.hooks.fs import DbtFSHook
    from airflow_dbt_python.hooks.target import DbtConnectionHook
    from airflow_dbt_python.utils.configs import BaseConfig
    from airflow_dbt_python.utils.url import URLLike

    DbtFSHooksDict = Dict[Tuple[str, Optional[str]], DbtFSHook]


class DbtTaskResult(NamedTuple):
    """A tuple returned after a dbt task executes.

    Attributes:
        success: Whether the task succeeded or not.
        run_results: Results from the dbt task, if available.
        artifacts: A dictionary of saved dbt artifacts. It may be empty.
    """

    success: bool
    run_results: Optional[RunResult]
    artifacts: dict[str, Any]


class DbtTemporaryDirectory(TemporaryDirectory):
    """A wrapper on TemporaryDirectory for older versions of Python.

    Support for ignore_cleanup_errors was added in Python 3.10. There is a very obscure
    error that can happen when cleaning up a directory, even though everything should
    be cleaned. We would like to use ignore_cleanup_errors to provide clean up on a
    best-effort basis. For the time being, we are addressing this only for Python>=3.10.
    """

    def __init__(self, suffix=None, prefix=None, dir=None, ignore_cleanup_errors=True):
        if sys.version_info.minor < 10 and sys.version_info.major == 3:
            super().__init__(suffix=suffix, prefix=prefix, dir=dir)
        else:
            super().__init__(
                suffix=suffix,
                prefix=prefix,
                dir=dir,
                ignore_cleanup_errors=ignore_cleanup_errors,
            )


class DbtHook(ABC, LoggingMixin):
    """A hook to interact with dbt.

    Allows for running dbt tasks and provides required configurations for each task.
    """

    def __init__(
        self,
        *args,
        dbt_conn_id: Optional[str] = None,
        project_conn_id: Optional[str] = None,
        profiles_conn_id: Optional[str] = None,
        **kwargs,
    ):
        self.dbt_conn_id = dbt_conn_id
        self.project_conn_id = project_conn_id
        self.profiles_conn_id = profiles_conn_id
        super().__init__(*args, **kwargs)

    @staticmethod
    def get_dbt_target_hook(conn_id: str) -> DbtConnectionHook:
        """Get a hook to get a dbt profile based on the Airflow connection."""
        from .target import DbtConnectionHook

        return DbtConnectionHook.get_db_conn_hook(conn_id)

    @staticmethod
    def get_fs_hook(scheme: str, conn_id: Optional[str]) -> DbtFSHook:
        """Get a fs_hook to interact with dbt files.

        FSHooks are defined by the scheme we are looking for and an optional
        connection id if we are looking to interface with any Airflow hook that
        uses a connection.
        """
        from .fs import get_fs_hook

        return get_fs_hook(scheme, conn_id)

    def download_dbt_profiles(
        self,
        profiles_dir: URLLike,
        destination: URLLike,
    ) -> Path:
        """Pull a dbt profiles.yml file from a given profiles_dir.

        This operation is delegated to a DbtFSHook. An optional connection id is
        supported for remotes that require it.
        """
        scheme = urlparse(str(profiles_dir)).scheme
        fs_hook = self.get_fs_hook(scheme, self.profiles_conn_id)

        return fs_hook.download_dbt_profiles(profiles_dir, destination)

    def download_dbt_project(
        self,
        project_dir: URLLike,
        destination: URLLike,
    ) -> Path:
        """Pull a dbt project from a given project_dir.

        This operation is delegated to a DbtFSHook. An optional connection id is
        supported for remotes that require it.
        """
        scheme = urlparse(str(project_dir)).scheme
        fs_hook = self.get_fs_hook(scheme, self.project_conn_id)

        return fs_hook.download_dbt_project(project_dir, destination)

    def upload_dbt_project(
        self,
        project_dir: URLLike,
        destination: URLLike,
        replace: bool = False,
        delete_before: bool = False,
    ) -> None:
        """Push a dbt project from a given project_dir.

        This operation is delegated to a DbtFSHook. An optional connection id is
        supported for remotes that require it.
        """
        scheme = urlparse(str(destination)).scheme
        fs_hook = self.get_fs_hook(scheme, self.project_conn_id)

        return fs_hook.upload_dbt_project(
            project_dir, destination, replace=replace, delete_before=delete_before
        )

    def run_dbt_task(
        self,
        command: str,
        upload_dbt_project: bool = False,
        delete_before_upload: bool = False,
        replace_on_upload: bool = False,
        artifacts: Optional[Iterable[str]] = None,
        env_vars: Optional[Dict[str, Any]] = None,
        write_perf_info: bool = False,
        **kwargs,
    ) -> DbtTaskResult:
        """Run a dbt task with a given configuration and return the results.

        The configuration used determines the task that will be ran.

        Returns:
            A tuple containing a boolean indicating success and optionally the results
                of running the dbt command.
        """
        from dbt.adapters.factory import adapter_management
        from dbt.task.base import get_nearest_project_dir
        from dbt.task.clean import CleanTask
        from dbt.task.deps import DepsTask
        from dbt.tracking import track_run

        if self.dbt_conn_id:
            kwargs["target"] = self.dbt_conn_id
            target_hook = self.get_dbt_target_hook(self.dbt_conn_id)
            extra_target = target_hook.get_dbt_target_from_connection()
        else:
            extra_target = None

        config = self.get_dbt_task_config(command, **kwargs)

        with self.dbt_directory(
            config,
            upload_dbt_project=upload_dbt_project,
            delete_before_upload=delete_before_upload,
            replace_on_upload=replace_on_upload,
            env_vars=env_vars,
        ) as dbt_dir:
            # When creating tasks via from_args, dbt switches to the project directory.
            # We have to do that here as we are not using from_args.
            nearest_project_dir = get_nearest_project_dir(config.project_dir)

            with chdir_ctx(nearest_project_dir):
                with adapter_management():
                    task, runtime_config = config.create_dbt_task(
                        extra_target, write_perf_info
                    )
                    requires_profile = isinstance(task, (CleanTask, DepsTask))

                    self.setup_dbt_logging(config.debug)

                    if runtime_config is not None and not requires_profile:
                        # The deps command installs the dependencies, which means they
                        # may not exist before deps runs and the following would raise a
                        # CompilationError.
                        runtime_config.load_dependencies()

                    with track_run(task):
                        results = task.run()
                    success = task.interpret_results(results)

                if artifacts is None:
                    return DbtTaskResult(success, results, {})

                saved_artifacts = {}
                for artifact in artifacts:
                    artifact_path = Path(dbt_dir) / "target" / artifact

                    if not artifact_path.exists():
                        self.log.warning(
                            "Required dbt artifact %s was not found. "
                            "Perhaps dbt failed and couldn't generate it.",
                            artifact,
                        )
                        continue

                    with open(artifact_path) as artifact_file:
                        json_artifact = json.load(artifact_file)

                    saved_artifacts[artifact] = json_artifact

        return DbtTaskResult(success, results, saved_artifacts)

    def get_dbt_task_config(self, command: str, **config_kwargs) -> BaseConfig:
        """Initialize a configuration for given dbt command with given kwargs."""
        from airflow_dbt_python.utils.configs import ConfigFactory

        return ConfigFactory.from_str(command).create_config(**config_kwargs)

    @contextmanager
    def dbt_directory(
        self,
        config,
        upload_dbt_project: bool = False,
        delete_before_upload: bool = False,
        replace_on_upload: bool = False,
        env_vars: Optional[Dict[str, Any]] = None,
    ) -> Iterator[str]:
        """Provides a temporary directory to execute dbt.

        Creates a temporary directory for dbt to run in and prepares the dbt files
        if they need to be pulled from S3. If a S3 backend is being used, and
        self.upload_dbt_project is True, before leaving the temporary directory, we push
        back the project to S3. Pushing back a project enables commands like deps or
        docs generate.

        Yields:
            The temporary directory's name.
        """
        from airflow_dbt_python.utils.env import update_environment

        store_profiles_dir = config.profiles_dir
        store_project_dir = config.project_dir

        with update_environment(env_vars):
            with DbtTemporaryDirectory(prefix="airflow_tmp") as tmp_dir:
                self.log.info("Initializing temporary directory: %s", tmp_dir)

                try:
                    project_dir, profiles_dir = self.prepare_directory(
                        tmp_dir,
                        store_project_dir,
                        store_profiles_dir,
                    )
                except Exception as e:
                    raise AirflowException(
                        "Failed to prepare temporary directory for dbt execution"
                    ) from e

                config.project_dir = project_dir
                config.profiles_dir = profiles_dir

                if getattr(config, "state", None) is not None:
                    state = Path(getattr(config, "state", ""))
                    # Since we are running in a temporary directory, we need to make
                    # state paths relative to this temporary directory.
                    if not state.is_absolute():
                        setattr(config, "state", str(Path(tmp_dir) / state))

                yield tmp_dir

                if upload_dbt_project is True:
                    self.log.info("Uploading dbt project to: %s", store_project_dir)
                    self.upload_dbt_project(
                        tmp_dir,
                        store_project_dir,
                        replace=replace_on_upload,
                        delete_before=delete_before_upload,
                    )

        config.profiles_dir = store_profiles_dir
        config.project_dir = store_project_dir

    def prepare_directory(
        self,
        tmp_dir: str,
        project_dir: URLLike,
        profiles_dir: Optional[URLLike] = None,
    ) -> tuple[str, Optional[str]]:
        """Prepares a dbt directory for execution of a dbt task.

        Preparation involves downloading the required dbt project files and
        profiles.yml.
        """
        project_dir_path = self.download_dbt_project(
            project_dir,
            tmp_dir,
        )

        if profiles_dir is not None:
            profiles_file_path = self.download_dbt_profiles(
                profiles_dir,
                tmp_dir,
            )
            profiles_dir_path = profiles_file_path.parent
        elif (project_dir_path / "profiles.yml").exists():
            profiles_dir_path = project_dir_path
        else:
            profiles_dir_path = None

        return (
            str(project_dir_path),
            str(profiles_dir_path) if profiles_dir_path is not None else None,
        )

    def setup_dbt_logging(self, debug: Optional[bool]):
        """Setup dbt logging.

        Starting with dbt v1, dbt initializes two loggers: default_file and
        default_stdout. As these are initialized by the CLI app, we need to
        initialize them here.
        """
        from dbt.events.logging import setup_event_logger
        from dbt.flags import get_flags

        flags = get_flags()
        setup_event_logger(flags)

        configured_file = logging.getLogger("configured_file")
        file_log = logging.getLogger("file_log")
        stdout_log = logging.getLogger("stdout_log")
        stdout_log.handlers.clear()
        stdout_log.propagate = True

        if not debug:
            # We have to do this after setting logs up as dbt hasn't
            # configured the loggers before the call to setup_event_logger.
            # In the future, handlers may also be cleared or setup to use Airflow's.
            file_log.setLevel("INFO")
            file_log.propagate = False
            configured_file.setLevel("INFO")
            configured_file.propagate = False
