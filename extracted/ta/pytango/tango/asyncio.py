# SPDX-FileCopyrightText: All Contributors to the PyTango project
# SPDX-License-Identifier: LGPL-3.0-or-later

"""This module exposes a asyncio version of :class:`PyTango.DeviceProxy` and
:class:`PyTango.AttributeProxy"""

from functools import partial

from tango._tango import GreenMode
from tango.device_proxy import get_device_proxy
from tango.attribute_proxy import get_attribute_proxy

__all__ = ("DeviceProxy", "AttributeProxy")


DeviceProxy = partial(get_device_proxy, green_mode=GreenMode.Asyncio)
DeviceProxy.__doc__ = """
    DeviceProxy(self, dev_name, wait=False, timeout=None)
        -> DeviceProxy

    DeviceProxy(self, dev_name, need_check_acc, wait=False, timeout=None)
        -> DeviceProxy

    Creates a *asyncio* enabled :class:`~PyTango.DeviceProxy`.

    The DeviceProxy constructor internally makes some network calls which makes
    it *slow*. By using the asyncio *green mode* you may give the control back
    to the asyncio event loop using the *yield from* or *await* synthax.

    .. note::
        The timeout parameter has no relation with the tango device client side
        timeout (gettable by :meth:`~PyTango.DeviceProxy.get_timeout_millis`
        and settable through :meth:`~PyTango.DeviceProxy.set_timeout_millis`)

    :param dev_name: the device name or alias
    :type dev_name: str
    :param need_check_acc: in first version of the function it defaults to True
                           Determines if at creation time of DeviceProxy it
                           should check for channel access (rarely used)
    :type need_check_acc: bool
    :param wait: whether or not to wait for result of creating a DeviceProxy.
    :type wait: bool
    :param timeout: The number of seconds to wait for the result.
                    If None, then there is no limit on the wait time.
                    Ignored when wait is False.
    :type timeout: float
    :returns:
        if wait is True:
            :class:`~PyTango.DeviceProxy`
        else:
            :class:`concurrent.futures.Future`
    :throws:
        * a *DevFailed* if wait is True and there is an error creating
          the device.
        * an *asyncio.TimeoutError* if wait is False, timeout is not
          None and the time to create the device has expired.

    New in PyTango 8.1.0
"""

AttributeProxy = partial(get_attribute_proxy, green_mode=GreenMode.Asyncio)
AttributeProxy.__doc__ = """
    AttributeProxy(self, full_attr_name, wait=False, timeout=False)
        -> AttributeProxy

    AttributeProxy(self, device_proxy, attr_name, wait=False, timeout=False)
        -> AttributeProxy

    Creates a *futures* enabled :class:`~PyTango.AttributeProxy`.

    The AttributeProxy constructor internally makes some network calls which
    makes it *slow*. By using the asyncio *green mode* you may give the control
    back to the asyncio event loop using the *yield from* or *await* synthax.

    :param full_attr_name: the full name of the attribute
    :type full_attr_name: str
    :param device_proxy: the :class:`~PyTango.DeviceProxy`
    :type device_proxy: DeviceProxy
    :param attr_name: attribute name for the given device proxy
    :type attr_name: str
    :param wait: whether or not to wait for result of creating an
                 AttributeProxy.
    :type wait: bool
    :param timeout: The number of seconds to wait for the result.
                    If None, then there is no limit on the wait time.
                    Ignored when wait is False.
    :type timeout: float
    :returns:
        if wait is True:
            :class:`~PyTango.AttributeProxy`
        else:
            :class:`concurrent.futures.Future`
    :throws:
        * a *DevFailed* if wait is True  and there is an error creating the
          attribute.
        * a *asyncio.TimeoutError* if wait is False, timeout is not
          None and the time to create the attribute has expired.

    New in PyTango 8.1.0
"""

Device = DeviceProxy
Attribute = AttributeProxy

del GreenMode
del get_device_proxy
del get_attribute_proxy
