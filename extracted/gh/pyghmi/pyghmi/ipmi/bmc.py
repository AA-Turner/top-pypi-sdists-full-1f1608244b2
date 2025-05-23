# Copyright 2015 Lenovo
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

import struct
import traceback

import pyghmi.ipmi.command as ipmicommand
import pyghmi.ipmi.console as console
import pyghmi.ipmi.private.serversession as serversession
import pyghmi.ipmi.private.session as ipmisession


__author__ = 'jjohnson2@lenovo.com'


class Bmc(serversession.IpmiServer):

    activated = False
    sol = None
    iohandler = None

    def get_system_guid(self):
        raise NotImplementedError

    def cold_reset(self):
        raise NotImplementedError

    def power_off(self):
        raise NotImplementedError

    def power_on(self):
        raise NotImplementedError

    def power_cycle(self):
        raise NotImplementedError

    def power_reset(self):
        raise NotImplementedError

    def pulse_diag(self):
        raise NotImplementedError

    def power_shutdown(self):
        raise NotImplementedError

    def get_power_state(self):
        raise NotImplementedError

    def is_active(self):
        raise NotImplementedError

    def activate_payload(self, request, session):
        if self.iohandler is None:
            session.send_ipmi_response(code=0x81)
        elif not self.is_active():
            session.send_ipmi_response(code=0x81)
        elif self.activated:
            session.send_ipmi_response(code=0x80)
        else:
            self.activated = True
            solport = list(struct.unpack('BB', struct.pack('!H', self.port)))
            session.send_ipmi_response(
                data=[0, 0, 0, 0, 1, 0, 1, 0] + solport + [0xff, 0xff])
            self.sol = console.ServerConsole(session, self.iohandler)

    def deactivate_payload(self, request, session):
        if self.iohandler is None:
            session.send_ipmi_response(code=0x81)
        elif not self.activated:
            session.send_ipmi_response(code=0x80)
        else:
            session.send_ipmi_response()
            self.sol.close()
            self.activated = False
            self.sol = None

    @staticmethod
    def handle_missing_command(session):
        session.send_ipmi_response(code=0xc1)

    def get_chassis_status(self, session):
        try:
            powerstate = self.get_power_state()
        except NotImplementedError:
            return session.send_ipmi_response(code=0xc1)
        if powerstate in ipmicommand.power_states:
            powerstate = ipmicommand.power_states[powerstate]
        if powerstate not in (0, 1):
            raise Exception('BMC implementation mistake')
        statusdata = [powerstate, 0, 0]
        session.send_ipmi_response(data=statusdata)

    def control_chassis(self, request, session):
        rc = 0
        try:
            directive = request['data'][0]
            if directive == 0:
                rc = self.power_off()
            elif directive == 1:
                rc = self.power_on()
            elif directive == 2:
                rc = self.power_cycle()
            elif directive == 3:
                rc = self.power_reset()
            elif directive == 4:
                # i.e. Pulse a diagnostic interrupt(NMI) directly
                rc = self.pulse_diag()
            elif directive == 5:
                rc = self.power_shutdown()
            if rc is None:
                rc = 0
            session.send_ipmi_response(code=rc)
        except NotImplementedError:
            session.send_ipmi_response(code=0xcc)

    def get_boot_device(self):
        raise NotImplementedError

    def get_system_boot_options(self, request, session):
        if request['data'][0] == 5:  # boot flags
            try:
                bootdevice = self.get_boot_device()
            except NotImplementedError:
                session.send_ipmi_response(data=[1, 5, 0, 0, 0, 0, 0])
            if (type(bootdevice) != int
                    and bootdevice in ipmicommand.boot_devices):
                bootdevice = ipmicommand.boot_devices[bootdevice]
            paramdata = [1, 5, 0b10000000, bootdevice, 0, 0, 0]
            return session.send_ipmi_response(data=paramdata)
        else:
            session.send_ipmi_response(code=0x80)

    def set_boot_device(self, bootdevice):
        raise NotImplementedError

    def set_system_boot_options(self, request, session):
        if request['data'][0] in (0, 3, 4):
            # for now, just smile and nod at boot flag bit clearing
            # implementing it is a burden and implementing it does more to
            # confuse users than serve a useful purpose
            session.send_ipmi_response()
        elif request['data'][0] == 5:
            bootdevice = (request['data'][2] >> 2) & 0b1111
            try:
                bootdevice = ipmicommand.boot_devices[bootdevice]
            except KeyError:
                session.send_ipmi_response(code=0xcc)
                return
            self.set_boot_device(bootdevice)
            session.send_ipmi_response()
        else:
            raise NotImplementedError

    def handle_raw_request(self, request, session):
        try:
            if request['netfn'] == 6:
                if request['command'] == 1:  # get device id
                    return self.send_device_id(session)
                elif request['command'] == 2:  # cold reset
                    return session.send_ipmi_response(code=self.cold_reset())
                elif request['command'] == 0x37:  # get system guid
                    guid = self.get_system_guid()
                    return session.send_ipmi_response(code=0x00, data=guid.bytes_le)
                elif request['command'] == 0x48:  # activate payload
                    return self.activate_payload(request, session)
                elif request['command'] == 0x49:  # deactivate payload
                    return self.deactivate_payload(request, session)
            elif request['netfn'] == 0:
                if request['command'] == 1:  # get chassis status
                    return self.get_chassis_status(session)
                elif request['command'] == 2:  # chassis control
                    return self.control_chassis(request, session)
                elif request['command'] == 8:  # set boot options
                    return self.set_system_boot_options(request, session)
                elif request['command'] == 9:  # get boot options
                    return self.get_system_boot_options(request, session)
            session.send_ipmi_response(code=0xc1)
        except NotImplementedError:
            session.send_ipmi_response(code=0xc1)
        except Exception:
            session._send_ipmi_net_payload(code=0xff)
            traceback.print_exc()

    @classmethod
    def listen(cls, timeout=30):
        while True:
            ipmisession.Session.wait_for_rsp(timeout)
