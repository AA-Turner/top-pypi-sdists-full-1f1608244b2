# SPDX-FileCopyrightText: All Contributors to the PyTango project
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
This is an internal PyTango module.
"""


import copy
import functools
import inspect
import os
import sys
import types
import warnings

from tango._tango import (
    DeviceImpl,
    Device_3Impl,
    Device_4Impl,
    Device_5Impl,
    Device_6Impl,
    DevFailed,
    Attribute,
    WAttribute,
    AttrWriteType,
    MultiAttribute,
    MultiClassAttribute,
    Attr,
    Logger,
    AttrDataFormat,
    DispLevel,
    UserDefaultAttrProp,
    StdStringVector,
    Except,
    constants,
)
from tango.pyutil import Util
from tango.release import Release
from tango.utils import document_method as __document_method
from tango.utils import (
    copy_doc,
    get_latest_device_class,
    set_complex_value,
    is_pure_str,
    parse_type_hint,
    get_attribute_type_format,
    _force_tracing,
    _forcefully_traced_method,
    _get_non_tango_source_location,
    PyTangoUserWarning,
)
from tango.green import get_executor
from tango.attr_data import AttrData

from tango.log4tango import TangoStream

__docformat__ = "restructuredtext"

__all__ = (
    "ChangeEventProp",
    "PeriodicEventProp",
    "ArchiveEventProp",
    "AttributeAlarm",
    "EventProperties",
    "AttributeConfig",
    "AttributeConfig_2",
    "AttributeConfig_3",
    "AttributeConfig_5",
    "MultiAttrProp",
    "device_server_init",
)

# Worker access

_WORKER = get_executor()


def set_worker(worker):
    global _WORKER
    _WORKER = worker


def get_worker():
    return _WORKER


# patcher for methods
def run_in_executor(fn):
    if not hasattr(fn, "wrapped_with_executor"):

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return get_worker().execute(fn, *args, **kwargs)

        # to avoid double wrapping we add an empty field, and then use it to check, whether function is already wrapped
        wrapper.wrapped_with_executor = True
        return wrapper
    else:
        return fn


def get_source_location(source=None):
    """Helper function that provides source location for logging functions.
    :param source:
        (optional) Method or function, which will be unwrapped of decorated wrappers
        and inspected for location. If not provided - current stack will be used to deduce the location.
    :type source: Callable

    :return:
        Tuple (filename, lineno)
    :rtype :tuple:
    """
    location = _get_non_tango_source_location(source)
    filename = os.path.basename(location.filepath)
    return filename, location.lineno


class _InterfaceDefinedByIDL:
    _initialized = False

    def __setattr__(self, name, value):
        if name not in self.__dict__ and self._initialized:
            warnings.warn(
                f"Attribute {repr(name)} is not supported by Tango IDL "
                f"struct {self.__class__.__name__} - it will be ignored.",
                category=PyTangoUserWarning,
            )

        return super().__setattr__(name, value)


# Note: the inheritance below doesn't call get_latest_device_class(),
#       because such dynamic inheritance breaks auto-completion in IDEs.
#       Instead, we manually provide the correct class here, and verify
#       that the inheritance is correct via a unit test, in test_server.py.
class LatestDeviceImpl(Device_6Impl):
    __doc__ = f"""\
    Latest implementation of the TANGO device base class (alias for {get_latest_device_class().__name__}).

    It inherits from CORBA classes where all the network layer is implemented.
    """

    def __init__(self, *args):
        super().__init__(*args)
        # Set up python related versions for DevInfo
        self.add_version_info("PyTango", Release.version_long)
        self.add_version_info("Build.PyTango.Python", constants.Compile.PY_VERSION)
        self.add_version_info("Build.PyTango.cppTango", constants.Compile.TANGO_VERSION)
        self.add_version_info("Build.PyTango.NumPy", constants.Compile.NUMPY_VERSION)
        self.add_version_info("Build.PyTango.Boost", constants.Compile.BOOST_VERSION)
        self.add_version_info("Python", constants.Runtime.PY_VERSION)
        self.add_version_info("NumPy", constants.Runtime.NUMPY_VERSION)


class AttributeAlarm(_InterfaceDefinedByIDL):
    """This class represents the python interface for the Tango IDL object
    AttributeAlarm."""

    def __init__(self):
        self.min_alarm = ""
        self.max_alarm = ""
        self.min_warning = ""
        self.max_warning = ""
        self.delta_t = ""
        self.delta_val = ""
        self.extensions = []
        self._initialized = True


class ChangeEventProp(_InterfaceDefinedByIDL):
    """This class represents the python interface for the Tango IDL object
    ChangeEventProp."""

    def __init__(self):
        self.rel_change = ""
        self.abs_change = ""
        self.extensions = []
        self._initialized = True


class PeriodicEventProp(_InterfaceDefinedByIDL):
    """This class represents the python interface for the Tango IDL object
    PeriodicEventProp."""

    def __init__(self):
        self.period = ""
        self.extensions = []
        self._initialized = True


class ArchiveEventProp(_InterfaceDefinedByIDL):
    """This class represents the python interface for the Tango IDL object
    ArchiveEventProp."""

    def __init__(self):
        self.rel_change = ""
        self.abs_change = ""
        self.period = ""
        self.extensions = []
        self._initialized = True


class EventProperties(_InterfaceDefinedByIDL):
    """This class represents the python interface for the Tango IDL object
    EventProperties."""

    def __init__(self):
        self.ch_event = ChangeEventProp()
        self.per_event = PeriodicEventProp()
        self.arch_event = ArchiveEventProp()
        self._initialized = True


class MultiAttrProp(_InterfaceDefinedByIDL):
    """This class represents the python interface for the Tango IDL object
    MultiAttrProp."""

    def __init__(self):
        self.label = ""
        self.description = ""
        self.unit = ""
        self.standard_unit = ""
        self.display_unit = ""
        self.format = ""
        self.min_value = ""
        self.max_value = ""
        self.min_alarm = ""
        self.max_alarm = ""
        self.min_warning = ""
        self.max_warning = ""
        self.delta_t = ""
        self.delta_val = ""
        self.event_period = ""
        self.archive_period = ""
        self.rel_change = ""
        self.abs_change = ""
        self.archive_rel_change = ""
        self.archive_abs_change = ""
        self._initialized = True


def _init_attr_config(attr_cfg):
    """Helper function to initialize attribute config objects"""
    attr_cfg.name = ""
    attr_cfg.writable = AttrWriteType.READ
    attr_cfg.data_format = AttrDataFormat.SCALAR
    attr_cfg.data_type = 0
    attr_cfg.max_dim_x = 0
    attr_cfg.max_dim_y = 0
    attr_cfg.description = ""
    attr_cfg.label = ""
    attr_cfg.unit = ""
    attr_cfg.standard_unit = ""
    attr_cfg.display_unit = ""
    attr_cfg.format = ""
    attr_cfg.min_value = ""
    attr_cfg.max_value = ""
    attr_cfg.writable_attr_name = ""
    attr_cfg.extensions = []


class AttributeConfig(_InterfaceDefinedByIDL):
    """This class represents the python interface for the Tango IDL object
    AttributeConfig."""

    def __init__(self):
        _init_attr_config(self)
        self.min_alarm = ""
        self.max_alarm = ""
        self._initialized = True


class AttributeConfig_2(_InterfaceDefinedByIDL):
    """This class represents the python interface for the Tango IDL object
    AttributeConfig_2."""

    def __init__(self):
        _init_attr_config(self)
        self.level = DispLevel.OPERATOR
        self.min_alarm = ""
        self.max_alarm = ""
        self._initialized = True


class AttributeConfig_3(_InterfaceDefinedByIDL):
    """This class represents the python interface for the Tango IDL object
    AttributeConfig_3."""

    def __init__(self):
        _init_attr_config(self)
        self.level = -1
        self.att_alarm = AttributeAlarm()
        self.event_prop = EventProperties()
        self.sys_extensions = []
        self._initialized = True


class AttributeConfig_5(_InterfaceDefinedByIDL):
    """This class represents the python interface for the Tango IDL object
    AttributeConfig_5."""

    def __init__(self):
        _init_attr_config(self)
        self.memorized = False
        self.mem_init = False
        self.level = -1
        self.root_attr_name = ""
        self.enum_labels = []
        self.att_alarm = AttributeAlarm()
        self.event_prop = EventProperties()
        self.sys_extensions = []
        self._initialized = True


def __Attribute__get_properties(self, attr_cfg=None):
    """
    get_properties(self, attr_cfg = None) -> AttributeConfig

        Get attribute properties.

        :param conf: the config object to be filled with
                     the attribute configuration. Default is None meaning the
                     method will create internally a new AttributeConfig_5
                     and return it.
                     Can be AttributeConfig, AttributeConfig_2,
                     AttributeConfig_3, AttributeConfig_5 or
                     MultiAttrProp

        :returns: the config object filled with attribute configuration information
        :rtype: AttributeConfig

        New in PyTango 7.1.4
    """

    if attr_cfg is None:
        attr_cfg = MultiAttrProp()
    if not isinstance(attr_cfg, MultiAttrProp):
        raise TypeError("attr_cfg must be an instance of MultiAttrProp")
    return self._get_properties_multi_attr_prop(attr_cfg)


def __Attribute__set_properties(self, attr_cfg, dev=None):
    """
    set_properties(self, attr_cfg, dev)

        Set attribute properties.

        This method sets the attribute properties value with the content
        of the fields in the AttributeConfig/ AttributeConfig_3 object

        :param conf: the config object.
        :type conf: AttributeConfig or AttributeConfig_3
        :param dev: the device (not used, maintained
                    for backward compatibility)
        :type dev: DeviceImpl

        New in PyTango 7.1.4
    """

    if not isinstance(attr_cfg, MultiAttrProp):
        raise TypeError("attr_cfg must be an instance of MultiAttrProp")
    return self._set_properties_multi_attr_prop(attr_cfg)


def __Attribute__str(self):
    return f"{self.__class__.__name__}({self.get_name()})"


def __Attribute__set_value(self, *args):
    """
    .. function:: set_value(self, data)
                  set_value(self, str_data, data)
                  DEPRECATED:  set_value(self, data, dim_x = 1, dim_y = 0)
        :noindex:

    Set internal attribute value.

    This method stores the attribute read value inside the object.
    This method also stores the date when it is called and initializes the
    attribute quality factor.

    :param data: the data to be set. Data must be compatible with the attribute type and format.
                 In the DEPRECATED form for SPECTRUM and IMAGE attributes, data
                 can be any type of FLAT sequence of elements compatible with the
                 attribute type.
                 In the new form (without dim_x or dim_y) data should be any
                 sequence for SPECTRUM and a SEQUENCE of equal-length SEQUENCES
                 for IMAGE attributes.
                 The recommended sequence is a C continuous and aligned numpy
                 array, as it can be optimized.
    :param str_data: special variation for DevEncoded data type. In this case 'data' must
                     be a str or an object with the buffer interface.
    :type str_data: str
    :param dim_x: [DEPRECATED] the attribute x length. Default value is 1
    :type dim_x: int
    :param dim_y: [DEPRECATED] the attribute y length. Default value is 0
    :type dim_y: int
    """

    if not len(args):
        raise TypeError("set_value method must be called with at least one argument!")

    for arg in args:
        if arg is None:
            raise TypeError("set_value method cannot be called with None!")

    self._set_value(*args)


def __Attribute__set_value_date_quality(self, *args):
    """
    .. function::   set_value_date_quality(self, data, time_stamp, quality)
                    set_value_date_quality(self, str_data, data, time_stamp, quality)
                    DEPRECATED:  set_value_date_quality(self, data, time_stamp, quality, dim_x = 1, dim_y = 0)
        :noindex:

    Set internal attribute value, date and quality factor.

    This method stores the attribute read value, the date and the attribute quality
    factor inside the object.

    :param data: the data to be set. Data must be compatible with the attribute type and format.
                 In the DEPRECATED form for SPECTRUM and IMAGE attributes, data
                 can be any type of FLAT sequence of elements compatible with the
                 attribute type.
                 In the new form (without dim_x or dim_y) data should be any
                 sequence for SPECTRUM and a SEQUENCE of equal-length SEQUENCES
                 for IMAGE attributes.
                 The recommended sequence is a C continuous and aligned numpy
                 array, as it can be optimized.
    :param str_data: special variation for DevEncoded data type. In this case 'data' must
                     be a str or an object with the buffer interface.
    :type str_data: str
    :param time_stamp: the time stamp
    :type time_stamp: double
    :param quality: the attribute quality factor
    :type quality: AttrQuality
    :param dim_x: [DEPRECATED] the attribute x length. Default value is 1
    :type dim_x: int
    :param dim_y: [DEPRECATED] the attribute y length. Default value is 0
    :type dim_y: int
    """

    if len(args) < 3:
        raise TypeError(
            "set_value_date_quality method must be called with at least three arguments!"
        )

    for arg in args:
        if arg is None:
            raise TypeError("set_value_date_quality method cannot be called with None!")

    self._set_value_date_quality(*args)


def __init_Attribute():
    Attribute.__str__ = __Attribute__str
    Attribute.__repr__ = __Attribute__str
    Attribute.get_properties = __Attribute__get_properties
    Attribute.set_properties = __Attribute__set_properties

    Attribute.set_value = __Attribute__set_value
    Attribute.set_value_date_quality = __Attribute__set_value_date_quality


def __DeviceImpl__get_device_class(self):
    """
    get_device_class(self)

        Get device class singleton.

        :returns: the device class singleton (device_class field)
        :rtype: DeviceClass

    """
    try:
        return self._device_class_instance
    except AttributeError:
        return None


def __DeviceImpl__get_device_properties(self, ds_class=None):
    """
    get_device_properties(self, ds_class = None)

        Utility method that fetches all the device properties from the database
        and converts them into members of this DeviceImpl.

        :param ds_class: the DeviceClass object. Optional. Default value is
                         None meaning that the corresponding DeviceClass object for this
                         DeviceImpl will be used
        :type ds_class: DeviceClass

        :raises DevFailed:
    """
    if ds_class is None:
        try:
            # Call this method in a try/except in case this is called during the DS shutdown sequence
            ds_class = self.get_device_class()
        except Exception:
            return
    try:
        pu = self.prop_util = ds_class.prop_util
        self.device_property_list = copy.deepcopy(ds_class.device_property_list)
        class_prop = ds_class.class_property_list
        pu.get_device_properties(self, class_prop, self.device_property_list)
        for prop_name in class_prop:
            setattr(self, prop_name, pu.get_property_values(prop_name, class_prop))
        for prop_name in self.device_property_list:
            setattr(
                self,
                prop_name,
                self.prop_util.get_property_values(
                    prop_name, self.device_property_list
                ),
            )
    except DevFailed as df:
        print(80 * "-")
        print(df)
        raise df


def __DeviceImpl__add_attribute(
    self, attr, r_meth=None, w_meth=None, is_allo_meth=None
):
    """
    add_attribute(self, attr, r_meth=None, w_meth=None, is_allo_meth=None) -> Attr

        Add a new attribute to the device attribute list.

        Please, note that if you add
        an attribute to a device at device creation time, this attribute will be added
        to the device class attribute list. Therefore, all devices belonging to the
        same class created after this attribute addition will also have this attribute.

        If you pass a reference to unbound method for read, write or is_allowed method
        (e.g. DeviceClass.read_function or self.__class__.read_function),
        during execution the corresponding bound method (self.read_function) will be used.

        Note: Calling the synchronous add_attribute method from a coroutine function in
        an asyncio server may cause a deadlock.
        Use ``await`` :meth:`async_add_attribute` instead.
        However, if overriding the synchronous method ``initialize_dynamic_attributes``,
        then the synchronous add_attribute method must be used, even in asyncio servers.

        :param attr: the new attribute to be added to the list.
        :type attr: server.attribute or Attr or AttrData
        :param r_meth: the read method to be called on a read request
                       (if attr is of type server.attribute, then use the
                       fget field in the attr object instead)
        :type r_meth: callable
        :param w_meth: the write method to be called on a write request
                       (if attr is writable)
                       (if attr is of type server.attribute, then use the
                       fset field in the attr object instead)
        :type w_meth: callable
        :param is_allo_meth: the method that is called to check if it
                             is possible to access the attribute or not
                             (if attr is of type server.attribute, then use the
                             fisallowed field in the attr object instead)
        :type is_allo_meth: callable

        :returns: the newly created attribute.
        :rtype: Attr

        :raises DevFailed:
    """

    return __DeviceImpl__add_attribute_realization(
        self, attr, r_meth, w_meth, is_allo_meth
    )


async def __DeviceImpl__async_add_attribute(
    self, attr, r_meth=None, w_meth=None, is_allo_meth=None
):
    """
    async_add_attribute(self, attr, r_meth=None, w_meth=None, is_allo_meth=None) -> Attr

        Add a new attribute to the device attribute list.

        Please, note that if you add
        an attribute to a device at device creation time, this attribute will be added
        to the device class attribute list. Therefore, all devices belonging to the
        same class created after this attribute addition will also have this attribute.

        If you pass a reference to unbound method for read, write or is_allowed method
        (e.g. DeviceClass.read_function or self.__class__.read_function),
        during execution the corresponding bound method (self.read_function) will be used.

        :param attr: the new attribute to be added to the list.
        :type attr: server.attribute or Attr or AttrData
        :param r_meth: the read method to be called on a read request
                       (if attr is of type server.attribute, then use the
                       fget field in the attr object instead)
        :type r_meth: callable
        :param w_meth: the write method to be called on a write request
                       (if attr is writable)
                       (if attr is of type server.attribute, then use the
                       fset field in the attr object instead)
        :type w_meth: callable
        :param is_allo_meth: the method that is called to check if it
                             is possible to access the attribute or not
                             (if attr is of type server.attribute, then use the
                             fisallowed field in the attr object instead)
        :type is_allo_meth: callable

        :returns: the newly created attribute.
        :rtype: Attr

        :raises DevFailed:

        .. versionadded:: 10.0.0
    """

    return await get_worker().delegate(
        __DeviceImpl__add_attribute_realization,
        self,
        attr,
        r_meth,
        w_meth,
        is_allo_meth,
    )


def __DeviceImpl__add_attribute_realization(self, attr, r_meth, w_meth, is_allo_meth):
    attr_data = None
    type_hint = None

    if isinstance(attr, AttrData):
        attr_data = attr
        attr = attr.to_attr()

    att_name = attr.get_name()

    # get read method and its name
    r_name = f"read_{att_name}"
    if r_meth is None:
        if attr_data is not None:
            r_name = attr_data.read_method_name
        if hasattr(attr_data, "fget"):
            r_meth = attr_data.fget
        elif hasattr(self, r_name):
            r_meth = getattr(self, r_name)
    else:
        r_name = r_meth.__name__

    # patch it if attribute is readable
    if attr.get_writable() in (
        AttrWriteType.READ,
        AttrWriteType.READ_WRITE,
        AttrWriteType.READ_WITH_WRITE,
    ):
        type_hint = dict(r_meth.__annotations__).get("return", None)
        r_name = f"__wrapped_read_{att_name}_{r_name}__"
        r_meth_green_mode = getattr(attr_data, "read_green_mode", True)
        __patch_device_with_dynamic_attribute_read_method(
            self, r_name, r_meth, r_meth_green_mode
        )

    # get write method and its name
    w_name = f"write_{att_name}"
    if w_meth is None:
        if attr_data is not None:
            w_name = attr_data.write_method_name
        if hasattr(attr_data, "fset"):
            w_meth = attr_data.fset
        elif hasattr(self, w_name):
            w_meth = getattr(self, w_name)
    else:
        w_name = w_meth.__name__

    # patch it if attribute is writable
    if attr.get_writable() in (
        AttrWriteType.WRITE,
        AttrWriteType.READ_WRITE,
        AttrWriteType.READ_WITH_WRITE,
    ):
        type_hints = dict(w_meth.__annotations__)
        if type_hint is None and type_hints:
            type_hint = list(type_hints.values())[-1]

        w_name = f"__wrapped_write_{att_name}_{w_name}__"
        w_meth_green_mode = getattr(attr_data, "write_green_mode", True)
        __patch_device_with_dynamic_attribute_write_method(
            self, w_name, w_meth, w_meth_green_mode
        )

    # get is allowed method and its name
    ia_name = f"is_{att_name}_allowed"
    if is_allo_meth is None:
        if attr_data is not None:
            ia_name = attr_data.is_allowed_name
        if hasattr(attr_data, "fisallowed"):
            is_allo_meth = attr_data.fisallowed
        elif hasattr(self, ia_name):
            is_allo_meth = getattr(self, ia_name)
    else:
        ia_name = is_allo_meth.__name__

    # patch it if exists
    if is_allo_meth is not None:
        ia_name = f"__wrapped_is_allowed_{att_name}_{ia_name}__"
        ia_meth_green_mode = getattr(attr_data, "isallowed_green_mode", True)
        __patch_device_with_dynamic_attribute_is_allowed_method(
            self, ia_name, is_allo_meth, ia_meth_green_mode
        )

    if attr_data and type_hint:
        if not attr_data.has_dtype_kword:
            dtype, dformat, max_x, max_y = parse_type_hint(
                type_hint, caller="attribute"
            )
            if dformat is None:
                if attr_data.attr_format not in [
                    AttrDataFormat.IMAGE,
                    AttrDataFormat.SPECTRUM,
                ]:
                    raise RuntimeError(
                        "For numpy.ndarrays AttrDataFormat has to be specified"
                    )
                dformat = attr_data.attr_format

            dtype, dformat, enum_labels = get_attribute_type_format(
                dtype, dformat, None
            )
            attr_data.attr_type = dtype
            attr_data.attr_format = dformat
            if enum_labels:
                attr_data.set_enum_labels_to_attr_prop(enum_labels)
            if not attr_data.has_size_kword:
                if max_x:
                    attr_data.dim_x = max_x
                if max_y:
                    attr_data.dim_y = max_y

            attr = attr_data.to_attr()

    self._add_attribute(attr, r_name, w_name, ia_name)
    return attr


def __patch_device_with_dynamic_attribute_read_method(
    device, name, r_meth, r_meth_green_mode
):
    if __is_device_method(device, r_meth):
        if r_meth_green_mode:

            @functools.wraps(r_meth)
            def read_attr(device, attr):
                worker = get_worker()
                # already bound to device, so exclude device arg
                ret = worker.execute(r_meth, attr)
                if not attr.get_value_flag() and ret is not None:
                    set_complex_value(attr, ret)
                return ret

        else:

            @functools.wraps(r_meth)
            def read_attr(device, attr):
                ret = r_meth(attr)
                if not attr.get_value_flag() and ret is not None:
                    set_complex_value(attr, ret)
                return ret

    else:
        if r_meth_green_mode:

            @functools.wraps(r_meth)
            def read_attr(device, attr):
                worker = get_worker()
                # unbound function or not on device object, so include device arg
                ret = worker.execute(r_meth, device, attr)
                if not attr.get_value_flag() and ret is not None:
                    set_complex_value(attr, ret)
                return ret

        else:

            @functools.wraps(r_meth)
            def read_attr(device, attr):
                ret = r_meth(device, attr)
                if not attr.get_value_flag() and ret is not None:
                    set_complex_value(attr, ret)
                return ret

    if _force_tracing:
        read_attr = _forcefully_traced_method(read_attr)

    bound_method = types.MethodType(read_attr, device)
    setattr(device, name, bound_method)


def __patch_device_with_dynamic_attribute_write_method(
    device, name, w_meth, w_meth_green_mode
):
    if __is_device_method(device, w_meth):
        if w_meth_green_mode:

            @functools.wraps(w_meth)
            def write_attr(device, attr):
                worker = get_worker()
                # already bound to device, so exclude device arg
                return worker.execute(w_meth, attr)

        else:

            @functools.wraps(w_meth)
            def write_attr(device, attr):
                return w_meth(attr)

    else:
        if w_meth_green_mode:

            @functools.wraps(w_meth)
            def write_attr(device, attr):
                worker = get_worker()
                # unbound function or not on device object, so include device arg
                return worker.execute(w_meth, device, attr)

        else:
            write_attr = w_meth

    if _force_tracing:
        write_attr = _forcefully_traced_method(write_attr)

    bound_method = types.MethodType(write_attr, device)
    setattr(device, name, bound_method)


def __patch_device_with_dynamic_attribute_is_allowed_method(
    device, name, is_allo_meth, ia_meth_green_mode
):
    if __is_device_method(device, is_allo_meth):
        if ia_meth_green_mode:

            @functools.wraps(is_allo_meth)
            def is_allowed_attr(device, request_type):
                worker = get_worker()
                # already bound to device, so exclude device arg
                return worker.execute(is_allo_meth, request_type)

        else:

            @functools.wraps(is_allo_meth)
            def is_allowed_attr(device, request_type):
                return is_allo_meth(request_type)

    else:
        if ia_meth_green_mode:

            @functools.wraps(is_allo_meth)
            def is_allowed_attr(device, request_type):
                worker = get_worker()
                # unbound function or not on device object, so include device arg
                return worker.execute(is_allo_meth, device, request_type)

        else:
            is_allowed_attr = is_allo_meth

    if _force_tracing:
        is_allowed_attr = _forcefully_traced_method(is_allowed_attr)

    bound_method = types.MethodType(is_allowed_attr, device)
    setattr(device, name, bound_method)


def __is_device_method(device, func):
    """Return True if func is bound to device object (i.e., a method)"""
    return inspect.ismethod(func) and func.__self__ is device


def __DeviceImpl__remove_attribute(self, attr_name, free_it=False, clean_db=True):
    """
    remove_attribute(self, attr_name)

        Remove one attribute from the device attribute list.

        Note: Call of synchronous remove_attribute method from a coroutine function in
        an asyncio server may cause a deadlock.
        Use ``await`` :meth:`async_remove_attribute` instead.
        However, if overriding the synchronous method ``initialize_dynamic_attributes``,
        then the synchronous remove_attribute method must be used, even in asyncio servers.

        :param attr_name: attribute name
        :type attr_name: str

        :param free_it: free Attr object flag. Default False
        :type free_it: bool

        :param clean_db: clean attribute related info in db. Default True
        :type clean_db: bool

        :raises DevFailed:

        .. versionadded:: 9.5.0
            *free_it* parameter.
            *clean_db* parameter.

    """

    self._remove_attribute(attr_name, free_it, clean_db)


async def __DeviceImpl__async_remove_attribute(
    self, attr_name, free_it=False, clean_db=True
):
    """

    async_remove_attribute(self, attr_name, free_it=False, clean_db=True)

        Remove one attribute from the device attribute list.

        :param attr_name: attribute name
        :type attr_name: str

        :param free_it: free Attr object flag. Default False
        :type free_it: bool

        :param clean_db: clean attribute related info in db. Default True
        :type clean_db: bool

        :raises DevFailed:

        .. versionadded:: 10.0.0

    """

    await get_worker().delegate(self._remove_attribute, attr_name, free_it, clean_db)


def __DeviceImpl__add_command(self, cmd, device_level=True):
    """
    add_command(self, cmd, device_level=True) -> cmd

        Add a new command to the device command list.

        :param cmd: the new command to be added to the list
        :param device_level: Set this flag to true if the command must be added
                             for only this device

        :returns: The command to add
        :rtype: Command

        :raises DevFailed:
    """
    config = dict(cmd.__tango_command__[1][2])
    disp_level = DispLevel.OPERATOR

    cmd_name = cmd.__name__

    # default values
    fisallowed = "is_{0}_allowed".format(cmd_name)
    fisallowed_green_mode = True

    if config:
        if "Display level" in config:
            disp_level = config["Display level"]

        if "Is allowed" in config:
            fisallowed = config["Is allowed"]

        fisallowed_green_mode = config["Is allowed green_mode"]

    if is_pure_str(fisallowed):
        fisallowed = getattr(self, fisallowed, None)

    if fisallowed is not None:
        fisallowed_name = (
            f"__wrapped_{getattr(fisallowed, '__name__', f'is_{cmd_name}_allowed')}__"
        )
        __patch_device_with_dynamic_command_is_allowed_method(
            self, fisallowed_name, fisallowed, fisallowed_green_mode
        )
    else:
        fisallowed_name = ""

    setattr(self, cmd_name, cmd)

    self._add_command(
        cmd_name, cmd.__tango_command__[1], fisallowed_name, disp_level, device_level
    )
    return cmd


def __patch_device_with_dynamic_command_method(device, name, method):
    if __is_device_method(device, method):

        @functools.wraps(method)
        def wrapped_command_method(device, *args):
            worker = get_worker()
            # already bound to device, so exclude device arg
            return worker.execute(method, *args)

    else:

        @functools.wraps(method)
        def wrapped_command_method(device, *args):
            worker = get_worker()
            # unbound function or not on device object, so include device arg
            return worker.execute(method, device, *args)

    bound_method = types.MethodType(wrapped_command_method, device)
    setattr(device, name, bound_method)


def __patch_device_with_dynamic_command_is_allowed_method(
    device, name, is_allo_meth, green_mode
):
    if __is_device_method(device, is_allo_meth):
        if green_mode:

            @functools.wraps(is_allo_meth)
            def is_allowed_cmd(device):
                worker = get_worker()
                # already bound to device, so exclude device arg
                return worker.execute(is_allo_meth)

        else:
            is_allowed_cmd = is_allo_meth

    else:
        if green_mode:

            @functools.wraps(is_allo_meth)
            def is_allowed_cmd(device):
                worker = get_worker()
                # unbound function or not on device object, so include device arg
                return worker.execute(is_allo_meth, device)

        else:

            @functools.wraps(is_allo_meth)
            def is_allowed_cmd(device):
                # unbound function or not on device object, so include device arg
                return is_allo_meth(device)

    if _force_tracing:
        is_allowed_cmd = _forcefully_traced_method(is_allowed_cmd)

    bound_method = types.MethodType(is_allowed_cmd, device)
    setattr(device, name, bound_method)


def __DeviceImpl__remove_command(self, cmd_name, free_it=False, clean_db=True):
    """
    remove_command(self, cmd_name, free_it=False, clean_db=True)

        Remove one command from the device command list.

        :param cmd_name: command name to be removed from the list
        :type cmd_name: str
        :param free_it: set to true if the command object must be freed.
        :type free_it: bool
        :param clean_db: Clean command related information (included polling info
                         if the command is polled) from database.

        :raises DevFailed:
    """
    self._remove_command(cmd_name, free_it, clean_db)


def __DeviceImpl__debug_stream(self, msg, *args, source=None):
    """
    debug_stream(self, msg, *args, source=None)

        Sends the given message to the tango debug stream.

        Since PyTango 7.1.3, the same can be achieved with::

            print(msg, file=self.log_debug)

        :param msg: the message to be sent to the debug stream
        :type msg: str

        :param \\*args: Arguments to format a message string.

        :param source: Function that will be inspected for filename and lineno in the log message.
        :type source: Callable

        .. versionadded:: 9.4.2
            added *source* parameter
    """
    filename, line = get_source_location(source)
    if args:
        msg = msg % args
    self.__debug_stream(filename, line, msg)


def __DeviceImpl__info_stream(self, msg, *args, source=None):
    """
    info_stream(self, msg, *args, source=None)

        Sends the given message to the tango info stream.

        Since PyTango 7.1.3, the same can be achieved with::

            print(msg, file=self.log_info)

        :param msg: the message to be sent to the info stream
        :type msg: str

        :param \\*args: Arguments to format a message string.

        :param source: Function that will be inspected for filename and lineno in the log message.
        :type source: Callable

        .. versionadded:: 9.4.2
            added *source* parameter
    """
    filename, line = get_source_location(source)
    if args:
        msg = msg % args
    self.__info_stream(filename, line, msg)


def __DeviceImpl__warn_stream(self, msg, *args, source=None):
    """
    warn_stream(self, msg, *args, source=None)

        Sends the given message to the tango warn stream.

        Since PyTango 7.1.3, the same can be achieved with::

            print(msg, file=self.log_warn)

        :param msg: the message to be sent to the warn stream
        :type msg: str

        :param \\*args: Arguments to format a message string.

        :param source: Function that will be inspected for filename and lineno in the log message.
        :type source: Callable

        .. versionadded:: 9.4.2
            added *source* parameter
    """
    filename, line = get_source_location(source)
    if args:
        msg = msg % args
    self.__warn_stream(filename, line, msg)


def __DeviceImpl__error_stream(self, msg, *args, source=None):
    """
    error_stream(self, msg, *args, source=None)

        Sends the given message to the tango error stream.

        Since PyTango 7.1.3, the same can be achieved with::

            print(msg, file=self.log_error)

        :param msg: the message to be sent to the error stream
        :type msg: str

        :param \\*args: Arguments to format a message string.

        :param source: Function that will be inspected for filename and lineno in the log message.
        :type source: Callable

        .. versionadded:: 9.4.2
            added *source* parameter
    """
    filename, line = get_source_location(source)
    if args:
        msg = msg % args
    self.__error_stream(filename, line, msg)


def __DeviceImpl__fatal_stream(self, msg, *args, source=None):
    """
    fatal_stream(self, msg, *args, source=None)

        Sends the given message to the tango fatal stream.

        Since PyTango 7.1.3, the same can be achieved with::

            print(msg, file=self.log_fatal)

        :param msg: the message to be sent to the fatal stream
        :type msg: str

        :param \\*args: Arguments to format a message string.

        :param source: Function that will be inspected for filename and lineno in the log message.
        :type source: Callable

        .. versionadded:: 9.4.2
            added *source* parameter
    """
    filename, line = get_source_location(source)
    if args:
        msg = msg % args
    self.__fatal_stream(filename, line, msg)


@property
def __DeviceImpl__debug(self):
    if not hasattr(self, "_debug_s"):
        self._debug_s = TangoStream(self.debug_stream)
    return self._debug_s


@property
def __DeviceImpl__info(self):
    if not hasattr(self, "_info_s"):
        self._info_s = TangoStream(self.info_stream)
    return self._info_s


@property
def __DeviceImpl__warn(self):
    if not hasattr(self, "_warn_s"):
        self._warn_s = TangoStream(self.warn_stream)
    return self._warn_s


@property
def __DeviceImpl__error(self):
    if not hasattr(self, "_error_s"):
        self._error_s = TangoStream(self.error_stream)
    return self._error_s


@property
def __DeviceImpl__fatal(self):
    if not hasattr(self, "_fatal_s"):
        self._fatal_s = TangoStream(self.fatal_stream)
    return self._fatal_s


def __DeviceImpl__str(self):
    dev_name = "unknown"
    try:
        util = Util.instance(False)
        if not util.is_svr_starting() and not util.is_svr_shutting_down():
            dev_name = self.get_name()
    except DevFailed:
        pass  # Util singleton hasn't been initialised yet
    return f"{self.__class__.__name__}({dev_name})"


def __event_exception_converter(*args, **kwargs):
    args = list(args)
    exception = None

    if len(args) and isinstance(args[0], Exception):
        exception = args[0]
    elif "except" in kwargs:
        exception = kwargs.pop("except")

    # if user managed to create DevFailed, we do not need ot convert it
    if exception and not isinstance(exception, DevFailed):
        if exception.__traceback__ is None:
            # to generate DevFailed we need traceback
            # if user does not provide one (Exception.with_traceback), we generate our
            try:
                raise Exception()
            except Exception:
                # to get to the frame, where user called push_event
                traceback = sys.exc_info()[2]
                try:
                    user_frame = traceback.tb_frame.f_back.f_back
                    exception.__traceback__ = types.TracebackType(
                        None, user_frame, user_frame.f_lasti, user_frame.f_lineno
                    )
                except Exception:
                    # if fails, use what we have
                    exception.__traceback__ = traceback
        args[0] = Except.to_dev_failed(
            exception.__class__, exception, exception.__traceback__
        )
    return args, kwargs


def __DeviceImpl__push_change_event(self, attr_name, *args, **kwargs):
    """
    .. function:: push_change_event(self, attr_name, except)
                  push_change_event(self, attr_name, data, dim_x = 1, dim_y = 0)
                  push_change_event(self, attr_name, str_data, data)
                  push_change_event(self, attr_name, data, time_stamp, quality, dim_x = 1, dim_y = 0)
                  push_change_event(self, attr_name, str_data, data, time_stamp, quality)
        :noindex:

    Push a change event for the given attribute name.

    :param attr_name: attribute name
    :type attr_name: str
    :param data: the data to be sent as attribute event data. Data must be compatible with the
                 attribute type and format.
                 for SPECTRUM and IMAGE attributes, data can be any type of sequence of elements
                 compatible with the attribute type
    :param str_data: special variation for DevEncoded data type. In this case 'data' must
                     be a str or an object with the buffer interface.
    :type str_data: str
    :param except: Instead of data, you may want to send an exception.
    :type except: DevFailed
    :param dim_x: the attribute x length. Default value is 1
    :type dim_x: int
    :param dim_y: the attribute y length. Default value is 0
    :type dim_y: int
    :param time_stamp: the time stamp
    :type time_stamp: double
    :param quality: the attribute quality factor
    :type quality: AttrQuality

    :raises DevFailed: If the attribute data type is not coherent.
    """
    args, kwargs = __event_exception_converter(*args, **kwargs)
    self.__push_change_event(attr_name, *args, **kwargs)


def __DeviceImpl__push_alarm_event(self, attr_name, *args, **kwargs):
    """
    .. function:: push_alarm_event(self, attr_name, except)
                  push_alarm_event(self, attr_name, data, dim_x = 1, dim_y = 0)
                  push_alarm_event(self, attr_name, str_data, data)
                  push_alarm_event(self, attr_name, data, time_stamp, quality, dim_x = 1, dim_y = 0)
                  push_alarm_event(self, attr_name, str_data, data, time_stamp, quality)
        :noindex:

    Push an alarm event for the given attribute name.

    :param attr_name: attribute name
    :type attr_name: str
    :param data: the data to be sent as attribute event data. Data must be compatible with the
                 attribute type and format.
                 for SPECTRUM and IMAGE attributes, data can be any type of sequence of elements
                 compatible with the attribute type
    :param str_data: special variation for DevEncoded data type. In this case 'data' must
                     be a str or an object with the buffer interface.
    :type str_data: str
    :param except: Instead of data, you may want to send an exception.
    :type except: DevFailed
    :param dim_x: the attribute x length. Default value is 1
    :type dim_x: int
    :param dim_y: the attribute y length. Default value is 0
    :type dim_y: int
    :param time_stamp: the time stamp
    :type time_stamp: double
    :param quality: the attribute quality factor
    :type quality: AttrQuality

    :raises DevFailed: If the attribute data type is not coherent.
    """
    args, kwargs = __event_exception_converter(*args, **kwargs)
    self.__push_alarm_event(attr_name, *args, **kwargs)


def __DeviceImpl__push_archive_event(self, attr_name, *args, **kwargs):
    """
    .. function:: push_archive_event(self, attr_name, except)
                  push_archive_event(self, attr_name, data, dim_x = 1, dim_y = 0)
                  push_archive_event(self, attr_name, str_data, data)
                  push_archive_event(self, attr_name, data, time_stamp, quality, dim_x = 1, dim_y = 0)
                  push_archive_event(self, attr_name, str_data, data, time_stamp, quality)
        :noindex:

    Push an archive event for the given attribute name.

    :param attr_name: attribute name
    :type attr_name: str
    :param data: the data to be sent as attribute event data. Data must be compatible with the
                 attribute type and format.
                 for SPECTRUM and IMAGE attributes, data can be any type of sequence of elements
                 compatible with the attribute type
    :param str_data: special variation for DevEncoded data type. In this case 'data' must
                     be a str or an object with the buffer interface.
    :type str_data: str
    :param except: Instead of data, you may want to send an exception.
    :type except: DevFailed
    :param dim_x: the attribute x length. Default value is 1
    :type dim_x: int
    :param dim_y: the attribute y length. Default value is 0
    :type dim_y: int
    :param time_stamp: the time stamp
    :type time_stamp: double
    :param quality: the attribute quality factor
    :type quality: AttrQuality

    :raises DevFailed: If the attribute data type is not coherent.
    """
    args, kwargs = __event_exception_converter(*args, **kwargs)
    self.__push_archive_event(attr_name, *args, **kwargs)


def __DeviceImpl__push_event(self, attr_name, filt_names, filt_vals, *args, **kwargs):
    """
    .. function:: push_event(self, attr_name, filt_names, filt_vals, except)
                  push_event(self, attr_name, filt_names, filt_vals, data, dim_x = 1, dim_y = 0)
                  push_event(self, attr_name, filt_names, filt_vals, str_data, data)
                  push_event(self, attr_name, filt_names, filt_vals, data, time_stamp, quality, dim_x = 1, dim_y = 0)
                  push_event(self, attr_name, filt_names, filt_vals, str_data, data, time_stamp, quality)
        :noindex:

    Push a user event for the given attribute name.

    :param attr_name: attribute name
    :type attr_name: str
    :param filt_names: unused (kept for backwards compatibility) - pass an empty list.
    :type filt_names: Sequence[str]
    :param filt_vals: unused (kept for backwards compatibility) - pass an empty list.
    :type filt_vals: Sequence[double]
    :param data: the data to be sent as attribute event data. Data must be compatible with the
                 attribute type and format.
                 for SPECTRUM and IMAGE attributes, data can be any type of sequence of elements
                 compatible with the attribute type
    :param str_data: special variation for DevEncoded data type. In this case 'data' must
                     be a str or an object with the buffer interface.
    :type str_data: str
    :param dim_x: the attribute x length. Default value is 1
    :type dim_x: int
    :param dim_y: the attribute y length. Default value is 0
    :type dim_y: int
    :param time_stamp: the time stamp
    :type time_stamp: double
    :param quality: the attribute quality factor
    :type quality: AttrQuality

    :raises DevFailed: If the attribute data type is not coherent.
    """
    args, kwargs = __event_exception_converter(*args, **kwargs)
    self.__push_event(attr_name, filt_names, filt_vals, *args, **kwargs)


def __DeviceImpl__set_telemetry_enabled(self, enabled: bool):
    """
    set_telemetry_enabled(self, enabled) -> None

        Enable or disable the device's telemetry interface.

        This is a no-op if telemetry support isn't compiled into cppTango.

        :param enabled: True to enable telemetry tracing
        :type enabled: bool

        .. versionadded:: 10.0.0
    """
    if enabled:
        self._enable_telemetry()
    else:
        self._disable_telemetry()


def __DeviceImpl__set_kernel_tracing_enabled(self, enabled: bool):
    """
    set_kernel_tracing_enabled(self, enabled) -> None

        Enable or disable telemetry tracing of cppTango kernel methods, and
        for high-level PyTango devices, tracing of the PyTango kernel (BaseDevice)
        methods.

        This is a no-op if telemetry support isn't compiled into cppTango.

        :param enabled: True to enable kernel tracing
        :type enabled: bool

        .. versionadded:: 10.0.0
    """
    if enabled:
        self._enable_kernel_traces()
    else:
        self._disable_kernel_traces()


def __init_DeviceImpl():
    DeviceImpl._device_class_instance = None
    DeviceImpl.get_device_class = __DeviceImpl__get_device_class
    DeviceImpl.get_device_properties = __DeviceImpl__get_device_properties
    DeviceImpl.add_attribute = __DeviceImpl__add_attribute
    DeviceImpl.remove_attribute = __DeviceImpl__remove_attribute
    DeviceImpl.add_command = __DeviceImpl__add_command
    DeviceImpl.remove_command = __DeviceImpl__remove_command
    DeviceImpl.async_add_attribute = __DeviceImpl__async_add_attribute
    DeviceImpl.async_remove_attribute = __DeviceImpl__async_remove_attribute
    DeviceImpl.__str__ = __DeviceImpl__str
    DeviceImpl.__repr__ = __DeviceImpl__str
    DeviceImpl.debug_stream = __DeviceImpl__debug_stream
    DeviceImpl.info_stream = __DeviceImpl__info_stream
    DeviceImpl.warn_stream = __DeviceImpl__warn_stream
    DeviceImpl.error_stream = __DeviceImpl__error_stream
    DeviceImpl.fatal_stream = __DeviceImpl__fatal_stream
    DeviceImpl.log_debug = __DeviceImpl__debug
    DeviceImpl.log_info = __DeviceImpl__info
    DeviceImpl.log_warn = __DeviceImpl__warn
    DeviceImpl.log_error = __DeviceImpl__error
    DeviceImpl.log_fatal = __DeviceImpl__fatal
    DeviceImpl.push_change_event = __DeviceImpl__push_change_event
    DeviceImpl.push_alarm_event = __DeviceImpl__push_alarm_event
    DeviceImpl.push_archive_event = __DeviceImpl__push_archive_event
    DeviceImpl.push_event = __DeviceImpl__push_event
    DeviceImpl.set_telemetry_enabled = __DeviceImpl__set_telemetry_enabled
    DeviceImpl.set_kernel_tracing_enabled = __DeviceImpl__set_kernel_tracing_enabled


def __Logger__log(self, level, msg, *args):
    """
    log(self, level, msg, *args)

        Sends the given message to the tango the selected stream.

        :param level: Log level
        :type level: Level.LevelLevel
        :param msg: the message to be sent to the stream
        :type msg: str
        :param args: list of optional message arguments
        :type args: Sequence[str]
    """
    filename, line = get_source_location()
    if args:
        msg = msg % args
    self.__log(filename, line, level, msg)


def __Logger__log_unconditionally(self, level, msg, *args):
    """
    log_unconditionally(self, level, msg, *args)

        Sends the given message to the tango the selected stream,
        without checking the level.

        :param level: Log level
        :type level: Level.LevelLevel
        :param msg: the message to be sent to the stream
        :type msg: str
        :param args: list of optional message arguments
        :type args: Sequence[str]
    """
    filename, line = get_source_location()
    if args:
        msg = msg % args
    self.__log_unconditionally(filename, line, level, msg)


def __Logger__debug(self, msg, *args):
    """
    debug(self, msg, *args)

        Sends the given message to the tango debug stream.

        :param msg: the message to be sent to the debug stream
        :type msg: str
        :param args: list of optional message arguments
        :type args: Sequence[str]
    """
    filename, line = get_source_location()
    if args:
        msg = msg % args
    self.__debug(filename, line, msg)


def __Logger__info(self, msg, *args):
    """
    info(self, msg, *args)

        Sends the given message to the tango info stream.

        :param msg: the message to be sent to the info stream
        :type msg: str
        :param args: list of optional message arguments
        :type args: Sequence[str]
    """
    filename, line = get_source_location()
    if args:
        msg = msg % args
    self.__info(filename, line, msg)


def __Logger__warn(self, msg, *args):
    """
    warn(self, msg, *args)

        Sends the given message to the tango warn stream.

        :param msg: the message to be sent to the warn stream
        :type msg: str
        :param args: list of optional message arguments
        :type args: Sequence[str]
    """
    filename, line = get_source_location()
    if args:
        msg = msg % args
    self.__warn(filename, line, msg)


def __Logger__error(self, msg, *args):
    """
    error(self, msg, *args)

        Sends the given message to the tango error stream.

        :param msg: the message to be sent to the error stream
        :type msg: str
        :param args: list of optional message arguments
        :type args: Sequence[str]
    """
    filename, line = get_source_location()
    if args:
        msg = msg % args
    self.__error(filename, line, msg)


def __Logger__fatal(self, msg, *args):
    """
    fatal(self, msg, *args)

        Sends the given message to the tango fatal stream.

        :param msg: the message to be sent to the fatal stream
        :type msg: str
        :param args: list of optional message arguments
        :type args: Sequence[str]
    """
    filename, line = get_source_location()
    if args:
        msg = msg % args
    self.__fatal(filename, line, msg)


def __UserDefaultAttrProp_set_enum_labels(self, enum_labels):
    """
    set_enum_labels(self, enum_labels)

        Set default enumeration labels.

        :param enum_labels: list of enumeration labels
        :type enum_labels: Sequence[str]

        New in PyTango 9.2.0
    """
    elbls = StdStringVector()
    for enu in enum_labels:
        elbls.append(enu)
    return self._set_enum_labels(elbls)


def __Attr__str(self):
    return f"{self.__class__.__name__}({self.get_name()})"


def __init_Attr():
    Attr.__str__ = __Attr__str
    Attr.__repr__ = __Attr__str


def __init_UserDefaultAttrProp():
    UserDefaultAttrProp.set_enum_labels = __UserDefaultAttrProp_set_enum_labels


def __init_Logger():
    Logger.log = __Logger__log
    Logger.log_unconditionally = __Logger__log_unconditionally
    Logger.debug = __Logger__debug
    Logger.info = __Logger__info
    Logger.warning = __Logger__warn
    Logger.error = __Logger__error
    Logger.fatal = __Logger__fatal

    # kept for backward compatibility
    Logger.warn = __Logger__warn


def __doc_DeviceImpl():
    def document_method(method_name, desc, append=True):
        return __document_method(DeviceImpl, method_name, desc, append)

    DeviceImpl.__doc__ = """
    Base class for all TANGO device.

    This class inherits from CORBA classes where all the network layer is implemented.
    """

    document_method(
        "init_device",
        """
    init_device(self)

        Code to handle device initialisation.

        This method is called automatically when the device starts,
        but before it is available to clients (i.e., before it is "exported").
        It also gets called if the device is re-initialised by a call to the
        ``Init`` command (after :meth:`~tango.LatestDeviceImpl.delete_device`).
    """,
    )

    document_method(
        "set_state",
        """
    set_state(self, new_state)

        Set device state.

        :param new_state: the new device state
        :type new_state: DevState
    """,
    )

    document_method(
        "get_state",
        """
    get_state(self) -> DevState

        Get a COPY of the device state.

        :returns: Current device state
        :rtype: DevState
    """,
    )

    document_method(
        "get_prev_state",
        """
    get_prev_state(self) -> DevState

        Get a COPY of the device's previous state.

        :returns: the device's previous state
        :rtype: DevState
    """,
    )

    document_method(
        "get_name",
        """
    get_name(self) -> (str)

        Get a COPY of the device name.

        :returns: the device name
        :rtype: str
    """,
    )

    document_method(
        "get_device_attr",
        """
    get_device_attr(self) -> MultiAttribute

        Get device multi attribute object.

        :returns: the device's MultiAttribute object
        :rtype: MultiAttribute
    """,
    )

    document_method(
        "register_signal",
        """
    register_signal(self, signo)

        Register a signal.

        Register this device as device to be informed when signal signo
        is sent to to the device server process

        :param signo: signal identifier
        :type signo: int
    """,
    )

    document_method(
        "unregister_signal",
        """
    unregister_signal(self, signo)

        Unregister a signal.

        Unregister this device as device to be informed when signal signo
        is sent to to the device server process

        :param signo: signal identifier
        :type signo: int
    """,
    )

    document_method(
        "get_status",
        """
    get_status(self, ) -> str

        Get a COPY of the device status.

        :returns: the device status
        :rtype: str
    """,
    )

    document_method(
        "set_status",
        """
    set_status(self, new_status)

        Set device status.

        :param new_status: the new device status
        :type new_status: str
    """,
    )

    document_method(
        "append_status",
        """
    append_status(self, status, new_line=False)

        Appends a string to the device status.

        :param status: the string to be appened to the device status
        :type status: str
        :param new_line: If true, appends a new line character before the string. Default is False
        :type new_line: bool
    """,
    )

    document_method(
        "dev_state",
        """
    dev_state(self) -> DevState

        Get device state.

        Default method to get device state. The behaviour of this method depends
        on the device state. If the device state is ON or ALARM, it reads the
        attribute(s) with an alarm level defined, check if the read value is
        above/below the alarm and eventually change the state to ALARM, return
        the device state. For all th other device state, this method simply
        returns the state This method can be redefined in sub-classes in case
        of the default behaviour does not fullfill the needs.

        :returns: the device state
        :rtype: DevState

        :raises DevFailed: If it is necessary to read attribute(s) and a problem occurs during the reading
    """,
    )

    document_method(
        "dev_status",
        """
    dev_status(self) -> str

        Get device status.

        Default method to get device status. It returns the contents of the device
        dev_status field. If the device state is ALARM, alarm messages are added
        to the device status. This method can be redefined in sub-classes in case
        of the default behaviour does not fullfill the needs.

        :returns: the device status
        :rtype: str

        :raises DevFailed: If it is necessary to read attribute(s) and a problem occurs during the reading
    """,
    )

    document_method(
        "set_change_event",
        """
    set_change_event(self, attr_name, implemented, detect=True)

        Set an implemented flag for the attribute to indicate that the server fires
        change events manually, without the polling to be started.

        If the detect parameter is set to true, the criteria specified for the
        change event are verified and the event is only pushed if they are fullfilled.
        If detect is set to false the event is fired without any value checking!

        :param attr_name: attribute name
        :type attr_name: str
        :param implemented: True when the server fires change events manually.
        :type implemented: bool
        :param detect: Triggers the verification of the change event properties
                       when set to true. Default value is true.
        :type detect: bool
    """,
    )

    document_method(
        "set_archive_event",
        """
    set_archive_event(self, attr_name, implemented, detect=True)

        Set an implemented flag for the attribute to indicate that the server fires
        archive events manually, without the polling to be started.

        If the detect parameter is set to true, the criteria specified for the
        archive event are verified and the event is only pushed if they are fullfilled.
        If detect is set to false the event is fired without any value checking!

        :param attr_name: attribute name
        :type attr_name: str
        :param implemented: True when the server fires change events manually.
        :type implemented: bool
        :param detect: Triggers the verification of the change event properties
                       when set to true. Default value is true.
        :type detect: bool
    """,
    )

    document_method(
        "set_data_ready_event",
        """
    set_data_ready_event(self, attr_name, implemented)

        Set an implemented flag for the attribute to indicate that the server fires
        data ready events manually.

        :param attr_name: attribute name
        :type attr_name: str
        :param implemented: True when the server fires change events manually.
        :type implemented: bool
    """,
    )

    document_method(
        "push_data_ready_event",
        """
    push_data_ready_event(self, attr_name, counter)

        Push a data ready event for the given attribute name.

        The method needs the attribute name and a
        "counter" which will be passed within the event

        :param attr_name: attribute name
        :type attr_name: str
        :param counter: the user counter
        :type counter: int

        :raises DevFailed: If the attribute name is unknown.
    """,
    )

    document_method(
        "push_pipe_event",
        """
    push_pipe_event(self, pipe_name, except)

        .. function:: push_pipe_event(self, pipe_name, blob, reuse_it)
                      push_pipe_event(self, pipe_name, blob, timeval, reuse_it)
            :noindex:

        Push a pipe event for the given blob.

        :param pipe_name: pipe name
        :type pipe_name: str
        :param blob: the blob data
        :type blob: DevicePipeBlob

        :raises DevFailed: If the pipe name is unknown.

        New in PyTango 9.2.2
    """,
    )

    document_method(
        "get_logger",
        """
    get_logger(self) -> Logger

        Returns the Logger object for this device

        :returns: the Logger object for this device
        :rtype: Logger
    """,
    )

    document_method(
        "init_logger",
        """
    init_logger(self) -> None

        Setups logger for the device.  Called automatically when device starts.
    """,
    )

    document_method(
        "start_logging",
        """
    start_logging(self) -> None

        Starts logging
    """,
    )

    document_method(
        "stop_logging",
        """
    stop_logging(self) -> None

        Stops logging
    """,
    )

    document_method(
        "is_telemetry_enabled",
        """
    is_telemetry_enabled(self) -> bool

        Indicates if telemetry tracing is enabled for the device.

        Always False if telemetry support isn't compiled into cppTango.

        :returns: if device telemetry tracing is enabled
        :rtype: bool

        .. versionadded:: 10.0.0
    """,
    )

    document_method(
        "is_kernel_tracing_enabled",
        """
    is_kernel_tracing_enabled(self) -> bool

        Indicates if telemetry tracing of the cppTango kernel API is enabled.

        Always False if telemetry support isn't compiled into cppTango.

        :returns: if kernel tracing is enabled
        :rtype: bool

        .. versionadded:: 10.0.0
    """,
    )

    document_method(
        "get_exported_flag",
        """
    get_exported_flag(self) -> bool

        Returns the state of the exported flag

        :returns: the state of the exported flag
        :rtype: bool

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "is_attribute_polled",
        """
    is_attribute_polled(self, attr_name) -> bool

        True if the attribute is polled.

        :param str attr_name: attribute name

        :return: True if the attribute is polled
        :rtype: bool
    """,
    )

    document_method(
        "is_command_polled",
        """
    is_command_polled(self, cmd_name) -> bool

        True if the command is polled.

        :param str cmd_name: attribute name

        :return: True if the command is polled
        :rtype: bool
    """,
    )

    document_method(
        "poll_attribute",
        """
    poll_attribute(self, attr_name, period) -> None

        Add an attribute to the list of polled attributes.

        :param str attr_name: attribute name

        :param int period: polling period in milliseconds

        :return: None
        :rtype: None
    """,
    )

    document_method(
        "poll_command",
        """
    poll_command(self, cmd_name, period) -> None

        Add a command to the list of polled commands.

        :param str cmd_name: attribute name

        :param int period: polling period in milliseconds

        :return: None
        :rtype: None
    """,
    )

    document_method(
        "stop_poll_attribute",
        """
    stop_poll_attribute(self, attr_name) -> None

        Remove an attribute from the list of polled attributes.

        :param str attr_name: attribute name

        :return: None
        :rtype: None
    """,
    )

    document_method(
        "stop_poll_command",
        """
    stop_poll_command(self, cmd_name) -> None

        Remove a command from the list of polled commands.

        :param str cmd_name: cmd_name name

        :return: None
        :rtype: None
    """,
    )

    document_method(
        "get_poll_ring_depth",
        """
    get_poll_ring_depth(self) -> int

        Returns the poll ring depth

        :returns: the poll ring depth
        :rtype: int

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "get_poll_old_factor",
        """
    get_poll_old_factor(self) -> int

        Returns the poll old factor

        :returns: the poll old factor
        :rtype: int

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "is_polled",
        """
    is_polled(self) -> bool

        Returns if it is polled

        :returns: True if it is polled or False otherwise
        :rtype: bool

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "get_polled_cmd",
        """
    get_polled_cmd(self) -> Sequence[str]

        Returns a COPY of the list of polled commands

        :returns: a COPY of the list of polled commands
        :rtype: Sequence[str]

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "get_polled_attr",
        """
    get_polled_attr(self) -> Sequence[str]

        Returns a COPY of the list of polled attributes

        :returns: a COPY of the list of polled attributes
        :rtype: Sequence[str]

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "get_non_auto_polled_cmd",
        """
    get_non_auto_polled_cmd(self) -> Sequence[str]

        Returns a COPY of the list of non automatic polled commands

        :returns: a COPY of the list of non automatic polled commands
        :rtype: Sequence[str]

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "get_non_auto_polled_attr",
        """
    get_non_auto_polled_attr(self) -> Sequence[str]

        Returns a COPY of the list of non automatic polled attributes

        :returns: a COPY of the list of non automatic polled attributes
        :rtype: Sequence[str]

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "stop_polling",
        """
    stop_polling(self)

        .. function:: stop_polling(self, with_db_upd)
            :noindex:

        Stop all polling for a device. if the device is polled, call this
        method before deleting it.

        :param with_db_upd: Is it necessary to update db?
        :type with_db_upd: bool

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "get_attribute_poll_period",
        """
    get_attribute_poll_period(self, attr_name) -> int

        Returns the attribute polling period (ms) or 0 if the attribute
        is not polled.

        :param attr_name: attribute name
        :type attr_name: str

        :returns: attribute polling period (ms) or 0 if it is not polled
        :rtype: int

        New in PyTango 8.0.0
    """,
    )

    document_method(
        "get_attribute_config",
        """
    get_attribute_config(self, attr_names) -> list[DeviceAttributeConfig]

        Returns the list of AttributeConfig for the requested names

        :param attr_names: sequence of str with attribute names
        :type attr_names: list[str]

        :returns: :class:`tango.DeviceAttributeConfig` for each requested attribute name
        :rtype: list[:class:`tango.DeviceAttributeConfig`]
    """,
    )

    document_method(
        "get_command_poll_period",
        """
    get_command_poll_period(self, cmd_name) -> int

        Returns the command polling period (ms) or 0 if the command
        is not polled.

        :param cmd_name: command name
        :type cmd_name: str

        :returns: command polling period (ms) or 0 if it is not polled
        :rtype: int

        New in PyTango 8.0.0
    """,
    )

    document_method(
        "check_command_exists",
        """
    check_command_exists(self)

        Check that a command is supported by the device and
        does not need input value.

        The method throws an exception if the
        command is not defined or needs an input value.

        :param cmd_name: the command name
        :type cmd_name: str

        :raises DevFailed:
        :raises API_IncompatibleCmdArgumentType:
        :raises API_CommandNotFound:

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "get_dev_idl_version",
        """
    get_dev_idl_version(self) -> int

        Returns the IDL version.

        :returns: the IDL version
        :rtype: int

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "get_cmd_poll_ring_depth",
        """
    get_cmd_poll_ring_depth(self, cmd_name) -> int

        Returns the command poll ring depth.

        :param cmd_name: the command name
        :type cmd_name: str

        :returns: the command poll ring depth
        :rtype: int

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "get_attr_poll_ring_depth",
        """
    get_attr_poll_ring_depth(self, attr_name) -> int

        Returns the attribute poll ring depth.

        :param attr_name: the attribute name
        :type attr_name: str

        :returns: the attribute poll ring depth
        :rtype: int

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "is_device_locked",
        """
    is_device_locked(self) -> bool

        Returns if this device is locked by a client.

        :returns: True if it is locked or False otherwise
        :rtype: bool

        New in PyTango 7.1.2
    """,
    )

    document_method(
        "get_min_poll_period",
        """
    get_min_poll_period(self) -> int

        Returns the min poll period.

        :returns: the min poll period
        :rtype: int

        New in PyTango 7.2.0
    """,
    )

    document_method(
        "get_cmd_min_poll_period",
        """
    get_cmd_min_poll_period(self) -> Sequence[str]

        Returns the min command poll period.

        :returns: the min command poll period
        :rtype: Sequence[str]

        New in PyTango 7.2.0
    """,
    )

    document_method(
        "get_attr_min_poll_period",
        """
    get_attr_min_poll_period(self) -> Sequence[str]

        Returns the min attribute poll period

        :returns: the min attribute poll period
        :rtype: Sequence[str]

        New in PyTango 7.2.0
    """,
    )

    document_method(
        "push_att_conf_event",
        """
    push_att_conf_event(self, attr)

        Push an attribute configuration event.

        :param attr: the attribute for which the configuration event
                     will be sent.
        :type attr: Attribute

        New in PyTango 7.2.1
    """,
    )

    document_method(
        "push_pipe_event",
        """
    push_pipe_event(self, blob)

        Push an pipe event.

        :param blob: the blob which pipe event will be send.

        New in PyTango 9.2.2
    """,
    )

    document_method(
        "is_there_subscriber",
        """
    is_there_subscriber(self, att_name, event_type) -> bool

        Check if there is subscriber(s) listening for the event.

        This method returns a boolean set to true if there are some
        subscriber(s) listening on the event specified by the two method
        arguments. Be aware that there is some delay (up to 600 sec)
        between this method returning false and the last subscriber
        unsubscription or crash...

        The device interface change event is not supported by this method.

        :param att_name: the attribute name
        :type att_name: str
        :param event_type: the event type
        :type event_type: EventType

        :returns: True if there is at least one listener or False otherwise
        :rtype: bool
    """,
    )

    document_method(
        "get_version_info",
        """
    get_version_info(self) -> dict

        Returns a dict with versioning of different modules related to the
        pytango device.

        Example:
            {
                "Build.PyTango.Boost": "1.84.0",
                "Build.PyTango.NumPy": "1.26.4",
                "Build.PyTango.Python": "3.12.2",
                "Build.PyTango.cppTango":"10.0.0",
                "NumPy": "1.26.4",
                "PyTango": "10.0.0.dev0",
                "Python": "3.12.2",
                "cppTango": "10.0.0",
                "omniORB": "4.3.2",
                "zmq": "4.3.5"
            }


        :returns: modules version dict
        :rtype: dict

        .. versionadded:: 10.0.0
    """,
    )

    document_method(
        "add_version_info",
        """
    add_version_info(self, key, value) -> dict

        Method to add information about the module version a device is using

        :param key: Module name
        :type key: str

        :param value: Module version, or other relevant information.
        :type value: str

        .. versionadded:: 10.0.0
    """,
    )


def __doc_extra_DeviceImpl(cls):
    def document_method(method_name, desc, append=True):
        return __document_method(cls, method_name, desc, append)

    document_method(
        "delete_device",
        """
    delete_device(self)

        Code to handle device clean-up.

        This method is called automatically when the device is shut down gracefully.
        It also gets called if the device is re-initialised by a call to the ``Init``
        command (before a new call to :meth:`~tango.LatestDeviceImpl.init_device`).
    """,
    )

    document_method(
        "always_executed_hook",
        """
    always_executed_hook(self)

        Hook method.

        Default method to implement an action necessary on a device before
        any command is executed. This method can be redefined in sub-classes
        in case of the default behaviour does not fullfill the needs

        :raises DevFailed: This method does not throw exception but a redefined method can.
    """,
    )

    document_method(
        "server_init_hook",
        """
    server_init_hook(self)

        Hook method.

        This method is called once the device server admin device is exported.
        This allows for instance for the different devices to subscribe
        to events at server startup on attributes from other devices
        of the same device server with stateless parameter set to false.

        This method can be redefined in sub-classes in case of the default
        behaviour does not fullfill the needs

        .. versionadded:: 9.4.2
    """,
    )

    document_method(
        "read_attr_hardware",
        """
    read_attr_hardware(self, attr_list)

        Read the hardware to return attribute value(s).

        Default method to implement an action necessary on a device to read
        the hardware involved in a read attribute CORBA call. This method
        must be redefined in sub-classes in order to support attribute reading

        :param attr_list: list of indices in the device object attribute vector
                          of an attribute to be read.
        :type attr_list: Sequence[int]

        :raises DevFailed: This method does not throw exception but a redefined method can.
    """,
    )

    document_method(
        "write_attr_hardware",
        """
    write_attr_hardware(self)

        Write the hardware for attributes.

        Default method to implement an action necessary on a device to write
        the hardware involved in a write attribute. This method must be
        redefined in sub-classes in order to support writable attribute

        :param attr_list: list of indices in the device object attribute vector
                          of an attribute to be written.
        :type attr_list: Sequence[int]

        :raises DevFailed: This method does not throw exception but a redefined method can.
    """,
    )

    document_method(
        "signal_handler",
        """
    signal_handler(self, signo)

        Signal handler.

        The method executed when the signal arrived in the device server process.
        This method is defined as virtual and then, can be redefined following
        device needs.

        :param signo: the signal number
        :type signo: int

        :raises DevFailed: This method does not throw exception but a redefined method can.
    """,
    )

    document_method(
        "get_attribute_config_2",
        """
    get_attribute_config_2(self, attr_names) -> list[AttributeConfig_2]

        Returns the list of AttributeConfig_2 for the requested names

        :param attr_names: sequence of str with attribute names
        :type attr_names: list[str]

        :returns: list of :class:`tango.AttributeConfig_2` for each requested attribute name
        :rtype: list[:class:`tango.AttributeConfig_2`]
    """,
    )

    document_method(
        "get_attribute_config_3",
        """
    get_attribute_config_3(self, attr_name) -> list[AttributeConfig_3]

        Returns the list of AttributeConfig_3 for the requested names

        :param attr_names: sequence of str with attribute names
        :type attr_names: list[str]

        :returns: list of :class:`tango.AttributeConfig_3` for each requested attribute name
        :rtype: list[:class:`tango.AttributeConfig_3`]
    """,
    )

    document_method(
        "set_attribute_config",
        """
    set_attribute_config(self, new_conf) -> None

        Sets attribute configuration locally and in the Tango database

        :param new_conf: The new attribute(s) configuration. One AttributeConfig structure is needed for each attribute to update
        :type new_conf: list[:class:`tango.AttributeConfig`]

        :returns: None
        :rtype: None

        .. versionadded:: 10.0.0
    """,
    )

    document_method(
        "set_attribute_config_3",
        """
    set_attribute_config_3(self, new_conf) -> None

        Sets attribute configuration locally and in the Tango database

        :param new_conf: The new attribute(s) configuration. One AttributeConfig structure is needed for each attribute to update
        :type new_conf: list[:class:`tango.AttributeConfig_3`]

        :returns: None
        :rtype: None
    """,
    )

    copy_doc(cls, "dev_state")
    copy_doc(cls, "dev_status")


def __doc_Attribute():
    def document_method(method_name, desc, append=True):
        return __document_method(Attribute, method_name, desc, append)

    Attribute.__doc__ = """
    This class represents a Tango attribute.
    """

    document_method(
        "is_write_associated",
        """
    is_write_associated(self) -> bool

        Check if the attribute has an associated writable attribute.

        :returns: True if there is an associated writable attribute
        :rtype: bool
    """,
    )

    document_method(
        "is_min_alarm",
        """
    is_min_alarm(self) -> bool

        Check if the attribute is in minimum alarm condition.

        :returns: true if the attribute is in alarm condition (read value below the min. alarm).
        :rtype: bool
    """,
    )

    document_method(
        "is_max_alarm",
        """
    is_max_alarm(self) -> bool

        Check if the attribute is in maximum alarm condition.

        :returns: true if the attribute is in alarm condition (read value above the max. alarm).
        :rtype: bool
    """,
    )

    document_method(
        "is_min_warning",
        """
    is_min_warning(self) -> bool

        Check if the attribute is in minimum warning condition.

        :returns: true if the attribute is in warning condition (read value below the min. warning).
        :rtype: bool
    """,
    )

    document_method(
        "is_max_warning",
        """
    is_max_warning(self) -> bool

        Check if the attribute is in maximum warning condition.

        :returns: true if the attribute is in warning condition (read value above the max. warning).
        :rtype: bool
    """,
    )

    document_method(
        "is_rds_alarm",
        """
    is_rds_alarm(self) -> bool

        Check if the attribute is in RDS alarm condition.

        :returns: true if the attribute is in RDS condition (Read Different than Set).
        :rtype: bool
    """,
    )

    document_method(
        "is_polled",
        """
    is_polled(self) -> bool

        Check if the attribute is polled.

        :returns: true if the attribute is polled.
        :rtype: bool
    """,
    )

    document_method(
        "check_alarm",
        """
    check_alarm(self) -> bool

        Check if the attribute read value is below/above the alarm level.

        :returns: true if the attribute is in alarm condition.
        :rtype: bool

        :raises DevFailed: If no alarm level is defined.
    """,
    )

    document_method(
        "get_writable",
        """
    get_writable(self) -> AttrWriteType

        Get the attribute writable type (RO/WO/RW).

        :returns: The attribute write type.
        :rtype: AttrWriteType
    """,
    )

    document_method(
        "get_name",
        """
    get_name(self) -> str

        Get attribute name.

        :returns: The attribute name
        :rtype: str
    """,
    )

    document_method(
        "get_data_type",
        """
    get_data_type(self) -> int

        Get attribute data type.

        :returns: the attribute data type
        :rtype: int
    """,
    )

    document_method(
        "get_data_format",
        """
    get_data_format(self) -> AttrDataFormat

        Get attribute data format.

        :returns: the attribute data format
        :rtype: AttrDataFormat
    """,
    )

    document_method(
        "get_assoc_name",
        """
    get_assoc_name(self) -> str

        Get name of the associated writable attribute.

        :returns: the associated writable attribute name
        :rtype: str
    """,
    )

    document_method(
        "get_assoc_ind",
        """
    get_assoc_ind(self) -> int

        Get index of the associated writable attribute.

        :returns: the index in the main attribute vector of the associated writable attribute
        :rtype: int
    """,
    )

    document_method(
        "set_assoc_ind",
        """
    set_assoc_ind(self, index)

        Set index of the associated writable attribute.

        :param index: The new index in the main attribute vector of the associated writable attribute
        :type index: int
    """,
    )

    document_method(
        "get_date",
        """
    get_date(self) -> TimeVal

        Get a COPY of the attribute date.

        :returns: the attribute date
        :rtype: TimeVal
    """,
    )

    document_method(
        "set_date",
        """
    set_date(self, new_date)

        Set attribute date.

        :param new_date: the attribute date
        :type new_date: TimeVal
    """,
    )

    document_method(
        "get_label",
        """
    get_label(self, ) -> str

        Get attribute label property.

        :returns: the attribute label
        :rtype: str
    """,
    )

    document_method(
        "get_quality",
        """
    get_quality(self) -> AttrQuality

        Get a COPY of the attribute data quality.

        :returns: the attribute data quality
        :rtype: AttrQuality
    """,
    )

    document_method(
        "set_quality",
        """
    set_quality(self, quality, send_event=False)

        Set attribute data quality.

        :param quality: the new attribute data quality
        :type quality: AttrQuality
        :param send_event: true if a change event should be sent. Default is false.
        :type send_event: bool
    """,
    )

    document_method(
        "get_data_size",
        """
    get_data_size(self)

        Get attribute data size.

        :returns: the attribute data size
        :rtype: int
    """,
    )

    document_method(
        "get_x",
        """
    get_x(self) -> int

        Get attribute data size in x dimension.

        :returns: the attribute data size in x dimension. Set to 1 for scalar attribute
        :rtype: int
    """,
    )

    document_method(
        "get_max_dim_x",
        """
    get_max_dim_x(self) -> int

        Get attribute maximum data size in x dimension.

        :returns: the attribute maximum data size in x dimension. Set to 1 for scalar attribute
        :rtype: int
    """,
    )

    document_method(
        "get_y",
        """
    get_y(self) -> int

        Get attribute data size in y dimension.

        :returns: the attribute data size in y dimension. Set to 0 for scalar attribute
        :rtype: int
    """,
    )

    document_method(
        "get_max_dim_y",
        """
    get_max_dim_y(self) -> int

        Get attribute maximum data size in y dimension.

        :returns: the attribute maximum data size in y dimension. Set to 0 for scalar attribute
        :rtype: int
    """,
    )

    document_method(
        "get_polling_period",
        """
    get_polling_period(self) -> int

        Get attribute polling period.

        :returns: The attribute polling period in mS. Set to 0 when the attribute is not polled
        :rtype: int
    """,
    )

    document_method(
        "set_attr_serial_model",
        """
    set_attr_serial_model(self, ser_model) -> void

        Set attribute serialization model.

        This method allows the user to choose the attribute serialization model.

        :param ser_model: The new serialisation model. The
                          serialization model must be one of ATTR_BY_KERNEL,
                          ATTR_BY_USER or ATTR_NO_SYNC
        :type ser_model: AttrSerialModel

        New in PyTango 7.1.0
    """,
    )

    document_method(
        "get_attr_serial_model",
        """
    get_attr_serial_model(self) -> AttrSerialModel

        Get attribute serialization model.

        :returns: The attribute serialization model
        :rtype: AttrSerialModel

        New in PyTango 7.1.0
    """,
    )

    document_method(
        "set_change_event",
        """
    set_change_event(self, implemented, detect = True)

        Set a flag to indicate that the server fires change events manually,
        without the polling to be started for the attribute.

        If the detect parameter is set to true, the criteria specified for
        the change event are verified and the event is only pushed if they
        are fullfilled. If detect is set to false the event is fired without
        any value checking!

        :param implemented: True when the server fires change events manually.
        :type implemented: bool
        :param detect: (optional, default is True) Triggers the verification of
                       the change event properties when set to true.
        :type detect: bool

        New in PyTango 7.1.0
    """,
    )

    document_method(
        "set_archive_event",
        """
    set_archive_event(self, implemented, detect = True)

        Set a flag to indicate that the server fires archive events manually,
        without the polling to be started for the attribute.

        If the detect parameter
        is set to true, the criteria specified for the archive event are verified
        and the event is only pushed if they are fullfilled.

        :param implemented: True when the server fires archive events manually.
        :type implemented: bool
        :param detect: (optional, default is True) Triggers the verification of
                       the archive event properties when set to true.
        :type detect: bool

        New in PyTango 7.1.0
    """,
    )

    document_method(
        "is_change_event",
        """
    is_change_event(self) -> bool

        Check if the change event is fired manually (without polling) for this attribute.

        :returns: True if a manual fire change event is implemented.
        :rtype: bool

        New in PyTango 7.1.0
    """,
    )

    document_method(
        "is_check_change_criteria",
        """
    is_check_change_criteria(self) -> bool

        Check if the change event criteria should be checked when firing the
        event manually.

        :returns: True if a change event criteria will be checked.
        :rtype: bool

        New in PyTango 7.1.0
    """,
    )

    document_method(
        "is_archive_event",
        """
    is_archive_event(self) -> bool

        Check if the archive event is fired manually (without polling) for this attribute.

        :returns: True if a manual fire archive event is implemented.
        :rtype: bool

        New in PyTango 7.1.0
    """,
    )

    document_method(
        "is_check_archive_criteria",
        """
    is_check_archive_criteria(self) -> bool

        Check if the archive event criteria should be checked when firing the
        event manually.

        :returns: True if a archive event criteria will be checked.
        :rtype: bool

        New in PyTango 7.1.0
    """,
    )

    document_method(
        "set_data_ready_event",
        """
    set_data_ready_event(self, implemented)

        Set a flag to indicate that the server fires data ready events.

        :param implemented: True when the server fires data ready events manually.
        :type implemented: bool

        New in PyTango 7.2.0
    """,
    )

    document_method(
        "is_data_ready_event",
        """
    is_data_ready_event(self) -> bool

        Check if the data ready event is fired manually (without polling)
        for this attribute.

        :returns: True if a manual fire data ready event is implemented.
        :rtype: bool

        New in PyTango 7.2.0
    """,
    )

    document_method(
        "remove_configuration",
        """
    remove_configuration(self)

        Remove the attribute configuration from the database.

        This method can be used to clean-up all the configuration of an
        attribute to come back to its default values or the remove all
        configuration of a dynamic attribute before deleting it.

        The method removes all configured attribute properties and removes
        the attribute from the list of polled attributes.

        New in PyTango 7.1.0
    """,
    )


def __doc_WAttribute():
    def document_method(method_name, desc, append=True):
        return __document_method(WAttribute, method_name, desc, append)

    WAttribute.__doc__ = """
    This class represents a Tango writable attribute.
    """

    document_method(
        "get_min_value",
        """
    get_min_value(self) -> obj

        Get attribute minimum value or throws an exception if the
        attribute does not have a minimum value.

        :returns: an object with the python minimum value
        :rtype: obj
    """,
    )

    document_method(
        "get_max_value",
        """
    get_max_value(self) -> obj

        Get attribute maximum value or throws an exception if the
        attribute does not have a maximum value.

        :returns: an object with the python maximum value
        :rtype: obj
    """,
    )

    document_method(
        "set_min_value",
        """
    set_min_value(self, data)

        Set attribute minimum value.

        :param data: the attribute minimum value. python data type must be compatible
                     with the attribute data format and type.
    """,
    )

    document_method(
        "set_max_value",
        """
    set_max_value(self, data)

        Set attribute maximum value.

        :param data: the attribute maximum value. python data type must be compatible
                     with the attribute data format and type.
    """,
    )

    document_method(
        "is_min_value",
        """
    is_min_value(self) -> bool

        Check if the attribute has a minimum value.

        :returns: true if the attribute has a minimum value defined
        :rtype: bool
    """,
    )

    document_method(
        "is_max_value",
        """
    is_max_value(self, ) -> bool

        Check if the attribute has a maximum value.

        :returns: true if the attribute has a maximum value defined
        :rtype: bool
    """,
    )

    document_method(
        "get_write_value_length",
        """
    get_write_value_length(self) -> int

        Retrieve the new value length (data number) for writable attribute.

        :returns: the new value data length
        :rtype: int
    """,
    )

    document_method(
        "set_write_value",
        """
    set_write_value(self, data, dim_x = 1, dim_y = 0)

       Set the writable attribute value.

       :param data: the data to be set. Data must be compatible with the attribute type and format.
                    for SPECTRUM and IMAGE attributes, data can be any type of sequence of elements
                    compatible with the attribute type
       :param dim_x: optional, the attribute set value x length
       :type dim_x: int
       :param dim_y: optional, the attribute set value y length
       :type dim_y: int
    """,
    )

    document_method(
        "get_write_value",
        """
    get_write_value(self, extract_as=ExtractAs.Numpy) -> obj

        Retrieve the new value for writable attribute.

        :param extract_as: defaults to ExtractAs.Numpy
        :type extract_as: ExtractAs

        :returns: the attribute write value.
        :rtype: obj
    """,
    )


def __doc_MultiClassAttribute():
    def document_method(method_name, desc, append=True):
        return __document_method(MultiClassAttribute, method_name, desc, append)

    MultiClassAttribute.__doc__ = """
    There is one instance of this class for each device class.

    This class is mainly an aggregate of :class:`~tango.Attr` objects.
    It eases management of multiple attributes

    New in PyTango 7.2.1"""

    document_method(
        "get_attr",
        """
    get_attr(self, attr_name) -> Attr

        Get the :class:`~tango.Attr` object for the attribute with
        name passed as parameter.

        :param attr_name: attribute name
        :type attr_name: str

        :returns: the attribute object
        :rtype: Attr

        :raises DevFailed: If the attribute is not defined.

        New in PyTango 7.2.1
    """,
    )

    document_method(
        "remove_attr",
        """
    remove_attr(self, attr_name, cl_name)

        Remove the :class:`~tango.Attr` object for the attribute with
        name passed as parameter.

        Does nothing if the attribute does not exist.

        :param attr_name: attribute name
        :type attr_name: str
        :param cl_name: the attribute class name
        :type cl_name: str

        New in PyTango 7.2.1
    """,
    )

    document_method(
        "get_attr_list",
        """
    get_attr_list(self) -> Sequence[Attr]

        Get the list of :class:`~tango.Attr` for this device class.

        :returns: the list of attribute objects
        :rtype: Sequence[Attr]

        New in PyTango 7.2.1
    """,
    )


def __doc_MultiAttribute():
    def document_method(method_name, desc, append=True):
        return __document_method(MultiAttribute, method_name, desc, append)

    MultiAttribute.__doc__ = """
    There is one instance of this class for each device.
    This class is mainly an aggregate of :class:`~tango.Attribute` or
    :class:`~tango.WAttribute` objects. It eases management of multiple
    attributes"""

    document_method(
        "get_attr_by_name",
        """
    get_attr_by_name(self, attr_name) -> Attribute

        Get :class:`~tango.Attribute` object from its name.

        This method returns an :class:`~tango.Attribute` object with a
        name passed as parameter. The equality on attribute name is case
        independant.

        :param attr_name: attribute name
        :type attr_name: str

        :returns: the attribute object
        :rtype: Attribute

        :raises DevFailed: If the attribute is not defined.
    """,
    )

    document_method(
        "get_attr_by_ind",
        """
    get_attr_by_ind(self, ind) -> Attribute

        Get :class:`~tango.Attribute` object from its index.

        This method returns an :class:`~tango.Attribute` object from the
        index in the main attribute vector.

        :param ind: the attribute index
        :type ind: int

        :returns: the attribute object
        :rtype: Attribute
    """,
    )

    document_method(
        "get_w_attr_by_name",
        """
    get_w_attr_by_name(self, attr_name) -> WAttribute

        Get a writable attribute object from its name.

        This method returns an :class:`~tango.WAttribute` object with a
        name passed as parameter. The equality on attribute name is case
        independant.

        :param attr_name: attribute name
        :type attr_name: str

        :returns: the attribute object
        :rtype: WAttribute

        :raises DevFailed: If the attribute is not defined.
    """,
    )

    document_method(
        "get_w_attr_by_ind",
        """
    get_w_attr_by_ind(self, ind) -> WAttribute

        Get a writable attribute object from its index.

        This method returns an :class:`~tango.WAttribute` object from the
        index in the main attribute vector.

        :param ind: the attribute index
        :type ind: int

        :returns: the attribute object
        :rtype: WAttribute
    """,
    )

    document_method(
        "get_attr_ind_by_name",
        """
    get_attr_ind_by_name(self, attr_name) -> int

        Get Attribute index into the main attribute vector from its name.

        This method returns the index in the Attribute vector (stored in the
        :class:`~tango.MultiAttribute` object) of an attribute with a
        given name. The name equality is case independant.

        :param attr_name: attribute name
        :type attr_name: str

        :returns: the attribute index
        :rtype: int

        :raises DevFailed: If the attribute is not found in the vector.

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "get_attr_nb",
        """
    get_attr_nb(self) -> int

        Get attribute number.

        :returns: the number of attributes
        :rtype: int

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "check_alarm",
        """
    check_alarm(self) -> bool

        .. function:: check_alarm(self, attr_name) -> bool
                      check_alarm(self, ind) -> bool
            :noindex:

        Checks an alarm.

        - The 1st version of the method checks alarm on all attribute(s) with an alarm defined.
        - The 2nd version of the method checks alarm for one attribute with a given name.
        - The 3rd version of the method checks alarm for one attribute from its index in the main attributes vector.

        :param attr_name: attribute name
        :type attr_name: str
        :param ind: the attribute index
        :type ind: int

        :returns: True if at least one attribute is in alarm condition
        :rtype: bool

        :raises DevFailed: If at least one attribute does not have any alarm level defined

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "read_alarm",
        """
    read_alarm(self, status)

        Add alarm message to device status.

        This method add alarm mesage to the string passed as parameter.
        A message is added for each attribute which is in alarm condition

        :param status: a string (should be the device status)
        :type status: str

        New in PyTango 7.0.0
    """,
    )

    document_method(
        "get_attribute_list",
        """
    get_attribute_list(self) -> Sequence[Attribute]

        Get the list of attribute objects.

        :returns: list of attribute objects
        :rtype: Sequence[Attribute]

        New in PyTango 7.2.1
    """,
    )


def __doc_Attr():
    def document_method(method_name, desc, append=True):
        return __document_method(Attr, method_name, desc, append)

    Attr.__doc__ = """
    This class represents a Tango writable attribute.
    """

    document_method(
        "check_type",
        """
    check_type(self)

        This method checks data type and throws an exception in case of unsupported data type

        :raises: :class:`DevFailed`: If the data type is unsupported.
    """,
    )

    document_method(
        "is_allowed",
        """
    is_allowed(self, device, request_type) -> bool

        Returns whether the request_type is allowed for the specified device

        :param device: instance of Device
        :type device: :class:`tango.server.Device`

        :param request_type: AttReqType.READ_REQ for read request or AttReqType.WRITE_REQ for write request
        :type request_type: :const:`AttReqType`

        :returns: True if request_type is allowed for the specified device
        :rtype: bool
    """,
    )

    # TODO finish description
    # document_method("read", """
    # read(self, device, attribute)
    #
    #     TODO: Check description
    #
    #     Default read empty method. For readable attribute, it is necessary to overwrite it
    #
    #     :param device: instance of Device
    #     :type device: Device
    # """)

    # TODO finish description
    # document_method("write", """
    # write(self, device, attribute)
    #
    #     TODO: Check description
    #
    #     Default write empty method. For writable attribute, it is necessary to overwrite it
    #
    #     :param device: instance of Device
    #     :type device: Device
    # """)

    document_method(
        "set_default_properties",
        """
    set_default_properties(self, attr_prop)

        Set default attribute properties.

        :param attr_prop: the user default property class
        :type attr_prop: UserDefaultAttrProp
    """,
    )

    document_method(
        "set_disp_level",
        """
    set_disp_level(self, disp_level)

        Set the attribute display level.

        :param disp_level: the new display level
        :type disp_level: DispLevel
    """,
    )

    document_method(
        "set_polling_period",
        """
    set_polling_period(self, period)

        Set the attribute polling update period.

        :param period: the attribute polling period (in mS)
        :type period: int
    """,
    )

    document_method(
        "set_memorized",
        """
    set_memorized(self)

        Set the attribute as memorized in database (only for scalar
        and writable attribute).

        By default the setpoint will be written to the attribute during initialisation!
        Use method set_memorized_init() with False as argument if you don't
        want this feature.
    """,
    )

    document_method(
        "set_memorized_init",
        """
    set_memorized_init(self, write_on_init)

        Set the initialisation flag for memorized attributes.

        - true = the setpoint value will be written to the attribute on initialisation
        - false = only the attribute setpoint is initialised.

        No action is taken on the attribute

        :param write_on_init: if true the setpoint value will be written
                              to the attribute on initialisation
        :type write_on_init: bool
    """,
    )

    document_method(
        "set_change_event",
        """
    set_change_event(self, implemented, detect)

        Set a flag to indicate that the server fires change events manually
        without the polling to be started for the attribute.

        If the detect parameter is set to true, the criteria specified for
        the change event are verified and the event is only pushed if they
        are fullfilled.

        If detect is set to false the event is fired without checking!

        :param implemented: True when the server fires change events manually.
        :type implemented: bool
        :param detect: Triggers the verification of the change event properties
                       when set to true.
        :type detect: bool
    """,
    )

    document_method(
        "is_change_event",
        """
    is_change_event(self) -> bool

        Check if the change event is fired manually for this attribute.

        :returns: true if a manual fire change event is implemented.
        :rtype: bool
    """,
    )

    document_method(
        "is_check_change_criteria",
        """
    is_check_change_criteria(self) -> bool

        Check if the change event criteria should be checked when firing the event manually.

        :returns: true if a change event criteria will be checked.
        :rtype: bool
    """,
    )

    document_method(
        "set_archive_event",
        """
    set_archive_event(self)

        Set a flag to indicate that the server fires archive events manually
        without the polling to be started for the attribute.

        If the detect
        parameter is set to true, the criteria specified for the archive
        event are verified and the event is only pushed if they are fullfilled.

        If detect is set to false the event is fired without checking!

        :param implemented: True when the server fires change events manually.
        :type implemented: bool
        :param detect: Triggers the verification of the archive event properties
                       when set to true.
        :type detect: bool
    """,
    )

    document_method(
        "is_archive_event",
        """
    is_archive_event(self) -> bool

        Check if the archive event is fired manually for this attribute.

        :returns: true if a manual fire archive event is implemented.
        :rtype: bool
    """,
    )

    document_method(
        "is_check_archive_criteria",
        """
    is_check_archive_criteria(self) -> bool

        Check if the archive event criteria should be checked when firing the event manually.

        :returns: true if a archive event criteria will be checked.
        :rtype: bool
    """,
    )

    document_method(
        "set_data_ready_event",
        """
    set_data_ready_event(self, implemented)

        Set a flag to indicate that the server fires data ready events.

        :param implemented: True when the server fires data ready events
        :type implemented: bool

        New in PyTango 7.2.0
    """,
    )

    document_method(
        "is_data_ready_event",
        """
    is_data_ready_event(self) -> bool

        Check if the data ready event is fired for this attribute.

        :returns: true if firing data ready event is implemented.
        :rtype: bool

        New in PyTango 7.2.0
    """,
    )

    document_method(
        "get_name",
        """
    get_name(self) -> str

        Get the attribute name.

        :returns: the attribute name
        :rtype: str
    """,
    )

    document_method(
        "get_format",
        """
    get_format(self) -> AttrDataFormat

        Get the attribute format.

        :returns: the attribute format
        :rtype: AttrDataFormat
    """,
    )

    document_method(
        "get_writable",
        """
    get_writable(self) -> AttrWriteType

        Get the attribute write type.

        :returns: the attribute write type
        :rtype: AttrWriteType
    """,
    )

    document_method(
        "get_type",
        """
    get_type(self) -> int

        Get the attribute data type.

        :returns: the attribute data type
        :rtype: int
    """,
    )

    document_method(
        "get_disp_level",
        """
    get_disp_level(self) -> DispLevel

        Get the attribute display level.

        :returns: the attribute display level
        :rtype: DispLevel
    """,
    )

    document_method(
        "get_polling_period",
        """
    get_polling_period(self) -> int

        Get the polling period (mS).

        :returns: the polling period (mS)
        :rtype: int
    """,
    )

    document_method(
        "get_memorized",
        """
    get_memorized(self) -> bool

        Determine if the attribute is memorized or not.

        :returns: True if the attribute is memorized
        :rtype: bool
    """,
    )

    document_method(
        "get_memorized_init",
        """
    get_memorized_init(self) -> bool

        Determine if the attribute is written at startup from the memorized
        value if it is memorized.

        :returns: True if initialized with memorized value or not
        :rtype: bool
    """,
    )

    document_method(
        "get_assoc",
        """
    get_assoc(self) -> str

        Get the associated name.

        :returns: the associated name
        :rtype: bool
    """,
    )

    document_method(
        "is_assoc",
        """
    is_assoc(self) -> bool

        Determine if it is assoc.

        :returns: if it is assoc
        :rtype: bool
    """,
    )

    document_method(
        "get_cl_name",
        """
    get_cl_name(self) -> str

        Returns the class name.

        :returns: the class name
        :rtype: str

        New in PyTango 7.2.0
    """,
    )

    document_method(
        "set_cl_name",
        """
    set_cl_name(self, cl)

        Sets the class name.

        :param cl: new class name
        :type cl: str

        New in PyTango 7.2.0
    """,
    )

    document_method(
        "get_class_properties",
        """
    get_class_properties(self) -> Sequence[AttrProperty]

        Get the class level attribute properties.

        :returns: the class attribute properties
        :rtype: Sequence[AttrProperty]
    """,
    )

    document_method(
        "get_user_default_properties",
        """
    get_user_default_properties(self) -> Sequence[AttrProperty]

        Get the user default attribute properties.

        :returns: the user default attribute properties
        :rtype: Sequence[AttrProperty]
    """,
    )

    document_method(
        "set_class_properties",
        """
    set_class_properties(self, props)

        Set the class level attribute properties.

        :param props: new class level attribute properties
        :type props: StdAttrPropertyVector
    """,
    )


def __doc_UserDefaultAttrProp():
    def document_method(method_name, desc, append=True):
        return __document_method(UserDefaultAttrProp, method_name, desc, append)

    UserDefaultAttrProp.__doc__ = """
    User class to set attribute default properties.

    This class is used to set attribute default properties.
    Three levels of attributes properties setting are implemented within Tango.
    The highest property setting level is the database.
    Then the user default (set using this UserDefaultAttrProp class) and finally
    a Tango library default value.
    """

    document_method(
        "set_label",
        """
    set_label(self, def_label)

        Set default label property.

        :param def_label: the user default label property
        :type def_label: str
    """,
    )

    document_method(
        "set_description",
        """
    set_description(self, def_description)

        Set default description property.

        :param def_description: the user default description property
        :type def_description: str
    """,
    )

    document_method(
        "set_format",
        """
    set_format(self, def_format)

        Set default format property.

        :param def_format: the user default format property
        :type def_format: str
    """,
    )

    document_method(
        "set_unit",
        """
    set_unit(self, def_unit)

        Set default unit property.

        :param def_unit: te user default unit property
        :type def_unit: str
    """,
    )

    document_method(
        "set_standard_unit",
        """
    set_standard_unit(self, def_standard_unit)

        Set default standard unit property.

        :param def_standard_unit: the user default standard unit property
        :type def_standard_unit: str
    """,
    )

    document_method(
        "set_display_unit",
        """
    set_display_unit(self, def_display_unit)

        Set default display unit property.

        :param def_display_unit: the user default display unit property
        :type def_display_unit: str
    """,
    )

    document_method(
        "set_min_value",
        """
    set_min_value(self, def_min_value)

        Set default min_value property.

        :param def_min_value: the user default min_value property
        :type def_min_value: str
    """,
    )

    document_method(
        "set_max_value",
        """
    set_max_value(self, def_max_value)

        Set default max_value property.

        :param def_max_value: the user default max_value property
        :type def_max_value: str
    """,
    )

    document_method(
        "set_min_alarm",
        """
    set_min_alarm(self, def_min_alarm)

        Set default min_alarm property.

        :param def_min_alarm: the user default min_alarm property
        :type def_min_alarm: str
    """,
    )

    document_method(
        "set_max_alarm",
        """
    set_max_alarm(self, def_max_alarm)

        Set default max_alarm property.

        :param def_max_alarm: the user default max_alarm property
        :type def_max_alarm: str
    """,
    )

    document_method(
        "set_min_warning",
        """
    set_min_warning(self, def_min_warning)

        Set default min_warning property.

        :param def_min_warning: the user default min_warning property
        :type def_min_warning: str
    """,
    )

    document_method(
        "set_max_warning",
        """
    set_max_warning(self, def_max_warning)

        Set default max_warning property.

        :param def_max_warning: the user default max_warning property
        :type def_max_warning: str
    """,
    )

    document_method(
        "set_delta_t",
        """
    set_delta_t(self, def_delta_t)

        Set default RDS alarm delta_t property.

        :param def_delta_t: the user default RDS alarm delta_t property
        :type def_delta_t: str
    """,
    )

    document_method(
        "set_delta_val",
        """
    set_delta_val(self, def_delta_val)

        Set default RDS alarm delta_val property.

        :param def_delta_val: the user default RDS alarm delta_val property
        :type def_delta_val: str
    """,
    )

    document_method(
        "set_abs_change",
        """
    set_abs_change(self, def_abs_change) <= DEPRECATED

        Set default change event abs_change property.

        :param def_abs_change: the user default change event abs_change property
        :type def_abs_change: str

        Deprecated since PyTango 8.0. Please use set_event_abs_change instead.
    """,
    )

    document_method(
        "set_event_abs_change",
        """
    set_event_abs_change(self, def_abs_change)

        Set default change event abs_change property.

        :param def_abs_change: the user default change event abs_change property
        :type def_abs_change: str

        New in PyTango 8.0
    """,
    )

    document_method(
        "set_rel_change",
        """
    set_rel_change(self, def_rel_change) <= DEPRECATED

        Set default change event rel_change property.

        :param def_rel_change: the user default change event rel_change property
        :type def_rel_change: str

        Deprecated since PyTango 8.0. Please use set_event_rel_change instead.
    """,
    )

    document_method(
        "set_event_rel_change",
        """
    set_event_rel_change(self, def_rel_change)

        Set default change event rel_change property.

        :param def_rel_change: the user default change event rel_change property
        :type def_rel_change: str

        New in PyTango 8.0
    """,
    )

    document_method(
        "set_period",
        """
    set_period(self, def_period) <= DEPRECATED

        Set default periodic event period property.

        :param def_period: the user default periodic event period property
        :type def_period: str

        Deprecated since PyTango 8.0. Please use set_event_period instead.
    """,
    )

    document_method(
        "set_event_period",
        """
    set_event_period(self, def_period)

        Set default periodic event period property.

        :param def_period: the user default periodic event period property
        :type def_period: str

        New in PyTango 8.0
    """,
    )

    document_method(
        "set_archive_abs_change",
        """
    set_archive_abs_change(self, def_archive_abs_change) <= DEPRECATED

        Set default archive event abs_change property.

        :param def_archive_abs_change: the user default archive event abs_change property
        :type def_archive_abs_change: str

        Deprecated since PyTango 8.0. Please use set_archive_event_abs_change instead.
    """,
    )

    document_method(
        "set_archive_event_abs_change",
        """
    set_archive_event_abs_change(self, def_archive_abs_change)

        Set default archive event abs_change property.

        :param def_archive_abs_change: the user default archive event abs_change property
        :type def_archive_abs_change: str

        New in PyTango 8.0
    """,
    )

    document_method(
        "set_archive_rel_change",
        """
    set_archive_rel_change(self, def_archive_rel_change) <= DEPRECATED

        Set default archive event rel_change property.

        :param def_archive_rel_change: the user default archive event rel_change property
        :type def_archive_rel_change: str

        Deprecated since PyTango 8.0. Please use set_archive_event_rel_change instead.
    """,
    )

    document_method(
        "set_archive_event_rel_change",
        """
    set_archive_event_rel_change(self, def_archive_rel_change)

        Set default archive event rel_change property.

        :param def_archive_rel_change: the user default archive event rel_change property
        :type def_archive_rel_change: str

        New in PyTango 8.0
    """,
    )

    document_method(
        "set_archive_period",
        """
    set_archive_period(self, def_archive_period) <= DEPRECATED

        Set default archive event period property.

        :param def_archive_period: t
        :type def_archive_period: str

        Deprecated since PyTango 8.0. Please use set_archive_event_period instead.
    """,
    )

    document_method(
        "set_archive_event_period",
        """
    set_archive_event_period(self, def_archive_period)

        Set default archive event period property.

        :param def_archive_period: t
        :type def_archive_period: str

        New in PyTango 8.0
    """,
    )


def device_server_init(doc=True):
    __init_DeviceImpl()
    __init_Attribute()
    __init_Attr()
    __init_UserDefaultAttrProp()
    __init_Logger()
    if doc:
        __doc_DeviceImpl()
        __doc_extra_DeviceImpl(Device_3Impl)
        __doc_extra_DeviceImpl(Device_4Impl)
        __doc_extra_DeviceImpl(Device_5Impl)
        __doc_extra_DeviceImpl(Device_6Impl)
        __doc_Attribute()
        __doc_WAttribute()
        __doc_MultiAttribute()
        __doc_MultiClassAttribute()
        __doc_UserDefaultAttrProp()
        __doc_Attr()
