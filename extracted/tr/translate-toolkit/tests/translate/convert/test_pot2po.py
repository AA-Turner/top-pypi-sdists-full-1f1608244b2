from io import BytesIO

from pytest import mark

from translate.convert import pot2po
from translate.storage import po

from . import test_convert


class TestPOT2PO:
    @staticmethod
    def convertpot(potsource, posource=None):
        """Helper that converts pot source to po source without requiring files."""
        potfile = BytesIO(potsource.encode())
        pofile = BytesIO(posource.encode()) if posource else None
        pooutfile = BytesIO()
        pot2po.convertpot(potfile, pooutfile, pofile)
        pooutfile.seek(0)
        return po.pofile(pooutfile.read())

    @staticmethod
    def singleunit(pofile):
        """Checks that the pofile contains a single non-header unit, and returns it."""
        assert len(pofile.units) == 2
        assert pofile.units[0].isheader()
        print(pofile.units[1])
        return pofile.units[1]

    def test_convertpot_blank(self):
        """Checks that the convertpot function is working for a simple file initialisation."""
        potsource = f"""#: simple.label{po.lsep}simple.accesskey\nmsgid "A &hard coded newline.\\n"\nmsgstr ""\n"""
        newpo = self.convertpot(potsource)
        assert str(self.singleunit(newpo)) == potsource

    def test_convertpot_blank_plurals(self):
        """Checks that the convertpot function is working for initialising plurals correctly."""
        potsource = r"""msgid ""
msgstr""

msgid "%d manual"
msgid_plural "%d manuals"
msgstr[0] ""
msgstr[1] ""
"""
        posource = r"""msgid ""
msgstr""
"Plural-Forms: nplurals=1; plural=0;\n"
"""

        poexpected = r"""msgid "%d manual"
msgid_plural "%d manuals"
msgstr[0] ""
"""
        newpo = self.convertpot(potsource, posource)
        assert str(self.singleunit(newpo)) == poexpected

    def test_merging_simple(self):
        """Checks that the convertpot function is working for a simple merge."""
        potsource = f"""#: simple.label{po.lsep}simple.accesskey\nmsgid "A &hard coded newline.\\n"\nmsgstr ""\n"""
        posource = f"""#: simple.label{po.lsep}simple.accesskey\nmsgid "A &hard coded newline.\\n"\nmsgstr "&Hart gekoeerde nuwe lyne\\n"\n"""
        newpo = self.convertpot(potsource, posource)
        assert str(self.singleunit(newpo)) == posource

    def test_merging_messages_marked_fuzzy(self):
        """Test that when we merge PO files with a fuzzy message that it remains fuzzy."""
        potsource = f"""#: simple.label{po.lsep}simple.accesskey\nmsgid "A &hard coded newline.\\n"\nmsgstr ""\n"""
        posource = f"""#: simple.label{po.lsep}simple.accesskey\n#, fuzzy\nmsgid "A &hard coded newline.\\n"\nmsgstr "&Hart gekoeerde nuwe lyne\\n"\n"""
        newpo = self.convertpot(potsource, posource)
        assert str(self.singleunit(newpo)) == posource

    def test_merging_plurals_with_fuzzy_matching(self):
        """Test that when we merge PO files with a fuzzy message that it remains fuzzy."""
        potsource = r"""#: file.cpp:2
msgid "%d manual"
msgid_plural "%d manuals"
msgstr[0] ""
msgstr[1] ""
"""
        posource = r"""#: file.cpp:3
#, fuzzy
msgid "%d manual"
msgid_plural "%d manuals"
msgstr[0] "%d handleiding."
msgstr[1] "%d handleidings."
"""
        # The #: comment and msgid's are different between the pot and the po
        poexpected = r"""#: file.cpp:2
#, fuzzy
msgid "%d manual"
msgid_plural "%d manuals"
msgstr[0] "%d handleiding."
msgstr[1] "%d handleidings."
"""
        newpo = self.convertpot(potsource, posource)
        assert str(self.singleunit(newpo)) == poexpected

    @mark.xfail(reason="Not implemented - review if this is even correct")
    def test_merging_msgid_change(self):
        """Tests that if the msgid changes but the location stays the same that we merge."""
        potsource = """#: simple.label\n#: simple.accesskey\nmsgid "Its &hard coding a newline.\\n"\nmsgstr ""\n"""
        posource = """#: simple.label\n#: simple.accesskey\nmsgid "A &hard coded newline.\\n"\nmsgstr "&Hart gekoeerde nuwe lyne\\n"\n"""
        poexpected = """#: simple.label\n#: simple.accesskey\n#, fuzzy\nmsgid "Its &hard coding a newline.\\n"\nmsgstr "&Hart gekoeerde nuwe lyne\\n"\n"""
        newpo = self.convertpot(potsource, posource)
        print(newpo)
        assert str(self.singleunit(newpo)) == poexpected

    def test_merging_location_change(self):
        """Tests that if the location changes but the msgid stays the same that we merge."""
        potsource = f"""#: new_simple.label{po.lsep}new_simple.accesskey\nmsgid "A &hard coded newline.\\n"\nmsgstr ""\n"""
        posource = f"""#: simple.label{po.lsep}simple.accesskey\nmsgid "A &hard coded newline.\\n"\nmsgstr "&Hart gekoeerde nuwe lyne\\n"\n"""
        poexpected = f"""#: new_simple.label{po.lsep}new_simple.accesskey\nmsgid "A &hard coded newline.\\n"\nmsgstr "&Hart gekoeerde nuwe lyne\\n"\n"""
        newpo = self.convertpot(potsource, posource)
        print(newpo)
        assert str(self.singleunit(newpo)) == poexpected

    def test_merging_location_and_whitespace_change(self):
        """
        Test that even if the location changes that if the msgid
        only has whitespace changes we can still merge.
        """
        potsource = f"""#: singlespace.label{po.lsep}singlespace.accesskey\nmsgid "&We have spaces"\nmsgstr ""\n"""
        posource = f"""#: doublespace.label{po.lsep}doublespace.accesskey\nmsgid "&We  have  spaces"\nmsgstr "&One  het  spasies"\n"""
        poexpected = f"""#: singlespace.label{po.lsep}singlespace.accesskey\n#, fuzzy\nmsgid "&We have spaces"\nmsgstr "&One  het  spasies"\n"""
        newpo = self.convertpot(potsource, posource)
        print(newpo)
        assert str(self.singleunit(newpo)) == poexpected

    def test_merging_location_ambiguous_with_disambiguous(self):
        """
        Test that when we have a PO in ambiguous (Gettext form) and merge with
        disamabiguous (KDE comment form) that we don't duplicate the
        location #: comments.
        """
        potsource = (
            """#: location.c:1\nmsgid ""\n"_: location.c:1\\n"\n"Source"\nmsgstr ""\n\n"""
            """#: location.c:10\nmsgid ""\n"_: location.c:10\\n"\n"Source"\nmsgstr ""\n"""
        )
        posource = (
            """#: location.c:1\n#: location.c:10\nmsgid "Source"\nmsgstr "Target"\n\n"""
        )
        poexpected1 = """#: location.c:1\n#, fuzzy\nmsgid ""\n"_: location.c:1\\n"\n"Source"\nmsgstr "Target"\n"""
        poexpected2 = """#: location.c:10\n#, fuzzy\nmsgid ""\n"_: location.c:10\\n"\n"Source"\nmsgstr "Target"\n"""
        newpo = self.convertpot(potsource, posource)
        print("Expected:\n", poexpected1, "Actual:\n", newpo.units[1])
        assert str(newpo.units[1]) == poexpected1
        assert str(newpo.units[2]) == poexpected2

    @mark.xfail(reason="Not Implemented - needs review")
    def test_merging_accelerator_changes(self):
        """Test that a change in the accelerator localtion still allows merging."""
        potsource = """#: someline.c\nmsgid "A&bout"\nmsgstr ""\n"""
        posource = """#: someline.c\nmsgid "&About"\nmsgstr "&Info"\n"""
        poexpected = """#: someline.c\nmsgid "A&bout"\nmsgstr "&Info"\n"""
        newpo = self.convertpot(potsource, posource)
        print(newpo)
        assert str(self.singleunit(newpo)) == poexpected

    @mark.xfail(reason="Not Implemented - review if this is even correct")
    def test_lines_cut_differently(self):
        """Checks that the correct formatting is preserved when pot an po lines differ."""
        potsource = (
            """#: simple.label\nmsgid "Line split "\n"differently"\nmsgstr ""\n"""
        )
        posource = """#: simple.label\nmsgid "Line"\n" split differently"\nmsgstr "Lyne verskillend gesny"\n"""
        newpo = self.convertpot(potsource, posource)
        newpounit = self.singleunit(newpo)
        assert str(newpounit) == posource

    def test_merging_automatic_comments_dont_duplicate(self):
        """Ensure that we can merge #. comments correctly."""
        potsource = """#. Row 35\nmsgid "&About"\nmsgstr ""\n"""
        posource = """#. Row 35\nmsgid "&About"\nmsgstr "&Info"\n"""
        newpo = self.convertpot(potsource, posource)
        newpounit = self.singleunit(newpo)
        assert str(newpounit) == posource

    def test_merging_automatic_comments_new_overides_old(self):
        """Ensure that new #. comments override the old comments."""
        potsource = """#. new comment\n#: someline.c\nmsgid "&About"\nmsgstr ""\n"""
        posource = """#. old comment\n#: someline.c\nmsgid "&About"\nmsgstr "&Info"\n"""
        poexpected = (
            """#. new comment\n#: someline.c\nmsgid "&About"\nmsgstr "&Info"\n"""
        )
        newpo = self.convertpot(potsource, posource)
        newpounit = self.singleunit(newpo)
        assert str(newpounit) == poexpected

    def test_merging_comments_with_blank_comment_lines(self):
        """Test that when we merge a comment that has a blank line we keep the blank line."""
        potsource = """#: someline.c\nmsgid "About"\nmsgstr ""\n"""
        posource = """# comment1\n#\n# comment2\n#: someline.c\nmsgid "About"\nmsgstr "Omtrent"\n"""
        poexpected = posource
        newpo = self.convertpot(potsource, posource)
        newpounit = self.singleunit(newpo)
        assert str(newpounit) == poexpected

    def test_empty_commentlines(self):
        potsource = """#: paneSecurity.title
msgid "Security"
msgstr ""
"""
        posource = """# - Contributor(s):
# -
# - Alternatively, the
# -
#: paneSecurity.title
msgid "Security"
msgstr "Sekuriteit"
"""
        poexpected = posource
        newpo = self.convertpot(potsource, posource)
        newpounit = self.singleunit(newpo)
        print("expected")
        print(poexpected)
        print("got:")
        print(str(newpounit))
        assert str(newpounit) == poexpected

    def test_merging_msgidcomments(self):
        """Ensure that we can merge msgidcomments messages."""
        potsource = r"""#: window.width
msgid ""
"_: Do not translate this.\n"
"36em"
msgstr ""
"""
        posource = r"""#: window.width
msgid ""
"_: Do not translate this.\n"
"36em"
msgstr "36em"
"""
        newpo = self.convertpot(potsource, posource)
        newpounit = self.singleunit(newpo)
        assert str(newpounit) == posource

    def test_merging_msgid_with_msgidcomment(self):
        """Test that we can merge an otherwise identical string that has a different msgid."""
        potsource = r"""#: pref.certs.title
msgid ""
"_: pref.certs.title\n"
"Certificates"
msgstr ""

#: certs.label
msgid ""
"_: certs.label\n"
"Certificates"
msgstr ""
"""
        posource = r"""#: pref.certs.title
msgid ""
"_: pref.certs.title\n"
"Certificates"
msgstr ""

#: certs.label
msgid ""
"_: certs.label\n"
"Certificates"
msgstr "Sertifikate"
"""
        expected = r"""#: pref.certs.title
#, fuzzy
msgid ""
"_: pref.certs.title\n"
"Certificates"
msgstr "Sertifikate"
"""
        newpo = self.convertpot(potsource, posource)
        newpounit = newpo.units[1]
        assert str(newpounit) == expected

    def test_merging_plurals(self):
        """Ensure that we can merge plural messages."""
        potsource = """msgid "One"\nmsgid_plural "Two"\nmsgstr[0] ""\nmsgstr[1] ""\n"""
        posource = """msgid "One"\nmsgid_plural "Two"\nmsgstr[0] "Een"\nmsgstr[1] "Twee"\nmsgstr[2] "Drie"\n"""
        newpo = self.convertpot(potsource, posource)
        print(newpo)
        newpounit = self.singleunit(newpo)
        assert str(newpounit) == posource

    def test_merging_obsoleting_messages(self):
        """Check that we obsolete messages no longer present in the new file."""
        # add emtpy msgid line to help factory identify format
        potsource = 'msgid ""\nmsgstr ""\n'
        posource = '# Some comment\n#. Extracted comment\n#: obsoleteme:10\nmsgid "One"\nmsgstr "Een"\n'
        expected = '# Some comment\n#~ msgid "One"\n#~ msgstr "Een"\n'
        newpo = self.convertpot(potsource, posource)
        print(bytes(newpo))
        newpounit = self.singleunit(newpo)
        assert str(newpounit) == expected

    def test_not_obsoleting_empty_messages(self):
        """Check that we don't obsolete (and keep) untranslated messages."""
        # add emtpy msgid line to help factory identify format
        potsource = 'msgid ""\nmsgstr ""\n'
        posource = '#: obsoleteme:10\nmsgid "One"\nmsgstr ""\n'
        newpo = self.convertpot(potsource, posource)
        print(bytes(newpo))
        # We should only have the header
        assert len(newpo.units) == 1

    def test_merging_new_before_obsolete(self):
        """Test to check that we place new blank message before obsolete messages."""
        potsource = """#: newline.c\nmsgid "&About"\nmsgstr ""\n"""
        posource = """#~ msgid "Old"\n#~ msgstr "Oud"\n"""
        newpo = self.convertpot(potsource, posource)
        assert len(newpo.units) == 3
        assert newpo.units[0].isheader()
        assert newpo.units[2].isobsolete()
        assert str(newpo.units[1]) == potsource
        assert str(newpo.units[2]) == posource

        # Now test with real units present in posource
        posource2 = """msgid "Old"\nmsgstr "Oud"\n"""
        newpo = self.convertpot(potsource, posource2)
        assert len(newpo.units) == 3
        assert newpo.units[0].isheader()
        assert newpo.units[2].isobsolete()
        assert str(newpo.units[1]) == potsource
        assert str(newpo.units[2]) == posource

    def test_merging_resurect_obsolete_messages(self):
        """Check that we can reuse old obsolete messages if the message comes back."""
        potsource = """#: resurect.c\nmsgid "&About"\nmsgstr ""\n"""
        posource = """#~ msgid "&About"\n#~ msgstr "&Omtrent"\n"""
        expected = """#: resurect.c\nmsgid "&About"\nmsgstr "&Omtrent"\n"""
        newpo = self.convertpot(potsource, posource)
        print(newpo)
        assert len(newpo.units) == 2
        assert newpo.units[0].isheader()
        newpounit = self.singleunit(newpo)
        assert str(newpounit) == expected

    def test_merging_resurect_obsolete_messages_into_msgidcomment(self):
        """Check that we can reuse old obsolete messages even if the recipient has a msgidcomment."""
        potsource = (
            """#: resurect1.c\nmsgid "About"\nmsgstr ""\n\n"""
            """#: resurect2.c\nmsgid ""\n"_: resurect2.c\\n"\n"About"\nmsgstr ""\n"""
        )
        posource = """#~ msgid "About"\n#~ msgstr "Omtrent"\n"""
        expected1 = """#: resurect1.c\nmsgid "About"\nmsgstr "Omtrent"\n"""
        expected2 = """#: resurect2.c\n#, fuzzy\nmsgid ""\n"_: resurect2.c\\n"\n"About"\nmsgstr "Omtrent"\n"""
        newpo = self.convertpot(potsource, posource)
        print(newpo)
        assert len(newpo.units) == 3
        assert newpo.units[0].isheader()
        assert str(newpo.units[1]) == expected1
        assert str(newpo.units[2]) == expected2

    def test_header_initialisation(self):
        """Test to check that we initialise the header correctly."""
        potsource = r"""#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"Report-Msgid-Bugs-To: new@example.com\n"
"POT-Creation-Date: 2006-11-11 11:11+0000\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=INTEGER; plural=EXPRESSION;\n"
"X-Generator: Translate Toolkit 0.10rc2\n"
"""
        posource = r"""msgid ""
msgstr ""
"Project-Id-Version: Pootle 0.10\n"
"Report-Msgid-Bugs-To: old@example.com\n"
"POT-Creation-Date: 2006-01-01 01:01+0100\n"
"PO-Revision-Date: 2006-09-09 09:09+0900\n"
"Last-Translator: Joe Translate <joe@example.com>\n"
"Language-Team: Pig Latin <piglatin@example.com>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\n"
"X-Generator: Translate Toolkit 0.9\n"
"""
        expected = r"""msgid ""
msgstr ""
"Project-Id-Version: Pootle 0.10\n"
"Report-Msgid-Bugs-To: new@example.com\n"
"POT-Creation-Date: 2006-11-11 11:11+0000\n"
"PO-Revision-Date: 2006-09-09 09:09+0900\n"
"Last-Translator: Joe Translate <joe@example.com>\n"
"Language-Team: Pig Latin <piglatin@example.com>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\n"
"X-Generator: Translate Toolkit 0.10rc2\n"
"""
        newpo = self.convertpot(potsource, posource)
        print(f"Output Header:\n{newpo}")
        print(f"Expected Header:\n{expected}")
        assert bytes(newpo).decode("utf-8") == expected

    def test_merging_comments(self):
        """Test that we can merge comments correctly."""
        potsource = """#. Don't do it!\n#: file.py:1\nmsgid "One"\nmsgstr ""\n"""
        posource = """#. Don't do it!\n#: file.py:2\nmsgid "One"\nmsgstr "Een"\n"""
        poexpected = """#. Don't do it!\n#: file.py:1\nmsgid "One"\nmsgstr "Een"\n"""
        newpo = self.convertpot(potsource, posource)
        print(newpo)
        newpounit = self.singleunit(newpo)
        assert str(newpounit) == poexpected

    def test_merging_typecomments(self):
        """Test that we can merge with typecomments."""
        potsource = """#: file.c:1\n#, c-format\nmsgid "%d pipes"\nmsgstr ""\n"""
        posource = """#: file.c:2\nmsgid "%d pipes"\nmsgstr "%d pype"\n"""
        poexpected = (
            """#: file.c:1\n#, c-format\nmsgid "%d pipes"\nmsgstr "%d pype"\n"""
        )
        newpo = self.convertpot(potsource, posource)
        newpounit = self.singleunit(newpo)
        print(newpounit)
        assert str(newpounit) == poexpected

        potsource = """#: file.c:1\n#, c-format\nmsgid "%d computers"\nmsgstr ""\n"""
        posource = """#: file.c:2\n#, c-format\nmsgid "%s computers "\nmsgstr "%s-rekenaars"\n"""
        poexpected = """#: file.c:1\n#, fuzzy, c-format\nmsgid "%d computers"\nmsgstr "%s-rekenaars"\n"""
        newpo = self.convertpot(potsource, posource)
        newpounit = self.singleunit(newpo)
        assert newpounit.isfuzzy()
        assert newpounit.hastypecomment("c-format")

    def test_msgctxt(self):
        """Test that msgctxt is migrated correctly."""
        potsource = """
#: something.h:5
msgctxt "context1"
msgid "text"
msgstr ""

#: something.h:6
msgctxt "context2"
msgid "text"
msgstr ""
"""
        posource = """
#: something.h:3
msgctxt "context0"
msgid "text"
msgstr "teks"

#: something.h:4
msgctxt "context1"
msgid "text"
msgstr "sms"
"""
        poexpected = """
#: something.h:5
msgctxt "context1"
msgid "text"
msgstr "sms"

#: something.h:6
#, fuzzy
msgctxt "context2"
msgid "text"
msgstr "teks"
"""
        newpo = self.convertpot(potsource, posource)
        print(newpo)
        assert poexpected in bytes(newpo).decode("utf-8")

    def test_msgctxt_multiline(self):
        """Test multiline msgctxt fields."""
        pot_source = r"""#. |1MV
#: ActionTe.ulf
msgctxt ""
"ActionTe.ulf\n"
"OOO_ACTIONTEXT_21\n"
"LngText.text"
msgid "Computing space requirements"
msgstr ""
"""

        po_source = r"""#. |1MV
#: ActionTe.ulf
msgctxt ""
"ActionTe.ulf\n"
"OOO_ACTIONTEXT_21\n"
"LngText.text"
msgid "Computing space requirements"
msgstr "A szükséges lemezterület kiszámítása"
"""

        new_po = self.convertpot(pot_source, po_source)
        assert new_po.units[0].isheader()
        unit = new_po.units[1]
        assert not unit.isfuzzy()
        assert po_source == str(unit)

    def test_msgid_merge_on_location(self):
        """Tests that unit merges rely on location-based matching."""
        pot_source = r"""
msgid ""
msgstr ""
"X-Merge-On: location\n"

#. $:am
#: ActionTe.ulf
msgctxt ""
"ActionTe.ulf\n"
"OOO_ACTIONTEXT_11\n"
"LngText.text"
msgid "Computing space requirements"
msgstr ""

#. NjJ3
#: ActionTe.ulf
msgctxt ""
"ActionTe.ulf\n"
"OOO_ACTIONTEXT_12\n"
"LngText.text"
msgid "Computing space requirements"
msgstr ""
"""

        po_source = r"""
#. $:am
#: ActionTe.ulf
msgctxt ""
"ActionTe.ulf\n"
"OOO_ACTIONTEXT_11\n"
"LngText.text"
msgid "Computing space requirements"
msgstr "A szükséges lemezterület kiszámítása"

#. NjJ3
#: ActionTe.ulf
msgctxt ""
"ActionTe.ulf\n"
"OOO_ACTIONTEXT_12\n"
"LngText.text"
msgid "Computing space requirements"
msgstr "A szükséges lemezterület kiszámítása"
"""

        new_po = self.convertpot(pot_source, po_source)

        assert len(new_po.units) == 3
        assert new_po.units[0].isheader()

        assert not new_po.units[1].isfuzzy()
        assert new_po.units[2].isfuzzy()

    def test_msgid_merge_on_id(self):
        """Tests that unit merges rely on location-based matching."""
        pot_source = r"""
msgid ""
msgstr ""
"X-Merge-On: id\n"

#. $:am
#: ActionTe.ulf
msgctxt ""
"ActionTe.ulf\n"
"OOO_ACTIONTEXT_11\n"
"LngText.text"
msgid "Computing space requirements"
msgstr ""

#. NjJ3
#: ActionTe.ulf
msgctxt ""
"ActionTe.ulf\n"
"OOO_ACTIONTEXT_12\n"
"LngText.text"
msgid "Computing space requirements"
msgstr ""
"""
        pot_source_noheader = r"""
#. $:am
#: ActionTe.ulf
msgctxt ""
"ActionTe.ulf\n"
"OOO_ACTIONTEXT_11\n"
"LngText.text"
msgid "Computing space requirements"
msgstr ""

#. NjJ3
#: ActionTe.ulf
msgctxt ""
"ActionTe.ulf\n"
"OOO_ACTIONTEXT_12\n"
"LngText.text"
msgid "Computing space requirements"
msgstr ""
"""

        po_source = r"""
#. $:am
#: ActionTe.ulf
msgctxt ""
"ActionTe.ulf\n"
"OOO_ACTIONTEXT_11\n"
"LngText.text"
msgid "Computing space requirements"
msgstr "A szükséges lemezterület kiszámítása"

#. NjJ3
#: ActionTe.ulf
msgctxt ""
"ActionTe.ulf\n"
"OOO_ACTIONTEXT_12\n"
"LngText.text"
msgid "Computing space requirements"
msgstr "A szükséges lemezterület kiszámítása"
"""

        for pot in (pot_source, pot_source_noheader):
            new_po = self.convertpot(pot, po_source)

            assert len(new_po.units) == 3
            assert new_po.units[0].isheader()

            assert not new_po.units[1].isfuzzy()
            assert not new_po.units[2].isfuzzy()

    def test_empty_msgid(self):
        """Test that we handle empty msgids correctly."""
        # TODO: this test will fail if we don't have the gettext location
        # comment in the pot file
        potsource = '#: file:1\nmsgctxt "bla"\nmsgid ""\nmsgstr ""\n'
        posource = r"""
msgid ""
"Project-Id-Version: Pootle 0.10\n"
msgstr ""

msgctxt "bla"
msgid ""
msgstr "trans"
"""
        newpo = self.convertpot(potsource, posource)
        print(newpo)
        assert len(newpo.units) == 2
        assert newpo.units[0].isheader()
        unit = newpo.units[1]
        assert unit.source == ""
        assert unit.getid() == "bla\04"
        assert unit.target == "trans"
        assert not unit.isfuzzy()

    def test_migrate_msgidcomment_to_msgctxt(self):
        """
        Test that we migrate correctly from msgidcomments to msgctxt.

        This is needed for our move away from using msgidcomments for mozilla.
        """
        potsource = r"""
msgid ""
msgstr ""
"X-Accelerator-Marker: &\n"
"X-Merge-On: location\n"


#: bla
msgctxt "bla"
msgid ""
msgstr ""
"""
        posource = r"""
msgid ""
msgstr ""
"Project-Id-Version: Pootle 0.10\n"
"X-Accelerator-Marker: &\n"


#: bla
msgid ""
"_: bla\n"
msgstr "trans"
"""
        newpo = self.convertpot(potsource, posource)
        print(newpo)
        assert len(newpo.units) == 2
        assert newpo.units[0].isheader()
        unit = newpo.units[1]
        assert unit.source == ""
        assert unit.getid() == "bla\04"
        assert unit.target == "trans"
        assert not unit.isfuzzy()

    def test_obsolete_msgctxt(self):
        """Test that obsolete units' msgctxt is preserved."""
        potsource = 'msgctxt "newContext"\nmsgid "First unit"\nmsgstr ""'
        posource = """
msgctxt "newContext"
msgid "First unit"
msgstr "Eerste eenheid"

#~ msgctxt "context"
#~ msgid "Old unit"
#~ msgstr "Ou eenheid1"

#~ msgctxt "context2"
#~ msgid "Old unit"
#~ msgstr "Ou eenheid2"

#~ msgid "Old unit"
#~ msgstr "Ou eenheid3"
"""
        newpo = self.convertpot(potsource, posource)
        print(newpo)
        assert len(newpo.units) == 5
        assert newpo.units[1].getcontext() == "newContext"
        # Search in unit string, because obsolete units can't return a context
        assert 'msgctxt "context"' in str(newpo.units[2])
        assert 'msgctxt "context2"' in str(newpo.units[3])

    def test_small_strings(self):
        """
        Test that units with small source strings are not incorrectly
        populated by means of fuzzy matching.
        """
        potsource = r"""#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"Report-Msgid-Bugs-To: new@example.com\n"
"POT-Creation-Date: 2006-11-11 11:11+0000\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=INTEGER; plural=EXPRESSION;\n"
"X-Accelerator-Marker: &\n"
"X-Generator: Translate Toolkit 0.10rc2\n"
"X-Merge-On: location\n"

#: new_disassociated_mozilla_accesskey
msgid "R"
msgstr ""
"""
        posource = r"""msgid ""
msgstr ""
"Project-Id-Version: Pootle 0.10\n"
"Report-Msgid-Bugs-To: old@example.com\n"
"POT-Creation-Date: 2006-01-01 01:01+0100\n"
"PO-Revision-Date: 2006-09-09 09:09+0900\n"
"Last-Translator: Joe Translate <joe@example.com>\n"
"Language-Team: Pig Latin <piglatin@example.com>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\n"
"X-Generator: Translate Toolkit 0.9\n"
"X-Accelerator-Marker: &\n"

#: old_disassociated_mozilla_accesskey
msgid "R"
msgstr "S"
"""
        expected = r"""msgid ""
msgstr ""
"Project-Id-Version: Pootle 0.10\n"
"Report-Msgid-Bugs-To: new@example.com\n"
"POT-Creation-Date: 2006-11-11 11:11+0000\n"
"PO-Revision-Date: 2006-09-09 09:09+0900\n"
"Last-Translator: Joe Translate <joe@example.com>\n"
"Language-Team: Pig Latin <piglatin@example.com>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\n"
"X-Accelerator-Marker: &\n"
"X-Generator: Translate Toolkit 0.10rc2\n"
"X-Merge-On: location\n"

#: new_disassociated_mozilla_accesskey
msgid "R"
msgstr ""
"""
        newpo = self.convertpot(potsource, posource)
        print(f"Output:\n{newpo}")
        print(f"Expected:\n{expected}")
        assert bytes(newpo).decode("utf-8") == expected


class TestPOT2POCommand(test_convert.TestConvertCommand, TestPOT2PO):
    """Tests running actual pot2po commands on files."""

    convertmodule = pot2po

    expected_options = [
        "-t TEMPLATE, --template=TEMPLATE",
        "-P, --pot",
        "--tm",
        "-s MIN_SIMILARITY, --similarity=MIN_SIMILARITY",
        "--nofuzzymatching",
    ]
