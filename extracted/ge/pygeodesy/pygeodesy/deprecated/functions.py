
# -*- coding: utf-8 -*-

u'''DEPRECATED functions kept for backward compatibility.
'''

from pygeodesy.constants import EPS, R_M, float0_
from pygeodesy.deprecated.classes import ClipCS3Tuple, TriAngle4Tuple, _TriAngle5Tuple
from pygeodesy.interns import NN, _area_, _COMMASPACE_, _negative_, \
                             _scalar_, _sep_, _SPACE_, _UNDER_, _value_
from pygeodesy.lazily import _ALL_DEPRECATED, _ALL_MODS as _MODS
from pygeodesy.props import deprecated_function
# from pygeodesy.resections import TriAngle5Tuple as _TriAngle5Tuple  # from .classes
from pygeodesy.units import _1mm, Number_, Scalar_

__all__ = _ALL_DEPRECATED.deprecated_functions
__version__ = '24.12.31'

_WGS84 = _UTM = object()


@deprecated_function
def anStr(name, OKd='._-', sub=_UNDER_):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.anstr}.'''
    return _MODS.streprs.anstr(name, OKd=OKd, sub=sub)


@deprecated_function
def areaof(points, adjust=True, radius=R_M, wrap=True):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.areaOf}.'''
    return _MODS.points.areaOf(points, adjust=adjust, radius=radius, wrap=wrap)


@deprecated_function
def atand(x):  # PYCHOK no cover
    '''DEPRECATED on 2023.09.28, use function L{pygeodesy.atan1d}.'''
    return _MODS.utily.atan1d(x)


@deprecated_function
def bounds(points, wrap=True, LatLon=None):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.boundsOf}.

       @return: 2-Tuple C{(latlonSW, latlonNE)}, each a B{C{LatLon}} or
                4-Tuple C{(latS, lonW, latN, lonE)} if C{B{LatLon} is None}.
    '''
    return tuple(_MODS.points.boundsOf(points, wrap=wrap, LatLon=LatLon))


@deprecated_function
def clipCS3(points, lowerleft, upperright, closed=False, inull=False):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.clipCS4}.

       @return: Yield a L{ClipCS3Tuple}C{(start, end, index)} for each
                edge of the I{clipped} path.
    '''
    for p1, p2, _, j in _MODS.clipy.clipCS4(points, lowerleft, upperright,
                                                    closed=closed, inull=inull):
        yield ClipCS3Tuple(p1, p2, j)


@deprecated_function
def clipDMS(deg, limit):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.clipDegrees}.'''
    return _MODS.dms.clipDegrees(deg, limit)


@deprecated_function
def clipStr(bstr, limit=50, white=NN):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.clips}.'''
    return _MODS.basics.clips(bstr, limit=limit, white=white)


@deprecated_function
def collins(pointA, pointB, pointC, alpha, beta, **useZ_Clas_and_kwds):
    '''DEPRECATED, use function L{pygeodesy.collins5}.'''
    return _MODS.resections.collins5(pointA, pointB, pointC, alpha, beta,
                                   **useZ_Clas_and_kwds)


@deprecated_function
def copysign(x, y):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.copysign0}.'''
    return _MODS.basics.copysign0(x, y)


@deprecated_function
def cosineAndoyerLambert(lat1, lon1, lat2, lon2, **datum_wrap):
    '''DEPRECATED on 2024.12.31, use function L{pygeodesy.cosineLaw} with C{B{corr}=1}.'''
    return _MODS.formy.cosineLaw(lat1, lon1, lat2, lon2, corr=1, **datum_wrap)


@deprecated_function
def cosineAndoyerLambert_(phi2, phi1, lam21, **datum):
    '''DEPRECATED on 2024.12.31, use function L{pygeodesy.cosineLaw_} with C{B{corr}=1}.'''
    return _MODS.formy.cosineLaw_(phi2, phi1, lam21, corr=1, **datum)


@deprecated_function
def cosineForsytheAndoyerLambert(lat1, lon1, lat2, lon2, **datum_wrap):
    '''DEPRECATED on 2024.12.31, use function L{pygeodesy.cosineLaw} with C{B{corr}=2}.'''
    return _MODS.formy.cosineLaw(lat1, lon1, lat2, lon2, corr=2, **datum_wrap)


@deprecated_function
def cosineForsytheAndoyerLambert_(phi2, phi1, lam21, **datum):
    '''DEPRECATED on 2024.12.31, use function L{pygeodesy.cosineLaw_} with C{B{corr}=2}.'''
    return _MODS.formy.cosineLaw_(phi2, phi1, lam21, corr=2, **datum)


@deprecated_function
def decodeEPSG2(arg):  # PYCHOK no cover
    '''DEPRECATED, use function L{epsg.decode2}.

       @return: 2-Tuple C{(zone, hemipole)}
    '''
    return tuple(_MODS.epsg.decode2(arg))


@deprecated_function
def encodeEPSG(zone, hemipole=NN, band=NN):  # PYCHOK no cover
    '''DEPRECATED, use function L{epsg.encode}.

       @return: C{EPSG} code (C{int}).
    '''
    return int(_MODS.epsg.encode(zone, hemipole=hemipole, band=band))


@deprecated_function
def enStr2(easting, northing, prec, *extras):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.enstr2}.'''
    return _MODS.streprs.enstr2(easting, northing, (int(prec) // 2 - 5), *extras)


@deprecated_function
def equirectangular_(lat1, lon1, lat2, lon2, **options):  # PYCHOK no cover
    '''DEPRECATED on 2024.05.25, use function L{pygeodesy.equirectangular4}.'''
    return _MODS.formy.equirectangular4(lat1, lon1, lat2, lon2, **options)


@deprecated_function
def equirectangular3(lat1, lon1, lat2, lon2, **options):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.equirectangular4}.

       @return: 3-Tuple C{(distance2, delta_lat, delta_lon)}.
    '''
    return tuple(_MODS.formy.equirectangular4(lat1, lon1, lat2, lon2, **options)[:3])


@deprecated_function
def excessAbc(A, b, c):  # PYCHOK no cover
    '''DEPRECATED on 2023.04.04, use function L{pygeodesy.excessAbc_}.'''
    return _MODS.formy.excessAbc_(A, b, c)


@deprecated_function
def excessGirard(A, B, C):  # PYCHOK no cover
    '''DEPRECATED on 2023.04.04, use function L{pygeodesy.excessGirard_}.'''
    return _MODS.formy.excessGirard_(A, B, C)


@deprecated_function
def excessLHuilier(a, b, c):  # PYCHOK no cover
    '''DEPRECATED on 2023.04.04, use function L{pygeodesy.excessLHuilier_}.'''
    return _MODS.formy.excessLHuilier_(a, b, c)


@deprecated_function
def false2f(value, name=_value_, false=True, Error=ValueError):  # PYCHOK no cover
    '''DEPRECATED, use class L{Easting} or L{Northing}.'''
    return falsed2f(falsed=false, Error=Error, **{name: value})


@deprecated_function
def falsed2f(falsed=True, Error=ValueError, **name_value):  # PYCHOK no cover
    '''DEPRECATED, use class L{Easting} or L{Northing}.

       Convert a falsed east-/northing to non-negative C{float}.

       @kwarg falsed: Value includes false origin (C{bool}).
       @kwarg Error: Optional, overriding error (C{Exception}).
       @kwarg name_value: One C{B{name}=value} pair.

       @return: The value (C{float}).

       @raise Error: Invalid or negative C{B{name}=value}.
    '''
    t = NN
    if len(name_value) == 1:
        try:
            for f in name_value.values():
                f = float(f)
                if falsed and f < 0:
                    break
                return f
            t = _COMMASPACE_('falsed', _negative_)
        except (TypeError, ValueError) as x:
            t = str(x)
    raise _MODS.errors._InvalidError(Error=Error, txt=t, **name_value)


@deprecated_function
def float0(*xs):  # PYCHOK no cover
    '''DEPRECATED on 2023.04.21, use function L{pygeodesy.float0_}.'''
    return float0_(*xs)


@deprecated_function
def fStr(floats, prec=6, fmt=_MODS.streprs.Fmt.f, ints=False, sep=_COMMASPACE_):  # PYCHOK no cover
    '''DEPRECATED, use function L{fstr}.'''
    return _MODS.streprs.fstr(floats, prec=prec, fmt=fmt, ints=ints, sep=sep)


@deprecated_function
def fStrzs(floatstr):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.fstrzs}.'''
    return _MODS.streprs.fstrzs(floatstr)


@deprecated_function
def Fsum2product(*xs, **kwds):
    '''DEPRECATED on 2024.09.19, use L{Fsum}C{(*B{xs}, B{f2product}=True, ...)}.'''
    F = _MODS.fsums.Fsum(**kwds)
    _ = F.f2product(True)
    return F._facc_args(xs, up=False) if xs else F


@deprecated_function
def hypot3(x, y, z):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.hypot_}.'''
    return _MODS.fmath.hypot_(x, y, z)


@deprecated_function
def inStr(inst, *args, **kwds):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.instr}.'''
    return _MODS.streprs.instr(inst, *args, **kwds)


@deprecated_function
def isenclosedby(point, points, wrap=False):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.isenclosedBy}.'''
    return _MODS.points.isenclosedBy(point, points, wrap=wrap)


@deprecated_function
def istuplist(obj, minum=0):  # PYCHOK no cover
    '''DEPRECATED on 2023.03.31, use function L{pygeodesy.islistuple}.'''
    return _MODS.basics.islistuple(obj, minum=minum)


@deprecated_function
def joined(*words, **sep):  # PYCHOK no cover
    '''DEPRECATED, use C{NN(...)}, C{NN.join_} or C{B{sep}.join}.'''
    return sep.get(_sep_, NN).join(map(str, words))


@deprecated_function
def joined_(*words, **sep):  # PYCHOK no cover
    '''DEPRECATED, use C{_SPACE_(...)}, C{_SPACE_.join_} or C{B{sep}.join}, sep=" ".'''
    return sep.get(_sep_, _SPACE_).join(map(str, words))


@deprecated_function
def nearestOn3(point, points, closed=False, wrap=False, **options):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.nearestOn5}.

       @return: 3-Tuple C{(lat, lon, distance)}
    '''
    return tuple(_MODS.points.nearestOn5(point, points, closed=closed, wrap=wrap, **options)[:3])


@deprecated_function
def nearestOn4(point, points, closed=False, wrap=False, **options):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.nearestOn5}.

       @return: 4-Tuple C{(lat, lon, distance, angle)}
    '''
    return tuple(_MODS.points.nearestOn5(point, points, closed=closed, wrap=wrap, **options)[:4])


@deprecated_function
def parseUTM(strUTM, datum=_WGS84, Utm=_UTM, name=NN):  # PYCHOK no cover
    '''DEPRECATED, use function L{parseUTM5}.

       @return: The UTM coordinate (B{L{Utm}}) or 4-tuple C{(zone,
                hemisphere, easting, northing)} if C{B{Utm} is None}.
    '''
    d = _MODS.datums.Datums.WGS84 if datum is _WGS84 else datum  # PYCHOK shadows?
    U = _MODS.utm.Utm if Utm is _UTM else Utm
    r = _MODS.utm.parseUTM5(strUTM, datum=d, Utm=U, name=name)
    if isinstance(r, tuple):  # UtmUps5Tuple
        r = r.zone, r.hemipole, r.easting, r.northing  # no band
    return r


@deprecated_function
def perimeterof(points, closed=False, adjust=True, radius=R_M, wrap=True):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.perimeterOf}.'''
    return _MODS.points.perimeterOf(points, closed=closed, adjust=adjust, radius=radius, wrap=wrap)


@deprecated_function
def polygon(points, closed=True, base=None):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.points2}.'''
    return _MODS.deprecated.bases.points2(points, closed=closed, base=base)


@deprecated_function
def scalar(value, low=EPS, high=1.0, name=_scalar_, Error=ValueError):  # PYCHOK no cover
    '''DEPRECATED, use class L{Number_} or L{Scalar_}.

       @return: New value (C{float} or C{int} for C{int} B{C{low}}).

       @raise Error: Invalid B{C{value}}.
    '''
    C_ = Number_ if _MODS.basics.isint(low) else Scalar_
    return C_(value, name=name, Error=Error, low=low, high=high)


@deprecated_function
def simplify2(points, pipe=_1mm, **radius_shortest_indices_options):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.simplifyRW}.'''
    return _MODS.simplify.simplifyRW(points, pipe=pipe, **radius_shortest_indices_options)


@deprecated_function
def simplifyRDPm(points, distance=_1mm, **radius_shortest_indices_options):
    '''DEPRECATED on 2024.11.28, use function L{pygeodesy.simplifyRDP}C{(points, modified=True, ...)}.'''
    return _MODS.simplify.simplifyRDP(points, modified=True, distance=distance, **radius_shortest_indices_options)


@deprecated_function
def simplifyVWm(points, area=_1mm, **radius_attr_indices_options):
    '''DEPRECATED on 2024.11.28, use function L{pygeodesy.simplifyVW}C{(points, modified=True, ...)}.'''
    return _MODS.simplify.simplifyVW(points, modified=True, area=area, **radius_attr_indices_options)


@deprecated_function
def tienstra(pointA, pointB, pointC, alpha, **beta_gamma_useZ_Clas_and_kwds):
    '''DEPRECATED, use function L{pygeodesy.tienstra7}.'''
    return _MODS.resections.tienstra7(pointA, pointB, pointC, alpha, **beta_gamma_useZ_Clas_and_kwds)


@deprecated_function
def toUtm(latlon, lon=None, datum=None, Utm=_UTM, cmoff=True, name=NN):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.toUtm8}.

       @return: The UTM coordinate (B{C{Utm}}) or a 6-tuple C{(zone, easting, northing,
                band, convergence, scale)} if C{B{Utm} is None} or C{B{cmoff} is False}.
    '''
    U = _MODS.utm.Utm if Utm is _UTM else Utm
    r = _MODS.utm.toUtm8(latlon, lon=lon, datum=datum, Utm=U, name=name, falsed=cmoff)
    if isinstance(r, tuple):  # UtmUps8Tuple
        # no hemisphere/pole and datum
        r = r.zone, r.easting, r.northing, r.band, r.gamma, r.scale
    return r


# @deprecated_function
# def trfTransforms(reframe, epoch, reframe2, epoch2):
#     '''DEPRECATED on 2024.02.02, use function L{trfTransform0}C{(reframe, reframe2, epoch=None, epoch2=None)}.
#
#        @return: A 0-, 1- or 2-tuple of Helmert L{Transform}s or C{None} if no conversion exists.
#     '''
#     t = _MODS.trf.trfTransform0(reframe, reframe2, epoch=epoch, epoch2=epoch2)
#     return (t,) if t else t


@deprecated_function
def triAngle4(a, b, c):
    '''DEPRECATED on 2023.09.14, use function L{pygeodesy.triAngle5}.

       @return: A I{DEPRECATED} L{TriAngle4Tuple}C{(radA, radB, radC, rIn)}.
    '''
    assert _TriAngle5Tuple._Names_.index(_area_) == 4
    return  TriAngle4Tuple(_MODS.resections.triAngle5(a, b, c)[:4])


@deprecated_function
def unsign0(x):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.unsigned0}.'''
    return _MODS.basics.unsigned0(x)


@deprecated_function
def unStr(name, *args, **kwds):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.unstr}.'''
    return _MODS.streprs.unstr(name, *args, **kwds)


@deprecated_function
def utmZoneBand2(lat, lon):  # PYCHOK no cover
    '''DEPRECATED, use function L{pygeodesy.utmZoneBand5}.

       @return: 2-Tuple C{(zone, band)}.
    '''
    r = _MODS.utm.utmZoneBand5(lat, lon)  # UtmUpsLatLon5Tuple
    return r.zone, r.band

# **) MIT License
#
# Copyright (C) 2018-2025 -- mrJean1 at Gmail -- All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
