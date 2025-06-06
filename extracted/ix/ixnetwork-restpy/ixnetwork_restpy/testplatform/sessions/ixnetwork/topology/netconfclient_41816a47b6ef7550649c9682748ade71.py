# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class NetconfClient(Base):
    """Netconf Client emulates a Netconf Controller which connects to a DUT supporting Netconf as per RFC6241/RFC6242
    The NetconfClient class encapsulates a list of netconfClient resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetconfClient.find() method.
    The list can be managed by using the NetconfClient.add() and NetconfClient.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "netconfClient"
    _SDM_ATT_MAP = {
        "Active": "active",
        "CapabilitiesBase1Dot0": "capabilitiesBase1Dot0",
        "CapabilitiesBase1Dot1": "capabilitiesBase1Dot1",
        "CapabilitiesCandidate": "capabilitiesCandidate",
        "CapabilitiesConfirmedCommit": "capabilitiesConfirmedCommit",
        "CapabilitiesInterleave": "capabilitiesInterleave",
        "CapabilitiesNotification": "capabilitiesNotification",
        "CapabilitiesRollbackOnError": "capabilitiesRollbackOnError",
        "CapabilitiesStartup": "capabilitiesStartup",
        "CapabilitiesUrl": "capabilitiesUrl",
        "CapabilitiesValidate": "capabilitiesValidate",
        "CapabilitiesWritableRunning": "capabilitiesWritableRunning",
        "CapabilitiesXpath": "capabilitiesXpath",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "DecryptedCapture": "decryptedCapture",
        "DescriptiveName": "descriptiveName",
        "DoNotValidateServerResponse": "doNotValidateServerResponse",
        "DownloadFilePath": "downloadFilePath",
        "EnablePassphrase": "enablePassphrase",
        "Errors": "errors",
        "FetchSchemaInfo": "fetchSchemaInfo",
        "LogCleanUpOption": "logCleanUpOption",
        "LogFileAge": "logFileAge",
        "Multiplier": "multiplier",
        "Name": "name",
        "NetconfSessionState": "netconfSessionState",
        "NumberOfCommandSnippetsPerClient": "numberOfCommandSnippetsPerClient",
        "OutputDirectory": "outputDirectory",
        "Passphrase": "passphrase",
        "Password": "password",
        "PortNumber": "portNumber",
        "PrivateKeyDirectory": "privateKeyDirectory",
        "PrivateKeyFileName": "privateKeyFileName",
        "SaveReplyXML": "saveReplyXML",
        "SchemaOutputDirectory": "schemaOutputDirectory",
        "SendCloseOnStop": "sendCloseOnStop",
        "ServerIpv4Address": "serverIpv4Address",
        "SessionStatus": "sessionStatus",
        "SshAuthenticationMechanism": "sshAuthenticationMechanism",
        "StackedLayers": "stackedLayers",
        "StateCounts": "stateCounts",
        "Status": "status",
        "UploadFilePath": "uploadFilePath",
        "UserName": "userName",
    }
    _SDM_ENUM_MAP = {
        "logCleanUpOption": ["notClean", "clean"],
        "status": [
            "configured",
            "error",
            "mixed",
            "notStarted",
            "started",
            "starting",
            "stopping",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(NetconfClient, self).__init__(parent, list_op)

    @property
    def CommandSnippetsData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.commandsnippetsdata_bfd4407665f4331cd53fee07f65b1820.CommandSnippetsData): An instance of the CommandSnippetsData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.commandsnippetsdata_bfd4407665f4331cd53fee07f65b1820 import (
            CommandSnippetsData,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CommandSnippetsData", None) is not None:
                return self._properties.get("CommandSnippetsData")
        return CommandSnippetsData(self)._select()

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import (
            LearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedInfo", None) is not None:
                return self._properties.get("LearnedInfo")
        return LearnedInfo(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def CapabilitiesBase1Dot0(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether base1.0 support should be advertised in Capabilities.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitiesBase1Dot0"])
        )

    @property
    def CapabilitiesBase1Dot1(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether base1.1 support should be advertised in Capabilities.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitiesBase1Dot1"])
        )

    @property
    def CapabilitiesCandidate(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether Netconf Client supports capability candidate to make changes into an intermediate candidate database. Normally this is preferred over writable-running.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitiesCandidate"])
        )

    @property
    def CapabilitiesConfirmedCommit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether Netconf Client supports capability confirmed-commit to specify ability to commit a group of commands or none as a batch.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitiesConfirmedCommit"])
        )

    @property
    def CapabilitiesInterleave(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether Netconf Client supports capability interleave to interleave notifications and responses.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitiesInterleave"])
        )

    @property
    def CapabilitiesNotification(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether Netconf Client supports capability notification to aynchronously handle notifications from Netconf server device connected to.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitiesNotification"])
        )

    @property
    def CapabilitiesRollbackOnError(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether Netconf Client supports capability rollback to rollback partial changes make changes on detection of error during validate or commit.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitiesRollbackOnError"])
        )

    @property
    def CapabilitiesStartup(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether Netconf Client supports capability startup to make changes in config persistent on device restart.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitiesStartup"])
        )

    @property
    def CapabilitiesUrl(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether Netconf Client supports capability url to specify netconf commands using url.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitiesUrl"])
        )

    @property
    def CapabilitiesValidate(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether Netconf Client supports capability validate to specify ability to validate a netconf command prior to commit.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitiesValidate"])
        )

    @property
    def CapabilitiesWritableRunning(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether Netconf Client supports capability writable-running to directly modify running config.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitiesWritableRunning"])
        )

    @property
    def CapabilitiesXpath(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether Netconf Client supports capability xpath to specify netconf commands and filters using xpath extensions.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CapabilitiesXpath"])
        )

    @property
    def ConnectedVia(self):
        # type: () -> List[str]
        """DEPRECATED
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectedVia"])

    @ConnectedVia.setter
    def ConnectedVia(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConnectedVia"], value)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DecryptedCapture(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether SSH packets for this session will be captured and stored on client in decrypted form.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DecryptedCapture"])
        )

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def DoNotValidateServerResponse(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this option is enabled, the Netconf client will not parse server responses. Use this option to optimize memory usage in the client.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DoNotValidateServerResponse"])
        )

    @property
    def DownloadFilePath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Download Path
        """
        return self._get_attribute(self._SDM_ATT_MAP["DownloadFilePath"])

    @property
    def EnablePassphrase(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If the Private Key was passphrase protected, this should be enabled to allow configuration of passphrase used.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnablePassphrase"])
        )

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def FetchSchemaInfo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether a get-schema operation will be performed after capability exchange
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FetchSchemaInfo"])
        )

    @property
    def LogCleanUpOption(self):
        # type: () -> str
        """
        Returns
        -------
        - str(notClean | clean): Debug Log Clean Up
        """
        return self._get_attribute(self._SDM_ATT_MAP["LogCleanUpOption"])

    @LogCleanUpOption.setter
    def LogCleanUpOption(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LogCleanUpOption"], value)

    @property
    def LogFileAge(self):
        # type: () -> int
        """
        Returns
        -------
        - number: This field determines how old logs to be deleted.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LogFileAge"])

    @LogFileAge.setter
    def LogFileAge(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LogFileAge"], value)

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Multiplier"])

    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Multiplier"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def NetconfSessionState(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[authenticating | connecting | initialized | none | openingChannel | ready | reconnecting | requestingSubsystem]): Shows the current state of the Netconf SSH Session. None - Not started. Initialized - Configuration has reached the port and TCP connect is on-going. Connecting - SSH Connect is in process. Authenticating - The SSH session is authenticating with the DUT using user/password or Key-based authentication. Open Channel - SSH session is established and SSH Channel is being opened on which data will be sent. Requesting Subsystem - Netconf Subsystem is being requested on top of SSH channel. Ready - The SSH session is in Ready state and waiting for Netconf data to be exchanged. Note that this does not mean that NETCONF is in Up state. That is reached only after Netconf Capabilities are negotiated and there is at least one matching Netconf version (1.0 or 1.1) supported on both client and server. Reconnecting - The TCP connection is broken with DUT and the client is trying to reconnect via TCP with the server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NetconfSessionState"])

    @property
    def NumberOfCommandSnippetsPerClient(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Command Snippets per client.Maximum 100 are allowed per client.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["NumberOfCommandSnippetsPerClient"]
        )

    @NumberOfCommandSnippetsPerClient.setter
    def NumberOfCommandSnippetsPerClient(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["NumberOfCommandSnippetsPerClient"], value
        )

    @property
    def OutputDirectory(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Location of Directory in Client where the decrypted capture, if enabled, and server replies, if enabled, will be stored.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OutputDirectory"])
        )

    @property
    def Passphrase(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The passphrase with which the Private Key was additionally protected during generation. For multiple clients and assymetric passphrases( which cannot be expressed easily as a pattern) please explore File option in Master Row Pattern Editor by putting the file namesin a .csv and pulling those values into the column cells.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Passphrase"]))

    @property
    def Password(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Password for Username/Password mode.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Password"]))

    @property
    def PortNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The TCP Port Number the Netconf server is listening on. Well-known port numbers are 830 (RFC 6242) and 22 (SSH).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PortNumber"]))

    @property
    def PrivateKeyDirectory(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Directory containing Private Key file for this session.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrivateKeyDirectory"])
        )

    @property
    def PrivateKeyFileName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): File containing Private Key.(e.g. generated using ssh_keygen) . For multiple clients and assymetric key file names( which cannot be expressed easily as a pattern) please explore File option in Master Row Pattern Editor by putting the file namesin a .csv and pulling those values into the column cells.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PrivateKeyFileName"])
        )

    @property
    def SaveReplyXML(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If this is enabled, Hellos and replies to commands sent via Command Snippets or global command (such as 'get') by the Netconf Server will be stored in the Output Directoryin current run folder/Replies. Any RPC errors recieved will be stored in a separate Error directory for convenience of debugging error scenarios.This option can be enabled even when a session is already up in which case the replies will be saved from that point of time.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SaveReplyXML"]))

    @property
    def SchemaOutputDirectory(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Location of Directory in Client where the retrieved modules will be stored.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SchemaOutputDirectory"])
        )

    @property
    def SendCloseOnStop(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This specifies whether a <close-session> message will be sent on stopping this client
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SendCloseOnStop"])
        )

    @property
    def ServerIpv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the IPv4 address of the DUT to which the Netconf Server should connect.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ServerIpv4Address"])
        )

    @property
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionStatus"])

    @property
    def SshAuthenticationMechanism(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The authentication mechanism for connecting to Netconf Server.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SshAuthenticationMechanism"])
        )

    @property
    def StackedLayers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP["StackedLayers"])

    @StackedLayers.setter
    def StackedLayers(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["StackedLayers"], value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP["StateCounts"])

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Status"])

    @property
    def UploadFilePath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Upload
        """
        return self._get_attribute(self._SDM_ATT_MAP["UploadFilePath"])

    @property
    def UserName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Username for Username/Password mode and also used for Key-based Authentication as the username.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["UserName"]))

    def update(
        self,
        ConnectedVia=None,
        LogCleanUpOption=None,
        LogFileAge=None,
        Multiplier=None,
        Name=None,
        NumberOfCommandSnippetsPerClient=None,
        StackedLayers=None,
    ):
        # type: (List[str], str, int, int, str, int, List[str]) -> NetconfClient
        """Updates netconfClient resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - LogCleanUpOption (str(notClean | clean)): Debug Log Clean Up
        - LogFileAge (number): This field determines how old logs to be deleted.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfCommandSnippetsPerClient (number): Number of Command Snippets per client.Maximum 100 are allowed per client.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ConnectedVia=None,
        LogCleanUpOption=None,
        LogFileAge=None,
        Multiplier=None,
        Name=None,
        NumberOfCommandSnippetsPerClient=None,
        StackedLayers=None,
    ):
        # type: (List[str], str, int, int, str, int, List[str]) -> NetconfClient
        """Adds a new netconfClient resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - LogCleanUpOption (str(notClean | clean)): Debug Log Clean Up
        - LogFileAge (number): This field determines how old logs to be deleted.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfCommandSnippetsPerClient (number): Number of Command Snippets per client.Maximum 100 are allowed per client.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved netconfClient resources using find and the newly added netconfClient resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained netconfClient resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ConnectedVia=None,
        Count=None,
        DescriptiveName=None,
        DownloadFilePath=None,
        Errors=None,
        LogCleanUpOption=None,
        LogFileAge=None,
        Multiplier=None,
        Name=None,
        NetconfSessionState=None,
        NumberOfCommandSnippetsPerClient=None,
        SessionStatus=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
        UploadFilePath=None,
    ):
        """Finds and retrieves netconfClient resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve netconfClient resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all netconfClient resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - DownloadFilePath (str): Download Path
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - LogCleanUpOption (str(notClean | clean)): Debug Log Clean Up
        - LogFileAge (number): This field determines how old logs to be deleted.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NetconfSessionState (list(str[authenticating | connecting | initialized | none | openingChannel | ready | reconnecting | requestingSubsystem])): Shows the current state of the Netconf SSH Session. None - Not started. Initialized - Configuration has reached the port and TCP connect is on-going. Connecting - SSH Connect is in process. Authenticating - The SSH session is authenticating with the DUT using user/password or Key-based authentication. Open Channel - SSH session is established and SSH Channel is being opened on which data will be sent. Requesting Subsystem - Netconf Subsystem is being requested on top of SSH channel. Ready - The SSH session is in Ready state and waiting for Netconf data to be exchanged. Note that this does not mean that NETCONF is in Up state. That is reached only after Netconf Capabilities are negotiated and there is at least one matching Netconf version (1.0 or 1.1) supported on both client and server. Reconnecting - The TCP connection is broken with DUT and the client is trying to reconnect via TCP with the server.
        - NumberOfCommandSnippetsPerClient (number): Number of Command Snippets per client.Maximum 100 are allowed per client.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - UploadFilePath (str): Upload

        Returns
        -------
        - self: This instance with matching netconfClient resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of netconfClient data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the netconfClient resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("abort", payload=payload, response_object=None)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, Arg3=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (bool):
        - Arg3 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def ClearAllLearnedSchemaInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the clearAllLearnedSchemaInfo operation on the server.

        Clear All Learned Schema Info.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearAllLearnedSchemaInfo(async_operation=bool)
        -----------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllLearnedSchemaInfo(SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllLearnedSchemaInfo(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "clearAllLearnedSchemaInfo", payload=payload, response_object=None
        )

    def ClearAllLearnedSchemaInfoInClient(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the clearAllLearnedSchemaInfoInClient operation on the server.

        Clears ALL learned info.

        clearAllLearnedSchemaInfoInClient(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "clearAllLearnedSchemaInfoInClient", payload=payload, response_object=None
        )

    def DownloadFile(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the downloadFile operation on the server.

        This will download the required files.

        downloadFile(Arg2=list, async_operation=bool)list
        -------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("downloadFile", payload=payload, response_object=None)

    def ExecuteCommandGet(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the executeCommandGet operation on the server.

        Send get command to DUT if the Netconf session is in established/ready state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        executeCommandGet(async_operation=bool)
        ---------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        executeCommandGet(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        executeCommandGet(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        executeCommandGet(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("executeCommandGet", payload=payload, response_object=None)

    def GetDecryptedCapture(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getDecryptedCapture operation on the server.

        If Enable Capture is enabled, this will fetch and open the decrypted capture for selected sessions.

        getDecryptedCapture(Arg2=list, async_operation=bool)list
        --------------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getDecryptedCapture", payload=payload, response_object=None
        )

    def GetLearnedSchemaInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getLearnedSchemaInfo operation on the server.

        Get Learned Schema Info.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getLearnedSchemaInfo(async_operation=bool)
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLearnedSchemaInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLearnedSchemaInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getLearnedSchemaInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "getLearnedSchemaInfo", payload=payload, response_object=None
        )

    def PerformActionOnAllObjects(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the performActionOnAllObjects operation on the server.

        Action on All Objects

        performActionOnAllObjects(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------------
        - Arg2 (str): Action Name
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "performActionOnAllObjects", payload=payload, response_object=None
        )

    def RestartDown(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("restartDown", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=list, async_operation=bool)
        -----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=string, async_operation=bool)
        -------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def UploadFile(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the uploadFile operation on the server.

        Required files should be uploaded.

        uploadFile(Arg2=list, Arg3=href, async_operation=bool)list
        ----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group.
        - Arg3 (obj(ixnetwork_restpy.files.Files)): Select files(s) to upload.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("uploadFile", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        CapabilitiesBase1Dot0=None,
        CapabilitiesBase1Dot1=None,
        CapabilitiesCandidate=None,
        CapabilitiesConfirmedCommit=None,
        CapabilitiesInterleave=None,
        CapabilitiesNotification=None,
        CapabilitiesRollbackOnError=None,
        CapabilitiesStartup=None,
        CapabilitiesUrl=None,
        CapabilitiesValidate=None,
        CapabilitiesWritableRunning=None,
        CapabilitiesXpath=None,
        DecryptedCapture=None,
        DoNotValidateServerResponse=None,
        EnablePassphrase=None,
        FetchSchemaInfo=None,
        OutputDirectory=None,
        Passphrase=None,
        Password=None,
        PortNumber=None,
        PrivateKeyDirectory=None,
        PrivateKeyFileName=None,
        SaveReplyXML=None,
        SchemaOutputDirectory=None,
        SendCloseOnStop=None,
        ServerIpv4Address=None,
        SshAuthenticationMechanism=None,
        UserName=None,
    ):
        """Base class infrastructure that gets a list of netconfClient device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - CapabilitiesBase1Dot0 (str): optional regex of capabilitiesBase1Dot0
        - CapabilitiesBase1Dot1 (str): optional regex of capabilitiesBase1Dot1
        - CapabilitiesCandidate (str): optional regex of capabilitiesCandidate
        - CapabilitiesConfirmedCommit (str): optional regex of capabilitiesConfirmedCommit
        - CapabilitiesInterleave (str): optional regex of capabilitiesInterleave
        - CapabilitiesNotification (str): optional regex of capabilitiesNotification
        - CapabilitiesRollbackOnError (str): optional regex of capabilitiesRollbackOnError
        - CapabilitiesStartup (str): optional regex of capabilitiesStartup
        - CapabilitiesUrl (str): optional regex of capabilitiesUrl
        - CapabilitiesValidate (str): optional regex of capabilitiesValidate
        - CapabilitiesWritableRunning (str): optional regex of capabilitiesWritableRunning
        - CapabilitiesXpath (str): optional regex of capabilitiesXpath
        - DecryptedCapture (str): optional regex of decryptedCapture
        - DoNotValidateServerResponse (str): optional regex of doNotValidateServerResponse
        - EnablePassphrase (str): optional regex of enablePassphrase
        - FetchSchemaInfo (str): optional regex of fetchSchemaInfo
        - OutputDirectory (str): optional regex of outputDirectory
        - Passphrase (str): optional regex of passphrase
        - Password (str): optional regex of password
        - PortNumber (str): optional regex of portNumber
        - PrivateKeyDirectory (str): optional regex of privateKeyDirectory
        - PrivateKeyFileName (str): optional regex of privateKeyFileName
        - SaveReplyXML (str): optional regex of saveReplyXML
        - SchemaOutputDirectory (str): optional regex of schemaOutputDirectory
        - SendCloseOnStop (str): optional regex of sendCloseOnStop
        - ServerIpv4Address (str): optional regex of serverIpv4Address
        - SshAuthenticationMechanism (str): optional regex of sshAuthenticationMechanism
        - UserName (str): optional regex of userName

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
