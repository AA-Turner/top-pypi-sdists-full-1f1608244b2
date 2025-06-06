""" The Script class provides a simple way for users to specify an executable
    or file to run (and is also a simple example of a workflow module).
"""
import os
import re
import shlex
import shutil
import stat
import sys

from DIRAC import gLogger, gConfig
from DIRAC.Core.Utilities.Subprocess import systemCall
from DIRAC.WorkloadManagementSystem.Utilities.RemoteRunner import RemoteRunner
from DIRAC.Workflow.Modules.ModuleBase import ModuleBase, GracefulTermination


class cta_script(ModuleBase):
    """Module for running executable"""

    #############################################################################
    def __init__(self, log=None):
        """c'tor"""
        if log is not None:
            self.log = log
        else:
            self.log = gLogger.getSubLogger(self.__class__.__name__)
        super().__init__(self.log)

        # Set defaults for all workflow parameters here
        self.executable = ""
        self.applicationName = ""
        self.applicationVersion = ""
        self.applicationLog = ""
        self.arguments = ""
        self.workflow_commons = None
        self.step_commons = None

        self.environment = None
        self.callbackFunction = None
        self.bufferLimit = 52428800

    #############################################################################

    def _resolveInputVariables(self):
        """By convention the workflow parameters are resolved here."""
        super()._resolveInputVariables()
        super()._resolveInputStep()

        self.arguments = self.step_commons.get("arguments", self.arguments)
        if not self.arguments.strip():
            self.arguments = self.workflow_commons.get("arguments", self.arguments)

    #############################################################################

    def _initialize(self):
        """check if the previous step failed"""
        if not self._checkWFAndStepStatus(noPrint=False):
            if self.workflowStatus["Errno"] == 166:
                self.log.info("Workflow failed with status 166 : input files partially processed")
            elif self.workflowStatus["Errno"] == 167:
                self.log.info("Workflow failed with status 167: no input file processed")
            else:
                raise GracefulTermination("Previous step failed : skipping this module")

        """simple checks"""
        if not self.executable:
            raise RuntimeError("No executable defined")

    def _setCommand(self):
        """set the command that will be executed"""
        self.command = self.executable
        if os.path.exists(os.path.basename(self.executable)):
            self.executable = os.path.basename(self.executable)
            if not os.access(f"{os.getcwd()}/{self.executable}", 5):
                # doc in https://docs.python.org/2/library/stat.html#stat.S_IRWXU
                os.chmod(
                    f"{os.getcwd()}/{self.executable}",
                    stat.S_IRWXU
                    | stat.S_IRGRP
                    | stat.S_IXGRP
                    | stat.S_IROTH
                    | stat.S_IXOTH,
                )
            self.command = f"{os.getcwd()}/{self.executable}"
        elif re.search(".py$", self.executable):
            self.command = f"{sys.executable} {self.executable}"
        elif shutil.which(self.executable):
            self.command = self.executable

        if self.arguments:
            self.command = f"{self.command} {self.arguments}"

        self.log.info(f"Command is: {self.command}")

    def _executeCommand(self):
        """execute the self.command (uses systemCall)"""
        failed = False

        # Check whether the execution should be done remotely
        if gConfig.getValue("/LocalSite/RemoteExecution", False):
            remoteRunner = RemoteRunner(
                gConfig.getValue("/LocalSite/Site"),
                gConfig.getValue("/LocalSite/GridCE"),
                gConfig.getValue("/LocalSite/CEQueue"),
            )
            retVal = remoteRunner.execute(self.command)
        else:
            retVal = systemCall(
                timeout=0,
                cmdSeq=shlex.split(self.command),
                env=self.environment,
                callbackFunction=self.callbackFunction,
                bufferLimit=self.bufferLimit,
            )

        if not retVal["OK"]:
            failed = True
            self.log.error(
                "System call execution failed:", "\n" + str(retVal["Message"])
            )
            self._exitWithError(1000)
        status, stdout, stderr = retVal["Value"][0:3]
        if status:
            failed = True
            self.log.error(
                "Non-zero status while executing",
                f"{self.command} exited with status {status}",
            )
        else:
            self.log.info(f"{self.command} execution completed with status {status}")

        self.log.verbose(stdout)
        self.log.verbose(stderr)
        if os.path.exists(self.applicationLog):
            self.log.verbose(f"Removing existing {self.applicationLog}")
            os.remove(self.applicationLog)
        with open(f"{os.getcwd()}/{self.applicationLog}", "w") as fopen:
            fopen.write(
                f"<<<<<<<<<< {self.executable} Standard Output >>>>>>>>>>\n\n{stdout} "
            )
            if stderr:
                fopen.write(
                    f"<<<<<<<<<< {self.executable} Standard Error >>>>>>>>>>\n\n{stderr} "
                )
        self.log.info(f"Output written to {self.applicationLog}, execution complete.")

        if failed:
            self._exitWithError(status)

    def _exitWithError(self, status):
        """Here because of possible extensions.

        :param str status: the status of the application becomes the status of the workflow,
                           and may be interpreted by JobWrapper (e.g. for rescheduling cases)
        """
        raise RuntimeError(
            f"'{os.path.basename(self.executable).split('_')[0]}' Exited With Status {status}",
            status,
        )

    def _finalize(self):
        """simply finalize"""
        applicationString = os.path.basename(self.executable).split("_")[0]
        if self.applicationName and self.applicationName.lower() != "unknown":
            applicationString += f" ({self.applicationName} {self.applicationVersion})"
        status = f"{applicationString} successful"

        super()._finalize(status)
