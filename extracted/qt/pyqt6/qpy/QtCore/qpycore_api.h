// This defines the API provided by this library.
//
// Copyright (c) 2025 Riverbank Computing Limited <info@riverbankcomputing.com>
// 
// This file is part of PyQt6.
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


#ifndef _QPYCORE_API_H
#define _QPYCORE_API_H


#include <QJsonValue>
#include <QMetaProperty>
#include <QString>
#include <QVariant>

#include "qpycore_namespace.h"
#include "qpycore_public_api.h"


QT_BEGIN_NAMESPACE
class QAbstractEventDispatcher;
class QObject;
QT_END_NAMESPACE


// Support for pyqtSlot().
PyObject *qpycore_pyqtslot(PyObject *args, PyObject *kwds);

// Support for pyqtConfigure().
PyObject *qpycore_pyqtconfigure(PyObject *self, PyObject *args,
        PyObject *kwds);

// Support for the QObject %FinalisationCode.
int qpycore_qobject_finalisation(PyObject *self, QObject *qobj, PyObject *kwds,
        PyObject **updated_kwds);

// Support for converting between PyObject and QString.
PyObject *qpycore_PyObject_FromQString(const QString &qstr);
QString qpycore_PyObject_AsQString(PyObject *obj);

// Support for converting between PyObject and QVariant.
PyObject *qpycore_PyObject_FromQVariant(const QVariant &qvar);
QVariant qpycore_PyObject_AsQVariant(PyObject *obj, int *is_err);
PyObject *qpycore_PyObject_FromQVariant(const QMetaProperty &mprop,
        const QVariant &qvar);
QVariant qpycore_PyObject_AsQVariant(const QMetaProperty &mprop, PyObject *obj,
        bool *ok);

// Support for pyqtClassInfo() and pyqtEnum().
PyObject *qpycore_pyqtClassInfo(PyObject *args, PyObject *kwds);
PyObject *qpycore_pyqtEnum(PyObject *enum_cls);

// Support for creating QGenericArgument and QGenericReturnArgument instances.
PyObject *qpycore_ArgumentFactory(PyObject *type, PyObject *data);
PyObject *qpycore_ReturnFactory(PyObject *type);
PyObject *qpycore_ReturnValue(PyObject *gra);

// Support for QObject.__getattr__().
PyObject *qpycore_qobject_getattr(const QObject *qobj, PyObject *py_qobj,
        const char *name);

// Support for QObject.staticMetaObject %GetCode.
PyObject *qpycore_qobject_staticmetaobject(PyObject *type_obj);

// Support for QMetaObject.connectSlotsByName().
void qpycore_qmetaobject_connectslotsbyname(QObject *qobj,
        PyObject *qobj_wrapper);

// Support for pyqt[Set]PickleProtocol().
extern PyObject *qpycore_pickle_protocol;

// Support for qDebug() etc.
int qpycore_current_context(const char **file, const char **function);

// Support for QObject.disconnect().
PyObject *qpycore_qobject_disconnect(const QObject *q_obj);

// Support for QObject's garbage collector code.
int qpycore_clearSlotProxies(const QObject *transmitter);
int qpycore_visitSlotProxies(const QObject *transmitter, visitproc visit,
        void *arg);

// Support for QJsonValue.
int qpycore_canConvertTo_QJsonValue(PyObject *py);
int qpycore_convertTo_QJsonValue(PyObject *py, PyObject *transferObj,
        QJsonValue **cpp, int *isErr);

// Support for an embedded qt.conf.
bool qpycore_qt_conf();

// Utilities.
void qpycore_Unicode_ConcatAndDel(PyObject **string, PyObject *newpart);

// Initialisation.
void qpycore_init();
void qpycore_post_init(PyObject *module_dict);


// Termination.
extern bool qpycore_created_qapp;


#endif
