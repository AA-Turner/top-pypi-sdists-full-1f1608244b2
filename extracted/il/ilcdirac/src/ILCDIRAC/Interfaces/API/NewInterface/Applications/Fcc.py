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
"""FCC application is defined by 2 modules which are :

- ILCDIRAC.Interfaces.API.NewInterface.Applications.Fcc (this module)
- ILCDIRAC.Workflow.Modules.FccAnalysis

FCC applications can run under a UserJob located here:

- ILCDIRAC.Interfaces.API.NewInterface.UserJob
"""

# standard libraries
from __future__ import absolute_import
import os
import re
import shutil

# DIRAC libraries
from ILCDIRAC.Interfaces.API.NewInterface.Application import Application
from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.Core.Workflow.Parameter import Parameter

LOG = gLogger.getSubLogger(__name__)
__RCSID__ = "$Id$"


class Fcc(Application):
  """Fcc class defines the skeleton of an FCC application.

  It inherits from the Application module.

  Fcc application is the base class for :
  -   FccSw
  -   FccAnalysis

  Look their definition at the end of this module.
  """

  def __init__(self):

    # Required
    self.fccExecutable = ''

    # Path of the FCCSW installation (Local or in CVMFS)
    self.fccSwPath = ''

    # FccSw generates an additionnal configuration file
    self.isGaudiOptionsFileNeeded = False

    # Read or generate events
    self.read = False

    # Random generator service used to set the seed and the number of events
    self.randomGenerator = {}

    # Final FCC input sandbox
    self._inputSandbox = set()

    # Temporary FCC input sandbox
    # contains user files/folders not yet checked
    self._tempInputSandbox = set()

    # Some folders have to be filtered (like 'Detector' folder of FCCSW installation)
    # to avoid sandbox overload (sandbox max size = 10 Mb)
    self._foldersToFilter = []

    # Folder filters
    # which extension to filter
    self._filteredExtensions = []

    # What operation to do for each extension (include it or exclude it)
    self._excludesOrIncludes = []

    # Local path of the temporary sandbox
    self._tempCwd = os.path.realpath('temp_fcc_dirac')

    # Output sandbox (not the real one)
    # used just for printing informations to the user
    self._outputSandbox = set()

    # Default application log level
    self.logLevel = "DEBUG"

    self.datatype = 'REC'
    self.detectortype = 'ILD'

    super(Fcc, self).__init__()
    # Those 6 need to come after default constructor
    self._modulename = 'FccAnalysis'
    #self._importLocation = 'ILCDIRAC.Workflow.Modules'
    self._moduledescription = "Module running FCC software"
    self.appname = self.__class__.__name__
    self.version = "v0.8.1"
    self.energy = 0
    self.numberOfEvents = 0

  def _applicationModule(self):
    """It transfers parameter names from the module Fcc to the module FccAnalysis.

    :return: The module that takes these parameters
    :rtype: moduleinstance
    """

    md1 = self._createModuleDefinition()

    md1.addParameter(Parameter("fccExecutable", "", "string", "", "", False, False,
                               "The executable to run"))

    md1.addParameter(Parameter("isGaudiOptionsFileNeeded", False, "bool", "", "", False, False,
                               "Gaudi configuration file"))

    md1.addParameter(Parameter("logLevel", "", "string", "", "", False, False,
                               "Gaudi Log Level"))

    md1.addParameter(Parameter("read", "", "string", "", "", False, False,
                               "Application can read or generate events"))

    md1.addParameter(Parameter("randomGenerator", {}, "dict", "", "", False, False,
                               "Pythia card files"))

    return md1

  def _applicationModuleValues(self, moduleinstance):
    """It transfers parameter values from the module Fcc to the module FccAnalysis.

    :param moduleinstance: The module we load (FccAnalysis)
    """

    moduleinstance.setValue("fccExecutable", self.fccExecutable)
    moduleinstance.setValue("isGaudiOptionsFileNeeded", self.isGaudiOptionsFileNeeded)
    moduleinstance.setValue("logLevel", self.logLevel)
    moduleinstance.setValue("read", self.read)
    moduleinstance.setValue("randomGenerator", self.randomGenerator)

  def _checkConsistency(self, job=None):
    """This function checks the minimum requirements of the application and updates the sandbox with files/folders required by the application.

    :param job: The job containing the application
    :type job: DIRAC.Interfaces.API.Job.Job

    :return: The success or failure of the consistency checking
    :rtype: DIRAC.S_OK, DIRAC.S_ERROR
    """

    infoMessage = (
        "Application general consistency :"
        " _checkConsistency() on '%(name)s'..." % {'name': self.appname}
        )
    LOG.info(infoMessage)

    if not self.version:
      errorMessage = 'Version not set!'
      LOG.error(errorMessage)
      return S_ERROR(errorMessage)

    infoMessage = (
        "Consistency : Version of the application set to :"
        "\nversion : %(version)s" % {'version': self.version}
        )
    LOG.info(infoMessage)

    # The executable is mandatory and also the configuration file except if the
    # input is taken from an other app hence the use of '_inputapp'
    if not (self.fccExecutable and (self.steeringFile or self._inputapp)):
      errorMessage = (
          "Consistency : Error in parsing '%(name)s' application :\n"
          "You have to provide at least an executable"
          " and a configuration file for each application" % {'name': self.appname}
          )
      LOG.error(errorMessage)
      return S_ERROR(errorMessage)

    if not isinstance(self.steeringFile, str):
      errorMessage = (
          "Consistency : Fcc Application accepts only one input configuration file:\n"
          "If you want to run the application '%(name)s' with many configurations then\n"
          "Create an new application with the other configuration\n"
          "You can also use the 'getInputFromApp' method to link applications" % {'name': self.appname}
          )
      LOG.error(errorMessage)
      return S_ERROR(errorMessage)

    debugMessage = (
        "Consistency : Executable and configuration of the application set to :"
        "\nexecutable : %(exec)s"
        "\nconfiguration : %(conf)s" % {'exec': self.fccExecutable, 'conf': self.steeringFile}
        )
    LOG.debug(debugMessage)

    # All input files are put in the FCC temporary sandbox for a
    # pre-checking before being added to the FCC final sandbox
    if self.steeringFile:
      self._tempInputSandbox.add(self.steeringFile)
      # Once steeringFile is given, we set the random generator for 'fcc-physics-read'
      if not self.read and "Pythia" in self.randomGenerator:
        self.randomGenerator["Pythia"].append(os.path.basename(self.steeringFile))

    LOG.info("Sandboxing : Sandboxing in progress...")

    # We update the sandbox with files/folders required by the application
    if not self._importToSandbox():
      errorMessage = "_importToSandbox() failed"
      LOG.error(errorMessage)
      return S_ERROR(errorMessage)

    LOG.info("Sandboxing : Sandboxing successfull")

    # setOutputFile() method informs the job that this application has an output file
    # This output can be used as input for another application.
    # In this way, app2.getInputFromApp(app1) method knows the ouput file of the given application
    # app1 thanks to its method setOutputFile().

    # self.inputSB is an attribute of the DIRAC Application and not of FCC.
    # The description file of the job (JDL file) contains a section for the input sandbox
    # This section is filled with a list of files (self.inputSB).
    # After user input files, application files, and application additionnal
    # files checked in the temporary sandbox, we set
    # the DIRAC application input sandbox : self.inputSB

    self._inputSandbox = self._inputSandbox.union(self._foldersToFilter)
    self.inputSB = list(self._inputSandbox)

    # Sandbox can be set at the application level or at the job level.
    # Whatever the level choosed, sandbox files are all put
    # in the same final destination which is a list of paths
    # in the JDL file (see Input Sandbox parameter of the JDL file).

    infoMessage = (
        "Application general consistency : _checkConsistency()"
        " on '%(name)s' successfull" % {'name': self.appname}
        )
    LOG.info(infoMessage)

    return S_OK(infoMessage)

  def _checkFinalConsistency(self):
    """

    :return: The success of the final consistency checking
    :rtype: DIRAC.S_OK

    """

    # Many output files can be managed if setOutputFile() method accepts list
    if self.outputFile:
      outputFiles = [self.outputFile] if isinstance(self.outputFile, str) else self.outputFile
      for outputFile in outputFiles:
        self._outputSandbox.add(
            "%s(_JobID).root (%s)" %
            (os.path.splitext(outputFile)[0],
             "Name of the eventual output root file"))

    # We add the log file and the output file to the output sandbox
    self._outputSandbox.add(self.logFile)

    infoMessage = (
        "\n********************************FCC SUMMARY******************************\n"
        "You plan to submit this application with its corresponding log :\n"
        "%(name)s --> %(log)s" % {'name': self.appname, 'log': self.logFile}
        )
    LOG.info(infoMessage)

    if self._inputSandbox:
      infoMessage = (
          "\nHere is the content of its input sandbox :\n%(input)s"
          % {'input': '\n'.join(self._inputSandbox)}
          )
      LOG.info(infoMessage)

    if self._outputSandbox:
      infoMessage = (
          "\nHere are the output files :\n%(output)s"
          % {'output': '\n'.join(self._outputSandbox)}
          )
      LOG.info(infoMessage)

    infoMessage = "\n********************************FCC SUMMARY******************************"
    LOG.info(infoMessage)

    return super(Fcc, self)._checkFinalConsistency()

  def _checkWorkflowConsistency(self):
    """Summary of the application done in _checkConsistency() method.

    :return: The success or the failure of _checkRequiredApp()
    :rtype: DIRAC.S_OK, DIRAC.S_ERROR
    """
    return self._checkRequiredApp()

  def _prodjobmodules(self, stepdefinition):

    # Here one needs to take care of listoutput
    if self.outputPath:
      self._listofoutput.append({'OutputFile': '@{OutputFile}', "outputPath": "@{OutputPath}",
                                 "outputDataSE": '@{OutputSE}'})

    res1 = self._setApplicationModuleAndParameters(stepdefinition)
    res2 = self._setOutputComputeDataList(stepdefinition)
    if not res1["OK"] or not res2["OK"]:
      return S_ERROR('prodjobmodules failed')
    return S_OK()

  def _resolveLinkedStepParameters(self, stepinstance):
    if isinstance(self._linkedidx, int):
      self._inputappstep = self._jobsteps[self._linkedidx]
    if self._inputappstep:
      stepinstance.setLink("InputFile", self._inputappstep.getType(), "OutputFile")
    return S_OK()

  def _userjobmodules(self, stepdefinition):
    res1 = self._setApplicationModuleAndParameters(stepdefinition)
    res2 = self._setUserJobFinalization(stepdefinition)
    if not res1["OK"] or not res2["OK"]:
      return S_ERROR('userjobmodules failed')
    return S_OK()

###############################  Fcc METHODS #####################################################
  @staticmethod
  def _findPath(path):
    """This function checks if file/folder exists.

    :param path: The path to look for
    :type path: str

    :return: The absolute path and its existence
    :rtype: (str, bool)
    """

    tempPath = os.path.realpath(path)
    return (tempPath, True) if os.path.exists(tempPath) else (path, False)

  def _importFiles(self):
    """This function adds folders/files to the sandbox specified by the user.

    :return: The success or the failure of the import
    :rtype: bool
    """

    if not self._tempInputSandbox:
      warnMessage = "Sandboxing : Your application has an empty input sandbox"
      LOG.warn(warnMessage)
      return True

    for path in self._tempInputSandbox:
      # We make a pre-checking of files in reachable filesystems (e.g. AFS, CVMFS)
      path, exists = self._findPath(path)

      # If file does not exist then consistency fails
      if not exists:
        errorMessage = (
            "Sandboxing : The path '%(path)s' does not exist\n"
            "Please ensure that your path exists in an accessible file system "
            "(AFS or CVMFS)" % {'path': path}
            )
        LOG.error(errorMessage)
        return False

      if path.startswith('/afs/'):
        warnMessage = (
            "Sandboxing : You plan to upload '%(path)s'"
            " which is stored on AFS\n"
            "STORING FILES ON AFS IS DEPRECATED" % {'path': path}
            )

        # We log the message into the warning level
        LOG.warn(warnMessage)

      # cvmfs paths do not need to be uploaded, they can be accessed remotely.
      # but for the moment do not be smart about it, add also cvmfs files,
      # no need to check.
      # if not path.startswith('/cvmfs/'):
      # if path is already in the sandbox, set type will kill duplicates
      self._inputSandbox.add(path)

      debugMessage = (
          "Sandboxing : The path '%(path)s' required by the application"
          " has been added to te sandbox" % {'path': path}
          )
      LOG.debug(debugMessage)

    debugMessage = (
        "Sandboxing : Files required by FCC application"
        " verified and added successfully to the sandbox"
        )

    LOG.debug(debugMessage)
    return True

  def _importToSandbox(self):
    """This function checks all the files and folders of the FCC temporary sandbox and add them to the FCC 'final' sandbox.

    :return: The success or the failure of the import
    :rtype: bool
    """

    LOG.debug("Sandboxing : Importation of user files/folders...")

    # Import files required by the application
    # If import process fails for some reasons (see functions above for more details)
    # then consistency fails
    if not self._importFiles():
      LOG.error("Sandboxing : _importFiles() failed")
      return False
      # Do not continue remaining checks

    LOG.debug("Sandboxing : Importation of user files/folders successfull")

    return True

  @staticmethod
  def _readFromFile(fileName):
    """This function reads a file and returns its content.

    :param fileName: The path of the file to read
    :type fileName: str

    :return: The content of the file
    :rtype: str, str
    """

    try:
      with open(fileName, 'r') as fileToRead:
        content = fileToRead.read()
    except IOError as e:
      return None, 'Sandboxing : FCC file reading failed\n%s' % e

    return content, 'Sandboxing : FCC file reading successfull'

###############################  Fcc DAUGHTER CLASSES ##############################################


class FccSw(Fcc):
  """Definition of an FCCSW application.

  Usage:

  >>> fccSw = FccSw(
      fccConfFile='/build/username/FCC/FCCSW/Examples/options/geant_pgun_fullsim.py',
      fccSwPath='/build/username/FCC/FCCSW'
    )
  """

  def __init__(self, fccConfFile="", fccSwPath="", read=False):

    super(FccSw, self).__init__()

    self.fccSwPath = os.path.realpath(fccSwPath)
    self.steeringFile = fccConfFile
    self.read = read

  def _checkConsistency(self, job=None):
    """Redefinition of ILCDIRAC.Workflow.Modules.Fcc._checkConsistency().

    :param job: The job containing the application
    :type job: DIRAC.Interfaces.API.Job.Job

    :return: The success or the failure of the consistency checking
    :rtype: DIRAC.S_OK, DIRAC.S_ERROR
    """

    LOG.debug("FCCSW specific consistency : _checkConsistency()...")

    if not self.fccSwPath or not os.path.exists(self.fccSwPath):
      errorMessage = (
          "FCCSW specific consistency : Error in parsing FCCSW application :\n"
          "You have to provide a valid path of the FCCSW installation"
          )
      LOG.error(errorMessage)
      return S_ERROR(errorMessage)

    debugMessage = (
        "FCCSW specific consistency : Creation of a temporary folder 'temp_fcc_dirac'"
        " in the current working directory..."
        )
    LOG.debug(debugMessage)

    # First, it creates a temporary local directory for folders whose
    # the content does not have to be sandboxed entirely
    # like filtered folders
    if not os.path.exists(self._tempCwd):
      try:
        os.makedirs(self._tempCwd)
      except OSError as e:
        errorMessage = "FCCSW specific consistency : Creation of 'temp_fcc_dirac' folder failed\n%s" % e
        LOG.error(errorMessage)
        return S_ERROR(errorMessage)

      LOG.debug("FCCSW specific consistency : Creation of 'temp_fcc_dirac' folder successfull")
    else:
      LOG.debug("FCCSW specific consistency : The temporary folder 'temp_fcc_dirac' already exists")

    # InstallArea folder is present on CVMFS so nothing to do
    # else if local FCCSW installation is used
    # download it because 'FCCSW.xenv' needs libraries from this folder

    self.fccExecutable = '%s/run gaudirun.py' % self.fccSwPath

    if not self.fccSwPath.startswith('/cvmfs/'):
      # 'FCCSW/run' script calls another 'run' script inside 'build.$BINARY_TAG' folder
      # The command works with a '.xenv' file located into 'build.$BINARY_TAG' relative to files of the cwd
      # We read the command of the 'run' script and we use the 'xenv' file of InstallArea instead
      # which is only related to CVMFS
      # If the reading of the command failed, we execute by default the command of the 0.8.1 release

      #python = '$PYTHON_BIN'
      python = '/cvmfs/sft.cern.ch/lcg/views/LCG_88/x86_64-slc6-gcc62-opt/bin/python'
      #xenv = '$XENV'
      xenv = '/cvmfs/fcc.cern.ch/sw/0.8.1/gaudi/v28r2/x86_64-slc6-gcc62-opt/scripts/xenv'
      argXenv = 'InstallArea/FCCSW.xenv'

      executablePath = ''

      for path in os.listdir(self.fccSwPath):
        absPath = os.path.join(self.fccSwPath, path)
        if path.startswith('build.') and not os.path.isfile(absPath):
          executablePath = os.path.join(absPath, 'run')

      if executablePath and os.path.exists(executablePath):
        executableContent, message = self._readFromFile(executablePath)

        if not executableContent:
          LOG.warn(message)
          LOG.debug('FCCSW specific consistency : Using by default the command of the 0.8.1 release !')
        else:
          LOG.debug(message)

          # Separate shebang (0) and command of the executable (1)
          executableCommand = executableContent.split('\n')[1]
          # Break command of the executable into parts
          executableParts = executableCommand.split()

          python = executableParts[1]
          xenv = executableParts[2]

      self.fccExecutable = 'exec %s %s --xml %s gaudirun.py' % (python, xenv, argXenv)
      installAreaFolder = os.path.join(self.fccSwPath, 'InstallArea')
      # We do not need all the content of these folders hence the filtering
      self._foldersToFilter.append(installAreaFolder)

      # Explanation
      # InstallAreaFolder : all dbg files are excluded
      # detectorFolder : only xml files are included
      self._filteredExtensions += ['.dbg']
      self._excludesOrIncludes += [True]

    # 'Detector' folder is not present on CVMFS in release v0.8.1 so the user has to add this
    # folder to the sandbox ('cf the corresponding warning message')
    # Actually, FCCSW installation of CVMFS run successfully only with configuration files that
    # do not need additionnal files like 'Generation/data/ParticleTable.txt' or folders like 'Detector'
    # FCCSW release made after 31/08/2017 will put a complete installation of FCCSW
    # And all examples of Examples/options should run successfully

    LOG.debug("FCCSW specific consistency : _checkConsistency() successfull")

    return super(FccSw, self)._checkConsistency()

  def _checkFinalConsistency(self):
    """Redefinition of ILCDIRAC.Workflow.Modules.Fcc._checkFinalConsistency(). Setting True 'isGaudiOptionsFileNeeded' attribute tells that the application needs to generate the gaudi option file of FccSw.

    :return: The success of the final consistency checking
    :rtype: DIRAC.S_OK
    """

    self.isGaudiOptionsFileNeeded = True
    return super(FccSw, self)._checkFinalConsistency()

  def _importToSandbox(self):
    """Redefinition of FCC._importToSandbox() method. FCCSW needs extra folders like 'InstallArea', 'Detector' and extra files specified in its configuration file.

    :return: The success or the failure of the import
    :rtype: bool
    """

    if not super(FccSw, self)._importToSandbox():
      errorMessage = "Sandboxing : _importToSandbox() failed"
      LOG.error(errorMessage)
      return False

    if not self._importFccswFiles():
      return False

    # After sandboxing, we filter some folders required by applications
    # and we import the filtered folders to the sandbox.
    if not self._setFilterToFolders():
      errorMessage = "_setFilterToFolders() failed"
      LOG.error(errorMessage)
      return False

    return True

  def _importFccswFiles(self):
    """FCCSW application needs additional files specified in the configuration file It also needs folders like 'InstallArea' and 'Detector'.

    :return: The success or the failure of the import
    :rtype: bool
    """

    # 'InstallArea' Folder already resolved and added in FccSw class
    # It is present in CVMFS contrary to 'Detector' folder
    #installAreaFolder = os.path.join(self.fccSwPath, 'InstallArea')
    detectorFolder = os.path.join(self.fccSwPath, 'Detector')

    # As CVMFS installation is not complete ('Detector' folder missing in release v0.8.1)
    # we do this check
    if not os.path.exists(detectorFolder):
      warnMessage = (
          "Sandboxing : The folder 'Detector' does not exist,"
          " it is not present in the FCCSW installation"
          "\nThen you should have added it manually to the input sandbox !"
          )
      LOG.warn(warnMessage)
    else:
      # We do not need all the content of these folders hence the filtering
      self._foldersToFilter.append(detectorFolder)

      # Explanation
      # InstallAreaFolder : all dbg files are excluded
      # detectorFolder : only xml files are included
      self._filteredExtensions += ['.xml']
      self._excludesOrIncludes += [False]

    LOG.debug("Sandboxing : FCC configuration file reading...")

    content, message = self._readFromFile(self.steeringFile)

    # If the configuration file is not valid then consistency fails
    if not content:
      LOG.error(message)
      return False

    LOG.debug(message)

    # Find all additional files specified in the fccsw configuration file
    #xml_files = re.findall(r'file:(.*.xml)',content)

    txtFiles = re.findall(r'(.*) *= *"(.*.txt)"', content)
    cmdFiles = re.findall(r'(.*) *= *"(.*.cmd)"', content)

    # Upload file not commented
    txtFiles = [txtFile[1] for txtFile in txtFiles if not txtFile[0].startswith("#")]
    cmdFiles = [cmdFile[1] for cmdFile in cmdFiles if not cmdFile[0].startswith("#")]

    lookForPythia = re.findall(r'.* *= *PythiaInterface *\(', content)

    # Check if PythiaInterface is instantiated somewhere and not commented
    isPythiaGeneratorUsed = True if lookForPythia and not lookForPythia[0].startswith("#") else False

    if isPythiaGeneratorUsed and cmdFiles:
      self.randomGenerator["Pythia"] = cmdFiles
    else:
      self.randomGenerator["Gaudi"] = True

    # From these paths we re-create the tree in the temporary sandbox
    # with only the desired file.
    # In the configuration file, these paths are relative to FCCSW installation.
    # e.g. Generation/data/foo.xml

    if not self._resolveTreeOfFiles(txtFiles, '.txt'):
      LOG.error("Sandboxing : _resolveTreeOfFiles() failed")
      return False
      # Do not continue remaining checks

    # We do the same now for '.cmd' files that may be specified in the configuration file
    return self._resolveTreeOfFiles(cmdFiles, '.cmd')

  def _resolveTreeOfFiles(self, files, extension):
    """Resolve FCC Configuration Files.

    FCC configuration file like 'Examples/options/geant_pgun_fullsim.py' needs files coming from FCCSW installation.
    The path of these files are hard-coded in the FCC configuration file with a relative path to FCCSW installation.

    This function aims to resolve the absolute path of each hard-coded files
    required by the configuration file.

    Once we have the absolute path of the file, we recreate the tree strucutre
    of the file in a temporary folder and copy the file to it.

    Because the original directory of the file may contain other files, in this
    way we copy only the desired file.

    The file has now a new location and this is this new tree that will be
    added to the sandbox.

    :param files: The files specified in the configuration file
    :type files: list

    :param extension: The extension of file to resolve
    :type extension: str

    :return: success or failure of the file copy
    :rtype: bool
    """

    if not files:
      warnMessage = (
          "Sandboxing : FCCSW configuration file"
          " does not seem to need any additional '%(ext)s' files" % {'ext': extension}
          )
      LOG.warn(warnMessage)
      return True

    for afile in files:

      source = os.path.realpath(os.path.join(self.fccSwPath, afile))
      destination = os.path.realpath(os.path.join(self._tempCwd, afile))

      if not os.path.exists(source):
        warnMessage = (
            "Sandboxing : The file '%s' does not exist,"
            " it is not present in the FCCSW installation"
            "\nThen you should have added it manually to the input sandbox !" % {'source': source}
            )
        LOG.warn(warnMessage)
        continue

      # We save the relative path of the file
      # e.g. Generation/data/
      tree = os.path.dirname(afile)
      # We prepend the temporary sandbox to the tree
      # which will become the new location of the file.
      treeFullPath = os.path.join(self._tempCwd, tree)

      debugMessage = (
          "Sandboxing : Tree '%(tree)s' of additionnal"
          " '%(ext)s' files creation..." % {'tree': treeFullPath, 'ext': extension}
          )
      LOG.debug(debugMessage)

      # We create the tree locally in the temporary folder
      if not os.path.exists(treeFullPath):
        try:
          os.makedirs(treeFullPath)
        except OSError as e:
          errorMessage = (
              "Sandboxing : Tree '%(tree)s' of additionnal"
              " '%(ext)s' files creation failed\n%(error)s" % {'tree': treeFullPath, 'ext': extension, 'error': e}
              )
          LOG.error(errorMessage)
          return False

        debugMessage = (
            "Sandboxing : Tree '%(tree)s' of additionnal"
            " '%(ext)s' files creation successfull" % {'tree': treeFullPath, 'ext': extension}
            )
        LOG.debug(debugMessage)

      else:
        debugMessage = "Sandboxing : Tree '%s' already exists" % treeFullPath
        LOG.debug(debugMessage)

      # We take the first directory of the tree
      # We add this root directory to the 'final' sandbox
      rootFolder = tree.split(os.path.sep)[0]
      rootFolderFullPath = os.path.join(self._tempCwd, rootFolder)

      self._inputSandbox.add(rootFolderFullPath)

      # if paths already exists do not copy it
      # go to the next file
      if os.path.exists(destination):
        debugMessage = "Sandboxing : The file '%s' already exists" % destination
        LOG.debug(debugMessage)
      else:
        debugMessage = "Sandboxing : Additional file '%s' copy..." % source
        LOG.debug(debugMessage)

        try:
          shutil.copyfile(source, destination)
        except (IOError, shutil.Error) as e:
          errorMessage = (
              "Sandboxing : Additionnal files"
              " '%(src)s' copy failed\n%(error)s" % {'src': source, 'error': e}
              )
          LOG.error(errorMessage)
          return False

        debugMessage = (
            "Sandboxing : Additionnal files"
            " '%(src)s' copy successfull to '%(dst)s'" % {'src': source, 'dst': destination}
            )
        LOG.debug(debugMessage)

    return True

  def _setFilterToFolders(self):
    """Some folders required by FCCSW do not need to be imported with all their content.

    Some files have to be excluded or only some files have to be included.
    Then for each folder, we have the include/exclude parameter and the linked extension.

    This function maps the folders with their corresponding filters if there are.

    :return: The success or the failure of the filter's setting
    :rtype: bool
    """

    if not self._foldersToFilter:
      debugMessage = "Sandboxing : No filtering required"
      LOG.debug(debugMessage)
      return True

    copiedFolders = []

    for idx, actualFolder in enumerate(self._foldersToFilter):

      if not os.path.exists(actualFolder):
        errorMessage = (
            "Sandboxing : _filterFolders() failed\n"
            "The folder '%(actual)s' does not exist\n"
            "Check if you're FCCSW installation is complete" % {'actual': actualFolder}
            )
        LOG.error(errorMessage)
        return False

      if idx < len(self._filteredExtensions):
        filteredExtension = self._filteredExtensions[idx]
        excludeOrInclude = self._excludesOrIncludes[idx]
      else:
        filteredExtension = False
        excludeOrInclude = False

      tempFolder = os.path.join(self._tempCwd, os.path.basename(actualFolder))

      # DIRAC already compress the sandbox before submitting the job
      # do not compress folders

      LOG.debug("Sandboxing : Folders filtering...")

      if not self._filterFolders(tempFolder, actualFolder, filteredExtension, excludeOrInclude):
        LOG.error("Sandboxing : _filterFolders() failed")
        return False

      LOG.debug("Sandboxing : Folders filtering successfull")

      copiedFolders.append(tempFolder)

    self._foldersToFilter = copiedFolders

    return True

  def _filterFolders(self, tempFolder, actualFolder,
                     filteredExtension, excludeOrInclude):
    """Knowing the filter for each folder, we copy the 'filtered' folder in the temporary folder 'temp_fcc_dirac'.

    After, we add the path of the 'filtered' folder to the sandbox instead of
    its original path.

    Like that, we do not import unnecessary files to the sandbox.
    It is like we create a 'light' copy of the orginal folder.

    If folders have to be filtered then, we do not have to add them directly to the sandbox
    because it will put all content of folders.

    So we copy only the content we want in the filtered folder
    inside the temporary folder 'temp_fcc_dirac'.

    After, we add the filtered folders located in 'temp_fcc_dirac' to the sandbox.

    :param tempFolder: The temporary working directory (destination) used for the sandboxing
    :type tempFolder: str

    :param actualFolder: The original (source) path of folder checked by the copy process
    :type actualFolder: str

    :param filteredExtension: The extension of file we do (not) want
    :type filteredExtension: str

    :param excludeOrInclude: extension is excluded or included
    :type excludeOrInclude: bool

    :return: The success or the failure of the filtering
    :rtype: bool
    """

    debugMessage = "Sandboxing : Checking of the filtered folder '%s'..." % tempFolder
    LOG.debug(debugMessage)

    if not os.path.exists(tempFolder):
      debugMessage = "Sandboxing : Creation of the filtered folder '%s'..." % tempFolder
      LOG.debug(debugMessage)

      try:
        os.makedirs(tempFolder)
      except OSError as e:
        errorMessage = (
            "Sandboxing : Creation of the filtered folder"
            " '%(temp)s' failed\n%(error)s" % {'temp': tempFolder, 'error': e}
            )
        LOG.error(errorMessage)
        return False

      debugMessage = (
          "Sandboxing : Creation of the filtered folder"
          " '%(temp)s' successfull" % {'temp': tempFolder}
          )
      LOG.debug(debugMessage)

    for path in os.listdir(actualFolder):
      source = os.path.realpath(os.path.join(actualFolder, path))
      destination = os.path.realpath(os.path.join(tempFolder, path))

      # If file then check existence
      if not os.path.exists(source):
        errorMessage = "Sandboxing : The file '%s' does not exist" % source
        LOG.error(errorMessage)
        return False

      if not os.path.isfile(source):
        # Recursive call for folders
        if not self._filterFolders(destination, source, filteredExtension, excludeOrInclude):
          LOG.error("Sandboxing : _filterFolders() failed")
          return False
      else:
        if os.path.exists(destination):
          debugMessage = "Sandboxing : The file '%s' already exists" % source
          LOG.debug(debugMessage)
        else:

          if ((excludeOrInclude and not path.endswith(filteredExtension))
              or (not excludeOrInclude and path.endswith(filteredExtension))
                  or not filteredExtension):

            warn = False
            debugMessage = "Sandboxing : File '%s' copy..." % source
            LOG.debug(debugMessage)

            # Copy considering filters to apply
            try:
              shutil.copyfile(source, destination)
            except (IOError, shutil.Error) as e:
              warnMessage = "Sandboxing : The copy of the file '%s' failed\n%s" % (destination, e)
              LOG.warn(warnMessage)
              warn = True
              # return False

            if not warn:
              debugMessage = (
                  "Sandboxing : Copy of the file"
                  " '%(src)s' successfull to '%(dst)s'" % {'src': source, 'dst': destination}
                  )
              LOG.debug(debugMessage)

    debugMessage = "Sandboxing : Folder '%s' filtering successfull" % tempFolder
    LOG.debug(debugMessage)

    return True


class FccAnalysis(Fcc):
  """Definition of an FCCAnalysis application. By default, it runs FCCPHYSICS.

  Usage:

  >>> FCC_PHYSICS = FccAnalysis(
      fccConfFile='/cvmfs/fcc.cern.ch/sw/0.7/fcc-physics/0.1/x86_64-slc6-gcc49-opt/share/ee_ZH_Zmumu_Hbb.txt'
    )
  """

  def __init__(self, executable='fcc-pythia8-generate', fccConfFile=""):

    super(FccAnalysis, self).__init__()

    self.steeringFile = fccConfFile
    self.fccExecutable = executable

    # If it is a different executable
    # then it is :
    # - fcc-physics-read-delphes or
    # - fcc-physics-read
    # So find card file and set the seed !

    if executable != 'fcc-pythia8-generate':
      self.read = True
    else:  # Set the seed for the generation of events
      self.randomGenerator = {"Pythia": []}
