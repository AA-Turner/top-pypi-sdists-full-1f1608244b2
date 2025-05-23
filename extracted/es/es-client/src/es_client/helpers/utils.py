"""Deprecated es_client.helpers.utils module"""

# pylint: disable=W0401,W0614
import warnings
from ..utils import *

warnings.warn(
    (
        "es_client.helpers.utils is deprecated. Use es_client.utils instead. "
        "Will be removed in 9.0.0"
    ),
    DeprecationWarning,
    stacklevel=2,
)


# import typing as t
# import logging
# import os
# import re
# import base64
# import binascii
# from pathlib import Path
# import yaml  # type: ignore
# import click
# from elasticsearch8 import Elasticsearch
# from es_client.debug import debug, begin_end
# from es_client.defaults import ES_DEFAULT, config_schema
# from es_client.exceptions import ConfigurationError
# from es_client.helpers.schemacheck import SchemaCheck, password_filter

# logger = logging.getLogger(__name__)


# @begin_end()
# def check_config(config: dict, quiet: bool = False) -> dict:
#     """
#     :param config: The configuration

#     :returns: A validated configuration dictionary for
#         :py:class:`~.es_client.builder.Builder`

#     Ensure that the top-level key ``elasticsearch`` and its sub-keys, ``other_settings``
#     and ``client`` are contained in `config` before passing it (or empty defaults) to
#     :class:`~es_client.helpers.schemacheck.SchemaCheck` for value validation.
#     """
#     if not isinstance(config, dict):
#         logger.warning(
#             "Elasticsearch client configuration must be provided as a dictionary."
#         )
#         logger.warning('You supplied: "%s" which is "%s".', config, type(config))
#         logger.warning("Using default values.")
#         es_settings = ES_DEFAULT
#     elif "elasticsearch" not in config:
#         # I only need this to be logged when Builder is initializing
#         if not quiet:
#             logger.warning(
#                 'No "elasticsearch" setting in supplied configuration.  Using defaults.'
#             )
#         es_settings = ES_DEFAULT
#     else:
#         es_settings = config
#     for key in ["client", "other_settings"]:
#         if key not in es_settings["elasticsearch"]:
#             es_settings["elasticsearch"][key] = {}
#         else:
#             es_settings["elasticsearch"][key] = prune_nones(
#                 es_settings["elasticsearch"][key]
#             )
#     retval = SchemaCheck(
#         es_settings["elasticsearch"],
#         config_schema(),
#         "Elasticsearch Configuration",
#         "elasticsearch",
#     ).result()
#     debug.lv5(f'Return value = "{password_filter(retval)}"')
#     return retval


# @begin_end()
# def ensure_list(data) -> list:
#     """
#     :param data: A list or scalar variable to act upon

#     Return a :py:class:`list`, even if `data` is a single value
#     """
#     if not isinstance(data, list):  # in case of a single value passed
#         data = [data]
#     debug.lv5(f'Return value = "{data}"')
#     return data


# @begin_end()
# def file_exists(file: str) -> bool:
#     """
#     :param file: The file to test

#     Verify `file` exists
#     """
#     retval = Path(file).is_file()
#     debug.lv5(f'Return value = "{retval}"')
#     return retval


# @begin_end()
# def get_version(client: Elasticsearch) -> t.Tuple:
#     """
#     :param client: An Elasticsearch client object
#     :type client: :py:class:`~.elasticsearch.Elasticsearch`

#     :returns: The Elasticsearch version as a 3-part tuple, (major, minor, patch)

#     Get the Elasticsearch version of the connected node
#     """
#     version = client.info()["version"]["number"]
#     # Split off any -dev, -beta, or -rc tags
#     version = version.split("-")[0]
#     # Only take SEMVER (drop any fields over 3)
#     if len(version.split(".")) > 3:
#         version = version.split(".")[:-1]
#     else:
#         version = version.split(".")
#     retval = tuple(map(int, version))
#     debug.lv5(f'Return value = "{retval}"')
#     return retval


# @begin_end()
# def get_yaml(path: str) -> t.Dict:
#     """
#     :param path: The path to a YAML configuration file.

#     :returns: The contents of `path` translated from YAML to :py:class:`dict`

#     Read the file identified by `path` and import its YAML contents.
#     """
#     # Set the stage here to parse single scalar value environment vars from
#     # the YAML file being read
#     single = re.compile(r"^\$\{(.*)\}$")
#     yaml.add_implicit_resolver("!single", single)

#     def single_constructor(loader, node):
#         value = loader.construct_scalar(node)
#         proto = single.match(value).group(1)
#         default = None
#         if len(proto.split(":")) > 1:
#             envvar, default = proto.split(":")
#         else:
#             envvar = proto
#         return os.environ[envvar] if envvar in os.environ else default

#     yaml.add_constructor("!single", single_constructor)

#     try:
#         debug.lv4('TRY: yaml.load()')
#         retval = yaml.load(read_file(path), Loader=yaml.FullLoader)
#     except (yaml.scanner.ScannerError, yaml.parser.ParserError) as exc:
#         raise ConfigurationError(f"Unable to parse YAML file. Error: {exc}") from exc
#     debug.lv5('Return value = "<REDACTED YAML>"')
#     return retval


# def option_wrapper() -> t.Callable:
#     """
#     :py:func:`~.es_client.helpers.utils.passthrough()` the :py:func:`click.option`
#     decorator function.
#     """
#     return passthrough(click.option)


# @begin_end()
# def parse_apikey_token(token: str) -> t.Tuple:
#     """
#     :param token: The base64 encoded API Key

#     :returns: A tuple of (id, api_key)

#     Split a base64 encoded API Key Token into id and api_key
#     """
#     try:
#         debug.lv4('TRY: base64.b64decode()')
#         decoded = base64.b64decode(token).decode("utf-8")
#         split = decoded.split(":")
#     except (binascii.Error, IndexError, UnicodeDecodeError) as exc:
#         debug.lv3('Exiting function, raising exception')
#         debug.lv5(f'Value = "{exc}"')
#         logger.error(
#             "Unable to parse base64 API Key Token.  Ensure you are using the correct "
#             "format: <id>:<api_key>"
#         )
#         raise ConfigurationError(
#             f"Unable to parse base64 API Key Token: {exc}"
#         ) from exc
#     retval = (split[0], split[1])
#     debug.lv5('Return value = "<REDACTED API Key>"')
#     return retval


# def passthrough(func) -> t.Callable:
#     """Wrapper to make it easy to store click configuration elsewhere"""
#     return lambda a, k: func(*a, **k)


# @begin_end()
# def prune_nones(mydict: t.Dict) -> t.Dict:
#     """
#     :param mydict: The dictionary to act on

#     Remove keys from `mydict` whose values are `None`
#     """
#     # Test for `None` instead of existence or zero values will be caught
#     retval = dict([(k, v) for k, v in mydict.items() if v is not None and v != "None"])
#     debug.lv5(f'Return value = "{password_filter(retval)}"')
#     return retval


# @begin_end()
# def read_file(myfile: str) -> str:
#     """
#     :param myfile: A file to read.

#     Read a file and return the resulting data. Raise an
#     :py:exc:`~.es_client.exceptions.ConfigurationError` exception if the file is unable
#     to be read.
#     """
#     try:
#         debug.lv4('TRY: open() and read() file...')
#         with open(myfile, "r", encoding="utf-8") as f:
#             data = f.read()
#         debug.lv3('Exiting function, returning value')
#         debug.lv5('Value = "<REDACTED FILE>"')
#         return data
#     except IOError as exc:
#         msg = f"Unable to read file {myfile}. Exception: {exc}"
#         debug.lv3('Exiting function, raising exception')
#         logger.error(msg)
#         raise ConfigurationError(msg) from exc


# @begin_end()
# def verify_ssl_paths(args: t.Dict) -> None:
#     """
#     :param args: The ``client`` block of the config dictionary.

#     Verify that the various certificate/key paths are readable.  The
#     :py:func:`~.es_client.helpers.utils.read_file` function will raise a
#     :py:exc:`~.es_client.exceptions.ConfigurationError` if a file fails to be read.
#     """
#     # Test whether certificate is a valid file path
#     if "ca_certs" in args and args["ca_certs"] is not None:
#         read_file(args["ca_certs"])
#     # Test whether client_cert is a valid file path
#     if "client_cert" in args and args["client_cert"] is not None:
#         read_file(args["client_cert"])
#     # Test whether client_key is a valid file path
#     if "client_key" in args and args["client_key"] is not None:
#         read_file(args["client_key"])


# @begin_end()
# def verify_url_schema(url: str) -> str:
#     """
#     :param url: The url to verify

#     :returns: Verified URL

#     Ensure that a valid URL schema (HTTP[S]://URL:PORT) is used

#     Raise a :py:exc:`~.es_client.exceptions.ConfigurationError` exception if a URL
#     schema is invalid for any reason.
#     """
#     parts = url.lower().split(":")
#     errmsg = f"URL Schema invalid for {url}"
#     if len(parts) < 3:
#         # We do not have a port
#         if parts[0] == "https":
#             port = "443"
#         elif parts[0] == "http":
#             port = "80"
#         else:
#             debug.lv3('Exiting function, raising exception')
#             debug.lv5(f'Value = "{errmsg}"')
#             logger.error(f'Invalid URL schema: "{url}". Missing port?')
#             raise ConfigurationError(errmsg)
#     elif len(parts) == 3:
#         if (parts[0] != "http") and (parts[0] != "https"):
#             debug.lv3('Exiting function, raising exception')
#             debug.lv5(f'Value = "{errmsg}"')
#             logger.error(f'Invalid URL schema: "{url}"')
#             raise ConfigurationError(errmsg)
#         port = parts[2]
#     else:
#         debug.lv3('Exiting function, raising exception')
#         debug.lv5(f'Value = "{errmsg}"')
#         logger.error(f'Invalid URL schema: "{url}"')
#         raise ConfigurationError(errmsg)
#     retval = parts[0] + ":" + parts[1] + ":" + port
#     debug.lv5(f'Return value = "{retval}"')
#     return retval
