from __future__ import annotations

import shutil
import logging

from textwrap import dedent, indent
from pathlib import Path
from datetime import datetime

from bigflow import commons
from bigflow.workflow import DEFAULT_EXECUTION_TIMEOUT, Workflow, WorkflowJob


logger = logging.getLogger(__name__)


def clear_dags_output_dir(workdir: str) -> None:
    dags_dir_path = get_dags_output_dir(workdir)
    logger.info("clearing dags_output_dir %s", dags_dir_path)
    shutil.rmtree(str(dags_dir_path.resolve()))


def secret_template(secret: str) -> str:
    secret_clean = secret.replace('_', '-')
    return f"Secret(deploy_type='env', deploy_target={secret!r}, secret={secret_clean!r}, key={secret!r})"


def generate_dag_file(
    workdir: str,
    image_version: str,
    workflow: Workflow,
    start_from: datetime | str,
    build_ver: str,
    root_package_name: str,
) -> str:

    start_from = _str_to_datetime(start_from)

    logger.info("start_from %s:", start_from)
    logger.info("build_ver: %s", build_ver)
    logger.info("image version: %s", image_version)

    dag_deployment_id = get_dag_deployment_id(workflow.workflow_id, start_from, build_ver)
    dag_file_path = get_dags_output_dir(workdir) / (dag_deployment_id + '_dag.py')
    workflow_start_date = workflow.start_time_factory(start_from)

    logger.info("dag_file_path: %s", dag_file_path)

    dag_chunks = []
    dag_chunks.append(dedent(f"""\
        # This file was generated by `bigflow build-dags`
        # bigflow-workflow:  \t{workflow.workflow_id}
        # bigflow-build-ver: \t{build_ver}
        # bigflow-startdate: \t{start_from.isoformat()}
        # bigflow-imageid:   \t{image_version}

        import datetime
        from airflow import DAG
        from airflow import version

        try:
            from airflow.kubernetes.secret import Secret
        except ImportError:
            # Fallback to older Airflow
            from airflow.contrib.kubernetes.secret import Secret

        try:
            from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
        except ImportError:
            # Fallback to older Airflow
            try:
                # Fallback to older Airflow
                from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
            except ImportError:
                # Fallback to even older Airflow
                from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

        # To deploy BigFlow project, following requirements options are needed: (airflow 1.x + composer 1.x) or (airflow 2.x + composer >= 2.1.0)
        IS_COMPOSER_2_X = version.version >= '2.0.0'
        IS_AIRFLOW_2_3_X = version.version >= '2.3.0'
        namespace = 'composer-user-workloads' if IS_COMPOSER_2_X else 'default'

        default_args = dict(
            owner='airflow',
            depends_on_past={workflow.depends_on_past!r},
            start_date={workflow_start_date!r},
            email_on_failure=False,
            email_on_retry=False,
            execution_timeout={DEFAULT_EXECUTION_TIMEOUT!r},
        )

        dag = DAG(
            {dag_deployment_id!r},
            default_args=default_args,
            max_active_runs=1,
            schedule_interval={workflow.schedule_interval!r},
        )
    """))

    def build_dag_operator(
        workflow_job: WorkflowJob,
        dependencies: list[WorkflowJob],
    ) -> None:

        job = workflow_job.job
        job_var = f"t{job.id}"
        pod_operator_params_var = f"{job_var}_pod_operator_params"
        task_id = job.id.replace("_", "-")
        retries = getattr(job, 'retry_count', 3)
        bf_job = workflow.workflow_id + "." + job.id
        env_var_name = workflow.env_variable

        if workflow.secrets:
            indent_prefix =  """\
                """
            secrets_definitions = "".join(
                f"{indent_prefix}    {secret_template(s)},\n"
                for s in workflow.secrets
            )
            secrets_definition_list = f"[\n{secrets_definitions}{indent_prefix}]"""
        else:
            secrets_definition_list = "[]"

        execution_timeout = commons.as_timedelta(
            getattr(job, 'execution_timeout_sec', None)
            or workflow.DEFAULT_EXECUTION_TIMEOUT_IN_SECONDS)
        retry_delay = commons.as_timedelta(getattr(job, 'retry_pause_sec', 60))

        dag_chunks.append(dedent(f"""\
            {pod_operator_params_var} = {{
                'dag': dag,
                'task_id': {task_id!r},
                'name': {task_id!r},
                'cmds': ['python', '-m', 'bigflow', 'run'],
                'arguments': [
                    '--job', {bf_job!r},
                    '--runtime', '{{{{ execution_date.strftime("%Y-%m-%d %H:%M:%S") }}}}',
                    '--project-package', {root_package_name!r},
                    '--config', '{{{{var.value.{env_var_name}}}}}',
                ],
                'namespace': namespace,
                'image': {image_version!r},
                'is_delete_operator_pod': True,
                'retries': {retries!r},
                'retry_delay': {retry_delay!r},
                'secrets': {secrets_definition_list},
                'execution_timeout': {execution_timeout!r},
            }}
            if IS_AIRFLOW_2_3_X:
                {pod_operator_params_var}['config_file'] = "/home/airflow/composer_kube_config"
                {pod_operator_params_var}['kubernetes_conn_id'] = "kubernetes_default"

            {job_var} = KubernetesPodOperator(**{pod_operator_params_var})
            """))

        for d in dependencies:
            up_job_var = f"t{d.job.id}"
            dag_chunks.append(f"{job_var}.set_upstream({up_job_var})")

        dag_chunks.append("")

    workflow._call_on_graph_nodes(build_dag_operator)
    dag_chunks.append("")

    dag_file_content = "\n".join(dag_chunks)
    dag_file_path.write_text(dag_file_content)

    return dag_file_path.as_posix()


def get_dag_deployment_id(
    workflow_name: str,
    start_from: datetime,
    build_ver: str,
) -> str:
    return '{workflow_name}__v{ver}__{start_from}'.format(
        workflow_name=workflow_name,
        ver=build_ver.translate(str.maketrans(".-+", "___")),
        start_from=_str_to_datetime(start_from).strftime('%Y_%m_%d_%H_%M_%S')
    )


def get_dags_output_dir(workdir: str) -> Path:
    dags_dir_path = Path(workdir) / '.dags'
    dags_dir_path.mkdir(parents=True, exist_ok=True)
    return dags_dir_path


def _str_to_datetime(dt: str | datetime) -> datetime:
    if isinstance(dt, datetime):
        return dt
    elif len(dt) <= 10:
        return datetime.strptime(dt, "%Y-%m-%d")
    else:
        return datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
