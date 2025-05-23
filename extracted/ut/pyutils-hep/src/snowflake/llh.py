import os
try:
    from functools import lru_cache
except ImportError:
    from functools32 import lru_cache
from collections import namedtuple
from common.calculator import mean_ang, med_ang_res, sphe_to_kent, interval
import pandas as pd
import numpy as np


def nice(icerec):
    """
    Translates ice-model version strings to a standardized format.

    Parameters
    ----------
    icerec : str
        The ice-model version string to be translated.

    Returns
    -------
    str
        The standardized ice-model version string.
    """
    translator = {'cxdx': '3.2+', 'latest-full': '3.2'}
    for icekey in translator:
        icerec = icerec.replace(icekey, translator[icekey])
    return icerec


def speclator(spec, icerec):
    """
    Constructs a descriptive string based on the specifier and ice-model version.

    Parameters
    ----------
    spec : str
        Specification string to determine additional descriptions.
    icerec : str
        The ice-model version string.

    Returns
    -------
    str
        A descriptive string combining ice-model version, mode, and additional info.
    """
    nicerec = nice(icerec)
    wbr = 'w/brights' if 'qsat1000000' in spec else ''
    mlp = 'track' if 'mlpd1' in spec else 'cascade'
    return ' '.join((nicerec, mlp, wbr))


@lru_cache(1024)
def qtots(dat):
    """
    Computes the total charge per DOM for PPC simulated hit files.

    Parameters
    ----------
    dat : str or DataFrame
        Input data file or DataFrame containing DOM simulation data.

    Returns
    -------
    numpy.ndarray
        Array of total charges per DOM.
    """
    if os.path.splitext(dat)[-1] == '.csv':
        dat = pd.read_csv(dat, index_col=0)
        qtots = [len(dat.loc[(dat['str'] == s) & (dat['om'] == om)]) for s
                 in dat['str'].unique() for om in
                 dat.loc[dat['str'] == s]['om'].unique()]
    else:
        dat = pd.read_csv(dat, sep=' ', header=None, names=('str', 'om', 'time', 'charge'))
        qtots = [dat.loc[(dat['str'] == s) & (dat['om'] == om)]['charge'].sum() for s
                 in dat['str'].unique() for om in
                 dat.loc[dat['str'] == s]['om'].unique()]

    return np.array(qtots)


def read_single(llhout, llhcut=np.inf, lpat=r'^[+0-9]'):
    """
    Reads and parses a single LLH output file into a pandas DataFrame.

    Parameters
    ----------
    llhout : str
        Filepath to the LLH output file.
    llhcut : float, optional
        Maximum allowed LLH value (default is infinity).
    lpat : str, optional
        Regular expression pattern to match LLH lines (default is '^[+0-9]').

    Returns
    -------
    pandas.DataFrame
        Parsed LLH data as a DataFrame.
    """
    def parse_losses(vect):
        """ parse energy loss vector, for cascades it's 1.0.
        """
        if isinstance(vect,str):
            return np.asarray([float(_) for _ in str.split(vect)])
        else:
            return vect

    llhdat = pd.read_csv(llhout, delim_whitespace=True, header=None,
                         names='l rlogl x y z zenith azimuth e t a b'.split(),
                         usecols=lambda x: x[0] in 'lrxyzaetb', engine='python')
    select = llhdat['l'].str.match(lpat)
    llhdat = llhdat.loc[select].apply(pd.to_numeric, errors='ignore')
    lssdat = pd.read_csv(llhout, delimiter=':', header=None,
                         names='ll losses'.split(), usecols=lambda x: x[0] == 'l')
    lssdat = lssdat.loc[(lssdat['ll'] == 'E') & np.roll(select, -2)]
    lssdat['losses'] = lssdat['losses'].apply(parse_losses)
    llhdat.reset_index(drop=True, inplace=True)
    lssdat.reset_index(drop=True, inplace=True)
    llhdat = pd.concat((llhdat, lssdat), axis=1)
    llhsteps = llhdat.loc[(llhdat['rlogl'] < llhcut)]
    return llhsteps


def read(llhouts, llhcut=np.inf, lpat=r'^[+0-9]'):
    """
    Reads and parses one or more LLH output files into a pandas DataFrame.

    Parameters
    ----------
    llhouts : str or list of str
        Filepath(s) to the LLH output file(s).
    llhcut : float, optional
        Maximum allowed LLH value (default is infinity).
    lpat : str, optional
        Regular expression pattern to match LLH lines (default is '^[+0-9]').

    Returns
    -------
    pandas.DataFrame
        Concatenated parsed LLH data as a DataFrame.
    """
    if isinstance(llhouts, str):
        return read_single(llhouts, llhcut, lpat)
    else:
        return pd.concat([read_single(llhout, llhcut, lpat) for llhout in llhouts])


def llh_stats(finput, llhchoice='minlast', llhcut=np.inf, lpat=r'^[+0-9]', mlpd_npad=12):
    """
    Computes statistics from LLH output data.

    Parameter *llhchoice* can be
    'min': returns the absolute best fit... in this case there are no errors
    'cut': uses fits with rlogl<llhcut
    'last': uses last 5% of steps
    'all': uses all steps
    'minlast': uses min rlogl half of last 10% of steps. used in llh.cxx
    'llhout': same as 'minlast' but returns the absolute best fit instead of mean

    Parameters
    ----------
    finput : str or list of str
        Input file or list of files containing LLH data.
    llhchoice : str, optional
        Method for selecting LLH steps. Options are 'min', 'cut', 'last', 
        'all', 'minlast', or 'llhout' (default is 'minlast').
    llhcut : float, optional
        Maximum allowed LLH value (default is infinity).
    lpat : str, optional
        Regular expression pattern to match LLH lines (default is '^[+0-9]').
    mlpd_npad : int, optional
        Number of 7.5m steps to exclude in the first and last part of MLPD=1
        reconstructions. This reduces contributions to the energy reconstruction
        from large stochastics fitted outside of the detector (default is 12).

    Returns
    -------
    namedtuple
        Contains centers, errors, and intervals based on LLH data.
    """
    Centers = namedtuple('Centers', 'rlogl x y z zenith azimuth e t')
    Errors = namedtuple('Errors', 'dl dx dy dz dr dA de dt N Dxyz')
    Intervals = namedtuple('Intervals', 'elow emode ehigh')
    dl = dx = dy = dz = dr = de = dt = dA = Dxyz = 0
    fn_npad = lambda frs: np.sum(frs[mlpd_npad:-mlpd_npad]) if isinstance(frs, np.ndarray) else 1
    if llhchoice == 'min':
        llhsteps = read(finput, llhcut, lpat)
        llhsteps['e'] *= llhsteps['losses'].apply(fn_npad)
        rlogl, x, y, z, zenith, azimuth, e, t = llhsteps.loc[llhsteps['rlogl'].idxmin()][
            ['rlogl', 'x', 'y', 'z', 'zenith', 'azimuth', 'e', 't']]
    else:
        if llhchoice == 'cut':
            llhsteps = read(finput, llhcut, lpat)
        elif llhchoice == 'last':
            llhfull = read(finput, np.inf)
            # keep only the last 5%
            keep = int(0.05*len(llhfull.index))
            llhsteps = llhfull.iloc[-keep:]
        elif llhchoice == 'minlast' or llhchoice == 'llhout':
            llhfull = read(finput, np.inf, lpat)
            keep = int(0.1*len(llhfull.index))
            llhsteps = llhfull.iloc[-keep:].sort_values('rlogl').iloc[:keep//2]
        elif llhchoice == 'all':
            # avg over all steps
            llhsteps = read(finput, np.inf, lpat)

        llhsteps['e'] *= llhsteps['losses'].apply(fn_npad)
        rlogl, x, y, z, t = llhsteps[['rlogl', 'x', 'y', 'z', 't']].mean()
        e = 10**np.log10(llhsteps['e']).mean()
        dl, dx, dy, dz, dt = llhsteps[['rlogl', 'x', 'y', 'z', 't']].std()
        Dxyz = llhsteps[['x', 'y', 'z']].cov()
        de = e*np.log10(llhsteps['e']).std()*np.log(10)
        dr = np.sqrt(llhsteps['x']**2+llhsteps['y']**2+llhsteps['z']**2).std()
        # zenith, azimuth, R, kappa, sigma = vmf_stats(np.radians(llhsteps['zenith']), np.radians(llhsteps['azimuth']))
        norm, zenith, azimuth = mean_ang(np.radians(llhsteps['zenith']), np.radians(llhsteps['azimuth']))
        dA = med_ang_res(zenith, azimuth, np.radians(llhsteps['zenith']), np.radians(llhsteps['azimuth']))
        zenith = np.degrees(zenith)
        azimuth = np.degrees(azimuth)

        if llhchoice == 'llhout':
            x, y, z, zenith, azimuth, e, t = llhsteps.loc[llhsteps['rlogl'].idxmin()][['x', 'y', 'z', 'zenith', 'azimuth', 'e', 't']]

    centers = Centers(rlogl, x, y, z, zenith, azimuth, e, t)
    errors = Errors(dl, dx, dy, dz, dr, np.degrees(dA), de, dt, len(llhsteps), Dxyz)
    intervals = Intervals(*interval(llhsteps['e']))
    return centers, errors, intervals


def fb8(finput, llhcut=np.inf, lpat=r'^[+0-9]', verbose=False, fb5_only=False):
    """
    Fits points to an FB8 distribution using the fb8 package.

    Parameters
    ----------
    finput : str
        Input file containing LLH data.
    llhcut : float, optional
        Maximum allowed LLH value (default is infinity).
    lpat : str, optional
        Regular expression pattern to match LLH lines (default is '^[+0-9]').
    verbose : bool, optional
        Whether to enable verbose output (default is False).
    fb5_only : bool, optional
        Whether to use only FB5 distribution (default is False).

    Returns
    -------
    dict or None
        FB8 distribution parameters or None if no data is available.
    """
    from sphere import distribution as sd
    llhsteps = read(finput, llhcut, lpat)

    xs = sphe_to_kent(np.radians(llhsteps['zenith']),
                      np.radians(llhsteps['azimuth']))
    if len(xs) > 0:
        return sd.fb8_mle(xs, verbose, fb5_only=fb5_only)
    else:
        return None
