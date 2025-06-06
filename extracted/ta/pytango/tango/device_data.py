# SPDX-FileCopyrightText: All Contributors to the PyTango project
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
This is an internal PyTango module.
"""

__all__ = ("device_data_init",)

__docformat__ = "restructuredtext"

from tango.utils import document_method as __document_method
from tango._tango import DeviceData


def __DeviceData__get_data(self):
    return self.get_data_raw().extract()


def __init_DeviceData():
    pass


def __doc_DeviceData():
    def document_method(method_name, desc, append=True):
        return __document_method(DeviceData, method_name, desc, append)

    DeviceData.__doc__ = """
        This is the fundamental type for sending and receiving data from
        device commands. The values can be inserted and extracted using the
        insert() and extract() methods.
    """

    document_method(
        "extract",
        """
    extract(self) -> any

            Get the actual value stored in the DeviceData.

        Parameters : None
        Return     : Whatever is stored there, or None.
    """,
    )

    document_method(
        "insert",
        """
    insert(self, data_type, value) -> None

            Inserts a value in the DeviceData.

        Parameters :
                - data_type :
                - value     : (any) The value to insert
        Return     : Whatever is stored there, or None.
    """,
    )

    document_method(
        "is_empty",
        """
    is_empty(self) -> bool

            It can be used to test whether the DeviceData object has been
            initialized or not.

        Parameters : None
        Return     : True or False depending on whether the DeviceData object
                    contains data or not.
    """,
    )

    document_method(
        "get_type",
        """
    get_type(self) -> CmdArgType

            This method returns the Tango data type of the data inside the
            DeviceData object.

        Parameters : None
        Return     : The content arg type.
    """,
    )


def device_data_init(doc=True):
    __init_DeviceData()
    if doc:
        __doc_DeviceData()
