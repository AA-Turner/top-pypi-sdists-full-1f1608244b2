/*
 * PythonMessage. Wrapper around errors and warnings.
 *
 * Copyright (c) 2010, Perforce Software, Inc.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * 1.  Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *
 * 2.  Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTR
 * IBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL PERFORCE SOFTWARE, INC. BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 * $Id: //depot/r25.1/p4-python/PythonMessage.cpp#1 $
 *
 */

/*******************************************************************************
 * Name		: PythonMessage.cpp
 *
 * Author	: Sven Erik Knop <sknop@perforce.com>
 *
 * Description	: Class for bridging Perforce's Error class to Python
 *
 ******************************************************************************/

#include <Python.h>
#include <bytesobject.h>
#include "undefdups.h"
#include "python2to3.h"

#include <clientapi.h>

#include "P4PythonDebug.h"
#include "SpecMgr.h"
#include "PythonMessage.h"

PythonMessage::PythonMessage(const Error *e, p4py::SpecMgr * s)
    :	specMgr(s)
{
	// The following is a hack. 
	// The error object omits certain fields if talking to a Unicode server.
	// Formatting the error into a StrBuf seems to retrieve the missing fields.
	// This code can probably be reverted again when the Error object is fixed
	
    StrBuf m;
    e->Fmt( &m, EF_PLAIN );
    err = *e;
}

PyObject * PythonMessage::getSeverity()
{
    return PyInt_FromLong(err.GetSeverity());
}

PyObject * PythonMessage::getGeneric()
{
    return PyInt_FromLong(err.GetGeneric());
}

PyObject * PythonMessage::getMsgid()
{
    ErrorId *id = err.GetId( 0 );
    if( !id )
	return PyInt_FromLong( 0 );
    return PyInt_FromLong(id->UniqueCode());
}

PyObject * PythonMessage::getText()
{
    StrBuf buf;
    err.Fmt(buf, EF_PLAIN);

    return CreatePythonStringAndSize(buf.Text(), buf.Length());
}

PyObject * PythonMessage::getDict()
{
    return specMgr->StrDictToDict( err.GetDict(), NULL);
}

PyObject * PythonMessage::getRepr()
{
    StrBuf a;
    StrBuf b;

    err.Fmt( a, EF_PLAIN );
    b << "[";
    b << "Gen:" << err.GetGeneric();
    b << "/Sev:" << err.GetSeverity();
    b << "]: ";
    b << a;

    return CreatePythonStringAndSize(b.Text(), b.Length());
}
