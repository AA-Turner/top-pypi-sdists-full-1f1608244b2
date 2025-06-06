# -*- coding: utf-8 -*-

"""
    pyap.source_US.data
    ~~~~~~~~~~~~~~~~~~~~

    This module provides regular expression definitions required for
    detecting US addresses.

    The module is expected to always contain 'full_address' variable containing
    all address parsing definitions.

    :copyright: (c) 2015 by Vladimir Goncharov.
    :license: MIT, see LICENSE for more details.
"""

import string
from typing import List
from typing import Optional


def str_list_to_upper_lower_regex(str_list: List[str]) -> str:
    regex = "|".join(set(str_list)).lower()
    for letter in string.ascii_lowercase:
        regex = regex.replace(
            letter, "[{upper}{lower}]".format(upper=letter.upper(), lower=letter)
        )

    return regex


space_div = r"(?:[\,\ ]{1,2}|$)"


"""Numerals from one to nine
Note: here and below we use syntax like '[Oo][Nn][Ee]'
instead of '(one)(?i)' to match 'One' or 'oNe' because
Python Regexps don't seem to support turning On/Off
case modes for subcapturing groups.
"""
zero_to_nine = r"""(?:
    [Zz][Ee][Rr][Oo]\ |[Oo][Nn][Ee]\ |[Tt][Ww][Oo]\ |
    [Tt][Hh][Rr][Ee][Ee]\ |[Ff][Oo][Uu][Rr]\ |
    [Ff][Ii][Vv][Ee]\ |[Ss][Ii][Xx]\ |
    [Ss][Ee][Vv][Ee][Nn]\ |[Ee][Ii][Gg][Hh][Tt]\ |
    [Nn][Ii][Nn][Ee]\ |[Tt][Ee][Nn]\ |
    [Ee][Ll][Ee][Vv][Ee][Nn]\ |
    [Tt][Ww][Ee][Ll][Vv][Ee]\ |
    [Tt][Hh][Ii][Rr][Tt][Ee][Ee][Nn]\ |
    [Ff][Oo][Uu][Rr][Tt][Ee][Ee][Nn]\ |
    [Ff][Ii][Ff][Tt][Ee][Ee][Nn]\ |
    [Ss][Ii][Xx][Tt][Ee][Ee][Nn]\ |
    [Ss][Ee][Vv][Ee][Nn][Tt][Ee][Ee][Nn]\ |
    [Ee][Ii][Gg][Hh][Tt][Ee][Ee][Nn]\ |
    [Nn][Ii][Nn][Ee][Tt][Ee][Ee][Nn]\ 
    )"""

# Numerals - 10, 20, 30 ... 90
ten_to_ninety = r"""(?:
    [Tt][Ee][Nn]\ |[Tt][Ww][Ee][Nn][Tt][Yy]\ |
    [Tt][Hh][Ii][Rr][Tt][Yy]\ |
    [Ff][Oo][Rr][Tt][Yy]\ |
    [Ff][Oo][Uu][Rr][Tt][Yy]\ |
    [Ff][Ii][Ff][Tt][Yy]\ |[Ss][Ii][Xx][Tt][Yy]\ |
    [Ss][Ee][Vv][Ee][Nn][Tt][Yy]\ |
    [Ee][Ii][Gg][Hh][Tt][Yy]\ |
    [Nn][Ii][Nn][Ee][Tt][Yy]\ 
    )"""

# One hundred
hundred = r"""(?:
    [Hh][Uu][Nn][Dd][Rr][Ee][Dd]\ 
    )"""

# One thousand
thousand = r"""(?:
    [Tt][Hh][Oo][Uu][Ss][Aa][Nn][Dd]\ 
    )"""

"""
Regexp for matching street number.
Street number can be written 2 ways:
1) Using letters - "One thousand twenty two"
2) Using numbers
   a) - "1022"
   b) - "85-1190"
   c) - "85 1190"
   d) - 5214F
"""
street_number = r"""(?P<street_number>
                        \b(?:
                            [Aa][Nn][Dd]\ 
                            |
                            {thousand}
                            |
                            {hundred}
                            |
                            {zero_to_nine}
                            |
                            {ten_to_ninety}
                        ){from_to}
                        |
                        (?:\b\d{from_to}(?:\-?(?:\d{from_to}|[A-Z]))?\ )
                    )
                """.format(
    thousand=thousand,
    hundred=hundred,
    zero_to_nine=zero_to_nine,
    ten_to_ninety=ten_to_ninety,
    from_to="{1,5}",
)

"""
Regexp for matching street name.
In example below:
"Hoover Boulevard": "Hoover" is a street name
"""
# Seems like the longest street names in the US are
# 'Jean Baptiste Point du Sable Lake Shore Drive' and
# 'Northeast Kentucky Industrial Parkway'
# https://atkinsbookshelf.wordpress.com/tag/longest-street-name-in-us/
# On the other hand, there are streets like "Ed Drive" and "M Street".
street_name_multi_word_re = r"""
            (?:
                \b[a-zA-Z0-9\ \.\-\'\’]{3,41}|\b[A-Z][A-Za-z]?(?=\ [A-Z])
            )(?<![Pp][Hh][Oo][Nn][Ee])
"""

# This pattern should be quite conservative because it will be followed by
# optional matchers - we want to avoid matching too much with this.
street_name_one_word_re = r"(?:[A-Z][A-Za-z]{,15})"


interstate_specs = [
    r"Service\ Road",
]


interstate_street_type = r"""
            (?:
                [Ii]\-\ ?\d{{1,4}}
                |
                [Ii][Nn][Tt][Ee][Rr][Ss][Tt][Aa][Tt][Ee]\ *\d{{1,4}}
            )
            (?:
                {space_div}{optional_interstate_specs}
            )?
""".format(
    space_div=space_div,
    optional_interstate_specs=str_list_to_upper_lower_regex(interstate_specs),
)

highway_re = r"""(?:[Hh][Ii][Gg][Hh][Ww][Aa][Yy]\ +\d{1,4})"""

post_direction_re = r"""
                (?:
                    (?:
                        [Nn][Oo][Rr][Tt][Hh]|
                        [Ss][Oo][Uu][Tt][Hh]|
                        [Ee][Aa][Ss][Tt]|
                        [Ww][Ee][Ss][Tt]
                    )
                    |
                    \b(?:NW|NE|SW|SE)\b
                    |
                    \b(?:N\.W\.|N\.E\.|S\.W\.|S\.E\.)
                    |
                    \b(?:N|S|E|W)\b\.?
                )
                """

numbered_avenue_re = r"""
                (?:{post_direction_re}\ [Aa][Vv][Ee](?:\.|[Nn][Uu][Ee])?\ \d{{1,2}})
""".format(
    post_direction_re=post_direction_re
)


single_street_name_list = [
    "Broadway",
    "Highpoint",
    "Parkway",
    r"Black\ Hou?rse",
]

numbered_road_re = r"""[Ss][Tt][Aa][Tt][Ee]\ [Rr][Oo][Aa][Dd]\ \d{1,4}(?!\d)"""

# Used to handle edge cases where streets don't have a street type:
# eg. `55 HIGHPOINT`, `600 HIGHWAY 32`
numbered_or_typeless_street_name = r"""
    (?P<typeless_street_name>
        (?:{post_direction_re}{space_div})?
        (?:
            {single_street_name_regex}
            |
            [Aa][Tt]\ {interstate_street_type}
            |
            {highway_re}
            |
            {numbered_avenue_re}
            |
            {numbered_road_re}
        )
    )
""".format(
    post_direction_re=post_direction_re,
    space_div=space_div,
    single_street_name_regex=str_list_to_upper_lower_regex(single_street_name_list),
    interstate_street_type=interstate_street_type,
    highway_re=highway_re,
    numbered_avenue_re=numbered_avenue_re,
    numbered_road_re=numbered_road_re,
)

post_direction = r"""
                    (?P<post_direction>
                        {post_direction_re}
                    )
                """.format(
    post_direction_re=post_direction_re
)

# This list was taken from: https://pe.usps.com/text/pub28/28apc_002.htm
# Bay, Broadway and Lp (abbreviation for Loop) were added to the list
street_type_list = [
    "Allee",
    "Alley",
    "Ally",
    "Aly",
    "Anex",
    "Annex",
    "Annx",
    "Anx",
    "Arc",
    "Arcade",
    "Av",
    "Ave",
    "Aven",
    "Avenu",
    "Avenue",
    "Avn",
    "Avnue",
    "Bay(?!\ [1-9])",
    "Bayoo",
    "Bayou",
    "Bch",
    "Beach",
    "Bend",
    "Bg",
    "Bgs",
    "Bl",
    "Blf",
    "Blfs",
    "Bluf",
    "Bluff",
    "Bluffs",
    "Blvd",
    "Bnd",
    "Bot",
    "Bottm",
    "Bottom",
    "Boul",
    "Boulevard",
    "Boulv",
    "Br",
    "Branch",
    "Brdge",
    "Brg",
    "Bridge",
    "Brk",
    "Brks",
    "Brnch",
    "Broadway",
    "Brook",
    "Brooks",
    "Btm",
    "Burg",
    "Burgs",
    "Bvd",
    "Byp",
    "Bypa",
    "Bypas",
    "Bypass",
    "Byps",
    "Byu",
    "Camp",
    "Canyn",
    "Canyon",
    "Cape",
    "Causeway",
    "Causwa",
    "Cen",
    "Cent",
    "Center",
    "Centers",
    "Centr",
    "Centre",
    "Cir",
    "Circ",
    "Circl",
    "Circle",
    "Circles",
    "Cirs",
    "Clb",
    "Clf",
    "Clfs",
    "Cliff",
    "Cliffs",
    "Club",
    "Cmn",
    "Cmns",
    "Cmp",
    "Cnter",
    "Cntr",
    "Cnyn",
    "Common",
    "Commons",
    "Cor",
    "Corner",
    "Corners",
    "Cors",
    "Course",
    "Court",
    "Courts",
    "Cove",
    "Coves",
    "Cp",
    "Cpe",
    "Crcl",
    "Crcle",
    "Creek",
    "Cres",
    "Crescent",
    "Crest",
    "Crk",
    "Crossing",
    "Crossroad",
    "Crossroads",
    "Crse",
    "Crsent",
    "Crsnt",
    "Crssng",
    "Crst",
    "Cswy",
    "Ct",
    "Ctr",
    "Ctrs",
    "Cts",
    "Curv",
    "Curve",
    r"Cut\ Off",
    "Cv",
    "Cvs",
    "Cyn",
    "Dale",
    "Dam",
    "Div",
    "Divide",
    "Dl",
    "Dm",
    "Dr",
    "Driv",
    "Drive",
    "Drives",
    "Drs",
    "Drv",
    "Dv",
    "Dvd",
    "Est",
    "Estate",
    "Estates",
    "Ests",
    "Exp",
    "Expr",
    "Express",
    "Expressway",
    "Expw",
    "Expy",
    "Ext",
    "Extension",
    "Extensions",
    "Extn",
    "Extnsn",
    "Exts",
    "Fall",
    "Falls",
    "Ferry",
    "Field",
    "Fields",
    "Flat",
    "Flats",
    "Fld",
    "Flds",
    "Fls",
    "Flt",
    "Flts",
    "Ford",
    "Fords",
    "Forest",
    "Forests",
    "Forg",
    "Forge",
    "Forges",
    "Fork",
    "Forks",
    "Fort",
    "Frd",
    "Frds",
    "Freeway",
    "Freewy",
    "Frg",
    "Frgs",
    "Frk",
    "Frks",
    "Frry",
    "Frst",
    "Frt",
    "Frway",
    "Frwy",
    "Fry",
    "Ft",
    "Fwy",
    "Garden",
    "Gardens",
    "Gardn",
    "Gateway",
    "Gatewy",
    "Gatway",
    "Gdn",
    "Gdns",
    "Glen",
    "Glens",
    "Gln",
    "Glns",
    "Grden",
    "Grdn",
    "Grdns",
    "Green",
    "Greens",
    "Grn",
    "Grns",
    "Grov",
    "Grove",
    "Groves",
    "Grv",
    "Grvs",
    "Gtway",
    "Gtwy",
    "Harb",
    "Harbor",
    "Harbors",
    "Harbr",
    "Haven",
    "Hbr",
    "Hbrs",
    "Heights",
    "Highway",
    "Highwy",
    "Hill",
    "Hills",
    "Hiway",
    "Hiwy",
    "Hl",
    "Hllw",
    "Hls",
    "Hollow",
    "Hollows",
    "Holw",
    "Holws",
    "Hrbor",
    "Ht",
    "Hts",
    "Hvn",
    "Hway",
    "Hwy",
    "Inlet",
    "Inlt",
    "Is",
    "Island",
    "Islands",
    "Isle",
    "Isles",
    "Islnd",
    "Islnds",
    "Iss",
    "Jct",
    "Jction",
    "Jctn",
    "Jctns",
    "Jcts",
    "Junction",
    "Junctions",
    "Junctn",
    "Juncton",
    "Key",
    "Keys",
    "Knl",
    "Knls",
    "Knol",
    "Knoll",
    "Knolls",
    "Ky",
    "Kys",
    "Lake",
    "Lakes",
    "Land",
    "Landing",
    "Lane",
    "Lck",
    "Lcks",
    "Ldg",
    "Ldge",
    "Lf",
    "Lgt",
    "Lgts",
    "Light",
    "Lights",
    "Lk",
    "Lks",
    "Ln",
    "Lndg",
    "Lndng",
    "Loaf",
    "Lock",
    "Locks",
    "Lodg",
    "Lodge",
    "Loop",
    "Loops",
    "Lp",
    "Mall",
    "Manor",
    "Manors",
    "Mdw",
    "Mdws",
    "Meadow",
    "Meadows",
    "Medows",
    "Mews",
    "Mill",
    "Mills",
    "Mission",
    "Missn",
    "Ml",
    "Mls",
    "Mnr",
    "Mnrs",
    "Mnt",
    "Mntain",
    "Mntn",
    "Mntns",
    "Motorway",
    "Mount",
    "Mountain",
    "Mountains",
    "Mountin",
    "Msn",
    "Mssn",
    "Mt",
    "Mtin",
    "Mtn",
    "Mtns",
    "Mtwy",
    "Nck",
    "Neck",
    "Opas",
    "Orch",
    "Orchard",
    "Orchrd",
    "Oval",
    "Overpass",
    "Ovl",
    "Park",
    "Parks",
    "Parkway",
    "Parkways",
    "Parkwy",
    "Pass",
    "Passage",
    "Path",
    "Paths",
    "Pike",
    "Pikes",
    "Pine",
    "Pines",
    "Pk",
    "Pkway",
    "Pkwy",
    "Pkwys",
    "Pky",
    "Pl",
    "Place",
    "Plain",
    "Plains",
    "Plaza",
    "Pln",
    "Plns",
    "Plz",
    "Plza",
    "Pne",
    "Pnes",
    "Point",
    "Points",
    "Port",
    "Ports",
    "Pr",
    "Prairie",
    "Prk",
    "Promenade",
    "Prr",
    "Prt",
    "Prts",
    "Psge",
    "Pt",
    "Pts",
    "Rad",
    "Radial",
    "Radiel",
    "Radl",
    "Ramp",
    "Ranch",
    "Ranches",
    "Rapid",
    "Rapids",
    "Rd",
    "Rdg",
    "Rdge",
    "Rdgs",
    "Rds",
    "Rest",
    "Ridge",
    "Ridges",
    "Riv",
    "River",
    "Rivr",
    "Rnch",
    "Rnchs",
    "Road",
    "Roads",
    "Route",
    "Row",
    "Rpd",
    "Rpds",
    "Rst",
    "Rte",
    "Rue",
    "Run",
    "Rvr",
    "Shl",
    "Shls",
    "Shoal",
    "Shoals",
    "Shoar",
    "Shoars",
    "Shore",
    "Shores",
    "Shr",
    "Shrs",
    "Skwy",
    "Skyway",
    "Smt",
    "Spg",
    "Spgs",
    "Spng",
    "Spngs",
    "Spring",
    "Springs",
    "Sprng",
    "Sprngs",
    "Spur",
    "Spurs",
    "Sq",
    "Sqr",
    "Sqre",
    "Sqrs",
    "Sqs",
    "Squ",
    "Square",
    "Squares",
    "St",
    "Sta",
    "Station",
    "Statn",
    "Stn",
    "Str",
    "Stra",
    "Strav",
    "Straven",
    "Stravenue",
    "Stravn",
    "Stream",
    "Street",
    "Streets",
    "Streme",
    "Strm",
    "Strt",
    "Strvn",
    "Strvnue",
    "Sts",
    "Sumit",
    "Sumitt",
    "Summit",
    "Ter",
    "Terr",
    "Terrace",
    "Throughway",
    "Tpke",
    "Trace",
    "Traces",
    "Track",
    "Tracks",
    "Trafficway",
    "Trail",
    "Trailer",
    "Trails",
    "Trak",
    "Trce",
    "Trfy",
    "Trk",
    "Trks",
    "Trl",
    "Trlr",
    "Trlrs",
    "Trls",
    "Trnpk",
    "Trwy",
    "Tunel",
    "Tunl",
    "Tunls",
    "Tunnel",
    "Tunnels",
    "Tunnl",
    "Turnpike",
    "Turnpk",
    "Un",
    "Underpass",
    "Union",
    "Unions",
    "Uns",
    "Upas",
    "Valley",
    "Valleys",
    "Vally",
    "Vdct",
    "Via",
    "Viadct",
    "Viaduct",
    "View",
    "Views",
    "Vill",
    "Villag",
    "Village",
    "Villages",
    "Ville",
    "Villg",
    "Villiage",
    "Vis",
    "Vist",
    "Vista",
    "Vl",
    "Vlg",
    "Vlgs",
    "Vlly",
    "Vly",
    "Vlys",
    "Vst",
    "Vsta",
    "Vw",
    "Vws",
    "Walk",
    "Walks",
    "Wall",
    "Way",
    "Ways",
    "Well",
    "Wells",
    "Wl",
    "Wls",
    "Wy",
    "Xing",
    "Xrd",
    "Xrds",
]

street_type_leading_list = ["Camino", "El\ Camino", "Avenue"]


def street_type_list_to_regex(street_type_list: list[str]) -> str:
    """Converts a list of street types into a regex"""
    street_types = str_list_to_upper_lower_regex(street_type_list)

    # Use \b to check that there are word boundaries before and after the street type
    # Optionally match zero to two of " ", ",", or "." after the street name
    street_types = street_types.replace("|", r"\b|\b")
    street_types = r"\b" + r"(?:" + street_types + r")" + r"\b\.?"
    return street_types


street_types_re = street_type_list_to_regex(street_type_list)

street_types_with_interstate_re = rf"{street_types_re}|{interstate_street_type}"

street_types_leading_re = street_type_list_to_regex(street_type_leading_list)

street_type_extended = r"""
            (?:
                {street_type_a}
                (?P<route_id>
                    {space_div}\(?[Rr][Oo][Uu][Tt][Ee]\ [A-Za-z0-9]+(?:\ ?\))?
                )?
            )
""".format(
    street_type_a=rf"(?P<street_type_a>{street_types_with_interstate_re})",
    space_div=space_div,
)


typed_street_name = r"""
            (?:      
                (?:{street_name_a}{space_div}{street_type_a})
                |
                (?:
                    (?:{post_direction_re}{space_div})?
                    {street_type_b}{space_div}{street_name_b}
                )
            )
""".format(
    space_div=space_div,
    street_name_a=rf"(?P<street_name_a>{street_name_multi_word_re})",
    street_type_a=street_type_extended,
    street_type_b=rf"(?P<street_type_b>{street_types_leading_re})",
    street_name_b=rf"(?P<street_name_b>{street_name_one_word_re})",
    post_direction_re=post_direction_re,
)

floor_indic = r"""
            (?:
                (?:[Ff][Ll][Oo][Oo][Rr]|[Ff][Ll][Rr]?\.?)
                (?:\ (?:[Hh][Oo][Rr][Ii][Zz][Oo][Nn][Tt][Aa][Ll]|[Hh][Oo][Rr][Ii][Zz]))?
            )
        """

floor = r"""
            (?P<floor>
                (?:
                    (?:\d+|\d-\d)[A-Za-z]{{0,2}}\.?\ {floor_indic}
                )
                |
                (?:
                    {floor_indic}\ \d+[A-Za-z]{{0,2}}
                )
            )
        """.format(
    floor_indic=floor_indic
)

building = r"""
            (?P<building_id>
                (?:
                    (?:[Bb][Uu][Ii][Ll][Dd][Ii][Nn][Gg])\.?
                    |
                    (?:[Bb][Ll][Dd][Gg])\.?
                    |
                    (?:[Bb][Ll][Vv])\.?
                )
                \ 
                (?:
                    (?:
                        [Aa][Nn][Dd]\ 
                        |
                        {thousand}
                        |
                        {hundred}
                        |
                        {zero_to_nine}
                        |
                        {ten_to_ninety}
                    ){{1,5}}
                    |
                    \d{{0,4}}(?:\.\d)?[A-Za-z]?[XxVvIi]{{0,4}}
                )
            )
            """.format(
    thousand=thousand,
    hundred=hundred,
    zero_to_nine=zero_to_nine,
    ten_to_ninety=ten_to_ninety,
)

occupancy_details = r"(?:[A-Za-z\#\&\-\d]{1,7}(?:\s?[SWNE])?)"

occupancy = r"""
            (?P<occupancy>
                (?:
                    (?:
                        (?:
                            # Suite
                            [Ss][Uu][Ii][Tt][Ee]
                            |
                            # Apartment
                            [Aa][Pp][Tt]|[Aa][Pp][Aa][Rr][Tt][Mm][Ee][Nn][Tt]
                            |
                            # Room
                            [Rr][Oo][Oo][Mm]|[Rr][Mm]
                            |
                            # Unit
                            [Uu][Nn][Ii][Tt]
                            |
                            # Place
                            [Pp][Ll][Aa][Cc][Ee]|[Pp][Ll]
                            |
                            # Bay
                            [Bb][Aa][Yy]
                            |
                            # Site
                            [Ss][Ii][Tt][Ee]
                        )\b[\ \,\.]+
                        {occupancy_details}? 
                        |
                        \d{{2,4}}\ [Ss][Tt][Ee](?:\ \*)?
                    )
                    |
                    (?:
                        \#\ ?[0-9]{{,4}}[A-Za-z]{{1}}
                    )
                    |
                    (?:
                        \#?\ ?[0-9]{{1,4}}
                    )
                    |
                    (?:\b\d{{2}}-\d{{4}})
                    |
                    (?:
                        # Other Suite case
                        # it needs to be separated to ensure `occupancy_details`
                        # is present because otherwise it would match stuff like
                        # the `ST.` in `ST. LOUIS`
                        [Ss][Tt][Ee]?\b[\ \,\.]+{occupancy_details}
                    )
                )
            )
            """.format(
    occupancy_details=occupancy_details
)

mail_stop = r"""
            (?P<mail_stop>
                # attention: do not to mix up with postal code
                MSC?:?\s[A-Z]{,4}\s?\d{3,4}\b
            )
            """

po_box = r"""
            (?:
                [Pp]\.?\ ?[Oo]\.?\ ?
                |
                [Pp][Oo][Ss][Tt]\ [Oo][Ff][Ff][Ii][Cc][Ee]\ ?
            )?
            (?:
                (?:
                    (?:
                        [Bb][Oo][Xx]
                        |
                        [Pp][Mm][Bb]
                    )
                    \ \#?\ ?A?\d+
                )
                |
                (?:[Dd][Rr][Aa][Ww][Ee][Rr]\ +[A-Z]\b)
            )
        """

phone_number = r"""
            (?:
                \*?(?:[Pp][Hh]\ )?
                (?P<phone_number>
                    \(?\d{3}\)?\-?\ ?\d{3}\-?\ ?\-?\d{4}
                )
            )
            """

part_div = r"(?:[\,\s]{1,3}|\ \-\ |$)"  # allows for line breaks

full_street = r"""
    (?:
        (?P<full_street>
            (?:
                (?:(?P<po_box_b>{po_box}){part_div})?
                {street_number}{space_div}?
                (?:
                    (?:{numbered_or_typeless_street_name})
                    |
                    (?:{typed_street_name}(?![A-Za-z\d\.]))
                    |
                    (?:
                        {post_direction_re}\ 
                        \d{{,3}}[A-Za-z\-]{{1,31}}
                    )
                )
                (?:{space_div}{post_direction})?
                (?:{part_div}{floor})?
                (?:{part_div}{building})?
                (?:{part_div}?{occupancy})?
                (?:{part_div}{mail_stop})?
                (?:{part_div}(?P<po_box_a>{po_box}))?
            )
            |
            (?P<po_box_c>{po_box})
        )
    )""".format(
    space_div=space_div,
    part_div=part_div,
    street_number=street_number,
    typed_street_name=typed_street_name,
    numbered_or_typeless_street_name=numbered_or_typeless_street_name,
    post_direction=post_direction,
    post_direction_re=post_direction_re,
    floor=floor,
    building=building,
    occupancy=occupancy,
    mail_stop=mail_stop,
    po_box=po_box,
)


def states_abbrvs_regex() -> str:
    # Some abbreviations are non-standard
    _STATE_ABBRS = {
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DE",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI(?:CH)?\.?",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY|N\.Y\.",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WV",
        "WI",
        "WY",
    }
    _NON_STATE_ABBRS = {
        "AS",
        "GU",
        "MP",
        "PR",
        "VI",
        "D\.?C\.?",
    }
    return (
        r"(?:"
        + str_list_to_upper_lower_regex(list(_STATE_ABBRS | _NON_STATE_ABBRS))
        + r")(?![A-Za-z])"
    )


# region1 is actually a "state"
def make_region1(idx: Optional[str] = None):
    maybe_idx = f"_{idx}" if idx else ""
    return r"""
        (?P<region1{maybe_idx}>
            (?:
                # states full
                [Aa][Ll][Aa][Bb][Aa][Mm][Aa]|
                [Aa][Ll][Aa][Ss][Kk][Aa]|
                [Aa][Rr][Ii][Zz][Oo][Nn][Aa]|
                [Aa][Rr][Kk][Aa][Nn][Ss][Aa][Ss]|
                [Cc][Aa][Ll][Ii][Ff][Oo][Rr][Nn][Ii][Aa]|
                [Cc][Oo][Ll][Oo][Rr][Aa][Dd][Oo]|
                [Cc][Oo][Nn][Nn][Ee][Cc][Tt][Ii][Cc][Uu][Tt]|
                [Dd][Ee][Ll][Aa][Ww][Aa][Rr][Ee]|
                [Dd][Ii][Ss][Tt][Rr][Ii][Cc][Tt]\ [Oo][Ff]\ 
                [Cc][Oo][Ll][Uu][Mm][Bb][Ii][Aa]|
                [Ff][Ll][Oo][Rr][Ii][Dd][Aa]|
                [Gg][Ee][Oo][Rr][Gg][Ii][Aa]|
                [Hh][Aa][Ww][Aa][Ii][Ii]|
                [Ii][Dd][Aa][Hh][Oo]|
                [Ii][Ll][Ll][Ii][Nn][Oo][Ii][Ss]|
                [Ii][Nn][Dd][Ii][Aa][Nn][Aa]|
                [Ii][Oo][Ww][Aa]|
                [Kk][Aa][Nn][Ss][Aa][Ss]|
                [Kk][Ee][Nn][Tt][Uu][Cc][Kk][Yy]|
                [Ll][Oo][Uu][Ii][Ss][Ii][Aa][Nn][Aa]|
                [Mm][Aa][Ii][Nn][Ee]|
                [Mm][Aa][Rr][Yy][Ll][Aa][Nn][Dd]|
                [Mm][Aa][Ss][Ss][Aa][Cc][Hh][Uu][Ss][Ee][Tt][Tt][Ss]|
                [Mm][Ii][Cc][Hh][Ii][Gg][Aa][Nn]|
                [Mm][Ii][Nn][Nn][Ee][Ss][Oo][Tt][Aa]|
                [Mm][Ii][Ss][Ss][Ii][Ss][Ss][Ii][Pp][Pp][Ii]|
                [Mm][Ii][Ss][Ss][Oo][Uu][Rr][Ii]|
                [Mm][Oo][Nn][Tt][Aa][Nn][Aa]|
                [Nn][Ee][Bb][Rr][Aa][Ss][Kk][Aa]|
                [Nn][Ee][Vv][Aa][Dd][Aa]|
                [Nn][Ee][Ww]\ [Hh][Aa][Mm][Pp][Ss][Hh][Ii][Rr][Ee]|
                [Nn][Ee][Ww]\ [Jj][Ee][Rr][Ss][Ee][Yy]|
                [Nn][Ee][Ww]\ [Mm][Ee][Xx][Ii][Cc][Oo]|
                [Nn][Ee][Ww]\ [Yy][Oo][Rr][Kk]|
                [Nn][Oo][Rr][Tt][Hh]\ [Cc][Aa][Rr][Oo][Ll][Ii][Nn][Aa]|
                [Nn][Oo][Rr][Tt][Hh]\ [Dd][Aa][Kk][Oo][Tt][Aa]|
                [Oo][Hh][Ii][Oo]|
                [Oo][Kk][Ll][Aa][Hh][Oo][Mm][Aa]|
                [Oo][Rr][Ee][Gg][Oo][Nn]|
                [Pp][Ee][Nn][Nn][Ss][Yy][Ll][Vv][Aa][Nn][Ii][Aa]|
                [Rr][Hh][Oo][Dd][Ee]\ [Ii][Ss][Ll][Aa][Nn][Dd]|
                [Ss][Oo][Uu][Tt][Hh]\ [Cc][Aa][Rr][Oo][Ll][Ii][Nn][Aa]|
                [Ss][Oo][Uu][Tt][Hh]\ [Dd][Aa][Kk][Oo][Tt][Aa]|
                [Tt][Ee][Nn][Nn][Ee][Ss][Ss][Ee][Ee]|
                [Tt][Ee][Xx][Aa][Ss]|
                [Uu][Tt][Aa][Hh]|
                [Vv][Ee][Rr][Mm][Oo][Nn][Tt]|
                [Vv][Ii][Rr][Gg][Ii][Nn][Ii][Aa]|
                [Ww][Aa][Ss][Hh][Ii][Nn][Gg][Tt][Oo][Nn]|
                [Ww][Ee][Ss][Tt]\ [Vv][Ii][Rr][Gg][Ii][Nn][Ii][Aa]|
                [Ww][Ii][Ss][Cc][Oo][Nn][Ss][Ii][Nn]|
                [Ww][Yy][Oo][Mm][Ii][Nn][Gg]|
                # unincorporated & commonwealth territories
                [Aa][Mm][Ee][Rr][Ii][Cc][Aa][Nn]\ [Ss][Aa][Mm][Oo][Aa]
                |[Gg][Uu][Aa][Mm]|
                [Nn][Oo][Rr][Tt][Hh][Ee][Rr][Nn]\ [Mm][Aa][Rr][Ii][Aa][Nn][Aa]\ 
                [Ii][Ss][Ll][Aa][Nn][Dd][Ss]|
                [Pp][Uu][Ee][Rr][Tt][Oo]\ [Rr][Ii][Cc][Oo]|
                [Vv][Ii][Rr][Gg][Ii][Nn]\ [Ii][Ss][Ll][Aa][Nn][Dd][Ss]
            )
            |
            (?:
                # states abbreviations
                {state_abbrvs}
            )
        )
        """.format(
        state_abbrvs=states_abbrvs_regex(), maybe_idx=maybe_idx
    )


# TODO: doesn't catch cities containing French characters
# We require short city names to contain a vowel
city = r"""
        (?P<city>
            [A-Za-z]{1}[a-zA-Z\ \-\'\.]{3,20}?
            |
            N\.?Y\.?
            |
            [AaEeIiUuOo][A-Za-z]{2}
            |
            [A-Za-z][AaEeIiUuOo][A-Za-z]
            |
            [A-Za-z]{2}[AaEeIiUuOoYy]
        )
        """

postal_code_re = r"""(?:\d{5}(?:\-\d{4})?(?!\d))"""
postal_code = rf"""(?P<postal_code>{postal_code_re})"""


def make_country(idx: Optional[str] = None) -> str:
    maybe_idx = f"_{idx}" if idx else ""
    return rf"""
            (?P<country{maybe_idx}>
                [Uu]\.?[Ss]\.?(?:[Aa]\.?)?|
                [Uu][Nn][Ii][Tt][Ee][Dd]\ [Ss][Tt][Aa][Tt][Ee][Ss](?:\ [Oo][Ff]\ [Aa][Mm][Ee][Rr][Ii][Cc][Aa])?
            )
            """


def make_region1_postal_code(
    part_div: str = part_div, postal_code: str = postal_code
) -> str:
    """This should match region1 (state) and postal code each at most once,
    but require at least one of the two."""

    def _indexed_region1(idx: Optional[str] = None):
        return rf"""(?:{part_div} {make_region1(idx)})"""

    _postal_code = f"""(?:{part_div}|\-)? {postal_code}"""
    return rf"""
            (?:{_indexed_region1("a")}?(?:{part_div}{make_country("b")})?{_postal_code}{_indexed_region1("b")}?
            |{_indexed_region1("c")}(?![-,.\sA-Za-z]{{0,10}}{postal_code_re}))
        """


region1_postal_code = make_region1_postal_code()


def make_full_address(
    *,
    full_street: str = full_street,
    part_div: str = part_div,
    city: str = city,
    region1_postal_code: str = region1_postal_code,
    country: Optional[str] = None,
    phone_number: str = phone_number,
) -> str:

    return r"""
                (?P<full_address>
                    {full_street}
                    (?:{part_div} {phone_number})?
                    {part_div}{city}
                    {region1_postal_code}
                    (?:{part_div} {country})?
                )
                """.format(
        full_street=full_street,
        part_div=part_div,
        city=city,
        region1_postal_code=region1_postal_code,
        country=country or make_country("a"),
        phone_number=phone_number,
    )


full_address = make_full_address()
