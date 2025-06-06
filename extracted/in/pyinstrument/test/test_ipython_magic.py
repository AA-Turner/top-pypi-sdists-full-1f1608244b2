import signal
import textwrap
from test.fake_time_util import fake_time
from threading import Thread
from time import sleep

import pytest

# note: IPython should be imported within each test. Importing it in our tests
# seems to cause problems with subsequent tests.

cell_code = """
import time

def function_a():
    function_b()
    function_c()

def function_b():
    function_d()

def function_c():
    function_d()

def function_d():
    function_e()

def function_e():
    time.sleep(0.1)

function_a()
"""

# Tests #


@pytest.mark.ipythonmagic
def test_magics(ip):
    from IPython.utils.capture import capture_output as capture_ipython_output

    with fake_time():
        with capture_ipython_output() as captured:
            ip.run_cell_magic("pyinstrument", line="", cell=cell_code)

    assert len(captured.outputs) == 1
    output = captured.outputs[0]
    assert "text/html" in output.data
    assert "text/plain" in output.data

    assert "function_a" in output.data["text/html"]
    assert "<iframe" in output.data["text/html"]
    assert "function_a" in output.data["text/plain"]

    assert "- 0.200 function_a" in output.data["text/plain"]
    assert "- 0.100 FakeClock.sleep" in output.data["text/plain"]

    with fake_time():
        with capture_ipython_output() as captured:
            # this works because function_a was defined in the previous cell
            ip.run_line_magic("pyinstrument", line="function_a()")

    assert len(captured.outputs) == 1
    output = captured.outputs[0]

    assert "function_a" in output.data["text/plain"]
    assert "- 0.100 FakeClock.sleep" in output.data["text/plain"]


@pytest.mark.ipythonmagic
def test_magic_empty_line(ip):
    # check empty line input
    ip.run_line_magic("pyinstrument", line="")


@pytest.mark.ipythonmagic
def test_magic_no_variable_expansion(ip, capsys):
    ip.run_line_magic("pyinstrument", line="print(\"hello {len('world')}\")")

    captured = capsys.readouterr()
    assert "hello {len('world')}" in captured.out
    assert "hello 5" not in captured.out


@pytest.mark.ipythonmagic
def test_pyinstrument_handles_interrupt_silently(ip, capsys):
    from pyinstrument.magic.magic import InterruptSilently

    thread = Thread(target=_interrupt_after_1s)
    thread.start()
    # expect our custom exception to bubble up
    with pytest.raises(InterruptSilently):
        ip.run_cell_magic("pyinstrument", "", "from time import sleep; sleep(2)")

    thread.join()
    # nothing should have hit stderr
    _, err = capsys.readouterr()
    assert err.strip() == ""


@pytest.mark.ipythonmagic
def test_async_cell_with_pyinstrument(ip, capsys):
    ip.run_cell_magic(
        "pyinstrument",
        line="--async_mode=enabled",
        cell=textwrap.dedent(
            """
            import asyncio
            async def function_a():
                await asyncio.sleep(0.1)
                return 42
            a = await function_a()
            print("a:", a)
            """
        ),
    )
    stdout, stderr = capsys.readouterr()
    assert "a: 42" in stdout


# Utils #


@pytest.fixture(scope="module")
def session_ip():
    from IPython.testing.globalipapp import start_ipython

    yield start_ipython()


def _interrupt_after_1s():
    sleep(1)
    signal.raise_signal(signal.SIGINT)


@pytest.fixture(scope="function")
def ip(session_ip):
    session_ip.run_line_magic(magic_name="load_ext", line="pyinstrument")
    yield session_ip
    session_ip.run_line_magic(magic_name="reset", line="-f")
