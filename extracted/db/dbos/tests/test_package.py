import json
import os
import shutil
import signal
import subprocess
import tempfile
import time
import urllib.error
import urllib.request

import requests
import sqlalchemy as sa
import yaml


def test_package(build_wheel: str, postgres_db_engine: sa.Engine) -> None:

    # Clean up the database from previous runs
    for template_name in ["dbos-db-starter", "dbos-app-starter"]:
        db_starter = template_name == "dbos-db-starter"
        app_db_name = template_name.replace("-", "_")
        with postgres_db_engine.connect() as connection:
            connection.execution_options(isolation_level="AUTOCOMMIT")
            connection.execute(sa.text(f"DROP DATABASE IF EXISTS {app_db_name}"))
            connection.execute(
                sa.text(f"DROP DATABASE IF EXISTS {app_db_name}_dbos_sys")
            )

        with tempfile.TemporaryDirectory() as temp_path:
            temp_path = tempfile.mkdtemp(prefix="dbos-")
            wheel_path = os.path.abspath(build_wheel)

            # Create a new virtual environment in the temp directory
            venv_path = os.path.join(temp_path, ".venv")
            if os.path.exists(venv_path):
                shutil.rmtree(venv_path)

            # To create a venv, we need the system Python executable. TODO: Don't hardcode the path.
            subprocess.check_call(
                [os.path.join("/", "usr", "bin", "python3"), "-m", "venv", venv_path]
            )

            venv = os.environ.copy()
            venv["PATH"] = f"{os.path.join(venv_path, 'bin')}:{venv['PATH']}"
            venv["VIRTUAL_ENV"] = venv_path
            venv["DBOS_DATABASE_URL"] = postgres_db_engine.url.set(
                database=app_db_name
            ).render_as_string(hide_password=False)

            # Install the dbos package into the virtual environment
            subprocess.check_call(
                ["pip", "install", wheel_path], cwd=temp_path, env=venv
            )

            # initalize the app with dbos scaffolding
            subprocess.check_call(
                ["dbos", "init", template_name, "--template", template_name],
                cwd=temp_path,
            )

            # Run schema migration
            subprocess.check_call(["dbos", "migrate"], cwd=temp_path, env=venv)

            # Launch the application in the virtual environment as a background process
            process = subprocess.Popen(["dbos", "start"], cwd=temp_path, env=venv)

            try:
                url = "http://localhost:8000"
                if db_starter:
                    url += "/greeting/dbos"
                max_retries = 10
                for attempt in range(max_retries):
                    try:
                        with urllib.request.urlopen(url, timeout=1) as response:
                            status_code = response.getcode()
                            assert status_code == 200
                            if db_starter:
                                response_data = response.read().decode("utf-8")
                                data = json.loads(response_data)
                                assert (
                                    data
                                    == "Greetings, dbos! You have been greeted 1 times."
                                )
                            break
                    except (urllib.error.URLError, AssertionError) as e:
                        if attempt < max_retries - 1:  # If not the last attempt
                            print(
                                f"Attempt {attempt + 1} failed: {e}. Retrying in 1 second..."
                            )
                            time.sleep(1)
                        else:
                            print(f"All {max_retries} attempts failed. Last error: {e}")
                            raise
            finally:
                os.kill(process.pid, signal.SIGINT)
                process.wait()


def test_init_config() -> None:
    app_name = "example-name"
    expected_yaml = {
        "name": app_name,
        "language": "python",
        "runtimeConfig": {"start": ["python3 main.py"]},
        "database_url": "${DBOS_DATABASE_URL}",
    }
    with tempfile.TemporaryDirectory() as temp_path:

        subprocess.check_call(
            ["dbos", "init", app_name, "--config"],
            cwd=temp_path,
        )

        config_path = os.path.join(temp_path, "dbos-config.yaml")
        assert os.path.exists(config_path)

        with open(config_path) as f:
            actual_yaml = yaml.safe_load(f)

        assert actual_yaml == expected_yaml


def test_reset(postgres_db_engine: sa.Engine) -> None:
    app_name = "reset-app"
    sysdb_name = "reset_app_dbos_sys"
    db_url = postgres_db_engine.url.set(database="reset_app").render_as_string(
        hide_password=False
    )
    with tempfile.TemporaryDirectory() as temp_path:
        env = os.environ.copy()
        env["DBOS_DATABASE_URL"] = db_url
        subprocess.check_call(
            ["dbos", "init", app_name, "--template", "dbos-db-starter"],
            cwd=temp_path,
        )

        # Create a system database and verify it exists
        subprocess.check_call(["dbos", "migrate"], cwd=temp_path, env=env)
        with postgres_db_engine.connect() as c:
            c.execution_options(isolation_level="AUTOCOMMIT")
            result = c.execute(
                sa.text(
                    f"SELECT COUNT(*) FROM pg_database WHERE datname = '{sysdb_name}'"
                )
            ).scalar()
            assert result == 1

        # Call reset and verify it's destroyed
        subprocess.check_call(
            ["dbos", "reset", "-y", "--db-url", db_url, "--sys-db-name", sysdb_name],
            cwd=temp_path,
        )
        with postgres_db_engine.connect() as c:
            c.execution_options(isolation_level="AUTOCOMMIT")
            result = c.execute(
                sa.text(
                    f"SELECT COUNT(*) FROM pg_database WHERE datname = '{sysdb_name}'"
                )
            ).scalar()
            assert result == 0


def test_workflow_commands(postgres_db_engine: sa.Engine) -> None:
    app_name = "reset-app"
    db_url = postgres_db_engine.url.set(database="dbos_toolbox").render_as_string(
        hide_password=False
    )
    with tempfile.TemporaryDirectory() as temp_path:
        env = os.environ.copy()
        env["DBOS_DATABASE_URL"] = db_url
        subprocess.check_call(
            ["dbos", "init", app_name, "--template", "dbos-toolbox"],
            cwd=temp_path,
            env=env,
        )
        subprocess.check_call(["dbos", "reset", "-y", "-D", db_url], cwd=temp_path)
        subprocess.check_call(
            ["dbos", "migrate"], cwd=temp_path, env=env
        )  # For the alembic migration

        # Get some workflows enqueued on the toolbox, then kill the toolbox
        process = subprocess.Popen(["dbos", "start"], cwd=temp_path, env=env)
        try:
            session = requests.Session()
            for i in range(10):
                try:
                    session.get(
                        "http://localhost:8000/queue", timeout=1
                    ).raise_for_status()
                    break
                except requests.exceptions.Timeout:
                    break
                except requests.exceptions.ConnectionError as e:
                    if i == 9:
                        raise
                    print(f"Attempt {i+1} failed: {e}. Retrying in 1 second...")
                    time.sleep(1)
            time.sleep(1)  # So the queued workflows can start
        finally:
            # Because the toolbox steps sleep for 5 seconds, all the steps should be PENDING
            os.kill(process.pid, signal.SIGINT)
            process.wait()

        # Verify the output is valid JSON
        output = subprocess.check_output(
            ["dbos", "workflow", "list", "--db-url", db_url], cwd=temp_path
        )
        data = json.loads(output)
        assert isinstance(data, list) and len(data) == 10

        # Verify the output is valid JSON
        output = subprocess.check_output(
            ["dbos", "workflow", "queue", "list", "--db-url", db_url], cwd=temp_path
        )
        workflows = json.loads(output)
        assert isinstance(workflows, list) and len(workflows) == 10
        for wf in workflows:
            output = subprocess.check_output(
                ["dbos", "workflow", "get", wf["workflow_id"], "--db-url", db_url],
                cwd=temp_path,
            )
            get_wf_data = json.loads(output)
            assert isinstance(get_wf_data, dict)
            assert get_wf_data["workflow_id"] == wf["workflow_id"]

        # workflow ID is a preffix to each step ID
        wf_id = "-".join(workflows[0]["workflow_id"].split("-")[:-1])
        get_steps_output = subprocess.check_output(
            ["dbos", "workflow", "steps", wf_id, "--db-url", db_url], cwd=temp_path
        )
        get_steps_data = json.loads(get_steps_output)
        assert isinstance(get_steps_data, list)
        assert len(get_steps_data) == 10

        # From now pass database url in the environment

        # cancel the workflow and check the status is CANCELLED
        subprocess.check_output(
            ["dbos", "workflow", "cancel", wf_id], cwd=temp_path, env=env
        )
        output = subprocess.check_output(
            ["dbos", "workflow", "get", wf_id], cwd=temp_path, env=env
        )
        get_wf_data = json.loads(output)
        assert isinstance(get_wf_data, dict)
        assert get_wf_data["status"] == "CANCELLED"

        # resume the workflow and check the status is ENQUEUED
        subprocess.check_output(
            ["dbos", "workflow", "resume", wf_id], cwd=temp_path, env=env
        )
        output = subprocess.check_output(
            ["dbos", "workflow", "get", wf_id], cwd=temp_path, env=env
        )
        get_wf_data = json.loads(output)
        assert isinstance(get_wf_data, dict)
        assert get_wf_data["status"] == "ENQUEUED"

        # restart the workflow and check it has a new ID and its status is ENQUEUED
        output = subprocess.check_output(
            ["dbos", "workflow", "restart", wf_id], cwd=temp_path, env=env
        )
        restart_wf_data = json.loads(output)
        assert isinstance(restart_wf_data, dict)
        assert restart_wf_data["workflow_id"] != wf_id
        assert restart_wf_data["status"] == "ENQUEUED"

        # fork the workflow at step 5 and check it has a new ID and its status is ENQUEUED
        output = subprocess.check_output(
            ["dbos", "workflow", "fork", wf_id, "--step", "5"],
            cwd=temp_path,
            env=env,
        )
        fork_wf_data = json.loads(output)
        assert isinstance(fork_wf_data, dict)
        assert fork_wf_data["workflow_id"] != wf_id
        assert fork_wf_data["status"] == "ENQUEUED"
