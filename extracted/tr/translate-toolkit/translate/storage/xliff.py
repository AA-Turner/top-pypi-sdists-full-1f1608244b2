#
# Copyright 2005-2011 Zuza Software Foundation
#
# This file is part of the Translate Toolkit.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

"""
Module for handling XLIFF files for translation.

The official recommendation is to use the extention .xlf for XLIFF files.
"""

import contextlib

from lxml import etree

from translate.misc.multistring import multistring
from translate.misc.xml_helpers import (
    clear_content,
    getXMLspace,
    safely_set_text,
    setXMLlang,
    setXMLspace,
)
from translate.storage import base, lisa
from translate.storage.placeables.lisa import strelem_to_xml, xml_to_strelem
from translate.storage.workflow import StateEnum as state

# TODO: handle translation types

ID_SEPARATOR = "\04"
# ID_SEPARATOR is commonly used through toolkit to generate compound
# unit ids (for instance to concatenate msgctxt and msgid in po), but
# \04 is an illegal char in XML 1.0, ID_SEPARATOR_SAFE will be used
# instead when converting between xliff and other toolkit supported
# formats
ID_SEPARATOR_SAFE = "__%04__"


class xliffunit(lisa.LISAunit):
    """A single term in the xliff file."""

    rootNode = "trans-unit"
    languageNode = "source"
    textNode = ""
    namespace = "urn:oasis:names:tc:xliff:document:1.1"

    _default_xml_space = "default"

    # TODO: id and all the trans-unit level stuff

    S_UNTRANSLATED = state.EMPTY
    S_NEEDS_TRANSLATION = state.NEEDS_WORK
    S_NEEDS_REVIEW = state.NEEDS_REVIEW
    S_TRANSLATED = state.UNREVIEWED
    S_SIGNED_OFF = state.FINAL

    statemap = {
        "new": S_UNTRANSLATED + 1,
        "needs-translation": S_NEEDS_TRANSLATION,
        "needs-adaptation": S_NEEDS_TRANSLATION + 1,
        "needs-l10n": S_NEEDS_TRANSLATION + 2,
        "needs-review-translation": S_NEEDS_REVIEW,
        "needs-review-adaptation": S_NEEDS_REVIEW + 1,
        "needs-review-l10n": S_NEEDS_REVIEW + 2,
        "translated": S_TRANSLATED,
        "signed-off": S_SIGNED_OFF,
        "final": S_SIGNED_OFF + 1,
    }

    statemap_r = {i[1]: i[0] for i in statemap.items()}

    STATE = {
        S_UNTRANSLATED: (state.EMPTY, state.NEEDS_WORK),
        S_NEEDS_TRANSLATION: (state.NEEDS_WORK, state.NEEDS_REVIEW),
        S_NEEDS_REVIEW: (state.NEEDS_REVIEW, state.UNREVIEWED),
        S_TRANSLATED: (state.UNREVIEWED, state.FINAL),
        S_SIGNED_OFF: (state.FINAL, state.MAX),
    }

    def __init__(self, source, empty=False, **kwargs):
        """Override the constructor to set xml:space="preserve"."""
        super().__init__(source, empty, **kwargs)
        if empty:
            return
        setXMLspace(self.xmlelement, "preserve")

    def createlanguageNode(self, lang, text, purpose):
        """Returns an xml Element setup with given parameters."""
        # TODO: for now we do source, but we have to test if it is target,
        # perhaps with parameter. Alternatively, we can use lang, if
        # supplied, since an xliff file has to conform to the bilingual
        # nature promised by the header.
        assert purpose
        langset = etree.Element(self.namespaced(purpose))
        # TODO: check language
        # setXMLlang(langset, lang)

        safely_set_text(langset, text)

        return langset

    def getlanguageNodes(self):
        """We override this to get source and target nodes."""
        source = None
        target = None
        nodes = []
        try:
            source = next(
                self.xmlelement.iterchildren(self.namespaced(self.languageNode))
            )
            target = next(self.xmlelement.iterchildren(self.namespaced("target")))
            nodes = [source, target]
        except StopIteration:
            if source is not None:
                nodes.append(source)
            if target is not None:
                nodes.append(target)
        return nodes

    def set_rich_source(self, value, sourcelang="en"):
        sourcelanguageNode = self.get_source_dom()
        if sourcelanguageNode is None:
            sourcelanguageNode = self.createlanguageNode(sourcelang, "", "source")
            self.set_source_dom(sourcelanguageNode)

        # Clear sourcelanguageNode first
        clear_content(sourcelanguageNode)

        strelem_to_xml(sourcelanguageNode, value[0])

    @property
    def rich_source(self):
        # rsrc = xml_to_strelem(self.source_dom)
        # logger.debug('rich source: %s' % (repr(rsrc)))
        # from dubulib.debug.misc import print_stack_funcs
        # print_stack_funcs()
        return [
            xml_to_strelem(
                self.source_dom, getXMLspace(self.xmlelement, self._default_xml_space)
            )
        ]

    @rich_source.setter
    def rich_source(self, value):
        self.set_rich_source(value)

    def set_rich_target(self, value, lang="xx", append=False):
        self._rich_target = None
        if value is None:
            self.set_target_dom(self.createlanguageNode(lang, "", "target"))
            return

        self._ensure_xml_space_preserve()
        languageNode = self.get_target_dom()
        if languageNode is None:
            languageNode = self.createlanguageNode(lang, "", "target")
            self.set_target_dom(languageNode, append)

        # Clear languageNode first
        clear_content(languageNode)

        strelem_to_xml(languageNode, value[0])
        ### currently giving some issues in Virtaal: self._rich_target = value

    def get_rich_target(self, lang=None):
        """
        Retrieves the "target" text (second entry), or the entry in the
        specified language, if it exists.
        """
        if self._rich_target is None:
            self._rich_target = [
                xml_to_strelem(
                    self.get_target_dom(lang),
                    getXMLspace(self.xmlelement, self._default_xml_space),
                )
            ]
        return self._rich_target

    @property
    def rich_target(self):
        return self.get_rich_target()

    @rich_target.setter
    def rich_target(self, value):
        self.set_rich_target(value)

    def addalttrans(
        self, txt, origin=None, lang=None, sourcetxt=None, matchquality=None
    ):
        """
        Adds an alt-trans tag and alt-trans components to the unit.

        :type txt: String
        :param txt: Alternative translation of the source text.
        """
        # TODO: support adding a source tag ad match quality attribute.  At the
        # source tag is needed to inject fuzzy matches from a TM.
        alttrans = etree.SubElement(self.xmlelement, self.namespaced("alt-trans"))
        setXMLspace(alttrans, "preserve")
        if sourcetxt:
            altsource = etree.SubElement(alttrans, self.namespaced("source"))
            altsource.text = sourcetxt
        alttarget = etree.SubElement(alttrans, self.namespaced("target"))
        alttarget.text = txt
        if matchquality:
            alttrans.set("match-quality", matchquality)
        if origin:
            alttrans.set("origin", origin)
        if lang:
            setXMLlang(alttrans, lang)

    def getalttrans(self, origin=None):
        """
        Returns <alt-trans> for the given origin as a list of units. No
        origin means all alternatives.
        """
        translist = []
        for node in self.xmlelement.iterdescendants(self.namespaced("alt-trans")):
            if self.correctorigin(node, origin):
                # We build some mini units that keep the xmlelement. This
                # makes it easier to delete it if it is passed back to us.
                newunit = base.TranslationUnit(self.source)

                # the source tag is optional
                sourcenode = node.iterdescendants(self.namespaced("source"))
                with contextlib.suppress(StopIteration):
                    newunit.source = lisa.getText(
                        next(sourcenode), getXMLspace(node, self._default_xml_space)
                    )

                # must have one or more targets
                targetnode = node.iterdescendants(self.namespaced("target"))
                newunit.target = lisa.getText(
                    next(targetnode), getXMLspace(node, self._default_xml_space)
                )
                # TODO: support multiple targets better
                # TODO: support notes in alt-trans
                newunit.xmlelement = node

                translist.append(newunit)
        return translist

    def delalttrans(self, alternative):
        """Removes the supplied alternative from the list of alt-trans tags."""
        self.xmlelement.remove(alternative.xmlelement)

    def addnote(self, text, origin=None, position="append"):
        """Add a note specifically in a "note" tag."""
        if position != "append":
            self.removenotes(origin=origin)

        if text:
            text = text.strip()
        if not text:
            return
        note = etree.SubElement(self.xmlelement, self.namespaced("note"))
        note.text = text
        if origin:
            note.set("from", origin)

    def _getnotelist(self, origin=None):
        """
        Returns the text from notes matching ``origin`` or all notes.

        :param origin: The origin of the note (or note type)
        :type origin: String
        :return: The text from notes matching ``origin``
        :rtype: List
        """
        note_nodes = self.xmlelement.iterdescendants(self.namespaced("note"))
        # TODO: consider using xpath to construct initial_list directly
        # or to simply get the correct text from the outset (just remember to
        # check for duplication.
        initial_list = [
            lisa.getText(note, getXMLspace(self.xmlelement, self._default_xml_space))
            for note in note_nodes
            if self.correctorigin(note, origin)
        ]

        # Remove duplicate entries from list:
        dictset = {}
        return [
            dictset.setdefault(note, note)
            for note in initial_list
            if note not in dictset
        ]

    def getnotes(self, origin=None):
        return "\n".join(self._getnotelist(origin=origin))

    def removenotes(self, origin=None):
        """Remove all the translator notes."""
        notes = self.xmlelement.iterdescendants(self.namespaced("note"))
        for note in notes:
            if self.correctorigin(note, origin=origin):
                self.xmlelement.remove(note)

    def adderror(self, errorname, errortext):
        """Adds an error message to this unit."""
        # TODO: consider factoring out: some duplication between XLIFF and TMX
        text = errorname
        if errortext:
            text += ": " + errortext
        self.addnote(text, origin="pofilter")

    def geterrors(self):
        """Get all error messages."""
        # TODO: consider factoring out: some duplication between XLIFF and TMX
        notelist = self._getnotelist(origin="pofilter")
        errordict = {}
        for note in notelist:
            errorname, errortext = note.split(": ")
            errordict[errorname] = errortext
        return errordict

    def get_state_n(self):
        targetnode = self.getlanguageNode(lang=None, index=1)
        if targetnode is None:
            if self.isapproved():
                return self.S_UNREVIEWED
            return self.S_UNTRANSLATED

        xmlstate = targetnode.get("state", None)
        state_n = self.statemap.get(xmlstate, self.S_UNTRANSLATED)

        if state_n < self.S_NEEDS_TRANSLATION and self.target:
            state_n = self.S_NEEDS_TRANSLATION

        if self.isapproved() and state_n < self.S_UNREVIEWED:
            state_n = self.S_UNREVIEWED

        if not self.isapproved() and state_n > self.S_UNREVIEWED:
            state_n = self.S_UNREVIEWED

        return state_n

    def set_state_n(self, value):
        if value not in self.statemap_r:
            value = self.get_state_id(value)

        targetnode = self.getlanguageNode(lang=None, index=1)

        # FIXME: handle state qualifiers
        if value == self.S_UNTRANSLATED:
            if targetnode is not None and "state" in targetnode.attrib:
                del targetnode.attrib["state"]
        elif targetnode is not None:
            xmlstate = self.statemap_r.get(value)
            targetnode.set("state", xmlstate)

        self.markapproved(value > self.S_NEEDS_REVIEW)

    def isapproved(self):
        """States whether this unit is approved."""
        return self.xmlelement.get("approved") == "yes"

    def markapproved(self, value=True):
        """Mark this unit as approved."""
        if value:
            self.xmlelement.set("approved", "yes")
        elif self.isapproved():
            self.xmlelement.set("approved", "no")

    def isreview(self):
        """States whether this unit needs to be reviewed."""
        return self.get_state_id() == self.S_NEEDS_REVIEW

    def markreviewneeded(self, needsreview=True, explanation=None):
        """
        Marks the unit to indicate whether it needs review.

        Adds an optional explanation as a note.
        """
        state_id = self.get_state_id()
        if needsreview and state_id != self.S_NEEDS_REVIEW:
            self.set_state_n(self.S_NEEDS_REVIEW)
            if explanation:
                self.addnote(explanation, origin="translator")
        elif not needsreview and state_id < self.S_UNREVIEWED:
            self.set_state_n(self.S_UNREVIEWED)

    def isfuzzy(self):
        # targetnode = self.getlanguageNode(lang=None, index=1)
        # return not targetnode is None and \
        #         (targetnode.get("state-qualifier") == "fuzzy-match" or \
        #         targetnode.get("state") == "needs-review-translation")
        return not self.isapproved() and bool(self.target)

    def markfuzzy(self, value=True):
        state_id = self.get_state_id()
        if value:
            self.markapproved(False)
            if state_id != self.S_NEEDS_TRANSLATION:
                self.set_state_n(self.S_NEEDS_TRANSLATION)
        else:
            self.markapproved(True)
            if state_id < self.S_UNREVIEWED:
                self.set_state_n(self.S_UNREVIEWED)

    def _ensure_xml_space_preserve(self):
        if getXMLspace(self.xmlelement) != "preserve":
            setXMLspace(self.xmlelement, "preserve")

    def settarget(self, target, lang="xx", append=False):
        """Sets the target string to the given value."""
        super().settarget(target, lang, append)
        if target:
            self._ensure_xml_space_preserve()
            self.marktranslated()

    # This code is commented while this will almost always return false.
    # This way pocount, etc. works well.
    #    def istranslated(self):
    #        targetnode = self.getlanguageNode(lang=None, index=1)
    #        return not targetnode is None and \
    #                (targetnode.get("state") == "translated")

    def istranslatable(self):
        value = self.xmlelement.get("translate")
        return not value or value.lower() != "no"

    def marktranslated(self):
        state_id = self.get_state_id()
        if state_id < self.S_UNREVIEWED:
            self.set_state_n(self.S_UNREVIEWED)

    def setid(self, id):
        # sanitize id in case ID_SEPERATOR is present
        self.xmlelement.set("id", id.replace(ID_SEPARATOR, ID_SEPARATOR_SAFE))

    def getid(self):
        uid = ""
        try:
            filename = next(self.xmlelement.iterancestors(self.namespaced("file"))).get(
                "original"
            )
            if filename:
                uid = filename + ID_SEPARATOR
        except StopIteration:
            # unit has no proper file ancestor, probably newly created
            pass
        # hide the fact that we sanitize ID_SEPERATOR
        uid += str(self.xmlelement.get("id") or "").replace(
            ID_SEPARATOR_SAFE, ID_SEPARATOR
        )
        return uid

    def addlocation(self, location):
        if ":" in location:
            sourcefile, linenumber = location.rsplit(":", 1)
            contexts = [("sourcefile", sourcefile), ("linenumber", linenumber)]
        else:
            contexts = [("sourcefile", location)]
        self.createcontextgroup("", contexts, "location")

    def getlocations(self):
        """Returns a list of locations."""
        locations = []
        for contextgroup in self.getcontextgroupsbyattribute("purpose", "location"):
            sourcefile = next((x for x in contextgroup if x[0] == "sourcefile"), None)
            linenumber = next((x for x in contextgroup if x[0] == "linenumber"), None)
            if sourcefile is not None and linenumber is not None:
                locations.append(sourcefile[1] + ":" + linenumber[1])
            elif sourcefile is not None:
                locations.append(sourcefile[1])

        return locations

    def createcontextgroup(self, name, contexts=None, purpose=None):
        """
        Add the context group to the trans-unit with contexts a list with
        (type, text) tuples describing each context.
        """
        assert contexts
        group = etree.Element(self.namespaced("context-group"))
        # context-group tags must appear at the start within <group>
        # tags. Otherwise it must be appended to the end of a group
        # of tags.
        if self.xmlelement.tag == self.namespaced("group"):
            self.xmlelement.insert(0, group)
        else:
            self.xmlelement.append(group)
        group.set("name", name)
        if purpose:
            group.set("purpose", purpose)
        for type, text in contexts:
            context = etree.SubElement(group, self.namespaced("context"))
            context.text = text
            context.set("context-type", type)

    def getcontextgroups(self, name):
        """Returns the contexts in the context groups with the specified name."""
        groups = []
        grouptags = self.xmlelement.iterdescendants(self.namespaced("context-group"))
        # TODO: conbine name in query
        for group in grouptags:
            if group.get("name") == name:
                contexts = group.iterdescendants(self.namespaced("context"))
                pairs = [
                    (
                        context.get("context-type"),
                        lisa.getText(
                            context,
                            getXMLspace(self.xmlelement, self._default_xml_space),
                        ),
                    )
                    for context in contexts
                ]
                groups.append(pairs)  # not extend
        return groups

    def getcontextgroupsbyattribute(self, attributeName, attributeValue):
        """Returns the contexts in the context groups with the specified attributeName and attributeValue."""
        groups = []
        grouptags = self.xmlelement.iterdescendants(self.namespaced("context-group"))
        for group in grouptags:
            if group.get(attributeName) == attributeValue:
                contexts = group.iterdescendants(self.namespaced("context"))
                pairs = [
                    (
                        context.get("context-type"),
                        lisa.getText(
                            context,
                            getXMLspace(self.xmlelement, self._default_xml_space),
                        ),
                    )
                    for context in contexts
                ]
                groups.append(pairs)  # not extend
        return groups

    def getrestype(self):
        """Returns the restype attribute in the trans-unit tag."""
        return self.xmlelement.get("restype")

    def merge(self, otherunit, overwrite=False, comments=True, authoritative=False):
        # TODO: consider other attributes like "approved"
        super().merge(otherunit, overwrite, comments)
        if self.target:
            self.marktranslated()
            if otherunit.isfuzzy():
                self.markfuzzy()
            elif otherunit.source == self.source:
                self.markfuzzy(False)
            elif otherunit.source != self.source:
                self.markfuzzy(True)
        if comments:
            self.addnote(otherunit.getnotes())

    @staticmethod
    def correctorigin(node, origin):
        """Check against node tag's origin (e.g note or alt-trans)."""
        return (
            origin is None
            or origin in node.get("from", "")
            or origin in node.get("origin", "")
        )

    @classmethod
    def multistring_to_rich(cls, mstr):
        """
        Override :meth:`TranslationUnit.multistring_to_rich` which is used
        by the ``rich_source`` and ``rich_target`` properties.
        """
        strings = mstr
        if isinstance(mstr, multistring):
            strings = mstr.strings
        elif isinstance(mstr, str):
            strings = [mstr]

        return [xml_to_strelem(s) for s in strings]

    @classmethod
    def rich_to_multistring(cls, elem_list):
        """
        Override :meth:`TranslationUnit.rich_to_multistring` which is used
        by the ``rich_source`` and ``rich_target`` properties.
        """
        return multistring([str(elem) for elem in elem_list])


class xlifffile(lisa.LISAfile):
    """Class representing a XLIFF file store."""

    UnitClass = xliffunit
    Name = "XLIFF Translation File"
    Mimetypes = ["application/x-xliff", "application/x-xliff+xml"]
    Extensions = ["xlf", "xliff", "sdlxliff"]
    rootNode = "xliff"
    bodyNode = "body"
    XMLskeleton = """<?xml version="1.0" ?>
<xliff version='1.1' xmlns='urn:oasis:names:tc:xliff:document:1.1'>
<file original='NoName' source-language='en' datatype='plaintext'>
<body>
</body>
</file>
</xliff>"""
    XMLindent = {
        "indent": "  ",
        "max_level": 8,
        "leaves": {"note", "source", "target"},
        "toplevel": False,
        "ignore_preserve": {"trans-unit"},
    }
    namespace = "urn:oasis:names:tc:xliff:document:1.1"
    unversioned_namespace = "urn:oasis:names:tc:xliff:document:"

    suggestions_in_format = True
    """xliff units have alttrans tags which can be used to store suggestions"""

    def __init__(self, *args, **kwargs):
        self._filename = None
        super().__init__(*args, **kwargs)

    def initbody(self):
        # detect the xliff namespace, handle both 1.1 and 1.2
        for ns in self.document.getroot().nsmap.values():
            if ns and ns.startswith(self.unversioned_namespace):
                self.namespace = ns
                break
        else:
            # handle crappy xliff docs without proper namespace declaration
            # by simply using the xmlns default namespace
            self.namespace = self.document.getroot().nsmap.get(None, None)

        if self._filename:
            filenode = self.getfilenode(self._filename, createifmissing=True)
        else:
            filenode = next(
                self.document.getroot().iterchildren(self.namespaced("file"))
            )
        self.body = self.getbodynode(filenode, createifmissing=True)

    def addheader(self):
        """Initialise the file header."""

    def createfilenode(
        self, filename, sourcelanguage=None, targetlanguage=None, datatype="plaintext"
    ):
        """
        Creates a filenode with the given filename. All parameters are
        needed for XLIFF compliance.
        """
        if sourcelanguage is None:
            sourcelanguage = self.sourcelanguage
        if targetlanguage is None:
            targetlanguage = self.targetlanguage

        # find the default NoName file tag and use it instead of creating a new one
        for filenode in self.document.getroot().iterchildren(self.namespaced("file")):
            if filenode.get("original") == "NoName":
                filenode.set("original", filename)
                filenode.set("source-language", sourcelanguage)
                if targetlanguage:
                    filenode.set("target-language", targetlanguage)
                return filenode

        filenode = etree.Element(self.namespaced("file"))
        filenode.set("original", filename)
        filenode.set("source-language", sourcelanguage)
        if targetlanguage:
            filenode.set("target-language", targetlanguage)
        filenode.set("datatype", datatype)
        etree.SubElement(filenode, self.namespaced(self.bodyNode))
        return filenode

    @staticmethod
    def getfilename(filenode):
        """Returns the name of the given file."""
        return filenode.get("original")

    @staticmethod
    def setfilename(filenode, filename):
        """Set the name of the given file."""
        return filenode.set("original", filename)

    def getfilenames(self):
        """Returns all filenames in this XLIFF file."""
        filenodes = self.document.getroot().iterchildren(self.namespaced("file"))
        filenames = [self.getfilename(filenode) for filenode in filenodes]
        filenames = list(filter(None, filenames))
        if len(filenames) == 1 and not filenames[0]:
            filenames = []
        return filenames

    def getfilenode(self, filename, createifmissing=False):
        """Finds the filenode with the given name."""
        filenodes = self.document.getroot().iterchildren(self.namespaced("file"))
        for filenode in filenodes:
            if self.getfilename(filenode) == filename:
                return filenode
        if createifmissing:
            return self.createfilenode(filename)
        return None

    def setsourcelanguage(self, language):
        if not language:
            return
        for filenode in self.document.getroot().iterchildren(self.namespaced("file")):
            filenode.set("source-language", language)

    def getsourcelanguage(self):
        filenode = next(self.document.getroot().iterchildren(self.namespaced("file")))
        return filenode.get("source-language")

    sourcelanguage = property(getsourcelanguage, setsourcelanguage)

    def settargetlanguage(self, language):
        if not language:
            return
        for filenode in self.document.getroot().iterchildren(self.namespaced("file")):
            filenode.set("target-language", language)

    def gettargetlanguage(self):
        filenode = next(self.document.getroot().iterchildren(self.namespaced("file")))
        return filenode.get("target-language")

    targetlanguage = property(gettargetlanguage, settargetlanguage)

    def getdatatype(self, filename=None):
        """
        Returns the datatype of the stored file. If no filename is given,
        the datatype of the first file is given.
        """
        if filename:
            node = self.getfilenode(filename)
            if node is not None:
                return node.get("datatype")
        else:
            filenames = self.getfilenames()
            if len(filenames) > 0 and filenames[0] != "NoName":
                return self.getdatatype(filenames[0])
        return ""

    def getdate(self, filename=None):
        """
        Returns the date attribute for the file.

        If no filename is given, the date of the first file is given.
        If the date attribute is not specified, None is returned.

        :returns: Date attribute of file
        :rtype: Date or None
        """
        if filename:
            node = self.getfilenode(filename)
            if node is not None:
                return node.get("date")
        else:
            filenames = self.getfilenames()
            if len(filenames) > 0 and filenames[0] != "NoName":
                return self.getdate(filenames[0])
        return None

    def removedefaultfile(self):
        """
        We want to remove the default file-tag as soon as possible if we
        know if still present and empty.
        """
        filenodes = list(self.document.getroot().iterchildren(self.namespaced("file")))
        if len(filenodes) > 1:
            for filenode in filenodes:
                if filenode.get("original") == "NoName" and not list(
                    filenode.iterdescendants(self.namespaced(self.UnitClass.rootNode))
                ):
                    self.document.getroot().remove(filenode)
                break

    def getheadernode(self, filenode, createifmissing=False):
        """Finds the header node for the given filenode."""
        # TODO: Deprecated?
        headernode = filenode.iterchildren(self.namespaced("header"))
        try:
            return next(headernode)
        except StopIteration:
            pass
        if not createifmissing:
            return None
        return etree.SubElement(filenode, self.namespaced("header"))

    def getbodynode(self, filenode, createifmissing=False):
        """Finds the body node for the given filenode."""
        bodynode = filenode.iterchildren(self.namespaced("body"))
        try:
            return next(bodynode)
        except StopIteration:
            pass
        if not createifmissing:
            return None
        return etree.SubElement(filenode, self.namespaced("body"))

    def addunit(self, unit, new=True):
        parts = unit.getid().split("\x04")
        if len(parts) > 1:
            filename, unitid = parts[0], "\x04".join(parts[1:])
            self.switchfile(filename, createifmissing=True)
            unit.setid(unitid)
        super().addunit(unit, new=new)

    def addsourceunit(self, source, filename="NoName", createifmissing=False):
        """
        Adds the given trans-unit to the last used body node if the filename
        has changed it uses the slow method instead (will create the nodes
        required if asked). Returns success.
        """
        if not self.switchfile(filename, createifmissing):
            return None
        unit = super().addsourceunit(source)
        # Add unique ID based on number of units. Doing this inside a body/file
        # tag would be better, but performs way worse as we have to query the
        # XML tree for that.
        messagenum = len(self.units) + 1
        unit.setid(f"{messagenum}")
        return unit

    def switchfile(self, filename, createifmissing=False):
        """
        Adds the given trans-unit (will create the nodes required if asked).

        :returns: Success
        :rtype: Boolean
        """
        if self._filename == filename:
            return True
        self._filename = filename
        filenode = self.getfilenode(filename)
        if filenode is None:
            if not createifmissing:
                return False
            filenode = self.createfilenode(filename)
            self.document.getroot().append(filenode)

        self.body = self.getbodynode(filenode, createifmissing=createifmissing)
        return self.body is not None

    def creategroup(self, filename="NoName", createifmissing=False, restype=None):
        """Adds a group tag into the specified file."""
        if not self.switchfile(filename, createifmissing):
            return None
        group = etree.SubElement(self.body, self.namespaced("group"))
        if restype:
            group.set("restype", restype)
        return group

    def serialize(self, out):
        self.removedefaultfile()
        super().serialize(out)

    @classmethod
    def parsestring(cls, storestring):
        """Parses the string to return the correct file object."""
        xliff = super().parsestring(storestring)
        if xliff.units:
            header = xliff.units[0]
            if (
                "gettext-domain-header" in (header.getrestype() or "")
                or xliff.getdatatype() == "po"
            ) and cls.__name__.lower() != "poxlifffile":
                from translate.storage import poxliff

                xliff = poxliff.PoXliffFile.parsestring(storestring)
        return xliff
