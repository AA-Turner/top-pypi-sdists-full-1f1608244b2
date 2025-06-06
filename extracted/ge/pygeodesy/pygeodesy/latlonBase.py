
# -*- coding: utf-8 -*-

u'''(INTERNAL) Base class L{LatLonBase} for all elliposiodal, spherical and N-vectorial C{LatLon} classes.

@see: I{(C) Chris Veness 2005-2024}' U{latlong<https://www.Movable-Type.co.UK/scripts/latlong.html>},
      U{-ellipsoidal<https://www.Movable-Type.co.UK/scripts/geodesy/docs/latlon-ellipsoidal.js.html>} and
      U{-vectors<https://www.Movable-Type.co.UK/scripts/latlong-vectors.html>} and I{Charles Karney}'s
      U{Rhumb<https://GeographicLib.SourceForge.io/C++/doc/classGeographicLib_1_1Rhumb.html>} and
      U{RhumbLine<https://GeographicLib.SourceForge.io/C++/doc/classGeographicLib_1_1RhumbLine.html>} classes.
'''

from pygeodesy.basics import _isin, isstr, map1, _xinstanceof
from pygeodesy.constants import EPS, EPS0, EPS1, EPS4, INT0, R_M, \
                               _EPSqrt as _TOL, _0_0, _0_5, _1_0, \
                               _360_0, _umod_360
from pygeodesy.datums import _spherical_datum
from pygeodesy.dms import F_D, F_DMS, latDMS, lonDMS, parse3llh
# from pygeodesy.ecef import EcefKarney  # _MODS
from pygeodesy.ecefLocals import _EcefLocal
from pygeodesy.errors import _AttributeError, IntersectionError, \
                             _incompatible, _IsnotError, _TypeError, \
                             _ValueError, _xattr, _xdatum, _xError, \
                             _xkwds, _xkwds_get, _xkwds_item2, _xkwds_not
# from pygeodesy.fmath import favg  # _MODS
# from pygeodesy import formy as _formy  # _MODS.into
from pygeodesy.internals import _passarg, typename
from pygeodesy.interns import NN, _COMMASPACE_, _concentric_, _intersection_, \
                             _LatLon_, _m_, _no_, _overlap_,  _point_  # PYCHOK used!
# from pygeodesy.iters import PointsIter, points2  # _MODS
# from pygeodesy.karney import Caps  # _MODS
from pygeodesy.lazily import _ALL_DOCS, _ALL_LAZY, _ALL_MODS as _MODS
from pygeodesy.named import _name2__, _NamedBase,  Fmt
from pygeodesy.namedTuples import Bounds2Tuple, LatLon2Tuple, PhiLam2Tuple, \
                                  Trilaterate5Tuple, Vector3Tuple
# from pygeodesy.nvectorBase import _N_vector_  # _MODS
from pygeodesy.props import deprecated_method, Property, Property_RO, \
                            property_RO, _update_all
# from pygeodesy.streprs import Fmt, hstr  # from .named, _MODS
from pygeodesy.units import _isDegrees, _isRadius, Distance_, Lat, Lon, \
                             Height, Radius, Radius_, Scalar, Scalar_
from pygeodesy.utily import sincos2d_, _unrollon, _unrollon3, _Wrap
# from pygeodesy.vector2d import _circin6, Circin6Tuple, _circum3, circum4_, \
#                                 Circum3Tuple, _radii11ABC4  # _MODS
# from pygeodesy.vector3d import nearestOn6, Vector3d  # _MODS

from contextlib import contextmanager
from math import asin, cos, degrees, fabs, radians

__all__ = _ALL_LAZY.latlonBase
__version__ = '25.05.07'

_formy = _MODS.into(formy=__name__)


class LatLonBase(_NamedBase, _EcefLocal):
    '''(INTERNAL) Base class for ellipsoidal and spherical C{satLon}s.
    '''
    _clipid = INT0  # polygonal clip, see .booleans
    _datum  = None  # L{Datum}, to be overriden
    _height = INT0  # height (C{meter}), default
    _lat    = 0     # latitude (C{degrees})
    _lon    = 0     # longitude (C{degrees})

    def __init__(self, lat_llh, lon=None, height=0, datum=None, **wrap_name):
        '''New C{LatLon}.

           @arg lat_llh: Latitude (C{degrees} or DMS C{str} with N or S suffix) or
                         a previous C{LatLon} instance provided C{B{lon}=None}.
           @kwarg lon: Longitude (C{degrees} or DMS C{str} with E or W suffix),
                       required if B{C{lat_llh}} is C{degrees} or C{str}.
           @kwarg height: Optional height above (or below) the earth surface
                          (C{meter}, conventionally).
           @kwarg datum: Optional datum (L{Datum}, L{Ellipsoid}, L{Ellipsoid2},
                         L{a_f2Tuple} or I{scalar} radius) or C{None}.
           @kwarg wrap_name: Optional C{B{name}=NN} (C{str}) and optional keyword
                       argument C{B{wrap}=False}, if C{True}, wrap or I{normalize}
                       B{C{lat}} and B{C{lon}} (C{bool}).

           @return: New instance (C{LatLon}).

           @raise RangeError: A B{C{lon}} or C{lat} value outside the valid
                              range and L{rangerrors} set to C{True}.

           @raise TypeError: If B{C{lat_llh}} is not a C{LatLon}.

           @raise UnitError: Invalid C{lat}, B{C{lon}} or B{C{height}}.
        '''
        w, n = self._wrap_name2(**wrap_name)
        if n:
            self.name = n

        if lon is None:
            lat, lon, height = _latlonheight3(lat_llh, height, w)
        elif w:
            lat, lon = _Wrap.latlonDMS2(lat_llh, lon)
        else:
            lat = lat_llh

        self._lat = Lat(lat)  # parseDMS2(lat, lon)
        self._lon = Lon(lon)  # PYCHOK LatLon2Tuple
        if height:  # elevation
            self._height = Height(height)
        if datum is not None:
            self._datum = _spherical_datum(datum, name=self.name)

    def __eq__(self, other):
        return self.isequalTo(other)

    def __ne__(self, other):
        return not self.isequalTo(other)

    def __str__(self):
        return self.toStr(form=F_D, prec=6)

    def antipode(self, height=None):
        '''Return the antipode, the point diametrically opposite to
           this point.

           @kwarg height: Optional height of the antipode (C{meter}),
                          this point's height otherwise.

           @return: The antipodal point (C{LatLon}).
        '''
        a = _formy.antipode(*self.latlon)
        h =  self._heigHt(height)
        return self.classof(*a, height=h)

    @deprecated_method
    def bounds(self, wide, tall, radius=R_M):  # PYCHOK no cover
        '''DEPRECATED, use method C{boundsOf}.'''
        return self.boundsOf(wide, tall, radius=radius)

    def boundsOf(self, wide, tall, radius=R_M, height=None, **name):
        '''Return the SW and NE lat-/longitude of a great circle
           bounding box centered at this location.

           @arg wide: Longitudinal box width (C{meter}, same units as
                      B{C{radius}} or C{degrees} if C{B{radius} is None}).
           @arg tall: Latitudinal box size (C{meter}, same units as
                      B{C{radius}} or C{degrees} if C{B{radius} is None}).
           @kwarg radius: Mean earth radius (C{meter}) or C{None} if I{both}
                          B{C{wide}} and B{C{tall}} are in C{degrees}.
           @kwarg height: Height for C{latlonSW} and C{latlonNE} (C{meter}),
                          overriding the point's height.
           @kwarg name: Optional C{B{name}=NN} (C{str}).

           @return: A L{Bounds2Tuple}C{(latlonSW, latlonNE)}, the lower-left
                    and upper-right corner (C{LatLon}).

           @see: U{https://www.Movable-Type.co.UK/scripts/latlong-db.html}
        '''
        w = Scalar_(wide=wide) * _0_5
        t = Scalar_(tall=tall) * _0_5
        if radius is not None:
            r = Radius_(radius)
            c = cos(self.phi)
            w = degrees(asin(w / r) / c) if fabs(c) > EPS0 else _0_0  # XXX
            t = degrees(t / r)
        y, t = self.lat, fabs(t)
        x, w = self.lon, fabs(w)

        h  = self._heigHt(height)
        sw = self.classof(y - t, x - w, height=h)
        ne = self.classof(y + t, x + w, height=h)
        return Bounds2Tuple(sw, ne, name=self._name__(name))

    def chordTo(self, other, height=None, wrap=False):
        '''Compute the length of the chord through the earth between
           this and an other point.

           @arg other: The other point (C{LatLon}).
           @kwarg height: Overriding height for both points (C{meter}),
                          or if C{None}, use each point's height.
           @kwarg wrap: If C{True}, wrap or I{normalize} the B{C{other}}
                        point (C{bool}).

           @return: The chord length (conventionally C{meter}).

           @raise TypeError: The B{C{other}} point is not C{LatLon}.
        '''
        def _v3d(ll, V3d=_MODS.vector3d.Vector3d):
            t = ll.toEcef(height=height)  # .toVector(Vector=V3d)
            return V3d(t.x, t.y, t.z)

        p = self.others(other)
        if wrap:
            p = _Wrap.point(p)
        return _v3d(self).minus(_v3d(p)).length

    def circin6(self, point2, point3, eps=EPS4, **wrap_name):
        '''Return the radius and center of the I{inscribed} aka I{In-}circle
           of the (planar) triangle formed by this and two other points.

           @arg point2: Second point (C{LatLon}).
           @arg point3: Third point (C{LatLon}).
           @kwarg eps: Tolerance for function L{pygeodesy.trilaterate3d2}.
           @kwarg wrap_name: Optional C{B{name}=NN} (C{str}) and optional keyword
                       argument C{B{wrap}=False}, if C{True}, wrap or I{normalize}
                       the B{C{points}} (C{bool}).

           @return: A L{Circin6Tuple}C{(radius, center, deltas, cA, cB, cC)}.  The
                    C{center} and contact points C{cA}, C{cB} and C{cC}, each an
                    instance of this (sub-)class, are co-planar with this and the
                    two given points, see the B{Note} below.

           @raise ImportError: Package C{numpy} not found, not installed or older
                               than version 1.10.

           @raise IntersectionError: Near-coincident or -colinear points or
                                     a trilateration or C{numpy} issue.

           @raise TypeError: Invalid B{C{point2}} or B{C{point3}}.

           @note: The C{center} is trilaterated in cartesian (ECEF) space and converted
                  back to geodetic lat-, longitude and height.  The latter, conventionally
                  in C{meter} indicates whether the C{center} is above, below or on the
                  surface of the earth model.  If C{deltas} is C{None}, the C{center} is
                  I{un}ambigous.  Otherwise C{deltas} is a L{LatLon3Tuple}C{(lat, lon,
                  height)} representing the differences between both results from
                  L{pygeodesy.trilaterate3d2} and C{center} is the mean thereof.

           @see: Function L{pygeodesy.circin6}, method L{circum3}, U{Incircle
                 <https://MathWorld.Wolfram.com/Incircle.html>} and U{Contact Triangle
                 <https://MathWorld.Wolfram.com/ContactTriangle.html>}.
        '''
        w, n = self._wrap_name2(**wrap_name)

        with _toCartesian3(self, point2, point3, w) as cs:
            m = _MODS.vector2d
            r, c, d, A, B, C = m._circin6(*cs, eps=eps, useZ=True, dLL3=True,
                                               datum=self.datum)  # PYCHOK unpack
            return m.Circin6Tuple(r, c.toLatLon(), d, A.toLatLon(),
                                                      B.toLatLon(),
                                                      C.toLatLon(), name=n)

    def circum3(self, point2, point3, circum=True, eps=EPS4, **wrap_name):
        '''Return the radius and center of the smallest circle I{through} or I{containing}
           this and two other points.

           @arg point2: Second point (C{LatLon}).
           @arg point3: Third point (C{LatLon}).
           @kwarg circum: If C{True}, return the C{circumradius} and C{circumcenter},
                          always, ignoring the I{Meeus}' Type I case (C{bool}).
           @kwarg eps: Tolerance for function L{pygeodesy.trilaterate3d2}.
           @kwarg wrap_name: Optional C{B{name}=NN} (C{str}) and optional keyword
                       argument C{B{wrap}=False}, if C{True}, wrap or I{normalize}
                       the B{C{points}} (C{bool}).

           @return: A L{Circum3Tuple}C{(radius, center, deltas)}.  The C{center}, an
                    instance of this (sub-)class, is co-planar with this and the two
                    given points.  If C{deltas} is C{None}, the C{center} is
                    I{un}ambigous.  Otherwise C{deltas} is a L{LatLon3Tuple}C{(lat,
                    lon, height)} representing the difference between both results
                    from L{pygeodesy.trilaterate3d2} and C{center} is the mean thereof.

           @raise ImportError: Package C{numpy} not found, not installed or older than
                               version 1.10.

           @raise IntersectionError: Near-concentric, -coincident or -colinear points,
                                     incompatible C{Ecef} classes or a trilateration
                                     or C{numpy} issue.

           @raise TypeError: Invalid B{C{point2}} or B{C{point3}}.

           @note: The C{center} is trilaterated in cartesian (ECEF) space and converted
                  back to geodetic lat-, longitude and height.  The latter, conventionally
                  in C{meter} indicates whether the C{center} is above, below or on the
                  surface of the earth model.  If C{deltas} is C{None}, the C{center} is
                  I{un}ambigous.  Otherwise C{deltas} is a L{LatLon3Tuple}C{(lat, lon,
                  height)} representing the difference between both results from
                  L{pygeodesy.trilaterate3d2} and C{center} is the mean thereof.

           @see: Function L{pygeodesy.circum3} and methods L{circin6} and L{circum4_}.
        '''
        w, n = self._wrap_name2(**wrap_name)

        with _toCartesian3(self, point2, point3, w, circum=circum) as cs:
            m = _MODS.vector2d
            r, c, d = m._circum3(*cs, circum=circum, eps=eps, useZ=True, dLL3=True,  # XXX -3d2
                                      clas=cs[0].classof, datum=self.datum)  # PYCHOK unpack
            return m.Circum3Tuple(r, c.toLatLon(), d, name=n)

    def circum4_(self, *points, **wrap_name):
        '''Best-fit a sphere through this and two or more other points.

           @arg points: The other points (each a C{LatLon}).
           @kwarg wrap_name: Optional C{B{name}=NN} (C{str}) and optional keyword argument
                       C{B{wrap}=False}, if C{True}, wrap or I{normalize} the B{C{points}}
                       (C{bool}).

           @return: A L{Circum4Tuple}C{(radius, center, rank, residuals)} with C{center} an
                    instance of this (sub-)class.

           @raise ImportError: Package C{numpy} not found, not installed or older than
                               version 1.10.

           @raise NumPyError: Some C{numpy} issue.

           @raise TypeError: One of the B{C{points}} invalid.

           @raise ValueError: Too few B{C{points}}.

           @see: Function L{pygeodesy.circum4_} and L{circum3}.
        '''
        w, n = self._wrap_name2(**wrap_name)

        def _cs(ps, C, w):
            _wp = _Wrap.point if w else _passarg
            for i, p in enumerate(ps):
                yield C(i=i, points=_wp(p))

        C =  self._toCartesianEcef
        c =  C(point=self)
        t = _MODS.vector2d.circum4_(c, Vector=c.classof, *_cs(points, C, w))
        c =  t.center.toLatLon(LatLon=self.classof)
        return t.dup(center=c, name=n)

    @property
    def clipid(self):
        '''Get the (polygonal) clip (C{int}).
        '''
        return self._clipid

    @clipid.setter  # PYCHOK setter!
    def clipid(self, clipid):
        '''Get the (polygonal) clip (C{int}).
        '''
        self._clipid = int(clipid)

    @deprecated_method
    def compassAngle(self, other, **adjust_wrap):  # PYCHOK no cover
        '''DEPRECATED, use method L{compassAngleTo}.'''
        return self.compassAngleTo(other, **adjust_wrap)

    def compassAngleTo(self, other, **adjust_wrap):
        '''Return the angle from North for the direction vector between
           this and an other point.

           Suitable only for short, non-near-polar vectors up to a few
           hundred Km or Miles.  Use method C{initialBearingTo} for
           larger distances.

           @arg other: The other point (C{LatLon}).
           @kwarg adjust_wrap: Optional keyword arguments for function
                               L{pygeodesy.compassAngle}.

           @return: Compass angle from North (C{degrees360}).

           @raise TypeError: The B{C{other}} point is not C{LatLon}.

           @note: Courtesy of Martin Schultz.

           @see: U{Local, flat earth approximation
                 <https://www.EdWilliams.org/avform.htm#flat>}.
        '''
        p = self.others(other)
        return _formy.compassAngle(self.lat, self.lon, p.lat, p.lon, **adjust_wrap)

    @deprecated_method
    def cosineAndoyerLambertTo(self, other, **wrap):
        '''DEPRECATED on 2024.12.31, use method L{cosineLawTo} with C{B{corr}=1}.'''
        return self.cosineLawTo(other, corr=1, **wrap)

    @deprecated_method
    def cosineForsytheAndoyerLambertTo(self, other, **wrap):
        '''DEPRECATED on 2024.12.31, use method L{cosineLawTo} with C{B{corr}=2}.'''
        return self.cosineLawTo(other, corr=2, **wrap)

    def cosineLawTo(self, other, **radius__corr_wrap):
        '''Compute the distance between this and an other point using the U{Law of
           Cosines<https://www.Movable-Type.co.UK/scripts/latlong.html#cosine-law>}
           formula, optionally corrected.

           @arg other: The other point (C{LatLon}).
           @kwarg radius__corr_wrap: Optional earth C{B{radius}=None} (C{meter}),
                          overriding the equatorial or mean radius of this point's
                          datum's ellipsoid and keyword arguments for function
                          L{pygeodesy.cosineLaw}.

           @return: Distance (C{meter}, same units as B{C{radius}}).

           @raise TypeError: The B{C{other}} point is not C{LatLon}.

           @see: Function L{pygeodesy.cosineLaw} and methods C{distanceTo*},
                 L{equirectangularTo}, L{euclideanTo}, L{flatLocalTo} /
                 L{hubenyTo}, L{flatPolarTo}, L{haversineTo}, L{thomasTo} and
                 L{vincentysTo}.
        '''
        c = _xkwds_get(radius__corr_wrap, corr=0)
        return self._distanceTo_(_formy.cosineLaw_, other, **radius__corr_wrap) if c else \
               self._distanceTo( _formy.cosineLaw,  other, **radius__corr_wrap)

    @property_RO
    def datum(self):  # PYCHOK no cover
        '''I{Must be overloaded}.'''
        self._notOverloaded()

    def destinationXyz(self, delta, LatLon=None, **LatLon_kwds):
        '''Calculate the destination using a I{local} delta from this point.

           @arg delta: Local delta to the destination (L{XyzLocal}, L{Aer}, L{Enu}, L{Ned}
                       or L{Local9Tuple}).
           @kwarg LatLon: Optional (geodetic) class to return the destination or C{None}.
           @kwarg LatLon_kwds: Optionally, additional B{C{LatLon}} keyword arguments,
                               ignored if C{B{LatLon} is None}.

           @return: An B{C{LatLon}} instance or if C{B{LatLon} is None}, a
                    L{LatLon4Tuple}C{(lat, lon, height, datum)} or L{LatLon3Tuple}C{(lat,
                    lon, height)} if a C{datum} keyword is specified or not.

           @raise TypeError: Invalid B{C{delta}}, B{C{LatLon}} or B{C{LatLon_kwds}} item.
        '''
        t = self._ltp._local2ecef(delta, nine=True)  # _EcefLocal._ltp
        return t.toLatLon(LatLon=LatLon, **_xkwds(LatLon_kwds, name=self.name))

    def _distanceTo(self, func, other, radius=None, **kwds):
        '''(INTERNAL) Helper for distance methods C{<func>To}.
        '''
        p = self.others(other, up=2)
        R = radius or (self._datum.ellipsoid.R1 if self._datum else R_M)
        return func(self.lat, self.lon, p.lat, p.lon, radius=R, **kwds)

    def _distanceTo_(self, func_, other, wrap=False, radius=None, **kwds):
        '''(INTERNAL) Helper for (ellipsoidal) distance methods C{<func>To}.
        '''
        p = self.others(other, up=2)
        D = self.datum or _spherical_datum(radius or R_M, func_)
        lam21, phi2, _ = _Wrap.philam3(self.lam, p.phi, p.lam, wrap)
        r = func_(phi2, self.phi, lam21, datum=D, **kwds)
        return r * (radius or D.ellipsoid.a)

    @Property_RO
    def _Ecef_forward(self):
        '''(INTERNAL) Helper for L{_ecef9} and L{toEcef} (C{callable}).
        '''
        return self.Ecef(self.datum, name=self.name).forward

    @Property_RO
    def _ecef9(self):
        '''(INTERNAL) Helper for L{toCartesian}, L{toEcef} and L{toCartesian} (L{Ecef9Tuple}).
        '''
        return self._Ecef_forward(self, M=True)

    @property_RO
    def ellipsoidalLatLon(self):
        '''Get the C{LatLon type} iff ellipsoidal, overloaded in L{LatLonEllipsoidalBase}.
        '''
        return False

    @deprecated_method
    def equals(self, other, eps=None):  # PYCHOK no cover
        '''DEPRECATED, use method L{isequalTo}.'''
        return self.isequalTo(other, eps=eps)

    @deprecated_method
    def equals3(self, other, eps=None):  # PYCHOK no cover
        '''DEPRECATED, use method L{isequalTo3}.'''
        return self.isequalTo3(other, eps=eps)

    def equirectangularTo(self, other, **radius_adjust_limit_wrap):
        '''Compute the distance between this and an other point
           using the U{Equirectangular Approximation / Projection
           <https://www.Movable-Type.co.UK/scripts/latlong.html#equirectangular>}.

           Suitable only for short, non-near-polar distances up to a
           few hundred Km or Miles.  Use method L{haversineTo} or
           C{distanceTo*} for more accurate and/or larger distances.

           @arg other: The other point (C{LatLon}).
           @kwarg radius_adjust_limit_wrap: Optional keyword arguments
                         for function L{pygeodesy.equirectangular},
                         overriding the default mean C{radius} of this
                         point's datum ellipsoid.

           @return: Distance (C{meter}, same units as B{C{radius}}).

           @raise TypeError: The B{C{other}} point is not C{LatLon}.

           @see: Function L{pygeodesy.equirectangular} and methods L{cosineLawTo},
                 C{distanceTo*}, C{euclideanTo}, L{flatLocalTo} / L{hubenyTo},
                 L{flatPolarTo}, L{haversineTo}, L{thomasTo} and L{vincentysTo}.
        '''
        return self._distanceTo(_formy.equirectangular, other, **radius_adjust_limit_wrap)

    def euclideanTo(self, other, **radius_adjust_wrap):
        '''Approximate the C{Euclidian} distance between this and
           an other point.

           See function L{pygeodesy.euclidean} for the available B{C{options}}.

           @arg other: The other point (C{LatLon}).
           @kwarg radius_adjust_wrap: Optional keyword arguments for function
                         L{pygeodesy.euclidean}, overriding the default mean
                         C{radius} of this point's datum ellipsoid.

           @return: Distance (C{meter}, same units as B{C{radius}}).

           @raise TypeError: The B{C{other}} point is not C{LatLon}.

           @see: Function L{pygeodesy.euclidean} and methods L{cosineLawTo}, C{distanceTo*},
                 L{equirectangularTo}, L{flatLocalTo} / L{hubenyTo}, L{flatPolarTo},
                 L{haversineTo}, L{thomasTo} and L{vincentysTo}.
        '''
        return self._distanceTo(_formy.euclidean, other, **radius_adjust_wrap)

    def flatLocalTo(self, other, radius=None, **wrap):
        '''Compute the distance between this and an other point using the
           U{ellipsoidal Earth to plane projection
           <https://WikiPedia.org/wiki/Geographical_distance#Ellipsoidal_Earth_projected_to_a_plane>}
           aka U{Hubeny<https://www.OVG.AT/de/vgi/files/pdf/3781/>} formula.

           @arg other: The other point (C{LatLon}).
           @kwarg radius: Mean earth radius (C{meter}) or C{None} for the I{equatorial
                          radius} of this point's datum ellipsoid.
           @kwarg wrap: Optional keyword argument C{B{wrap}=False}, if C{True}, wrap
                        or I{normalize} and unroll the B{C{other}} point (C{bool}).

           @return: Distance (C{meter}, same units as B{C{radius}}).

           @raise TypeError: The B{C{other}} point is not C{LatLon}.

           @raise ValueError: Invalid B{C{radius}}.

           @see: Function L{pygeodesy.flatLocal}/L{pygeodesy.hubeny}, methods L{cosineLawTo},
                 C{distanceTo*}, L{equirectangularTo}, L{euclideanTo}, L{flatPolarTo},
                 L{haversineTo}, L{thomasTo} and L{vincentysTo} and U{local, flat Earth
                 approximation<https://www.edwilliams.org/avform.htm#flat>}.
        '''
        r = radius if _isin(radius, None, R_M, _1_0, 1) else Radius(radius)
        return self._distanceTo_(_formy.flatLocal_, other, radius=r, **wrap)  # PYCHOK kwargs

    hubenyTo = flatLocalTo  # for Karl Hubeny

    def flatPolarTo(self, other, **radius_wrap):
        '''Compute the distance between this and an other point using
           the U{polar coordinate flat-Earth<https://WikiPedia.org/wiki/
           Geographical_distance#Polar_coordinate_flat-Earth_formula>} formula.

           @arg other: The other point (C{LatLon}).
           @kwarg radius_wrap: Optional C{B{radius}=R_M} and C{B{wrap}=False} for
                         function L{pygeodesy.flatPolar}, overriding the default
                         C{mean radius} of this point's datum ellipsoid.

           @return: Distance (C{meter}, same units as B{C{radius}}).

           @raise TypeError: The B{C{other}} point is not C{LatLon}.

           @see: Function L{pygeodesy.flatPolar} and methods L{cosineLawTo}, C{distanceTo*},
                 L{equirectangularTo}, L{euclideanTo}, L{flatLocalTo} / L{hubenyTo},
                 L{haversineTo}, L{thomasTo} and L{vincentysTo}.
        '''
        return self._distanceTo(_formy.flatPolar, other, **radius_wrap)

    def hartzell(self, los=False, earth=None):
        '''Compute the intersection of a Line-Of-Sight from this (geodetic) Point-Of-View
           (pov) with this point's ellipsoid surface.

           @kwarg los: Line-Of-Sight, I{direction} to the ellipsoid (L{Los}, L{Vector3d}),
                       C{True} for the I{normal, plumb} onto the surface or I{False} or
                       C{None} to point to the center of the ellipsoid.
           @kwarg earth: The earth model (L{Datum}, L{Ellipsoid}, L{Ellipsoid2}, L{a_f2Tuple}
                         or C{scalar} radius in C{meter}), overriding this point's C{datum}
                         ellipsoid.

           @return: The intersection (C{LatLon}) with attribute C{.height} set to the distance
                    to this C{pov}.

           @raise IntersectionError: Null or bad C{pov} or B{C{los}}, this C{pov} is inside
                                     the ellipsoid or B{C{los}} points outside or away from
                                     the ellipsoid.

           @raise TypeError: Invalid B{C{los}} or invalid or undefined B{C{earth}} or C{datum}.

           @see: Function L{hartzell<pygeodesy.formy.hartzell>} for further details.
        '''
        return _formy._hartzell(self, los, earth, LatLon=self.classof)

    def haversineTo(self, other, **radius_wrap):
        '''Compute the distance between this and an other point using the U{Haversine
           <https://www.Movable-Type.co.UK/scripts/latlong.html>} formula.

           @arg other: The other point (C{LatLon}).
           @kwarg radius_wrap: Optional C{B{radius}=R_M} and C{B{wrap}=False} for function
                         L{pygeodesy.haversine}, overriding the default C{mean radius} of
                         this point's datum ellipsoid.

           @return: Distance (C{meter}, same units as B{C{radius}}).

           @raise TypeError: The B{C{other}} point is not C{LatLon}.

           @see: Function L{pygeodesy.haversine} and methods L{cosineLawTo}, C{distanceTo*},
                 L{equirectangularTo}, L{euclideanTo}, L{flatLocalTo} / L{hubenyTo}, \
                 L{flatPolarTo}, L{thomasTo} and L{vincentysTo}.
        '''
        return self._distanceTo(_formy.haversine, other, **radius_wrap)

    def _havg(self, other, f=_0_5, h=None):
        '''(INTERNAL) Weighted, average height.

           @arg other: An other point (C{LatLon}).
           @kwarg f: Optional fraction (C{float}).
           @kwarg h: Overriding height (C{meter}).

           @return: Average, fractional height (C{float}) or the
                    overriding height B{C{h}} (C{Height}).
        '''
        return Height(h) if h is not None else \
              _MODS.fmath.favg(self.height, other.height, f=f)

    @Property
    def height(self):
        '''Get the height (C{meter}).
        '''
        return self._height

    @height.setter  # PYCHOK setter!
    def height(self, height):
        '''Set the height (C{meter}).

           @raise TypeError: Invalid B{C{height}} C{type}.

           @raise ValueError: Invalid B{C{height}}.
        '''
        h = Height(height)
        if self._height != h:
            _update_all(self)
            self._height = h

    def _heigHt(self, height):
        '''(INTERNAL) Overriding this C{height}.
        '''
        return self.height if height is None else Height(height)

    def height4(self, earth=None, normal=True, LatLon=None, **LatLon_kwds):
        '''Compute the projection of this point on and the height above or below
           this datum's ellipsoid surface.

           @kwarg earth: A datum, ellipsoid, triaxial ellipsoid or earth radius,
                         I{overriding} this datum (L{Datum}, L{Ellipsoid},
                         L{Ellipsoid2}, L{a_f2Tuple}, L{Triaxial}, L{Triaxial_},
                         L{JacobiConformal} or C{meter}, conventionally).
           @kwarg normal: If C{True}, the projection is the normal to this ellipsoid's
                          surface, otherwise the intersection of the I{radial} line to
                          this ellipsoid's center (C{bool}).
           @kwarg LatLon: Optional class to return the projection, height and datum
                          (C{LatLon}) or C{None}.
           @kwarg LatLon_kwds: Optionally, additional B{C{LatLon}} keyword arguments,
                               ignored if C{B{LatLon} is None}.

           @note: Use keyword argument C{height=0} to override C{B{LatLon}.height}
                  to {0} or any other C{scalar}, conventionally in C{meter}.

           @return: A B{C{LatLon}} instance or if C{B{LatLon} is None}, a L{Vector4Tuple}C{(x,
                    y, z, h)} with the I{projection} C{x}, C{y} and C{z} coordinates and
                    height C{h} in C{meter}, conventionally.

           @raise TriaxialError: No convergence in triaxial root finding.

           @raise TypeError: Invalid B{C{LatLon}}, B{C{LatLon_kwds}} item, B{C{earth}}
                             or triaxial B{C{earth}} couldn't be converted to biaxial
                             B{C{LatLon}} datum.

           @see: Methods L{Ellipsoid.height4} and L{Triaxial_.height4} for more information.
        '''
        c = self.toCartesian()
        if LatLon is None:
            r = c.height4(earth=earth, normal=normal)
        else:
            c = c.height4(earth=earth, normal=normal, Cartesian=c.classof, height=0)
            r = c.toLatLon(LatLon=LatLon, **_xkwds(LatLon_kwds, datum=c.datum, height=c.height))
            if r.datum != c.datum:
                raise _TypeError(earth=earth, datum=r.datum)
        return r

    def heightStr(self, prec=-2, m=_m_):
        '''Return this point's B{C{height}} as C{str}ing.

           @kwarg prec: Number of (decimal) digits, unstripped (C{int}).
           @kwarg m: Optional unit of the height (C{str}).

           @see: Function L{pygeodesy.hstr}.
        '''
        return _MODS.streprs.hstr(self.height, prec=prec, m=m)

    def intersecant2(self, *args, **kwds):  # PYCHOK no cover
        '''B{Not implemented}, throws a C{NotImplementedError} always.'''
        self._notImplemented(*args, **kwds)

    def _intersecend2(self, p, q, wrap, height, g_or_r, P, Q, unused):  # in .LatLonEllipsoidalBaseDI.intersecant2
        '''(INTERNAL) Interpolate 2 heights along a geodesic or rhumb
           line and return the 2 intersecant points accordingly.
        '''
        if height is None:
            hp = hq = _xattr(p, height=INT0)
            h = _xattr(q, height=hp)  # if isLatLon(q) else hp
            if h != hp:
                s = g_or_r._Inverse(p, q, wrap).s12
                if s:  # fmath.fidw?
                    s = (h - hp) / s  # slope
                    hq += s * Q.s12
                    hp += s * P.s12
                else:
                    hp = hq = _MODS.fmath.favg(hp, h)
        else:
            hp = hq = Height(height)

#       n = self.name or typename(unused)
        p = q = self.classof(P.lat2, P.lon2, datum=g_or_r.datum, height=hp)  # name=n
        p._iteration = P.iteration
        if P is not Q:
            q = self.classof(Q.lat2, Q.lon2, datum=g_or_r.datum, height=hq)  # name=n
            q._iteration = Q.iteration
        return p, q

    @deprecated_method
    def isantipode(self, other, eps=EPS):  # PYCHOK no cover
        '''DEPRECATED, use method L{isantipodeTo}.'''
        return self.isantipodeTo(other, eps=eps)

    def isantipodeTo(self, other, eps=EPS):
        '''Check whether this and an other point are antipodal, on diametrically
           opposite sides of the earth.

           @arg other: The other point (C{LatLon}).
           @kwarg eps: Tolerance for near-equality (C{degrees}).

           @return: C{True} if points are antipodal within the given tolerance,
                    C{False} otherwise.
        '''
        p = self.others(other)
        return _formy.isantipode(*(self.latlon + p.latlon), eps=eps)

    @Property_RO
    def isEllipsoidal(self):
        '''Check whether this point is ellipsoidal (C{bool} or C{None} if unknown).
        '''
        return _xattr(self.datum, isEllipsoidal=None)

    def isequalTo(self, other, eps=None):
        '''Compare this point with an other point, I{ignoring} height.

           @arg other: The other point (C{LatLon}).
           @kwarg eps: Tolerance for equality (C{degrees}).

           @return: C{True} if both points are identical, I{ignoring} height,
                    C{False} otherwise.

           @raise TypeError: The B{C{other}} point is not C{LatLon} or mismatch
                             of the B{C{other}} and this C{class} or C{type}.

           @raise UnitError: Invalid B{C{eps}}.

           @see: Method L{isequalTo3}.
        '''
        return _formy._isequalTo(self, self.others(other), eps=eps)

    def isequalTo3(self, other, eps=None):
        '''Compare this point with an other point, I{including} height.

           @arg other: The other point (C{LatLon}).
           @kwarg eps: Tolerance for equality (C{degrees}).

           @return: C{True} if both points are identical I{including} height,
                    C{False} otherwise.

           @raise TypeError: The B{C{other}} point is not C{LatLon} or mismatch
                             of the B{C{other}} and this C{class} or C{type}.

           @see: Method L{isequalTo}.
        '''
        return self.height == self.others(other).height and \
               _formy._isequalTo(self, other, eps=eps)

    @Property_RO
    def isnormal(self):
        '''Return C{True} if this point is normal (C{bool}),
           meaning C{abs(lat) <= 90} and C{abs(lon) <= 180}.

           @see: Methods L{normal}, L{toNormal} and functions L{isnormal
                 <pygeodesy.isnormal>} and L{normal<pygeodesy.normal>}.
        '''
        return _formy.isnormal(self.lat, self.lon, eps=0)

    @Property_RO
    def isSpherical(self):
        '''Check whether this point is spherical (C{bool} or C{None} if unknown).
        '''
        return _xattr(self.datum, isSpherical=None)

    @Property_RO
    def lam(self):
        '''Get the longitude (B{C{radians}}).
        '''
        return radians(self.lon)

    @Property
    def lat(self):
        '''Get the latitude (C{degrees90}).
        '''
        return self._lat

    @lat.setter  # PYCHOK setter!
    def lat(self, lat):
        '''Set the latitude (C{str[N|S]} or C{degrees}).

           @raise ValueError: Invalid B{C{lat}}.
        '''
        lat = Lat(lat)  # parseDMS(lat, suffix=_NS_, clip=90)
        if self._lat != lat:
            _update_all(self)
            self._lat = lat

    @Property
    def latlon(self):
        '''Get the lat- and longitude (L{LatLon2Tuple}C{(lat, lon)}).
        '''
        return LatLon2Tuple(self._lat, self._lon, name=self.name)

    @latlon.setter  # PYCHOK setter!
    def latlon(self, latlonh):
        '''Set the lat- and longitude and optionally the height (2- or 3-tuple
           or comma- or space-separated C{str} of C{degrees90}, C{degrees180}
           and C{meter}).

           @raise TypeError: Height of B{C{latlonh}} not C{scalar} or B{C{latlonh}}
                             not C{list} or C{tuple}.

           @raise ValueError: Invalid B{C{latlonh}} or M{len(latlonh)}.

           @see: Function L{pygeodesy.parse3llh} to parse a B{C{latlonh}} string
                 into a 3-tuple C{(lat, lon, h)}.
        '''
        if isstr(latlonh):
            latlonh = parse3llh(latlonh, height=self.height)
        else:
            _xinstanceof(list, tuple, latlonh=latlonh)
        if len(latlonh) == 3:
            h = Height(latlonh[2], name=Fmt.SQUARE(latlonh=2))
        elif len(latlonh) != 2:
            raise _ValueError(latlonh=latlonh)
        else:
            h = self.height

        llh = Lat(latlonh[0]), Lon(latlonh[1]), h  # parseDMS2(latlonh[0], latlonh[1])
        if (self._lat, self._lon, self._height) != llh:
            _update_all(self)
            self._lat, self._lon, self._height   = llh

    def latlon2(self, ndigits=0):
        '''Return this point's lat- and longitude in C{degrees}, rounded.

           @kwarg ndigits: Number of (decimal) digits (C{int}).

           @return: A L{LatLon2Tuple}C{(lat, lon)}, both C{float} and rounded
                    away from zero.

           @note: The C{round}ed values are always C{float}, also if B{C{ndigits}}
                  is omitted.
        '''
        return LatLon2Tuple(round(self.lat, ndigits),
                            round(self.lon, ndigits), name=self.name)

    @deprecated_method
    def latlon_(self, ndigits=0):  # PYCHOK no cover
        '''DEPRECATED, use method L{latlon2}.'''
        return self.latlon2(ndigits=ndigits)

    latlon2round = latlon_  # PYCHOK no cover

    @Property
    def latlonheight(self):
        '''Get the lat-, longitude and height (L{LatLon3Tuple}C{(lat, lon, height)}).
        '''
        return self.latlon.to3Tuple(self.height)

    @latlonheight.setter  # PYCHOK setter!
    def latlonheight(self, latlonh):
        '''Set the lat- and longitude and optionally the height
           (2- or 3-tuple or comma- or space-separated C{str} of
           C{degrees90}, C{degrees180} and C{meter}).

           @see: Property L{latlon} for more details.
        '''
        self.latlon = latlonh

    @Property
    def lon(self):
        '''Get the longitude (C{degrees180}).
        '''
        return self._lon

    @lon.setter  # PYCHOK setter!
    def lon(self, lon):
        '''Set the longitude (C{str[E|W]} or C{degrees}).

           @raise ValueError: Invalid B{C{lon}}.
        '''
        lon = Lon(lon)  # parseDMS(lon, suffix=_EW_, clip=180)
        if self._lon != lon:
            _update_all(self)
            self._lon = lon

#   _ltp = _EcefLocal._ltp(self)

    def nearestOn6(self, points, closed=False, height=None, wrap=False):
        '''Locate the point on a path or polygon closest to this point.

           Points are converted to and distances are computed in I{geocentric},
           cartesian space.

           @arg points: The path or polygon points (C{LatLon}[]).
           @kwarg closed: Optionally, close the polygon (C{bool}).
           @kwarg height: Optional height, overriding the height of this and all
                          other points (C{meter}).  If C{None}, take the height
                          of points into account for distances.
           @kwarg wrap: If C{True}, wrap or I{normalize} and unroll the B{C{points}}
                        (C{bool}).

           @return: A L{NearestOn6Tuple}C{(closest, distance, fi, j, start, end)}
                    with the C{closest}, the C{start} and the C{end} point each an
                    instance of this C{LatLon} and C{distance} in C{meter}, same
                    units as the cartesian axes.

           @raise PointsError: Insufficient number of B{C{points}}.

           @raise TypeError: Some B{C{points}} or some B{C{points}}' C{Ecef} invalid.

           @raise ValueError: Some B{C{points}}' C{Ecef} is incompatible.

           @see: Function L{nearestOn6<pygeodesy.nearestOn6>}.
        '''
        def _cs(Ps, h, w, C):
            p = None  # not used
            for i, q in Ps.enumerate():
                if w and i:
                    q = _unrollon(p, q)
                yield C(height=h, i=i, up=3, points=q)
                p = q

        C  = self._toCartesianEcef  # to verify datum and Ecef
        Ps = self.PointsIter(points, wrap=wrap)

        c =  C(height=height, this=self)  # this Cartesian
        t = _MODS.vector3d.nearestOn6(c, _cs(Ps, height, wrap, C), closed=closed)
        c, s, e = t.closest, t.start, t.end

        kwds = _xkwds_not(None, LatLon=self.classof,  # this LatLon
                                height=height)
        _r =  self.Ecef(self.datum).reverse
        p  = _r(c).toLatLon(**kwds)
        s  = _r(s).toLatLon(**kwds) if s is not c else p
        e  = _r(e).toLatLon(**kwds) if e is not c else p
        return t.dup(closest=p, start=s, end=e)

    def nearestTo(self, *args, **kwds):  # PYCHOK no cover
        '''B{Not implemented}, throws a C{NotImplementedError} always.'''
        self._notImplemented(*args, **kwds)

    def normal(self):
        '''Normalize this point I{in-place} to C{abs(lat) <= 90} and C{abs(lon) <= 180}.

           @return: C{True} if this point was I{normal}, C{False} if it wasn't (but is now).

           @see: Property L{isnormal} and method L{toNormal}.
        '''
        n = self.isnormal
        if not n:
            self.latlon = _formy.normal(*self.latlon)
        return n

    @property_RO
    def _N_vector(self):
        '''(INTERNAL) Get the C{Nvector} (C{nvectorBase._N_vector_})
        '''
        _N = _MODS.nvectorBase._N_vector_
        return _N(*self._n_xyz3, h=self.height, name=self.name)

    @Property_RO
    def _n_xyz3(self):
        '''(INTERNAL)  Get the n-vector components as L{Vector3Tuple}.
        '''
        return philam2n_xyz(self.phi, self.lam, name=self.name)

    @Property_RO
    def phi(self):
        '''Get the latitude (B{C{radians}}).
        '''
        return radians(self.lat)

    @Property_RO
    def philam(self):
        '''Get the lat- and longitude (L{PhiLam2Tuple}C{(phi, lam)}).
        '''
        return PhiLam2Tuple(self.phi, self.lam, name=self.name)

    def philam2(self, ndigits=0):
        '''Return this point's lat- and longitude in C{radians}, rounded.

           @kwarg ndigits: Number of (decimal) digits (C{int}).

           @return: A L{PhiLam2Tuple}C{(phi, lam)}, both C{float} and rounded
                    away from zero.

           @note: The C{round}ed values are C{float}, always.
        '''
        return PhiLam2Tuple(round(self.phi, ndigits),
                            round(self.lam, ndigits), name=self.name)

    @Property_RO
    def philamheight(self):
        '''Get the lat-, longitude in C{radians} and height (L{PhiLam3Tuple}C{(phi, lam, height)}).
        '''
        return self.philam.to3Tuple(self.height)

    @deprecated_method
    def points(self, points, **closed):  # PYCHOK no cover
        '''DEPRECATED, use method L{points2}.'''
        return self.points2(points, **closed)

    def points2(self, points, closed=True):
        '''Check a path or polygon represented by points.

           @arg points: The path or polygon points (C{LatLon}[])
           @kwarg closed: Optionally, consider the polygon closed, ignoring any
                          duplicate or closing final B{C{points}} (C{bool}).

           @return: A L{Points2Tuple}C{(number, points)}, an C{int} and a C{list}
                    or C{tuple}.

           @raise PointsError: Insufficient number of B{C{points}}.

           @raise TypeError: Some B{C{points}} are not C{LatLon}.
        '''
        return _MODS.iters.points2(points, closed=closed, base=self)

    def PointsIter(self, points, loop=0, dedup=False, wrap=False):
        '''Return a C{PointsIter} iterator.

           @arg points: The path or polygon points (C{LatLon}[])
           @kwarg loop: Number of loop-back points (non-negative C{int}).
           @kwarg dedup: If C{True}, skip duplicate points (C{bool}).
           @kwarg wrap: If C{True}, wrap or I{normalize} the enum-/iterated
                        B{C{points}} (C{bool}).

           @return: A new C{PointsIter} iterator.

           @raise PointsError: Insufficient number of B{C{points}}.
        '''
        return _MODS.iters.PointsIter(points, base=self, loop=loop,
                                             dedup=dedup, wrap=wrap)

    def radii11(self, point2, point3, wrap=False):
        '''Return the radii of the C{Circum-}, C{In-}, I{Soddy} and C{Tangent}
           circles of a (planar) triangle formed by this and two other points.

           @arg point2: Second point (C{LatLon}).
           @arg point3: Third point (C{LatLon}).
           @kwarg wrap: If C{True}, wrap or I{normalize} B{C{point2}} and
                        B{C{point3}} (C{bool}).

           @return: L{Radii11Tuple}C{(rA, rB, rC, cR, rIn, riS, roS, a, b, c, s)}.

           @raise IntersectionError: Near-coincident or -colinear points.

           @raise TypeError: Invalid B{C{point2}} or B{C{point3}}.

           @see: Function L{pygeodesy.radii11}, U{Incircle
                 <https://MathWorld.Wolfram.com/Incircle.html>}, U{Soddy Circles
                 <https://MathWorld.Wolfram.com/SoddyCircles.html>} and U{Tangent
                 Circles<https://MathWorld.Wolfram.com/TangentCircles.html>}.
        '''
        with _toCartesian3(self, point2, point3, wrap) as cs:
            return _MODS.vector2d._radii11ABC4(*cs, useZ=True)[0]

    def _rhumb3(self, exact, radius):  # != .sphericalBase._rhumbs3
        '''(INTERNAL) Get the C{rhumb} for this point's datum or for
           the B{C{radius}}' earth model iff non-C{None}.
        '''
        try:
            d = self._rhumb3dict
            t = d[(exact, radius)]
        except KeyError:
            D = self.datum if radius is None else \
               _spherical_datum(radius)  # ellipsoidal OK
            try:
                r = D.ellipsoid.rhumb_(exact=exact)  # or D.isSpherical
            except AttributeError as x:
                raise _AttributeError(datum=D, radius=radius, cause=x)
            t = r, D, _MODS.karney.Caps
            if len(d) > 2:
                d.clear()  # d[:] = {}
            d[(exact, radius)] = t  # cache 3-tuple
        return t

    @Property_RO
    def _rhumb3dict(self):  # in ._update
        return {}  # 3-item cache

    def rhumbAzimuthTo(self, other, exact=False, radius=None, wrap=False, b360=False):
        '''Return the azimuth (bearing) of a rhumb line (loxodrome) between this and
           an other (ellipsoidal) point.

           @arg other: The other point (C{LatLon}).
           @kwarg exact: Exact C{Rhumb...} to use (C{bool} or C{Rhumb...}), see method
                         L{Ellipsoid.rhumb_}.
           @kwarg radius: Optional earth radius (C{meter}) or earth model (L{Datum}, L{Ellipsoid},
                          L{Ellipsoid2} or L{a_f2Tuple}), overriding this point's datum.
           @kwarg wrap: If C{True}, wrap or I{normalize} and unroll the B{C{other}} point (C{bool}).
           @kwarg b360: If C{True}, return the azimuth as bearing in compass degrees (C{bool}).

           @return: Rhumb azimuth (C{degrees180} or compass C{degrees360}).

           @raise TypeError: The B{C{other}} point is incompatible or B{C{radius}} is invalid.
        '''
        r, _, Cs = self._rhumb3(exact, radius)
        z = r._Inverse(self, other, wrap, outmask=Cs.AZIMUTH).azi12
        return _umod_360(z + _360_0) if b360 else z

    def rhumbDestination(self, distance, azimuth, radius=None, height=None, exact=False, **name):
        '''Return the destination point having travelled the given distance from this point along
           a rhumb line (loxodrome) of the given azimuth.

           @arg distance: Distance travelled (C{meter}, same units as this point's datum (ellipsoid)
                          axes or B{C{radius}}, may be negative.
           @arg azimuth: Azimuth (bearing) of the rhumb line (compass C{degrees}).
           @kwarg radius: Optional earth radius (C{meter}) or earth model (L{Datum}, L{Ellipsoid},
                          L{Ellipsoid2} or L{a_f2Tuple}), overriding this point's datum.
           @kwarg height: Optional height, overriding the default height (C{meter}).
           @kwarg exact: Exact C{Rhumb...} to use (C{bool} or C{Rhumb...}), see method L{Ellipsoid.rhumb_}.
           @kwarg name: Optional C{B{name}=NN} (C{str}).

           @return: The destination point (ellipsoidal C{LatLon}).

           @raise TypeError: Invalid B{C{radius}}.

           @raise ValueError: Invalid B{C{distance}}, B{C{azimuth}}, B{C{radius}} or B{C{height}}.
        '''
        r, D, _ = self._rhumb3(exact, radius)
        d = r._Direct(self, azimuth, distance)
        h = self._heigHt(height)
        return self.classof(d.lat2, d.lon2, datum=D, height=h, **name)

    def rhumbDistanceTo(self, other, exact=False, radius=None, wrap=False):
        '''Return the distance from this to an other point along a rhumb line (loxodrome).

           @arg other: The other point (C{LatLon}).
           @kwarg exact: Exact C{Rhumb...} to use (C{bool} or C{Rhumb...}), see  method L{Ellipsoid.rhumb_}.
           @kwarg radius: Optional earth radius (C{meter}) or earth model (L{Datum}, L{Ellipsoid},
                          L{Ellipsoid2} or L{a_f2Tuple}), overriding this point's datum.
           @kwarg wrap: If C{True}, wrap or I{normalize} and unroll the B{C{other}} point (C{bool}).

           @return: Distance (C{meter}, the same units as this point's datum (ellipsoid) axes or B{C{radius}}.

           @raise TypeError: The B{C{other}} point is incompatible or B{C{radius}} is invalid.

           @raise ValueError: Invalid B{C{radius}}.
        '''
        r, _, Cs = self._rhumb3(exact, radius)
        return r._Inverse(self, other, wrap, outmask=Cs.DISTANCE).s12

    def rhumbIntersecant2(self, circle, point, other, height=None,
                                                    **exact_radius_wrap_eps_tol):
        '''Compute the intersections of a circle and a rhumb line given as two points or as a
           point and azimuth.

           @arg circle: Radius of the circle centered at this location (C{meter}), or a point
                        on the circle (same C{LatLon} class).
           @arg point: The start point of the rhumb line (same C{LatLon} class).
           @arg other: An other point I{on} (same C{LatLon} class) or the azimuth I{of} (compass
                       C{degrees}) the rhumb line.
           @kwarg height: Optional height for the intersection points (C{meter}, conventionally)
                          or C{None} for interpolated heights.
           @kwarg exact_radius_wrap_eps_tol: Optional keyword arguments, see methods L{rhumbLine}
                        and L{RhumbLineAux.Intersecant2} or L{RhumbLine.Intersecant2}.

           @return: 2-Tuple of the intersection points (representing a chord), each an instance of
                    this class.  Both points are the same instance if the rhumb line is tangent to
                    the circle.

           @raise IntersectionError: The circle and rhumb line do not intersect.

           @raise TypeError: Invalid B{C{point}}, B{C{circle}} or B{C{other}}.

           @raise ValueError: Invalid B{C{circle}}, B{C{other}}, B{C{height}} or B{C{exact_radius_wrap}}.

           @see: Methods L{RhumbLineAux.Intersecant2} and L{RhumbLine.Intersecant2}.
        '''
        def _kwds3(eps=EPS, tol=_TOL, wrap=False, **kwds):
            return kwds, wrap, dict(eps=eps, tol=tol)

        exact_radius, w, eps_tol = _kwds3(**exact_radius_wrap_eps_tol)

        p = _unrollon(self, self.others(point=point), wrap=w)
        try:
            r = Radius_(circle=circle) if _isRadius(circle) else \
                self.rhumbDistanceTo(self.others(circle=circle), wrap=w, **exact_radius)
            rl = p.rhumbLine(other, wrap=w, **exact_radius)
            P, Q = rl.Intersecant2(self.lat, self.lon, r, **eps_tol)

            return self._intersecend2(p, other, w, height, rl.rhumb, P, Q,
                                                           self.rhumbIntersecant2)
        except (TypeError, ValueError) as x:
            raise _xError(x, center=self, circle=circle, point=point, other=other,
                                                       **exact_radius_wrap_eps_tol)

    def rhumbLine(self, other, exact=False, radius=None, wrap=False, **name_caps):
        '''Get a rhumb line through this point at a given azimuth or through this and an other point.

           @arg other: The azimuth I{of} (compass C{degrees}) or an other point I{on} (same
                       C{LatLon} class) the rhumb line.
           @kwarg exact: Exact C{Rhumb...} to use (C{bool} or C{Rhumb...}), see method L{Ellipsoid.rhumb_}.
           @kwarg radius: Optional earth radius (C{meter}) or earth model (L{Datum}, L{Ellipsoid},
                          L{Ellipsoid2} or L{a_f2Tuple}), overriding this point's C{datum}.
           @kwarg wrap: If C{True}, wrap or I{normalize} and unroll the B{C{other}} point (C{bool}).
           @kwarg name_caps: Optional C{B{name}=str} and C{caps}, see L{RhumbLine} or L{RhumbLineAux} C{B{caps}}.

           @return: A C{RhumbLine} instance (C{RhumbLine} or C{RhumbLineAux}).

           @raise TypeError: Invalid B{C{radius}} or B{C{other}} not C{scalar} nor same C{LatLon} class.

           @see: Modules L{rhumb.aux_} and L{rhumb.ekx}.
        '''
        r, _, Cs = self._rhumb3(exact, radius)
        kwds = _xkwds(name_caps, name=self.name, caps=Cs.LINE_OFF)
        rl = r._DirectLine( self, other, **kwds) if _isDegrees(other) else \
             r._InverseLine(self, self.others(other), wrap, **kwds)
        return rl

    def rhumbMidpointTo(self, other, exact=False, radius=None, height=None, fraction=_0_5, **wrap_name):
        '''Return the (loxodromic) midpoint on the rhumb line between this and an other point.

           @arg other: The other point (same C{LatLon} class).
           @kwarg exact: Exact C{Rhumb...} to use (C{bool} or C{Rhumb...}), see method L{Ellipsoid.rhumb_}.
           @kwarg radius: Optional earth radius (C{meter}) or earth model (L{Datum}, L{Ellipsoid},
                          L{Ellipsoid2} or L{a_f2Tuple}), overriding this point's datum.
           @kwarg height: Optional height, overriding the mean height (C{meter}).
           @kwarg fraction: Midpoint location from this point (C{scalar}), 0 for this, 1 for the B{C{other}},
                            0.5 for halfway between this and the B{C{other}} point, may be negative or
                            greater than 1.
           @kwarg wrap_name: Optional C{B{name}=NN} (C{str}) and C{B{wrap}=False}, if C{True}, wrap or
                       I{normalize} and unroll the B{C{other}} point (C{bool}).

           @return: The midpoint at the given B{C{fraction}} along the rhumb line (same C{LatLon} class).

           @raise TypeError: The B{C{other}} point is incompatible or B{C{radius}} is invalid.

           @raise ValueError: Invalid B{C{height}} or B{C{fraction}}.
        '''
        w, n    = self._wrap_name2(**wrap_name)
        r, D, _ = self._rhumb3(exact, radius)
        f = Scalar(fraction=fraction)
        d = r._Inverse(self, self.others(other), w)  # C.AZIMUTH_DISTANCE
        d = r._Direct( self, d.azi12, d.s12 * f)
        h = self._havg(other, f=f, h=height)
        return self.classof(d.lat2, d.lon2, datum=D, height=h, name=n)

    @property_RO
    def sphericalLatLon(self):
        '''Get the C{LatLon type} iff spherical, overloaded in L{LatLonSphericalBase}.
        '''
        return False

    def thomasTo(self, other, **wrap):
        '''Compute the distance between this and an other point using U{Thomas'
           <https://apps.DTIC.mil/dtic/tr/fulltext/u2/703541.pdf>} formula.

           @arg other: The other point (C{LatLon}).
           @kwarg wrap: Optional keyword argument C{B{wrap}=False}, if C{True}, wrap
                        or I{normalize} and unroll the B{C{other}} point (C{bool}).

           @return: Distance (C{meter}, same units as the axes of this point's datum ellipsoid).

           @raise TypeError: The B{C{other}} point is not C{LatLon}.

           @see: Function L{pygeodesy.thomas} and methods L{cosineLawTo}, C{distanceTo*},
                 L{equirectangularTo}, L{euclideanTo}, L{flatLocalTo} / L{hubenyTo},
                 L{flatPolarTo}, L{haversineTo} and L{vincentysTo}.
        '''
        return self._distanceTo_(_formy.thomas_, other, **wrap)

    @deprecated_method
    def to2ab(self):  # PYCHOK no cover
        '''DEPRECATED, use property L{philam}.'''
        return self.philam

    def toCartesian(self, height=None, Cartesian=None, **Cartesian_kwds):
        '''Convert this point to cartesian, I{geocentric} coordinates, also known as
           I{Earth-Centered, Earth-Fixed} (ECEF).

           @kwarg height: Optional height, overriding this point's height (C{meter},
                          conventionally).
           @kwarg Cartesian: Optional class to return the geocentric coordinates
                             (C{Cartesian}) or C{None}.
           @kwarg Cartesian_kwds: Optionally, additional B{C{Cartesian}} keyword
                                  arguments, ignored if C{B{Cartesian} is None}.

           @return: A B{C{Cartesian}} instance or if B{C{Cartesian} is None}, an
                    L{Ecef9Tuple}C{(x, y, z, lat, lon, height, C, M, datum)} with
                    C{C=0} and C{M} if available.

           @raise TypeError: Invalid B{C{Cartesian}} or B{C{Cartesian_kwds}} item.

           @see: Methods C{toNvector}, C{toVector} and C{toVector3d}.
        '''
        r = self._ecef9 if height is None else self.toEcef(height=height)
        if Cartesian is not None:  # class or .classof
            r = Cartesian(r, **self._name1__(Cartesian_kwds))
        _xdatum(r.datum, self.datum)
        return r

    def _toCartesianEcef(self, height=None, i=None, up=2, **name_point):
        '''(INTERNAL) Convert to cartesian and check Ecef's before and after.
        '''
        p = self.others(up=up, **name_point)
        c = p.toCartesian(height=height)
        E = self.Ecef
        if E:
            for p in (p, c):
                e = _xattr(p, Ecef=None)
                if not _isin(e, None, E):  # PYCHOK no cover
                    n, _ = _xkwds_item2(name_point)
                    n =  Fmt.INDEX(n, i)
                    t = _incompatible(typename(E))
                    raise _ValueError(n, e, txt=t)  # txt__
        return c

    def toDatum(self, datum2, height=None, **name):
        '''I{Must be overloaded}.'''
        self._notOverloaded(datum2, height=height, **name)

    def toEcef(self, height=None, M=False):
        '''Convert this point to I{geocentric} coordinates, also known as
           I{Earth-Centered, Earth-Fixed} (U{ECEF<https://WikiPedia.org/wiki/ECEF>}).

           @kwarg height: Optional height, overriding this point's height (C{meter},
                          conventionally).
           @kwarg M: Optionally, include the rotation L{EcefMatrix} (C{bool}).

           @return: An L{Ecef9Tuple}C{(x, y, z, lat, lon, height, C, M, datum)} with
                    C{C=0} and C{M} if available.

           @raise EcefError: A C{.datum} or an ECEF issue.
        '''
        return self._ecef9 if _isin(height, None, self.height) else \
               self._Ecef_forward(self.lat, self.lon, height=height, M=M)

    @deprecated_method
    def to3llh(self, height=None):  # PYCHOK no cover
        '''DEPRECATED, use property L{latlonheight} or C{latlon.to3Tuple(B{height})}.'''
        return self.latlonheight if _isin(height, None, self.height) else \
               self.latlon.to3Tuple(height)

    def toNormal(self, deep=False, **name):
        '''Get this point I{normalized} to C{abs(lat) <= 90} and C{abs(lon) <= 180}.

           @kwarg deep: If C{True}, make a deep, otherwise a shallow copy (C{bool}).
           @kwarg name: Optional C{B{name}=NN} (C{str}).

           @return: A copy of this point, I{normalized} (C{LatLon}), optionally renamed.

           @see: Property L{isnormal}, method L{normal} and function L{pygeodesy.normal}.
        '''
        ll = self.copy(deep=deep)
        _  = ll.normal()
        if name:
            ll.rename(name)
        return ll

    def toNvector(self, h=None, Nvector=None, **name_Nvector_kwds):
        '''Convert this point to C{n-vector} (normal to the earth's surface) components,
           I{including height}.

           @kwarg h: Optional height, overriding this point's height (C{meter}).
           @kwarg Nvector: Optional class to return the C{n-vector} components (C{Nvector})
                           or C{None}.
           @kwarg name_Nvector_kwds: Optional C{B{name}=NN} (C{str}) and optionally,
                       additional B{C{Nvector}} keyword arguments, ignored if C{B{Nvector}
                       is None}.

           @return: An B{C{Nvector}} instance or a L{Vector4Tuple}C{(x, y, z, h)} if
                    C{B{Nvector} is None}.

           @raise TypeError: Invalid B{C{h}}, B{C{Nvector}} or B{C{name_Nvector_kwds}}.

           @see: Methods C{toCartesian}, C{toVector} and C{toVector3d}.
        '''
        h = self._heigHt(h)
        if Nvector is None:
            r = self._n_xyz3.to4Tuple(h)
            n, _ = _name2__(name_Nvector_kwds, _or_nameof=self)
            if n:
                r.rename(n)
        else:
            x, y, z = self._n_xyz3
            r = Nvector(x, y, z, h=h, ll=self, **self._name1__(name_Nvector_kwds))
        return r

    def toStr(self, form=F_DMS, joined=_COMMASPACE_, m=_m_, **prec_sep_s_D_M_S):  # PYCHOK expected
        '''Convert this point to a "lat, lon[, +/-height]" string, formatted in the
           given C{B{form}at}.

           @kwarg form: The lat-/longitude C{B{form}at} to use (C{str}), see functions
                        L{pygeodesy.latDMS} or L{pygeodesy.lonDMS}.
           @kwarg joined: Separator to join the lat-, longitude and height strings (C{str}
                          or C{None} or C{NN} for non-joined).
           @kwarg m: Optional unit of the height (C{str}), use C{None} to exclude height
                     from the returned string.
           @kwarg prec_sep_s_D_M_S: Optional C{B{prec}ision}, C{B{sep}arator}, B{C{s_D}},
                       B{C{s_M}}, B{C{s_S}} and B{C{s_DMS}} keyword arguments, see function
                       L{pygeodesy.toDMS} for details.

           @return: This point in the specified C{B{form}at}, etc. (C{str} or a 2- or 3-tuple
                    C{(lat_str, lon_str[, height_str])} if B{C{joined}} is C{NN} or C{None}).

           @see: Function L{pygeodesy.latDMS} or L{pygeodesy.lonDMS} for more details about
                 keyword arguments C{B{form}at}, C{B{prec}ision}, C{B{sep}arator}, B{C{s_D}},
                 B{C{s_M}}, B{C{s_S}} and B{C{s_DMS}}.
        '''
        t = (latDMS(self.lat, form=form, **prec_sep_s_D_M_S),
             lonDMS(self.lon, form=form, **prec_sep_s_D_M_S))
        if self.height and m is not None:
            t += (self.heightStr(m=m),)
        return joined.join(t) if joined else t

    def toVector(self, Vector=None, **Vector_kwds):
        '''Convert this point to a C{Vector} with the I{geocentric} C{(x, y, z)} (ECEF)
           coordinates, I{ignoring height}.

           @kwarg Vector: Optional class to return the I{geocentric} components (L{Vector3d})
                          or C{None}.
           @kwarg Vector_kwds: Optionally, additional B{C{Vector}} keyword arguments,
                         ignored if C{B{Vector} is None}.

           @return: A B{C{Vector}} instance or a L{Vector3Tuple}C{(x, y, z)} if C{B{Vector}
                    is None}.

           @raise TypeError: Invalid B{C{Vector}} or B{C{Vector_kwds}}.

           @see: Methods C{toCartesian}, C{toNvector} and C{toVector3d}.
        '''
        return self._ecef9.toVector(Vector=Vector, **self._name1__(Vector_kwds))

    def toVector3d(self, norm=True, **Vector3d_kwds):
        '''Convert this point to a L{Vector3d} with the I{geocentric} C{(x, y, z)}
           (ECEF) coordinates, I{ignoring height}.

           @kwarg norm: If C{False}, don't normalize the coordinates (C{bool}).
           @kwarg Vector3d_kwds: Optional L{Vector3d} keyword arguments.

           @return: Named, unit vector or vector (L{Vector3d}).

           @raise TypeError: Invalid B{C{Vector3d_kwds}}.

           @see: Methods C{toCartesian}, C{toNvector} and C{toVector}.
        '''
        r = self.toVector(Vector=_MODS.vector3d.Vector3d, **Vector3d_kwds)
        if norm:
            r = r.unit(ll=self)
        return r

    def toWm(self, **toWm_kwds):
        '''Convert this point to a WM coordinate.

           @kwarg toWm_kwds: Optional L{pygeodesy.toWm} keyword arguments.

           @return: The WM coordinate (L{Wm}).

           @see: Function L{pygeodesy.toWm}.
        '''
        return _MODS.webmercator.toWm(self, **self._name1__(toWm_kwds))

    @deprecated_method
    def to3xyz(self):  # PYCHOK no cover
        '''DEPRECATED, use property L{xyz} or method L{toNvector}, L{toVector},
           L{toVector3d} or perhaps (geocentric) L{toEcef}.'''
        return self.xyz  # self.toVector()

#   def _update(self, updated, *attrs, **setters):
#       '''(INTERNAL) See C{_NamedBase._update}.
#       '''
#       if updated:
#           self._rhumb3dict.clear()
#       return _NamedBase._update(self, updated, *attrs, **setters)

    def vincentysTo(self, other, **radius_wrap):
        '''Compute the distance between this and an other point using U{Vincenty's
           <https://WikiPedia.org/wiki/Great-circle_distance>} spherical formula.

           @arg other: The other point (C{LatLon}).
           @kwarg radius_wrap: Optional C{B{radius}=R_M} and C{B{wrap}=False} for
                         function L{pygeodesy.vincentys}, overriding the default
                         C{mean radius} of this point's datum ellipsoid.

           @return: Distance (C{meter}, same units as B{C{radius}}).

           @raise TypeError: The B{C{other}} point is not C{LatLon}.

           @see: Function L{pygeodesy.vincentys} and methods L{cosineLawTo}, C{distanceTo*},
                 L{equirectangularTo}, L{euclideanTo}, L{flatLocalTo} / L{hubenyTo},
                 L{flatPolarTo}, L{haversineTo} and L{thomasTo}.
        '''
        return self._distanceTo(_formy.vincentys, other, **_xkwds(radius_wrap, radius=None))

    def _wrap_name2(self, wrap=False, **name):
        '''(INTERNAL) Return the C{wrap} and C{name} value.
        '''
        return wrap, (self._name__(name) if name else NN)

    @property_RO
    def xyz(self):
        '''Get the I{geocentric} C{(x, y, z)} coordinates (L{Vector3Tuple}C{(x, y, z)})
        '''
        return self._ecef9.xyz

    @property_RO
    def xyz3(self):
        '''Get the I{geocentric} C{(x, y, z)} coordinates as C{3-tuple}.
        '''
        return tuple(self.xyz)

    @Property_RO
    def xyzh(self):
        '''Get the I{geocentric} C{(x, y, z)} coordinates and height (L{Vector4Tuple}C{(x, y, z, h)})
        '''
        return self.xyz.to4Tuple(self.height)


class _toCartesian3(object):  # see also .formy._idllmn6, .geodesicw._wargs, .vector2d._numpy
    '''(INTERNAL) Wrapper to convert 2 other points.
    '''
    @contextmanager  # <https://www.Python.org/dev/peps/pep-0343/> Examples
    def __call__(self, p, p2, p3, wrap, **kwds):
        try:
            if wrap:
                p2, p3 =  map1(_Wrap.point, p2, p3)
                kwds   = _xkwds(kwds, wrap=wrap)
            yield (p. toCartesian().copy(name=_point_),  # copy to rename
                   p._toCartesianEcef(up=4, point2=p2),
                   p._toCartesianEcef(up=4, point3=p3))
        except (AssertionError, TypeError, ValueError) as x:  # Exception?
            raise _xError(x, point=p, point2=p2, point3=p3, **kwds)

_toCartesian3 = _toCartesian3()  # PYCHOK singleton


def _latlonheight3(latlonh, height, wrap):  # in .points.LatLon_.__init__
    '''(INTERNAL) Get 3-tuple C{(lat, lon, height)}.
    '''
    try:
        lat, lon = latlonh.lat, latlonh.lon
        height = _xattr(latlonh, height=height)
    except AttributeError:
        raise _IsnotError(_LatLon_, latlonh=latlonh)
    if wrap:
        lat, lon = _Wrap.latlon(lat, lon)
    return lat, lon, height


def latlon2n_xyz(lat_ll, lon=None, **name):
    '''Convert lat-, longitude to C{n-vector} (I{normal} to the earth's surface) X, Y and Z components.

       @arg lat_ll: Latitude (C{degrees}) or a C{LatLon} instance, L{LatLon2Tuple} or other C{LatLon*Tuple}.
       @kwarg lon: Longitude (C{degrees}), required if C{B{lon_ll} is degrees}, ignored otherwise.
       @kwarg name: Optional C{B{name}=NN} (C{str}).

       @return: A L{Vector3Tuple}C{(x, y, z)}.

       @see: Function L{philam2n_xyz}.

       @note: These are C{n-vector} x, y and z components, I{NOT geocentric} x, y and z (ECEF) coordinates!
    '''
    lat = lat_ll
    if lon is None:
        try:
            lat, lon = lat_ll.latlon
        except AttributeError:
            lat = lat_ll.lat
            lon = lat_ll.lon
    # Kenneth Gade eqn 3, but using right-handed
    # vector x -> 0°E,0°N, y -> 90°E,0°N, z -> 90°N
    sa, ca, sb, cb = sincos2d_(lat, lon)
    return Vector3Tuple(ca * cb, ca * sb, sa, **name)


def philam2n_xyz(phi_ll, lam=None, **name):
    '''Convert lat-, longitude to C{n-vector} (I{normal} to the earth's surface) X, Y and Z components.

       @arg phi_ll: Latitude (C{radians}) or a C{LatLon} instance with C{phi}, C{lam} or C{philam} attributes.
       @kwarg lam: Longitude (C{radians}), required if C{B{phi_ll} is radians}, ignored otherwise.
       @kwarg name: Optional name (C{str}).

       @return: A L{Vector3Tuple}C{(x, y, z)}.

       @see: Function L{latlon2n_xyz}.

       @note: These are C{n-vector} x, y and z components, I{NOT geocentric} x, y and z (ECEF) coordinates!
    '''
    phi = phi_ll
    if lam is None:
        try:
            phi, lam = phi_ll.philam
        except AttributeError:
            phi = phi_ll.phi
            lam = phi_ll.lam
    return latlon2n_xyz(degrees(phi), degrees(lam), **name)


def _trilaterate5(p1, d1, p2, d2, p3, d3, area=True, eps=EPS1, radius=R_M, wrap=False):  # MCCABE 13
    '''(INTERNAL) Trilaterate three points by I{area overlap} or by I{perimeter intersection} of three circles.

       @note: The B{C{radius}} is needed only for C{n-vectorial} and C{sphericalTrigonometry.LatLon.distanceTo}
              methods and silently ignored by the C{ellipsoidalExact}, C{-GeodSolve}, C{-Karney} and
              C{-Vincenty.LatLon.distanceTo} methods.
    '''
    p2, p3, w = _unrollon3(p1, p2, p3, wrap)
    rw = dict(radius=radius, wrap=w)

    r1 = Distance_(distance1=d1)
    r2 = Distance_(distance2=d2)
    r3 = Distance_(distance3=d3)
    m  = 0 if area else (r1 + r2 + r3)
    pc = 0
    t  = []
    for _ in range(3):
        try:  # intersection of circle (p1, r1) and (p2, r2)
            c1, c2 = p1.intersections2(r1, p2, r2, wrap=w)

            if area:  # check overlap
                if c1 is c2:  # abutting
                    c = c1
                else:  # nearest point on radical
                    c = p3.nearestOn(c1, c2, within=True, wrap=w)
                d = r3 - p3.distanceTo(c, **rw)
                if d > eps:  # sufficient overlap
                    t.append((d, c))
                m = max(m, d)

            else:  # check intersection
                for c in ((c1,) if c1 is c2 else (c1, c2)):
                    d = fabs(r3 - p3.distanceTo(c, **rw))
                    if d < eps:  # below margin
                        t.append((d, c))
                    m = min(m, d)

        except IntersectionError as x:
            if _concentric_ in str(x):  # XXX ConcentricError?
                pc += 1

        p1, r1, p2, r2, p3, r3 = p2, r2, p3, r3, p1, r1  # rotate

    if t:  # get min, max, points and count ...
        t = tuple(sorted(t))
        n = len(t),  # as 1-tuple
        # ... or for a single trilaterated result,
        # min *is* max, min- *is* maxPoint and n=1, 2 or 3
        return Trilaterate5Tuple(t[0] + t[-1] + n)  # *(t[0] + ...)

    elif area and pc == 3:  # all pairwise concentric ...
        r, p = min((r1, p1), (r2, p2), (r3, p3))
        m = max(r1, r2, r3)
        # ... return "smallest" point twice, the smallest
        # and largest distance and n=0 for concentric
        return Trilaterate5Tuple(float(r), p, float(m), p, 0)

    n, f = (_overlap_, max) if area else (_intersection_, min)
    t = _COMMASPACE_(_no_(n), '%s %.3g' % (typename(f), m))
    raise IntersectionError(area=area, eps=eps, wrap=wrap, txt=t)


__all__ += _ALL_DOCS(LatLonBase)

# **) MIT License
#
# Copyright (C) 2016-2025 -- mrJean1 at Gmail -- All Rights Reserved.
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
