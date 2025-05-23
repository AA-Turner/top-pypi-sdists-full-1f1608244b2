#
# Copyright (c) 2009-2022 CERN. All rights nots expressly granted are
# reserved.
#
# This file is part of iLCDirac
# (see ilcdirac.cern.ch, contact: ilcdirac-support@cern.ch).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# In applying this licence, CERN does not waive the privileges and
# immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
"""Remove any system library provided in the application tar ball.

:author: sposs
:since: Jan 26, 2011
"""

from __future__ import print_function
from __future__ import absolute_import
__RCSID__ = "$Id$"

import os
from DIRAC import gLogger
LOG = gLogger.getSubLogger(__name__)
FILES_TO_REMOVE = ["libc.so", "libc-2.5", "libm.so", "libpthread.so", "libdl.so", "libstdc++.so", "libgcc_s.so.1"]


def removeLibc(libraryPath):
  """Remove libraries that can be problematic, like libc.so.

  :param str libraryPath: libraryPath to look for libraries to remove
  :returns: True on Success, False in case of error
  """

  LOG.debug("RemoveLibC: Trying to remove these libraries:")
  LOG.debug("RemoveLibC - " + "\nRemoveLibC - ".join(FILES_TO_REMOVE))

  curdir = os.getcwd()
  try:
    os.chdir(libraryPath)
  except OSError:
    return True
  listlibs = os.listdir(os.getcwd())
  for lib in listlibs:
    for lib_to_remove in FILES_TO_REMOVE:
      if lib.count(lib_to_remove):
        try:
          libraryPath = os.getcwd() + os.sep + lib
          LOG.info("RemoveLibC: Trying to remove: %s" % libraryPath)
          os.remove(libraryPath)
        except OSError:
          LOG.error("RemoveLibC: Could not remove", lib)
          os.chdir(curdir)
          return False
  os.chdir(curdir)
  return True


def getLibsToIgnore():
  """ :returns: static list of system libraries """
  return FILES_TO_REMOVE


def main():
  """Main method, executed when this file is executed as a python script."""
  import sys
  if not len(sys.argv) > 1:
    LOG.error("You need to pass the path")
    return 1
  PATH = sys.argv[1]
  LOG.notice("Will remove from %s the files that look like %s" % (PATH, getLibsToIgnore()))

  if not removeLibc(PATH):
    LOG.error("Could not clean libs")
    return 1
  return 0


if __name__ == "__main__":
  exit(main())
