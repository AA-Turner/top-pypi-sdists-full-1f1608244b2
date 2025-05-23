import importlib
import json
import logging
import os
import re
import subprocess
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from airflow.exceptions import AirflowException
from airflow.models import BaseOperator
from airflow.utils.context import Context

from airflow_mcd.hooks import SessionHook

from pycarlo.core import Client
from pycarlo.features.dbt import DbtImporter

logger = logging.getLogger(__name__)


class DbtConfig:
    """
    Configuration for the execution of a dbt operator.

    :param mc_conn_id: Identifier of Monte Carlo connection configured in Airflow
    :param mc_include_logs: If `True`, write a copy of the logs generated by the dbt command to a local file and include with artifacts sent to Monte Carlo
    :param dir: The directory to run the CLI in
    :param dbt_bin: The `dbt` CLI. Defaults to `dbt`, so assumes it's on your `PATH`
    :param env: Optional environment variables to add to dbt command execution
    :param profiles_dir: If set, passed as the `--profiles-dir` argument to the `dbt` command
    :param target_path: If set, overrides expected location of dbt artifacts (default is `./target`)
    :param target: If set, passed as the `--target` argument to the `dbt` command
    :param vars: If set, passed as the `--vars` argument to the `dbt` command
    :param models: If set, passed as the `--models` argument to the `dbt` command
    :param exclude: If set, passed as the `--exclude` argument to the `dbt` command
    :param select: If set, passed as the `--select` argument to the `dbt` command
    :param verbose: The operator will log verbosely to the Airflow logs
    :param warn_error: If `True`, treat warnings as errors.
    :param full_refresh: If `True`, will fully-refresh incremental models.
    :param data: If `True`, includes `--data` in the `dbt` command
    :param schema: If `True`, includes `--schema` in the `dbt` command
    """
    def __init__(
            self,
            mc_conn_id: Optional[str] = None,
            mc_include_logs: bool = True,
            dir: str = ".",
            dbt_bin: str = "dbt",
            env: Optional[Dict] = None,
            profiles_dir: Optional[str] = None,
            target_path: Optional[str] = None,
            target: Optional[str] = None,
            vars: Optional[Dict] = None,
            models: Optional[str] = None,
            exclude: Optional[str] = None,
            select: Optional[str] = None,
            verbose: bool = True,
            warn_error: bool = False,
            full_refresh: bool = False,
            data: bool = False,
            schema: bool = False,
    ):
        self.mc_conn_id = mc_conn_id
        self.mc_include_logs = mc_include_logs
        self.dir = dir
        self.dbt_bin = dbt_bin
        self.env = {} if env is None else env
        self.profiles_dir = profiles_dir
        self.target_path = target_path
        self.target = target
        self.vars = vars
        self.models = models
        self.exclude = exclude
        self.select = select
        self.verbose = verbose
        self.warn_error = warn_error
        self.full_refresh = full_refresh
        self.data = data
        self.schema = schema

    def build_command(self, command: str) -> List[str]:
        """
        Build dbt command

        :param command: dbt command, e.g. "run" or "docs generate"
        """
        dbt_cmd = [self.dbt_bin] + command.split()

        if self.profiles_dir is not None:
            dbt_cmd.extend(['--profiles-dir', self.profiles_dir])

        if self.target is not None:
            dbt_cmd.extend(['--target', self.target])

        if self.vars is not None:
            dbt_cmd.extend(['--vars', json.dumps(self.vars)])

        if self.models is not None:
            dbt_cmd.extend(['--models', self.models])

        if self.exclude is not None:
            dbt_cmd.extend(['--exclude', self.exclude])

        if self.select is not None:
            dbt_cmd.extend(['--select', self.select])

        if self.full_refresh:
            dbt_cmd.extend(['--full-refresh'])

        if self.data:
            dbt_cmd.extend(['--data'])

        if self.schema:
            dbt_cmd.extend(['--schema'])

        if self.warn_error:
            dbt_cmd.insert(1, '--warn-error')

        return dbt_cmd


class DefaultConfigProvider(ABC):
    """
    Concrete implementations of this class will provide a default dbt CLI configuration for each dbt operator.

    The fully qualified name of the concrete class should be set in a `AIRFLOW_MCD_DBT_CONFIG_PROVIDER` environment
    variable in the Airflow runtime environment.

    AWS MWAA users should add an `mc.airflow_mcd_dbt_config_provider` custom configuration property to the MWAA environment.
    """
    ENV_VAR_NAME = "AIRFLOW_MCD_DBT_CONFIG_PROVIDER"

    @abstractmethod
    def config(self) -> DbtConfig:
        """
        Concrete implementation should return a default dbt CLI configuration.
        """
        pass

    @classmethod
    def get(cls) -> DbtConfig:
        """
        Get the default dbt CLI configuration.
        (from fully qualified class name defined in `AIRFLOW_MCD_DEFAULT_CONFIG_PROVIDER`).
        """
        provider_fqn = os.getenv(cls.ENV_VAR_NAME) or \
            os.getenv(f"AIRFLOW__MC__{cls.ENV_VAR_NAME}")  # for AWS MWAA

        if provider_fqn:
            module_and_class_name = provider_fqn.rsplit(".", 1)
            provider_module = importlib.import_module(module_and_class_name[0])
            provider_class = getattr(provider_module, module_and_class_name[1])
            provider = provider_class()
            if isinstance(provider, DefaultConfigProvider):
                logger.info(f"Loading default dbt operator configuration from: {provider_fqn}")
                return provider.config()
            else:
                raise Exception(f"dbt configuration provider defined in {cls.ENV_VAR_NAME} is not an instance of {cls.__name__}")

        return DbtConfig()


class DbtOperator(BaseOperator):
    """
    Airflow operator that executes a dbt command and sends artifacts to Monte Carlo.

    :param command: dbt command to execute, e.g. "run", "test", or "build"
    :param project_name: dbt project name to send to Monte Carlo
    :param job_name: dbt job name to send to Monte Carlo
    :param mc_conn_id: Identifier of Monte Carlo connection configured in Airflow
    :param mc_resource_id: Identifier of Monte Carlo lake/warehouse to use to match dbt results to tables (required if you are monitoring multiple lake/warehouse resources in Monte Carlo)
    :param mc_enabled: If `True`, send dbt artifacts to Monte Carlo after dbt command has completed
    :param mc_include_logs: If `True`, write a copy of the logs generated by the dbt command to a local file and include with artifacts sent to Monte Carlo
    :param mc_success_required: If `True`, Airflow task will fail if dbt artifacts cannot be sent to Monte Carlo
    :param dbt_success_required: If `True`, Airflow task will fail if dbt command returns a non-zero status code
    :param dir: The directory to run the CLI in
    :param dbt_bin: The `dbt` CLI. Defaults to `dbt`, so assumes it's on your `PATH`
    :param env: Optional environment variables to add to dbt command execution
    :param profiles_dir: If set, passed as the `--profiles-dir` argument to the `dbt` command
    :param target_path: If set, overrides expected location of dbt artifacts (default is `./target`)
    :param target: If set, passed as the `--target` argument to the `dbt` command
    :param vars: If set, passed as the `--vars` argument to the `dbt` command
    :param models: If set, passed as the `--models` argument to the `dbt` command
    :param exclude: If set, passed as the `--exclude` argument to the `dbt` command
    :param select: If set, passed as the `--select` argument to the `dbt` command
    :param verbose: The operator will log verbosely to the Airflow logs
    :param warn_error: If `True`, treat warnings as errors.
    :param full_refresh: If `True`, will fully-refresh incremental models.
    :param data: If `True`, includes `--data` in the `dbt` command
    :param schema: If `True`, includes `--schema` in the `dbt` command
    """

    # color of nodes in the Airflow UI (blue from MC logo)
    ui_color = "#248BF0"

    # allow use of Jinja templates in these fields
    template_fields = ['vars']

    # dbt spits out some escape characters in the logs for some reason, this regex is used to remove them
    ESCAPE_REGEX = re.compile(r'\x1b')

    def __init__(self,
                 command: str,
                 project_name: str,
                 job_name: str,
                 mc_conn_id: Optional[str] = None,
                 mc_resource_id: Optional[str] = None,
                 mc_enabled: bool = True,
                 mc_include_logs: bool = False,
                 mc_success_required: bool = False,
                 dbt_success_required: bool = True,
                 dir: str = None,
                 dbt_bin: str = None,
                 env: Optional[Dict] = None,
                 profiles_dir: Optional[str] = None,
                 target_path: Optional[str] = None,
                 target: Optional[str] = None,
                 vars: Optional[Dict] = None,
                 models: Optional[str] = None,
                 exclude: Optional[str] = None,
                 select: Optional[str] = None,
                 verbose: bool = True,
                 warn_error: bool = False,
                 full_refresh: bool = False,
                 data: bool = False,
                 schema: bool = False,
                 **kwargs):

        super(DbtOperator, self).__init__(**kwargs)
        self.command = command
        self.project_name = project_name
        self.job_name = job_name
        self.mc_conn_id = mc_conn_id
        self.mc_resource_id = mc_resource_id
        self.mc_enabled = mc_enabled
        self.mc_include_logs = mc_include_logs
        self.mc_success_required = mc_success_required
        self.dbt_success_required = dbt_success_required
        self.dir = dir
        self.dbt_bin = dbt_bin
        self.env = env
        self.profiles_dir = profiles_dir
        self.target_path = target_path
        self.target = target
        self.vars = vars
        self.models = models
        self.exclude = exclude
        self.select = select
        self.verbose = verbose
        self.warn_error = warn_error
        self.full_refresh = full_refresh
        self.data = data
        self.schema = schema

    def execute(self, context: Context) -> Any:
        config = self._merge_config()
        log_file_path = f"{config.dir}/dbt.log" if config.mc_include_logs else None
        return_code = self._execute_dbt(config, log_file_path)
        self._send_artifacts_to_monte_carlo(config, log_file_path)
        if return_code > 0 and self.dbt_success_required:
            raise AirflowException("dbt command failed")

    def _merge_config(self) -> DbtConfig:
        # get default config to be applied to all operators
        default_config = DefaultConfigProvider.get()

        # merge operator-provided config with default
        config = DbtConfig(
            mc_conn_id=self.mc_conn_id or default_config.mc_conn_id,
            mc_include_logs=self.mc_include_logs or default_config.mc_include_logs,
            dir=self.dir or default_config.dir,
            dbt_bin=self.dbt_bin or default_config.dbt_bin,
            env=default_config.env,
            profiles_dir=self.profiles_dir or default_config.profiles_dir,
            target_path=self.target_path or default_config.target_path,
            target=self.target or default_config.target,
            vars=self.vars or default_config.vars,
            models=self.models or default_config.models,
            exclude=self.exclude or default_config.exclude,
            select=self.select or default_config.select,
            verbose=self.verbose or default_config.verbose,
            warn_error=self.warn_error or default_config.warn_error,
            full_refresh=self.full_refresh or default_config.full_refresh,
            data=self.data or default_config.data,
            schema=self.schema or default_config.schema,
        )
        if self.env:
            config.env.update(self.env)

        return config

    def _execute_dbt(self, config: DbtConfig, log_file_path: Optional[str]) -> int:
        # build dbt command
        cmd = config.build_command(self.command)
        if config.verbose:
            self.log.info(" ".join(cmd))

        # gather environment variables
        env = os.environ.copy()
        if config.env:
            env.update(config.env)

        # submit dbt command
        process = subprocess.Popen(
            cmd,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=config.dir,
            close_fds=True,
        )

        # logging, both to Airflow logger and a file (to be sent to Monte Carlo)
        log_file = open(log_file_path, "w") if log_file_path else None
        for line in iter(process.stdout.readline, b""):
            line = self.ESCAPE_REGEX.sub('', line.decode("utf-8"))
            self.log.info(line.rstrip())
            if log_file:
                log_file.write(line)

        # wait for command to finish
        process.wait()
        self.log.info(f"Command exited with return code: {process.returncode}")
        if log_file:
            log_file.close()

        return process.returncode

    def _send_artifacts_to_monte_carlo(self, config: DbtConfig, log_file_path: Optional[str]):
        if self.mc_enabled:
            target_path = config.target_path or f"{config.dir}/target"
            self.log.info(f"Sending dbt artifacts in '{target_path}' to Monte Carlo")
            try:
                DbtImporter(
                    mc_client=Client(session=SessionHook(mcd_session_conn_id=config.mc_conn_id).get_conn())
                ).import_run(
                    manifest_path=f"{target_path}/manifest.json",
                    run_results_path=f"{target_path}/run_results.json",
                    logs_path=log_file_path,
                    project_name=self.project_name,
                    job_name=self.job_name,
                    resource_id=self.mc_resource_id,
                )
                self.log.info("Successfully sent dbt artifacts to Monte Carlo")
            except Exception as ex:
                self.log.warning(f"Failed to send dbt artifacts to Monte Carlo: {ex}")
                if self.mc_success_required:
                    raise ex


class DbtBuildOperator(DbtOperator):
    def __init__(self, **kwargs):
        super(DbtBuildOperator, self).__init__(command="build", **kwargs)


class DbtRunOperator(DbtOperator):
    def __init__(self, **kwargs):
        super(DbtRunOperator, self).__init__(command="run", **kwargs)


class DbtSeedOperator(DbtOperator):
    def __init__(self, **kwargs):
        super(DbtSeedOperator, self).__init__(command="seed", **kwargs)


class DbtSnapshotOperator(DbtOperator):
    def __init__(self, **kwargs):
        super(DbtSnapshotOperator, self).__init__(command="snapshot", **kwargs)


class DbtTestOperator(DbtOperator):
    def __init__(self, **kwargs):
        super(DbtTestOperator, self).__init__(command="test", **kwargs)
