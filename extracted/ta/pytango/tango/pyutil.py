# SPDX-FileCopyrightText: All Contributors to the PyTango project
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
This is an internal PyTango module.
"""

__all__ = ("Util", "pyutil_init", "EnsureOmniThread", "is_omni_thread")

__docformat__ = "restructuredtext"

import os
import sys
import re
import copy

from argparse import ArgumentParser

from tango._tango import (
    Util,
    Except,
    DevFailed,
    DbDevInfo,
    EnsureOmniThread,
    is_omni_thread,
    _telemetry,
)
from tango.utils import document_method as __document_method
from tango.utils import document_static_method as __document_static_method
from tango.utils import PyTangoHelpFormatter
from tango.globals import class_list, cpp_class_list, get_constructed_classes

import collections.abc


def __simplify_device_name(dev_name):
    if dev_name.startswith("tango://"):
        dev_name = dev_name[8:]
    if dev_name.count("/") > 2:
        dev_name = dev_name[dev_name.index("/") + 1 :]
    return dev_name.lower()


#
# Methods on Util
#


def __Util__get_class_list(self):
    """
    get_class_list(self) -> seq<DeviceClass>

            Returns a list of objects of inheriting from DeviceClass

        Parameters : None

        Return     : (seq<DeviceClass>) a list of objects of inheriting from DeviceClass
    """
    return get_constructed_classes()


def __Util__create_device(self, klass_name, device_name, alias=None, cb=None):
    """
    create_device(self, klass_name, device_name, alias=None, cb=None) -> None

        Creates a new device of the given class in the database, creates a new
        DeviceImpl for it and calls init_device (just like it is done for
        existing devices when the DS starts up)

        An optional parameter callback is called AFTER the device is
        registered in the database and BEFORE the init_device for the
        newly created device is called

        Throws tango.DevFailed:
            - the device name exists already or
            - the given class is not registered for this DS.
            - the cb is not a callable

    New in PyTango 7.1.2

    Parameters :
        - klass_name : (str) the device class name
        - device_name : (str) the device name
        - alias : (str) optional alias. Default value is None meaning do not create device alias
        - cb : (callable) a callback that is called AFTER the device is registered
               in the database and BEFORE the init_device for the newly created
               device is called. Typically you may want to put device and/or attribute
               properties in the database here. The callback must receive a parameter:
               device name (str). Default value is None meaning no callback

    Return     : None"""
    if cb is not None and not isinstance(cb, collections.abc.Callable):
        Except.throw_exception(
            "PyAPI_InvalidParameter",
            "The optional cb parameter must be a python callable",
            "Util.create_device",
        )

    db = self.get_database()

    device_name = __simplify_device_name(device_name)

    device_exists = True
    try:
        db.import_device(device_name)
    except DevFailed as df:
        device_exists = not df.args[0].reason == "DB_DeviceNotDefined"

    # 1 - Make sure device name doesn't exist already in the database
    if device_exists:
        Except.throw_exception(
            "PyAPI_DeviceAlreadyDefined",
            f"The device {device_name} is already defined in the database",
            "Util.create_device",
        )

    # 2 - Make sure the device class is known
    klass_list = self.get_class_list()
    klass = None
    for k in klass_list:
        name = k.get_name()
        if name == klass_name:
            klass = k
            break
    if klass is None:
        Except.throw_exception(
            "PyAPI_UnknownDeviceClass",
            f"The device class {klass_name} could not be found",
            "Util.create_device",
        )

    # 3 - Create entry in the database (with alias if necessary)
    dev_info = DbDevInfo()
    dev_info.name = device_name
    dev_info._class = klass_name
    dev_info.server = self.get_ds_name()

    db.add_device(dev_info)

    if alias is not None:
        db.put_device_alias(device_name, alias)

    # from this point on, if anything wrong happens we need to clean the database
    try:
        # 4 - run the callback which tipically is used to initialize
        #     device and/or attribute properties in the database
        if cb is not None:
            cb(device_name)

        # 5 - Initialize device object on this server
        k.device_factory([device_name])
    except Exception:
        try:
            if alias is not None:
                db.delete_device_alias(alias)
        except Exception:
            pass
        db.delete_device(device_name)


def __Util__delete_device(self, klass_name, device_name):
    """
    delete_device(self, klass_name, device_name) -> None

        Deletes an existing device from the database and from this running
        server

        Throws tango.DevFailed:
            - the device name doesn't exist in the database
            - the device name doesn't exist in this DS.

    New in PyTango 7.1.2

    Parameters :
        - klass_name : (str) the device class name
        - device_name : (str) the device name

    Return     : None"""

    db = self.get_database()
    device_name = __simplify_device_name(device_name)
    device_exists = True
    try:
        db.import_device(device_name)
    except DevFailed as df:
        device_exists = not df.args[0].reason == "DB_DeviceNotDefined"

    # 1 - Make sure device name exists in the database
    if not device_exists:
        Except.throw_exception(
            "PyAPI_DeviceNotDefined",
            f"The device {device_name} is not defined in the database",
            "Util.delete_device",
        )

    # 2 - Make sure device name is defined in this server
    class_device_name = f"{klass_name}::{device_name}"
    ds = self.get_dserver_device()
    dev_names = ds.query_device()
    device_exists = False
    for dev_name in dev_names:
        p = dev_name.index("::")
        dev_name = dev_name[:p] + dev_name[p:].lower()
        if dev_name == class_device_name:
            device_exists = True
            break
    if not device_exists:
        Except.throw_exception(
            "PyAPI_DeviceNotDefinedInServer",
            f"The device {class_device_name} is not defined in this server",
            "Util.delete_device",
        )

    db.delete_device(device_name)

    dimpl = self.get_device_by_name(device_name)

    dc = dimpl.get_device_class()
    dc.device_destroyer(device_name)


def parse_args(args):
    parser = ArgumentParser(
        prog=os.path.splitext(args[0])[0],
        usage="%(prog)s instance_name [-v[trace level]] "
        + "[-host] [-port] [-file=<file_name> | -nodb [-dlist]]",
        add_help=False,
        formatter_class=PyTangoHelpFormatter,
    )

    parser.add_argument("instance_name", nargs="+", help="Device server instance name")
    parser.add_argument(
        "-h", "-?", "--help", action="help", help="show this help message and exit"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="count",
        help="set the trace level. "
        + "Can be used in count way: -vv or --verbose --verbose",
    )
    # this option won't be used, since we manually pop all -vN and -v N arguments, but we have to display help about it
    parser.add_argument(
        "-vLEVEL",
        dest="vn",
        action="store",
        metavar=" ",
        help="directly set the trace level to LEVEL",
    )

    parser.add_argument(
        "-file",
        "--file",
        dest="file",
        metavar="FILE_PATH",
        help="start device server using an ASCII file instead of the Tango database",
    )

    parser.add_argument(
        "-host",
        "--host",
        dest="host",
        default="0.0.0.0",
        action="store",
        help="Force the host from which server accepts requests (alternatively use ORBendPoint option)",
    )
    parser.add_argument(
        "-port",
        "--port",
        dest="port",
        default="",
        action="store",
        help="Force the port on which the device server listens (alternatively use ORBendPoint option)",
    )

    if sys.platform.startswith("win"):
        parser.add_argument(
            "-dbg",
            "--dbg",
            dest="dbg",
            action="store_true",
            default=False,
            help="Enable debug",
        )
        parser.add_argument(
            "-i",
            dest="i",
            action="store_true",
            default=False,
            help="Install the service",
        )
        parser.add_argument(
            "-s",
            dest="s",
            action="store_true",
            default=False,
            help="Install the service and choose the automatic startup mode",
        )
        parser.add_argument(
            "-u",
            dest="u",
            action="store_true",
            default=False,
            help="Uninstall the service",
        )

    group = parser.add_argument_group("Run device server without database")
    group.add_argument(
        "-nodb",
        "--nodb",
        dest="nodb",
        action="store_true",
        help="run server without DB",
    )
    group.add_argument(
        "-dlist",
        "--dlist",
        dest="dlist",
        metavar="DEV1,DEV2,etc",
        help="The device name list. This option is supported only with the -nodb option.",
    )

    group = parser.add_argument_group(
        "ORB options (started with -ORBxxx):"
        + "options directly passed to the underlying ORB. Should be rarely used"
    )

    group.add_argument(
        "-ORBendPoint",
        "--ORBendPoint",
        dest="ORBendPoint",
        action="store",
        metavar="giop:tcp:<host>:<port>",
        help="Specifying the host from which server accept "
        "requests and port on which the device server listens.",
    )

    group.add_argument(
        "-ORB<other_option>",
        "--ORB<other_option>",
        dest="ORB_not_used",
        action="store",
        metavar="other_value",
        help="Any other ORB option, e.g., -ORBtraceLevel 5",
    )

    # workaround to add arbitrary ORB options
    for arg in args:
        match = re.match(r"(-ORB|--ORB)(?P<suffix>\w+)", arg)
        if match:
            suffix = match.group("suffix")
            if suffix != "endPoint":
                arg = arg.lstrip("-")
                group.add_argument("-" + arg, "--" + arg, action="store", dest=arg)

    # since -vvvv and -v4 options are incompatible, we have to pop all -vN options
    verbose = None
    for ind, arg in enumerate(args):
        if re.match(r"-[vV][=]?\d+", arg) is not None:
            verbose = int(re.findall(r"\d+", arg)[0])
            args.remove(arg)
            break
        if len(arg) == 2 and re.match(r"-[vV]", arg) is not None:
            if ind + 1 < len(args) and re.match(r"\d+", args[ind + 1]) is not None:
                verbose = int(args[ind + 1])
                args.pop(ind + 1)
                args.remove(arg)
                break

    parsed_args = parser.parse_args(args[1:])

    if parsed_args.port and parsed_args.ORBendPoint is None:
        parsed_args.ORBendPoint = f"giop:tcp:{parsed_args.host:s}:{parsed_args.port:s}"

    if parsed_args.nodb and parsed_args.ORBendPoint is None:
        raise SystemExit(
            "-nodb option should used with [-host] -port or -ORBendPoint options"
        )

    if parsed_args.dlist is not None and not parsed_args.nodb:
        raise SystemExit("-dlist should be used only with -nodb option")

    args = [os.path.splitext(args[0])[0]]

    args += parsed_args.instance_name

    # -v4 has priority on -vvvv
    if verbose is not None:
        args += [f"-v{verbose}"]
    elif parsed_args.verbose is not None:
        args += [f"-v{parsed_args.verbose}"]

    # we add back only exist options
    for key, value in parsed_args.__dict__.items():
        if type(value) is bool:
            if value:
                args += [f"-{key:s}"]
        elif value is not None:
            if key == "file":
                args += [f"-{key:s}={value:s}"]
            elif key not in [
                "host",
                "port",
                "verbose",
                "instance_name",
                "ORB_not_used",
            ]:
                args += [f"-{key:s}", f"{value:s}"]

    return args


def __Util__init__(self, args):
    args = parse_args(copy.copy(args))
    Util.__init_orig__(self, args)


def __Util__init(args):
    args = parse_args(list(args))
    return Util.__init_orig(args)


def __Util__add_TgClass(self, klass_device_class, klass_device, device_class_name=None):
    """Register a new python tango class. Example::

        util.add_TgClass(MotorClass, Motor)
        util.add_TgClass(MotorClass, Motor, 'Motor') # equivalent to previous line

    .. deprecated:: 7.1.2
        Use :meth:`tango.Util.add_class` instead."""
    if device_class_name is None:
        device_class_name = klass_device.__name__
    class_list.append((klass_device_class, klass_device, device_class_name))


def __Util__add_Cpp_TgClass(self, device_class_name, tango_device_class_name):
    """Register a new C++ tango class.

    If there is a shared library file called MotorClass.so which
    contains a MotorClass class and a _create_MotorClass_class method. Example::

        util.add_Cpp_TgClass('MotorClass', 'Motor')

    .. note:: the parameter 'device_class_name' must match the shared
              library name.

    .. deprecated:: 7.1.2
        Use :meth:`tango.Util.add_class` instead."""
    cpp_class_list.append((device_class_name, tango_device_class_name))


def __Util__add_class(self, *args, **kwargs):
    """
    add_class(self, class<DeviceClass>, class<DeviceImpl>, language="python") -> None

        Register a new tango class ('python' or 'c++').

        If language is 'python' then args must be the same as
        :meth:`tango.Util.add_TgClass`. Otherwise, args should be the ones
        in :meth:`tango.Util.add_Cpp_TgClass`. Example::

            util.add_class(MotorClass, Motor)
            util.add_class('CounterClass', 'Counter', language='c++')

    New in PyTango 7.1.2"""
    language = kwargs.get("language", "python")
    f = self.add_TgClass
    if language != "python":
        f = self.add_Cpp_TgClass
    return f(*args)


def __init_Util():
    Util.__init_orig__ = Util.__init__
    Util.__init__ = __Util__init__
    Util.__init_orig = staticmethod(Util.init)
    Util.init = staticmethod(__Util__init)
    Util.add_TgClass = __Util__add_TgClass
    Util.add_Cpp_TgClass = __Util__add_Cpp_TgClass
    Util.add_class = __Util__add_class
    Util.get_class_list = __Util__get_class_list
    Util.create_device = __Util__create_device
    Util.delete_device = __Util__delete_device


def __doc_Util():
    Util.__doc__ = """\
    This class is a used to store TANGO device server process data and to
    provide the user with a set of utilities method.

    This class is implemented using the singleton design pattern.
    Therefore a device server process can have only one instance of this
    class and its constructor is not public. Example::

        util = tango.Util.instance()
        print(util.get_host_name())
    """

    def document_method(method_name, desc, append=True):
        return __document_method(Util, method_name, desc, append)

    def document_static_method(method_name, desc, append=True):
        return __document_static_method(Util, method_name, desc, append)

    document_static_method(
        "instance",
        """
    instance(exit = True) -> Util

           Static method that gets the singleton object reference.
           If the class has not been initialised with it's init method,
           this method prints a message and aborts the device server process.

       :param bool exit: exit or throw DevFailed

       :returns: the tango :class:`Util` object
       :rtype: :class:`Util`

       :raises: :class:`DevFailed` instead of aborting if exit is set to False
    """,
    )

    document_static_method(
        "init",
        """
    init(*args) -> Util

       Static method that creates and gets the singleton object reference.
       This method returns a reference to the object of the Util class.
       If the class singleton object has not been created, it will be instantiated

       :param str \\*args: the process commandline arguments

       :return: :class:`Util` the tango Util object
       :rtype: :class:`Util`
    """,
    )

    document_method(
        "get_device_ior",
        """
    get_device_ior(self, device) -> str

        Get the CORBA Interoperable Object Reference (IOR) associated with the device

        :param device: :class:`tango.LatestDeviceImpl` device object
        :type device: :class:`tango.LatestDeviceImpl`

        :return: the associated CORBA object reference
        :rtype: str
    """,
    )

    document_method(
        "get_dserver_ior",
        """
    get_dserver_ior(self, device_server) -> str

        Get the CORBA Interoperable Object Reference (IOR) associated with the device server

        :param device_server: :class:`DServer` device object
        :type device_server: :class:`DServer`

        :return: the associated CORBA object reference
        :rtype: str
    """,
    )

    document_method(
        "set_trace_level",
        """
    set_trace_level(self, level) -> None

            Set the process trace level.

        Parameters :
            - level : (int) the new process level
        Return     : None
    """,
    )

    document_method(
        "get_trace_level",
        """
    get_trace_level(self) -> int

            Get the process trace level.

        Parameters : None
        Return     : (int) the process trace level.
    """,
    )

    document_method(
        "get_ds_inst_name",
        """
    get_ds_inst_name(self) -> str

            Get a COPY of the device server instance name.

        Parameters : None
        Return     : (str) a COPY of the device server instance name.

        New in PyTango 3.0.4
    """,
    )

    document_method(
        "get_ds_exec_name",
        """
    get_ds_exec_name(self) -> str

            Get a COPY of the device server executable name.

        Parameters : None
        Return     : (str) a COPY of the device server executable name.

        New in PyTango 3.0.4
    """,
    )

    document_method(
        "get_ds_name",
        """
    get_ds_name(self) -> str

            Get the device server name.
            The device server name is the <device server executable name>/<the device server instance name>

        Parameters : None
        Return     : (str) device server name

        New in PyTango 3.0.4
    """,
    )

    document_method(
        "get_host_name",
        """
    get_host_name(self) -> str

            Get the host name where the device server process is running.

        Parameters : None
        Return     : (str) the host name where the device server process is running

        New in PyTango 3.0.4
    """,
    )

    document_method(
        "get_pid_str",
        """
    get_pid_str(self) -> str

            Get the device server process identifier as a string.

        Parameters : None
        Return     : (str) the device server process identifier as a string

        New in PyTango 3.0.4
    """,
    )

    document_method(
        "get_pid",
        """
    get_pid(self) -> TangoSys_Pid

            Get the device server process identifier.

        Parameters : None
        Return     : (int) the device server process identifier
    """,
    )

    document_method(
        "get_tango_lib_release",
        """
    get_tango_lib_release(self) -> int

            Get the TANGO library version number.

        Parameters : None
        Return     : (int) The Tango library release number coded in
                     3 digits (for instance 550,551,552,600,....)
    """,
    )

    document_method(
        "get_version_str",
        """
    get_version_str(self) -> str

            Get the IDL TANGO version.

        Parameters : None
        Return     : (str) the IDL TANGO version.

        New in PyTango 3.0.4
    """,
    )

    document_method(
        "get_server_version",
        """
    get_server_version(self) -> str

            Get the device server version.

        Parameters : None
        Return     : (str) the device server version.
    """,
    )

    document_method(
        "set_server_version",
        """
    set_server_version(self, vers) -> None

            Set the device server version.

        Parameters :
            - vers : (str) the device server version
        Return     : None
    """,
    )

    document_method(
        "set_serial_model",
        """
    set_serial_model(self, ser) -> None

            Set the serialization model.

        Parameters :
            - ser : (SerialModel) the new serialization model. The serialization model must
                    be one of BY_DEVICE, BY_CLASS, BY_PROCESS or NO_SYNC
        Return     : None
    """,
    )

    document_method(
        "get_serial_model",
        """
    get_serial_model(self) ->SerialModel

            Get the serialization model.

        Parameters : None
        Return     : (SerialModel) the serialization model
    """,
    )

    document_method(
        "connect_db",
        """
    connect_db(self) -> None

            Connect the process to the TANGO database.
            If the connection to the database failed, a message is
            displayed on the screen and the process is aborted

        Parameters : None
        Return     : None
    """,
    )

    document_method(
        "reset_filedatabase",
        """
    reset_filedatabase(self) -> None

            Reread the file database.

        Parameters : None
        Return     : None
    """,
    )

    document_method(
        "unregister_server",
        """
    unregister_server(self) -> None

            Unregister a device server process from the TANGO database.

        Parameters : None
        Return     : None
    """,
    )

    document_method(
        "get_dserver_device",
        """
    get_dserver_device(self) -> DServer

            Get a reference to the dserver device attached to the device server process.

        Parameters : None
        Return     : (DServer) the dserver device attached to the device server process

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "server_init",
        """
    server_init(self, with_window = False) -> None

            Initialize all the device server pattern(s) embedded in a device server process.

        Parameters :
            - with_window : (bool) default value is False
        Return     : None

        Throws     : DevFailed If the device pattern initialistaion failed
    """,
    )

    document_method(
        "server_run",
        """
    server_run(self) -> None

            Run the CORBA event loop.
            This method runs the CORBA event loop. For UNIX or Linux operating system,
            this method does not return. For Windows in a non-console mode, this method
            start a thread which enter the CORBA event loop.

        Parameters : None
        Return     : None
    """,
    )

    # TODO finish documentation
    document_method(
        "orb_run",
        """
    orb_run(self) -> None

            Run the CORBA event loop directly (EXPERT FEATURE!)

            This method runs the CORBA event loop.  It may be useful if the
            Util.server_run method needs to be bypassed.  Normally, that method
            runs the CORBA event loop.

        Parameters : None
        Return     : None
    """,
    )

    document_method(
        "trigger_cmd_polling",
        """
    trigger_cmd_polling(self, dev, name) -> None

            Trigger polling for polled command.
            This method send the order to the polling thread to poll one object registered
            with an update period defined as "externally triggerred"

        Parameters :
            - dev : (DeviceImpl) the TANGO device
            - name : (str) the command name which must be polled
        Return     : None

        Throws     : DevFailed If the call failed
    """,
    )

    document_method(
        "trigger_attr_polling",
        """
    trigger_attr_polling(self, dev, name) -> None

            Trigger polling for polled attribute.
            This method send the order to the polling thread to poll one object registered
            with an update period defined as "externally triggerred"

        Parameters :
            - dev : (DeviceImpl) the TANGO device
            - name : (str) the attribute name which must be polled
        Return     : None
    """,
    )

    document_method(
        "set_polling_threads_pool_size",
        """
    set_polling_threads_pool_size(self, thread_nb) -> None

            Set the polling threads pool size.

        Parameters :
            - thread_nb : (int) the maximun number of threads in the polling threads pool
        Return     : None

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "get_polling_threads_pool_size",
        """
    get_polling_threads_pool_size(self) -> int

            Get the polling threads pool size.

        Parameters : None
        Return     : (int) the maximun number of threads in the polling threads pool
    """,
    )

    document_method(
        "is_svr_starting",
        """
    is_svr_starting(self) -> bool

            Check if the device server process is in its starting phase

        Parameters : None
        Return     : (bool) True if the server is in its starting phase

        New in PyTango 8.0.0
    """,
    )

    document_method(
        "is_svr_shutting_down",
        """
    is_svr_shutting_down(self) -> bool

            Check if the device server process is in its shutting down sequence

        Parameters : None
        Return     : (bool) True if the server is in its shutting down phase.

        New in PyTango 8.0.0
    """,
    )

    document_method(
        "is_device_restarting",
        """
    is_device_restarting(self, (str)dev_name) -> bool

            Check if the device is actually restarted by the device server
            process admin device with its DevRestart command

        Parameters :
            dev_name : (str) device name
        Return     : (bool) True if the device is restarting.

        New in PyTango 8.0.0
    """,
    )

    document_method(
        "get_sub_dev_diag",
        """
    get_sub_dev_diag(self) -> SubDevDiag

            Get the internal sub device manager

        Parameters : None
        Return     : (SubDevDiag) the sub device manager

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "reset_filedatabase",
        """
    reset_filedatabase(self) -> None

            Reread the file database

        Parameters : None
        Return     : None

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "get_database",
        """
    get_database(self) -> Database

            Get a reference to the TANGO database object

        Parameters : None
        Return     : (Database) the database

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "unregister_server",
        """
    unregister_server(self) -> None

            Unregister a device server process from the TANGO database.
            If the database call fails, a message is displayed on the screen
            and the process is aborted

        Parameters : None
        Return     : None

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "get_device_list_by_class",
        """
    get_device_list_by_class(self, class_name) -> sequence<DeviceImpl>

            Get the list of device references for a given TANGO class.
            Return the list of references for all devices served by one implementation
            of the TANGO device pattern implemented in the process.

        Parameters :
            - class_name : (str) The TANGO device class name

        Return     : (sequence<DeviceImpl>) The device reference list

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "get_device_by_name",
        """
    get_device_by_name(self, dev_name) -> DeviceImpl

            Get a device reference from its name

        Parameters :
            - dev_name : (str) The TANGO device name
        Return     : (DeviceImpl) The device reference

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "get_dserver_device",
        """
    get_dserver_device(self) -> DServer

            Get a reference to the dserver device attached to the device server process

        Parameters : None
        Return     : (DServer) A reference to the dserver device

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "get_device_list",
        """
    get_device_list(self) -> sequence<DeviceImpl>

            Get device list from name.
            It is possible to use a wild card ('*') in the name parameter
            (e.g. "*", "/tango/tangotest/n*", ...)

        Parameters : None
        Return     : (sequence<DeviceImpl>) the list of device objects

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "server_set_event_loop",
        """
    server_set_event_loop(self, event_loop) -> None

        This method registers an event loop function in a Tango server.
        This function will be called by the process main thread in an infinite loop
        The process will not use the classical ORB blocking event loop.
        It is the user responsability to code this function in a way that it implements
        some kind of blocking in order not to load the computer CPU. The following
        piece of code is an example of how you can use this feature::

            _LOOP_NB = 1
            def looping():
                global _LOOP_NB
                print "looping", _LOOP_NB
                time.sleep(0.1)
                _LOOP_NB += 1
                return _LOOP_NB > 100

            def main():
                util = tango.Util(sys.argv)

                # ...

                U = tango.Util.instance()
                U.server_set_event_loop(looping)
                U.server_init()
                U.server_run()

        Parameters : None
        Return     : None

        New in PyTango 8.1.0
    """,
    )

    # TODO finish documentation
    # document_method("set_interceptors", """
    # set_interceptors(self) -> None
    #
    #     TODO DOCU
    #
    # """)

    document_static_method(
        "set_use_db",
        """
    set_use_db(self) -> None

       Set the database use Tango::Util::_UseDb flag.
       Implemented for device server started without database usage.

       Use with extreme care!

    """,
    )

    document_method(
        "server_cleanup",
        """
    server_cleanup(self) -> None

        Release device server resources (EXPERT FEATURE!)

        This method cleans up the Tango device server and relinquishes
        all computer resources before the process exits.  It is
        unnecessary to call this, unless Util.server_run has been bypassed.

    """,
    )

    document_method(
        "is_auto_alarm_on_change_event",
        """
    is_auto_alarm_on_change_event(self) -> bool

        Returns True if alarm events are automatically pushed to subscribers when a device
        pushes a change event, and the attribute quality has changed to or from alarm.

        Can be configured in two ways:

          - via the ``CtrlSystem`` free Tango database property
            ``AutoAlarmOnChangeEvent`` (set to true or false),
          - by calling the :meth:`tango.Util.set_auto_alarm_on_change_event`.

        Parameters : None
        Return     : bool

        .. versionadded:: 10.0.0
    """,
    )

    document_method(
        "set_auto_alarm_on_change_event",
        """
    set_auto_alarm_on_change_event(self, bool) -> None

        Toggles if alarm events are automatically pushed - see
        :meth:`tango.Util.is_auto_alarm_on_change_event`.

        This method takes priority over the value of the free property in the Tango database.

        Parameters : bool
        Return     : None

        .. versionadded:: 10.0.0
    """,
    )


#
# EnsureOmniThread context handler
#


def __EnsureOmniThread__enter__(self):
    self._acquire()
    return self


def __EnsureOmniThread__exit__(self, exc_type, exc_value, traceback):
    self._release()
    return False


def __init_EnsureOmniThread():
    EnsureOmniThread.__enter__ = __EnsureOmniThread__enter__
    EnsureOmniThread.__exit__ = __EnsureOmniThread__exit__


def __doc_EnsureOmniThread():
    EnsureOmniThread.__doc__ = """\

    Tango servers and clients that start their own additional threads
    that will interact with Tango must guard these threads within this
    Python context.  This is especially important when working with
    event subscriptions, and pushing events.

    This context handler class ensures a non-omniORB thread will still
    get a dummy omniORB thread ID - cppTango requires threads to
    be identifiable in this way.  It should only be acquired once for
    the lifetime of the thread, and must be released before the thread
    is cleaned up.

    Here is an example::

        import tango
        from threading import Thread
        from time import sleep


        def my_thread_run():
            with tango.EnsureOmniThread():
                eid = dp.subscribe_event(
                    "double_scalar", tango.EventType.PERIODIC_EVENT, cb)
                while running:
                    print(f"num events stored {len(cb.get_events())}")
                    sleep(1)
                dp.unsubscribe_event(eid)


        cb = tango.utils.EventCallback()  # print events to stdout
        dp = tango.DeviceProxy("sys/tg_test/1")
        dp.poll_attribute("double_scalar", 1000)
        thread = Thread(target=my_thread_run)
        running = True
        thread.start()
        sleep(5)
        running = False
        thread.join()

    .. versionadded:: 9.3.2
    """


def __doc_is_omni_thread():
    is_omni_thread.__doc__ = """\

    Determines if the calling thread is (or looks like) an omniORB thread.
    This includes user threads that have a dummy omniORB thread ID, such
    as that provided by EnsureOmniThread.

        Parameters : None

        Return     : (bool) True if the calling thread is an omnithread.

    New in PyTango 9.3.2
    """


#
# TraceContextScope context handler
#


def __TraceContextScope__enter__(self):
    self._acquire()
    return self


def __TraceContextScope__exit__(self, exc_type, exc_value, traceback):
    self._release()
    return False


def __init_TraceContextScope():
    _telemetry.TraceContextScope.__enter__ = __TraceContextScope__enter__
    _telemetry.TraceContextScope.__exit__ = __TraceContextScope__exit__


def __doc_TraceContextScope():
    _telemetry.TraceContextScope.__doc__ = """\

    Internal - for telemetry tracing purposes.

    Used to propagate the Python OpenTelemetry context to the cppTango telemetry context.
    When the context handler is entered, a new span is created.  During this process, the
    the current cppTango context is stored before the new span is set as the active scope.
    When the context handler exists, the span ends and the old context is restored at the
    C++ level.

    trace_parent and trace_state strings encoded as per the W3C standard: https://www.w3.org/TR/trace-context/

    with tango._telemetry.TraceContextScope(new_span_name, trace_parent, trace_state):
        x = proxy.read_attribute("foo")

    This is a no-op if telemetry support isn't compiled into cppTango (check tango.constants.TANGO_USE_TELEMETRY)

    .. versionadded:: 10.0.0
    """


def pyutil_init(doc=True):
    __init_Util()
    __init_EnsureOmniThread()
    __init_TraceContextScope()
    if doc:
        __doc_Util()
        __doc_EnsureOmniThread()
        __doc_is_omni_thread()
        __doc_TraceContextScope()
