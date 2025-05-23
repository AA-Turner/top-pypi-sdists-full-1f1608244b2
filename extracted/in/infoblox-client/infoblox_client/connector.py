# Copyright 2015 Infoblox Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import functools
import re
import urllib
import requests
import six
import urllib3
import time
from requests import exceptions as req_exc

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

try:
    from oslo_log import log as logging
except ImportError:  # pragma: no cover
    import logging

try:
    from oslo_serialization import jsonutils
except ImportError:  # pragma: no cover
    import json as jsonutils

from infoblox_client import exceptions as ib_ex
from infoblox_client import utils

LOG = logging.getLogger(__name__)
CLOUD_WAPI_MAJOR_VERSION = 2


def reraise_neutron_exception(func):
    """This decorator catches third-party exceptions and replaces them with
    Infoblox exceptions"""

    @functools.wraps(func)
    def callee(*args, **kwargs):
        """Catches third-party exceptions and raises Infoblox exceptions"""
        try:
            return func(*args, **kwargs)
        except req_exc.Timeout as e:
            raise ib_ex.InfobloxTimeoutError(e, reason=e)
        except req_exc.RequestException as e:
            raise ib_ex.InfobloxConnectionError(reason=e)

    return callee


def retry_on_expired_cookie(func):
    """
    Decorator to handle expired cookies by re-authenticating
    and retrying the request.
    """
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function to handle expired cookies by re-authenticating
        and retrying the request.
        """
        try:
            return func(self, *args, **kwargs)
        except (req_exc.HTTPError, ib_ex.InfobloxBadWAPICredential,
                ib_ex.InfobloxFileDownloadFailed,
                ib_ex.InfobloxFileUploadFailed) as e:
            if isinstance(e, (req_exc.HTTPError,
                              ib_ex.InfobloxBadWAPICredential,
                              ib_ex.InfobloxFileDownloadFailed,
                              ib_ex.InfobloxFileUploadFailed)):
                LOG.warning("Bad WAPI credentials or Cookie timeout.\
                         Re-authenticating and retrying the request.")
            else:
                raise

            LOG.warning("Clearing cookies and re-authenticating.")
            self.session.cookies.clear()
            if hasattr(self, 'username') and hasattr(self, 'password'):
                LOG.warning("Re-authenticating with username and password.")
                self.session.auth = (self.username, self.password)
            elif hasattr(self, 'cert') and hasattr(self, 'key'):
                LOG.warning("Re-authenticating with client certificate.")
                self.session.cert = (self.cert, self.key)
            else:
                LOG.warning("No valid credentials found to re-authenticate.")
                raise ib_ex.InfobloxConfigException(
                    msg="No valid credentials found to re-authenticate.")
            return func(self, *args, **kwargs)
    return wrapper


class Connector(object):
    """Connector stands for interacting with Infoblox NIOS

    Defines methods for getting, creating, updating and
    removing objects from an Infoblox server instance.
    """

    DEFAULT_HEADER = {'Content-type': 'application/json'}
    DEFAULT_OPTIONS = {'ssl_verify': False,
                       'silent_ssl_warnings': False,
                       'http_request_timeout': 10,
                       'http_pool_connections': 10,
                       'http_pool_maxsize': 10,
                       'max_retries': 3,
                       'wapi_version': '2.10',
                       'max_results': None,
                       'log_api_calls_as_info': False,
                       'paging': False}

    def __init__(self, options):
        self._parse_options(options)
        self._configure_session()
        # urllib has different interface for py27 and py34
        try:
            self._urlencode = urllib.urlencode
            self._quote = urllib.quote
            self._urljoin = urlparse.urljoin
        except AttributeError:
            self._urlencode = urlparse.urlencode
            self._quote = urlparse.quote
            self._urljoin = urlparse.urljoin
        masked_options = utils.mask_sensitive_data(options)
        LOG.debug(
            "Connector initialized with options: {}".format(masked_options))

    def _parse_options(self, options):
        """Copy necessary options to self"""
        attributes = ('host', 'wapi_version', 'username', 'password',
                      'cert', 'key', 'ssl_verify', 'http_request_timeout',
                      'max_retries', 'http_pool_connections',
                      'http_pool_maxsize', 'silent_ssl_warnings',
                      'log_api_calls_as_info', 'max_results',
                      'paging')

        creds_basic_auth = ['username', 'password']
        creds_cert_auth = ['cert', 'key']
        creds = creds_basic_auth + creds_cert_auth

        for attr in attributes:
            if isinstance(options, dict) and \
                attr in options and \
                    options[attr] is not None:
                setattr(self, attr, options[attr])
            elif hasattr(options, attr):
                value = getattr(options, attr)
                setattr(self, attr, value)
            elif attr in self.DEFAULT_OPTIONS:
                setattr(self, attr, self.DEFAULT_OPTIONS[attr])
            elif attr not in creds:
                msg = "WAPI config error. Option %s is not defined" % attr
                LOG.error(msg)
                raise ib_ex.InfobloxConfigException(msg=msg)

        def check_creds(credentials):
            for attr in credentials:
                try:
                    getattr(self, attr)
                except AttributeError:
                    return False
            return True

        # If no basic and cert creds are provided, return an error
        if not check_creds(creds_basic_auth) and \
                not check_creds(creds_cert_auth):
            msg = "WAPI config error. Option either (username, password) " \
                  "or (cert, key) should be passed"
            LOG.error(msg)
            raise ib_ex.InfobloxConfigException(msg=msg)

        self.wapi_url = "https://%s/wapi/v%s/" % (self.host,
                                                  self.wapi_version)
        self.cloud_api_enabled = self.is_cloud_wapi(
            self.wapi_version)

    def _configure_session(self):
        LOG.debug("Configuring session")
        self.session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=self.http_pool_connections,
            pool_maxsize=self.http_pool_maxsize,
            max_retries=self.max_retries)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        if hasattr(self, 'username') and hasattr(self, 'password'):
            LOG.info("Authenticating with username and password.")
            self.session.auth = (self.username, self.password)
        else:
            self.session.cert = (self.cert, self.key)
            LOG.info("Authenticating with client certificate.")
        self.session.verify = utils.try_value_to_bool(self.ssl_verify,
                                                      strict_mode=False)
        LOG.debug("SSL verification is %s", self.session.verify)

        if self.silent_ssl_warnings:
            LOG.debug("Silencing SSL warnings")
            urllib3.disable_warnings()

    def _construct_url(self, relative_path, query_params=None,
                       extattrs=None, force_proxy=False):
        """
        Construct URL for Infoblox WAPI request
        """
        LOG.debug("Constructing URL for relative path: %s", relative_path)
        if query_params is None:
            query_params = {}
        if extattrs is None:
            extattrs = {}
        if force_proxy:
            LOG.debug("Forcing proxy search")
            query_params['_proxy_search'] = 'GM'

        if not relative_path or relative_path[0] == '/':
            raise ValueError('Path in request must be relative.')
        query = ''
        if query_params or extattrs:
            query = '?'

        if extattrs:
            attrs_queries = []
            for key, value in extattrs.items():
                param = "*%s" % key
                value = value['value']
                if isinstance(value, list):
                    for item in value:
                        attrs_queries.append(self._urlencode({param: item}))
                else:
                    attrs_queries.append(self._urlencode({param: value}))
            query += '&'.join(attrs_queries)
        if query_params:
            if len(query) > 1:
                query += '&'
            query += self._urlencode(query_params, doseq=True)

        base_url = self._urljoin(self.wapi_url,
                                 self._quote(relative_path))
        LOG.debug("Constructed URL: %s", base_url + query)
        return base_url + query

    @staticmethod
    def _validate_obj_type_or_die(obj_type, obj_type_expected=True):
        """Validate object type

        Args:
            obj_type_expected (bool): If False, method will assume, that object
                                      ref is passed as the first argument.
        """
        if not obj_type:
            raise ValueError('NIOS object type cannot be empty.')
        if obj_type_expected and '/' in obj_type:
            LOG.error(
                "NIOS object type cannot contain slash: {}".format(obj_type))
            raise ValueError('NIOS object type cannot contain slash.')

    @staticmethod
    def _validate_authorized(response):
        if response.status_code == requests.codes.UNAUTHORIZED:
            raise ib_ex.InfobloxBadWAPICredential(
                response=response.content,
                content=utils.format_html(response.content),
                code=response.status_code
            )

    @staticmethod
    def _build_query_params(payload=None, return_fields=None,
                            max_results=None, paging=False):
        if payload:
            query_params = payload
        else:
            query_params = dict()

        if return_fields:
            if 'default' in return_fields:
                return_fields.remove('default')
                query_params['_return_fields+'] = ','.join(return_fields)
            else:
                query_params['_return_fields'] = ','.join(return_fields)

        if max_results:
            query_params['_max_results'] = max_results

        if paging:
            query_params['_paging'] = 1
            query_params['_return_as_object'] = 1

        return query_params

    def is_cookie_expired(self):
        """
        Check if the cookie is expired by comparing the expiration time
        with the current time.
        """
        LOG.debug("Validating cookie expiration")
        cookie_jar = self.session.cookies
        for cookie in cookie_jar:
            if cookie.name == 'ibapauth':
                # Parse the cookie value
                cookie_value = cookie.value.strip('"')
                cookie_parts = {}
                for part in cookie_value.split(','):
                    if '=' in part:
                        key, value = part.split('=', 1)
                        cookie_parts[key] = value

                # Extract ctime and timeout
                ctime = int(cookie_parts.get('ctime', 0))
                timeout = int(cookie_parts.get('timeout', 0))

                # Calculate expiration time
                expiration_time = ctime + timeout

                # Get current time
                current_time = int(time.time())

                # Check if the cookie is expired
                return current_time > expiration_time
        return True  # If the cookie is not found, consider it expired

    def _get_request_options(self, data=None):
        opts = dict(timeout=self.http_request_timeout,
                    headers=self.DEFAULT_HEADER,
                    verify=self.session.verify)
        if data:
            opts['data'] = jsonutils.dumps(data)
        return opts

    def _validate_cookie(self):
        if self.is_cookie_expired():
            LOG.info("Cookie expired. \
            Clearing cookies and re-authenticating on the next request.")
            self.session.cookies.clear()
            if hasattr(self, 'username') and hasattr(self, 'password'):
                LOG.info("Re-authenticating with username and password.")
                self.session.auth = (self.username, self.password)
            elif hasattr(self, 'cert') and hasattr(self, 'key'):
                LOG.info("Re-authenticating with client certificate.")
                self.session.cert = (self.cert, self.key)
            else:
                LOG.warning("No valid credentials found to re-authenticate.")
                raise ib_ex.InfobloxConfigException(
                    msg="No valid credentials found to re-authenticate.")
        else:
            LOG.info("Using existing cookie for authentication")
            self.session.auth = None  # Do not re-authenticate

    @staticmethod
    def _parse_reply(request):
        """Tries to parse reply from NIOS.

        Raises exception with content if reply is not in json format
        """
        try:
            LOG.debug("WAPI Response: %s", request.content)
            return jsonutils.loads(request.content)
        except ValueError:
            LOG.error("Failed to parse reply from NIOS: %s", request.content)
            raise ib_ex.InfobloxConnectionError(reason=request.content)

    def _log_request(self, verb, url, opts):
        message = ("Sending %s request to %s with parameters %s",
                   verb, url, opts)
        if self.log_api_calls_as_info:
            LOG.info(*message)
        else:
            LOG.debug(*message)

    @reraise_neutron_exception
    @retry_on_expired_cookie
    def get_object(self, obj_type, payload=None, return_fields=None,
                   extattrs=None, force_proxy=False, max_results=None,
                   paging=None):
        """Retrieve a list of Infoblox objects of type 'obj_type'

        Some get requests like 'ipv4address' should be always
        proxied to GM on Hellfire
        If request is cloud and proxy is not forced yet,
        then plan to do two requests:
        - the first one is not proxied to GM
        - the second is proxied to GM

        Args:
            obj_type  (str): Infoblox object type, e.g. 'network',
                            'range', etc.
            payload (dict): Payload with data to send
            return_fields (list): List of fields to be returned
            extattrs      (dict): List of Extensible Attributes
            force_proxy   (bool): Set _proxy_search flag
                                  to process requests on GM
            max_results   (int): Maximum number of objects to be returned.
                If set to a negative number, the appliance will return an error
                when the number of returned objects would exceed the setting.
                The default is -1000. If this is set to a positive number,
                the results will be truncated when necessary.
            Paging (bool): Enables paging to wapi calls if paging = True,
                it uses _max_results to set paging size of the wapi calls.
                If _max_results is negative, it will take paging size as 1000.

        Returns:
            A list of the Infoblox objects requested
        Raises:
            requests.exceptions.HTTPError: If API responded with error HTTP
                status code.
        """
        self._validate_obj_type_or_die(obj_type, obj_type_expected=False)

        # max_results passed to get_object has priority over
        # one defined as connector option
        if max_results is None and self.max_results:
            max_results = self.max_results

        if paging is None:
            paging = self.paging if self.paging else False

        query_params = self._build_query_params(payload=payload,
                                                return_fields=return_fields,
                                                max_results=max_results,
                                                paging=paging)
        # Clear proxy flag if wapi version is too old (non-cloud)
        proxy_flag = self.cloud_api_enabled and force_proxy

        try:
            return self._handle_get_object(
                obj_type, query_params, extattrs, proxy_flag)
        except req_exc.HTTPError:
            LOG.warning(
                "Failed on object search with proxy flag %s", proxy_flag)
            # Do second get call with force_proxy if not done yet
            return self._handle_get_object(obj_type, query_params,
                                           extattrs, proxy_flag=True)

    def _handle_get_object(self, obj_type, query_params, extattrs,
                           proxy_flag=False):
        if '_paging' in query_params:

            if not ('_max_results' in query_params):
                query_params['_max_results'] = 1000

            if query_params['_max_results'] < 0:
                # Since pagination is enabled with _max_results < 0,
                # set _max_results = 1000.
                query_params['_max_results'] = 1000

            result = []
            while True:

                url = self._construct_url(obj_type, query_params, extattrs,
                                          force_proxy=proxy_flag)
                resp = self._get_object(obj_type, url)
                if not resp:
                    return None
                if not ('next_page_id' in resp):
                    result.extend(resp['result'])
                    query_params.pop('_page_id', None)
                    return result
                else:
                    query_params['_page_id'] = resp['next_page_id']
                    result.extend(resp['result'])
        else:
            url = self._construct_url(obj_type, query_params, extattrs,
                                      force_proxy=proxy_flag)
            return self._get_object(obj_type, url)

    def _get_object(self, obj_type, url):
        opts = self._get_request_options()
        self._log_request('get', url, opts)
        if self.session.cookies:
            # the first 'get' or 'post' action will generate a cookie
            # after that, we don't need to re-authenticate
            self._validate_cookie()
        r = self.session.get(url, **opts)

        self._validate_authorized(r)

        if r.status_code != requests.codes.ok:
            LOG.warning("Failed on object search with url %s: %s",
                        url, r.content)
            r.raise_for_status()
        return self._parse_reply(r)

    @reraise_neutron_exception
    @retry_on_expired_cookie
    def download_file(self, url):
        LOG.debug("Downloading file from %s", url)
        req_cookies = None
        if self.session.cookies:
            self._validate_cookie()
            cookies_dict = self.session.cookies.get_dict()
            ibapauth_cookie = cookies_dict.get('ibapauth', None)
            if ibapauth_cookie:
                req_cookies = {'ibapauth': ibapauth_cookie}
            else:
                req_cookies = None

        headers = {'content-type': 'application/force-download'}
        r = self.session.get(url, headers=headers, cookies=req_cookies)
        if r.status_code != requests.codes.ok:
            res_content = utils.format_html(r.content)
            LOG.error("Failed to download file from %s: %s", url, res_content)
            response = utils.safe_json_load(r.content)
            raise ib_ex.InfobloxFileDownloadFailed(
                response=response,
                url=url,
                content=res_content,
                code=r.status_code
            )
        return r

    @reraise_neutron_exception
    @retry_on_expired_cookie
    def upload_file(self, url, files):
        """Upload file to fully-qualified upload url

        Args:
            url (str): upload url provided by infoblox fileop uploadinit
            files (dict): file contents payload
        Returns:
            The requests response
        Raises:
            InfobloxException
        """
        LOG.debug("Uploading file to %s", url)
        req_cookies = None
        if self.session.cookies:
            self._validate_cookie()
            cookies_dict = self.session.cookies.get_dict()
            ibapauth_cookie = cookies_dict.get('ibapauth', None)
            if ibapauth_cookie:
                req_cookies = {'ibapauth': ibapauth_cookie}
            else:
                req_cookies = None
        r = self.session.post(url, files=files, cookies=req_cookies)
        if r.status_code != requests.codes.ok:
            response = utils.safe_json_load(r.content)
            res_content = utils.format_html(r.content)
            LOG.error("Failed to upload file to %s: %s", url, res_content)
            raise ib_ex.InfobloxFileUploadFailed(
                response=response,
                url=url,
                content=res_content,
                code=r.status_code,
            )
        return r

    @reraise_neutron_exception
    @retry_on_expired_cookie
    def create_object(self, obj_type, payload, return_fields=None):
        """Create an Infoblox object of type 'obj_type'

        Args:
            obj_type (str): Infoblox object type,
                            e.g. 'network', 'range', etc.
            payload (dict): Payload with data to send
            return_fields (list): List of fields to be returned
        Returns:
            The object reference of the new creation object
        Raises:
            InfobloxException
        """
        self._validate_obj_type_or_die(obj_type)

        query_params = self._build_query_params(return_fields=return_fields)

        url = self._construct_url(obj_type, query_params)
        opts = self._get_request_options(data=payload)
        self._log_request('post', url, opts)
        if self.session.cookies:
            # the first 'get' or 'post' action will generate a cookie
            # after that, we don't need to re-authenticate
            self._validate_cookie()
        r = self.session.post(url, **opts)

        self._validate_authorized(r)

        if r.status_code != requests.codes.CREATED:
            LOG.error(
                "Failed to create object with url %s: %s", url, r.content)
            response = utils.safe_json_load(r.content)
            already_assigned = 'is assigned to another network view'
            if response and already_assigned in response.get('text'):
                exception = ib_ex.InfobloxMemberAlreadyAssigned
            else:
                exception = ib_ex.InfobloxCannotCreateObject
            raise exception(
                response=response,
                obj_type=obj_type,
                content=r.content,
                args=payload,
                code=r.status_code)

        return self._parse_reply(r)

    def _check_service_availability(self, operation, resp, ref):
        if resp.status_code == requests.codes.SERVICE_UNAVAILABLE:
            raise ib_ex.InfobloxGridTemporaryUnavailable(
                response=resp.content,
                operation=operation,
                ref=ref,
                content=resp.content,
                code=resp.status_code)

    @reraise_neutron_exception
    @retry_on_expired_cookie
    def call_func(self, func_name, ref, payload, return_fields=None):
        LOG.debug("Calling function %s on object %s", func_name, ref)
        if self.session.cookies:
            self._validate_cookie()
        query_params = self._build_query_params(return_fields=return_fields)
        query_params['_function'] = func_name

        url = self._construct_url(ref, query_params)
        opts = self._get_request_options(data=payload)
        self._log_request('post', url, opts)
        r = self.session.post(url, **opts)

        self._validate_authorized(r)

        if r.status_code not in (requests.codes.CREATED,
                                 requests.codes.ok):
            self._check_service_availability('call_func', r, ref)

            raise ib_ex.InfobloxFuncException(
                response=jsonutils.loads(r.content),
                ref=ref,
                func_name=func_name,
                content=r.content,
                code=r.status_code)

        return self._parse_reply(r)

    @reraise_neutron_exception
    @retry_on_expired_cookie
    def update_object(self, ref, payload, return_fields=None):
        """Update an Infoblox object

        Args:
            ref      (str): Infoblox object reference
            payload (dict): Payload with data to send
            return_fields (list): List of fields to return
        Returns:
            The object reference of the updated object
        Raises:
            InfobloxException
        """
        query_params = self._build_query_params(return_fields=return_fields)

        opts = self._get_request_options(data=payload)
        url = self._construct_url(ref, query_params)
        self._log_request('put', url, opts)
        if self.session.cookies:
            self._validate_cookie()
        r = self.session.put(url, **opts)

        self._validate_authorized(r)

        if r.status_code != requests.codes.ok:
            self._check_service_availability('update', r, ref)

            raise ib_ex.InfobloxCannotUpdateObject(
                response=jsonutils.loads(r.content),
                ref=ref,
                content=r.content,
                code=r.status_code)

        return self._parse_reply(r)

    @reraise_neutron_exception
    @retry_on_expired_cookie
    def delete_object(self, ref, delete_arguments=None):
        """Remove an Infoblox object

        Args:
            ref               (str): Object reference
            delete_arguments (dict): Extra delete arguments
        Returns:
            The object reference of the removed object
        Raises:
            InfobloxException
        """
        opts = self._get_request_options()
        if not isinstance(delete_arguments, dict):
            delete_arguments = {}
        url = self._construct_url(ref, query_params=delete_arguments)
        self._log_request('delete', url, opts)
        if self.session.cookies:
            self._validate_cookie()
        r = self.session.delete(url, **opts)

        self._validate_authorized(r)

        if r.status_code != requests.codes.ok:
            self._check_service_availability('delete', r, ref)

            raise ib_ex.InfobloxCannotDeleteObject(
                response=jsonutils.loads(r.content),
                ref=ref,
                content=r.content,
                code=r.status_code)

        return self._parse_reply(r)

    @staticmethod
    def is_cloud_wapi(wapi_version):
        """Validate that a WAPI semantic version is valid.

        Args:
            wapi_version (str): WAPI semantic version

        Returns:
            True if the major version is higher than a given threshold,
            False otherwise.

        Raises:
            ValueError: if an invalid version is passed
        """
        valid = wapi_version and isinstance(wapi_version, six.string_types)
        if not valid:
            raise ValueError("Invalid argument was passed")
        version_match = re.search(r'(\d+)\.(\d+)', wapi_version)
        if version_match:
            if int(version_match.group(1)) >= CLOUD_WAPI_MAJOR_VERSION:
                LOG.debug("Cloud WAPI version detected: %s", wapi_version)
                return True
        LOG.debug("Non-cloud WAPI version detected: %s", wapi_version)
        return False
