# Copyright 2018 Goldman Sachs.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
#
# Chart Service will attempt to make public functions (not prefixed with _) from this module available. Such functions
# should be fully documented: docstrings should describe parameters and the return value, and provide a 1-line
# description. Type annotations should be provided for parameters.
import math
from enum import IntEnum, Enum
from typing import Union

import numpy as np
import pandas as pd

from gs_quant.api.gs.data import GsDataApi, QueryType
from gs_quant.common import Currency
from gs_quant.markets.securities import Asset
from .analysis import LagMode, lag
from .datetime import align, interpolate
from .helper import CurveType, Interpolate, Window, normalize_window, apply_ramp, plot_session_function, \
    plot_function, Returns, SeriesType
from .statistics import std, product, sum_
from ..data import DataContext
from ..datetime import DayCountConvention, day_count_fraction
from ..errors import MqValueError, MqTypeError

"""
Econometrics timeseries library is for standard economic and time series analytics operations, including returns,
diffs, lags, volatilities and other numerical operations which are generally finance-oriented
"""


class AnnualizationFactor(IntEnum):
    DAILY = 252
    WEEKLY = 52
    SEMI_MONTHLY = 26
    MONTHLY = 12
    QUARTERLY = 4
    ANNUALLY = 1


class SharpeAssets(Enum):
    USD = 'MAP35DA6K5B1YXGX'
    AUD = 'MAFRZWJ790MQY0EW'
    CHF = 'MAS0NN4ZX7NYXB36'
    EUR = 'MA95W0N1214395N8'
    GBP = 'MA41ZEFTWR8Q7HBM'
    JPY = 'MA8GXV3SJ0TXH1JV'
    SEK = 'MAGNZZY0GJ4TATNG'


def excess_returns_pure(price_series: pd.Series, spot_curve: pd.Series) -> pd.Series:
    curve, bench_curve = align(price_series, spot_curve, Interpolate.INTERSECT)

    e_returns = [curve.iloc[0]]
    for i in range(1, len(curve)):
        multiplier = 1 + curve.iloc[i] / curve.iloc[i - 1] - bench_curve.iloc[i] / bench_curve.iloc[i - 1]
        e_returns.append(e_returns[-1] * multiplier)
    return pd.Series(e_returns, index=curve.index)


def excess_returns(price_series: pd.Series, benchmark_or_rate: Union[Asset, Currency, float], *,
                   day_count_convention=DayCountConvention.ACTUAL_360) -> pd.Series:
    if isinstance(benchmark_or_rate, float):
        er = [price_series.iloc[0]]
        for j in range(1, len(price_series)):
            fraction = day_count_fraction(price_series.index[j - 1], price_series.index[j], day_count_convention)
            er.append(er[-1] + price_series.iloc[j] - price_series.iloc[j - 1] * (1 + benchmark_or_rate * fraction))
        return pd.Series(er, index=price_series.index)

    if isinstance(benchmark_or_rate, Currency):
        try:
            marquee_id = SharpeAssets[benchmark_or_rate.value].value
        except KeyError:
            raise MqValueError(f"unsupported currency {benchmark_or_rate}")
    else:
        marquee_id = benchmark_or_rate.get_marquee_id()

    with DataContext(price_series.index[0], price_series.index[-1]):
        q = GsDataApi.build_market_data_query([marquee_id], QueryType.SPOT)
        df = GsDataApi.get_market_data(q)
    if df.empty:
        raise MqValueError(f'could not retrieve risk-free rate {marquee_id}')
    df = df[~df.index.duplicated(keep='first')]  # handle bad data (duplicate rows)

    return excess_returns_pure(price_series, df['spot'])


def _annualized_return(levels: pd.Series, rolling: Union[int, pd.DateOffset],
                       interpolation_method: Interpolate = Interpolate.NAN) -> pd.Series:
    if isinstance(rolling, pd.DateOffset):
        starting = [tstamp - rolling for tstamp in levels.index]
        levels = interpolate(levels, method=interpolation_method)
        points = list(
            map(lambda d, v, i: pow(v / levels.get(i, np.nan),
                                    365.25 / (d - i).days) - 1,
                levels.index[1:],
                levels.values[1:], starting[1:]))
    else:
        if interpolation_method is not Interpolate.NAN:
            raise MqValueError(f'If w is not a relative date, method must be nan. You specified method: '
                               f'{interpolation_method.value}.')
        starting = [0] * rolling
        starting.extend([a for a in range(1, len(levels) - rolling + 1)])
        points = list(
            map(lambda d, v, i: pow(v / levels.iloc[i], 365.25 / (d - levels.index[i]).days) - 1, levels.index[1:],
                levels.values[1:], starting[1:]))
    points.insert(0, 0)
    return pd.Series(points, index=levels.index)


def get_ratio_pure(er: pd.Series, w: Union[Window, int, str],
                   interpolation_method: Interpolate = Interpolate.NAN) -> pd.Series:
    w = normalize_window(er, w or None)  # continue to support 0 as an input for window
    ann_return = _annualized_return(er, w.w, interpolation_method=interpolation_method)
    long_enough = (er.index[-1] - w.w) >= er.index[0] if isinstance(w.w, pd.DateOffset) else w.w < len(er)
    ann_vol = volatility(er, w).iloc[1:] if long_enough else volatility(er)
    result = ann_return / ann_vol * 100
    return apply_ramp(result, w)


def _get_ratio(input_series: pd.Series, benchmark_or_rate: Union[Asset, float, str], w: Union[Window, int, str], *,
               day_count_convention: DayCountConvention, curve_type: CurveType = CurveType.PRICES,
               interpolation_method: Interpolate = Interpolate.NAN) -> pd.Series:
    if curve_type == CurveType.PRICES:
        er = excess_returns(input_series, benchmark_or_rate, day_count_convention=day_count_convention)
    else:
        assert curve_type == CurveType.EXCESS_RETURNS
        er = input_series

    return get_ratio_pure(er, w, interpolation_method)


class RiskFreeRateCurrency(Enum):
    USD = "USD"
    AUD = "AUD"
    CHF = "CHF"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"
    SEK = "SEK"
    _USD = "usd"
    _AUD = "aud"
    _CHF = "chf"
    _EUR = "eur"
    _GBP = "gbp"
    _JPY = "jpy"
    _SEK = "sek"


@plot_session_function
def excess_returns_(price_series: pd.Series, currency: RiskFreeRateCurrency = RiskFreeRateCurrency.USD) -> pd.Series:
    """
    Calculate excess returns

    :param price_series: price series
    :param currency: currency for risk-free rate, defaults to USD
    :return: excess returns

    **Usage**

    Given a price series P and risk-free rate R, excess returns E are defined as:

    :math:`E_t = E_{t-1} + P_t - P_{t-1} * (1 + R * (D_t - D_{t-1}) / 360)`

    The `Actual/360 <https://en.wikipedia.org/wiki/Day_count_convention#Actual/360>`_ day count convention is used.

    **Examples**

    Get excess returns from a price series.

    >>> er = excess_returns(generate_series(100), USD)
    """
    return excess_returns(price_series, Currency(currency.value), day_count_convention=DayCountConvention.ACTUAL_360)


@plot_session_function
def sharpe_ratio(series: pd.Series, currency: RiskFreeRateCurrency = RiskFreeRateCurrency.USD,
                 w: Union[Window, int, str] = None, curve_type: CurveType = CurveType.PRICES,
                 method: Interpolate = Interpolate.NAN) -> pd.Series:
    """
    Calculate Sharpe ratio

    :param series: series of prices or excess returns for an asset
    :param currency: currency for risk-free rate, defaults to USD
    :param w: Window or int: size of window and ramp up to use. e.g. Window(22, 10) where 22 is the window size
              and 10 the ramp up value.  If w is a string, it should be a relative date like '1m', '1d', etc.
              Window size defaults to length of series.
    :param curve_type: whether input series is of prices or excess returns, defaults to prices
    :param method: interpolation method (default: nan). Used to calculate returns on dates without data (i.e. weekends)
              when window is a relative date. Defaults to no interpolation.
    :return: Sharpe ratio

    **Usage**

    Given a price series P, risk-free rate R, and window of size w returns the rolling
    `Sharpe ratio <https://en.wikipedia.org/wiki/Sharpe_ratio>`_ S:

    :math:`S_t = \\frac{(E_t / E_{t-w+1})^{365.25 / (D_t - D_{t-w})}-1}{volatility(E, w)_t}`

    Excess returns E are defined as:

    :math:`E_t = E_{t-1} + P_t - P_{t-1} * (1 + R * (D_t - D_{t-1}) / 360)`

    where D is the date for a data point. The
    `Actual/360 <https://en.wikipedia.org/wiki/Day_count_convention#Actual/360>`_ day count convention is used.

    **Examples**

    Get rolling sharpe ratio of a price series (with window of 22).

    >>> sr = sharpe_ratio(generate_series(365, END_TODAY), USD, 22, PRICES)

    **See also**

    :func:`volatility`
    """
    return _get_ratio(series, Currency(currency.value), w, day_count_convention=DayCountConvention.ACTUAL_360,
                      curve_type=curve_type, interpolation_method=method)


@plot_function
def returns(series: pd.Series, obs: Union[Window, int, str] = 1, type: Returns = Returns.SIMPLE) -> pd.Series:
    """
    Calculate returns from price series

    :param series: time series of prices
    :param obs: number of observations or relative date e.g. 3d, 1w, 1m
    :param type: returns type: simple, logarithmic or absolute
    :return: date-based time series of return

    **Usage**

    Compute returns series from price levels, based on the value of *type*:

    ===========   =============================
    Type          Description
    ===========   =============================
    simple        Simple arithmetic returns
    logarithmic   Logarithmic returns
    absolute      Absolute returns
    ===========   =============================

    *Simple*

    Simple geometric change in asset prices, which can be aggregated across assets

    :math:`Y_t = \\frac{X_t}{X_{t-obs}} - 1`

    where :math:`X_t` is the asset price at time :math:`t`

    *Logarithmic*

    Natural logarithm of asset price changes, which can be aggregated through time

    :math:`Y_t = log(X_t) - log(X_{t-obs})`

    where :math:`X_t` is the asset price at time :math:`t`

    *Absolute*

    Absolute change in asset prices

    :math:`Y_t = X_t - X_{t-obs}`

    where :math:`X_t` is the asset price at time :math:`t`

    **Examples**

    Generate price series and take compute returns

    >>> prices = generate_series(100)
    >>> returns = returns(prices)

    **See also**

    :func:`prices`
    """

    if series.size < 1:
        return series

    shifted_series = lag(series, obs, LagMode.TRUNCATE)

    if type == Returns.SIMPLE:
        ret_series = series / shifted_series - 1
    elif type == Returns.LOGARITHMIC:
        ret_series = series.apply(math.log) - shifted_series.apply(math.log)
    elif type == Returns.ABSOLUTE:
        ret_series = series - shifted_series
    else:
        raise MqValueError('Unknown returns type (use simple / logarithmic / absolute)')

    return ret_series


@plot_function
def prices(series: pd.Series, initial: int = 1, type: Returns = Returns.SIMPLE) -> pd.Series:
    """
    Calculate price levels from returns series

    :param series: time series of returns
    :param initial: initial price level
    :param type: returns type: simple, logarithmic or absolute
    :return: date-based time series of return

    **Usage**

    Compute price levels from returns series, based on the value of *type*:

    ===========   =============================
    Type          Description
    ===========   =============================
    simple        Simple arithmetic returns
    logarithmic   Logarithmic returns
    absolute      Absolute returns
    ===========   =============================

    *Simple*

    Compute asset price series from simple returns:

    :math:`Y_t = (1 + X_{t-1}) Y_{t-1}`

    where :math:`X_t` is the asset price at time :math:`t` and :math:`Y_0 = initial`

    *Logarithmic*

    Compute asset price series from logarithmic returns:

    :math:`Y_t = e^{X_{t-1}} Y_{t-1}`

    where :math:`X_t` is the asset price at time :math:`t` and :math:`Y_0 = initial`

    *Absolute*

    Compute asset price series from absolute returns:

    :math:`Y_t = X_{t-1} + Y_{t-1}`

    where :math:`X_t` is the asset price at time :math:`t` and :math:`Y_0 = initial`

    **Examples**

    Generate price series and take compute returns

    >>> series = generate_series(100)
    >>> returns = prices(returns(series))

    **See also**

    :func:`returns` :func:`product` :func:`exp`
    """

    if series.size < 1:
        return series

    if type == Returns.SIMPLE:
        return product(1 + series) * initial
    elif type == Returns.LOGARITHMIC:
        return product(series.apply(math.exp)) * initial
    elif type == Returns.ABSOLUTE:
        return sum_(series) + initial
    else:
        raise MqValueError('Unknown returns type (use simple / Logarithmic / absolute)')


@plot_function
def index(x: pd.Series, initial: int = 1) -> pd.Series:
    """
    Geometric series normalization

    :param x: time series
    :param initial: initial value
    :return: normalized time series

    **Usage**

    Divides every value in x by the initial value of x:

    :math:`Y_t = initial * X_t / X_0`

    where :math:`X_0` is the first value in the series

    **Examples**

    Normalize series to 1:

    >>> series = generate_series(100)
    >>> returns = index(series)

    **See also**

    :func:`returns`

    """
    i = x.first_valid_index()
    if not x[i]:
        raise MqValueError('Divide by zero error. Ensure that the first value of series passed to index(...) '
                           'is non-zero')
    return pd.Series(dtype=float) if i is None else initial * x / x[i]


@plot_function
def change(x: pd.Series) -> pd.Series:
    """
    Arithmetic series normalization

    :param x: time series
    :return: normalized time series

    **Usage**

    Compute difference of every value from the initial value of x:

    :math:`Y_t = X_t - X_0`

    where :math:`X_0` is the first value in the series

    **Examples**

    Change in level from initial value:

    >>> series = generate_series(100)
    >>> returns = change(series)

    **See also**

    :func:`index`

    """
    return x - x[0]


def _get_annualization_factor(x):
    prev_idx = x.index[0]
    distances = []

    for idx, value in x.iloc[1:].items():
        d = (idx - prev_idx).days
        if d == 0:
            raise MqValueError('multiple data points on same date')
        distances.append(d)
        prev_idx = idx

    average_distance = np.average(distances)
    if average_distance < 2.1:
        factor = AnnualizationFactor.DAILY
    elif 6 <= average_distance < 8:
        factor = AnnualizationFactor.WEEKLY
    elif 14 <= average_distance < 17:
        factor = AnnualizationFactor.SEMI_MONTHLY
    elif 25 <= average_distance < 35:
        factor = AnnualizationFactor.MONTHLY
    elif 85 <= average_distance < 97:
        factor = AnnualizationFactor.QUARTERLY
    elif 360 <= average_distance < 386:
        factor = AnnualizationFactor.ANNUALLY
    else:
        raise MqValueError('Cannot infer annualization factor, average distance: ' + str(average_distance))
    return factor


@plot_function
def annualize(x: pd.Series) -> pd.Series:
    """
    Annualize series based on sample observation frequency

    :param x: time series of prices
    :return: date-based time series of annualized values

    **Usage**

    Based on number of days between observations, will determine an annualization factor and then adjust values
    accordingly. Useful for annualizing daily or monthly returns

    :math:`Y_t = X_t * \\sqrt{F}`

    Annualization factors as follows, based on period implied by observations:

    =========   =============================
    Period      Annualization Factor (F)
    =========   =============================
    Daily       :math:`252`
    Weekly      :math:`52`
    Bi-Weekly   :math:`26`
    Monthly     :math:`12`
    Quarterly   :math:`4`
    Annually    :math:`1`
    =========   =============================

    **Examples**

    Annualize daily returns series:

    >>> prices = generate_series(100)
    >>> ann = annualize(returns(prices))

    **See also**

    :func:`returns`
    """

    factor: int = _get_annualization_factor(x)
    return x * math.sqrt(factor)


@plot_function
def volatility(x: pd.Series, w: Union[Window, int, str] = Window(None, 0),
               returns_type: Returns = Returns.SIMPLE) -> pd.Series:
    """
    Realized volatility of price series

    :param x: time series of prices
    :param w: Window or int: size of window and ramp up to use. e.g. Window(22, 10) where 22 is the window size
              and 10 the ramp up value.  If w is a string, it should be a relative date like '1m', '1d', etc.
              Window size defaults to length of series.
    :param returns_type: returns type: simple, logarithmic or absolute
    :return: date-based time series of return

    **Usage**

    Calculate rolling annualized realized volatility of a price series over a given window. Annual volatility of 20% is
    returned as 20.0:

    :math:`Y_t = \\sqrt{\\frac{1}{N-1} \\sum_{i=t-w+1}^t (R_t - \\overline{R_t})^2} * \\sqrt{252} * 100`

    where N is the number of observations in each rolling window :math:`w`, :math:`R_t` is the return on time
    :math:`t` based on *returns_type*

    ===========   =======================================================
    Type          Description
    ===========   =======================================================
    simple        Simple geometric change in asset prices:
                  :math:`R_t = \\frac{X_t}{X_{t-1}} - 1`
                  where :math:`X_t` is the asset price at time :math:`t`
    logarithmic   Natural logarithm of asset price changes:
                  :math:`R_t = log(X_t) - log(X_{t-1})`
                  where :math:`X_t` is the asset price at time :math:`t`
    absolute      Absolute change in asset prices:
                  :math:`Y_t = X_t - X_{t-obs}`
                  where :math:`X_t` is the asset price at time :math:`t`
    ===========   =======================================================

    and :math:`\\overline{R_t}` is the mean value over the same window:

    :math:`\\overline{R_t} = \\frac{\\sum_{i=t-w+1}^{t} R_t}{N}`

    If window is not provided, computes realized volatility over the full series

    **Examples**

    Compute rolling :math:`1` month (:math:`22` business day) annualized volatility of price series

    >>> series = generate_series(100)
    >>> vol_series = volatility(series, 22)
    >>> vol_series = volatility(series, Window(22, 30))

    **See also**

    :func:`std` :func:`annualize` :func:`returns`

    """
    w = normalize_window(x, w)

    if x.size < 1:
        return x

    return apply_ramp(annualize(std(returns(x, type=returns_type), Window(w.w, 0))).mul(100), w)


@plot_function
def correlation(x: pd.Series, y: pd.Series,
                w: Union[Window, int, str] = Window(None, 0), type_: SeriesType = SeriesType.PRICES,
                returns_type: Returns = Returns.SIMPLE) -> pd.Series:
    """
    Rolling correlation of two price series

    :param x: price series
    :param y: price series
    :param w: Window, int, or str: size of window and ramp up to use. e.g. Window(22, 10) where 22 is the window size
              and 10 the ramp up value. If w is a string, it should be a relative date like '1m', '1d', etc.
              Window size defaults to length of series.
    :param type_: type of both input series: prices or returns
    :param returns_type: Method to calculate returns when type_ is PRICES, simple, logarithmic or absolute. You can
                        also pass two methods to calculate returns for x and y respectively.
    :return: date-based time series of correlation

    **Usage**

    Calculate rolling `realized correlation <https://en.wikipedia.org/wiki/Correlation_and_dependence>`_,
    :math:`\\rho_t` of two price series over a given window:

    :math:`\\rho_t =
    \\frac{\\sum_{i=t-w+1}^t (R_t - \\overline{R_t})(Y_t - \\overline{S_t})}{(N-1)\\sigma R_t\\sigma S_t}`

    where N is the number of observations in each rolling window, :math:`w`, and :math:`R_t` and :math:`S_t` are the
    simple returns for each series on time :math:`t`

    If prices are provided then returns are calculated based on the returns_type e.g. for simple returns:

    :math:`R_t = \\frac{X_t}{X_{t-1}} - 1` and :math:`S_t = \\frac{Y_t}{Y_{t-1}} - 1`

    If returns are provided:

    :math:`R_t = X_t` and :math:`S_t = Y_t`

    :math:`\\overline{R_t}`, :math:`\\overline{S_t}` are the mean values, and :math:`\\sigma R_{t}` and
    :math:`\\sigma S_{t}` are the sample standard deviations, of  series
    :math:`R_t` and :math:`S_t` over the same window

    If window is not provided, computes realized correlation over the full series

    **Examples**

    Compute rolling :math:`1` month (:math:`22` business day) correlation of price series

    >>> series1 = generate_series(100)
    >>> series2 = generate_series(100)
    >>> corr = correlation(series1, series2, 22)

    **See also**

    :func:`std` :func:`returns`

    """
    w = normalize_window(x, w)

    if x.size < 1:
        return x

    given_prices = type_ == SeriesType.PRICES
    if given_prices:
        if isinstance(returns_type, (tuple, list)):
            if len(returns_type) != 2:
                raise MqValueError('Expected a list of length 2 for "returns_type"')
            if not all(isinstance(r, Returns) for r in returns_type):
                raise MqTypeError('Expected a list of Returns for "returns_type"')
            returns_type_x, returns_type_y = returns_type
        else:
            returns_type_x = returns_type_y = returns_type
        ret_1 = returns(x, type=returns_type_x)
        ret_2 = returns(y, type=returns_type_y)
    else:
        ret_1 = x
        ret_2 = y

    clean_ret1 = ret_1.dropna()
    clean_ret2 = ret_2.dropna()

    if isinstance(w.w, pd.DateOffset):
        if isinstance(clean_ret1.index, pd.DatetimeIndex):
            values = [clean_ret1.loc[(clean_ret1.index > idx - w.w) & (clean_ret1.index <= idx)].corr(clean_ret2)
                      for idx in clean_ret1.index]
        else:
            values = [clean_ret1.loc[(clean_ret1.index > (idx - w.w).date()) &
                                     (clean_ret1.index <= idx)].corr(clean_ret2)
                      for idx in clean_ret1.index]
        corr = pd.Series(values, index=clean_ret1.index)
    else:
        corr = clean_ret1.rolling(w.w, 0).corr(clean_ret2)

    return apply_ramp(interpolate(corr, x, Interpolate.NAN), w)


@plot_function
def beta(x: pd.Series, b: pd.Series, w: Union[Window, int, str] = Window(None, 0), prices: bool = True) -> pd.Series:
    """
    Rolling beta of price series and benchmark

    :param x: time series of prices
    :param b: time series of benchmark prices
    :param w: Window, int, or str: size of window and ramp up to use. e.g. Window(22, 10) where 22 is the window size
              and 10 the ramp up value.  If w is a string, it should be a relative date like '1m', '1d', etc.
              Window size defaults to length of series.
    :param prices: True if input series are prices, False if they are returns
    :return: date-based time series of beta

    **Usage**

    Calculate rolling `beta <https://en.wikipedia.org/wiki/Beta_(finance)>`_,
    :math:`\\beta_t` of a series to a benchmark over a given window:

    :math:`R_t = \\alpha_t + \\beta S_t + \\epsilon_t`

    Calculated as:

    :math:`\\beta_t = \\frac{\\sum_{i=t-w+1}^t Cov(R_t, S_t)}{Var(S_t)}`

    where N is the number of observations in each rolling window, :math:`w`, and :math:`R_t` and :math:`S_t` are the
    simple returns for each series on time :math:`t`:

    :math:`R_t = \\frac{X_t}{X_{t-1}} - 1` and :math:`S_t = \\frac{b_t}{b_{t-1}} - 1`

    If prices = False, assumes returns are provided:

    :math:`R_t = X_t` and :math:`S_t = b_t`

    :math:`Cov(R_t, S_t)` and :math:`Var(S_t)` are the covariance and variance of the series
    :math:`R_t` and :math:`S_t` over the same window

    If window is not provided, computes beta over the full series

    **Examples**

    Compute rolling :math:`1` month (:math:`22` business day) beta of two price series

    >>> series = generate_series(100)
    >>> benchmark = generate_series(100)
    >>> b = beta(series, benchmark, 22)

    **See also**

    :func:`var` :func:`cov` :func:`correlation` :func:`returns`
    """
    if not isinstance(prices, bool):
        raise MqTypeError('expected a boolean value for "prices"')

    w = normalize_window(x, w)

    ret_series = returns(x) if prices else x
    ret_benchmark = returns(b) if prices else b

    if isinstance(w.w, pd.DateOffset):
        series_index = ret_series.index.intersection(ret_benchmark.index)
        size = len(series_index)
        ret_series = ret_series.loc[series_index]
        benchmark_series = ret_benchmark.loc[series_index]

        ret_values = np.array(ret_series.values, dtype=np.double)
        benchmark_values = np.array(benchmark_series.values, dtype=np.double)

        cov_results = np.empty(size, dtype=np.double)
        var_results = np.empty(size, dtype=np.double)

        offset = w.w
        start = 0
        for i in range(1, size):
            min_index_value = (series_index[i] - offset).date()
            for idx in range(start, i + 1):
                if series_index[idx] > min_index_value:
                    start = idx
                    break

            sub_benchmark_values = benchmark_values[start:i + 1]
            var_results[i] = np.var(sub_benchmark_values, ddof=1)
            cov_results[i] = np.cov(ret_values[start:i + 1], sub_benchmark_values, ddof=1)[0][1]

        result = pd.Series(cov_results / var_results, index=series_index, dtype=np.double)
    else:
        cov = ret_series.rolling(w.w, 0).cov(ret_benchmark)
        result = cov / ret_benchmark.rolling(w.w, 0).var()

    # do not compute initial values as they may be extreme when sample size is small
    result[0:3] = np.nan
    return apply_ramp(interpolate(result, x, Interpolate.NAN), w)


@plot_function
def max_drawdown(x: pd.Series, w: Union[Window, int, str] = Window(None, 0)) -> pd.Series:
    """
    Compute the maximum peak to trough drawdown over a rolling window as a ratio.

    i.e. if the max drawdown for a period is 20%, this function will return -0.2.

    :param x: time series
    :param w: Window, int, or str: size of window and ramp up to use. e.g. Window(22, 10) where 22 is the window size
              and 10 the ramp up value.  If w is a string, it should be a relative date like '1m', '1d', etc.
              Window size defaults to length of series.
    :return: time series of rolling maximum drawdown

    **Examples**

    Compute the maximum peak to trough `drawdown <https://en.wikipedia.org/wiki/Drawdown_(economics)>`_

    >>> series = generate_series(100)
    >>> max_drawdown(series)

    **See also**

    :func:`returns`

    """
    w = normalize_window(x, w)
    if isinstance(w.w, pd.DateOffset):
        if pd.api.types.is_datetime64_dtype(x.index):
            scores = pd.Series([x[idx] / x.loc[(x.index > (idx - w.w)) & (x.index <= idx)].max() - 1
                                for idx in x.index], index=x.index)
            result = pd.Series([scores.loc[(scores.index > (idx - w.w)) & (scores.index <= idx)].min()
                                for idx in scores.index], index=scores.index)
        else:
            raise TypeError('Please pass in list of dates as index')
    else:
        rolling_max = x.rolling(w.w, 0).max()
        result = (x / rolling_max - 1).rolling(w.w, 0).min()
    return apply_ramp(result, w)
