# coding: utf8
# Copyright 2025 Lenovo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
The command module for redfish systems.  Provides https-only support
for redfish compliant endpoints
"""

import base64
from datetime import datetime
from datetime import timedelta
import json
import os
import re
import socket
import struct
import sys
import time

from dateutil import tz

import pyghmi.constants as const
import pyghmi.exceptions as exc
import pyghmi.redfish.oem.lookup as oem
from pyghmi.util.parse import parse_time
import pyghmi.util.webclient as webclient


numregex = re.compile('([0-9]+)')


powerstates = {
    'on': 'On',
    'off': 'ForceOff',
    'softoff': 'GracefulShutdown',
    'shutdown': 'GracefulShutdown',
    'reset': 'ForceRestart',
    'boot': None,
}


boot_devices_read = {
    'BiosSetup': 'setup',
    'Cd': 'optical',
    'Floppy': 'floppy',
    'Hdd': 'hd',
    'None': 'default',
    'Pxe': 'network',
    'Usb': 'usb',
    'SDCard': 'sdcard',
}


_healthmap = {
    'Critical': const.Health.Critical,
    'Unknown': const.Health.Warning,
    'Warning': const.Health.Warning,
    'OK': const.Health.Ok,
    None: const.Health.Ok,
}


def _mask_to_cidr(mask):
    maskn = socket.inet_pton(socket.AF_INET, mask)
    maskn = struct.unpack('!I', maskn)[0]
    cidr = 32
    while maskn & 0b1 == 0 and cidr > 0:
        cidr -= 1
        maskn >>= 1
    return cidr


def _cidr_to_mask(cidr):
    return socket.inet_ntop(
        socket.AF_INET, struct.pack(
            '!I', (2**32 - 1) ^ (2**(32 - cidr) - 1)))


def naturalize_string(key):
    """Analyzes string in a human way to enable natural sort

    :param nodename: The node name to analyze
    :returns: A structure that can be consumed by 'sorted'
    """
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(numregex, key)]


def natural_sort(iterable):
    """Return a sort using natural sort if possible

    :param iterable:
    :return:
    """
    try:
        return sorted(iterable, key=naturalize_string)
    except TypeError:
        # The natural sort attempt failed, fallback to ascii sort
        return sorted(iterable)


class SensorReading(object):
    def __init__(self, healthinfo, sensor=None, value=None, units=None,
                 unavailable=False):
        self.states = []
        if sensor:
            self.name = sensor['name']
        else:
            self.name = healthinfo['Name']
            self.health = _healthmap.get(healthinfo.get(
                'Status', {}).get('Health', None), const.Health.Warning)
            self.states = [healthinfo.get('Status', {}).get('Health',
                                                            'Unknown')]
            self.health = _healthmap[healthinfo['Status']['Health']]
            if self.health == const.Health.Ok:
                self.states = []
        self.value = value
        self.state_ids = None
        self.imprecision = None
        self.units = units
        self.unavailable = unavailable
    
    def __repr__(self):
        return repr({
            'value': self.value,
            'state_ids': self.state_ids,
            'units': self.units,
            'imprecision': self.imprecision,
            'name': self.name,
            'unavailable': self.unavailable,
        })


class Command(object):

    def __init__(self, bmc, userid, password, verifycallback, sysurl=None,
                 bmcurl=None, chassisurl=None, pool=None, port=443):
        self.wc = webclient.SecureHTTPConnection(
            bmc, port, verifycallback=verifycallback)
        self._hwnamemap = {}
        self._fwnamemap = {}
        self._urlcache = {}
        self._varbmcurl = bmcurl
        self._varbiosurl = None
        self._varbmcnicurl = None
        self._varsetbiosurl = None
        self._varchassisurl = chassisurl
        self._varresetbmcurl = None
        self._varupdateservice = None
        self._varfwinventory = None
        self._oem = None
        self._gpool = pool
        self._bmcv4ip = None
        self._bmcv6ip = None
        self.xauthtoken = None
        for addrinf in socket.getaddrinfo(bmc, 0, 0, socket.SOCK_STREAM):
            if addrinf[0] == socket.AF_INET:
                self._bmcv4ip = socket.inet_pton(addrinf[0], addrinf[-1][0])
            elif addrinf[0] == socket.AF_INET6:
                theip = addrinf[-1][0]
                theip = theip.split('%')[0]
                self._bmcv6ip = socket.inet_pton(addrinf[0], theip)
        self.wc.set_header('Accept', 'application/json')
        self.wc.set_header('User-Agent', 'pyghmi')
        self.wc.set_header('Accept-Encoding', 'gzip')
        self.wc.set_header('OData-Version', '4.0')
        overview = self.wc.grab_json_response('/redfish/v1/')
        self.username = userid
        self.password = password
        self.wc.set_basic_credentials(self.username, self.password)
        self.wc.set_header('Content-Type', 'application/json')
        if 'Systems' not in overview and 'Managers' not in overview:
            raise exc.PyghmiException('Redfish not ready')
        if 'SessionService' in overview:
            self._get_session_token(self.wc)
        self._varsensormap = {}
        self.powerurl = None
        self.sysurl = None
        if 'Managers' in overview:
            bmcoll = systems = overview['Managers']['@odata.id']
            res = self.wc.grab_json_response_with_status(bmcoll)
            if res[1] == 401:
                raise exc.PyghmiException('Access Denied')
            elif res[1] < 200 or res[1] >= 300:
                raise exc.PyghmiException(repr(res[0]))
            bmcs = res[0]['Members']
            if len(bmcs) == 1:
                self._varbmcurl = bmcs[0]['@odata.id']
        if 'Systems' in overview:
            systems = overview['Systems']['@odata.id']
            res = self.wc.grab_json_response_with_status(systems)
            if res[1] == 401:
                raise exc.PyghmiException('Access Denied')
            elif res[1] < 200 or res[1] >= 300:
                raise exc.PyghmiException(repr(res[0]))
            members = res[0]
            systems = members['Members']
            if sysurl:
                for system in systems:
                    if system['@odata.id'] == sysurl or system['@odata.id'].split('/')[-1] == sysurl:
                        self.sysurl = system['@odata.id']
                        break
                else:
                    raise exc.PyghmiException(
                        'Specified sysurl not found: {0}'.format(sysurl))
            else:
                if len(systems) > 1:
                    systems = [x for x in systems if 'DPU' not in x['@odata.id']]
                if len(systems) > 1:
                    raise exc.PyghmiException(
                        'Multi system manager, sysurl is required parameter')
                if len(systems):
                    self.sysurl = systems[0]['@odata.id']
                else:
                    self.sysurl = None
            self.powerurl = self.sysinfo.get('Actions', {}).get(
                '#ComputerSystem.Reset', {}).get('target', None)

    def _get_session_token(self, wc):
        # specification actually indicates we can skip straight to this url
        username = self.username
        password = self.password
        if not isinstance(username, str):
            username = username.decode()
        if not isinstance(password, str):
            password = password.decode()
        rsp = wc.grab_rsp('/redfish/v1/SessionService/Sessions',
                          {'UserName': username, 'Password': password})
        rsp.read()
        self.xauthtoken = rsp.getheader('X-Auth-Token')
        if self.xauthtoken:
            if 'Authorization' in wc.stdheaders:
                del wc.stdheaders['Authorization']
            if 'Authorization' in self.wc.stdheaders:
                del self.wc.stdheaders['Authorization']
            wc.stdheaders['X-Auth-Token'] = self.xauthtoken
            self.wc.stdheaders['X-Auth-Token'] = self.xauthtoken

    @property
    def _accountserviceurl(self):
        sroot = self._do_web_request('/redfish/v1/')
        return sroot.get('AccountService', {}).get('@odata.id', None)

    @property
    def _validroles(self):
        okroles = set([])
        roleurl = self._do_web_request(self._accountserviceurl).get(
            'Roles', {}).get('@odata.id', None)
        if roleurl:
            roles = self._do_web_request(roleurl).get('Members', [])
            for role in roles:
                role = role.get('@odata.id', '')
                if not role:
                    continue
                okroles.add(role.split('/')[-1])
        if not okroles:
            okroles.add('Administrator')
            okroles.add('Operator')
            okroles.add('ReadOnly')
        return okroles

    def get_users(self):
        """get list of users and channel access information (helper)

        :param channel: number [1:7]

        :return:
            name: (str)
            uid: (int)
            channel: (int)
            access:
                callback (bool)
                link_auth (bool)
                ipmi_msg (bool)
                privilege_level: (str)[callback, user, operatorm administrator,
                                       proprietary, no_access]
        """
        srvurl = self._accountserviceurl
        names = {}
        if srvurl:
            srvinfo = self._do_web_request(srvurl)
            srvurl = srvinfo.get('Accounts', {}).get('@odata.id', None)
            if srvurl:
                srvinfo = self._do_web_request(srvurl)
                accounts = srvinfo.get('Members', [])
                for account in accounts:
                    accinfo = self._do_web_request(account['@odata.id'])
                    currname = accinfo.get('UserName', '')
                    currid = accinfo.get('Id', None)
                    if currname:
                        names[currid] = {
                            'name': currname,
                            'uid': currid,
                            'expiration': self.oem.get_user_expiration(currid),
                            'access': {
                                'privilege_level': accinfo.get('RoleId',
                                                               'Unknown')
                            }
                        }
        return names

    def _account_url_info_by_id(self, uid):
        srvurl = self._accountserviceurl
        if srvurl:
            srvinfo = self._do_web_request(srvurl)
            srvurl = srvinfo.get('Accounts', {}).get('@odata.id', None)
            if srvurl:
                srvinfo = self._do_web_request(srvurl)
                accounts = srvinfo.get('Members', [])
                for account in accounts:
                    accinfo = self._do_web_request(account['@odata.id'])
                    currid = accinfo.get('Id', None)
                    if str(currid) == str(uid):
                        accinfo['expiration'] = self.oem.get_user_expiration(
                            uid)
                        return account['@odata.id'], accinfo

    def get_user(self, uid):
        srvurl = self._accountserviceurl
        if srvurl:
            srvinfo = self._do_web_request(srvurl)
            srvurl = srvinfo.get('Accounts', {}).get('@odata.id', None)
            if srvurl:
                srvinfo = self._do_web_request(srvurl)
                accounts = srvinfo.get('Members', [])
                for account in accounts:
                    accinfo = self._do_web_request(account['@odata.id'])
                    currname = accinfo.get('UserName', '')
                    currid = accinfo.get('Id', None)
                    if str(currid) == str(uid):
                        return {'name': currname, 'uid': uid,
                                'expiration': self.oem.get_user_expiration(
                                    uid),
                                'access': {
                                    'privilege_level': accinfo.get(
                                        'RoleId', 'Unknown')}}

    def set_user_password(self, uid, mode='set_password', password=None):
        """Set user password and (modes)

        :param uid: id number of user.  see: get_names_uid()['name']

        :param mode:
            disable       = disable user connections
            enable        = enable user connections
            set_password  = set or ensure password

        :param password: Password
            (optional when mode is [disable or enable])

        :return:
            True on success
        """

        accinfo = self._account_url_info_by_id(uid)
        if not accinfo:
            raise Exception("No such account found")
        etag = accinfo[1].get('@odata.etag', None)
        if mode == 'set_password':
            self._do_web_request(accinfo[0], {'Password': password},
                                 method='PATCH', etag=etag)
        elif mode == 'disable':
            self._do_web_request(accinfo[0], {'Enabled': False},
                                 method='PATCH', etag=etag)
        elif mode == 'enable':
            self._do_web_request(accinfo[0], {'Enabled': True},
                                 method='PATCH', etag=etag)
        return True

    def disable_user(self, uid, mode):
        """Disable User

        Just disable the User.
        This will not disable the password or revoke privileges.

        :param uid: user id
        :param mode:
            disable       = disable user connections
            enable        = enable user connections
        """
        self.set_user_password(uid, mode)
        return True

    def set_user_access(self, uid, privilege_level='ReadOnly'):
        if privilege_level.startswith('custom.'):
            privilege_level = privilege_level.replace('custom.', '')
        accinfo = self._account_url_info_by_id(uid)
        if not accinfo:
            raise Exception("Unable to find indicated uid")
        etag = accinfo[1].get('@odata.etag', None)
        for role in self._validroles:
            if role.lower() == privilege_level.lower():
                privilege_level = role
                break
        self._do_web_request(accinfo[0], {'RoleId': privilege_level},
                             method='PATCH', etag=etag)

    def create_user(self, uid, name, password, privilege_level='ReadOnly'):
        """create/ensure a user is created with provided settings

        :param privilege_level:
            User Privilege level.  Redfish role, commonly Administrator,
            Operator, and ReadOnly
        """
        accinfo = self._account_url_info_by_id(uid)
        if not accinfo:
            raise Exception("Unable to find indicated uid")
        if privilege_level.startswith('custom.'):
            privilege_level = privilege_level.replace('custom.', '')
        for role in self._validroles:
            if role.lower() == privilege_level.lower():
                privilege_level = role
                break
        etag = accinfo[1].get('@odata.etag', None)
        userinfo = {
            "UserName": name,
            "Password": password,
            "RoleId": privilege_level,
        }
        self._do_web_request(accinfo[0], userinfo, method='PATCH', etag=etag)
        return True

    def get_screenshot(self, outfile):
        return self.oem.get_screenshot(outfile)

    def get_ikvm_methods(self):
        return self.oem.get_ikvm_methods()

    def get_ikvm_launchdata(self):
        return self.oem.get_ikvm_launchdata()

    def user_delete(self, uid):
        self.oem.user_delete(uid)

    def set_user_name(self, uid, name):
        """Set user name

        :param uid: user id
        :param name: username
        """
        accinfo = self._account_url_info_by_id(uid)
        if not accinfo:
            raise Exception("No such account found")
        etag = accinfo[1].get('@odata.etag', None)
        self._do_web_request(accinfo[0], {'UserName': name}, method='PATCH',
                             etag=etag)
        return True

    @property
    def _updateservice(self):
        if not self._varupdateservice:
            overview = self._do_web_request('/redfish/v1/')
            us = overview.get('UpdateService', {}).get('@odata.id', None)
            if not us:
                raise exc.UnsupportedFunctionality(
                    'BMC does not implement extended firmware information')
            self._varupdateservice = us
        return self._varupdateservice

    @property
    def _fwinventory(self):
        if not self._varfwinventory:
            usi = self._do_web_request(self._updateservice)
            self._varfwinventory = usi.get('FirmwareInventory', {}).get(
                '@odata.id', None)
            if not self._varfwinventory:
                raise exc.UnsupportedFunctionality(
                    'BMC does not implement extended firmware information')
        return self._varfwinventory

    @property
    def sysinfo(self):
        if not self.sysurl:
            return {}
        try:
            return self._do_web_request(self.sysurl)
        except exc.RedfishError:
            self.sysurl = None
            return {}

    @property
    def bmcinfo(self):
        return self._do_web_request(self._bmcurl)

    def get_power(self):
        currinfo = self._do_web_request(self.sysurl, cache=False)
        return {'powerstate': str(currinfo['PowerState'].lower())}

    def reseat_bay(self, bay):
        """Request the reseat of a bay

        Request the enclosure manager to reseat the system in a particular
        bay.

        :param bay: The bay identifier to reseat
        :return:
        """
        self.oem.reseat_bay(bay)

    def set_power(self, powerstate, wait=False):
        if powerstate == 'boot':
            oldpowerstate = self.get_power()['powerstate']
            powerstate = 'on' if oldpowerstate == 'off' else 'reset'
        elif powerstate in ('on', 'off'):
            oldpowerstate = self.get_power()['powerstate']
            if oldpowerstate == powerstate:
                return {'powerstate': powerstate}
        reqpowerstate = powerstate
        if powerstate not in powerstates:
            raise exc.InvalidParameterValue(
                "Unknown power state %s requested" % powerstate)
        powerstate = powerstates[powerstate]
        self._do_web_request(
            self.powerurl, {'ResetType': powerstate})
        if wait and reqpowerstate in ('on', 'off', 'softoff', 'shutdown'):
            if reqpowerstate in ('softoff', 'shutdown'):
                reqpowerstate = 'off'
            timeout = os.times()[4] + 300
            while (self.get_power()['powerstate'] != reqpowerstate
                   and os.times()[4] < timeout):
                time.sleep(1)
            if self.get_power()['powerstate'] != reqpowerstate:
                raise exc.PyghmiException(
                    "System did not accomplish power state change")
            return {'powerstate': reqpowerstate}
        return {'pendingpowerstate': reqpowerstate}

    def _get_cache(self, url, cache=30):
        now = os.times()[4]
        cachent = self._urlcache.get(url, None)
        if cachent and cachent['vintage'] > now - cache:
            return cachent['contents']
        return None

    def _do_bulk_requests(self, urls, cache=True):
        if self._gpool:
            urls = [(x, None, None, cache) for x in urls]
            for res in self._gpool.starmap(self._do_web_request_withurl, urls):
                yield res
        else:
            for url in urls:
                yield self._do_web_request_withurl(url, cache=cache)

    def _do_web_request_withurl(self, url, payload=None, method=None,
                                cache=True):
        return self._do_web_request(url, payload, method, cache), url

    def _do_web_request(self, url, payload=None, method=None, cache=True,
                        etag=None):
        res = None
        if cache is True:
            cache = 30
        if cache and payload is None and method is None:
            res = self._get_cache(url, cache)
        if res:
            return res
        wc = self.wc.dupe()
        if etag:
            wc.stdheaders['If-Match'] = etag
        try:
            res = wc.grab_json_response_with_status(url, payload,
                                                    method=method)
        finally:
            if 'If-Match' in wc.stdheaders:
                del wc.stdheaders['If-Match']
        if res[1] == 401 and self.xauthtoken:
            wc.set_basic_credentials(self.username, self.password)
            self._get_session_token(wc)
            if etag:
                wc.stdheaders['If-Match'] = etag
            try:
                res = wc.grab_json_response_with_status(url, payload,
                                                        method=method)
            finally:
                if 'If-Match' in wc.stdheaders:
                    del wc.stdheaders['If-Match']
        if res[1] < 200 or res[1] >= 300:
            try:
                info = json.loads(res[0])
                errmsg = [
                    x.get('Message', x['MessageId']) for x in info.get(
                        'error', {}).get('@Message.ExtendedInfo', {})]
                msgid = [
                    x['MessageId'] for x in info.get(
                        'error', {}).get('@Message.ExtendedInfo', {})]
                errmsg = ','.join(errmsg)
                msgid = ','.join(msgid)
                raise exc.RedfishError(errmsg, msgid=msgid)
            except (ValueError, KeyError):
                raise exc.PyghmiException(str(url) + ":" + str(res[0]))
        if payload is None and method is None:
            self._urlcache[url] = {'contents': res[0],
                                   'vintage': os.times()[4]}
        return res[0]

    def get_bootdev(self):
        """Get current boot device override information.

        :raises: PyghmiException on error
        :returns: dict
        """
        result = self._do_web_request(self.sysurl)
        overridestate = result.get('Boot', {}).get(
            'BootSourceOverrideEnabled', None)
        if overridestate == 'Disabled':
            return {'bootdev': 'default', 'persistent': True}
        persistent = None
        if overridestate == 'Once':
            persistent = False
        elif overridestate == 'Continuous':
            persistent = True
        else:
            raise exc.PyghmiException('Unrecognized Boot state: %s'
                                      % repr(overridestate))
        uefimode = result.get('Boot', {}).get('BootSourceOverrideMode', None)
        if uefimode == 'UEFI':
            uefimode = True
        elif uefimode == 'Legacy':
            uefimode = False
        else:
            raise exc.PyghmiException('Unrecognized mode: %s' % uefimode)
        bootdev = result.get('Boot', {}).get('BootSourceOverrideTarget', None)
        if bootdev not in boot_devices_read:
            raise exc.PyghmiException('Unrecognized boot target: %s'
                                      % repr(bootdev))
        bootdev = boot_devices_read[bootdev]
        return {'bootdev': bootdev, 'persistent': persistent,
                'uefimode': uefimode}

    def set_bootdev(self, bootdev, persist=False, uefiboot=None):
        """Set boot device to use on next reboot

        :param bootdev:
                        *network -- Request network boot
                        *hd -- Boot from hard drive
                        *safe -- Boot from hard drive, requesting 'safe mode'
                        *optical -- boot from CD/DVD/BD drive
                        *setup -- Boot into setup utility
                        *default -- remove any directed boot device request
        :param persist: If true, ask that system firmware use this device
                        beyond next boot.  Be aware many systems do not honor
                        this
        :param uefiboot: If true, request UEFI boot explicitly.  If False,
                         request BIOS style boot.
                         None (default) does not modify the boot mode.
        :raises: PyghmiException on an error.
        :returns: dict or True -- If callback is not provided, the response
        """
        return self.oem.set_bootdev(bootdev, persist, uefiboot, self)

    @property
    def _biosurl(self):
        if not self._varbiosurl:
            self._varbiosurl = self.sysinfo.get('Bios', {}).get('@odata.id',
                                                                None)
        if self._varbiosurl is None:
            raise exc.UnsupportedFunctionality(
                'Bios management not detected on this platform')
        return self._varbiosurl

    @property
    def _setbiosurl(self):
        if self._varsetbiosurl is None:
            biosinfo = self._do_web_request(self._biosurl)
            self._varsetbiosurl = biosinfo.get(
                '@Redfish.Settings', {}).get('SettingsObject', {}).get(
                    '@odata.id', None)
        if self._varsetbiosurl is None:
            raise exc.UnsupportedFunctionality('Ability to set BIOS settings '
                                               'not detected on this platform')
        return self._varsetbiosurl

    @property
    def _sensormap(self):
        if not self._varsensormap:
            if self.sysinfo:
                for chassis in self.sysinfo.get('Links', {}).get('Chassis', []):
                    self._mapchassissensors(chassis)
            else:  # no system, but check if this is a singular chassis
                rootinfo = self._do_web_request('/redfish/v1/')
                chassiscol = rootinfo.get('Chassis', {}).get('@odata.id', '')
                if chassiscol:
                    chassislist = self._do_web_request(chassiscol)
                    if len(chassislist.get('Members', [])) == 1:
                        self._mapchassissensors(chassislist['Members'][0])
        return self._varsensormap

    def _mapchassissensors(self, chassis):
        chassisurl = chassis['@odata.id']
        chassisinfo = self._do_web_request(chassisurl)
        sensors = None
        if self.oem.usegenericsensors:
            sensors = chassisinfo.get('Sensors', {}).get('@odata.id', '')
        if sensors:
            sensorinf = self._do_web_request(sensors)
            for sensor in sensorinf.get('Members', []):
                sensedata = self._do_web_request(sensor['@odata.id'])
                if 'Name' in sensedata:
                    sensetype = sensedata.get('ReadingType', 'Unknown')
                    self._varsensormap[sensedata['Name']] = {
                        'name': sensedata['Name'], 'type': sensetype,
                        'url': sensor['@odata.id'], 'generic': True}
        else:
            powurl = chassisinfo.get('Power', {}).get('@odata.id', '')
            if powurl:
                powinf = self._do_web_request(powurl)
                for voltage in powinf.get('Voltages', []):
                    if 'Name' in voltage:
                        self._varsensormap[voltage['Name']] = {
                            'name': voltage['Name'], 'url': powurl,
                            'type': 'Voltage'}
            thermurl = chassisinfo.get('Thermal', {}).get('@odata.id', '')
            if thermurl:
                therminf = self._do_web_request(thermurl)
                for fan in therminf.get('Fans', []):
                    if 'Name' in fan:
                        self._varsensormap[fan['Name']] = {
                            'name': fan['Name'], 'type': 'Fan',
                            'url': thermurl}
                for temp in therminf.get('Temperatures', []):
                    if 'Name' in temp:
                        self._varsensormap[temp['Name']] = {
                            'name': temp['Name'], 'type': 'Temperature',
                            'url': thermurl}
        for subchassis in chassisinfo.get('Links', {}).get('Contains', []):
            self._mapchassissensors(subchassis)

    def _get_thermals(self, chassis):
        chassisurl = chassis['@odata.id']
        chassisinfo = self._do_web_request(chassisurl)
        thermurl = chassisinfo.get('Thermal', {}).get('@odata.id', '')
        if thermurl:
            therminf = self._do_web_request(thermurl, cache=1)
            return therminf.get('Temperatures', [])

    @property
    def _bmcurl(self):
        if not self._varbmcurl:
            self._varbmcurl = self.sysinfo.get('Links', {}).get(
                'ManagedBy', [{}])[0].get('@odata.id', None)
        return self._varbmcurl

    @property
    def _bmcnicurl(self):
        if not self._varbmcnicurl:
            self._varbmcnicurl = self._get_bmc_nic_url()
        return self._varbmcnicurl

    def list_network_interface_names(self):
        bmcinfo = self._do_web_request(self._bmcurl)
        nicurl = bmcinfo.get('EthernetInterfaces', {}).get('@odata.id', None)
        if not nicurl:
            return
        niclist = self._do_web_request(nicurl)
        for nic in niclist.get('Members', []):
            curl = nic.get('@odata.id', None)
            if not curl:
                continue
            yield curl.rsplit('/', 1)[1]

    def _get_bmc_nic_url(self, name=None):
        bmcinfo = self._do_web_request(self._bmcurl)
        nicurl = bmcinfo.get('EthernetInterfaces', {}).get('@odata.id', None)
        niclist = self._do_web_request(nicurl)
        foundnics = 0
        lastnicurl = None
        for nic in niclist.get('Members', []):
            curl = nic.get('@odata.id', None)
            if not curl:
                continue
            if name is not None:
                if curl.endswith('/{0}'.format(name)):
                    return curl
                continue
            if self.oem.hostnic and curl.endswith('/{0}'.format(
                    self.oem.hostnic)):
                continue
            nicinfo = self._do_web_request(curl)
            if nicinfo.get('Links', {}).get('HostInterface', None):
                # skip host interface
                continue
            if not nicinfo.get('InterfaceEnabled', True):
                # skip disabled interfaces
                continue
            for addrs in nicinfo.get('IPv4Addresses', []):
                v4addr = socket.inet_pton(
                    socket.AF_INET, addrs.get('Address', '0.0.0.0'))
                if self._bmcv4ip == v4addr:
                    return curl
            for addrs in nicinfo.get('IPv6Addresses', []):
                v6addr = socket.inet_pton(
                    socket.AF_INET6, addrs.get('Address', '::'))
                if self._bmcv6ip == v6addr:
                    return curl
            foundnics += 1
            lastnicurl = curl
        if name is None and foundnics != 1:
            raise exc.PyghmiException(
                'BMC does not have exactly one interface')
        if name is None:
            return lastnicurl

    @property
    def _bmcresetinfo(self):
        if not self._varresetbmcurl:
            bmcinfo = self._do_web_request(self._bmcurl)
            resetinf = bmcinfo.get('Actions', {}).get('#Manager.Reset', {})
            url = resetinf.get('target', '')
            valid = resetinf.get('ResetType@Redfish.AllowableValues', [])
            if not valid:
                tmpurl = resetinf.get('@Redfish.ActionInfo', None)
                if tmpurl:
                    resetinf = self._do_web_request(tmpurl)
                    valid = resetinf.get('Parameters', [{}])[0].get(
                        'AllowableValues')
            resettype = None
            if 'GracefulRestart' in valid:
                resettype = 'GracefulRestart'
            elif 'ForceRestart' in valid:
                resettype = 'ForceRestart'
            elif 'ColdReset' in valid:
                resettype = 'ColdReset'
            self._varresetbmcurl = url, resettype
        return self._varresetbmcurl

    def reset_bmc(self):
        url, action = self._bmcresetinfo
        if not url:
            raise Exception('BMC does not provide reset action')
        if not action:
            raise Exception('BMC does not accept a recognized reset type')
        self._do_web_request(url, {'ResetType': action})

    def set_identify(self, on=True, blink=None):
        if hasattr(self.oem, 'set_identify'):
            return self.oem.set_identify(on, blink)
        targurl = self.sysurl
        if not targurl:
            root = self._do_web_request('/redfish/v1')
            systemsurl = root.get('Systems', {}).get('@odata.id', None)
            if systemsurl:
                targurl = self._do_web_request(systemsurl)
                if len(targurl.get('Members', [])) == 1:
                    targurl = targurl['Members'][0]['@odata.id']
        if not targurl:
            raise Exception("Unable to identify system url")
        self._do_web_request(
            targurl,
            {'IndicatorLED': 'Blinking' if blink else 'Lit' if on else 'Off'},
            method='PATCH', etag='*')

    _idstatemap = {
        'Blinking': 'blink',
        'Lit': 'on',
        'Off': 'off',
    }

    def get_identify(self):
        ledstate = self.sysinfo['IndicatorLED']
        return {'identifystate': self._idstatemap[ledstate]}

    def get_health(self, verbose=True):
        return self.oem.get_health(self, verbose)

    def get_extended_bmc_configuration(self, hideadvanced=True):
        return self.oem.get_extended_bmc_configuration(self, hideadvanced=hideadvanced)

    def get_bmc_configuration(self):
        """Get miscellaneous BMC configuration

        In much the same way a bmc can present arbitrary key-value
        structure for BIOS/UEFI configuration, provide a mechanism
        for a BMC to provide arbitrary key-value for BMC specific
        settings.
        """

        # For now, this is a stub, no implementation for redfish currently
        return self.oem.get_bmc_configuration()

    def set_bmc_configuration(self, changeset):
        """Get miscellaneous BMC configuration

        In much the same way a bmc can present arbitrary key-value
        structure for BIOS/UEFI configuration, provide a mechanism
        for a BMC to provide arbitrary key-value for BMC specific
        settings.
        """

        # For now, this is a stub, no implementation for redfish currently
        return self.oem.set_bmc_configuration(changeset)

    def set_system_configuration(self, changeset):
        return self.oem.set_system_configuration(changeset, self)

    def get_ntp_enabled(self):
        bmcinfo = self._do_web_request(self._bmcurl)
        netprotocols = bmcinfo.get('NetworkProtocol', {}).get('@odata.id', None)
        if netprotocols:
            netprotoinfo = self._do_web_request(netprotocols)
            enabled = netprotoinfo.get('NTP', {}).get('ProtocolEnabled', False)
            return enabled
        return False

    def set_ntp_enabled(self, enable):
        bmcinfo = self._do_web_request(self._bmcurl)
        netprotocols = bmcinfo.get('NetworkProtocol', {}).get('@odata.id', None)
        if netprotocols:
            request = {'NTP':{'ProtocolEnabled': enable}}
            self._do_web_request(netprotocols, request, method='PATCH')
            self._do_web_request(netprotocols, cache=0)

    def get_ntp_servers(self):
        bmcinfo = self._do_web_request(self._bmcurl)
        netprotocols = bmcinfo.get('NetworkProtocol', {}).get('@odata.id', None)
        if not netprotocols:
            return []
        netprotoinfo = self._do_web_request(netprotocols)
        return netprotoinfo.get('NTP', {}).get('NTPServers', [])

    def set_ntp_server(self, server, index=None):
        bmcinfo = self._do_web_request(self._bmcurl)
        netprotocols = bmcinfo.get('NetworkProtocol', {}).get('@odata.id', None)
        currntpservers = self.get_ntp_servers()
        if index is None:
            if server in currntpservers:
                return
            currntpservers = [server] + currntpservers
        else:
            if (index + 1) > len(currntpservers):
                if not server:
                    return
                currntpservers.append(server)
            else:
                if not server:
                    del currntpservers[index]
                else:
                    currntpservers[index] = server
        request = {'NTP':{'NTPServers': currntpservers}}
        self._do_web_request(netprotocols, request, method='PATCH')
        self._do_web_request(netprotocols, cache=0)


    def clear_bmc_configuration(self):
        """Reset BMC to factory default

        Call appropriate function to clear BMC to factory default settings.
        In many cases, this may render remote network access impracticle or
        impossible."
        """
        bmcinfo = self._do_web_request(self._bmcurl)
        rc = bmcinfo.get('Actions', {}).get('#Manager.ResetToDefaults', {})
        actinf = rc.get('ResetType@Redfish.AllowableValues', [])
        if 'ResetAll' in actinf:
            acturl = rc.get('target', None)
            if acturl:
                self._do_web_request(acturl, {'ResetType': 'ResetAll'})
                return
        raise exc.UnsupportedFunctionality(
            'Clear BMC configuration not supported on this platform')

    def get_system_configuration(self, hideadvanced=True):
        return self.oem.get_system_configuration(hideadvanced, self)

    def clear_system_configuration(self):
        """Clear the BIOS/UEFI configuration

        """
        biosinfo = self._do_web_request(self._biosurl)
        rb = biosinfo.get('Actions', {}).get('#Bios.ResetBios', {})
        actinf = rb.get('@Redfish.ActionInfo', None)
        rb = rb.get('target', '')
        parms = {}
        if actinf:
            actinf = self._do_web_request(
                '/redfish/v1/Systems/Self/Bios/ResetBiosActionInfo')
            for parm in actinf.get('Parameters', ()):
                if parm.get('Required', False):
                    if parm.get('Name', None) == 'ResetType' and parm.get(
                            'AllowableValues', [None])[0] == 'Reset':
                        parms['ResetType'] = 'Reset'
                    else:
                        raise Exception(
                            'Unrecognized required parameter {0}'.format(
                                parm.get('Name', 'Unknown')))
        if not rb:
            raise Exception('BIOS reset not detected on this system')
        if not parms:
            parms = {'Action': 'Bios.ResetBios'}
        self._do_web_request(rb, parms)

    def set_net6_configuration(self, static_addresses=None, static_gateway=None, name=None):
        patch = {}
        if static_addresses is not None:
            sa = []
            patch['IPv6StaticAddresses'] = sa
            for addr in static_addresses:
                if '/' in addr:
                    addr, plen = addr.split('/', 1)
                else:
                    plen = '64'
                sa.append({
                    'PrefixLength': int(plen),
                    'Address': addr
                })
        if static_gateway:
            patch['IPv6StaticDefaultGateways'] = [{
                'Address': static_gateway,
            }]
        if patch:
            nicurl = self._get_bmc_nic_url(name)
            self._do_web_request(nicurl, patch, 'PATCH')

    def set_net_configuration(self, ipv4_address=None, ipv4_configuration=None,
                              ipv4_gateway=None, name=None):
        patch = {}
        ipinfo = {}
        dodhcp = None
        netmask = None
        if (ipv4_address is None and ipv4_configuration is None
                and ipv4_gateway is None):
            return
        if ipv4_address:
            if '/' in ipv4_address:
                ipv4_address, cidr = ipv4_address.split('/')
                netmask = _cidr_to_mask(int(cidr))
            patch['IPv4StaticAddresses'] = [ipinfo]
            ipinfo['Address'] = ipv4_address
            ipv4_configuration = 'static'
            if netmask:
                ipinfo['SubnetMask'] = netmask
        if ipv4_gateway:
            patch['IPv4StaticAddresses'] = [ipinfo]
            ipinfo['Gateway'] = ipv4_gateway
            ipv4_configuration = 'static'
        if ipv4_configuration and ipv4_configuration.lower() == 'dhcp':
            dodhcp = True
            patch['DHCPv4'] = {'DHCPEnabled': True}
        elif (ipv4_configuration == 'static'
              or 'IPv4StaticAddresses' in patch):
            dodhcp = False
            patch['DHCPv4'] = {'DHCPEnabled': False}
        if patch:
            nicurl = self._get_bmc_nic_url(name)
            try:
                self._do_web_request(nicurl, patch, 'PATCH')
            except exc.RedfishError:
                patch = {'IPv4Addresses': [ipinfo]}
                if dodhcp:
                    ipinfo['AddressOrigin'] = 'DHCP'
                elif dodhcp is not None:
                    ipinfo['AddressOrigin'] = 'Static'
                self._do_web_request(nicurl, patch, 'PATCH')

    def get_net6_configuration(self, name=None):
        nicurl = self._get_bmc_nic_url(name)
        netcfg = self._do_web_request(nicurl, cache=False)
        retdata = {}
        saddrs = netcfg.get('IPv6StaticAddresses', ())
        retdata['static_addrs'] = []
        for sa in saddrs:
            ca = '{}/{}'.format(sa['Address'], sa['PrefixLength'])
            retdata['static_addrs'].append(ca)
        gws = netcfg.get('IPv6StaticDefaultGateways', None)
        if gws:
            for gw in gws:
                retdata['static_gateway'] = gw['Address']
        return retdata

    def get_net_configuration(self, name=None):
        nicurl = self._get_bmc_nic_url(name)
        netcfg = self._do_web_request(nicurl, cache=False)
        ipv4 = netcfg.get('IPv4Addresses', {})
        if not ipv4:
            raise exc.PyghmiException('Unable to locate network information')
        retval = {}
        if len(netcfg['IPv4Addresses']) != 1:
            netcfg['IPv4Addresses'] = [
                x for x in netcfg['IPv4Addresses']
                if x['Address'] != '0.0.0.0']
        if len(netcfg['IPv4Addresses']) != 1:
            raise exc.PyghmiException('Multiple IP addresses not supported')
        currip = netcfg['IPv4Addresses'][0]
        cidr = _mask_to_cidr(currip['SubnetMask'])
        retval['ipv4_address'] = '{0}/{1}'.format(currip['Address'], cidr)
        retval['mac_address'] = netcfg['MACAddress']
        hasgateway = _mask_to_cidr(currip['Gateway'])
        retval['ipv4_gateway'] = currip['Gateway'] if hasgateway else None
        retval['ipv4_configuration'] = currip['AddressOrigin']
        return retval

    def get_hostname(self):
        netcfg = self._do_web_request(self._bmcnicurl)
        return netcfg['HostName']

    def set_hostname(self, hostname):
        self._do_web_request(self._bmcnicurl,
                             {'HostName': hostname}, 'PATCH')

    def get_firmware(self, components=()):
        self._fwnamemap = {}
        try:
            for firminfo in self.oem.get_firmware_inventory(components, self):
                yield firminfo
        except exc.BypassGenericBehavior:
            return
        fwlist = self._do_web_request(self._fwinventory)
        fwurls = [x['@odata.id'] for x in fwlist.get('Members', [])]
        for res in self._do_bulk_requests(fwurls):
            res = self._extract_fwinfo(res)
            if res[0] is None:
                continue
            yield res

    def _extract_fwinfo(self, inf):
        currinf = self._oem._extract_fwinfo(inf)
        fwi, url = inf
        fwname = fwi.get('Name', 'Unknown')
        if fwname in self._fwnamemap:
            fwname = fwi.get('Id', fwname)
        if fwname in self._fwnamemap:
            # Block duplicates for by name retrieval
            self._fwnamemap[fwname] = None
        else:
            self._fwnamemap[fwname] = url
        currinf['name'] = fwname
        currinf['id'] = fwi.get('Id', None)
        currinf['version'] = fwi.get('Version', 'Unknown')
        currinf['date'] = parse_time(fwi.get('ReleaseDate', ''))
        currinf['software_id'] = fwi.get('SoftwareId', '')
        if not (currinf['version'] or currinf['date']):
            return None, None
        # TODO(Jarrod Johnson): OEM extended data with buildid
        currstate = fwi.get('Status', {}).get('State', 'Unknown')
        if currstate == 'StandbyOffline':
            currinf['state'] = 'pending'
        elif currstate == 'Enabled':
            currinf['state'] = 'active'
        elif currstate == 'StandbySpare':
            currinf['state'] = 'backup'
        return fwname, currinf

    def get_inventory_descriptions(self, withids=False):
        return self.oem.get_inventory_descriptions(withids)

    def get_inventory_of_component(self, component):
        return self.oem.get_inventory_of_component(component)

    def get_inventory(self, withids=False):
        return self.oem.get_inventory(withids)

    def get_location_information(self):
        locationinfo = {}
        for chassis in self.sysinfo.get('Links', {}).get('Chassis', []):
            chassisurl = chassis['@odata.id']
            data = self._do_web_request(chassisurl)
            locdata = data.get('Location', {})
            postaladdress = locdata.get('PostalAddress', {})
            placement = locdata.get('Placement', {})
            contactinfo = locdata.get('Contacts', [])
            currval = postaladdress.get('Room', '')
            if currval:
                locationinfo['room'] = currval
            currval = postaladdress.get('Location', '')
            if currval:
                locationinfo['location'] = currval
            currval = postaladdress.get('Building', '')
            if currval:
                locationinfo['building'] = currval
            currval = placement.get('Rack', '')
            if currval:
                locationinfo['rack'] = currval
            for contact in contactinfo:
                contact = contact.get('ContactName', '')
                if not contact:
                    continue
                if 'contactnames' not in locationinfo:
                    locationinfo['contactnames'] = [contact]
                else:
                    locationinfo['contactnames'].append(contact)
        return locationinfo

    def set_location_information(self, room=None, contactnames=None,
                                 location=None, building=None, rack=None):
        locationinfo = {}
        postaladdress = {}
        placement = {}
        if contactnames is not None:
            locationinfo['Contacts'] = [
                {'ContactName': x} for x in contactnames]
        if room is not None:
            postaladdress['Room'] = room
        if location is not None:
            postaladdress['Location'] = location
        if building is not None:
            postaladdress['Building'] = building
        if rack is not None:
            placement['Rack'] = rack
        if postaladdress:
            locationinfo['PostalAddress'] = postaladdress
        if placement:
            locationinfo['Placement'] = placement
        if locationinfo:
            for chassis in self.sysinfo.get('Links', {}).get('Chassis', []):
                chassisurl = chassis['@odata.id']
                self._do_web_request(chassisurl, {'Location': locationinfo},
                                     method='PATCH')

    @property
    def oem(self):
        if not self._oem:
            if self.sysurl:
                self._do_web_request(self.sysurl, cache=False)  # This is to trigger token validation and renewel
            elif self._varbmcurl:
                self._do_web_request(self._varbmcurl, cache=False)  # This is to trigger token validation and renewel
            self._oem = oem.get_oem_handler(
                self.sysinfo, self.sysurl, self.wc, self._urlcache, self)
            self._oem.set_credentials(self.username, self.password)
        return self._oem

    def get_description(self):
        return self.oem.get_description(self)

    def get_event_log(self, clear=False):
        return self.oem.get_event_log(clear, self)

    def _get_chassis_env(self, chassis):
        chassisurl = chassis['@odata.id']
        chassisinfo = self._do_web_request(chassisurl)
        envurl = chassisinfo.get('EnvironmentMetrics', {}).get('@odata.id', '')
        if not envurl:
            return {}
        envmetric = self._do_web_request(envurl, cache=1)
        retval = {
            'watts': envmetric.get('PowerWatts', {}).get('Reading', None),
            'inlet': envmetric.get('TemperatureCelsius', {}).get('Reading', None)
        }
        return retval

    def get_average_processor_temperature(self):
        return self.oem.get_average_processor_temperature(self)


    def get_system_power_watts(self):
        return self.oem.get_system_power_watts(self)

    def get_inlet_temperature(self):
        inlets = []
        for chassis in self.sysinfo.get('Links', {}).get('Chassis', []):
            envinfo = self._get_chassis_env(chassis)
            currinlet = envinfo.get('inlet', None)
            if currinlet:
                inlets.append(currinlet)
        if inlets:
            val = sum(inlets) / len(inlets)
            unavail = False
        else:
            val = None
            unavail = True
        return SensorReading(
                        None, {'name': 'Inlet Temperature'}, value=val, units='°C',
                        unavailable=unavail)
    def get_sensor_descriptions(self):
        for sensor in natural_sort(self._sensormap):
            yield self._sensormap[sensor]

    def get_sensor_reading(self, sensorname):
        if sensorname not in self._sensormap:
            raise Exception('Sensor not found')
        sensor = self._sensormap[sensorname]
        reading = self._do_web_request(sensor['url'], cache=1)
        return self._extract_reading(sensor, reading)

    def get_sensor_data(self):
        for sensor in natural_sort(self._sensormap):
            yield self.get_sensor_reading(sensor)

    def _extract_reading(self, sensor, reading):
        if sensor.get('generic', False):  # generic sensor
            val = reading.get('Reading', None)
            unavail = val is None
            units = reading.get('ReadingUnits', None)
            if units == 'Cel':
                units = '°C'
            if units == 'cft_i/min':
                units = 'CFM'
            return SensorReading(reading, None, value=val, units=units,
                          unavailable=unavail)
        if sensor['type'] == 'Fan':
            for fan in reading['Fans']:
                if fan['Name'] == sensor['name']:
                    val = fan.get('Reading', None)
                    unavail = val is None
                    units = fan.get('ReadingUnits', None)
                    return SensorReading(
                        None, sensor, value=val, units=units,
                        unavailable=unavail)
        elif sensor['type'] == 'Temperature':
            for temp in reading['Temperatures']:
                if temp['Name'] == sensor['name']:
                    val = temp.get('ReadingCelsius', None)
                    unavail = val is None
                    return SensorReading(
                        None, sensor, value=val, units='°C',
                        unavailable=unavail)
        elif sensor['type'] == 'Voltage':
            for volt in reading['Voltages']:
                if volt['Name'] == sensor['name']:
                    val = volt.get('ReadingVolts', None)
                    unavail = val is None
                    return SensorReading(
                        None, sensor, value=val, units='V',
                        unavailable=unavail)

    def list_media(self):
        return self.oem.list_media(self)

    def get_storage_configuration(self):
        """"Get storage configuration data

        Retrieves the storage configuration from the target.  Data is given
        about disks, pools, and volumes.  When referencing something, use the
        relevant 'cfgpath' attribute to describe it.  It is not guaranteed that
        cfgpath will be consistent version to version, so a lookup is suggested
        in end user applications.

        :return: A pyghmi.storage.ConfigSpec object describing current config
        """
        return self.oem.get_storage_configuration()

    def remove_storage_configuration(self, cfgspec):
        """Remove specified storage configuration from controller.

        :param cfgspec: A pyghmi.storage.ConfigSpec describing what to remove
        :return:
        """
        return self.oem.remove_storage_configuration(cfgspec)

    def apply_storage_configuration(self, cfgspec=None):
        """Evaluate a configuration for validity

        This will check if configuration is currently available and, if given,
        whether the specified cfgspec can be applied.
        :param cfgspec: A pyghmi.storage.ConfigSpec describing desired oonfig
        :return:
        """
        return self.oem.apply_storage_configuration(cfgspec)

    def check_storage_configuration(self, cfgspec=None):
        """Evaluate a configuration for validity

        This will check if configuration is currently available and, if given,
        whether the specified cfgspec can be applied.
        :param cfgspec: A pyghmi.storage.ConfigSpec describing desired oonfig
        :return:
        """
        return self._oem.check_storage_configuration(cfgspec)

    def attach_remote_media(self, url, username=None, password=None):
        """Attach remote media by url

        Given a url, attach remote media (cd/usb image) to the target system.

        :param url:  URL to indicate where to find image (protocol support
                     varies by BMC)
        :param username: Username for endpoint to use when accessing the URL.
                         If applicable, 'domain' would be indicated by '@' or
                         '\' syntax.
        :param password: Password for endpoint to use when accessing the URL.
        """
        # At the moment, there isn't a viable way to
        # identify the correct resource ahead of time.
        # As such it's OEM specific until the standard
        # provides a better way.
        vmurls = []
        vmcoll = self.sysinfo.get(
            'VirtualMedia', {}).get('@odata.id', None)
        if not vmcoll:
            vmcoll = self.bmcinfo.get(
                'VirtualMedia', {}).get('@odata.id', None)
        if vmcoll:
            vmlist = self._do_web_request(vmcoll)
            vmurls = [x['@odata.id'] for x in vmlist.get('Members', [])]
        suspendedxauth = False
        if 'X-Auth-Token' in self.wc.stdheaders:
            suspendedxauth = True
            del self.wc.stdheaders['X-Auth-Token']
            self.wc.set_basic_credentials(self.username, self.password)
        try:
            self.oem.attach_remote_media(url, username, password, vmurls)
        except exc.BypassGenericBehavior:
            if suspendedxauth:
                self.wc.stdheaders['X-Auth-Token'] = self.xauthtoken
                if 'Authorization' in self.wc.stdheaders:
                    del self.wc.stdheaders['Authorization']
            return
        for vmurl in vmurls:
            vminfo = self._do_web_request(vmurl, cache=False)
            if vminfo.get('ConnectedVia', None) != 'NotConnected':
                continue
            inserturl = vminfo.get(
                'Actions', {}).get(
                    '#VirtualMedia.InsertMedia', {}).get('target', None)
            if inserturl:
                self._do_web_request(inserturl, {'Image': url})
            else:
                try:
                    self._do_web_request(vmurl,
                                         {'Image': url, 'Inserted': True},
                                         'PATCH')
                except exc.RedfishError as re:
                    if re.msgid.endswith(u'PropertyUnknown'):
                        self._do_web_request(vmurl, {'Image': url}, 'PATCH')
                    else:
                        raise
            break
        if suspendedxauth:
                self.wc.stdheaders['X-Auth-Token'] = self.xauthtoken
                if 'Authorization' in self.wc.stdheaders:
                    del self.wc.stdheaders['Authorization']
        for res in self.oem.list_media(self, cache=False):
            pass

    def detach_remote_media(self):
        try:
            self.oem.detach_remote_media()
        except exc.BypassGenericBehavior:
            return
        vmcoll = self.sysinfo.get('VirtualMedia', {}).get('@odata.id', None)
        if not vmcoll:
            bmcinfo = self._do_web_request(self._bmcurl)
            vmcoll = bmcinfo.get('VirtualMedia', {}).get('@odata.id', None)
        if vmcoll:
            vmlist = self._do_web_request(vmcoll)
            vmurls = [x['@odata.id'] for x in vmlist.get('Members', [])]
            for vminfo in self._do_bulk_requests(vmurls):
                vminfo, currl = vminfo
                if vminfo['Image']:
                    ejurl = vminfo.get(
                        'Actions', {}).get(
                            '#VirtualMedia.EjectMedia', {}).get('target', None)
                    if ejurl:
                        self._do_web_request(ejurl, {})
                    else:
                        try:
                            self._do_web_request(currl,
                                                 {'Image': None,
                                                  'Inserted': False},
                                                 method='PATCH')
                        except exc.RedfishError as re:
                            if re.msgid.endswith(u'PropertyUnknown'):
                                self._do_web_request(currl, {'Image': None},
                                                     method='PATCH')
                            else:
                                raise
        for res in self.oem.list_media(self, cache=False):
            pass

    def upload_media(self, filename, progress=None, data=None):
        """Upload a file to be hosted on the target BMC

        This will upload the specified data to
        the BMC so that it will make it available to the system as an emulated
        USB device.

        :param filename: The filename to use, the basename of the parameter
                         will be given to the bmc.
        :param progress: Optional callback for progress updates
        """
        return self.oem.upload_media(filename, progress, data)

    def get_update_status(self):
        return self.oem.get_update_status()

    def update_firmware(self, file, data=None, progress=None, bank=None):
        """Send file to BMC to perform firmware update

         :param filename:  The filename to upload to the target BMC
         :param data:  The payload of the firmware.  Default is to read from
                       specified filename.
         :param progress:  A callback that will be given a dict describing
                           update process.  Provide if
         :param bank: Indicate a target 'bank' of firmware if supported
        """
        if progress is None:
            progress = lambda x: True
        return self.oem.update_firmware(file, data, progress, bank)

    def get_diagnostic_data(self, savefile, progress=None, autosuffix=False):
        if os.path.exists(savefile) and not os.path.isdir(savefile):
            raise exc.InvalidParameterValue(
                'Not allowed to overwrite existing file: {0}'.format(
                    savefile))
        return self.oem.get_diagnostic_data(savefile, progress, autosuffix)

    def get_licenses(self):
        return self.oem.get_licenses(self)

    def delete_license(self, name):
        return self.oem.delete_license(name, self)

    def save_licenses(self, directory):
        if os.path.exists(directory) and not os.path.isdir(directory):
            raise exc.InvalidParameterValue(
                'Not allowed to overwrite existing file: {0}'.format(
                    directory))
        return self.oem.save_licenses(directory, self)

    def apply_license(self, filename, progress=None, data=None):
        return self.oem.apply_license(filename, self, progress, data)


if __name__ == '__main__':
    print(repr(
        Command(sys.argv[1], os.environ['BMCUSER'], os.environ['BMCPASS'],
                verifycallback=lambda x: True).get_power()))

