# -*- coding: utf-8 -*-
"""Test pypostal near_dupe."""

from __future__ import unicode_literals

import unittest
from postal.near_dupe import near_dupe_hashes


class TestExpand(unittest.TestCase):
    """Test expansions."""

    def contained_in_hashes(self, address, output, **kw):
        """Test whether an expansion contains a particular output."""
        hashes = near_dupe_hashes(address.keys(), address.values(), **kw)
        self.assertTrue(hashes)

        hashes = set(expansions)
        self.assertTrue(output in expansions)

    def have_hash_in_common(self, address1, address2, **kw):
        """Test whether strings have at least one shared expansion."""
        expansions1 = near_dupe_hashes(address1.keys(), address1.values(), **kw)
        expansions2 = near_dupe_hashes(address2.keys(), address2.values(), **kw)

        self.assertTrue(set(expansions1) & set(expansions2))

    def test_expansions(self):
        """Near-dupe tests"""

        self.have_hash_in_common({'house': 'National Association for the Advancement of Colored People', 'postcode': '12345'}, {'house': 'NAACP', 'postcode': '12345'}, languages=['en'])


        self.contained_in_expansions('781 Franklin Ave Crown Hts Brooklyn NY', '781 franklin avenue crown heights brooklyn new york')

        self.have_expansion_in_common('Thirty W 26th St Fl #7', '30 West Twenty-sixth Street Floor Number 7', languages=['en'])

        self.contained_in_expansions('Friedrichstraße 128, Berlin, Germany', 'friedrich strasse 128 berlin germany')

        self.contained_in_expansions('MAPLE ST.', 'maple street')
        self.contained_in_expansions('ST ISIDORE DR', 'saint isidore drive')
        self.contained_in_expansions('ST. Sebastian ST', 'saint sebastian street')
        self.contained_in_expansions("St John's St.", 'saint johns street')
        self.contained_in_expansions('MORNINGTON CR', 'mornington crescent')
        self.contained_in_expansions('Cércle rouge', 'cercle rouge')
        self.contained_in_expansions('Third St', '3rd street')

        self.contained_in_expansions('123 Dr. MLK Jr. Dr.', '123 doctor martin luther king junior drive')

        self.has_exact_expansions('120 Malcolm X Blvd', ['120 malcolm x boulevard'], roman_numerals=False)

if __name__ == '__main__':
    unittest.main()
