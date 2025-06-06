from typing import overload
from enum import Enum
import datetime
import typing

import QuantConnect.Data
import QuantConnect.Data.Custom.Intrinio
import QuantConnect.Util
import System


class IntrinioConfig(System.Object):
    """Auxiliary class to access all Intrinio API data."""

    rate_gate: QuantConnect.Util.RateGate = ...
    """"""

    IS_INITIALIZED: bool
    """Check if Intrinio API user and password are not empty or null."""

    password: str = ...
    """Intrinio API password"""

    user: str = ...
    """Intrinio API user"""

    @staticmethod
    def set_time_interval_between_calls(time_span: datetime.timedelta) -> None:
        """
        Sets the time interval between calls.
        For more information, please refer to: https://intrinio.com/documentation/api#limits
        
        :param time_span: Time interval between to consecutive calls.
        """
        ...

    @staticmethod
    def set_user_and_password(user: str, password: str) -> None:
        """Set the Intrinio API user and password."""
        ...


class IntrinioEconomicDataSources(System.Object):
    """Intrinio Data Source"""

    class BofAMerrillLynch(System.Object):
        """Bank of America Merrill Lynch"""

        US_CORPORATE_BBB_EFFECTIVE_YIELD: str = "$BAMLC0A4CBBBEY"
        """
        This data represents the effective yield of the BofA Merrill Lynch US Corporate BBB Index, a subset of the BofA
            Merrill Lynch US Corporate Master Index tracking the performance of US dollar denominated investment grade rated
            corporate debt publically issued in the US domestic market.
        """

        US_CORPORATE_BBB_OPTION_ADJUSTED_SPREAD: str = "$BAMLC0A4CBBB"
        """
        This data represents the Option-Adjusted Spread (OAS) of the BofA Merrill Lynch US Corporate BBB Index, a subset of
            the BofA Merrill Lynch US Corporate Master Index tracking the performance of US dollar denominated investment grade
            rated corporate debt publically issued in the US domestic market.
        """

        US_CORPORATE_MASTER_OPTION_ADJUSTED_SPREAD: str = "$BAMLC0A0CM"
        """
        The BofA Merrill Lynch Option-Adjusted Spreads (OASs) are the calculated spreads between a computed OAS index of
            all bonds in a given rating category and a spot Treasury curve. An OAS index is constructed using each constituent
            bond’s OAS, weighted by market capitalization.
        """

        US_HIGH_YIELD_BB_OPTION_ADJUSTED_SPREAD: str = "$BAMLH0A1HYBB"
        """
        This data represents the Option-Adjusted Spread (OAS) of the BofA Merrill Lynch US Corporate BB Index, a subset of
            the BofA Merrill Lynch US High Yield Master II Index tracking the performance of US dollar denominated below
            investment grade rated corporate debt publically issued in the US domestic market.
        """

        US_HIGH_YIELD_B_OPTION_ADJUSTED_SPREAD: str = "$BAMLH0A2HYB"
        """
        This data represents the Option-Adjusted Spread (OAS) of the BofA Merrill Lynch US Corporate B Index, a subset of
            the BofA Merrill Lynch US High Yield Master II Index tracking the performance of US dollar denominated below
            investment grade rated corporate debt publically issued in the US domestic market. This subset includes all
            securities with a given investment grade rating B.
        """

        US_HIGH_YIELD_CC_COR_BELOW_OPTION_ADJUSTED_SPREAD: str = "$BAMLH0A3HYC"
        """
        This data represents the Option-Adjusted Spread (OAS) of the BofA Merrill Lynch US Corporate C Index, a subset of
            the BofA Merrill Lynch US High Yield Master II Index tracking the performance of US dollar denominated below
            investment grade rated corporate debt publically issued in the US domestic market.
        """

        US_HIGH_YIELD_EFFECTIVE_YIELD: str = "$BAMLH0A0HYM2EY"
        """
        This data represents the effective yield of the BofA Merrill Lynch US High Yield Master II Index, which tracks the
            performance of US dollar denominated below investment grade rated corporate debt publically issued in the US
            domestic market.
            Source: https://fred.stlouisfed.org/series/BAMLH0A0HYM2EY
        """

        US_HIGH_YIELD_MASTER_II_TOTAL_RETURN_INDEX_VALUE: str = "$BAMLHYH0A0HYM2TRIV"
        """
        This data represents the BofA Merrill Lynch US High Yield Master II Index value, which tracks the performance of US
            dollar denominated below investment grade rated corporate debt publically issued in the US domestic market.
        """

        US_HIGH_YIELD_OPTION_ADJUSTED_SPREAD: str = "$BAMLH0A0HYM2"
        """
        The BofA Merrill Lynch Option-Adjusted Spreads (OASs) are the calculated spreads between a computed OAS index of
            all bonds in a given rating category and a spot Treasury curve. An OAS index is constructed using each constituent
            bond’s OAS, weighted by market capitalization.
            Source: https://fred.stlouisfed.org/series/BAMLH0A0HYM2
        """

    class CBOE(System.Object):
        """Chicago Board Options Exchange"""

        CHINA_ETF_VOLATILITY_INDEX: str = "$VXFXICLS"
        """CBOE China ETF Volatility Index"""

        CRUDE_OIL_ETF_VOLATILITY_INDEX: str = "$OVXCLS"
        """CBOE Crude Oil ETF Volatility Index"""

        EMERGING_MARKETS_ETF_VOLATILITY_INDEX: str = "$VXEEMCLS"
        """CBOE Emerging Markets ETF Volatility Index"""

        GOLD_ETF_VOLATILITY_INDEX: str = "$GVZCLS"
        """CBOE Gold ETF Volatility Index"""

        TEN_YEAR_TREASURY_NOTE_VOLATILITY_FUTURES: str = "$VXTYN"
        """CBOE 10-Year Treasury Note Volatility Futures"""

        VIX: str = "$VIXCLS"
        """CBOE Volatility Index: VIX"""

        VXO: str = "$VXOCLS"
        """CBOE S&P 100 Volatility Index: VXO"""

        VXV: str = "$VXVCLS"
        """CBOE S&P 500 3-Month Volatility Index"""

    class Commodities(System.Object):
        """Commodities"""

        CRUDE_OIL_BRENT: str = "$DCOILBRENTEU"
        """Crude Oil Prices: Brent - Europe"""

        CRUDE_OIL_WTI: str = "$DCOILWTICO"
        """Crude Oil Prices: West Texas Intermediate (WTI) - Cushing, Oklahoma"""

        GASOLINE_US_GULF_COAST: str = "$DGASUSGULF"
        """Conventional Gasoline Prices: U.S. Gulf Coast, Regular"""

        GOLD_FIXING_PRICE_1030_AM_LONDON: str = "$GOLDAMGBD228NLBM"
        """Gold Fixing Price 10:30 A.M. (London time) in London Bullion Market, based in U.S. Dollars"""

        GOLD_FIXING_PRICE_1500_AM_LONDON: str = "$GOLDPMGBD228NLBM"
        """Gold Fixing Price 3:00 P.M. (London time) in London Bullion Market, based in U.S. Dollars"""

        NATURAL_GAS: str = "$DHHNGSP"
        """Henry Hub Natural Gas Spot Price"""

        PROPANE: str = "$DPROPANEMBTX"
        """Propane Prices: Mont Belvieu, Texas"""

    class ExchangeRates(System.Object):
        """Exchange Rates"""

        BRAZIL_USA: str = "$DEXBZUS"
        """Brazilian Reals to One U.S. Dollar"""

        CANADA_USA: str = "$DEXCAUS"
        """Canadian Dollars to One U.S. Dollar"""

        CHINA_USA: str = "$DEXCHUS"
        """Chinese Yuan to One U.S. Dollar"""

        HONG_KONG_USA: str = "$DEXHKUS"
        """Hong Kong Dollars to One U.S. Dollar"""

        INDIA_USA: str = "$DEXINUS"
        """Indian Rupees to One U.S. Dollar"""

        JAPAN_USA: str = "$DEXJPUS"
        """Japanese Yen to One U.S. Dollar"""

        MALAYSIA_USA: str = "$DEXMAUS"
        """Malaysian Ringgit to One U.S. Dollar"""

        MEXICO_USA: str = "$DEXMXUS"
        """Mexican New Pesos to One U.S. Dollar"""

        NORWAY_USA: str = "$DEXNOUS"
        """Norwegian Kroner to One U.S. Dollar"""

        SINGAPORE_USA: str = "$DEXSIUS"
        """Singapore Dollars to One U.S. Dollar"""

        SOUTH_AFRICA_USA: str = "$DEXSFUS"
        """South African Rand to One U.S. Dollar"""

        SOUTH_KOREA_USA: str = "$DEXKOUS"
        """South Korean Won to One U.S. Dollar"""

        SRI_LANKA_USA: str = "$DEXSLUS"
        """Sri Lankan Rupees to One U.S. Dollar"""

        SWITZERLAND_USA: str = "$DEXSZUS"
        """Swiss Francs to One U.S. Dollar"""

        TAIWAN_USA: str = "$DEXTAUS"
        """New Taiwan Dollars to One U.S. Dollar"""

        THAILAND_USA: str = "$DEXTHUS"
        """Thai Baht to One U.S. Dollar"""

        USA_AUSTRALIA: str = "$DEXUSAL"
        """U.S. Dollars to One Australian Dollar"""

        USA_EURO: str = "$DEXUSEU"
        """U.S. Dollars to One Euro"""

        USA_NEW_ZEALAND: str = "$DEXUSNZ"
        """U.S. Dollars to One New Zealand Dollar"""

        USA_UK: str = "$DEXUSUK"
        """U.S. Dollars to One British Pound"""

    class Moodys(System.Object):
        """Moody's Investors Service"""

        SEASONED_AAA_CORPORATE_BOND_YIELD: str = "$DAAA"
        """
        Moody's Seasoned Aaa Corporate Bond© and 10-Year Treasury Constant Maturity.
            These instruments are based on bonds with maturities 20 years and above.
        """

        SEASONED_AAA_CORPORATE_BOND_YIELD_RELATIVE_TO_10_YEAR_TREASURY_CONSTANT_MATURITY: str = "$AAA10Y"
        """
        Series is calculated as the spread between Moody's Seasoned Aaa Corporate Bond© and 10-Year Treasury Constant
            Maturity
        """

        SEASONED_BAA_CORPORATE_BOND_YIELD: str = "$DBAA"
        """
        Moody's Seasoned Baa Corporate Bond© and 10-Year Treasury Constant Maturity.
            These instruments are based on bonds with maturities 20 years and above.
        """

        SEASONED_BAA_CORPORATE_BOND_YIELD_RELATIVE_TO_10_YEAR_TREASURY_CONSTANT_MATURITY: str = "$BAA10Y"
        """Series is calculated as the spread between Moody's Seasoned Baa Corporate Bond© and 10-Year Treasury Constant Maturity"""

    class TradeWeightedUsDollarIndex(System.Object):
        """Trade Weighted US Dollar Index"""

        BROAD: str = "$DTWEXB"
        """
        A weighted average of the foreign exchange value of the U.S. dollar against the currencies of a broad group of
            major U.S. trading partners. Broad currency index includes the Euro Area, Canada, Japan, Mexico, China, United
            Kingdom, Taiwan, Korea, Singapore, Hong Kong, Malaysia, Brazil, Switzerland, Thailand, Philippines, Australia,
            Indonesia, India, Israel, Saudi Arabia, Russia, Sweden, Argentina, Venezuela, Chile and Colombia.
        """

        MAJOR_CURRENCIES: str = "$DTWEXM"
        """
        A weighted average of the foreign exchange value of the U.S. dollar against a subset of the broad index currencies
            that circulate widely outside the country of issue. Major currencies index includes the Euro Area, Canada, Japan,
            United Kingdom, Switzerland, Australia, and Sweden.
        """

        OTHER_IMPORTANT_TRADING_PARTNERS: str = "$DTWEXO"
        """
        A weighted average of the foreign exchange value of the U.S. dollar against a subset of the broad index currencies
            that do not circulate widely outside the country of issue. Countries whose currencies are included in the other
            important trading partners index are Mexico, China, Taiwan, Korea, Singapore, Hong Kong, Malaysia, Brazil,
            Thailand, Philippines, Indonesia, India, Israel, Saudi Arabia, Russia, Argentina, Venezuela, Chile and Colombia.
        """


class IntrinioDataTransformation(Enum):
    """TRanformation available for the Economic data."""

    ROC = 0
    """The rate of change"""

    ANNUALY_ROC = 1
    """Rate of change from Year Ago"""

    COMPOUNDED_ANNUAL_ROC = 2
    """The compounded annual rate of change"""

    ANNUALY_CC_ROC = 3
    """The continuously compounded annual rate of change"""

    CC_ROC = 4
    """The continuously compounded rateof change"""

    LEVEL = 5
    """The level, no transformation."""

    LN = 6
    """The natural log"""

    PC = 7
    """The percent change"""

    ANNUALY_PC = 8
    """The percent change from year ago"""


class IntrinioEconomicData(QuantConnect.Data.BaseData):
    """Access the massive repository of economic data from the Federal Reserve Economic Data system via the Intrinio API."""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the IntrinioEconomicData class."""
        ...

    @overload
    def __init__(self, data_transformation: QuantConnect.Data.Custom.Intrinio.IntrinioDataTransformation) -> None:
        """
        Initializes a new instance of the IntrinioEconomicData class.
        
        :param data_transformation: The item.
        """
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method,
            and returns a new instance of the object
            each time it is called. The returned object is assumed to be time stamped in the config.ExchangeTimeZone.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...


