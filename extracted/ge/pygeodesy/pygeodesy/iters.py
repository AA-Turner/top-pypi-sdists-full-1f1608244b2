
# -*- coding: utf-8 -*-

u'''Iterators with options.

Iterator classes L{LatLon2PsxyIter} and L{PointsIter} to iterate
over iterables, lists, sets, tuples, etc. with optional loop-back to
the initial items, skipping of duplicate items and copying of the
iterated items.
'''

from pygeodesy.basics import _isin, islistuple, issubclassof, \
                              len2, map2,  _passarg, typename
# from pygeodesy.constants import _1_0  # from .utily
from pygeodesy.errors import _IndexError, LenError, PointsError, \
                             _TypeError, _ValueError
# from pygeodesy.internals import _passarg, typename  # from .basics
from pygeodesy.interns import _0_, _composite_, _few_, _latlon_, \
                              _points_, _too_
from pygeodesy.lazily import _ALL_DOCS, _ALL_LAZY, _ALL_MODS as _MODS
from pygeodesy.named import _Named, property_RO,  Fmt
from pygeodesy.namedTuples import Point3Tuple, Points2Tuple
# from pygeodesy.props import property_RO  # from .named
# from pygeodesy.streprs import Fmt  # from .named
from pygeodesy.units import Int, Radius
from pygeodesy.utily import degrees2m, _Wrap,  _1_0

__all__ = _ALL_LAZY.iters
__version__ = '25.05.19'

_items_        = 'items'
_iterNumpy2len =  1  # adjustable for testing purposes
_NOTHING       =  object()  # unique


class _BaseIter(_Named):
    '''(INTERNAL) Iterator over items with loop-back and de-duplication.

       @see: Luciano Ramalho, "Fluent Python", O'Reilly, 2016 p. 418+, 2022 p. 600+
    '''
    _closed =  True
    _copies = ()
    _dedup  =  False
    _Error  =  LenError
    _items  =  None
    _len    =  0
    _loop   = ()
    _looped =  False
    _name   = _items_
    _prev   = _NOTHING
    _wrap   =  False

    def __init__(self, items, loop=0, dedup=False, Error=None, **name):
        '''New iterator over an iterable of B{C{items}}.

           @arg items: Iterable (any C{type}, except composites).
           @kwarg loop: Number of loop-back items, also initial enumerate and
                        iterate index (non-negative C{int}).
           @kwarg dedup: Skip duplicate items (C{bool}).
           @kwarg Error: Error to raise (L{LenError}).
           @kwarg name: Optional C{B{name}="items"} (C{str}).

           @raise Error: Invalid B{C{items}} or sufficient number of B{C{items}}.

           @raise TypeError: Composite B{C{items}}.
        '''
        if dedup:
            self._dedup = True
        if issubclassof(Error, Exception):
            self._Error = Error
        if name:
            self.rename(name)

        if islistuple(items):  # range in Python 2
            self._items = items
        elif _MODS.booleans.isBoolean(items):
            raise _TypeError(points=_composite_)
# XXX   if hasattr(items, 'next') or hasattr(items, '__length_hint__'):
# XXX       # handle reversed, iter, etc. items types
        self._iter = iter(items)
        self._indx = -1
        if Int(loop) > 0:
            try:
                self._loop = tuple(self.next for _ in range(loop))
                if self.loop != loop:
                    raise RuntimeError()  # force Error
            except (RuntimeError, StopIteration):
                raise self._Error(self.name, self.loop, txt=_too_(_few_))

    @property_RO
    def copies(self):
        '''Get the saved copies, if any (C{tuple} or C{list}) and only I{once}.
        '''
        cs = self._copies
        if cs:
            self._copies = ()
        return cs

    @property_RO
    def dedup(self):
        '''Get the de-duplication setting (C{bool}).
        '''
        return self._dedup

    def enumerate(self, closed=False, copies=False, dedup=False):
        '''Yield all items, each as a 2-tuple C{(index, item)}.

           @kwarg closed: Loop back to the first B{C{point(s)}}.
           @kwarg copies: Make a copy of all B{C{items}} (C{bool}).
           @kwarg dedup: Set de-duplication in loop-back (C{bool}).
        '''
        for item in self.iterate(closed=closed, copies=copies, dedup=dedup):
            yield self._indx, item

    def __getitem__(self, index):
        '''Get the item(s) at the given B{C{index}} or C{slice}.

           @raise IndexError: Invalid B{C{index}}, beyond B{C{loop}}.
        '''
        t = self._items or self._copies or self._loop
        try:  # Luciano Ramalho, "Fluent Python", O'Reilly, 2016 p. 293+, 2022 p. 408+
            if isinstance(index, slice):
                return t[index.start:index.stop:index.step]
            else:
                return t[index]
        except IndexError as x:
            t = Fmt.SQUARE(self.name, index)
            raise _IndexError(str(x), txt=t, cause=x)

    def __iter__(self):  # PYCHOK no cover
        '''Make this iterator C{iterable}.
        '''
        # Luciano Ramalho, "Fluent Python", O'Reilly, 2016 p. 421, 2022 p. 604+
        return self.iterate()  # XXX or self?

    def iterate(self, closed=False, copies=False, dedup=False):
        '''Yield all items, each as C{item}.

           @kwarg closed: Loop back to the first B{C{point(s)}}.
           @kwarg copies: Make a copy of all B{C{items}} (C{bool}).
           @kwarg dedup: Set de-duplication in loop-back (C{bool}).

           @raise Error: Using C{B{closed}=True} without B{C{loop}}-back.
        '''
        if closed and not self.loop:
            raise self._Error(closed=closed, loop=self.loop)

        if copies:
            if self._items:
                self._copies = self._items
                self._items = _copy = None
            else:
                self._copies = list(self._loop)
                _copy = self._copies.append
        else:  # del B{C{items}} reference
            self._items = _copy = None

        self._closed = closed
        self._looped = False
        if self._iter:
            try:
                _next_ = self.next_
                if _copy:
                    while True:
                        item = _next_(dedup=dedup)
                        _copy(item)
                        yield item
                else:
                    while True:
                        yield _next_(dedup=dedup)
            except StopIteration:
                self._iter = ()  # del self._iter, prevent re-iterate

    def __len__(self):
        '''Get the number of items seen so far.
        '''
        return self._len

    @property_RO
    def loop(self):
        '''Get the B{C{loop}} setting (C{int}), C{0} for non-loop-back.
        '''
        return len(self._loop)

    @property_RO
    def looped(self):
        '''In this C{Iter}ator in loop-back? (C{bool}).
        '''
        return self._looped

    @property_RO
    def next(self):
        '''Get the next item.
        '''
        return self._next_dedup() if self._dedup else self._next(False)

#   __next__  # NO __next__ AND __iter__ ... see Luciano Ramalho,
#             # "Fluent Python", O'Reilly, 2016 p. 426, 2022 p. 610

    def next_(self, dedup=False):
        '''Return the next item.

           @kwarg dedup: Set de-duplication for loop-back (C{bool}).
        '''
        return self._next_dedup() if self._dedup else self._next(dedup)

    def _next(self, dedup):
        '''Return the next item, regardless.

           @arg dedup: Set de-duplication for loop-back (C{bool}).
        '''
        try:
            self._indx += 1
            self._len   = self._indx  # max(_len, _indx)
            self._prev  = item = next(self._iter)
            return item
        except StopIteration:
            pass
        if self._closed and self._loop:  # loop back
            self._dedup  = bool(dedup or self._dedup)
            self._indx   = 0
            self._iter   = iter(self._loop)
            self._loop   = ()
            self._looped = True
        return next(self._iter)

    def _next_dedup(self):
        '''Return the next item, different from the previous one.
        '''
        prev = self._prev
        item = self._next(True)
        if prev is not _NOTHING:
            while item == prev:
                item = self._next(True)
        return item


class PointsIter(_BaseIter):
    '''Iterator for C{points} with optional loop-back and copies.
    '''
    _base  =  None
    _Error =  PointsError
    _name  = _points_

    def __init__(self, points, loop=0, base=None, dedup=False, wrap=False, **name):
        '''New L{PointsIter} iterator.

           @arg points: C{Iterable} or C{list}, C{sequence}, C{set}, C{tuple},
                        etc. (C{point}s).
           @kwarg loop: Number of loop-back points, also initial C{enumerate} and
                        C{iterate} index (non-negative C{int}).
           @kwarg base: Optional B{C{points}} instance for type checking (C{any}).
           @kwarg dedup: Skip duplicate points (C{bool}).
           @kwarg wrap: If C{True}, wrap or I{normalize} the enum-/iterated
                        B{C{points}} (C{bool}).
           @kwarg name: Optional C{B{name}="points"} (C{str}).

           @raise PointsError: Insufficient number of B{C{points}}.

           @raise TypeError: Some B{C{points}} are not B{C{base}}.
       '''
        _BaseIter.__init__(self, points, loop=loop, dedup=dedup, **name)

        if base and not (isNumpy2(points) or isTuple2(points)):
            self._base = base
        if wrap:
            self._wrap = True

    def enumerate(self, closed=False, copies=False):  # PYCHOK signature
        '''Iterate and yield each point as a 2-tuple C{(index, point)}.

           @kwarg closed: Loop back to the first B{C{point(s)}}, de-dup'ed (C{bool}).
           @kwarg copies: Save a copy of all B{C{points}} (C{bool}).

           @raise PointsError: Insufficient number of B{C{points}} or using
                               C{B{closed}=True} without B{C{loop}}-back.

           @raise TypeError: Some B{C{points}} are not B{C{base}}-compatible.
        '''
        for p in self.iterate(closed=closed, copies=copies):
            yield self._indx, p

    def iterate(self, closed=False, copies=False):  # PYCHOK signature
        '''Iterate through all B{C{points}} starting at index C{loop}.

           @kwarg closed: Loop back to the first B{C{point(s)}}, de-dup'ed (C{bool}).
           @kwarg copies: Save a copy of all B{C{points}} (C{bool}).

           @raise PointsError: Insufficient number of B{C{points}} or using
                               C{B{closed}=True} without B{C{loop}}-back.

           @raise TypeError: Some B{C{points}} are not B{C{base}}-compatible.
        '''
        if self._base:
            _oth =  self._base.others
            _fmt =  Fmt.SQUARE(points=0).replace
        else:
            _oth = _fmt = None

        n  =  self.loop if self._iter else 0
        _p = _Wrap.point if self._wrap else _passarg  # and _Wrap.normal is not None
        for p in _BaseIter.iterate(self, closed=closed, copies=copies, dedup=closed):
            if _oth:
                _oth(p, name=_fmt(_0_, str(self._indx)), up=2)
            yield _p(p)
            n += 1
        if n < (4 if closed else 2):
            raise self._Error(self.name, n, txt=_too_(_few_))


class LatLon2PsxyIter(PointsIter):
    '''Iterate and convert for C{points} with optional loop-back and copies.
    '''
    _deg2m  =  None
    _name   = _latlon_
    _radius =  None  # keep degrees
    _wrap   =  True

    def __init__(self, points, loop=0, base=None, wrap=True, radius=None,
                                                  dedup=False, **name):
        '''New L{LatLon2PsxyIter} iterator.

           @note: The C{LatLon} latitude is considered the I{pseudo-y} and
                  longitude the I{pseudo-x} coordinate, like L{LatLon2psxy}.

           @arg points: C{Iterable} or C{list}, C{sequence}, C{set}, C{tuple},
                        etc. (C{LatLon}[]).
           @kwarg loop: Number of loop-back points, also initial C{enumerate} and
                        C{iterate} index (non-negative C{int}).
           @kwarg base: Optional B{C{points}} instance for type checking (C{any}).
           @kwarg wrap: If C{True}, wrap or I{normalize} the enum-/iterated
                        B{C{points}} (C{bool}).
           @kwarg radius: Mean earth radius (C{meter}) for conversion from
                          C{degrees} to C{meter} (or C{radians} if C{B{radius}=1}).
           @kwarg dedup: Skip duplicate points (C{bool}).
           @kwarg name: Optional C{B{name}="latlon"} (C{str}).

           @raise PointsError: Insufficient number of B{C{points}}.

           @raise TypeError: Some B{C{points}} are not B{C{base}}-compatible.
        '''
        PointsIter.__init__(self, points, loop=loop, base=base, dedup=dedup, **name)
        if not wrap:
            self._wrap = False
        if radius:
            self._radius = r = Radius(radius)
            self._deg2m  = degrees2m(_1_0, r)

    def __getitem__(self, index):
        '''Get the point(s) at the given B{C{index}} or C{slice}.

           @raise IndexError: Invalid B{C{index}}, beyond B{C{loop}}.
        '''
        ll = PointsIter.__getitem__(self, index)
        if isinstance(index, slice):
            return map2(self._point3Tuple, ll)
        else:
            return self._point3Tuple(ll)

    def enumerate(self, closed=False, copies=False):  # PYCHOK signature
        '''Iterate and yield each point as a 2-tuple C{(index, L{Point3Tuple})}.

           @kwarg closed: Loop back to the first B{C{point(s)}}, de-dup'ed (C{bool}).
           @kwarg copies: Save a copy of all B{C{points}} (C{bool}).

           @raise PointsError: Insufficient number of B{C{points}} or using
                               C{B{closed}=True} without B{C{loop}}-back.

           @raise TypeError: Some B{C{points}} are not B{C{base}}-compatible.
        '''
        return PointsIter.enumerate(self, closed=closed, copies=copies)

    def iterate(self, closed=False, copies=False):  # PYCHOK signature
        '''Iterate the B{C{points}} starting at index B{C{loop}} and
           yield each as a L{Point3Tuple}C{(x, y, ll)}.

           @kwarg closed: Loop back to the first B{C{point(s)}}, de-dup'ed (C{bool}).
           @kwarg copies: Save a copy of all B{C{points}} (C{bool}).

           @raise PointsError: Insufficient number of B{C{points}} or using
                               C{B{closed}=True} without B{C{loop}}-back.

           @raise TypeError: Some B{C{points}} are not B{C{base}}-compatible.
        '''
        if not _isin(self._deg2m, None, _1_0):
            _p3 = self._point3Tuple
        else:
            def _p3(ll):  # PYCHOK redef
                return Point3Tuple(ll.lon, ll.lat, ll)

        for ll in PointsIter.iterate(self, closed=closed, copies=copies):
            yield _p3(ll)

    def _point3Tuple(self, ll):
        '''(INTERNAL) Create a L{Point3Tuple} for point B{C{ll}}.
        '''
        x, y = ll.lon, ll.lat  # note, x, y = lon, lat
        d = self._deg2m
        if d:  # convert degrees
            x *= d
            y *= d
        return Point3Tuple(x, y, ll)


def _imdex2(closed, n):  # PYCHOK by .clipy
    '''(INTERNAL) Return first and second index of C{range(B{n})}.
    '''
    return (n-1, 0) if closed else (0, 1)


def isNumpy2(obj):
    '''Check for a B{C{Numpy2LatLon}} points wrapper.

       @arg obj: The object (any C{type}).

       @return: C{True} if B{C{obj}} is a B{C{Numpy2LatLon}}
                instance, C{False} otherwise.
    '''
    # isinstance(self, (Numpy2LatLon, ...))
    return getattr(obj, typename(isNumpy2), False)


def isPoints2(obj):
    '''Check for a B{C{LatLon2psxy}} points wrapper.

       @arg obj: The object (any C{type}).

       @return: C{True} if B{C{obj}} is a B{C{LatLon2psxy}}
                instance, C{False} otherwise.
    '''
    # isinstance(self, (LatLon2psxy, ...))
    return getattr(obj, typename(isPoints2), False)


def isTuple2(obj):
    '''Check for a B{C{Tuple2LatLon}} points wrapper.

       @arg obj: The object (any).

       @return: C{True} if B{C{obj}} is a B{C{Tuple2LatLon}}
                instance, C{False} otherwise.
    '''
    # isinstance(self, (Tuple2LatLon, ...))
    return getattr(obj, typename(isTuple2), False)


def iterNumpy2(obj):
    '''Iterate over Numpy2 wrappers or other sequences exceeding
       the threshold.

       @arg obj: Points array, list, sequence, set, etc. (any).

       @return: C{True} do, C{False} don't iterate.
    '''
    try:
        return isNumpy2(obj) or len(obj) > _iterNumpy2len
    except TypeError:
        return False


def iterNumpy2over(n=None):
    '''Get or set the L{iterNumpy2} threshold.

       @kwarg n: Optional, new threshold (C{int}).

       @return: Previous threshold (C{int}).

       @raise ValueError: Invalid B{C{n}}.
    '''
    global _iterNumpy2len
    p = _iterNumpy2len
    if n is not None:
        try:
            i = int(n)
            if i > 0:
                _iterNumpy2len = i
            else:
                raise ValueError
        except (TypeError, ValueError):
            raise _ValueError(n=n)
    return p


def points2(points, closed=True, base=None, Error=PointsError):
    '''Check a path or polygon represented by points.

       @arg points: The path or polygon points (C{LatLon}[])
       @kwarg closed: Optionally, consider the polygon closed,
                      ignoring any duplicate or closing final
                      B{C{points}} (C{bool}).
       @kwarg base: Optionally, check all B{C{points}} against
                    this base class, if C{None} don't check.
       @kwarg Error: Exception to raise (C{ValueError}).

       @return: A L{Points2Tuple}C{(number, points)} with the number
                of points and the points C{list} or C{tuple}.

       @raise PointsError: Insufficient number of B{C{points}}.

       @raise TypeError: Some B{C{points}} are not B{C{base}}
                         compatible or composite B{C{points}}.
    '''
    if _MODS.booleans.isBoolean(points):
        raise Error(points=points, txt=_composite_)

    n, points = len2(points)

    if closed:
        # remove duplicate or closing final points
        while n > 1 and points[n-1] in (points[0], points[n-2]):
            n -= 1
        # XXX following line is unneeded if points
        # are always indexed as ... i in range(n)
        points = points[:n]  # XXX numpy.array slice is a view!

    if n < (3 if closed else 1):
        raise Error(points=n, txt=_too_(_few_))

    if base and not (isNumpy2(points) or isTuple2(points)):
        for i in range(n):
            base.others(points[i], name=Fmt.SQUARE(points=i))

    return Points2Tuple(n, points)


__all__ += _ALL_DOCS(_BaseIter)

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
