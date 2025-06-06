// This is the initialisation support code for the QtCore module.
//
// Copyright (c) 2024 Riverbank Computing Limited <info@riverbankcomputing.com>
// 
// This file is part of PyQt5.
// 
// This file may be used under the terms of the GNU General Public License
// version 3.0 as published by the Free Software Foundation and appearing in
// the file LICENSE included in the packaging of this file.  Please review the
// following information to ensure the GNU General Public License version 3.0
// requirements will be met: http://www.gnu.org/copyleft/gpl.html.
// 
// If you do not wish to use this file under the terms of the GPL version 3.0
// then you may purchase a commercial license.  For more information contact
// info@riverbankcomputing.com.
// 
// This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
// WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


#include <Python.h>

#include "qpycore_api.h"
#include "qpycore_public_api.h"
#include "qpycore_pyqtslotproxy.h"
#include "qpycore_qobject_helpers.h"

#include "sipAPIQtCore.h"

#include <QCoreApplication>


// Set if any QCoreApplication (or sub-class) instance was created from Python.
bool qpycore_created_qapp;


// This is called to clean up on exit.  It is done in case the QCoreApplication
// dealloc code hasn't been called.
static PyObject *cleanup_on_exit(PyObject *, PyObject *)
{
    pyqt5_cleanup_qobjects();

    // Never destroy a QCoreApplication if we didn't create it (eg. if we are
    // embedded in a C++ application).
    if (qpycore_created_qapp)
    {
        QCoreApplication *app = QCoreApplication::instance();

        if (app)
        {
            Py_BEGIN_ALLOW_THREADS
            delete app;
            Py_END_ALLOW_THREADS
        }
    }

    Py_INCREF(Py_None);
    return Py_None;
}


// Perform any required initialisation.
void qpycore_init()
{
    // We haven't created a QCoreApplication instance.
    qpycore_created_qapp = false;

    // Export the private helpers, ie. those that should not be used by
    // external handwritten code.
    sipExportSymbol("qtcore_qt_metaobject",
            (void *)qpycore_qobject_metaobject);
    sipExportSymbol("qtcore_qt_metacall", (void *)qpycore_qobject_qt_metacall);
    sipExportSymbol("qtcore_qt_metacast", (void *)qpycore_qobject_qt_metacast);
    sipExportSymbol("qtcore_qobject_sender",
            (void *)PyQtSlotProxy::lastSender);

    // Export the public API.
    sipExportSymbol("pyqt5_cleanup_qobjects", (void *)pyqt5_cleanup_qobjects);
    sipExportSymbol("pyqt5_err_print", (void *)pyqt5_err_print);
    sipExportSymbol("pyqt5_from_argv_list", (void *)pyqt5_from_argv_list);
    sipExportSymbol("pyqt5_from_qvariant_by_type",
            (void *)pyqt5_from_qvariant_by_type);
    sipExportSymbol("pyqt5_get_connection_parts",
            (void *)pyqt5_get_connection_parts);
    sipExportSymbol("pyqt5_get_pyqtsignal_parts",
            (void *)pyqt5_get_pyqtsignal_parts);
    sipExportSymbol("pyqt5_get_pyqtslot_parts",
            (void *)pyqt5_get_pyqtslot_parts);
    sipExportSymbol("pyqt5_get_qmetaobject", (void *)pyqt5_get_qmetaobject);
    sipExportSymbol("pyqt5_get_signal_signature",
            (void *)pyqt5_get_signal_signature);
    sipExportSymbol("pyqt5_register_from_qvariant_convertor",
            (void *)pyqt5_register_from_qvariant_convertor);
    sipExportSymbol("pyqt5_register_to_qvariant_convertor",
            (void *)pyqt5_register_to_qvariant_convertor);
    sipExportSymbol("pyqt5_register_to_qvariant_data_convertor",
            (void *)pyqt5_register_to_qvariant_data_convertor);
    sipExportSymbol("pyqt5_update_argv_list", (void *)pyqt5_update_argv_list);

    // Register the cleanup function.
    static PyMethodDef cleanup_md = {
        "_qtcore_cleanup", cleanup_on_exit, METH_NOARGS, SIP_NULLPTR
    };

    sipRegisterExitNotifier(&cleanup_md);
}
