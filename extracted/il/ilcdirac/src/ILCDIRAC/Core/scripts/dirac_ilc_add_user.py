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
"""Register a user in ILCDIRAC.

.. warning :: This script is disfavoured in view of the
      :class:`~DIRAC.ConfigurationSystem.Agent.VOMS2CSAgent.VOMS2CSAgent`

Register the user in the CS, the FileCatalog, and in the e-group.

For that last functionality to be work, you need to have the sections /Security/egroupAdmin and /Security/egroupPass
options in a dirac.cfg. Ideally, the local dirac.cfg (~/.dirac.cfg) can be used. It's also possible to pass the value
with ``-o /Security/egroupAdmin=something -o /Security/egroupPass=something``.

To figure out the commands available from WSDL::

  print client
"""

from __future__ import print_function
from __future__ import absolute_import
__RCSID__ = "$Id$"

try:
  import suds
  from suds.client import Client
except ImportError:
  print("suds module missing: Install it with [sudo] easy_install suds")
  raise

from DIRAC.Core.Base.Script import Script
from DIRAC import gLogger, gConfig, exit as dexit

from DIRAC import S_OK, S_ERROR


class _Params(object):
  """Parameter Object."""

  def __init__(self):
    self.uname = ''
    self.groups = []
    self.certDN = ''
    self.certCN = ''
    self.email = ''
    self.cernid = ''
    self.external = False

  def setUName(self, opt):
    self.uname = opt
    return S_OK()

  def setGroup(self, opt):
    self.groups = opt.split(",")
    return S_OK()

  def setDN(self, opt):
    self.certDN = opt
    return S_OK()

  def setCN(self, opt):
    self.certCN = opt
    return S_OK()

  def setEmail(self, opt):
    if not opt.find('@') > 0:
      return S_ERROR('Not a valid mail address')
    self.email = opt
    return S_OK()

  def setCERNID(self, opt):
    self.cernid = opt
    return S_OK()

  def setExternal(self, dummy_opt):
    self.external = True
    return S_OK()

  def registerSwitches(self):
    Script.registerSwitch("U:", "UserName=", "DIRAC user name", self.setUName)
    Script.registerSwitch("G:", "Groups=", "DIRAC groups in which to add the new user, comma separated", self.setGroup)
    Script.registerSwitch("D:", "DN=", "user DN", self.setDN)
    Script.registerSwitch("C:", "CN=", "user CN (or CA)", self.setCN)
    Script.registerSwitch("E:", "Email=", "User mail", self.setEmail)
    Script.registerSwitch("", "CCID=", "CERN CC user ID (if any)", self.setCERNID)
    Script.registerSwitch("X", "external", "set if user is external, no checking of the PhoneBook", self.setExternal)
    Script.setUsageMessage(
        """%s -U <username> -G <ilc_user,private_pilot,...> -D"<DN>" -C"<CN>" -E <email>""" %
        Script.scriptName)


def addUserToCS(clip, userProps):
  """Add the user to the CS, return list of errors."""
  from DIRAC.Interfaces.API.DiracAdmin import DiracAdmin
  diracAdmin = DiracAdmin()
  exitCode = 0
  errorList = []

  if not diracAdmin.csModifyUser(clip.uname, userProps, createIfNonExistant=True)['OK']:
    errorList.append(("add user", "Cannot register user: '%s'" % clip.uname))
    exitCode = 255
  else:
    result = diracAdmin.csCommitChanges()
    if not result['OK']:
      errorList.append(("commit", result['Message']))
      exitCode = 255
  for error in errorList:
    gLogger.error("%s: %s" % error)
  if exitCode:
    dexit(exitCode)


def addUserToFC(clip):
  """Add the user to the filecatalog Try to figure out in which VOs the user must be, and create the catalog entries accordingly."""
  from DIRAC.ConfigurationSystem.Client.Helpers import Registry
  from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient
  from DIRAC.ConfigurationSystem.Client.Helpers.Operations import Operations
  fc = FileCatalogClient()
  res = fc.addUser(clip.uname)
  if not res['OK']:
    gLogger.error("Failed to add user to FC, but it does not really matter:", res['Message'])
    gLogger.error("Add by hand (in the FC-CLI: user add %s)" % (clip.uname))

  bpath = ''
  for grp in clip.groups:
    bpath = '/'
    voName = Registry.getVOForGroup(grp)
    if not voName:
      gLogger.error("NO VO for group", grp)
      continue
    bpath += voName + "/"
    lfnprefix = Operations(vo=voName).getValue("LFNUserPrefix")
    if lfnprefix:
      bpath += lfnprefix + "/"
    bpath += clip.uname[0] + "/" + clip.uname

    res = fc.createDirectory(bpath)
    if not res['OK']:
      gLogger.error(res['Message'])
      continue

    res = fc.changePathGroup({bpath: grp}, False)
    if not res['OK']:
      gLogger.error(res['Message'])

    res = fc.changePathOwner({bpath: clip.uname}, False)
    if not res['OK']:
      gLogger.error(res['Message'])

    res = fc.setMetadata(bpath, {"Owner": clip.uname})
    if not res['OK']:
      gLogger.error(res['Message'])


def addUserToEgroup(clip):
  """Add user to e-group."""
  login = gConfig.getValue("/Security/egroupAdmin", "").strip('"')
  pwd = gConfig.getValue("/Security/egroupPass", "").strip('"')
  url = 'https://foundservices.cern.ch/ws/egroups/v1/EgroupsWebService/EgroupsWebService.wsdl'
  if not (login and pwd):
    gLogger.warn("Missing configuration parameters: username or password for WSDL interactions")
    gLogger.warn("Add options: -o /Security/egroupAdmin=<cernusername> -o /Security/egroupPass=<password>")
    gLogger.error("User registration in e-group must be done manually")
    return
  try:
    client = Client(url=url, username=login, password=pwd)
    # gLogger.notice(client)
  except suds.transport.TransportError as exc:
    gLogger.error("Failed to get the WSDL client:%s" % exc)
    gLogger.error("User registration in e-group must be done manually")
    return
  except BaseException:
    gLogger.error("Something unexpected happened with the suds client, aborting")
    return

  if clip.external:
    sudsUser = client.factory.create("ns0:MemberType")
    sudsUser['Type'] = 'External'
    sudsUser['Email'] = clip.email
    userl = [sudsUser]
  else:
    user = getUserInfoFromPhonebook(client, clip)
    userl = [user]
  res = client.service.AddEgroupMembers('ilc-dirac', False, userl)
  if hasattr(res, 'warnings'):
    gLogger.notice(res.warnings)


def getUserInfoFromPhonebook(client, clip):
  """return user information from the phonebook."""
  sudsUser = client.factory.create("ns0:MemberType")
  comm = "phonebook --login %s --terse firstname --terse surname --terse ccid --terse email" % clip.uname
  from DIRAC.Core.Utilities.Subprocess import shellCall
  res = shellCall(0, comm)
  if not res['OK']:
    gLogger.error("Failed getting user info:", res['Message'])
    gLogger.error("Please add user in e-group by hand.")
    dexit(1)
  if res['Value'][0]:
    gLogger.error("phonebook command returned an error:", res['Value'][2])
    gLogger.error("Please add user in e-group by hand.")
    dexit(1)
  output = res['Value'][1]
  if output:
    output = output.split("\n")
    if len(output) > 2:
      gLogger.error("This username somehow has more than one account, please choose the right one and register by hand")
      gLogger.error("%s" % output)
      dexit(1)
    user_fname = output[0].split(";")[0]  # firstname
    user_sname = output[0].split(";")[1]  # surname
    phoneBookEmail = output[0].split(";")[3]  # email
    if phoneBookEmail != clip.email and clip.email:
      gLogger.error("Email for user (%s) does not match the email given in the command line (%s))"
                     % (phoneBookEmail, clip.email))
      dexit(1)
    else:
      clip.email = phoneBookEmail
    sudsUser['PrimaryAccount'] = clip.uname.upper()
    sudsUser['ID'] = output[0].split(";")[2]  # CCID
    sudsUser['Type'] = 'Person'
    sudsUser['Name'] = '%s, %s' % (user_sname.upper(), user_fname)
    sudsUser['Email'] = output[0].split(";")[3]  # email
  else:
    gLogger.notice("User '%s' does not appear to be in the CERN phonebook" % clip.uname)
    if not clip.email:
      gLogger.error("Email address for external user is not given, please add -E<address>")
      dexit(1)

    sudsUser['Type'] = 'External'
    sudsUser['Email'] = clip.email

  return sudsUser


@Script()
def main():
  """Add user to configuration service and other things."""
  clip = _Params()
  clip.registerSwitches()
  Script.parseCommandLine()
  if not (clip.certCN and clip.groups and clip.certDN and clip.uname):
    gLogger.error("Username, DN, CN, and groups have to be given")
    Script.showHelp()
  gLogger.notice("Add User to Egroup")
  addUserToEgroup(clip)
  if not clip.email:
    gLogger.fatal("No email defined and not found in phonebook, you have to provide it: -E<email>")
    dexit(1)
  userProps = {'DN': clip.certDN, 'Email': clip.email, 'CN': clip.certCN, 'Groups': clip.groups}
  gLogger.notice("Add User to CS")
  addUserToCS(clip, userProps)
  gLogger.notice("Add User to FC")
  addUserToFC(clip)
  gLogger.notice("Done")


if __name__ == "__main__":
  main()
  dexit(0)
