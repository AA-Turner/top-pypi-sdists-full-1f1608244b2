from enum import unique
from typing import Optional, Union

from ..._tools import make_enum_arg_parser_by_members
from ..._base_enum import StrEnum


@unique
class CountryCode(StrEnum):
    """
    List of ISO 3166 country codes.

    'G:7R' is unique country code for Afghanistan
    """

    AFG = "G:7R"
    ALB = "G:7G"
    DZA = "G:7S"
    ASM = "G:39"
    AND = "G:32"
    AGO = "G:82"
    AIA = "G:1H"
    ATA = "G:AY"
    ATG = "G:31"
    ARG = "G:60"
    ARM = "G:7I"
    ABW = "G:AD"
    AUS = "G:2H"
    AUT = "G:1F"
    AZE = "G:4R"
    BHS = "G:5E"
    BHR = "G:5Q"
    BGD = "G:9B"
    BRB = "G:8P"
    BLR = "G:8B"
    BEL = "G:9Y"
    BLZ = "G:6C"
    BEN = "G:48"
    BMU = "G:75"
    BTN = "G:8F"
    BOL = "G:3J"
    BIH = "G:2D"
    BWA = "G:61"
    BVT = "G:6F"
    BRA = "G:26"
    IOT = "G:9R"
    BRN = "G:80"
    BGR = "G:1W"
    BFA = "G:5A"
    BDI = "G:68"
    KHM = "G:9G"
    CMR = "G:4I"
    CAN = "G:8W"
    CPV = "G:AF"
    CYM = "G:4J"
    CAF = "G:5G"
    TCD = "G:A6"
    CHL = "G:4M"
    CHN = "G:B1"
    CXR = "G:5R"
    CCK = "G:67"
    COL = "G:2S"
    COM = "G:99"
    COD = "G:8A"
    COG = "G:5K"
    COK = "G:1L"
    CRI = "G:5H"
    HRV = "G:5X"
    CUB = "G:7X"
    CYP = "G:8T"
    CZE = "G:2E"
    DNK = "G:19"
    DJI = "G:6Z"
    DMA = "G:8U"
    DOM = "G:76"
    ECU = "G:8Q"
    EGY = "G:3G"
    SLV = "G:AB"
    GNQ = "G:5L"
    ERI = "G:6K"
    EST = "G:9D"
    SWZ = "G:7H"
    ETH = "G:6L"
    FLK = "G:3L"
    FRO = "G:24"
    FJI = "G:3Z"
    FIN = "G:90"
    FRA = "G:5M"
    GUF = "G:3B"
    PYF = "G:54"
    ATF = "G:9V"
    GAB = "G:69"
    GMB = "G:77"
    GEO = "G:9F"
    DEU = "G:3D"
    GHA = "G:5N"
    GIB = "G:79"
    GRC = "G:6A"
    GRL = "G:2R"
    GRD = "G:9A"
    GLP = "G:4Q"
    GUM = "G:2Y"
    GTM = "G:96"
    GGY = "G:34"
    GIN = "G:9L"
    GNB = "G:9Z"
    GUY = "G:44"
    HTI = "G:22"
    HMD = "G:4W"
    HND = "G:AG"
    HKG = "G:3H"
    HUN = "G:46"
    ISL = "G:6I"
    IND = "G:5B"
    IDN = "G:25"
    IRN = "G:56"
    IRQ = "G:8G"
    IRL = "G:6X"
    IMN = "G:35"
    ISR = "G:3S"
    ITA = "G:5J"
    JAM = "G:1G"
    JPN = "G:41"
    JEY = "G:33"
    JOR = "G:1Z"
    KAZ = "G:85"
    KEN = "G:70"
    KIR = "G:7P"
    PRK = "G:AE"
    KOR = "G:83"
    KWT = "G:7Q"
    KGZ = "G:8R"
    LAO = "G:8L"
    LVA = "G:4H"
    LBN = "G:64"
    LSO = "G:2M"
    LBR = "G:3U"
    LBY = "G:6W"
    LIE = "G:A9"
    LTU = "G:8I"
    LUX = "G:7M"
    MAC = "G:3I"
    MKD = "G:AI"
    MDG = "G:7Z"
    MWI = "G:6G"
    MYS = "G:8S"
    MDV = "G:6H"
    MLI = "G:3V"
    MLT = "G:4G"
    MHL = "G:36"
    MTQ = "G:8C"
    MRT = "G:2X"
    MUS = "G:9N"
    MEX = "G:2V"
    FSM = "G:9E"
    MDA = "G:6P"
    MCO = "G:88"
    MNG = "G:66"
    MNE = "G:3E"
    MSR = "G:1X"
    MAR = "G:8X"
    MOZ = "G:2B"
    MMR = "G:72"
    NAM = "G:6Q"
    NRU = "G:8J"
    NPL = "G:2J"
    NLD = "G:7K"
    NCL = "G:2L"
    NZL = "G:49"
    NIC = "G:AC"
    NER = "G:2U"
    NGA = "G:6B"
    NIU = "G:62"
    NFK = "G:7Y"
    NOR = "G:3N"
    OMN = "G:7B"
    PAK = "G:2P"
    PLW = "G:2N"
    PSE = "G:59"
    PAN = "G:4U"
    PNG = "G:2G"
    PRY = "G:89"
    PER = "G:3T"
    PHL = "G:7L"
    PCN = "G:15"
    POL = "G:5Y"
    PRT = "G:A3"
    PRI = "G:5U"
    QAT = "G:51"
    REU = "G:6N"
    ROU = "G:2Z"
    RUS = "G:38"
    RWA = "G:AA"
    SHN = "G:9S"
    KNA = "G:40"
    LCA = "G:3A"
    SPM = "G:4E"
    VCT = "G:3F"
    WSM = "G:2F"
    SMR = "G:78"
    STP = "G:5F"
    SAU = "G:92"
    SEN = "G:6E"
    SRB = "G:7F"
    SYC = "G:5C"
    SLE = "G:A5"
    SGP = "G:7D"
    SVK = "G:1C"
    SVN = "G:74"
    SLB = "G:1Y"
    SOM = "G:5D"
    ZAF = "G:2I"
    SGS = "G:1N"
    SSD = "G:C2"
    ESP = "G:55"
    LKA = "G:1J"
    SDN = "G:C1"
    SUR = "G:86"
    SJM = "G:1M"
    SWE = "G:6V"
    CHE = "G:30"
    SYR = "G:4P"
    TWN = "G:7U"
    TJK = "G:4N"
    TZA = "G:2T"
    THA = "G:3R"
    TGO = "G:91"
    TKL = "G:5P"
    TON = "G:8K"
    TTO = "G:9T"
    TUN = "G:2W"
    TUR = "G:8Z"
    TKM = "G:42"
    TCA = "G:9I"
    TUV = "G:2C"
    UGA = "G:47"
    UKR = "G:71"
    ARE = "G:A4"
    GBR = "G:7J"
    UMI = "G:9W"
    USA = "G:6J"
    URY = "G:4Y"
    UZB = "G:8M"
    VAT = "G:8Y"
    VUT = "G:9M"
    VEN = "G:2K"
    VNM = "G:5Z"
    WLF = "G:4L"
    ESH = "G:4F"
    YEM = "G:28"
    ZMB = "G:73"
    ZWE = "G:52"


OptCountryCode = Optional[Union[str, CountryCode]]

country_code_arg_parser = make_enum_arg_parser_by_members(CountryCode)
