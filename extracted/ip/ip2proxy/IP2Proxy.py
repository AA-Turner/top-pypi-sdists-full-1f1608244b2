# Copyright (C) 2002-2024 IP2Location.com
# All Rights Reserved
#
# This library is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; If not, see <http://www.gnu.org/licenses/>.

import sys
import struct
import socket
import ipaddress
import os
import json
import re

if sys.version < '3':
    import urllib, httplib
    def urlencode(x):
        return urllib.urlencode(x)
    def httprequest(x, usessl):
        try:
            # conn = httplib.HTTPConnection("api.ip2proxy.com")
            if (usessl is True):
                conn = httplib.HTTPSConnection("api.ip2proxy.com")
            else:
                conn = httplib.HTTPConnection("api.ip2proxy.com")
            conn.request("GET", "/?" + x)
            res = conn.getresponse()
            return json.loads(res.read())
        except:
            return None
    def u(x):
        return x.decode('utf-8')
    def b(x):
        return str(x)
else:
    import urllib.parse, http.client
    def urlencode(x):
        return urllib.parse.urlencode(x)
    def httprequest(x, usessl):
        try:
            # conn = http.client.HTTPConnection("api.ip2proxy.com")
            if (usessl is True):
                conn = http.client.HTTPSConnection("api.ip2proxy.com")
            else:
                conn = http.client.HTTPConnection("api.ip2proxy.com")
            conn.request("GET", "/?" + x)
            res = conn.getresponse()
            return json.loads(res.read())
        except:
            return None
    def u(x):
        if isinstance(x, bytes):
            return x.decode()
        return x
    def b(x):
        if isinstance(x, bytes):
            return x
        return x.encode('ascii')
        

# Windows version of Python does not provide it
#          for compatibility with older versions of Windows.
if not hasattr(socket, 'inet_pton'):
    def inet_pton(t, addr):
        import ctypes
        a = ctypes.WinDLL('ws2_32.dll')
        in_addr_p = ctypes.create_string_buffer(b(addr))
        if t == socket.AF_INET:
            out_addr_p = ctypes.create_string_buffer(4)
        elif t == socket.AF_INET6:
            out_addr_p = ctypes.create_string_buffer(16)
        n = a.inet_pton(t, in_addr_p, out_addr_p)
        if n == 0:
            raise ValueError('Invalid address')
        return out_addr_p.raw
    socket.inet_pton = inet_pton

_VERSION = '3.5.1' 
_NO_IP = 'MISSING IP ADDRESS'
_FIELD_NOT_SUPPORTED = 'NOT SUPPORTED'
_INVALID_IP_ADDRESS  = 'INVALID IP ADDRESS'
MAX_IPV4_RANGE = 4294967295
MAX_IPV6_RANGE = 340282366920938463463374607431768211455

class IP2ProxyRecord:
    ''' IP2Proxy record with all fields from the database '''
    ip = None
    country_short = _FIELD_NOT_SUPPORTED
    country_long = _FIELD_NOT_SUPPORTED
    region = _FIELD_NOT_SUPPORTED
    city = _FIELD_NOT_SUPPORTED
    isp = _FIELD_NOT_SUPPORTED
    proxy_type = _FIELD_NOT_SUPPORTED
    usage_type = _FIELD_NOT_SUPPORTED
    as_name = _FIELD_NOT_SUPPORTED
    asn = _FIELD_NOT_SUPPORTED
    last_seen = _FIELD_NOT_SUPPORTED
    domain = _FIELD_NOT_SUPPORTED
    threat = _FIELD_NOT_SUPPORTED
    provider = _FIELD_NOT_SUPPORTED
    fraud_score = _FIELD_NOT_SUPPORTED

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

_COUNTRY_POSITION             = (0,  2,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3)
_REGION_POSITION              = (0,  0,  0,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4)
_CITY_POSITION                = (0,  0,  0,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5)
_ISP_POSITION                 = (0,  0,  0,  0,  6,  6,  6,  6,  6,  6,  6,  6,  6)
_PROXYTYPE_POSITION           = (0,  0,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2)
_DOMAIN_POSITION              = (0,  0,  0,  0,  0,  7,  7,  7,  7,  7,  7,  7,  7)
_USAGETYPE_POSITION           = (0,  0,  0,  0,  0,  0,  8,  8,  8,  8,  8,  8,  8)
_ASN_POSITION                 = (0,  0,  0,  0,  0,  0,  0,  9,  9,  9,  9,  9,  9)
_AS_POSITION                  = (0,  0,  0,  0,  0,  0,  0, 10, 10, 10, 10, 10, 10)
_LASTSEEN_POSITION            = (0,  0,  0,  0,  0,  0,  0,  0, 11, 11, 11, 11, 11)
_THREAT_POSITION              = (0,  0,  0,  0,  0,  0,  0,  0,  0, 12, 12, 12, 12)
_PROVIDER_POSITION            = (0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 13, 13)
_FRAUD_SCORE_POSITION         = (0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 14)

class IP2Proxy(object):
    ''' IP2Proxy database '''

    def __init__(self, filename=None):
        ''' Creates a database object and opens a file if filename is given '''
        
        if filename:
            self.open(filename)

    def __enter__(self):
        if not hasattr(self, '_f') or self._f.closed:
            raise ValueError("Cannot enter context with closed file")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def open(self, filename):
        ''' Opens a database file '''
        # Ensure old file is closed before opening a new one
        self.close()
        
        # if filename is not None:
        if os.path.isfile(filename) == False:
            raise ValueError("The database file does not seem to exist.")

        self._f = open(filename, 'rb')
        self._f.seek(0)
        header_row = self._f.read(32)
        self._dbtype = struct.unpack('B', header_row[0:1])[0]
        self._dbcolumn = struct.unpack('B', header_row[1:2])[0]
        self._dbyear = struct.unpack('B', header_row[2:3])[0]
        self._dbmonth = struct.unpack('B', header_row[3:4])[0]
        self._dbday = struct.unpack('B', header_row[4:5])[0]
        self._ipv4dbcount = struct.unpack('<I', header_row[5:9])[0]
        self._ipv4dbaddr = struct.unpack('<I', header_row[9:13])[0]
        self._ipv6dbcount = struct.unpack('<I', header_row[13:17])[0]
        self._ipv6dbaddr = struct.unpack('<I', header_row[17:21])[0]
        self._ipv4indexbaseaddr = struct.unpack('<I', header_row[21:25])[0]
        self._ipv6indexbaseaddr = struct.unpack('<I', header_row[25:29])[0]
        self._productcode = struct.unpack('B', header_row[29:30])[0]
        self._licensecode = struct.unpack('B', header_row[30:31])[0]
        self._databasesize = struct.unpack('B', header_row[31:32])[0]
        if (self._productcode != 2) :
            if (self._dbyear > 20 and self._productcode != 0) :
                self._f.close()
                del self._f
                raise ValueError("Incorrect IP2Location BIN file format. Please make sure that you are using the latest IP2Location BIN file.")

    def close(self):
        if hasattr(self, '_f'):
            # If there is file close it.
            self._f.close()
            del self._f

    def get_module_version(self):
        return _VERSION

    def get_package_version(self):
        return str(self._dbtype)

    def get_database_version(self):
        return str(self._dbyear) + "." + str(self._dbmonth) + "." + str(self._dbday)

    def get_country_short(self, ip):
        ''' Get country_short '''
        try:
            rec = self._get_record(ip)
            country_short = rec.country_short
        except:
            country_short = _INVALID_IP_ADDRESS
        return country_short

    def get_country_long(self, ip):
        ''' Get country_long '''
        try:
            rec = self._get_record(ip)
            country_long = rec.country_long
        except:
            country_long = _INVALID_IP_ADDRESS
        return country_long

    def get_region(self, ip):
        ''' Get region '''
        try:
            rec = self._get_record(ip)
            region = rec.region
        except:
            region = _INVALID_IP_ADDRESS
        return region

    def get_city(self, ip):
        ''' Get city '''
        try:
            rec = self._get_record(ip)
            city = rec.city
        except:
            city = _INVALID_IP_ADDRESS
        return city

    def get_isp(self, ip):
        ''' Get isp '''
        try:
            rec = self._get_record(ip)
            isp = rec.isp
        except:
            isp = _INVALID_IP_ADDRESS
        return isp

    def get_proxy_type(self, ip):
        ''' Get proxy_type '''
        try:
            rec = self._get_record(ip)
            proxy_type = rec.proxy_type
        except:
            proxy_type = _INVALID_IP_ADDRESS
        return proxy_type

    def is_proxy(self, ip):
        ''' Determine whether is a proxy '''
        try:
            rec = self._get_record(ip)
            if rec.country_short != _INVALID_IP_ADDRESS:
                if self._dbtype == 1:
                    is_proxy = 0 if (rec.country_short == '-') else ( 2 if ((rec.proxy_type == 'DCH') | (rec.proxy_type == 'SES')) else 1)
                else:
                    is_proxy = 0 if (rec.proxy_type == '-') else ( 2 if ((rec.proxy_type == 'DCH') | (rec.proxy_type == 'SES')) else 1)
            else:
                is_proxy = -1
        except:
            is_proxy = -1
        return is_proxy

    def get_domain(self, ip):
        ''' Get domain '''
        try:
            rec = self._get_record(ip)
            domain = rec.domain
        except:
            domain = _INVALID_IP_ADDRESS
        return domain

    def get_usage_type(self, ip):
        ''' Get usage_type '''
        try:
            rec = self._get_record(ip)
            usage_type = rec.usage_type
        except:
            usage_type = _INVALID_IP_ADDRESS
        return usage_type

    def get_asn(self, ip):
        ''' Get asn '''
        try:
            rec = self._get_record(ip)
            asn = rec.asn
        except:
            asn = _INVALID_IP_ADDRESS
        return asn

    def get_as_name(self, ip):
        ''' Get as_name '''
        try:
            rec = self._get_record(ip)
            as_name = rec.as_name
        except:
            as_name = _INVALID_IP_ADDRESS
        return as_name

    def get_last_seen(self, ip):
        ''' Get last_seen '''
        try:
            rec = self._get_record(ip)
            last_seen = rec.last_seen
        except:
            last_seen = _INVALID_IP_ADDRESS
        return last_seen

    def get_threat(self, ip):
        ''' Get threat'''
        try:
            rec = self._get_record(ip)
            threat = rec.threat
        except:
            threat = _INVALID_IP_ADDRESS
        return threat

    def get_provider(self, ip):
        ''' Get provider'''
        try:
            rec = self._get_record(ip)
            provider = rec.provider
        except:
            provider = _INVALID_IP_ADDRESS
        return provider

    def get_fraud_score(self, ip):
        ''' Get fraud_score'''
        try:
            rec = self._get_record(ip)
            fraud_score = rec.fraud_score
        except:
            fraud_score = _INVALID_IP_ADDRESS
        return fraud_score

    def get_all(self, ip):
        ''' Get the whole record with all fields read from the file '''
        try:
            rec = self._get_record(ip)
            country_short = rec.country_short
            country_long = rec.country_long
            region = rec.region
            city = rec.city
            isp = rec.isp
            proxy_type = rec.proxy_type
            domain = rec.domain
            usage_type = rec.usage_type
            asn = rec.asn
            as_name = rec.as_name
            last_seen = rec.last_seen
            threat = rec.threat
            provider = rec.provider
            fraud_score = rec.fraud_score
            if rec.country_short != _INVALID_IP_ADDRESS:
                if self._dbtype == 1:
                    is_proxy = 0 if (rec.country_short == '-') else ( 2 if ((rec.proxy_type == 'DCH') | (rec.proxy_type == 'SES')) else 1)
                else:
                    is_proxy = 0 if (rec.proxy_type == '-') else ( 2 if ((rec.proxy_type == 'DCH') | (rec.proxy_type == 'SES')) else 1)
            else:
                is_proxy = -1
        except:
            country_short = _INVALID_IP_ADDRESS
            country_long = _INVALID_IP_ADDRESS
            region = _INVALID_IP_ADDRESS
            city = _INVALID_IP_ADDRESS
            isp = _INVALID_IP_ADDRESS
            proxy_type = _INVALID_IP_ADDRESS
            is_proxy = -1
            domain = _INVALID_IP_ADDRESS
            usage_type = _INVALID_IP_ADDRESS
            asn = _INVALID_IP_ADDRESS
            as_name = _INVALID_IP_ADDRESS
            last_seen = _INVALID_IP_ADDRESS
            threat = _INVALID_IP_ADDRESS
            provider = _INVALID_IP_ADDRESS
            fraud_score = _INVALID_IP_ADDRESS

        results = {}
        results['is_proxy'] = is_proxy
        results['proxy_type'] = proxy_type
        results['country_short'] = country_short
        results['country_long'] = country_long
        results['region'] = region
        results['city'] = city
        results['isp'] = isp
        results['domain'] = domain
        results['usage_type'] = usage_type
        results['asn'] = asn
        results['as_name'] = as_name
        results['last_seen'] = last_seen
        results['threat'] = threat
        results['provider'] = provider
        results['fraud_score'] = fraud_score
        return results

    def _reads(self, offset):
        self._f.seek(offset - 1)
        data = self._f.read(257)
        char_count = struct.unpack('B', data[0:1])[0]
        string = data[1:char_count+1]
        return u(string.decode('iso-8859-1').encode('utf-8'))

    def _readi(self, offset):
        self._f.seek(offset - 1)
        return struct.unpack('<I', self._f.read(4))[0]

    def _readip(self, offset, ipv):
        if ipv == 4:
            return self._readi(offset)
        elif ipv == 6:
            a, b, c, d = self._readi(offset), self._readi(offset + 4), self._readi(offset + 8), self._readi(offset + 12) 
            return (d << 96) | (c << 64) | (b << 32) | a

    def _readips(self, offset, ipv):
        if ipv == 4:
            return socket.inet_ntoa(struct.pack('!L', self._readi(offset)))
        elif ipv == 6:
            return str(self._readip(offset, ipv))

    def _read_record(self, mid, ipv):
        rec = IP2ProxyRecord()

        if ipv == 4:
            off = 0
            baseaddr = self._ipv4dbaddr
        elif ipv == 6:
            off = 12
            baseaddr = self._ipv6dbaddr

        rec.ip = self._readips(baseaddr + (mid) * self._dbcolumn * 4, ipv)

        def calc_off(what, mid):
            return baseaddr + mid * (self._dbcolumn * 4 + off) + off + 4 * (what[self._dbtype]-1)

        if _COUNTRY_POSITION[self._dbtype] != 0:
            rec.country_short = self._reads(self._readi(calc_off(_COUNTRY_POSITION, mid)) + 1)

            rec.country_long =  self._reads(self._readi(calc_off(_COUNTRY_POSITION, mid)) + 4)
        elif _COUNTRY_POSITION[self._dbtype] == 0:
            rec.country_short = _FIELD_NOT_SUPPORTED
            rec.country_long = _FIELD_NOT_SUPPORTED

        if _REGION_POSITION[self._dbtype] != 0:
            rec.region = self._reads(self._readi(calc_off(_REGION_POSITION, mid)) + 1)
        elif _REGION_POSITION[self._dbtype] == 0:
            rec.region = _FIELD_NOT_SUPPORTED

        if _CITY_POSITION[self._dbtype] != 0:
            rec.city = self._reads(self._readi(calc_off(_CITY_POSITION, mid)) + 1)
        elif _CITY_POSITION[self._dbtype] == 0:
            rec.city = _FIELD_NOT_SUPPORTED

        if _ISP_POSITION[self._dbtype] != 0:
            rec.isp = self._reads(self._readi(calc_off(_ISP_POSITION, mid)) + 1)
        elif _ISP_POSITION[self._dbtype] == 0:
            rec.isp = _FIELD_NOT_SUPPORTED

        if _PROXYTYPE_POSITION[self._dbtype] != 0:
            rec.proxy_type = self._reads(self._readi(calc_off(_PROXYTYPE_POSITION, mid)) + 1)
        elif _PROXYTYPE_POSITION[self._dbtype] == 0:
            rec.proxy_type = _FIELD_NOT_SUPPORTED

        if _DOMAIN_POSITION[self._dbtype] != 0:
            rec.domain = self._reads(self._readi(calc_off(_DOMAIN_POSITION, mid)) + 1)
        elif _DOMAIN_POSITION[self._dbtype] == 0:
            rec.domain = _FIELD_NOT_SUPPORTED

        if _USAGETYPE_POSITION[self._dbtype] != 0:
            rec.usage_type = self._reads(self._readi(calc_off(_USAGETYPE_POSITION, mid)) + 1)
        elif _USAGETYPE_POSITION[self._dbtype] == 0:
            rec.usage_type = _FIELD_NOT_SUPPORTED

        if _ASN_POSITION[self._dbtype] != 0:
            rec.asn = self._reads(self._readi(calc_off(_ASN_POSITION, mid)) + 1)
        elif _ASN_POSITION[self._dbtype] == 0:
            rec.asn = _FIELD_NOT_SUPPORTED

        if _AS_POSITION[self._dbtype] != 0:
            rec.as_name = self._reads(self._readi(calc_off(_AS_POSITION, mid)) + 1)
        elif _AS_POSITION[self._dbtype] == 0:
            rec.as_name = _FIELD_NOT_SUPPORTED

        if _LASTSEEN_POSITION[self._dbtype] != 0:
            rec.last_seen = self._reads(self._readi(calc_off(_LASTSEEN_POSITION, mid)) + 1)
        elif _LASTSEEN_POSITION[self._dbtype] == 0:
            rec.last_seen = _FIELD_NOT_SUPPORTED

        if _THREAT_POSITION[self._dbtype] != 0:
            rec.threat = self._reads(self._readi(calc_off(_THREAT_POSITION, mid)) + 1)
        elif _THREAT_POSITION[self._dbtype] == 0:
            rec.threat = _FIELD_NOT_SUPPORTED

        if _PROVIDER_POSITION[self._dbtype] != 0:
            rec.provider = self._reads(self._readi(calc_off(_PROVIDER_POSITION, mid)) + 1)
        elif _PROVIDER_POSITION[self._dbtype] == 0:
            rec.provider = _FIELD_NOT_SUPPORTED

        if _FRAUD_SCORE_POSITION[self._dbtype] != 0:
            rec.fraud_score = self._reads(self._readi(calc_off(_FRAUD_SCORE_POSITION, mid)) + 1)
        elif _FRAUD_SCORE_POSITION[self._dbtype] == 0:
            rec.fraud_score = _FIELD_NOT_SUPPORTED

        return rec

    def __iter__(self):
        low, high = 0, self._ipv4dbcount
        while low <= high:
            yield self._read_record(low, 4)
            low += 1

        low, high = 0, self._ipv6dbcount
        while low <= high:
            yield self._read_record(low, 6)
            low += 1

    def _validate_addr(self, addr):
        ''' Validate IP address '''
        try:
            # ip = ipaddress.ip_address(addr)
            ip = ipaddress.ip_address(u(addr))
            return True
        except ValueError:
            return False

    def _parse_addr(self, addr): 
        ''' Parses address and returns IP version. Raises exception on invalid argument '''
        ipv = 0
        ipnum = -1
        ipvalidateresult = self._validate_addr(addr)
        if (ipvalidateresult == False):
            return ipv, ipnum
        try:
            # socket.inet_pton(socket.AF_INET6, addr)
            a, b = struct.unpack('!QQ', socket.inet_pton(socket.AF_INET6, addr))
            ipnum = (a << 64) | b
            # Convert ::FFFF:x.y.z.y to IPv4
            if addr.lower().startswith('::ffff:'):
                try:
                    # ipnum = struct.unpack('!L', socket.inet_pton(socket.AF_INET, addr))[0]
                    socket.inet_pton(socket.AF_INET, addr)
                    ipv = 4
                except:
                    # reformat ipv4 address in ipv6 
                    if ((ipnum >= 281470681743360) and (ipnum <= 281474976710655)):
                        ipv = 4
                        ipnum = ipnum - 281470681743360
                    else:
                        ipv = 6
            else:
                # ipv = 6
                if ((ipnum >= 42545680458834377588178886921629466624) and (ipnum <= 42550872755692912415807417417958686719)):
                    ipv = 4
                    ipnum = ipnum >> 80
                    ipnum = ipnum % 4294967296
                elif ((ipnum >= 42540488161975842760550356425300246528) and (ipnum <= 42540488241204005274814694018844196863)):
                    ipv = 4
                    # ipnum = ipnum % 100000000000000000000000000000000
                    ipnum = ~ ipnum
                    ipnum = ipnum % 4294967296
                else:
                    ipv = 6
        except:
            ipnum = struct.unpack('!L', socket.inet_pton(socket.AF_INET, addr))[0]
            # socket.inet_pton(socket.AF_INET, addr)
            ipv = 4
        return ipv, ipnum

    def calc_off(self, off, baseaddr, what, mid):
        # return baseaddr + mid * (self._dbcolumn * 4 + off) + off + 4 * (what[self._dbtype]-1)
        return baseaddr + mid * (self._dbcolumn * 4 + off) + off + 4 * (what-1)

    def read32x2(self, offset):
        self._f.seek(offset - 1)
        data = self._f.read(8)
        return struct.unpack('<L', data[0:4])[0], struct.unpack('<L', data[4:8])[0]

    def readRow32(self, offset):
        data_length = self._dbcolumn * 4 + 4
        self._f.seek(offset - 1)
        raw_data = self._f.read(data_length)
        ip_from = struct.unpack('<L', raw_data[0:4])[0]
        ip_to = struct.unpack('<L', raw_data[data_length-4:data_length])[0]
        return (ip_from, ip_to)

    def readRow128(self, offset):
        data_length = self._dbcolumn * 4 + 12 + 16
        self._f.seek(offset - 1)
        raw_data = self._f.read(data_length)
        return ((struct.unpack('<L', raw_data[12:16])[0] << 96) | (struct.unpack('<L', raw_data[8:12])[0] << 64) | (struct.unpack('<L', raw_data[4:8])[0] << 32) | struct.unpack('<L', raw_data[0:4])[0], (struct.unpack('<L', raw_data[data_length-4:data_length])[0] << 96) | (struct.unpack('<L', raw_data[data_length-8:data_length-4])[0] << 64) | (struct.unpack('<L', raw_data[data_length-12:data_length-8])[0] << 32) | struct.unpack('<L', raw_data[data_length-16:data_length-12])[0])

    def _get_record(self, ip):
        low = 0
        ipv = self._parse_addr(ip)[0] 
        ipnum = self._parse_addr(ip)[1]
        # print (ipv)
        # print (ipnum)
        if (ipv == 0):
            rec = IP2ProxyRecord()
            rec.country_short = _INVALID_IP_ADDRESS
            rec.country_long = _INVALID_IP_ADDRESS
            rec.region = _INVALID_IP_ADDRESS
            rec.city = _INVALID_IP_ADDRESS
            rec.isp = _INVALID_IP_ADDRESS
            rec.proxy_type = _INVALID_IP_ADDRESS
            rec.domain = _INVALID_IP_ADDRESS
            rec.usage_type = _INVALID_IP_ADDRESS
            rec.asn = _INVALID_IP_ADDRESS
            rec.as_name = _INVALID_IP_ADDRESS
            rec.last_seen = _INVALID_IP_ADDRESS
            rec.threat = _INVALID_IP_ADDRESS
            rec.provider = _INVALID_IP_ADDRESS
            rec.fraud_score = _INVALID_IP_ADDRESS
            return rec
        elif ipv == 4:
            # ipnum = struct.unpack('!L', socket.inet_pton(socket.AF_INET, ip))[0]
            if (ipnum == MAX_IPV4_RANGE):
                ipno = ipnum - 1
            else:
                ipno = ipnum
            off = 0
            baseaddr = self._ipv4dbaddr
            high = self._ipv4dbcount
            if self._ipv4indexbaseaddr > 0:
                indexpos = ((ipno >> 16) << 3) + self._ipv4indexbaseaddr
                low,high = self.read32x2(indexpos)

        elif ipv == 6:
            # a, b = struct.unpack('!QQ', socket.inet_pton(socket.AF_INET6, ip))
            # ipnum = (a << 64) | b
            if (ipnum == MAX_IPV6_RANGE):
                ipno = ipnum - 1
            else:
                ipno = ipnum
            off = 12
            baseaddr = self._ipv6dbaddr
            high = self._ipv6dbcount
            if self._ipv6indexbaseaddr > 0:
                indexpos = ((ipno >> 112) << 3) + self._ipv6indexbaseaddr
                low,high = self.read32x2(indexpos)
                
        # elif (ipnum == '' or ipv == ):
        elif (ipnum == ''):
            rec = IP2ProxyRecord()
            rec.country_short = _NO_IP
            rec.country_long = _NO_IP
            rec.region = _NO_IP
            rec.city = _NO_IP
            rec.isp = _NO_IP
            rec.proxy_type = _NO_IP
            rec.domain = _NO_IP
            rec.usage_type = _NO_IP
            rec.asn = _NO_IP
            rec.as_name = _NO_IP
            rec.last_seen = _NO_IP
            rec.threat = _NO_IP
            rec.provider = _NO_IP
            rec.fraud_score = _NO_IP
            return rec
        else:
            rec = IP2ProxyRecord()
            rec.country_short = _INVALID_IP_ADDRESS
            rec.country_long = _INVALID_IP_ADDRESS
            rec.region = _INVALID_IP_ADDRESS
            rec.city = _INVALID_IP_ADDRESS
            rec.isp = _INVALID_IP_ADDRESS
            rec.proxy_type = _INVALID_IP_ADDRESS
            rec.domain = _INVALID_IP_ADDRESS
            rec.usage_type = _INVALID_IP_ADDRESS
            rec.asn = _INVALID_IP_ADDRESS
            rec.as_name = _INVALID_IP_ADDRESS
            rec.last_seen = _INVALID_IP_ADDRESS
            rec.threat = _INVALID_IP_ADDRESS
            rec.provider = _INVALID_IP_ADDRESS
            rec.fraud_score = _INVALID_IP_ADDRESS
            return rec

        while low <= high:
            # mid = int((low + high) / 2)
            mid = int((low + high) >> 1)
            if ipv == 4:
                ipfrom, ipto = self.readRow32(baseaddr + mid * self._dbcolumn * 4 )
            elif ipv == 6:
                ipfrom, ipto = self.readRow128(baseaddr + mid * ((self._dbcolumn * 4) + 12) )

            if ipfrom <= ipno < ipto:
                return self._read_record(mid, ipv)
            else:
                if ipno < ipfrom:
                    high = mid - 1
                else:
                    low = mid + 1

class IP2ProxyWebService(object):
    ''' IP2Proxy web service '''
    def __init__(self,apikey,package,usessl=True):
        if ((re.match(r"^[0-9A-Z]{10}$", apikey) == None) and (apikey != 'demo')):
            raise ValueError("Please provide a valid IP2Proxy web service API key.")
        if (re.match(r"^PX[0-9]+$", package) == None):
            package = 'PX1'
        self.apikey = apikey
        self.package = package
        self.usessl = usessl

    def lookup(self,ip):
        '''This function will look the given IP address up in IP2Proxy web service.'''
        parameters = urlencode((("ip", ip), ("key", self.apikey), ("package", self.package)))
        response = httprequest(parameters, self.usessl)
        if (response == None):
            return False
        if (('response' in response) and (response['response'] != "OK")):
            raise IP2ProxyAPIError(response['response'])
        return response

    def getcredit(self):
        '''Get the remaing credit in your IP2Proxy web service account.'''
        parameters = urlencode((("key", self.apikey), ("check", True)))
        response = httprequest(parameters, self.usessl)
        if (response == None):
            return 0
        if ('response' in response is False):
            return 0
        return response['response']

class IP2ProxyAPIError(Exception):
    """Raise for IP2Proxy API Error Message"""
