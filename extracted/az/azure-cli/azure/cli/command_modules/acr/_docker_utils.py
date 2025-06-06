# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from urllib.parse import urlencode, urlparse, urlunparse

import time
from json import loads
from enum import Enum
from base64 import b64encode
import requests
from requests import RequestException
from requests.utils import to_native_string
from msrest.http_logger import log_request, log_response

from knack.util import CLIError
from knack.prompting import prompt, prompt_pass, NoTTYException
from knack.log import get_logger

from azure.cli.core.util import should_disable_connection_verify
from azure.cli.core.cloud import CloudSuffixNotSetException
from azure.cli.core._profile import _AZ_LOGIN_MESSAGE
from azure.cli.core.commands.client_factory import get_subscription_id
from azure.cli.core.azclierror import AzureResponseError

from ._client_factory import cf_acr_registries
from ._constants import get_managed_sku
from ._constants import ACR_AUDIENCE_RESOURCE_NAME
from ._utils import get_registry_by_name, ResourceNotFound
from .policy import acr_config_authentication_as_arm_show
from ._format import add_timestamp
from ._errors import CONNECTIVITY_TOOMANYREQUESTS_ERROR


logger = get_logger(__name__)


EMPTY_GUID = '00000000-0000-0000-0000-000000000000'
ALLOWED_HTTP_METHOD = ['get', 'patch', 'put', 'delete', 'post']
AAD_TOKEN_BASE_ERROR_MESSAGE = "Unable to get AAD authorization tokens with message"
ADMIN_USER_BASE_ERROR_MESSAGE = "Unable to get admin user credentials with message"
ALLOWS_BASIC_AUTH = "allows_basic_auth"


class RepoAccessTokenPermission(Enum):
    METADATA_READ = 'metadata_read'
    METADATA_WRITE = 'metadata_write'
    DELETE = 'delete'
    DELETED_READ = 'deleted_read'
    DELETED_RESTORE = 'deleted_restore'
    PULL = 'pull'
    PUSH = 'push'
    PULL_PUSH = '{},{}'.format(PULL, PUSH)
    META_WRITE_META_READ = '{},{}'.format(METADATA_WRITE, METADATA_READ)
    DELETE_META_READ = '{},{}'.format(DELETE, METADATA_READ)
    PULL_META_READ = '{},{}'.format(PULL, METADATA_READ)
    DELETED_READ_RESTORE = '{},{}'.format(DELETED_READ, DELETED_RESTORE)
    PULL_PUSH_META_WRITE_META_READ_DELETE = '{},{},{},{},{}'.format(PULL, PUSH, METADATA_WRITE, METADATA_READ, DELETE)


class RegistryAccessTokenPermission(Enum):
    CATALOG = 'catalog'
    DELETED_CATALOG = 'deleted_catalog'


class HelmAccessTokenPermission(Enum):
    PULL = 'pull'
    PUSH = 'push'
    DELETE = 'delete'
    PUSH_PULL = 'push,pull'
    DELETE_PULL = 'delete,pull'


def _handle_challenge_phase(login_server,
                            repository,
                            artifact_repository,
                            permission,
                            is_aad_token=True,
                            is_diagnostics_context=False):

    if repository and artifact_repository:
        raise ValueError("Only one of repository and artifact_repository can be provided.")

    repo_permissions = {permission.value for permission in RepoAccessTokenPermission}
    if repository and permission not in repo_permissions:
        raise ValueError(
            "Permission is required for a repository. Allowed access token permission: {}"
            .format(repo_permissions))

    helm_permissions = {permission.value for permission in HelmAccessTokenPermission}
    if artifact_repository and permission not in helm_permissions:
        raise ValueError(
            "Permission is required for an artifact_repository. Allowed access token permission: {}"
            .format(helm_permissions))

    login_server = login_server.rstrip('/')

    request_url = 'https://' + login_server + '/v2/'
    logger.debug(add_timestamp("Sending a HTTP Get request to {}".format(request_url)))
    challenge = requests.get(request_url, verify=not should_disable_connection_verify())

    if challenge.status_code != 401 or 'WWW-Authenticate' not in challenge.headers:
        from ._errors import CONNECTIVITY_CHALLENGE_ERROR
        if is_diagnostics_context:
            return CONNECTIVITY_CHALLENGE_ERROR.format_error_message(login_server)
        raise CLIError(CONNECTIVITY_CHALLENGE_ERROR.format_error_message(login_server).get_error_message())

    authenticate = challenge.headers['WWW-Authenticate']

    tokens = authenticate.split(' ', 2)

    if not is_aad_token and tokens[0].lower() == 'basic':
        return {ALLOWS_BASIC_AUTH: True}

    token_params = {y[0]: y[1].strip('"') for y in (x.strip().split('=', 2) for x in tokens[1].split(','))} \
        if len(tokens) >= 2 and tokens[0].lower() == 'bearer' else None

    if not token_params or 'realm' not in token_params or 'service' not in token_params:
        from ._errors import CONNECTIVITY_AAD_LOGIN_ERROR, CONNECTIVITY_WWW_AUTHENTICATE_ERROR
        error = CONNECTIVITY_AAD_LOGIN_ERROR if is_aad_token else CONNECTIVITY_WWW_AUTHENTICATE_ERROR

        if is_diagnostics_context:
            return error.format_error_message(login_server)
        raise CLIError(error.format_error_message(login_server).get_error_message())

    return token_params


def _get_aad_token_after_challenge(cli_ctx,
                                   token_params,
                                   login_server,
                                   only_refresh_token,
                                   repository,
                                   artifact_repository,
                                   permission,
                                   is_diagnostics_context,
                                   use_acr_audience,
                                   verify_user_permissions):
    authurl = urlparse(token_params['realm'])
    authhost = urlunparse((authurl[0], authurl[1], '/oauth2/exchange', '', '', ''))

    from azure.cli.core._profile import Profile
    profile = Profile(cli_ctx=cli_ctx)

    scope = None
    if use_acr_audience:
        logger.debug("Using ACR audience token for authentication")
        scope = "https://{}.azure.net".format(ACR_AUDIENCE_RESOURCE_NAME)

    # this might be a cross tenant scenario, so pass subscription to get_raw_token
    creds, _, tenant = profile.get_raw_token(subscription=get_subscription_id(cli_ctx),
                                             resource=scope)

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    content = {
        'grant_type': 'access_token',
        'service': token_params['service'],
        'tenant': tenant,
        'access_token': creds[1]
    }

    logger.debug(add_timestamp("Sending a HTTP Post request to {}".format(authhost)))
    response = requests.post(url=authhost, data=urlencode(content), headers=headers,
                             verify=not should_disable_connection_verify())

    if response.status_code == 429:
        if is_diagnostics_context:
            return CONNECTIVITY_TOOMANYREQUESTS_ERROR.format_error_message(login_server)
        raise AzureResponseError(CONNECTIVITY_TOOMANYREQUESTS_ERROR.format_error_message(login_server)
                                 .get_error_message())
    if response.status_code not in [200]:
        from ._errors import CONNECTIVITY_REFRESH_TOKEN_ERROR
        if is_diagnostics_context:
            return CONNECTIVITY_REFRESH_TOKEN_ERROR.format_error_message(login_server, response.status_code)
        raise CLIError(CONNECTIVITY_REFRESH_TOKEN_ERROR.format_error_message(login_server, response.status_code)
                       .get_error_message())

    refresh_token = loads(response.content.decode("utf-8"))["refresh_token"]
    if only_refresh_token:
        return refresh_token

    authhost = urlunparse((authurl[0], authurl[1], '/oauth2/token', '', '', ''))

    if repository:
        scope = 'repository:{}:{}'.format(repository, permission)
    elif artifact_repository:
        scope = 'artifact-repository:{}:{}'.format(artifact_repository, permission)
    else:
        # Registry level permissions only have * as permission, even for a read operation
        scope = 'registry:{}:*'.format(permission)
    content = {
        'grant_type': 'refresh_token',
        'service': login_server,
        'scope': scope,
        'refresh_token': refresh_token
    }

    logger.debug(add_timestamp("Sending a HTTP Post request to {}".format(authhost)))
    response = requests.post(url=authhost, data=urlencode(content), headers=headers,
                             verify=not should_disable_connection_verify())

    if response.status_code not in [200]:
        from ._errors import CONNECTIVITY_ACCESS_TOKEN_ERROR
        if is_diagnostics_context:
            return CONNECTIVITY_ACCESS_TOKEN_ERROR.format_error_message(login_server, response.status_code)
        raise CLIError(CONNECTIVITY_ACCESS_TOKEN_ERROR.format_error_message(login_server, response.status_code)
                       .get_error_message())

    access_token = loads(response.content.decode("utf-8"))["access_token"]
    if verify_user_permissions:
        return _verify_allowed_actions(access_token, permission, is_diagnostics_context)

    return access_token


def _verify_allowed_actions(access_token, permission, is_diagnostics_context):
    actions_value = None
    try:
        import jwt
        decoded_token = jwt.decode(access_token, options={"verify_signature": False})
        access_list = decoded_token.get("access", [])
        if isinstance(access_list, list):
            access_value = access_list[0] if access_list else {}
            actions_value = access_value.get('actions', [])
    except Exception as err:
        raise CLIError(f"Failed to decode access token: {str(err)}")

    required_actions = permission.split(',')

    if not actions_value or not isinstance(actions_value, list):
        missing_actions_value_str = _convert_action_list_to_str(required_actions)
        from ._errors import CONNECTIVITY_ACCESS_TOKEN_PERMISSIONS_ERROR

        if is_diagnostics_context:
            return CONNECTIVITY_ACCESS_TOKEN_PERMISSIONS_ERROR.format_error_message("no", missing_actions_value_str)
        raise CLIError(CONNECTIVITY_ACCESS_TOKEN_PERMISSIONS_ERROR.format_error_message("no", missing_actions_value_str)
                       .get_error_message())

    missing_actions_value = [action for action in required_actions if action not in actions_value]
    if missing_actions_value:
        missing_actions_value_str = _convert_action_list_to_str(missing_actions_value)
        allowed_actions_value_str = _convert_action_list_to_str(actions_value)
        from ._errors import CONNECTIVITY_ACCESS_TOKEN_PERMISSIONS_ERROR

        if is_diagnostics_context:
            return CONNECTIVITY_ACCESS_TOKEN_PERMISSIONS_ERROR.format_error_message(
                allowed_actions_value_str, missing_actions_value_str)
        raise CLIError(CONNECTIVITY_ACCESS_TOKEN_PERMISSIONS_ERROR.format_error_message(
            allowed_actions_value_str, missing_actions_value_str).get_error_message())

    return access_token


def _convert_action_list_to_str(actions):
    if len(actions) > 1:
        res = ', '.join(actions[:-1]) + ' and ' + actions[-1]
    else:
        res = ''.join(actions)
    return res


def _get_aad_token(cli_ctx,
                   login_server,
                   only_refresh_token,
                   repository=None,
                   artifact_repository=None,
                   permission=None,
                   is_diagnostics_context=False,
                   use_acr_audience=False,
                   verify_user_permissions=False):
    """Obtains refresh and access tokens for an AAD-enabled registry. Will return the allowed actions if
    verify_user_permissions is set to True.
    :param str login_server: The registry login server URL to log in to
    :param bool only_refresh_token: Whether to ask for only refresh token, or for both refresh and access tokens
    :param str repository: Repository for which the access token is requested
    :param str artifact_repository: Artifact repository for which the access token is requested
    :param str permission: The requested permission on the repository
    :param bool verify_user_permissions: Specifies whether to verify the allowed permissions in the access token.
    This is set to True when the --repository flag is used with the check-health command.
    """
    token_params = _handle_challenge_phase(
        login_server, repository, artifact_repository, permission, True, is_diagnostics_context
    )
    from ._errors import ErrorClass
    if isinstance(token_params, ErrorClass):
        if is_diagnostics_context:
            return token_params
        raise CLIError(token_params.get_error_message())

    return _get_aad_token_after_challenge(cli_ctx,
                                          token_params,
                                          login_server,
                                          only_refresh_token,
                                          repository,
                                          artifact_repository,
                                          permission,
                                          is_diagnostics_context,
                                          use_acr_audience,
                                          verify_user_permissions)


def _get_token_with_username_and_password(login_server,
                                          username,
                                          password,
                                          repository=None,
                                          artifact_repository=None,
                                          permission=None,
                                          is_login_context=False,
                                          is_diagnostics_context=False):
    """Decides and obtains credentials for a registry using username and password.
       To be used for scoped access credentials.
    :param str login_server: The registry login server URL to log in to
    :param bool only_refresh_token: Whether to ask for only refresh token, or for both refresh and access tokens
    :param str repository: Repository for which the access token is requested
    :param str artifact_repository: Artifact repository for which the access token is requested
    :param str permission: The requested permission on the repository, '*' or 'pull'
    """

    if is_login_context:
        return username, password

    token_params = _handle_challenge_phase(
        login_server, repository, artifact_repository, permission, False, is_diagnostics_context
    )

    from ._errors import ErrorClass
    if isinstance(token_params, ErrorClass):
        if is_diagnostics_context:
            return token_params
        raise CLIError(token_params.get_error_message())

    if ALLOWS_BASIC_AUTH in token_params:
        return username, password

    if repository:
        scope = 'repository:{}:{}'.format(repository, permission)
    elif artifact_repository:
        scope = 'artifact-repository:{}:{}'.format(artifact_repository, permission)
    else:
        # Registry level permissions only have * as permission, even for a read operation
        scope = 'registry:{}:*'.format(permission)

    authurl = urlparse(token_params['realm'])
    authhost = urlunparse((authurl[0], authurl[1], '/oauth2/token', '', '', ''))
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    content = {
        'service': token_params['service'],
        'grant_type': 'password',
        'username': username,
        'password': password,
        'scope': scope
    }

    logger.debug(add_timestamp("Sending a HTTP Post request to {}".format(authhost)))
    response = requests.post(url=authhost, data=urlencode(content), headers=headers,
                             verify=not should_disable_connection_verify())

    if response.status_code != 200:
        from ._errors import CONNECTIVITY_ACCESS_TOKEN_ERROR
        if is_diagnostics_context:
            return CONNECTIVITY_ACCESS_TOKEN_ERROR.format_error_message(login_server, response.status_code)
        raise CLIError(CONNECTIVITY_ACCESS_TOKEN_ERROR.format_error_message(login_server, response.status_code)
                       .get_error_message())

    access_token = loads(response.content.decode("utf-8"))["access_token"]

    return EMPTY_GUID, access_token


def _get_credentials(cmd,  # pylint: disable=too-many-statements
                     registry_name,
                     tenant_suffix,
                     username,
                     password,
                     only_refresh_token,
                     repository=None,
                     artifact_repository=None,
                     permission=None,
                     is_login_context=False,
                     resource_group_name=None):
    """Try to get AAD authorization tokens or admin user credentials.
    :param str registry_name: The name of container registry
    :param str tenant_suffix: The registry login server tenant suffix
    :param str username: The username used to log into the container registry
    :param str password: The password used to log into the container registry
    :param bool only_refresh_token: Whether to ask for only refresh token, or for both refresh and access tokens
    :param str repository: Repository for which the access token is requested
    :param str artifact_repository: Artifact repository for which the access token is requested
    :param str permission: The requested permission on the repository, '*' or 'pull'
    """
    # Raise an error if password is specified but username isn't
    if not username and password:
        raise CLIError('Please also specify username if password is specified.')

    cli_ctx = cmd.cli_ctx
    resource_not_found, registry = None, None
    try:
        registry, resource_group_name = get_registry_by_name(cli_ctx, registry_name, resource_group_name)
        login_server = registry.login_server
        if tenant_suffix:
            logger.warning(
                "Obtained registry login server '%s' from service. The specified suffix '%s' is ignored.",
                login_server, tenant_suffix)
    except (ResourceNotFound, CLIError) as e:
        resource_not_found = str(e)
        logger.debug("Could not get registry from service. Exception: %s", resource_not_found)
        if not isinstance(e, ResourceNotFound) and _AZ_LOGIN_MESSAGE not in resource_not_found:
            raise
        # Try to use the pre-defined login server suffix to construct login server from registry name.
        login_server_suffix = get_login_server_suffix(cli_ctx)
        if not login_server_suffix:
            raise
        login_server = '{}{}{}'.format(
            registry_name, '-{}'.format(tenant_suffix) if tenant_suffix else '', login_server_suffix).lower()

    # Validate the login server is reachable
    url = 'https://' + login_server + '/v2/'
    try:
        logger.debug(add_timestamp("Sending a HTTP Get request to {}".format(url)))
        challenge = requests.get(url, verify=not should_disable_connection_verify())
        if challenge.status_code == 403:
            raise CLIError("Looks like you don't have access to registry '{}'. "
                           "To see configured firewall rules, run 'az acr show --query networkRuleSet --name {}'. "
                           "To see if public network access is enabled, run 'az acr show --query publicNetworkAccess'."
                           "Please refer to https://aka.ms/acr/errors#connectivity_forbidden_error for more information."  # pylint: disable=line-too-long
                           .format(login_server, registry_name))
    except RequestException as e:
        logger.debug("Could not connect to registry login server. Exception: %s", str(e))
        if resource_not_found:
            logger.warning("%s\nUsing '%s' as the default registry login server.", resource_not_found, login_server)

        from .check_health import ACR_CHECK_HEALTH_MSG
        check_health_msg = ACR_CHECK_HEALTH_MSG.format(registry_name)
        raise CLIError("Could not connect to the registry login server '{}'. "
                       "Please verify that the registry exists and the URL '{}' is reachable from your environment.\n{}"
                       .format(login_server, url, check_health_msg))

    # 1. if username was specified, verify that password was also specified
    if username:
        if not password:
            try:
                password = prompt_pass(msg='Password: ')
            except NoTTYException:
                raise CLIError('Please specify both username and password in non-interactive mode.')

        username, password = _get_token_with_username_and_password(
            login_server, username, password, repository, artifact_repository, permission, is_login_context
        )
        return login_server, username, password

    # 2. if we don't yet have credentials, attempt to get a refresh token
    if not registry or registry.sku.name in get_managed_sku(cmd):
        logger.info("Attempting to retrieve AAD refresh token...")
        try:
            use_acr_audience = False

            if registry:
                aad_auth_policy = acr_config_authentication_as_arm_show(cmd, registry_name, resource_group_name)
                use_acr_audience = (aad_auth_policy and aad_auth_policy.status == 'disabled')

            return login_server, EMPTY_GUID, _get_aad_token(cli_ctx,
                                                            login_server,
                                                            only_refresh_token,
                                                            repository,
                                                            artifact_repository,
                                                            permission,
                                                            use_acr_audience=use_acr_audience)
        except CLIError as e:
            raise_toomanyrequests_error(str(e))
            logger.warning("%s: %s", AAD_TOKEN_BASE_ERROR_MESSAGE, str(e))

    # 3. if we still don't have credentials, attempt to get the admin credentials (if enabled)
    if registry:
        if registry.admin_user_enabled:
            logger.info("Attempting with admin credentials...")
            try:
                cred = cf_acr_registries(cli_ctx).list_credentials(resource_group_name, registry_name)
                return login_server, cred.username, cred.passwords[0].value
            except CLIError as e:
                logger.warning("%s: %s", ADMIN_USER_BASE_ERROR_MESSAGE, str(e))
        else:
            logger.warning("%s: %s", ADMIN_USER_BASE_ERROR_MESSAGE, "Admin user is disabled.")
    else:
        logger.warning("%s: %s", ADMIN_USER_BASE_ERROR_MESSAGE, resource_not_found)

    # 4. if we still don't have credentials, prompt the user
    try:
        username = prompt('Username: ')
        password = prompt_pass(msg='Password: ')
        username, password = _get_token_with_username_and_password(
            login_server, username, password, repository, artifact_repository, permission, is_login_context
        )
        return login_server, username, password
    except NoTTYException:
        raise CLIError(
            'Unable to authenticate using AAD or admin login credentials. ' +
            'Please specify both username and password in non-interactive mode.')

    return login_server, None, None


def raise_toomanyrequests_error(error):
    if CONNECTIVITY_TOOMANYREQUESTS_ERROR.error_title in error:
        raise AzureResponseError("{}: {}".format(AAD_TOKEN_BASE_ERROR_MESSAGE, error))


def get_login_credentials(cmd,
                          registry_name,
                          tenant_suffix=None,
                          username=None,
                          password=None,
                          resource_group_name=None):
    """Try to get AAD authorization tokens or admin user credentials to log into a registry.
    :param str registry_name: The name of container registry
    :param str username: The username used to log into the container registry
    :param str password: The password used to log into the container registry
    """
    return _get_credentials(cmd,
                            registry_name,
                            tenant_suffix,
                            username,
                            password,
                            only_refresh_token=True,
                            is_login_context=True,
                            resource_group_name=resource_group_name)


def get_access_credentials(cmd,
                           registry_name,
                           tenant_suffix=None,
                           username=None,
                           password=None,
                           repository=None,
                           artifact_repository=None,
                           permission=None,
                           resource_group_name=None):
    """Try to get AAD authorization tokens or admin user credentials to access a registry.
    :param str registry_name: The name of container registry
    :param str username: The username used to log into the container registry
    :param str password: The password used to log into the container registry
    :param str repository: Repository for which the access token is requested
    :param str artifact_repository: Artifact repository for which the access token is requested
    :param str permission: The requested permission on the repository
    """
    return _get_credentials(cmd,
                            registry_name,
                            tenant_suffix,
                            username,
                            password,
                            only_refresh_token=False,
                            repository=repository,
                            artifact_repository=artifact_repository,
                            permission=permission,
                            resource_group_name=resource_group_name)


def log_registry_response(response):
    """Log the HTTP request and response of a registry API call.
    :param Response response: The response object
    """
    log_request(None, response.request)
    log_response(None, response.request, RegistryResponse(response.request, response))


def get_login_server_suffix(cli_ctx):
    """Get the Azure Container Registry login server suffix in the current cloud."""
    try:
        return cli_ctx.cloud.suffixes.acr_login_server_endpoint
    except CloudSuffixNotSetException as e:
        logger.debug("Could not get login server endpoint suffix. Exception: %s", str(e))
        # Ignore the error if the suffix is not set, the caller should then try to get login server from server.
        return None


def _get_basic_auth_str(username, password):
    return 'Basic ' + to_native_string(
        b64encode(('%s:%s' % (username, password)).encode('latin1')).strip()
    )


def _get_bearer_auth_str(token):
    return 'Bearer ' + token


def get_authorization_header(username, password):
    """Get the authorization header as Basic auth if username is provided, or Bearer auth otherwise
    :param str username: The username used to log into the container registry
    :param str password: The password used to log into the container registry
    """
    if username == EMPTY_GUID:
        auth = _get_bearer_auth_str(password)
    else:
        auth = _get_basic_auth_str(username, password)
    return {'Authorization': auth}


def get_manifest_authorization_header(username, password):
    if username == EMPTY_GUID:
        auth = _get_bearer_auth_str(password)
    else:
        auth = _get_basic_auth_str(username, password)
    return {'Authorization': auth,
            'Accept': '*/*, application/vnd.oci.artifact.manifest.v1+json'
            ', application/vnd.cncf.oras.artifact.manifest.v1+json'
            ', application/vnd.oci.image.manifest.v1+json'
            ', application/vnd.oci.image.index.v1+json'
            ', application/vnd.docker.distribution.manifest.v2+json'
            ', application/vnd.docker.distribution.manifest.list.v2+json'}


# pylint: disable=too-many-statements
def request_data_from_registry(http_method,
                               login_server,
                               path,
                               username,
                               password,
                               result_index=None,
                               json_payload=None,
                               file_payload=None,
                               params=None,
                               manifest_headers=False,
                               raw=False,
                               retry_times=3,
                               retry_interval=5,
                               timeout=300):
    if http_method not in ALLOWED_HTTP_METHOD:
        raise ValueError("Allowed http method: {}".format(ALLOWED_HTTP_METHOD))

    if json_payload and file_payload:
        raise ValueError("One of json_payload and file_payload can be specified.")

    if http_method in ['get', 'delete'] and (json_payload or file_payload):
        raise ValueError("Empty payload is required for http method: {}".format(http_method))

    if http_method in ['patch', 'put'] and not (json_payload or file_payload):
        raise ValueError("Non-empty payload is required for http method: {}".format(http_method))

    url = 'https://{}{}'.format(login_server, path)

    if manifest_headers:
        headers = get_manifest_authorization_header(username, password)
    else:
        headers = get_authorization_header(username, password)

    for i in range(0, retry_times):
        errorMessage = None
        try:
            if file_payload:
                with open(file_payload, 'rb') as data_payload:
                    logger.debug(add_timestamp("Sending a HTTP {} request to {}".format(http_method, url)))
                    response = requests.request(
                        method=http_method,
                        url=url,
                        headers=headers,
                        params=params,
                        data=data_payload,
                        timeout=timeout,
                        verify=(not should_disable_connection_verify())
                    )
            else:
                logger.debug(add_timestamp("Sending a HTTP {} request to {}".format(http_method, url)))
                response = requests.request(
                    method=http_method,
                    url=url,
                    headers=headers,
                    params=params,
                    json=json_payload,
                    timeout=timeout,
                    verify=(not should_disable_connection_verify())
                )

            log_registry_response(response)

            if manifest_headers and raw and response.status_code == 200:
                return response.content.decode('utf-8'), None, response.status_code
            if response.status_code == 200:
                result = response.json()[result_index] if result_index else response.json()
                next_link = response.headers['link'] if 'link' in response.headers else None
                return result, next_link, response.status_code
            if response.status_code == 201 or response.status_code == 202:
                result = None
                try:
                    result = response.json()[result_index] if result_index else response.json()
                except ValueError as e:
                    logger.debug('Response is empty or is not a valid json. Exception: %s', str(e))
                return result, None, response.status_code
            if response.status_code == 204:
                return None, None, response.status_code
            if response.status_code == 401:
                raise RegistryException(
                    parse_error_message('Authentication required.', response),
                    response.status_code)
            if response.status_code == 404:
                raise RegistryException(
                    parse_error_message('The requested data does not exist.', response),
                    response.status_code)
            if response.status_code == 405:
                raise RegistryException(
                    parse_error_message('This operation is not supported.', response),
                    response.status_code)
            if response.status_code == 409:
                raise RegistryException(
                    parse_error_message('Failed to request data due to a conflict.', response),
                    response.status_code)
            raise Exception(parse_error_message('Could not {} the requested data.'.format(http_method), response))  # pylint: disable=broad-exception-raised
        except CLIError:
            raise
        except Exception as e:  # pylint: disable=broad-except
            errorMessage = str(e)
            logger.debug('Retrying %s with exception %s', i + 1, errorMessage)
            time.sleep(retry_interval)

    raise CLIError(errorMessage)


def parse_image_name(image, allow_digest=False, default_latest=True):
    if allow_digest and '@' in image:
        # This is probably an image name by manifest digest
        tokens = image.split('@')
        if len(tokens) == 2:
            return tokens[0], None, tokens[1]

    if ':' in image and '@' not in image:
        # This is probably an image name by tag
        tokens = image.split(':')
        if len(tokens) == 2:
            return tokens[0], tokens[1], None

    if ':' not in image and '@' not in image:
        # This is probably an image with implicit latest tag
        if default_latest:
            return image, 'latest', None

        return image, None, None

    if allow_digest:
        raise CLIError("The name of the image may include a tag in the format"
                       " 'name:tag' or digest in the format 'name@digest'.")
    raise CLIError("The name of the image may include a tag in the format 'name:tag'.")


def parse_error_message(error_message, response):
    import json
    try:
        server_error = json.loads(response.text)['errors'][0]
        if 'message' in server_error:
            server_message = server_error['message']
            if 'detail' in server_error and isinstance(server_error['detail'], str):
                server_details = server_error['detail']
                error_message = 'Error: {} Detail: {}'.format(server_message, server_details)
            else:
                error_message = 'Error: {}'.format(server_message)
    except (ValueError, KeyError, TypeError, IndexError):
        pass

    if not error_message.endswith('.'):
        error_message = '{}.'.format(error_message)

    try:
        correlation_id = response.headers['x-ms-correlation-request-id']
        return add_timestamp('{} Correlation ID: {}.'.format(error_message, correlation_id))
    except (KeyError, TypeError, AttributeError):
        return error_message


class RegistryException(CLIError):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code


class RegistryResponse:  # pylint: disable=too-few-public-methods
    def __init__(self, request, internal_response):
        self.request = request
        self.internal_response = internal_response
        self.status_code = internal_response.status_code
        self.headers = internal_response.headers
        self.encoding = internal_response.encoding
        self.reason = internal_response.reason
        self.content = internal_response.content

    def text(self):
        return self.content.decode(self.encoding or "utf-8")
