#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
# Aegis is your shield to protect you on the Brave New Web

# Python Imports
import asyncio
import base64
import copy
import datetime
import functools
import json
import logging
import operator
import os
import signal
import socket
import sys
import time
import traceback
import urllib

# Extern Imports
import pkg_resources
import pyreferrer
import requests
from tornado.options import options
import tornado.web
import tornado.platform.asyncio
import user_agents
import zlib

# Project Imports
import aegis.stdlib
import aegis.model
import aegis.config
import aegis.database
import aegis.build
import config


class AegisHandler(tornado.web.RequestHandler):

    def __init__(self, *args, **kwargs):
        # Initialize timer_obj on self, since this could be called before a subclass calls on self.timer_obj
        self._parent_timer = not hasattr(self, 'timer_obj')
        if not hasattr(self, 'timer_obj'):
            self.timer_obj = aegis.stdlib.TimerObj()
        if self._parent_timer:
            aegis.stdlib.timer_start(self.timer_obj, 'init')
        super(AegisHandler, self).__init__(*args, **kwargs)
        self.tmpl = {}
        self.tmpl['logw'] = self.logw = aegis.stdlib.logw
        hostname = self.request.host.split(':')[0]
        self.tmpl['host'] = hostname
        if not aegis.config.get('skip_hostname_check'):
            # Don't allow direct IP address in the Host header
            if aegis.stdlib.validate_ip_address(self.tmpl['host']):
                logging.warning("Disallow IP Address in Host Header: %s", self.tmpl['host'])
                raise tornado.web.HTTPError(400)
            # Implement *.domain.com to still work on domain.com
            host_split = hostname.split('.')
            valid_subdomains = aegis.config.get('valid_subdomains')
            if len(host_split) > 2 and valid_subdomains and host_split[0] not in valid_subdomains:
                self.tmpl['host'] = '.'.join(host_split[1:])
            # Ignore hostnames not in config.py. Only use the ones we have specified.
            if self.tmpl['host'] not in config.hostnames.keys():
                logging.warning("Ignore hostname not specified in config.py: %s", self.tmpl['host'])
                raise tornado.web.HTTPError(404)
        if not aegis.config.get('skip_apply_hostname'):
            config.apply_hostname(self.tmpl['host'])
        self.tmpl['host_config'] = config.hostnames[self.tmpl['host']]
        if not aegis.config.get('skip_hostname_check'):
            self.tmpl['domain'] = self.tmpl['host_config'].get('domain') or options.domain
        self.tmpl['options'] = options
        self.tmpl['program_name'] = options.program_name
        self.tmpl['app_name'] = options.app_name
        self.tmpl['env'] = config.get_env()
        self.tmpl['referer'] = self.request.headers.get('Referer')
        self.tmpl['user_agent'] = self.request.headers.get('User-Agent')
        self.tmpl['scheme'] = 'https://'
        #self.tmpl['xsrf_token'] = self.xsrf_token    # Maybe not needed anymore
        self.tmpl['nl2br'] = aegis.stdlib.nl2br
        self.tmpl['format_integer'] = aegis.stdlib.format_integer
        self.tmpl['get_user_id'] = self.get_user_id
        self.tmpl['get_member_id'] = self.get_member_id
        self.tmpl['get_member_email'] = self.get_member_email
        self.tmpl['get_current_user'] = self.get_current_user
        self.tmpl['utcnow'] = datetime.datetime.utcnow()
        self.tmpl['start_t'] = time.time()
        if self.cookie_get('session'):
            self.tmpl['session_ck'] = self.cookie_get('session')
        self.dbconn = None    # Set this to use it in model calls in webapp.py
        self.audit_session = {}
        self.audit_request = {}
        self.audit_relations = []
        self.models = {}
        self.models['UserAgent'] = aegis.model.UserAgent
        self.models['User'] = aegis.model.User
        # Initializing db takes ~5ms, then each read by ip takes about 0.3ms
        if aegis.config.get('geolite_path'):
            self.tmpl['geoip'] = aegis.stdlib.GeoLite(options.geolite_path).get_ip(self.request.remote_ip)
        if self._parent_timer:
            aegis.stdlib.timer_stop(self.timer_obj, 'init')

    def prepare(self):
        if self._parent_timer:
            aegis.stdlib.timer_start(self.timer_obj, 'prepare')
        self.set_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.set_header('Pragma', 'no-cache')
        self.set_header('Expires', 'Fri, 21 Dec 2012 03:08:13 GMT')
        self.tmpl['request_name'] = self.page_name = '%s.%s' % (self.__class__.__name__, self.request.method)
        self.tmpl['next_url'] = self.get_next_url()
        self.request.args = dict([(key, self.get_argument(key, strip=False)) for key, val in self.request.arguments.items()])
        self.setup_user()
        self.track_email()
        # Enable/Disable auditing. Allow for host-specific override in config.py hostnames. Else just use from options.use_audit, or False. Disable for admin_member_id.
        self.use_audit = False
        if aegis.config.exists('use_audit'):
            self.use_audit = self.tmpl['host_config'].get('use_audit') or options.use_audit
            # When admin is logged in as someone else, don't use_audit
            auth_ck = self.cookie_get('auth')
            if auth_ck and type(auth_ck) is dict and auth_ck.get('admin_member_id'):
                self.use_audit = False
        if self.use_audit:
            self.set_marketing_id()
            self.audit_start()
        super(AegisHandler, self).prepare()
        if self._parent_timer:
            aegis.stdlib.timer_stop(self.timer_obj, 'prepare')

    def finish(self, chunk=None):
        # Fail fast for maintenance errors
        if self.get_status() in (503,):
            super(AegisHandler, self).finish(chunk)
            return
        if self._parent_timer:
            aegis.stdlib.timer_start(self.timer_obj, 'finish')
        auth_ck = self.cookie_get('auth')
        logged_out = (self.tmpl.get('logged_out') == True)
        if auth_ck and not logged_out:
            # If there's a member_auth, refresh the expiration in the backend along with the cookie
            if hasattr(self, '_member_auth'):
                self._member_auth.refresh(options.cookie_durations['auth'] * 86400)
            # Update auth cookie as long as it isn't being overwritten
            new_cookie_value = None
            if hasattr(self, "_new_cookie"):
                new_cookie_value = self._new_cookie.get(self.cookie_name('auth'))
            if not new_cookie_value:
                self.cookie_set('auth', auth_ck)
            else:
                new_cookie_value = new_cookie_value.value.split(':')[-1].split('|')[0]
                decoded = self.cookie_decode(base64.b64decode(new_cookie_value))
                if decoded == auth_ck:
                    self.cookie_set('auth', auth_ck)
        if 'session_ck' in self.tmpl:
            if self.tmpl.get('session_ck'):
                self.cookie_set('session', self.tmpl['session_ck'])
            else:
                self.cookie_clear('session')
        # Cookie Debug
        if aegis.config.get('cookie_debug'):
            cookies = []
            if hasattr(self, "_new_cookie"):
                for cookie in self._new_cookie.values():
                    cookies.append("Set-Cookie: %s" % cookie.OutputString(None))
            self.logw(cookies, "HTTP Reponse Set-Cookie Header")
        if self._parent_timer:
            aegis.stdlib.timer_stop(self.timer_obj, 'finish')
        super(AegisHandler, self).finish(chunk)

    def on_finish(self):
        # This runs after the response has been sent to the client, intended for cleanup.
        if hasattr(self, 'use_audit') and self.use_audit:
            self.audit_request_id = self.audit_finish()

    def debug_request(self):
        req_str = str(self.request).rstrip(')') + ', headers={'
        for header in sorted(self.request.headers.items()):
            req_str += "'%s': '%s', " % header
        req_str = "%s})" % req_str.rstrip(', ')
        logging.warning(req_str)

    def setup_user(self):
        # Set up user-cookie tracking system, based on user-agent. This function takes ~2-5ms depending on cpu and database speed and latency.
        if not self.tmpl['user_agent']:
            self.tmpl['user_agent'] = 'NULL USER AGENT'
        self.tmpl['user_agent_obj'] = ua = user_agents.parse(self.tmpl['user_agent'])
        ua_json = {'is_mobile': ua.is_mobile, 'is_tablet': ua.is_tablet, 'is_pc': ua.is_pc, 'is_touch': ua.is_touch_capable,
                   'is_email': ua.is_email_client, 'is_robot': ua.is_bot,
                   'os_name': ua.get_os(), 'os_family': ua.os.family, 'os_version': ua.os.version_string,
                   'browser_name': ua.get_browser(), 'browser_family': ua.browser.family, 'browser_version': ua.browser.version_string}
        if not (aegis.config.get('pg_database') or aegis.config.get('mysql_database')) and not self.dbconn:
            return
        user_agent = self.models['UserAgent'].set_user_agent(self.tmpl['user_agent'], dbconn=self.dbconn)
        # if ua_json not set, set it
        if not user_agent['user_agent_json'] and ua_json:
            ua_json = json.dumps(ua_json, cls=aegis.stdlib.DateTimeEncoder)
            user_agent.set_ua_json(ua_json, dbconn=self.dbconn)
        if self.user_is_robot():
            self.models['UserAgent'].set_robot_ind(user_agent['user_agent_id'], True, dbconn=self.dbconn)
            user_agent = self.models['UserAgent'].get_id(user_agent['user_agent_id'], dbconn=self.dbconn)
        # Set up all robots to use the same user_id, based on the user-agent string, and don't bother with cookies.
        # Regular users just get tagged with a user cookie matching a row.
        user = None
        if user_agent['robot_ind']:
            if not user_agent['robot_user_id']:
                user_id = self.models['User'].insert(user_agent['user_agent_id'], dbconn=self.dbconn)
                self.models['UserAgent'].set_robot_user_id(user_agent['user_agent_id'], user_id, dbconn=self.dbconn)
                user_agent = self.models['UserAgent'].get_id(user_agent['user_agent_id'], dbconn=self.dbconn)
            user = self.models['User'].get_id(user_agent['robot_user_id'], dbconn=self.dbconn)
            user_ck = {}
            self.tmpl['user_row'] = user
        else:
            # Check if the cookie exists, and if the record exists. If either doesn't exist, start a new user record.
            user_ck = self.cookie_get('user')
            if user_ck and user_ck.get('user_id'):
                user = self.models['User'].get_id(user_ck['user_id'], dbconn=self.dbconn)
                self.tmpl['user_row'] = user
                if user:
                    self.cookie_set('user', user_ck)
            if not user:
                user_id = self.models['User'].insert(user_agent['user_agent_id'], dbconn=self.dbconn)
                user = self.models['User'].get_id(user_id, dbconn=self.dbconn)
                self.tmpl['user_row'] = user
                if user_ck:
                    user_ck['user_id'] = user_id
                else:
                    user_ck = {'user_id': user_id}
                self.cookie_set('user', user_ck)
        self.tmpl['user'] = {}
        if user:
            self.tmpl['user']['user_id'] = user['user_id']
        # At the end leave the row behind for later use in the request
        self.tmpl['user_agent_row'] = user_agent
        self.tmpl['show_cookie_banner'] = not (self.tmpl.get('user_row') and self.tmpl['user_row'].get('preferences') and self.tmpl['user_row']['preferences'].get('cookie_ok_dttm'))

    def enforce_admin(self):
        if not self.is_super_admin():
            raise tornado.web.HTTPError(403)

    def user_is_robot(self):
        # If this fails so early that setup_user() doesn't run, just parse the user_agent here
        if not self.tmpl.get('user_agent_obj'):
            self.tmpl['user_agent_obj'] = user_agents.parse(self.tmpl['user_agent'])
        return bool(self.tmpl['user_agent_obj'].is_bot or aegis.stdlib.is_robot(self.tmpl['user_agent']))

    def get_template_path(self):
        return self.tmpl['host_config'].get('template_path') or options.template_path

    def render(self, template_name, **kwargs):
        aegis.stdlib.timer_start(self.timer_obj, 'render')
        # XXX template_path seems unused...
        #template_path = self.tmpl['host_config'].get('template_path') or options.template_path
        #template_path = os.path.join(template_path, template_name)
        # Override parent class render to remove the embeds and instrument a timer here. Copied in from tornado/web.py render()
        if self._finished:
            raise RuntimeError("Cannot render() after finish()")
        html = self.render_string(template_name, **kwargs)
        aegis.stdlib.timer_stop(self.timer_obj, 'render')
        self.finish(html)

    def render_path(self, template_name, **kwargs):
        template_path = os.path.join(self.get_template_path(), template_name)
        self.render(template_path, **kwargs)

    def _handle_request_exception(self, ex):
        if type(ex) in (aegis.database.PgsqlAdminShutdown, aegis.database.PgsqlOperationalError, aegis.database.MysqlOperationalError, aegis.database.MysqlInterfaceError):
            logging.error("Error connecting to: %s", aegis.config.get('pg_database') or aegis.config.get('mysql_database'))
            logging.exception(ex)
            logging.error("Database is down. Send HTTP 503.")
            self.exception_alert(ex)
            self.send_error(503)
            return
        if aegis.config.get('pg_database') or aegis.config.get('mysql_database'):
            aegis.model.db().close()  # Closing database effectively does a transaction ROLLBACK
        #self.logw(ex, "EX")
        #logging.exception(ex)
        # Remove cookie info to anonymize and make message shorter and more useful. Almost never used in debug.
        if self.request.headers.get('Cookie'):
            del self.request.headers['Cookie']
        # Don't post boring pseudo-errors to channels
        if isinstance(ex, tornado.web.HTTPError) and ex.status_code == 400 and 'No CSRF token in Cookie' in ex.log_message:
            #logging.warning("Prevent CSRF token errors from POSTing to Chat")
            super(AegisHandler, self)._handle_request_exception(ex)
            return
        if isinstance(ex, tornado.web.HTTPError) and ex.status_code in [401, 403, 404, 405, 410]:
            logging.warning("Prevent annoying errors from POSTing to Chat")
            super(AegisHandler, self)._handle_request_exception(ex)
            return
        self.exception_alert(ex)

    def exception_alert(self, ex):
        # Send errors to chat hooks, based on them being configured for the environment
        header = "`[%s ENV   %s   %s   uid: %s   mid: %s]`" % (config.get_env().upper(), self.request.uri, self.tmpl['request_name'], self.get_user_id() or '-', self.get_member_id() or '-')
        template_opts = {'handler': self, 'traceback': traceback.format_exc(), 'kwargs': {}, 'header': header}
        template_opts['kwargs']['user_agent'] = self.tmpl['user_agent']
        template_opts['kwargs']['remote_ip'] = self.request.remote_ip
        if hasattr(self, 'audit_request'):
            template_opts['kwargs']['country_cd'] = self.audit_request.get('country_cd', 'N/A')
            template_opts['kwargs']['region_cd'] = self.audit_request.get('region_cd', 'N/A')
        if hasattr(self, 'audit_session'):
            template_opts['kwargs']['audit_session_id'] = self.audit_session.get('audit_session_id')
        template_opts['kwargs']['robot'] = self.user_is_robot()
        template_opts['kwargs']['Python UTC Now'] = self.tmpl['utcnow'].strftime('%Y-%m-%dT%H:%M:%S')
        error_message = self.render_string("error_message.txt", **template_opts).decode('utf-8')
        if config.get_env() == 'prod':
            hooks = ['alerts_chat_hook']
        else:
            hooks = ['debug_chat_hook']
        for hook in hooks:
            hook_url = aegis.config.get(hook)
            # Call own function? So the client can write custom error messages.
            if hook_url:
                requests.post(hook_url, json={"text": error_message})
        super(AegisHandler, self)._handle_request_exception(ex)

    def get_next_url(self, default_url='/'):
        next_url = self.get_argument('next', None)
        url_parts = aegis.stdlib.validate_url(next_url)
        if not url_parts:
            return default_url
        url_str = urllib.parse.urlunparse(url_parts)
        if url_str:
            return tornado.escape.url_unescape(url_str)
        return default_url

    def get_url_next(self, url):
        # Validate and parse uri
        url_parts = urllib.parse.urlparse(url)
        url_parts = url_parts._replace(scheme='https', netloc=self.tmpl['domain'])
        url_str = urllib.parse.urlunparse(url_parts)
        url_parts = aegis.stdlib.validate_url(url_str)
        if not url_parts:
            return
        # Remove ?next= param in query string to prevent looping
        query_dict = urllib.parse.parse_qs(url_parts.query)
        if 'next' in query_dict:
            del query_dict['next']
        query_params = urllib.parse.urlencode(query_dict, doseq=True)
        url_parts = url_parts._replace(query=query_params)
        next_url = urllib.parse.urlunparse(url_parts)
        return next_url


    # Cookie Handling
    def cookie_encode(self, val):
        return tornado.escape.url_escape(tornado.escape.json_encode(val))

    def cookie_decode(self, val):
        if val is None:
            return None
        unescaped_val = tornado.escape.url_unescape(val)
        if unescaped_val == '':
            return unescaped_val
        ck = tornado.escape.json_decode(unescaped_val)
        if type(ck) is dict:
            ck = dict([(str(key), ck[key]) for key in ck])
        return ck

    def cookie_name(self, name):
        if self.tmpl['env'] in ('prod', 'prod-admin'):
            return name
        # Authentication for special -admin environment to use cookies from the main env
        if self.tmpl['env'].endswith('-admin'):
            name = "%s_%s" % (self.tmpl['env'].rsplit('-', maxsplit=1)[0], name)
        else:
            name = "%s_%s" % (self.tmpl['env'], name)
        return name

    def cookie_set(self, name, value, cookie_duration=None):
        # Session cookie is set to None duration to implement a browser session cookie
        if not cookie_duration:
            cookie_durations = aegis.config.get('cookie_durations')
            if not cookie_durations:
                cookie_durations = {'user': 3650, 'session': None, 'auth': 90}
            cookie_duration = cookie_durations[name]
        cookie_flags = {'httponly': True, 'secure': True, 'samesite': 'Lax'}
        hostname = self.tmpl['host_config'].get('hostname') or options.hostname
        if hostname == 'localhost':
            cookie_flags['secure'] = False
        # XXX Way to not set httponly for reading in javascript
        cookie_val = self.cookie_encode(value)
        cookie_domain = hostname
        self.set_secure_cookie(self.cookie_name(name), cookie_val, expires_days=cookie_duration, domain=cookie_domain, **cookie_flags)

    def cookie_get(self, name, cookie_duration=None):
        # Session cookie is set to 30 since browser should expire session cookie not time-limit
        if not cookie_duration:
            cookie_durations = aegis.config.get('cookie_durations')
            if not cookie_durations:
                cookie_durations = {'user': 3650, 'session': 30, 'auth': 90}
            cookie_duration = cookie_durations[name]
        cookie_val = self.get_secure_cookie(self.cookie_name(name), max_age_days=cookie_duration)
        cookie_val = tornado.escape.to_basestring(cookie_val)
        cookie_val = self.cookie_decode(cookie_val)
        return cookie_val

    def cookie_clear(self, name):
        domain = self.tmpl['host_config'].get('hostname') or options.hostname
        self.clear_cookie(self.cookie_name(name), domain=domain)


    # Authentication
    def get_user_id(self):
        return self.tmpl.get('user', {}).get('user_id')

    def member_auth(self, member_auth_type_id, member_id, email_id, register_flag=False, login_flag=False):
        auth_duration_sec = options.cookie_durations['auth'] * 86400
        member_auth = {'member_auth_type_id': member_auth_type_id, 'email_id': email_id, 'register_flag': bool(register_flag), 'login_flag': bool(login_flag),
                       'member_id': member_id, 'user_id': self.get_user_id(), 'ip_address': self.request.remote_ip,
                       'expire_dttm': datetime.datetime.utcnow() + datetime.timedelta(seconds=auth_duration_sec)}
        return aegis.model.MemberAuth.insert(**member_auth)

    def validate_member_auth_ck(self):
        # Cookie can't change mid-request so we can just cache the value on the handler
        if hasattr(self, '_member_id') and hasattr(self, '_member_auth_id') and hasattr(self, '_member_auth'):
            return (self._member_id, self._member_auth_id, self._member_auth)
        # No cookie, no authie
        if not self.cookie_get("auth"):
            return None
        # Default is to only have a member_id. Alternately member_id|member_auth_id|magic_token
        self._member_id = aegis.stdlib.validate_int(self.cookie_get("auth"))
        if self._member_id:
            return self._member_id
        # Unpack and check the auth and token
        member_id, member_auth_id, magic_token = self.cookie_get("auth").split('|')
        member_id = aegis.stdlib.validate_int(member_id)
        member_auth_id = aegis.stdlib.validate_int(member_auth_id)
        member_auth = None
        if member_id and member_auth_id:
            member_auth = aegis.model.MemberAuth.get_auth(member_id, member_auth_id, magic_token)
        if not member_auth:
            raise Exception("MemberAuth doesn't match, is expired, or is deleted: %s|%s|%s" % (member_id, member_auth_id, magic_token))
        self._member_id = member_id
        self._member_auth_id = member_auth_id
        self._member_auth = member_auth
        return (self._member_id, self._member_auth_id, self._member_auth)

    def get_member_id(self):
        # Cookie can't change mid-request so we can just cache the value on the handler
        logged_out = (self.tmpl.get('logged_out') == True)
        if logged_out:
            return None
        if hasattr(self, '_member_id') and not logged_out:
            return self._member_id
        # When not on production, if test token and test member_id are present, use that for the request.
        test_token = self.request.headers.get('Test-Token')
        test_member_id = aegis.stdlib.validate_int(self.request.headers.get('Test-Member-Id'))
        if self.tmpl['env'] != 'prod' and test_token and test_token == options.test_token and test_member_id:
            # Check member exists so we don't just explode from exuberant testing!
            if aegis.model.Member.get_id(test_member_id):
                logging.warning("Test Mode | MemberId Override: %s", test_member_id)
                self._member_id = test_member_id
                return self._member_id
        ck = self.cookie_get("auth")
        #self.logw(ck, "Auth Cookie")
        if ck:
            try:
                if aegis.config.get('use_server_logout'):
                    self.validate_member_auth_ck()
                else:
                    self._member_id = int(ck)
                return self._member_id
            except Exception as ex:
                logging.exception(ex)
                self.del_current_user()
                return None

    def set_current_user(self, member_id, member_auth_id=None, magic_token=None, get_auth_fn=aegis.model.Member.get_auth):
        cookie_val = int(member_id)
        if member_auth_id and magic_token:
            cookie_val = '%s|%s|%s' % (member_id, member_auth_id, magic_token)
        self.cookie_set('auth', cookie_val)
        self.tmpl['member'] = get_auth_fn(member_id)

    def get_current_user(self, get_auth_fn=aegis.model.Member.get_auth):
        if not aegis.database.pgsql_available and not aegis.database.mysql_available:
            return None
        if self.tmpl.get('member'):
            return self.tmpl['member']
        if self.get_member_id():
            self.tmpl['member'] = get_auth_fn(self.get_member_id(), dbconn=self.dbconn)
            return self.tmpl['member']

    def get_member_email(self, get_auth_fn=aegis.model.Member.get_auth):
        if not aegis.database.pgsql_available and not aegis.database.mysql_available:
            return None
        if 'member' not in self.tmpl:
            self.get_current_user(get_auth_fn=get_auth_fn)
        if self.tmpl['member'] and self.tmpl['member'].get('email'):
            return self.tmpl['member']['email']['email']
        logging.error("No email for this member. Does get_member_email() need to be overridden in a subclass? Is self.get_current_user() overridden in a subclass?")

    def del_current_user(self):
        # check if member_auth record exists, if so delete it, but don't explode if it doesn't match
        try:
            self.validate_member_auth_ck()
        except Exception as ex:
            logging.exception(ex)
            logging.error("This *should* be an unusual case, when cookies aren't matching. Cookies will be cleared now.")
        if aegis.config.get('use_server_logout') and hasattr(self, '_member_auth'):
            self._member_auth.revoke()
        self.cookie_clear('auth')
        self.tmpl['logged_out'] = True
        self.audit_session_end()

    def email_link_auth(self, email_link_id, token, email_type=None):
        if not aegis.stdlib.validate_token(email_link_id, token):
            return {'error_message': "Invalid Parameters"}
        # Fetch Email Link and do sanity check
        email_link = aegis.model.EmailLink.get_id_token(email_link_id, token)
        if not email_link:
            return {'error_message': "No Magic Link"}
        if email_link['delete_dttm'] or email_link['access_dttm']:
            return {'error_message': "Already Accessed"}
        # If email_type is present, checks that the token is of the same email_type
        if email_type:
            email_tracking = aegis.model.EmailTracking.get_id(email_link['email_tracking_id'])
            if email_type['email_type_id'] != email_tracking['email_type_id']:
                return {'error_message': "Wrong Email Type"}
        # Mark email accessed and fetch it back to be more atomic and mitigate race conditions
        email_link.mark_accessed()
        email_link = aegis.model.EmailLink.get_id_token(email_link_id, token)
        # Link expires 15m after it was sent
        time_diff = email_link['access_dttm'] - email_link['create_dttm']
        if time_diff.seconds > 15*60:
            return {'error_message': "Magic Link Expired"}
        return email_link

    def is_super_admin(self):
        if not self.get_current_user():
            return False
        super_admins = aegis.config.get('super_admins')
        # Look for self.tmpl['host_config']['super_admins']
        if hasattr(self, 'tmpl') and self.tmpl.get('host_config') and 'super_admins' in self.tmpl['host_config']:
            for host_admin in self.tmpl['host_config']['super_admins']:
                if host_admin not in super_admins:
                    super_admins.append(host_admin)
        if super_admins and self.get_member_email() in super_admins:
            return True

    @staticmethod
    def auth_admin():
        """ Require user to be both logged-in and a super admin, or 403. """
        def call_wrapper(func):
            def authorize(self, *args, **kwargs):
                if not self.is_super_admin():
                    raise tornado.web.HTTPError(403)
                return func(self, *args, **kwargs)
            return authorize
        return call_wrapper

    # Instead of tornado.web.authenticated sending users to a login url, only send a 403
    @staticmethod
    def auth_required(method):
        def wrapper(self, *args, **kwargs):
            if not self.current_user:
                raise tornado.web.HTTPError(403)
            return method(self, *args, **kwargs)
        return wrapper

    # Request and session auditing
    def audit_start(self):
        # Set up the session first
        is_robot = self.user_is_robot()
        audit_session_id = None
        audit_session_row = None
        # If session_ck has audit_session_id, also try to fetch it to make sure it exists.
        if self.tmpl.get('session_ck', {}).get('audit_session_id'):
            audit_session_id = self.tmpl['session_ck']['audit_session_id']
            audit_session_row = aegis.model.AuditSession.get_id(audit_session_id, dbconn=self.dbconn)
        if audit_session_row:
            self.audit_session['last_request_name'] = self.tmpl['request_name']
            self.audit_session['last_request_dttm'] = aegis.database.Literal('NOW()')
            if aegis.database.mysql_available:
                self.audit_session['session_time'] = aegis.database.Literal('UNIX_TIMESTAMP(NOW()) - UNIX_TIMESTAMP(create_dttm)')
            elif aegis.database.pgsql_available:
                self.audit_session['session_time'] = aegis.database.Literal('EXTRACT(EPOCH FROM NOW()) - EXTRACT(EPOCH FROM create_dttm)')
            self.audit_session['request_cnt'] = aegis.database.Literal('request_cnt+1')
            self.audit_request['request_nbr'] = audit_session_row['request_cnt'] + 1
            self.audit_session['marketing_id'] = audit_session_row['marketing_id']
        else:
            self.audit_session['marketing_id'] = aegis.stdlib.validate_int(self.get_marketing_id())
            self.audit_session['request_cnt'] = 1
            self.audit_request['request_nbr'] = 1
            self.audit_session['view_cnt'] = 0
            if hasattr(self, 'view_ind') and self.view_ind:
                self.audit_session['view_cnt'] = 1
            if hasattr(self, 'api_ind') and self.api_ind:
                self.audit_session['api_cnt'] = 1
            self.audit_session['first_request_name'] = self.tmpl['request_name']
            self.audit_session['last_request_name'] = self.tmpl['request_name']
            self.audit_session['last_request_dttm'] = aegis.database.Literal('NOW()')
            self.audit_session['ip_tx'] = self.request.remote_ip
            if aegis.config.get('geolite_path') and self.tmpl['geoip']:
                self.audit_session['country_cd'] = self.tmpl['geoip'].get('country_iso_code')
                self.audit_session['region_cd'] = self.tmpl['geoip'].get('region_iso_code')
            if self.tmpl['user_agent_row']:
                self.audit_session['user_agent_id'] = self.tmpl['user_agent_row']['user_agent_id']
            self.audit_session['robot_ind'] = is_robot
            self.audit_session['referer_tx'] = self.request.headers.get('Referer')
            audit_session_id = aegis.model.AuditSession.insert_columns(dbconn=self.dbconn, **self.audit_session)
            self.tmpl['session_ck'] = {'audit_session_id': audit_session_id}
            self.cookie_set('session', self.tmpl['session_ck'])
        # Audit Request
        url_parts = urllib.parse.urlparse(self.request.uri)
        self.audit_session['audit_session_id'] = audit_session_id
        self.audit_request['audit_session_id'] = audit_session_id
        self.audit_request['request_name'] = self.tmpl['request_name']
        self.audit_request['url_path_tx'] = url_parts.path
        self.audit_request['url_query_tx'] = url_parts.query or None
        self.audit_request['ip_tx'] = self.request.remote_ip
        if aegis.config.get('geolite_path') and self.tmpl['geoip']:
            self.audit_request['country_cd'] = self.tmpl['geoip'].get('country_iso_code')
            self.audit_request['region_cd'] = self.tmpl['geoip'].get('region_iso_code')
        user_agent = aegis.model.UserAgent.get_agent(self.tmpl['user_agent'], dbconn=self.dbconn)
        if user_agent:
            self.audit_request['user_agent_id'] = user_agent['user_agent_id']
        self.audit_request['robot_ind'] = self.audit_request['robot_ind'] = is_robot
        self.audit_request['referer_tx'] = self.request.headers.get('Referer')
        self.audit_request['cookies_tx'] = self.request.headers.get('Cookie')
        return audit_session_id

    def audit_finish(self):
        # The time spent in here is the database calls... almost entirely.
        # 403 can be DOA, when no _xsrf __init__() and prepare() not called. Manually call self.prepare() to set up.
        if self._status_code == 403 and not hasattr(self.request, 'args'):
            self.prepare()
        # Audit Session - takes 10ms !!
        audit_session_id = self.tmpl.get('session_ck', {}).get('audit_session_id')
        #aegis.stdlib.logw(audit_session_id, "AUDIT SESSION ID")
        self.audit_session['user_id'] = self.get_user_id()
        self.audit_session['member_id'] = self.get_member_id()
        if audit_session_id:
            if hasattr(self, 'view_ind') and self.view_ind:
                self.audit_session['view_cnt'] = aegis.database.Literal('view_cnt+1')
            if hasattr(self, 'api_ind') and self.api_ind:
                self.audit_session['api_cnt'] = aegis.database.Literal('api_cnt+1')
            aegis.model.AuditSession.update_columns(self.audit_session, {'audit_session_id': audit_session_id}, dbconn=self.dbconn)
        # Audit Request
        request_args = {}
        if self.request.method in ('POST', 'PUT', 'PATCH') and self.request.args:
            post_secret_fields = ['password']
            if aegis.config.exists('post_secret_fields') and options.post_secret_fields:
                post_secret_fields += options.post_secret_fields
            request_args = dict(self.request.args)
            for field in post_secret_fields:
                if field in request_args:
                    request_args[field] = 'SECRET'
            try:
                #self.logw(request_args, "ARGS")
                self.audit_request['formpost_tx'] = json.dumps(request_args, cls=aegis.stdlib.DateTimeEncoder)[:65535]
            except UnicodeDecodeError:
                self.audit_request['formpost_tx'] = str(request_args)[:65535]
        self.audit_request['user_id'] = self.get_user_id()
        self.audit_request['member_id'] = self.get_member_id()
        self.audit_request['marketing_id'] = aegis.stdlib.validate_int(self.get_marketing_id())
        self.audit_request['audit_session_id'] = audit_session_id
        self.audit_request['view_ind'] = hasattr(self, 'view_ind') and self.view_ind
        self.audit_request['api_ind'] = hasattr(self, 'api_ind') and self.api_ind
        self.audit_request['http_status_nbr'] = self._status_code
        # Optional application-specific columns
        if aegis.config.exists('audit_request_columns'):
            for column in options.audit_request_columns:
                if hasattr(self, column):
                    self.audit_request[column] = getattr(self, column)
        # Make the finish time the very last thing
        self.audit_request['exec_time'] = int((time.time() - self.tmpl['start_t']) * 1000)
        # getting the database, memcache, render times on the timer - will be higher than during aegis.webapp.log_request because of above auditing
        timer_obj = aegis.stdlib.get_timer()
        if timer_obj and timer_obj._timers:
            database_time_s = timer_obj._timers.get('_database_exec_s')
            if database_time_s:
                self.audit_request['db_query_time'] = database_time_s * 1000
                self.audit_request['db_query_cnt'] = timer_obj._timers.get('_database_cnt')
            memcache_time_s = timer_obj._timers.get('_memcache_exec_s')
            if memcache_time_s:
                self.audit_request['mc_time'] = memcache_time_s * 1000
                self.audit_request['mc_cnt'] = timer_obj._timers.get('_memcache_cnt')
            render_time_s = timer_obj._timers.get('_render_exec_s')
            if render_time_s:
                self.audit_request['render_time'] = render_time_s * 1000
        audit_request_id = aegis.model.AuditRequest.insert_columns(dbconn=self.dbconn, **self.audit_request)
        #aegis.stdlib.logw(audit_request_id, "AUDIT REQUEST ID")
        self.save_audit_relations(audit_request_id)
        # In some error cases, log all the data from POST, headers, response.
        if (self._status_code >= 400 and self._status_code != 404) or (hasattr(self, 'json_resp') and self.json_resp.get('errors')):
            # Formatting request headers
            req_headers = json.dumps(str(self.request.headers).splitlines(), cls=aegis.stdlib.DateTimeEncoder)
            # Formatting response headers
            resp_headers = []
            for (k,v) in sorted(self._headers.get_all()):
                resp_headers.append('%s: %s' % (k,v))
            resp_headers = json.dumps(resp_headers, cls=aegis.stdlib.DateTimeEncoder)
            # Wiping user personal fields in JSON body
            request_body = {}
            if hasattr(self, 'json_req'):
                request_body = self.json_req
            # Needs Testing - maybe against HTML form
            #elif self.request.body:
            #    request_body = self.request.body
            #    aegis.stdlib.logw(request_body, "REQUEST BODY ")
            #    logging.warning("This may not always be a dictionary")
            post_secret_fields = ['password', 'accessToken', 'idToken', 'tokenObj']
            if aegis.config.exists('post_secret_fields') and options.post_secret_fields:
                post_secret_fields += options.post_secret_fields
            for field in post_secret_fields:
                if field in request_args:
                    request_body[field] = 'SECRET'
            # convert request_body to json for writing to db
            request_body = json.dumps(request_body, cls=aegis.stdlib.DateTimeEncoder)
            self.audit_request_data = {'audit_request_id': audit_request_id, 'audit_session_id': audit_session_id,
                                       'request_url': self.request.uri, 'request_method': self.request.method,
                                       'request_headers': req_headers, 'request_body': request_body,
                                       'run_host': socket.gethostname(), 'run_env': aegis.config.get('env'),
                                       'request_bytes': len(self.request.uri) + len(self.request.headers) + len(self.request.body),
                                       'response_status': self._status_code, 'response_headers': resp_headers, 'response_ms': self.audit_request['exec_time']}
            if hasattr(self, 'json_resp'):
                #self.json_resp['stuff'] = "123 \xe9 é and others"   # This was breaking mysql without str(self.json_resp)
                self.audit_request_data['response_body'] = str(self.json_resp)
                self.audit_request_data['response_bytes'] = len(json.dumps(self.json_resp, cls=aegis.stdlib.DateTimeEncoder))
                self.audit_request_data['response_error'] = json.dumps(self.json_resp.get('errors'), cls=aegis.stdlib.DateTimeEncoder)
            audit_request_data_id = aegis.model.AuditRequestData.insert_columns(dbconn=self.dbconn, **self.audit_request_data)
            audit_request_data = aegis.model.AuditRequestData.get_id(audit_request_data_id, dbconn=self.dbconn)
        return audit_request_id

    def prepare_audit_relation(self, model_class, row_id):
        self.audit_relations.append([model_class, row_id])

    def save_audit_relations(self, audit_request_id):
        for audit_relation in self.audit_relations:
            model_class, row_id = audit_relation
            model_class.set_audit_request_id(row_id, audit_request_id, dbconn=self.dbconn)

    def audit_session_end(self):
        # closes the session by deleting the cookie
        self.cookie_clear('session')
        if hasattr(self.tmpl, 'session_ck'):
            del self.tmpl['session_ck']

    def get_marketing_id(self):
        return self.audit_session.get('marketing_id')

    def set_marketing_id(self):
        # This runs before self.audit_session gets initialized from database, but skip if session_ck has audit_session_id.
        if self.tmpl.get('session_ck', {}).get('audit_session_id'):
            return
        # If there's an mid in request args, use if it's in the marketing table
        mid = aegis.stdlib.validate_int(self.request.args.get('mid'))
        if mid:
            marketing = aegis.model.Marketing.get_id(mid, dbconn=self.dbconn)
            if marketing:
                self.audit_session['marketing_id'] = mid
                return
        # Without explicit mid, infer from Referer header
        referer = self.request.headers.get('Referer')
        # Is 'direct' with no referer
        if not referer:
            logging.warning("No Referer -> direct")
            return self.finish_marketing('direct')
        # Is 'direct' if the referer netloc endswith the domain
        url_parts = aegis.stdlib.validate_url(referer)
        if url_parts and url_parts.netloc.endswith(self.tmpl['domain']):
            logging.warning("Referer endswith domain -> direct")
            return self.finish_marketing('direct')
        # Run it through pyreferrer
        pr = pyreferrer.Referrer.parse(referer)
        if pr and pr['type'] == 'search':
            logging.warning("Pyreferrer type is search -> organic")
            return self.finish_marketing('organic')
        if pr and pr['type'] == 'social':
            logging.warning("Pyreferrer type is social -> social")
            return self.finish_marketing('social')
        aegis.stdlib.logw(pr, "Pyreferrer")
        # Custom organic "netlocs" not (yet) in pyreferrer
        organic_netlocs = ['aol.com', 'baidu.com', 'www.daum.net', 'daum.net', 'presearch.com', 'search.brave.com', 'www.ecosia.org', 'www.msn.com',
                           'com.google.android.googlequicksearchbox']   # android-app://com.google.android.googlequicksearchbox
        for organic_netloc in organic_netlocs:
            if url_parts and url_parts.netloc.endswith(organic_netloc):
                logging.warning("Netloc endswith organic domain -> organic")
                return self.finish_marketing('organic')
        # Mark it as an unknown referral
        logging.warning("Url unknown: %s" % referer)
        return self.finish_marketing('referral')

    def finish_marketing(self, marketing_name):
        marketing = aegis.model.Marketing.get_name(marketing_name, dbconn=self.dbconn)
        if marketing:
            mid = marketing['marketing_id']
            self.audit_session['marketing_id'] = mid
        else:
            logging.error("%s finish_marketing() marketing_name slipping through cracks: %s" % (self.tmpl['host'], marketing_name))

    def track_email(self):
        if not self.request.args.get('t') or not self.request.args.get('e'):
            return
        email_tracking = aegis.model.EmailTracking.get_params(aegis.stdlib.validate_int(self.request.args['t']), self.request.args['e'])
        if not email_tracking:
            return
        if not email_tracking['deliver_dttm']:
            email_tracking.mark_delivered()
        if not email_tracking['open_dttm']:
            email_tracking.mark_opened()
        if self.request.args.get('c') and not email_tracking['click_dttm']:
            email_tracking.mark_clicked()
        # Mark email and member verified
        email = aegis.model.Email.get_id(email_tracking['to_email_id'], dbconn=self.dbconn)
        if email:
            email.mark_verified()
            if email['member_id'] and email['member_id'] == self.get_member_id():
                self.get_current_user().mark_verified()
        self.tmpl['email_tracking'] = email_tracking
        return email_tracking


class JsonRestApi(AegisHandler):
    def check_xsrf_cookie(self): pass

    def __init__(self, *args, **kwargs):
        super(JsonRestApi, self).__init__(*args, **kwargs)
        self.debug = False

    def prepare(self):
        super(JsonRestApi, self).prepare()
        if aegis.config.get('api_token_header'):
            api_token_value = self.request.headers.get(options.api_token_header)
            if not api_token_value or api_token_value != options.api_token_value:
                raise tornado.web.HTTPError(401, 'Wrong API Token')
        else:
            logging.error("Set options.api_token_header and options.api_token_value to enforce basic API Keys from clients")
        self.json_req = self.json_unpack()
        self.json_resp = {}

    def _handle_request_exception(self, e):
        super(JsonRestApi, self)._handle_request_exception(e)
        if hasattr(self.request, 'connection') and not self.request.connection.stream.closed():
            self.json_response({'error': "Unknown error, we're looking into it"})
        logging.exception(e)
        logging.error(e)

    @staticmethod
    def json_authenticated(method):
        def wrapper(self, *args, **kwargs):
            if not self.current_user:
                return self.general_error('Must be logged in to do this', 'not_logged_in', 403)
            return method(self, *args, **kwargs)
        return wrapper

    def json_unpack(self):
        content_type = self.request.headers.get('Content-Type')
        if self.request.body and content_type and content_type.startswith('application/json'):
            try:
                json_req = json.loads(self.request.body.decode("utf-8"))
                return json_req or {}
            except json.decoder.JSONDecodeError:
                raise tornado.web.HTTPError(401, 'Bad JSON Value')
        else:
            return dict(self.request.args)

    def json_debug(self, debug=True):
        if options.env == 'prod':
            return False
        self.debug = debug
        if self.debug:
            self.logw(self.request, "REQ")
            req_str = 'REQ HEADERS'
            req_headers = ["%s: %s" % (item[0], item[1]) for item in sorted(self.request.headers.items())]
            if req_headers:
                req_str += '\n'
                req_str += '\n'.join(req_headers)
            else:
                req_str += ' ()'
            logging.warning(req_str)
            self.logw(self.request.args, "ARGS")
            self.logw(self.json_req, "JSON REQ")

    def json_response(self, data, debug=False, status=200, snake_to_camel=False):
        self.set_header("Content-Type", 'application/json')
        self.set_status(status)
        if snake_to_camel:
            data = copy.deepcopy(data)
            aegis.stdlib.json_snake_to_camel(data)
        data['handler'] = self.tmpl['request_name']
        json_resp = json.dumps(data, cls=aegis.stdlib.DateTimeEncoder)
        if debug or self.debug:
            logging.warning("=== JSON RESPONSE ===")
            # Limit length of a single log line
            if len(str(data)) < 50000:
                self.logw(data, "RESPONSE DATA")
            else:
                self.logw(str(data)[:50000], "RESPONSE DATA - TOO LONG TO LOG")
            headers = []
            for (k,v) in sorted(self._headers.get_all()):
                headers.append('%s: %s' % (k,v))
            self.logw(headers, "HEADERS")
            cookies = []
            if hasattr(self, "_new_cookie"):
                for cookie in self._new_cookie.values():
                    cookies.append("Set-Cookie: %s" % cookie.OutputString(None))
            self.logw(cookies, "COOKIES")
            self.logw(json_resp, "JSON RESPONSE")
        self.json_length = len(zlib.compress(json_resp.encode("utf-8")))
        self.write(json_resp + '\n')
        self.finish()

    def json_error(self, field, error_message, error_code):
        self.json_resp.setdefault('errors', []).append({'field': field, 'error_message': error_message, 'error_code': error_code})

    def general_error(self, error_message, error_code, status=200):
        return self.json_response({'errors': [{'field': 'general', 'error_message': error_message, 'error_code': error_code}]}, status=status)

    def write_error(self, status_code, **kwargs):
        """ Overrides tornado.web.RequestHandler """
        if options.app_debug:
            exc_info = kwargs.get('exc_info')
            tb = ' '.join(traceback.format_tb(exc_info[2]))
            resp = json.dumps({'exception': tb})
        else:
            if status_code == 403:
                resp = "403 Forbidden"
            else:
                resp = json.dumps({'error': 'Sorry, something went wrong :-|'})
        self.write(resp + '\n')
        self.finish()


### Overall Application Architecture
class AegisApplication():
    def __init__(self, **kwargs):
        settings = dict(
            cookie_secret=options.cookie_secret,
            xsrf_cookies=True,
            xsrf_cookie_kwargs=dict(httponly=True, secure=True, samesite='Strict'),
            login_url='/login',
            debug=options.app_debug
        )
        settings.update(kwargs)
        if 'static_path' in options:
            settings['static_path'] = options.static_path
        if 'static_url_prefix' in options:
            settings['static_url_prefix'] = options.static_url_prefix
        return settings

    def log_request(self, handler):
        """ From: https://github.com/tornadoweb/tornado/blob/8afac1f805de738ccd0f58618b84b0a5f90dd346/tornado/web.py#L2114
        Writes a completed HTTP request to the logs. By default writes to the python root logger.  To change this behavior either:
        subclass Application and override this method, or pass a function in the application settings dictionary as ``log_function``.
        """
        if "log_function" in self.settings:
            self.settings["log_function"](handler)
            return
        if handler.get_status() < 400:
            log_method = tornado.log.access_log.info
        elif handler.get_status() < 500:
            log_method = tornado.log.access_log.warning
        else:
            log_method = tornado.log.access_log.error
        # Main part of the response
        host = handler.request.host.split(':')[0]
        extra_debug = ''
        user_id = None
        if hasattr(handler, 'tmpl'):
            user_id = handler.tmpl.get('user', {}).get('user_id')
            extra_debug = '| uid: %s | mid: %s' % (user_id or '-', handler.get_member_id() or '-')
            if hasattr(handler, 'json_length'):
                extra_debug += ' | kb: %4.2f' % (handler.json_length / 1024.0)
            extra_debug = aegis.stdlib.cstr(extra_debug, 'yellow')
            geoip = handler.tmpl.get('geoip')
            if geoip:
                extra_debug += aegis.stdlib.cstr("  %s / %s / %s" % (geoip.get('country_iso_code'), geoip.get('region_iso_code'), geoip.get('city')), 'cyan')
            if handler.user_is_robot():
                extra_debug += aegis.stdlib.cstr('   BOT', 'blue')
        if hasattr(handler, 'log_request_debug'):
            extra_debug += handler.log_request_debug()
        # Timing
        request_t_ms = handler.request.request_time() * 1000   # Use tornado's from start of __init__ to end of finish() as a reference
        timers = None
        if hasattr(handler, 'timer_obj'):
            timers = handler.timer_obj._timers
        log_method("%s %d %s %.2fms %s", host, handler.get_status(), handler._request_summary(), request_t_ms, extra_debug)
        # If request takes over options.slow_req_ms we can give some extra debug output
        slow_req_ms = aegis.config.get('slow_req_ms') or 250
        if request_t_ms > slow_req_ms and timers:
            net_t_ms = timers.get('_network_exec_s', 0) * 1000
            db_t_ms = timers.get('_database_exec_s', 0) * 1000
            cpu_t_ms = request_t_ms - net_t_ms - db_t_ms
            init_t_ms = timers.get('_init_exec_s', 0) * 1000
            prepare_t_ms = timers.get('_prepare_exec_s', 0) * 1000
            render_t_ms = timers.get('_render_exec_s', 0) * 1000
            finish_t_ms = timers.get('_finish_exec_s', 0) * 1000
            handler_t_ms = request_t_ms - init_t_ms - prepare_t_ms - render_t_ms - finish_t_ms
            msg = "Req Time: %.3fms  |  %.3fms cpu  %.3fms db  %.3fms net  |  %.3fms init  %.3fms prepare  %.3fms handler   %.3fms render  %.3fms finish"
            msg = msg % (request_t_ms, cpu_t_ms, db_t_ms, net_t_ms, init_t_ms, prepare_t_ms, handler_t_ms, render_t_ms, finish_t_ms)
            tornado.log.access_log.warning(msg)



def sig_handler(sig, frame):
    io_loop = tornado.ioloop.IOLoop.instance()
    def stop_loop():
        if len(asyncio.Task.all_tasks(io_loop)) == 0:
            io_loop.stop()
        else:
            io_loop.call_later(1, stop_loop)
    io_loop.add_callback_from_signal(stop_loop)


class WebApplication(AegisApplication, tornado.web.Application):
    application = None

    def __init__(self, **kwargs):
        settings = AegisApplication.__init__(self, **kwargs)
        tornado.web.Application.__init__(self, **settings)

    @staticmethod
    def start(application):
        WebApplication.application = application
        host = options.host
        port = options.port
        http_server = tornado.httpserver.HTTPServer(application, xheaders=True, no_keep_alive=True)
        logging.info('listening on %s:%s' % (host, port))
        if host:
            http_server.listen(port, address=host)
        else:
            http_server.listen(port)  # bind all (0.0.0.0:*)
        tornado.ioloop.IOLoop.instance().start()

    @staticmethod
    def start_asyncio(application):
        host = options.host
        port = options.port
        tornado.platform.asyncio.AsyncIOMainLoop().install()
        http_server = tornado.httpserver.HTTPServer(application, xheaders=True, no_keep_alive=True)
        logging.info('listening on %s:%s' % (host, port))
        if host:
            http_server.bind(port, address=host)
        else:
            http_server.bind(port)  # bind all (0.0.0.0:*)
        signal.signal(signal.SIGTERM, functools.partial(sig_handler))
        signal.signal(signal.SIGINT, functools.partial(sig_handler))
        http_server.start()


### Aegis Web Admin

class AegisWeb(AegisHandler):
    def prepare(self):
        # Need template_dir before calling super prepare, in case it breaks.
        self.tmpl['aegis_dir'] = aegis.config.aegis_dir()
        self.tmpl['template_dir'] = os.path.join(self.tmpl['aegis_dir'], 'templates')
        super(AegisWeb, self).prepare()
        self.tmpl['page_title'] = self.tmpl['request_name'].split('.')[0].replace('Aegis', '')
        self.tmpl['home_link'] = '/admin'
        self.tmpl['aegis_version'] = pkg_resources.require("aegis-tools")[0].version
        try:
            self.tmpl['app_version'] = pkg_resources.require(aegis.config.get('program_name'))[0].version
        except (pkg_resources.ContextualVersionConflict, pkg_resources.DistributionNotFound) as ex:
            logging.exception(ex)
            self.tmpl['app_version'] = 'N/A'
        self.tmpl['favicon_url'] = aegis.config.get('aegis_favicon_url') or '/favicon.ico'

    def get_template_path(self):
        return self.tmpl.get('template_dir')


class AegisHome(AegisWeb):
    @tornado.web.authenticated    # Could do something like @aegis.webapp.admin_only which also sends for login but then rejects if not admin
    def get(self, *args):
        self.enforce_admin()
        return self.render_path("index.html", **self.tmpl)


class AegisHydraForm(AegisWeb):
    @tornado.web.authenticated
    def get(self, hydra_type_id=None, *args):
        self.enforce_admin()
        self.tmpl['page_title'] = 'Hydra'
        self.tmpl['home_link'] = '/admin/hydra'
        self.tmpl['errors'] = {}
        hydra_type_id = aegis.stdlib.validate_int(hydra_type_id)
        if hydra_type_id:
            self.tmpl['hydra_type'] = aegis.model.HydraType.get_id(hydra_type_id, dbconn=self.dbconn)
        else:
            self.tmpl['hydra_type'] = {}
        self.tmpl['home_link'] = '/admin/hydra'
        return self.render_path("hydra_form.html", **self.tmpl)

    @tornado.web.authenticated
    def post(self, hydra_type_id=None, *args):
        self.enforce_admin()
        # Validate Input
        self.tmpl['errors'] = {}
        hydra_type = {}
        hydra_type['hydra_type_name'] = self.request.args.get('hydra_type_name')
        hydra_type['hydra_type_desc'] = self.request.args.get('hydra_type_desc')
        hydra_type['priority_ndx'] = aegis.stdlib.validate_int(self.request.args.get('priority_ndx'))
        hydra_type['next_run_sql'] = self.request.args.get('next_run_sql')
        hydra_type['run_host'] = self.request.args.get('run_host')
        hydra_type['run_env'] = self.request.args.get('run_env')
        self.tmpl['hydra_type'] = hydra_type
        if not hydra_type['hydra_type_name']:
            self.tmpl['errors']['hydra_type_name'] = '** required (string)'
        if not hydra_type['priority_ndx']:
            self.tmpl['errors']['priority_ndx'] = '** required (integer)'
        if self.tmpl['errors']:
            return self.render_path("hydra_form.html", **self.tmpl)
        # Run against database and send back to Hydra main
        hydra_type_id = aegis.stdlib.validate_int(hydra_type_id)
        if hydra_type_id:
            where = {'hydra_type_id': hydra_type_id}
            aegis.model.HydraType.update_columns(hydra_type, where, dbconn=self.dbconn)
        else:
            hydra_type_id = aegis.model.HydraType.insert_columns(dbconn=self.dbconn, **hydra_type)
            hydra_type_row = aegis.model.HydraType.get_id(hydra_type_id, dbconn=self.dbconn)
            hydra_type_row.set_status('paused')
        return self.redirect('/admin/hydra')


class AegisHydra(AegisWeb):
    @tornado.web.authenticated
    def get(self, *args):
        self.enforce_admin()
        header_logo = self.tmpl['host_config'].get('header_logo') or options.header_logo
        if header_logo.endswith('svg'):
            logging.warning("DO SVG")
            self.tmpl['page_title'] = 'Hydra %s' % self.tmpl['domain']
        else:
            self.tmpl['page_title'] = 'Hydra %s' % self.tmpl['domain']
        self.tmpl['home_link'] = '/'
        # Hydra Types sorted by status, priority, importance
        self.tmpl['hydra_types'] = aegis.model.HydraType.scan(dbconn=self.dbconn)
        self.tmpl['hydra_types'] = sorted(self.tmpl['hydra_types'], key=lambda x: x.get('next_run_dttm') is None)
        self.tmpl['hydra_types'] = sorted(self.tmpl['hydra_types'], key=lambda x: x.get('status') == 'paused')
        self.tmpl['hydra_types'] = sorted(self.tmpl['hydra_types'], key=lambda x: x.get('status') != 'running')
        return self.render_path("hydra.html", **self.tmpl)

    @tornado.web.authenticated
    def post(self, *args):
        self.enforce_admin()
        pause_ids = [aegis.stdlib.validate_int(k.replace('pause_', '')) for k in self.request.args.keys() if k.startswith('pause_')]
        unpause_ids = [aegis.stdlib.validate_int(k.replace('unpause_', '')) for k in self.request.args.keys() if k.startswith('unpause_')]
        run_ids = [aegis.stdlib.validate_int(k.replace('run_', '')) for k in self.request.args.keys() if k.startswith('run_')]
        # Do Pause
        if pause_ids:
            hydra_type = aegis.model.HydraType.get_id(pause_ids[0], dbconn=self.dbconn)
            #self.logw(hydra_type, "HYDRA TYPE")
            hydra_type.set_status('paused', dbconn=self.dbconn)
        # Do Unpause
        if unpause_ids:
            hydra_type = aegis.model.HydraType.get_id(unpause_ids[0], dbconn=self.dbconn)
            #self.logw(hydra_type, "HYDRA TYPE")
            hydra_type.set_status('live', dbconn=self.dbconn)
        # Do Run --- hooks over to batch!
        if run_ids:
            hydra_type = aegis.model.HydraType.get_id(run_ids[0], dbconn=self.dbconn)
            #self.logw(hydra_type, "HYDRA TYPE")
            hydra_type.run_now(dbconn=self.dbconn)
        return self.redirect(self.request.uri)


class AegisHydraQueue(AegisWeb):
    @tornado.web.authenticated
    def get(self, *args):
        self.enforce_admin()
        self.tmpl['page_title'] = 'Hydra'
        self.tmpl['home_link'] = '/admin/hydra'
        self.tmpl['queue_cnt'] = aegis.model.HydraQueue.count_live(dbconn=self.dbconn)
        self.tmpl['hydra_queues'] = aegis.model.HydraQueue.scan(dbconn=self.dbconn)
        # Sort by priority that will run, then by if the item is claimed
        self.tmpl['hydra_queues'] = sorted(self.tmpl['hydra_queues'], key=operator.itemgetter('priority_ndx'))
        self.tmpl['hydra_queues'] = sorted(self.tmpl['hydra_queues'], key=lambda x: x.get('claimed_dttm') is None)
        # If the queue item is running internally, sort it to the top
        for hydra_queue in self.tmpl['hydra_queues']:
            hydra_queue['_running'] = (hydra_queue['next_run_sql'] and hydra_queue['status'] == 'running') or (not hydra_queue['next_run_sql'] and hydra_queue['claimed_dttm'])
        self.tmpl['hydra_queues'] = sorted(self.tmpl['hydra_queues'], key=lambda x: x.get('_running') is True, reverse=True)
        return self.render_path("hydra_queue.html", **self.tmpl)

    @tornado.web.authenticated
    def post(self, *args):
        self.enforce_admin()
        run_ids = [aegis.stdlib.validate_int(k.replace('run_', '')) for k in self.request.args.keys() if k.startswith('run_')]
        if run_ids:
            hydra_queue = aegis.model.HydraQueue.get_id(run_ids[0], dbconn=self.dbconn)
            if hydra_queue:
                self.logw(hydra_queue['hydra_queue_id'], "RUN NOW HYDRA_QUEUE_ID")
                hydra_queue.run_now(dbconn=self.dbconn)
        return self.redirect('/admin/hydra/queue')


class AegisReportForm(AegisWeb):

    def validate_report_type(self, report_type_id):
        report_type_id = aegis.stdlib.validate_int(report_type_id)
        if report_type_id:
            self.tmpl['report_type'] = aegis.model.ReportType.get_id(report_type_id, dbconn=self.dbconn)
        else:
            self.tmpl['report_type'] = {}

    def validate_input(self):
        self.tmpl['errors'] = {}
        self.columns = {}
        self.columns['report_type_name'] = self.request.args.get('report_type_name')
        if not self.columns['report_type_name']:
            self.tmpl['errors']['report_type_name'] = 'Report Name Required'
        self.columns['report_sql'] = self.request.args.get('report_sql')
        if not self.columns['report_sql']:
            self.tmpl['errors']['report_sql'] = 'Report SQL Required'

    @tornado.web.authenticated
    def get(self, report_type_id=None, *args):
        self.enforce_admin()
        self.tmpl['errors'] = {}
        self.validate_report_type(report_type_id)
        return self.screen()

    @tornado.web.authenticated
    def post(self, report_type_id=None, *args):
        self.enforce_admin()
        self.validate_report_type(report_type_id)
        self.validate_input()
        if self.tmpl['errors']:
            return self.screen()
        # Set which schema the report runs against
        report_schema = self.request.args.get('report_schema')
        if report_schema and report_schema in aegis.database.dbconns.databases.keys():
            self.columns['report_schema'] = report_schema
        # Run against database and send back to Report main
        report_type_id = aegis.stdlib.validate_int(report_type_id)
        try:
            if report_type_id:
                where = {'report_type_id': report_type_id}
                aegis.model.ReportType.update_columns(self.columns, where, dbconn=self.dbconn)
            else:
                report_type_id = aegis.model.ReportType.insert_columns(dbconn=self.dbconn, **self.columns)
        except Exception as ex:
            logging.exception(ex)
            sql_error = [str(arg) for arg in ex.args]
            self.tmpl['errors']['sql_error'] = ': '.join(sql_error)
            return self.screen()
        return self.redirect('/admin/report/%s' % report_type_id)

    def screen(self):
        self.tmpl['schemas'] = []
        if aegis.database.pgsql_available and aegis.database.mysql_available:
            self.tmpl['schemas'] = list(aegis.database.dbconns.databases.keys())
        return self.render_path("report_form.html", **self.tmpl)


class AegisReport(AegisWeb):
    @tornado.web.authenticated
    def get(self, report_type_id=None, *args):
        self.enforce_admin()
        self.tmpl['errors'] = {}
        self.tmpl['column_names'] = []
        if report_type_id:
            self.tmpl['report'] = aegis.model.ReportType.get_id(report_type_id, dbconn=self.dbconn)
            self.tmpl['output'] = None
            self.tmpl['report_totals'] = {}
            sql = self.tmpl['report']['report_sql']
            try:
                dbconn = self.dbconn if self.dbconn else aegis.model.db()
                data, column_names = dbconn.query(sql, return_column_names=True)
                for row in data:
                    for column_name, value in row.items():
                        if type(value) is int:
                            colname = aegis.stdlib.snake_to_camel(column_name, upper=True, space=True)
                            self.tmpl['report_totals'].setdefault(colname, 0)
                            self.tmpl['report_totals'][colname] += value
                data = copy.deepcopy(data)
                aegis.stdlib.json_snake_to_camel(data, upper=True, space=True, debug=False)
                self.tmpl['num_rows'] = len(data)
                self.tmpl['output'] = data
                for column_name in column_names:
                    self.tmpl['column_names'].append(aegis.stdlib.snake_to_camel(column_name, upper=True, space=True))
            except Exception as ex:
                logging.exception(ex)
                sql_error = [str(arg) for arg in ex.args]
                self.tmpl['errors']['sql_error'] = ': '.join(sql_error)
            self.tmpl['report'] = aegis.model.ReportType.get_id(report_type_id, dbconn=self.dbconn)
            return self.render_path("report.html", **self.tmpl)
        else:
            self.tmpl['reports'] = aegis.model.ReportType.scan(dbconn=self.dbconn)
            return self.render_path("reports.html", **self.tmpl)


class AegisBuild(AegisWeb):
    @tornado.web.authenticated
    def get(self, *args):
        self.enforce_admin()
        self.tmpl['builds'] = [b for b in aegis.model.Build.scan(dbconn=self.dbconn) if (not b['delete_dttm'] and b['build_target'] != 'admin')]
        self.tmpl['home_link'] = '/admin/build'
        env = aegis.config.get('env')
        if env.endswith('-admin'):
            env = env.rsplit('-', maxsplit=1)[0]
        self.tmpl['live_build'] = aegis.model.Build.get_live_build(env, dbconn=self.dbconn)
        self.tmpl['aegis_version'] = pkg_resources.require("aegis-tools")[0].version
        try:
            self.tmpl['app_version'] = pkg_resources.require(aegis.config.get('program_name'))[0].version
        except pkg_resources.ContextualVersionConflict as ex:
            logging.exception(ex)
            self.tmpl['app_version'] = 'N/A'
        return self.render_path("build.html", **self.tmpl)

    @tornado.web.authenticated
    def post(self, *args):
        self.tmpl['build_step'] = self.request.args.get('build_step', 'build')
        self.enforce_admin()
        # DEPLOY
        build_keys = [k for k in self.request.args.keys() if k.startswith('deploy_')]
        if build_keys:
            build_id = [aegis.stdlib.validate_int(k.replace('deploy_', '')) for k in build_keys][0]
            if build_id:
                # Set output to '' so the web can see that it's started
                build_row = aegis.model.Build.get_id(build_id, dbconn=self.dbconn)
                build_row.set_output('deploy', '', dbconn=self.dbconn)
                hydra_type = aegis.model.HydraType.get_name('deploy_build', dbconn=self.dbconn)
                # Put an item on the work queue to signal each host to deploy
                for deploy_host in options.deploy_hosts:
                    hydra_queue = {'hydra_type_id': hydra_type['hydra_type_id'], 'priority_ndx': hydra_type['priority_ndx'], 'work_dttm': aegis.database.Literal("NOW()"),
                                   'work_host': deploy_host, 'work_env': aegis.config.get('env')}
                    work_data = {'build_id': build_id, 'user': self.get_member_email()}
                    hydra_queue['work_data'] = json.dumps(work_data, cls=aegis.stdlib.DateTimeEncoder)
                    hydra_queue_id = aegis.model.HydraQueue.insert_columns(dbconn=self.dbconn, **hydra_queue)
                return self.redirect('/admin/build')
        # REVERT
        revert_keys = [k for k in self.request.args.keys() if k.startswith('revert_')]
        if revert_keys:
            build_id = [aegis.stdlib.validate_int(k.replace('revert_', '')) for k in revert_keys][0]
            if build_id:
                # Set output to '' so the web can see that it's started
                build_row = aegis.model.Build.get_id(build_id, dbconn=self.dbconn)
                build_row.set_output('revert', '', dbconn=self.dbconn)
                hydra_type = aegis.model.HydraType.get_name('revert_build', dbconn=self.dbconn)
                # Put an item on the work queue to signal each host to deploy
                for deploy_host in options.deploy_hosts:
                    hydra_queue = {'hydra_type_id': hydra_type['hydra_type_id'], 'priority_ndx': hydra_type['priority_ndx'], 'work_dttm': aegis.database.Literal("NOW()"),
                                   'work_host': deploy_host, 'work_env': aegis.config.get('env')}
                    work_data = {'build_id': build_id, 'user': self.get_member_email()}
                    hydra_queue['work_data'] = json.dumps(work_data, cls=aegis.stdlib.DateTimeEncoder)
                    hydra_queue_id = aegis.model.HydraQueue.insert_columns(dbconn=self.dbconn, **hydra_queue)
                return self.redirect('/admin/build')
        # DELETE
        delete_keys = [k for k in self.request.args.keys() if k.startswith('delete_')]
        if delete_keys:
            build_id = [aegis.stdlib.validate_int(k.replace('delete_', '')) for k in delete_keys][0]
            if build_id:
                build = aegis.model.Build.get_id(build_id, dbconn=self.dbconn)
                build.set_soft_deleted(dbconn=self.dbconn)
                return self.redirect('/admin/build')


class AegisBuildForm(AegisWeb):
    @tornado.web.authenticated
    def get(self, *args):
        self.enforce_admin()
        self.tmpl['page_title'] = 'Build'
        self.tmpl['errors'] = {}
        self.tmpl['build'] = {}
        self.tmpl['build_step'] = self.request.args.get('build_step', 'build')
        self.tmpl['home_link'] = '/admin/build'
        return self.render_path("build_form.html", **self.tmpl)

    @tornado.web.authenticated
    def post(self, *args):
        self.enforce_admin()
        # Validate Input
        self.tmpl['errors'] = {}
        self.tmpl['build'] = build = {}
        build['branch'] = self.request.args.get('branch')
        build['revision'] = self.request.args.get('revision')
        if not build['branch']:
            self.tmpl['errors']['branch'] = '** required (string)'
        if self.tmpl['errors']:
            return self.render_path("build_form.html", **self.tmpl)
        if not build['revision']:
            build['revision'] = 'HEAD'
        aegis.stdlib.logw(aegis.config.get('env'), "RUNNING ENV")
        build['env'] = aegis.config.get('env')
        if aegis.config.get('env').endswith('-admin'):
            build['env'] = aegis.config.get('env').rsplit('-', maxsplit=1)[0]
        aegis.stdlib.logw(build['env'], "SET BUILD ENV FROM PROCESS ENV")
        build['build_target'] = 'application'

        # Create build row and add it to run on Hydra
        build_id = aegis.model.Build.insert_columns(dbconn=self.dbconn, **build)
        hydra_type = aegis.model.HydraType.get_name('build_build', dbconn=self.dbconn)
        hydra_queue = {'hydra_type_id': hydra_type['hydra_type_id'], 'priority_ndx': hydra_type['priority_ndx'], 'work_dttm': aegis.database.Literal("NOW()"),
                       'work_host': aegis.config.get('build_host'), 'work_env': aegis.config.get('env')}
        work_data = {'build_id': build_id, 'user': self.get_member_email()}
        hydra_queue['work_data'] = json.dumps(work_data, cls=aegis.stdlib.DateTimeEncoder)
        hydra_queue_id = aegis.model.HydraQueue.insert_columns(dbconn=self.dbconn, **hydra_queue)
        self.redirect('/admin/build')


class AegisBuildView(AegisWeb):
    @tornado.web.authenticated
    def get(self, build_id, *args):
        self.tmpl['page_title'] = 'Build'
        self.tmpl['home_link'] = '/admin/build'
        self.enforce_admin()
        self.tmpl['errors'] = {}
        build_id = aegis.stdlib.validate_int(build_id)
        if build_id:
            self.tmpl['build'] = aegis.model.Build.get_id(build_id, dbconn=self.dbconn)
        else:
            self.tmpl['build'] = {}
        self.tmpl['build_step'] = self.request.args.get('build_step', 'build')
        return self.render_path("build_view.html", **self.tmpl)

    @tornado.web.authenticated
    def post(self, build_id, *args):
        self.enforce_admin()
        # Validate Input
        self.tmpl['errors'] = {}
        self.tmpl['build'] = build = {}
        build['branch'] = self.request.args.get('branch')
        build['revision'] = self.request.args.get('revision')
        if not build['branch']:
            self.tmpl['errors']['branch'] = '** required (string)'
        if not build['revision']:
            build['revision'] = 'HEAD'
        if self.tmpl['errors']:
            return self.render_path("build_form.html", **self.tmpl)
        build['env'] = aegis.config.get('env')
        # Create build row and add it to run on Hydra
        build_id = aegis.model.Build.insert_columns(dbconn=self.dbconn, **build)
        hydra_type = aegis.model.HydraType.get_name('build_build', dbconn=self.dbconn)
        hydra_queue = {'hydra_type_id': hydra_type['hydra_type_id'], 'priority_ndx': hydra_type['priority_ndx'], 'work_dttm': aegis.database.Literal("NOW()"),
                       'work_host': aegis.config.get('build_host'), 'work_env': aegis.config.get('env')}
        work_data = {'build_id': build_id, 'user': self.get_member_email()}
        hydra_queue['work_data'] = json.dumps(work_data, cls=aegis.stdlib.DateTimeEncoder)
        hydra_queue_id = aegis.model.HydraQueue.insert_columns(dbconn=self.dbconn, **hydra_queue)
        self.redirect('/admin/build')


class AegisBuildConfirm(AegisWeb):
    @tornado.web.authenticated
    def get(self, build_id, build_step, *args):
        self.enforce_admin()
        self.tmpl['build_row'] = aegis.model.Build.get_id(aegis.stdlib.validate_int(build_id), dbconn=self.dbconn)
        self.tmpl['build_step'] = build_step
        self.tmpl['errors'] = {}
        return self.screen()

    @tornado.web.authenticated
    def post(self, build_id, build_step, *args):
        self.enforce_admin()
        self.tmpl['build_row'] = aegis.model.Build.get_id(aegis.stdlib.validate_int(build_id), dbconn=self.dbconn)
        self.tmpl['build_step'] = build_step
        self.tmpl['errors'] = {}
        # Validate Input
        message = self.request.args.get('message')
        if not message:
            self.tmpl['errors']['message'] = '** required (string)'
            return self.screen()
        # Save the user message and start the deploy/revert
        self.tmpl['build_row'].set_message(message, build_step, dbconn=self.dbconn)
        self.tmpl['build_row'] = aegis.model.Build.get_id(aegis.stdlib.validate_int(build_id), dbconn=self.dbconn)
        if build_step == 'deploy':
            aegis.build.Build.start_deploy(self.tmpl['build_row'], self.get_member_email(), dbconn=self.dbconn)
        elif build_step == 'revert':
            aegis.build.Build.start_revert(self.tmpl['build_row'], self.get_member_email(), dbconn=self.dbconn)
        # Set output to '' so the web can see that it's started
        self.tmpl['build_row'] = aegis.model.Build.get_id(aegis.stdlib.validate_int(build_id), dbconn=self.dbconn)
        self.tmpl['build_row'].set_output(build_step, '', dbconn=self.dbconn)
        hydra_type = aegis.model.HydraType.get_name('%s_build' % build_step, dbconn=self.dbconn)
        # Put an item on the work queue to signal each host to deploy
        for deploy_host in options.deploy_hosts:
            hydra_queue = {'hydra_type_id': hydra_type['hydra_type_id'], 'priority_ndx': hydra_type['priority_ndx'], 'work_dttm': aegis.database.Literal("NOW()"),
                           'work_host': deploy_host, 'work_env': aegis.config.get('env')}
            work_data = {'build_id': build_id, 'user': self.get_member_email()}
            hydra_queue['work_data'] = json.dumps(work_data, cls=aegis.stdlib.DateTimeEncoder)
            hydra_queue_id = aegis.model.HydraQueue.insert_columns(dbconn=self.dbconn, **hydra_queue)
        return self.redirect('/admin/build')

    def screen(self):
        self.tmpl['home_link'] = '/admin/build'
        self.tmpl['page_title'] = 'Build'
        self.tmpl['commits'] = aegis.build.Build.commit_diff(self.tmpl['build_row'], dbconn=self.dbconn)
        self.tmpl['live_build'] = aegis.model.Build.get_live_build(self.tmpl['build_row']['env'], dbconn=self.dbconn)
        return self.render_path("build_confirm.html", **self.tmpl)


class AegisUsage(AegisWeb):
    @tornado.web.authenticated
    def get(self, *args):
        self.enforce_admin()
        self.tmpl['home_link'] = '/admin/usage'
        self.tmpl['page_title'] = 'Usage'
        self.tmpl['usages'] = aegis.model.Usage.scan_slowest()
        self.tmpl['min_date'] = 'N/A'
        if self.tmpl['usages']:
            self.tmpl['min_date'] = min([str(usage['create_dttm']) for usage in self.tmpl['usages']]).split('.')[0]
        self.tmpl['usage_map'] = aegis.stdlib.map_items(self.tmpl['usages'], 'usage_name')
        self.tmpl['usage_set'] = aegis.stdlib.Accumulator.usage_set
        self.tmpl['no_usage_set'] = set([usage_name for usage_name in self.tmpl['usage_set'] if usage_name not in self.tmpl['usage_map']])
        self.tmpl['no_usage_list'] = [no_usage for no_usage in sorted(list(self.tmpl['no_usage_set']))]
        return self.render_path("usage.html", **self.tmpl)


handler_urls = [
    (r'^/admin/build/(\d+)/(deploy|revert)\W*$', AegisBuildConfirm),
    (r'^/admin/build/(\d+)\W*$', AegisBuildView),
    (r'^/admin/build/add\W*$', AegisBuildForm),
    (r'^/admin/build\W*$', AegisBuild),
    (r'^/admin/hydra/queue\W*$', AegisHydraQueue),
    (r'^/admin/hydra/add\W*$', AegisHydraForm),
    (r'^/admin/hydra/(\d+)\W*$', AegisHydraForm),
    (r'^/admin/hydra\W*$', AegisHydra),
    (r'^/admin/report/form/(\d+)\W*$', AegisReportForm),
    (r'^/admin/report/form\W*$', AegisReportForm),
    (r'^/admin/report/(\d+)\W*$', AegisReport),
    (r'^/admin/report\W*$', AegisReport),
    (r'^/admin/usage\W*$', AegisUsage),
    (r'^/admin\W*$', AegisHome),
]
