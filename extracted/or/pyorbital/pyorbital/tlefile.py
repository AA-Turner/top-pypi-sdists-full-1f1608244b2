#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2011-2024 Pytroll Community
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Classes and functions for handling TLE files."""
import contextlib
import datetime as dt
import glob
import io
import logging
import os
import sqlite3
from itertools import zip_longest
from urllib.request import urlopen

import defusedxml.ElementTree as ET
import numpy as np
import requests

TLE_GROUPS = ("active",
              "weather",
              "resource",
              "cubesat",
              "stations",
              "sarsat",
              "noaa",
              "amateur",
              "engineering")

TLE_URLS = [f"https://celestrak.org/NORAD/elements/gp.php?GROUP={group}&FORMAT=tle"
            for group in TLE_GROUPS]


LOGGER = logging.getLogger(__name__)
PKG_CONFIG_DIR = os.path.join(os.path.realpath(os.path.dirname(__file__)), "etc")

class TleDownloadTimeoutError(Exception):
    """TLE download timeout exception."""


def _get_config_path():
    """Get the config path for Pyorbital."""
    if "PPP_CONFIG_DIR" in os.environ and "PYORBITAL_CONFIG_PATH" not in os.environ:
        LOGGER.warning(
            "The use of PPP_CONFIG_DIR is no longer supported!" +
            " Please use PYORBITAL_CONFIG_PATH if you need a custom config path for pyorbital!")
        LOGGER.debug("Using the package default for configuration: %s", PKG_CONFIG_DIR)
        return PKG_CONFIG_DIR
    else:
        pyorbital_config_path = os.getenv("PYORBITAL_CONFIG_PATH", PKG_CONFIG_DIR)

    LOGGER.debug("Path to the Pyorbital configuration (where e.g. platforms.txt is found): %s",
                 str(pyorbital_config_path))
    return pyorbital_config_path


def get_platforms_filepath():
    """Get the platforms.txt file path.

    Check that the file exists or raise an error.
    """
    config_path = _get_config_path()
    platform_file = os.path.join(config_path, "platforms.txt")
    if not os.path.isfile(platform_file):
        platform_file = os.path.join(PKG_CONFIG_DIR, "platforms.txt")
        if not os.path.isfile(platform_file):
            raise OSError("Platform file {filepath} does not exist!".format(filepath=platform_file))

    return platform_file


def read_platform_numbers(filename, in_upper=False, num_as_int=False):
    """Read platform numbers from $PYORBITAL_CONFIG_PATH/platforms.txt."""
    out_dict = {}

    with open(filename, "r") as fid:
        for row in fid:
            # skip comment lines
            if not row.startswith("#"):
                parts = row.split()
                if len(parts) < 2:
                    continue
                # The satellite name might have whitespace
                platform = " ".join(parts[:-1])
                num = parts[-1]
                if in_upper:
                    platform = platform.upper()
                if num_as_int:
                    num = int(num)
                out_dict[platform] = num

    return out_dict


SATELLITES = read_platform_numbers(get_platforms_filepath(),
                                   in_upper=True, num_as_int=False)
"""
The platform numbers are given in a file $PYORBITAL_CONFIG_PATH/platforms.txt
in the following format:

.. literalinclude:: ../../pyorbital/etc/platforms.txt
  :language: text
  :lines: 5-
"""


def check_is_platform_supported(satname):
    """Check if satellite is supported and print info."""
    if satname in SATELLITES:
        LOGGER.info("Satellite {name} is supported. NORAD number: {norad}".format(
            name=satname, norad=SATELLITES[satname]))
    else:
        LOGGER.info("Satellite {name} is NOT supported.".format(name=satname))
        LOGGER.info("Please add it to a local copy of the platforms.txt file and put in " +
                    "the directory pointed to by the environment variable PYORBITAL_CONFIG_PATH")

    LOGGER.info("Satellite names and NORAD numbers are defined in {filepath}".format(
        filepath=get_platforms_filepath()))


def _dummy_open_stringio(stream):
    return stream


def read(platform, tle_file=None, line1=None, line2=None):
    """Read TLE for *platform*.

    The data are read from *tle_file*, from *line1* and *line2*, from
    the newest file provided in the TLES pattern, or from internet if
    none is provided.

    """
    return Tle(platform, tle_file=tle_file, line1=line1, line2=line2)


def fetch(destination):
    """Fetch TLE from internet and save it to `destination`."""
    with io.open(destination, mode="w", encoding="utf-8") as dest:
        for url in TLE_URLS:
            if not url.lower().startswith("http"):
                raise ValueError(f"{str(url)} is not accepted!")
            response = urlopen(url)  # nosec
            dest.write(response.read().decode("utf-8"))


class ChecksumError(Exception):
    """ChecksumError."""


class Tle(object):
    """Class holding TLE objects."""

    def __init__(self, platform, tle_file=None, line1=None, line2=None):
        """Init."""
        self._platform = platform.strip().upper()
        self._tle_file = tle_file
        self._line1 = line1
        self._line2 = line2

        self.satnumber = None
        self.classification = None
        self.id_launch_year = None
        self.id_launch_number = None
        self.id_launch_piece = None
        self.epoch_year = None
        self.epoch_day = None
        self.epoch = None
        self.mean_motion_derivative = None
        self.mean_motion_sec_derivative = None
        self.bstar = None
        self.ephemeris_type = None
        self.element_number = None
        self.inclination = None
        self.right_ascension = None
        self.excentricity = None
        self.arg_perigee = None
        self.mean_anomaly = None
        self.mean_motion = None
        self.orbit = None

        self._read_tle()
        self._checksum()
        self._parse_tle()

    @property
    def line1(self):
        """Return first TLE line."""
        return self._line1

    @property
    def line2(self):
        """Return second TLE line."""
        return self._line2

    @property
    def platform(self):
        """Return satellite platform name."""
        return self._platform

    def _checksum(self):
        """Calculate checksum for the current TLE."""
        for line in [self._line1, self._line2]:
            check = 0
            for char in line[:-1]:
                if char.isdigit():
                    check += int(char)
                if char == "-":
                    check += 1

            if (check % 10) != int(line[-1]):
                raise ChecksumError(self._platform + " " + line)

    def _read_tle(self):
        """Read TLE data."""
        if self._line1 is not None and self._line2 is not None:
            tle = self._line1.strip() + "\n" + self._line2.strip()
        else:
            uris, open_func = _get_uris_and_open_func(tle_file=self._tle_file)
            tle = _get_first_tle(uris, open_func, platform=self._platform)

            if not tle:
                raise KeyError("Found no TLE entry for '%s'" % self._platform)

        self._line1, self._line2 = tle.split("\n")

    def _parse_tle(self):
        """Parse values from TLE data."""
        def _read_tle_decimal(rep):
            """Convert *rep* to decimal value."""
            if rep[0] in ["-", " ", "+"]:
                digits = rep[1:-2].strip()
                val = rep[0] + "." + digits + "e" + rep[-2:]
            else:
                digits = rep[:-2].strip()
                val = "." + digits + "e" + rep[-2:]

            return float(val)

        self.satnumber = self._line1[2:7]
        self.classification = self._line1[7]
        self.id_launch_year = self._line1[9:11]
        self.id_launch_number = self._line1[11:14]
        self.id_launch_piece = self._line1[14:17]
        self.epoch_year = self._line1[18:20]
        self.epoch_day = float(self._line1[20:32])
        self.epoch = \
            np.datetime64(dt.datetime.strptime(self.epoch_year, "%y") +
                          dt.timedelta(days=self.epoch_day - 1), "us")
        self.mean_motion_derivative = float(self._line1[33:43])
        self.mean_motion_sec_derivative = _read_tle_decimal(self._line1[44:52])
        self.bstar = _read_tle_decimal(self._line1[53:61])
        try:
            self.ephemeris_type = int(self._line1[62])
        except ValueError:
            self.ephemeris_type = 0
        self.element_number = int(self._line1[64:68])

        self.inclination = float(self._line2[8:16])
        self.right_ascension = float(self._line2[17:25])
        self.excentricity = int(self._line2[26:33]) * 10 ** -7
        self.arg_perigee = float(self._line2[34:42])
        self.mean_anomaly = float(self._line2[43:51])
        self.mean_motion = float(self._line2[52:63])
        self.orbit = int(self._line2[63:68])

    def __str__(self):
        """Format the class data for printing."""
        import pprint
        s_var = io.StringIO()
        d_var = dict(([(k, v) for k, v in
                       list(self.__dict__.items()) if k[0] != "_"]))
        pprint.pprint(d_var, s_var)
        return s_var.getvalue()[:-1]


def _get_local_tle_path_from_env():
    """Get the path to possible local TLE files using the environment variable."""
    return os.environ.get("TLES")


def _get_uris_and_open_func(tle_file=None):
    """Get the uri's and the adequate file open call for the TLE files."""
    def _open(filename):
        return io.open(filename, "rb")

    local_tle_path = _get_local_tle_path_from_env()

    if tle_file:
        if isinstance(tle_file, io.StringIO):
            uris = (tle_file,)
            open_func = _dummy_open_stringio
        elif "ADMIN_MESSAGE" in tle_file:
            uris = (io.StringIO(read_tle_from_mmam_xml_file(tle_file)),)
            open_func = _dummy_open_stringio
        else:
            uris = (tle_file,)
            open_func = _open
    elif local_tle_path:
        # TODO: get the TLE file closest in time to the actual satellite
        # overpass, NOT the latest!
        list_of_tle_files = glob.glob(local_tle_path)
        uris = (max(list_of_tle_files, key=os.path.getctime), )
        LOGGER.debug("Reading TLE from %s", uris[0])
        open_func = _open
    else:
        LOGGER.debug("Fetch TLE from the internet.")
        uris = TLE_URLS
        open_func = urlopen

    return uris, open_func


def _get_first_tle(uris, open_func, platform=""):
    return _get_tles_from_uris(uris, open_func, platform=platform, only_first=True)


def _get_tles_from_uris(uris, open_func, platform="", only_first=True):
    tles = []
    for url in uris:
        tles += _get_tles_from_url(url, open_func, platform, only_first)
    if only_first:
        if tles:
            return tles[0]
        return ""
    return tles


@contextlib.contextmanager
def _uri_open(uri, open_func):
    file_obj = open_func(uri)
    try:
        yield file_obj
    finally:
        if hasattr(file_obj, "close"):
            file_obj.close()


def _get_tles_from_url(url, open_func, platform, only_first):
    with _uri_open(url, open_func) as fid:
        open_is_dummy = open_func == _dummy_open_stringio
        tles = []
        for l_0 in fid:
            tle = _decode_lines(fid, l_0, platform, only_first, open_is_dummy=open_is_dummy)
            if tle:
                if only_first:
                    return [tle]
                tles.append(tle)
        return tles


def _decode(itm):
    if isinstance(itm, str):
        return itm
    return itm.decode("utf-8")


def _decode_lines(fid, l_0, platform, only_first, open_is_dummy=False):
    designator = "1 " + SATELLITES.get(platform, "")
    tle = ""
    l_0 = _decode(l_0)
    if l_0.strip() == platform:
        l_1 = _decode(next(fid))
        l_2 = _decode(next(fid))
        tle = _merge_tle_from_two_lines(l_1, l_2)
    elif l_0.strip().startswith(designator):
        if (platform in SATELLITES or not only_first) or open_is_dummy:
            l_1 = l_0
            l_2 = _decode(next(fid))
            tle = _merge_tle_from_two_lines(l_1, l_2)
            if platform:
                LOGGER.debug("Found platform %s, ID: %s", platform, SATELLITES[platform])
    elif l_0.startswith(platform) and platform not in SATELLITES:
        LOGGER.debug("Found a possible match: %s?", str(l_0.strip()))

    return tle


def _merge_tle_from_two_lines(l_1, l_2):
    """Merge line1 and line2 to fulle TLE string."""
    return l_1.strip() + "\n" + l_2.strip()


PLATFORM_NAMES_TABLE = "(satid text primary key, platform_name text)"
SATID_TABLE = ("'{}' (epoch date primary key, tle text, insertion_time date,"
               " source text)")
SATID_VALUES = "INSERT INTO '{}' VALUES (?, ?, ?, ?)"
PLATFORM_VALUES = "INSERT INTO platform_names VALUES (?, ?)"
ISO_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class Downloader(object):
    """Class for downloading TLE data."""

    def __init__(self, config):
        """Init."""
        self.config = config

    def fetch_plain_tle(self):
        """Fetch plain text-formated TLE data."""
        tles = {}
        if "fetch_plain_tle" in self.config["downloaders"]:
            sources = self.config["downloaders"]["fetch_plain_tle"]
            for source in sources:
                tles[source] = []
                failures = []
                for uri in sources[source]:
                    try:
                        req = requests.get(uri, timeout=15)  # 15 seconds
                    except requests.exceptions.Timeout:
                        raise TleDownloadTimeoutError(f"Failed to make request to {str(uri)} within 15 seconds!")
                    if req.status_code == 200:
                        tles[source] += _parse_tles_for_downloader((req.text,), io.StringIO)
                    else:
                        failures.append(uri)
                if len(failures) > 0:
                    logging.error(
                        "Could not fetch TLEs from %s, %d failure(s): [%s]",
                        source, len(failures), ", ".join(failures))
                logging.info("Downloaded %d TLEs from %s",
                             len(tles[source]), source)
        return tles

    def fetch_spacetrack(self):
        """Fetch TLE data from Space-Track."""
        tles = []
        login_url = "https://www.space-track.org/ajaxauth/login"
        download_url = ("https://www.space-track.org/basicspacedata/query/"
                        "class/tle_latest/ORDINAL/1/NORAD_CAT_ID/%s/format/"
                        "tle")
        download_url = download_url % ",".join(
            [str(key) for key in self.config["platforms"]])

        user = self.config["downloaders"]["fetch_spacetrack"]["user"]
        password = self.config["downloaders"]["fetch_spacetrack"]["password"]
        credentials = {"identity": user, "password": password}

        with requests.Session() as session:
            # Login
            req = session.post(login_url, data=credentials)

            if req.status_code != 200:
                logging.error("Could not login to Space-Track")
                return tles

            # Get the data
            req = session.get(download_url)

            if req.status_code == 200:
                tles = _parse_tles_for_downloader((req.text,), io.StringIO)
            else:
                logging.error("Could not retrieve TLEs from Space-Track")

        logging.info("Downloaded %d TLEs from %s", len(tles), "spacetrack")

        return tles

    def read_tle_files(self):
        """Read TLE data from files."""
        paths = self.config["downloaders"]["read_tle_files"]["paths"]

        # Collect filenames
        fnames = collect_filenames(paths)
        tles = _parse_tles_for_downloader(fnames, open)
        logging.info("Loaded %d TLEs from local files", len(tles))

        return tles

    def read_xml_admin_messages(self):
        """Read Eumetsat admin messages in XML format."""
        paths = self.config["downloaders"]["read_xml_admin_messages"]["paths"]
        tles = read_tles_from_mmam_xml_files(paths)
        logging.info("Loaded %d TLEs from admin message XML files", len(tles))

        return tles


def _parse_tles_for_downloader(item, open_func):
    return [Tle("", tle_file=io.StringIO(tle)) for tle in
            _get_tles_from_uris(item, open_func, platform="", only_first=False)]


def collect_filenames(paths):
    """Collect all filenames from *paths*."""
    fnames = []
    for path in paths:
        if "*" in path:
            fnames += glob.glob(path)
        else:
            if not os.path.exists(path):
                logging.error("File %s doesn't exist.", path)
                continue
            fnames += [path]
    return fnames


def read_tles_from_mmam_xml_files(paths):
    """Read TLE data from a list of MMAM XMl file (EUMETSAT).

    MMAM = Multi-Mission Administration Message
    """
    fnames = collect_filenames(paths)
    tles = []
    for fname in fnames:
        data = read_tle_from_mmam_xml_file(fname).split("\n")
        for two_lines in _group_iterable_to_chunks(2, data):
            tl_stream = io.StringIO("\n".join(two_lines))
            tles.append(Tle("", tle_file=tl_stream))
    return tles


def read_tle_from_mmam_xml_file(fname):
    """Read TLE data from MMAM XMl file (EUMETSAT)."""
    tree = ET.parse(fname)
    root = tree.getroot()
    data = []
    for nav in root.findall(".//navigation"):
        data.append(nav.find(".//line-1").text)
        data.append(nav.find(".//line-2").text)

    return "\n".join(data)


def _group_iterable_to_chunks(n, iterable, fillvalue=None):
    """Collect data into fixed-length chunks or blocks."""
    # _group_iterable_to_chunks(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


class SQLiteTLE(object):
    """Store TLE data in a sqlite3 database."""

    def __init__(self, db_location, platforms, writer_config):
        """Init."""
        self.db = sqlite3.connect(db_location)
        self.platforms = platforms
        self.writer_config = writer_config
        self.updated = False

        # Create platform_names table if it doesn't exist
        if not table_exists(self.db, "platform_names"):
            cmd = "CREATE TABLE platform_names " + PLATFORM_NAMES_TABLE
            with self.db:
                self.db.execute(cmd)
                logging.info("Created database table 'platform_names'")

    def update_db(self, tle, source):
        """Update the collected data.

        Only data with newer epoch than the existing one is used.

        """
        num = int(tle.satnumber)
        if num not in self.platforms:
            return
        tle.platform_name = self.platforms[num]
        if not table_exists(self.db, num):
            cmd = "CREATE TABLE " + SATID_TABLE.format(num)
            with self.db:
                self.db.execute(cmd)
                logging.info("Created database table '%d'", num)
            cmd = ""
            with self.db:
                self.db.execute(PLATFORM_VALUES, (num, self.platforms[num]))
                logging.info("Added platform name '%s' for ID '%d'",
                             self.platforms[num], num)
        cmd = SATID_VALUES.format(num)
        epoch = tle.epoch.item().isoformat()
        tle = "\n".join([tle.line1, tle.line2])
        now = _utcnow().isoformat()
        try:
            with self.db:
                self.db.execute(cmd, (epoch, tle, now, source))
                logging.info("Added TLE for %d (%s), epoch: %s, source: %s",
                             num, self.platforms[num], epoch, source)
                self.updated = True
        except sqlite3.IntegrityError:
            pass

    def write_tle_txt(self):
        """Write TLE data to a text file."""
        if not self.updated and not self.writer_config.get("write_always",
                                                           False):
            return
        pattern = os.path.join(self.writer_config["output_dir"],
                               self.writer_config["filename_pattern"])
        now = _utcnow()
        fname = now.strftime(pattern)
        out_dir = os.path.dirname(fname)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
            logging.info("Created directory %s", out_dir)
        data = []

        for satid, platform_name in self.platforms.items():
            if self.writer_config.get("write_name", False):
                data.append(platform_name)
            query = f"SELECT epoch, tle FROM '{satid:d}' ORDER BY epoch DESC LIMIT 1"  # nosec
            epoch, tle = self.db.execute(query).fetchone()  # nosec
            date_epoch = dt.datetime.strptime(epoch, ISO_TIME_FORMAT)
            tle_age = (_utcnow() - date_epoch).total_seconds() / 3600.
            logging.info("Latest TLE for '%s' (%s) is %d hours old.",
                         satid, platform_name, int(tle_age))
            data.append(tle)

        with open(fname, "w") as fid:
            fid.write("\n".join(data))

        logging.info("Wrote %d TLEs to %s", len(data), fname)

    def close(self):
        """Close the database."""
        self.db.close()


def table_exists(db, name):
    """Check if the table 'name' exists in the database."""
    name = str(name)
    query = "SELECT 1 FROM sqlite_master WHERE type='table' and name=?"
    return db.execute(query, (name,)).fetchone() is not None  # nosec


def _utcnow():
    return dt.datetime.now(tz=dt.timezone.utc).replace(tzinfo=None)

def main():
    """Run a test TLE reading."""
    tle_data = read("Noaa-19")
    print(tle_data)


if __name__ == "__main__":
    main()
