// This is the definition of the QPyQuickItem classes.
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


#ifndef _QPYQUICKITEM_H
#define _QPYQUICKITEM_H


#include <Python.h>

#include <qqmlprivate.h>
#include <QByteArray>
#include <QMetaObject>
#include <QQuickItem>

#include "sipAPIQtQuick.h"


class QPyQuickItem : public sipQQuickItem
{
public:
    QPyQuickItem(QQuickItem *parent = 0);

    virtual int typeNr() const = 0;

    static QQmlPrivate::RegisterType *addType(PyTypeObject *type,
            const QMetaObject *mo, const QByteArray &ptr_name,
            const QByteArray &list_name);
    void createPyObject(QQuickItem *parent);

private:
    QPyQuickItem(const QPyQuickItem &);
};


// The canned type declarations.
#define QPYQUICKITEM_DECL(n) \
class QPyQuickItem##n : public QPyQuickItem \
{ \
public: \
    QPyQuickItem##n(QQuickItem *parent = 0); \
    static QMetaObject staticMetaObject; \
    virtual const QMetaObject *metaObject() const; \
    virtual int typeNr() const {return n##U;} \
private: \
    QPyQuickItem##n(const QPyQuickItem##n &); \
}


QPYQUICKITEM_DECL(0);
QPYQUICKITEM_DECL(1);
QPYQUICKITEM_DECL(2);
QPYQUICKITEM_DECL(3);
QPYQUICKITEM_DECL(4);
QPYQUICKITEM_DECL(5);
QPYQUICKITEM_DECL(6);
QPYQUICKITEM_DECL(7);
QPYQUICKITEM_DECL(8);
QPYQUICKITEM_DECL(9);
QPYQUICKITEM_DECL(10);
QPYQUICKITEM_DECL(11);
QPYQUICKITEM_DECL(12);
QPYQUICKITEM_DECL(13);
QPYQUICKITEM_DECL(14);
QPYQUICKITEM_DECL(15);
QPYQUICKITEM_DECL(16);
QPYQUICKITEM_DECL(17);
QPYQUICKITEM_DECL(18);
QPYQUICKITEM_DECL(19);
QPYQUICKITEM_DECL(20);
QPYQUICKITEM_DECL(21);
QPYQUICKITEM_DECL(22);
QPYQUICKITEM_DECL(23);
QPYQUICKITEM_DECL(24);
QPYQUICKITEM_DECL(25);
QPYQUICKITEM_DECL(26);
QPYQUICKITEM_DECL(27);
QPYQUICKITEM_DECL(28);
QPYQUICKITEM_DECL(29);
QPYQUICKITEM_DECL(30);
QPYQUICKITEM_DECL(31);
QPYQUICKITEM_DECL(32);
QPYQUICKITEM_DECL(33);
QPYQUICKITEM_DECL(34);
QPYQUICKITEM_DECL(35);
QPYQUICKITEM_DECL(36);
QPYQUICKITEM_DECL(37);
QPYQUICKITEM_DECL(38);
QPYQUICKITEM_DECL(39);
QPYQUICKITEM_DECL(40);
QPYQUICKITEM_DECL(41);
QPYQUICKITEM_DECL(42);
QPYQUICKITEM_DECL(43);
QPYQUICKITEM_DECL(44);
QPYQUICKITEM_DECL(45);
QPYQUICKITEM_DECL(46);
QPYQUICKITEM_DECL(47);
QPYQUICKITEM_DECL(48);
QPYQUICKITEM_DECL(49);
QPYQUICKITEM_DECL(50);
QPYQUICKITEM_DECL(51);
QPYQUICKITEM_DECL(52);
QPYQUICKITEM_DECL(53);
QPYQUICKITEM_DECL(54);
QPYQUICKITEM_DECL(55);
QPYQUICKITEM_DECL(56);
QPYQUICKITEM_DECL(57);
QPYQUICKITEM_DECL(58);
QPYQUICKITEM_DECL(59);


#endif
