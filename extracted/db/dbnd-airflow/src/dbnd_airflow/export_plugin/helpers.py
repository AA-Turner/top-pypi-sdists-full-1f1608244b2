# © Copyright Databand.ai, an IBM Company 2022

import datetime
import inspect
import json
import logging
import os
import sys

from airflow.models import BaseOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from dbnd._core.utils.basics.memoized import cached
from dbnd._core.utils.git import get_git_commit, is_git_dirty
from dbnd._core.utils.uid_utils import source_md5
from dbnd.utils.helpers import get_callable_name
from dbnd_airflow.export_plugin.compat import get_task_log_reader


logger = logging.getLogger(__name__)

MAX_LOGS_SIZE_IN_BYTES = 10000
MAX_RECURSIVE_CALL_NUM = 5
TASK_ARG_TYPES = (str, float, bool, int, datetime.datetime)


def resolve_attribute_or_default_value(obj, attribute, default_value):
    if hasattr(obj, attribute):
        return getattr(obj, attribute)
    return default_value


def resolve_attribute_or_default_attribute(obj, attributes_list, default_value=None):
    for attribute in attributes_list:
        if hasattr(obj, attribute):
            return getattr(obj, attribute)
    return default_value


def interval_to_str(schedule_interval):
    if isinstance(schedule_interval, datetime.timedelta):
        if schedule_interval == datetime.timedelta(days=1):
            return "@daily"
        if schedule_interval == datetime.timedelta(hours=1):
            return "@hourly"
    return str(schedule_interval)


def _get_log(ti, task):
    try:
        ti.task = task
        af_logger = logging.getLogger("airflow.task")
        task_log_reader = get_task_log_reader()
        handler = next(
            (
                handler
                for handler in af_logger.handlers
                if handler.name == task_log_reader
            ),
            None,
        )
        logs, metadatas = handler.read(ti, ti._try_number, metadata={})
        if not logs:
            return None
        all_logs = logs[0]
        logs_size = sys.getsizeof(all_logs)
        if logs_size < MAX_LOGS_SIZE_IN_BYTES:
            return all_logs

        result = (
            all_logs[-MAX_LOGS_SIZE_IN_BYTES:]
            + f"... ({MAX_LOGS_SIZE_IN_BYTES} of {len(all_logs)})"
        )
        return result
    except Exception:
        pass
    finally:
        del ti.task


@cached()
def _get_git_status(path):
    commit = get_git_commit(path) or ""
    is_dirty = is_git_dirty(path) or False
    return commit, not is_dirty


def _get_source_code(t):
    # type: (BaseOperator) -> str | None
    # TODO: add other "code" extractions
    # TODO: maybe return it with operator code as well
    try:
        if isinstance(t, PythonOperator):
            return inspect.getsource(t.python_callable)
        if isinstance(t, BashOperator):
            if isinstance(t.bash_command, str):
                return t.bash_command
            if hasattr(t, "python_callable"):
                # Adds support for bash decorator added in Airflow 2.9
                return inspect.getsource(t.python_callable)
        return None
    except Exception:
        return None


def _get_module_code(t):
    # type: (BaseOperator) -> str
    try:
        if isinstance(t, PythonOperator):
            return inspect.getsource(inspect.getmodule(t.python_callable))
    except Exception:
        pass


def _add_source_code(tasks_hash_to_source, source_code):
    source_hash = source_md5(source_code)
    tasks_hash_to_source[source_hash] = source_code
    return source_hash


def _get_command_from_operator(t):
    # type: (BaseOperator) -> str
    if isinstance(t, BashOperator):
        return f"bash_command='{t.bash_command}'"
    elif isinstance(t, PythonOperator):
        func_name = get_callable_name(t.python_callable)
        return f"python_callable={func_name}, op_kwargs={t.op_kwargs}"


def _extract_args_from_dict(t_dict, call_num=1):
    # type: (Dict) -> Dict[str]
    if not t_dict:
        return {}

    if isinstance(t_dict, str) and t_dict.startswith("{"):
        # try load json. is this correct at all?
        try:
            t_dict = json.loads(t_dict)
        except Exception:
            logger.debug("String looked like json but failed to load: %s", t_dict)

    if isinstance(t_dict, str):
        t_dict = {"value": t_dict}

    try:
        # Return only numeric, bool and string attributes
        res = {}
        for k, v in t_dict.items():
            if v is None or isinstance(v, TASK_ARG_TYPES):
                res[k] = v
            elif isinstance(v, list):
                res[k] = [
                    val for val in v if val is None or isinstance(val, TASK_ARG_TYPES)
                ]
            elif isinstance(v, dict):
                if call_num <= MAX_RECURSIVE_CALL_NUM:
                    res[k] = _extract_args_from_dict(v, call_num + 1)
                else:
                    continue
        return res
    except Exception as ex:
        task_id = t_dict.get("task_id") or t_dict.get("_dag_id")
        logging.error("Could not collect task args for %s: %s", task_id, ex)
        return {}


def _read_dag_file(dag_file):
    # TODO: Change implementation when this is done:
    # https://github.com/apache/airflow/pull/7217

    if dag_file and os.path.exists(dag_file):
        with open(dag_file) as file:
            try:
                return file.read()
            except Exception:
                pass

    return ""
