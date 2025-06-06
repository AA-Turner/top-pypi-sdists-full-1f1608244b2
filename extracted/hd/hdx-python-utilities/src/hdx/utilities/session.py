"""Session utilities for urls."""

import logging
import os
from typing import Any, Optional

import requests
from requests.adapters import HTTPAdapter
from requests_file import FileAdapter
from urllib3.util import Retry

from .encoding import basicauth_decode
from .loader import load_json, load_text, load_yaml
from .useragent import UserAgent

logger = logging.getLogger(__name__)


class SessionError(Exception):
    pass


def get_session(
    user_agent: Optional[str] = None,
    user_agent_config_yaml: Optional[str] = None,
    user_agent_lookup: Optional[str] = None,
    use_env: bool = True,
    fail_on_missing_file: bool = True,
    verify: bool = True,
    retry_attempts: int = 5,
    backoff_factor: int = 1,
    **kwargs: Any,
) -> requests.Session:
    """Set up and return Session object that is set up with retrying. Requires
    either global user agent to be set or appropriate user agent parameter(s)
    to be completed. If the EXTRA_PARAMS, BASIC_AUTH or BEARER_TOKEN
    environment variable is supplied, the extra_params* parameters will be
    ignored.

    Args:
        user_agent (Optional[str]): User agent string. HDXPythonUtilities/X.X.X- is prefixed.
        user_agent_config_yaml (Optional[str]): Path to YAML user agent configuration. Ignored if user_agent supplied. Defaults to ~/.useragent.yaml.
        user_agent_lookup (Optional[str]): Lookup key for YAML. Ignored if user_agent supplied.
        use_env (bool): Whether to read environment variables. Defaults to True.
        fail_on_missing_file (bool): Raise an exception if any specified configuration files are missing. Defaults to True.
        verify (bool): Whether to verify SSL certificates. Defaults to True.
        retry_attempts (int): Number of retry attempts. Defaults to 5.
        backoff_factor (int): Backoff factor for retry. Defaults to 1 (0s, 2s, 4s, 8s, 16s, 32s).
        **kwargs: See below
        auth (Tuple[str, str]): Authorisation information in tuple form (user, pass) OR
        basic_auth (str): Authorisation information in basic auth string form (Basic xxxxxxxxxxxxxxxx) OR
        basic_auth_file (str): Path to file containing authorisation information in basic auth string form (Basic xxxxxxxxxxxxxxxx) OR
        bearer_token (str): Bearer token string OR
        bearer_token_file (str): Path to file containing bearer token string OR
        extra_params_dict (Dict): Extra parameters to put on end of url as a dictionary OR
        extra_params_json (str): Path to JSON file containing extra parameters to put on end of url OR
        extra_params_yaml (str): Path to YAML file containing extra parameters to put on end of url
        extra_params_lookup (str): Lookup key for parameters. If not given assumes parameters are at root of the dict.
        headers (Dict): Additional headers to add to request.
        use_auth (str): If more than one auth found, specify which one to use, rather than failing.
        status_forcelist (ListTuple[int]): HTTP statuses for which to force retry. Defaults to (429, 500, 502, 503, 504).
        allowed_methods (ListTuple[str]): HTTP methods for which to force retry. Defaults to ("HEAD", "TRACE", "GET", "PUT", "OPTIONS", "DELETE").
    """
    s = requests.Session()
    s.verify = verify
    ua = kwargs.get("full_agent")
    if not ua:
        ua = UserAgent.get(
            user_agent, user_agent_config_yaml, user_agent_lookup, **kwargs
        )
    s.headers["User-Agent"] = ua

    auths_found = []
    headers = kwargs.get("headers")
    if headers is not None:
        s.headers.update(headers)
        if "Authorization" in headers:
            auths_found.append("headers")

    extra_params_found = False
    extra_params_dict = None
    basic_auth = None
    bearer_token = None
    if use_env:
        basic_auth_env = os.getenv("BASIC_AUTH")
        if basic_auth_env:
            basic_auth = basic_auth_env
            auths_found.append("BASIC_AUTH environment variable")
        bearer_token_env = os.getenv("BEARER_TOKEN")
        if bearer_token_env:
            bearer_token = bearer_token_env
            auths_found.append("BEARER_TOKEN environment variable")
        extra_params = os.getenv("EXTRA_PARAMS")
        if extra_params:
            if "=" in extra_params:
                extra_params_dict = {}
                logger.info("Loading extra parameters from environment variable")
                for extra_param in extra_params.split(","):
                    key, value = extra_param.split("=", maxsplit=1)
                    extra_params_dict[key] = value
            extra_params_found = True
    if not extra_params_found:
        # only do this if extra params env vars not supplied
        extra_params_dict = kwargs.get("extra_params_dict")
        if extra_params_dict:
            extra_params_found = True
            logger.info("Loading extra parameters from dictionary")

        extra_params_json = kwargs.get("extra_params_json", "")
        if extra_params_json:
            if extra_params_found:
                raise SessionError("More than one set of extra parameters given!")
            extra_params_found = True
            logger.info(f"Loading extra parameters from: {extra_params_json}")
            try:
                extra_params_dict = load_json(extra_params_json)
            except OSError:
                if fail_on_missing_file:
                    raise
        extra_params_yaml = kwargs.get("extra_params_yaml", "")
        if extra_params_yaml:
            if extra_params_found:
                raise SessionError("More than one set of extra parameters given!")
            logger.info(f"Loading extra parameters from: {extra_params_yaml}")
            try:
                extra_params_dict = load_yaml(extra_params_yaml)
            except OSError:
                if fail_on_missing_file:
                    raise
        extra_params_lookup = kwargs.get("extra_params_lookup")
        if extra_params_lookup and extra_params_dict:
            extra_params_dict = extra_params_dict.get(extra_params_lookup)
            if extra_params_dict is None:
                raise SessionError(
                    f"{extra_params_lookup} does not exist in extra_params!"
                )
    if extra_params_dict:
        basic_auth_param = extra_params_dict.get("basic_auth")
        bearer_token_param = extra_params_dict.get("bearer_token")
        if basic_auth_param:
            basic_auth = basic_auth_param
            auths_found.append("basic_auth parameter")
            del extra_params_dict["basic_auth"]
        if bearer_token_param:
            bearer_token = bearer_token_param
            auths_found.append("bearer_token parameter")
            del extra_params_dict["bearer_token"]

    s.params = extra_params_dict

    basic_auth_arg = kwargs.get("basic_auth")
    if basic_auth_arg:
        basic_auth = basic_auth_arg
        auths_found.append("basic_auth argument")
    bearer_token_arg = kwargs.get("bearer_token")
    if bearer_token_arg:
        bearer_token = bearer_token_arg
        auths_found.append("bearer_token argument")

    auth = kwargs.get("auth")
    if auth:
        auths_found.append("auth argument")
    basic_auth_file = kwargs.get("basic_auth_file")
    if basic_auth_file:
        logger.info(f"Loading basic auth from: {basic_auth_file}")
        try:
            basic_auth = load_text(basic_auth_file, strip=True)
            auths_found.append(f"file {basic_auth_file}")
        except OSError:
            if fail_on_missing_file:
                raise
    bearer_token_file = kwargs.get("bearer_token_file")
    if bearer_token_file:
        logger.info(f"Loading bearer token from: {bearer_token_file}")
        try:
            bearer_token = load_text(bearer_token_file, strip=True)
            auths_found.append(f"file {bearer_token_file}")
        except OSError:
            if fail_on_missing_file:
                raise
    if len(auths_found) > 1:
        use_auth = kwargs.get("use_auth")
        if use_auth is None:
            auths_found_str = ", ".join(auths_found)
            raise SessionError(
                f"More than one authorisation given! ({auths_found_str})"
            )
        else:
            if use_auth == "basic_auth":
                auth = basicauth_decode(basic_auth)
                s.auth = auth
            elif use_auth == "bearer_token":
                s.headers.update(
                    {
                        "Accept": "application/json",
                        "Authorization": f"Bearer {bearer_token}",
                    }
                )
            elif use_auth == "auth":
                s.auth = auth
    elif "headers" not in auths_found:
        if basic_auth:
            auth = basicauth_decode(basic_auth)
            s.auth = auth
        elif bearer_token:
            s.headers.update(
                {
                    "Accept": "application/json",
                    "Authorization": f"Bearer {bearer_token}",
                }
            )
        else:
            s.auth = auth

    status_forcelist = kwargs.get("status_forcelist", (429, 500, 502, 503, 504))
    allowed_methods = kwargs.get(
        "allowed_methods",
        ("HEAD", "TRACE", "GET", "PUT", "OPTIONS", "DELETE"),
    )

    retries = Retry(
        total=retry_attempts,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        allowed_methods=allowed_methods,
        raise_on_redirect=True,
        raise_on_status=True,
    )
    s.mount("file://", FileAdapter())
    httpadapter = HTTPAdapter(
        max_retries=retries, pool_connections=100, pool_maxsize=100
    )
    s.mount(
        "http://",
        httpadapter,
    )
    s.mount(
        "https://",
        httpadapter,
    )
    return s
