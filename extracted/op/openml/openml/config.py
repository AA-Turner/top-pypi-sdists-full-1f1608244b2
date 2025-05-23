"""Store module level information like the API key, cache directory and the server"""

# License: BSD 3-Clause
from __future__ import annotations

import configparser
import logging
import logging.handlers
import os
import platform
import shutil
import warnings
from contextlib import contextmanager
from io import StringIO
from pathlib import Path
from typing import Any, Iterator, cast
from typing_extensions import Literal, TypedDict
from urllib.parse import urlparse

logger = logging.getLogger(__name__)
openml_logger = logging.getLogger("openml")
console_handler: logging.StreamHandler | None = None
file_handler: logging.handlers.RotatingFileHandler | None = None

OPENML_CACHE_DIR_ENV_VAR = "OPENML_CACHE_DIR"
OPENML_SKIP_PARQUET_ENV_VAR = "OPENML_SKIP_PARQUET"


class _Config(TypedDict):
    apikey: str
    server: str
    cachedir: Path
    avoid_duplicate_runs: bool
    retry_policy: Literal["human", "robot"]
    connection_n_retries: int
    show_progress: bool


def _create_log_handlers(create_file_handler: bool = True) -> None:  # noqa: FBT001, FBT002
    """Creates but does not attach the log handlers."""
    global console_handler, file_handler  # noqa: PLW0603
    if console_handler is not None or file_handler is not None:
        logger.debug("Requested to create log handlers, but they are already created.")
        return

    message_format = "[%(levelname)s] [%(asctime)s:%(name)s] %(message)s"
    output_formatter = logging.Formatter(message_format, datefmt="%H:%M:%S")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(output_formatter)

    if create_file_handler:
        one_mb = 2**20
        log_path = _root_cache_directory / "openml_python.log"
        file_handler = logging.handlers.RotatingFileHandler(
            log_path,
            maxBytes=one_mb,
            backupCount=1,
            delay=True,
        )
        file_handler.setFormatter(output_formatter)


def _convert_log_levels(log_level: int) -> tuple[int, int]:
    """Converts a log level that's either defined by OpenML/Python to both specifications."""
    # OpenML verbosity level don't match Python values directly:
    openml_to_python = {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG}
    python_to_openml = {
        logging.DEBUG: 2,
        logging.INFO: 1,
        logging.WARNING: 0,
        logging.CRITICAL: 0,
        logging.ERROR: 0,
    }
    # Because the dictionaries share no keys, we use `get` to convert as necessary:
    openml_level = python_to_openml.get(log_level, log_level)
    python_level = openml_to_python.get(log_level, log_level)
    return openml_level, python_level


def _set_level_register_and_store(handler: logging.Handler, log_level: int) -> None:
    """Set handler log level, register it if needed, save setting to config file if specified."""
    _oml_level, py_level = _convert_log_levels(log_level)
    handler.setLevel(py_level)

    if openml_logger.level > py_level or openml_logger.level == logging.NOTSET:
        openml_logger.setLevel(py_level)

    if handler not in openml_logger.handlers:
        openml_logger.addHandler(handler)


def set_console_log_level(console_output_level: int) -> None:
    """Set console output to the desired level and register it with openml logger if needed."""
    global console_handler  # noqa: PLW0602
    assert console_handler is not None
    _set_level_register_and_store(console_handler, console_output_level)


def set_file_log_level(file_output_level: int) -> None:
    """Set file output to the desired level and register it with openml logger if needed."""
    global file_handler  # noqa: PLW0602
    assert file_handler is not None
    _set_level_register_and_store(file_handler, file_output_level)


# Default values (see also https://github.com/openml/OpenML/wiki/Client-API-Standards)
_user_path = Path("~").expanduser().absolute()


def _resolve_default_cache_dir() -> Path:
    user_defined_cache_dir = os.environ.get(OPENML_CACHE_DIR_ENV_VAR)
    if user_defined_cache_dir is not None:
        return Path(user_defined_cache_dir)

    if platform.system().lower() != "linux":
        return _user_path / ".openml"

    xdg_cache_home = os.environ.get("XDG_CACHE_HOME")
    if xdg_cache_home is None:
        return Path("~", ".cache", "openml")

    # This is the proper XDG_CACHE_HOME directory, but
    # we unfortunately had a problem where we used XDG_CACHE_HOME/org,
    # we check heuristically if this old directory still exists and issue
    # a warning if it does. There's too much data to move to do this for the user.

    # The new cache directory exists
    cache_dir = Path(xdg_cache_home) / "openml"
    if cache_dir.exists():
        return cache_dir

    # The old cache directory *does not* exist
    heuristic_dir_for_backwards_compat = Path(xdg_cache_home) / "org" / "openml"
    if not heuristic_dir_for_backwards_compat.exists():
        return cache_dir

    root_dir_to_delete = Path(xdg_cache_home) / "org"
    openml_logger.warning(
        "An old cache directory was found at '%s'. This directory is no longer used by "
        "OpenML-Python. To silence this warning you would need to delete the old cache "
        "directory. The cached files will then be located in '%s'.",
        root_dir_to_delete,
        cache_dir,
    )
    return Path(xdg_cache_home)


_defaults: _Config = {
    "apikey": "",
    "server": "https://www.openml.org/api/v1/xml",
    "cachedir": _resolve_default_cache_dir(),
    "avoid_duplicate_runs": True,
    "retry_policy": "human",
    "connection_n_retries": 5,
    "show_progress": False,
}

# Default values are actually added here in the _setup() function which is
# called at the end of this module
server = _defaults["server"]


def get_server_base_url() -> str:
    """Return the base URL of the currently configured server.

    Turns ``"https://www.openml.org/api/v1/xml"`` in ``"https://www.openml.org/"``

    Returns
    -------
    str
    """
    return server.split("/api")[0]


apikey: str = _defaults["apikey"]
show_progress: bool = _defaults["show_progress"]
# The current cache directory (without the server name)
_root_cache_directory: Path = Path(_defaults["cachedir"])
avoid_duplicate_runs = _defaults["avoid_duplicate_runs"]

retry_policy: Literal["human", "robot"] = _defaults["retry_policy"]
connection_n_retries: int = _defaults["connection_n_retries"]


def set_retry_policy(value: Literal["human", "robot"], n_retries: int | None = None) -> None:
    global retry_policy  # noqa: PLW0603
    global connection_n_retries  # noqa: PLW0603
    default_retries_by_policy = {"human": 5, "robot": 50}

    if value not in default_retries_by_policy:
        raise ValueError(
            f"Detected retry_policy '{value}' but must be one of "
            f"{list(default_retries_by_policy.keys())}",
        )
    if n_retries is not None and not isinstance(n_retries, int):
        raise TypeError(f"`n_retries` must be of type `int` or `None` but is `{type(n_retries)}`.")

    if isinstance(n_retries, int) and n_retries < 1:
        raise ValueError(f"`n_retries` is '{n_retries}' but must be positive.")

    retry_policy = value
    connection_n_retries = default_retries_by_policy[value] if n_retries is None else n_retries


class ConfigurationForExamples:
    """Allows easy switching to and from a test configuration, used for examples."""

    _last_used_server = None
    _last_used_key = None
    _start_last_called = False
    _test_server = "https://test.openml.org/api/v1/xml"
    _test_apikey = "c0c42819af31e706efe1f4b88c23c6c1"

    @classmethod
    def start_using_configuration_for_example(cls) -> None:
        """Sets the configuration to connect to the test server with valid apikey.

        To configuration as was before this call is stored, and can be recovered
        by using the `stop_use_example_configuration` method.
        """
        global server  # noqa: PLW0603
        global apikey  # noqa: PLW0603

        if cls._start_last_called and server == cls._test_server and apikey == cls._test_apikey:
            # Method is called more than once in a row without modifying the server or apikey.
            # We don't want to save the current test configuration as a last used configuration.
            return

        cls._last_used_server = server
        cls._last_used_key = apikey
        cls._start_last_called = True

        # Test server key for examples
        server = cls._test_server
        apikey = cls._test_apikey
        warnings.warn(
            f"Switching to the test server {server} to not upload results to the live server. "
            "Using the test server may result in reduced performance of the API!",
            stacklevel=2,
        )

    @classmethod
    def stop_using_configuration_for_example(cls) -> None:
        """Return to configuration as it was before `start_use_example_configuration`."""
        if not cls._start_last_called:
            # We don't want to allow this because it will (likely) result in the `server` and
            # `apikey` variables being set to None.
            raise RuntimeError(
                "`stop_use_example_configuration` called without a saved config."
                "`start_use_example_configuration` must be called first.",
            )

        global server  # noqa: PLW0603
        global apikey  # noqa: PLW0603

        server = cast(str, cls._last_used_server)
        apikey = cast(str, cls._last_used_key)
        cls._start_last_called = False


def _handle_xdg_config_home_backwards_compatibility(
    xdg_home: str,
) -> Path:
    # NOTE(eddiebergman): A previous bug results in the config
    # file being located at `${XDG_CONFIG_HOME}/config` instead
    # of `${XDG_CONFIG_HOME}/openml/config`. As to maintain backwards
    # compatibility, where users may already may have had a configuration,
    # we copy it over an issue a warning until it's deleted.
    # As a heurisitic to ensure that it's "our" config file, we try parse it first.
    config_dir = Path(xdg_home) / "openml"

    backwards_compat_config_file = Path(xdg_home) / "config"
    if not backwards_compat_config_file.exists():
        return config_dir

    # If it errors, that's a good sign it's not ours and we can
    # safely ignore it, jumping out of this block. This is a heurisitc
    try:
        _parse_config(backwards_compat_config_file)
    except Exception:  # noqa: BLE001
        return config_dir

    # Looks like it's ours, lets try copy it to the correct place
    correct_config_location = config_dir / "config"
    try:
        # We copy and return the new copied location
        shutil.copy(backwards_compat_config_file, correct_config_location)
        openml_logger.warning(
            "An openml configuration file was found at the old location "
            f"at {backwards_compat_config_file}. We have copied it to the new "
            f"location at {correct_config_location}. "
            "\nTo silence this warning please verify that the configuration file "
            f"at {correct_config_location} is correct and delete the file at "
            f"{backwards_compat_config_file}."
        )
        return config_dir
    except Exception as e:  # noqa: BLE001
        # We failed to copy and its ours, return the old one.
        openml_logger.warning(
            "While attempting to perform a backwards compatible fix, we "
            f"failed to copy the openml config file at "
            f"{backwards_compat_config_file}' to {correct_config_location}"
            f"\n{type(e)}: {e}",
            "\n\nTo silence this warning, please copy the file "
            "to the new location and delete the old file at "
            f"{backwards_compat_config_file}.",
        )
        return backwards_compat_config_file


def determine_config_file_path() -> Path:
    if platform.system().lower() == "linux":
        xdg_home = os.environ.get("XDG_CONFIG_HOME")
        if xdg_home is not None:
            config_dir = _handle_xdg_config_home_backwards_compatibility(xdg_home)
        else:
            config_dir = Path("~", ".config", "openml")
    else:
        config_dir = Path("~") / ".openml"

    # Still use os.path.expanduser to trigger the mock in the unit test
    config_dir = Path(config_dir).expanduser().resolve()
    return config_dir / "config"


def _setup(config: _Config | None = None) -> None:
    """Setup openml package. Called on first import.

    Reads the config file and sets up apikey, server, cache appropriately.
    key and server can be set by the user simply using
    openml.config.apikey = THEIRKEY
    openml.config.server = SOMESERVER
    We could also make it a property but that's less clear.
    """
    global apikey  # noqa: PLW0603
    global server  # noqa: PLW0603
    global _root_cache_directory  # noqa: PLW0603
    global avoid_duplicate_runs  # noqa: PLW0603
    global show_progress  # noqa: PLW0603

    config_file = determine_config_file_path()
    config_dir = config_file.parent

    # read config file, create directory for config file
    try:
        if not config_dir.exists():
            config_dir.mkdir(exist_ok=True, parents=True)
    except PermissionError:
        openml_logger.warning(
            f"No permission to create OpenML directory at {config_dir}!"
            " This can result in OpenML-Python not working properly."
        )

    if config is None:
        config = _parse_config(config_file)

    avoid_duplicate_runs = config["avoid_duplicate_runs"]
    apikey = config["apikey"]
    server = config["server"]
    show_progress = config["show_progress"]
    n_retries = int(config["connection_n_retries"])

    set_retry_policy(config["retry_policy"], n_retries)

    user_defined_cache_dir = os.environ.get(OPENML_CACHE_DIR_ENV_VAR)
    if user_defined_cache_dir is not None:
        short_cache_dir = Path(user_defined_cache_dir)
    else:
        short_cache_dir = Path(config["cachedir"])
    _root_cache_directory = short_cache_dir.expanduser().resolve()

    try:
        cache_exists = _root_cache_directory.exists()
        # create the cache subdirectory
        if not cache_exists:
            _root_cache_directory.mkdir(exist_ok=True, parents=True)
        _create_log_handlers()
    except PermissionError:
        openml_logger.warning(
            f"No permission to create OpenML directory at {_root_cache_directory}!"
            " This can result in OpenML-Python not working properly."
        )
        _create_log_handlers(create_file_handler=False)


def set_field_in_config_file(field: str, value: Any) -> None:
    """Overwrites the `field` in the configuration file with the new `value`."""
    if field not in _defaults:
        raise ValueError(f"Field '{field}' is not valid and must be one of '{_defaults.keys()}'.")

    # TODO(eddiebergman): This use of globals has gone too far
    globals()[field] = value
    config_file = determine_config_file_path()
    config = _parse_config(config_file)
    with config_file.open("w") as fh:
        for f in _defaults:
            # We can't blindly set all values based on globals() because when the user
            # sets it through config.FIELD it should not be stored to file.
            # There doesn't seem to be a way to avoid writing defaults to file with configparser,
            # because it is impossible to distinguish from an explicitly set value that matches
            # the default value, to one that was set to its default because it was omitted.
            value = config.get("FAKE_SECTION", f)  # type: ignore
            if f == field:
                value = globals()[f]
            fh.write(f"{f} = {value}\n")


def _parse_config(config_file: str | Path) -> _Config:
    """Parse the config file, set up defaults."""
    config_file = Path(config_file)
    config = configparser.RawConfigParser(defaults=_defaults)  # type: ignore

    # The ConfigParser requires a [SECTION_HEADER], which we do not expect in our config file.
    # Cheat the ConfigParser module by adding a fake section header
    config_file_ = StringIO()
    config_file_.write("[FAKE_SECTION]\n")
    try:
        with config_file.open("r") as fh:
            for line in fh:
                config_file_.write(line)
    except FileNotFoundError:
        logger.info("No config file found at %s, using default configuration.", config_file)
    except OSError as e:
        logger.info("Error opening file %s: %s", config_file, e.args[0])
    config_file_.seek(0)
    config.read_file(config_file_)
    configuration = dict(config.items("FAKE_SECTION"))
    for boolean_field in ["avoid_duplicate_runs", "show_progress"]:
        if isinstance(config["FAKE_SECTION"][boolean_field], str):
            configuration[boolean_field] = config["FAKE_SECTION"].getboolean(boolean_field)  # type: ignore
    return configuration  # type: ignore


def get_config_as_dict() -> _Config:
    return {
        "apikey": apikey,
        "server": server,
        "cachedir": _root_cache_directory,
        "avoid_duplicate_runs": avoid_duplicate_runs,
        "connection_n_retries": connection_n_retries,
        "retry_policy": retry_policy,
        "show_progress": show_progress,
    }


# NOTE: For backwards compatibility, we keep the `str`
def get_cache_directory() -> str:
    """Get the current cache directory.

    This gets the cache directory for the current server relative
    to the root cache directory that can be set via
    ``set_root_cache_directory()``. The cache directory is the
    ``root_cache_directory`` with additional information on which
    subdirectory to use based on the server name. By default it is
    ``root_cache_directory / org / openml / www`` for the standard
    OpenML.org server and is defined as
    ``root_cache_directory / top-level domain / second-level domain /
    hostname``
    ```

    Returns
    -------
    cachedir : string
        The current cache directory.

    """
    url_suffix = urlparse(server).netloc
    reversed_url_suffix = os.sep.join(url_suffix.split(".")[::-1])  # noqa: PTH118
    return os.path.join(_root_cache_directory, reversed_url_suffix)  # noqa: PTH118


def set_root_cache_directory(root_cache_directory: str | Path) -> None:
    """Set module-wide base cache directory.

    Sets the root cache directory, wherin the cache directories are
    created to store content from different OpenML servers. For example,
    by default, cached data for the standard OpenML.org server is stored
    at ``root_cache_directory / org / openml / www``, and the general
    pattern is ``root_cache_directory / top-level domain / second-level
    domain / hostname``.

    Parameters
    ----------
    root_cache_directory : string
         Path to use as cache directory.

    See Also
    --------
    get_cache_directory
    """
    global _root_cache_directory  # noqa: PLW0603
    _root_cache_directory = Path(root_cache_directory)


start_using_configuration_for_example = (
    ConfigurationForExamples.start_using_configuration_for_example
)
stop_using_configuration_for_example = ConfigurationForExamples.stop_using_configuration_for_example


@contextmanager
def overwrite_config_context(config: dict[str, Any]) -> Iterator[_Config]:
    """A context manager to temporarily override variables in the configuration."""
    existing_config = get_config_as_dict()
    merged_config = {**existing_config, **config}

    _setup(merged_config)  # type: ignore
    yield merged_config  # type: ignore

    _setup(existing_config)


__all__ = [
    "get_cache_directory",
    "set_root_cache_directory",
    "start_using_configuration_for_example",
    "stop_using_configuration_for_example",
    "get_config_as_dict",
]

_setup()
