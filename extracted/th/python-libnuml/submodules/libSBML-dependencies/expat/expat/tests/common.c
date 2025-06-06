/* Commonly used functions for the Expat test suite
                            __  __            _
                         ___\ \/ /_ __   __ _| |_
                        / _ \\  /| '_ \ / _` | __|
                       |  __//  \| |_) | (_| | |_
                        \___/_/\_\ .__/ \__,_|\__|
                                 |_| XML parser

   Copyright (c) 2001-2006 Fred L. Drake, Jr. <fdrake@users.sourceforge.net>
   Copyright (c) 2003      Greg Stein <gstein@users.sourceforge.net>
   Copyright (c) 2005-2007 Steven Solie <steven@solie.ca>
   Copyright (c) 2005-2012 Karl Waclawek <karl@waclawek.net>
   Copyright (c) 2016-2022 Sebastian Pipping <sebastian@pipping.org>
   Copyright (c) 2017-2022 Rhodri James <rhodri@wildebeest.org.uk>
   Copyright (c) 2017      Joe Orton <jorton@redhat.com>
   Copyright (c) 2017      José Gutiérrez de la Concha <jose@zeroc.com>
   Copyright (c) 2018      Marco Maggi <marco.maggi-ipsu@poste.it>
   Copyright (c) 2019      David Loffredo <loffredo@steptools.com>
   Copyright (c) 2020      Tim Gates <tim.gates@iress.com>
   Copyright (c) 2021      Donghee Na <donghee.na@python.org>
   Copyright (c) 2023      Sony Corporation / Snild Dolkow <snild@sony.com>
   Licensed under the MIT license:

   Permission is  hereby granted,  free of charge,  to any  person obtaining
   a  copy  of  this  software   and  associated  documentation  files  (the
   "Software"),  to  deal in  the  Software  without restriction,  including
   without  limitation the  rights  to use,  copy,  modify, merge,  publish,
   distribute, sublicense, and/or sell copies of the Software, and to permit
   persons  to whom  the Software  is  furnished to  do so,  subject to  the
   following conditions:

   The above copyright  notice and this permission notice  shall be included
   in all copies or substantial portions of the Software.

   THE  SOFTWARE  IS  PROVIDED  "AS  IS",  WITHOUT  WARRANTY  OF  ANY  KIND,
   EXPRESS  OR IMPLIED,  INCLUDING  BUT  NOT LIMITED  TO  THE WARRANTIES  OF
   MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
   NO EVENT SHALL THE AUTHORS OR  COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
   DAMAGES OR  OTHER LIABILITY, WHETHER  IN AN  ACTION OF CONTRACT,  TORT OR
   OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
   USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

#include <stdio.h>
#include <string.h>

#include "expat_config.h"
#include "expat.h"
#include "internal.h"
#include "chardata.h"
#include "minicheck.h"
#include "common.h"

/* Common test data */

const char *long_character_data_text
    = "<?xml version='1.0' encoding='iso-8859-1'?><s>"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "</s>";

const char *long_cdata_text
    = "<s><![CDATA["
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "012345678901234567890123456789012345678901234567890123456789"
      "]]></s>";

/* Having an element name longer than 1024 characters exercises some
 * of the pool allocation code in the parser that otherwise does not
 * get executed.  The count at the end of the line is the number of
 * characters (bytes) in the element name by that point.x
 */
const char *get_buffer_test_text
    = "<documentwitharidiculouslylongelementnametotease"  /* 0x030 */
      "aparticularcorneroftheallocationinXML_GetBuffers"  /* 0x060 */
      "othatwecanimprovethecoverageyetagain012345678901"  /* 0x090 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x0c0 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x0f0 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x120 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x150 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x180 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x1b0 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x1e0 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x210 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x240 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x270 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x2a0 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x2d0 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x300 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x330 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x360 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x390 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x3c0 */
      "123456789abcdef0123456789abcdef0123456789abcdef0"  /* 0x3f0 */
      "123456789abcdef0123456789abcdef0123456789>\n<ef0"; /* 0x420 */

/* Test control globals */

/* Used as the "resumable" parameter to XML_StopParser by some tests */
XML_Bool g_resumable = XML_FALSE;

/* Used to control abort checks in some tests */
XML_Bool g_abortable = XML_FALSE;

/* Used to control _XML_Parse_SINGLE_BYTES() chunk size */
int g_chunkSize = 1;

/* Common test functions */

void
tcase_add_test__ifdef_xml_dtd(TCase *tc, tcase_test_function test) {
#ifdef XML_DTD
  tcase_add_test(tc, test);
#else
  UNUSED_P(tc);
  UNUSED_P(test);
#endif
}

void
basic_teardown(void) {
  if (g_parser != NULL) {
    XML_ParserFree(g_parser);
    g_parser = NULL;
  }
}

/* Generate a failure using the parser state to create an error message;
   this should be used when the parser reports an error we weren't
   expecting.
*/
void
_xml_failure(XML_Parser parser, const char *file, int line) {
  char buffer[1024];
  enum XML_Error err = XML_GetErrorCode(parser);
  snprintf(buffer, sizeof(buffer),
           "    %d: %" XML_FMT_STR " (line %" XML_FMT_INT_MOD
           "u, offset %" XML_FMT_INT_MOD "u)\n    reported from %s, line %d\n",
           err, XML_ErrorString(err), XML_GetCurrentLineNumber(parser),
           XML_GetCurrentColumnNumber(parser), file, line);
  _assert_true(0, file, line, buffer);
}

enum XML_Status
_XML_Parse_SINGLE_BYTES(XML_Parser parser, const char *s, int len,
                        int isFinal) {
  const int chunksize = g_chunkSize;
  int offset = 0;
  if (chunksize > 0) {
    // parse in chunks of `chunksize` bytes as long as possible
    for (; offset + chunksize < len; offset += chunksize) {
      enum XML_Status res = XML_Parse(parser, s + offset, chunksize, XML_FALSE);
      if (res != XML_STATUS_OK) {
        return res;
      }
    }
  }
  // parse the final chunk, the size of which will be <= chunksize
  return XML_Parse(parser, s + offset, len - offset, isFinal);
}

void
_expect_failure(const char *text, enum XML_Error errorCode,
                const char *errorMessage, const char *file, int lineno) {
  if (_XML_Parse_SINGLE_BYTES(g_parser, text, (int)strlen(text), XML_TRUE)
      == XML_STATUS_OK)
    /* Hackish use of _assert_true() macro, but let's us report
       the right filename and line number. */
    _assert_true(0, file, lineno, errorMessage);
  if (XML_GetErrorCode(g_parser) != errorCode)
    _xml_failure(g_parser, file, lineno);
}

/* Character data support for handlers, built on top of the code in
 * chardata.c
 */
void XMLCALL
accumulate_characters(void *userData, const XML_Char *s, int len) {
  CharData_AppendXMLChars((CharData *)userData, s, len);
}

void XMLCALL
accumulate_attribute(void *userData, const XML_Char *name,
                     const XML_Char **atts) {
  CharData *storage = (CharData *)userData;
  UNUSED_P(name);
  /* Check there are attributes to deal with */
  if (atts == NULL)
    return;

  while (storage->count < 0 && atts[0] != NULL) {
    /* "accumulate" the value of the first attribute we see */
    CharData_AppendXMLChars(storage, atts[1], -1);
    atts += 2;
  }
}

void
_run_character_check(const char *text, const XML_Char *expected,
                     const char *file, int line) {
  CharData storage;

  CharData_Init(&storage);
  XML_SetUserData(g_parser, &storage);
  XML_SetCharacterDataHandler(g_parser, accumulate_characters);
  if (_XML_Parse_SINGLE_BYTES(g_parser, text, (int)strlen(text), XML_TRUE)
      == XML_STATUS_ERROR)
    _xml_failure(g_parser, file, line);
  CharData_CheckXMLChars(&storage, expected);
}

void
_run_attribute_check(const char *text, const XML_Char *expected,
                     const char *file, int line) {
  CharData storage;

  CharData_Init(&storage);
  XML_SetUserData(g_parser, &storage);
  XML_SetStartElementHandler(g_parser, accumulate_attribute);
  if (_XML_Parse_SINGLE_BYTES(g_parser, text, (int)strlen(text), XML_TRUE)
      == XML_STATUS_ERROR)
    _xml_failure(g_parser, file, line);
  CharData_CheckXMLChars(&storage, expected);
}

void XMLCALL
ext_accumulate_characters(void *userData, const XML_Char *s, int len) {
  ExtTest *test_data = (ExtTest *)userData;
  accumulate_characters(test_data->storage, s, len);
}

void
_run_ext_character_check(const char *text, ExtTest *test_data,
                         const XML_Char *expected, const char *file, int line) {
  CharData *const storage = (CharData *)malloc(sizeof(CharData));

  CharData_Init(storage);
  test_data->storage = storage;
  XML_SetUserData(g_parser, test_data);
  XML_SetCharacterDataHandler(g_parser, ext_accumulate_characters);
  if (_XML_Parse_SINGLE_BYTES(g_parser, text, (int)strlen(text), XML_TRUE)
      == XML_STATUS_ERROR)
    _xml_failure(g_parser, file, line);
  CharData_CheckXMLChars(storage, expected);

  free(storage);
}

/* Control variable; the number of times duff_allocator() will successfully
 * allocate */
#define ALLOC_ALWAYS_SUCCEED (-1)
#define REALLOC_ALWAYS_SUCCEED (-1)

int g_allocation_count = ALLOC_ALWAYS_SUCCEED;
int g_reallocation_count = REALLOC_ALWAYS_SUCCEED;

/* Crocked allocator for allocation failure tests */
void *
duff_allocator(size_t size) {
  if (g_allocation_count == 0)
    return NULL;
  if (g_allocation_count != ALLOC_ALWAYS_SUCCEED)
    g_allocation_count--;
  return malloc(size);
}

/* Crocked reallocator for allocation failure tests */
void *
duff_reallocator(void *ptr, size_t size) {
  if (g_reallocation_count == 0)
    return NULL;
  if (g_reallocation_count != REALLOC_ALWAYS_SUCCEED)
    g_reallocation_count--;
  return realloc(ptr, size);
}
