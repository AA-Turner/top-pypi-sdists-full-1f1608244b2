# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _StepVector
else:
    import _StepVector

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class _Pair_long_float(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    first = property(_StepVector._Pair_long_float_first_get, _StepVector._Pair_long_float_first_set)
    second = property(_StepVector._Pair_long_float_second_get, _StepVector._Pair_long_float_second_set)

    def __init__(self, first_, second_):
        _StepVector._Pair_long_float_swiginit(self, _StepVector.new__Pair_long_float(first_, second_))
    __swig_destroy__ = _StepVector.delete__Pair_long_float

# Register _Pair_long_float in _StepVector:
_StepVector._Pair_long_float_swigregister(_Pair_long_float)
class _StepVector_Iterator_float(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, first, last_):
        _StepVector._StepVector_Iterator_float_swiginit(self, _StepVector.new__StepVector_Iterator_float(first, last_))

    def __next__(self):
        return _StepVector._StepVector_Iterator_float___next__(self)

    def __iter__(self):
        return _StepVector._StepVector_Iterator_float___iter__(self)
    __swig_destroy__ = _StepVector.delete__StepVector_Iterator_float

# Register _StepVector_Iterator_float in _StepVector:
_StepVector._StepVector_Iterator_float_swigregister(_StepVector_Iterator_float)
class _StepVector_float(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _StepVector._StepVector_float_swiginit(self, _StepVector.new__StepVector_float())

    def set_value(self, _from, to, value):
        return _StepVector._StepVector_float_set_value(self, _from, to, value)

    def remove_step(self, i):
        return _StepVector._StepVector_float_remove_step(self, i)

    def add_value(self, _from, to, value):
        return _StepVector._StepVector_float_add_value(self, _from, to, value)

    def get_all_values_pystyle(self):
        return _StepVector._StepVector_float_get_all_values_pystyle(self)

    def get_values_pystyle(self, _from):
        return _StepVector._StepVector_float_get_values_pystyle(self, _from)

    def num_values(self):
        return _StepVector._StepVector_float_num_values(self)
    __swig_destroy__ = _StepVector.delete__StepVector_float

# Register _StepVector_float in _StepVector:
_StepVector._StepVector_float_swigregister(_StepVector_float)
cvar = _StepVector.cvar
_StepVector_float.min_index = _StepVector.cvar._StepVector_float_min_index
_StepVector_float.max_index = _StepVector.cvar._StepVector_float_max_index

class _Pair_long_int(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    first = property(_StepVector._Pair_long_int_first_get, _StepVector._Pair_long_int_first_set)
    second = property(_StepVector._Pair_long_int_second_get, _StepVector._Pair_long_int_second_set)

    def __init__(self, first_, second_):
        _StepVector._Pair_long_int_swiginit(self, _StepVector.new__Pair_long_int(first_, second_))
    __swig_destroy__ = _StepVector.delete__Pair_long_int

# Register _Pair_long_int in _StepVector:
_StepVector._Pair_long_int_swigregister(_Pair_long_int)
class _StepVector_Iterator_int(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, first, last_):
        _StepVector._StepVector_Iterator_int_swiginit(self, _StepVector.new__StepVector_Iterator_int(first, last_))

    def __next__(self):
        return _StepVector._StepVector_Iterator_int___next__(self)

    def __iter__(self):
        return _StepVector._StepVector_Iterator_int___iter__(self)
    __swig_destroy__ = _StepVector.delete__StepVector_Iterator_int

# Register _StepVector_Iterator_int in _StepVector:
_StepVector._StepVector_Iterator_int_swigregister(_StepVector_Iterator_int)
class _StepVector_int(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _StepVector._StepVector_int_swiginit(self, _StepVector.new__StepVector_int())

    def set_value(self, _from, to, value):
        return _StepVector._StepVector_int_set_value(self, _from, to, value)

    def remove_step(self, i):
        return _StepVector._StepVector_int_remove_step(self, i)

    def add_value(self, _from, to, value):
        return _StepVector._StepVector_int_add_value(self, _from, to, value)

    def get_all_values_pystyle(self):
        return _StepVector._StepVector_int_get_all_values_pystyle(self)

    def get_values_pystyle(self, _from):
        return _StepVector._StepVector_int_get_values_pystyle(self, _from)

    def num_values(self):
        return _StepVector._StepVector_int_num_values(self)
    __swig_destroy__ = _StepVector.delete__StepVector_int

# Register _StepVector_int in _StepVector:
_StepVector._StepVector_int_swigregister(_StepVector_int)
_StepVector_int.min_index = _StepVector.cvar._StepVector_int_min_index
_StepVector_int.max_index = _StepVector.cvar._StepVector_int_max_index

class _Pair_long_long(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    first = property(_StepVector._Pair_long_long_first_get, _StepVector._Pair_long_long_first_set)
    second = property(_StepVector._Pair_long_long_second_get, _StepVector._Pair_long_long_second_set)

    def __init__(self, first_, second_):
        _StepVector._Pair_long_long_swiginit(self, _StepVector.new__Pair_long_long(first_, second_))
    __swig_destroy__ = _StepVector.delete__Pair_long_long

# Register _Pair_long_long in _StepVector:
_StepVector._Pair_long_long_swigregister(_Pair_long_long)
class _StepVector_Iterator_long(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, first, last_):
        _StepVector._StepVector_Iterator_long_swiginit(self, _StepVector.new__StepVector_Iterator_long(first, last_))

    def __next__(self):
        return _StepVector._StepVector_Iterator_long___next__(self)

    def __iter__(self):
        return _StepVector._StepVector_Iterator_long___iter__(self)
    __swig_destroy__ = _StepVector.delete__StepVector_Iterator_long

# Register _StepVector_Iterator_long in _StepVector:
_StepVector._StepVector_Iterator_long_swigregister(_StepVector_Iterator_long)
class _StepVector_long(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _StepVector._StepVector_long_swiginit(self, _StepVector.new__StepVector_long())

    def set_value(self, _from, to, value):
        return _StepVector._StepVector_long_set_value(self, _from, to, value)

    def remove_step(self, i):
        return _StepVector._StepVector_long_remove_step(self, i)

    def add_value(self, _from, to, value):
        return _StepVector._StepVector_long_add_value(self, _from, to, value)

    def get_all_values_pystyle(self):
        return _StepVector._StepVector_long_get_all_values_pystyle(self)

    def get_values_pystyle(self, _from):
        return _StepVector._StepVector_long_get_values_pystyle(self, _from)

    def num_values(self):
        return _StepVector._StepVector_long_num_values(self)
    __swig_destroy__ = _StepVector.delete__StepVector_long

# Register _StepVector_long in _StepVector:
_StepVector._StepVector_long_swigregister(_StepVector_long)
_StepVector_long.min_index = _StepVector.cvar._StepVector_long_min_index
_StepVector_long.max_index = _StepVector.cvar._StepVector_long_max_index

class _Pair_long_bool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    first = property(_StepVector._Pair_long_bool_first_get, _StepVector._Pair_long_bool_first_set)
    second = property(_StepVector._Pair_long_bool_second_get, _StepVector._Pair_long_bool_second_set)

    def __init__(self, first_, second_):
        _StepVector._Pair_long_bool_swiginit(self, _StepVector.new__Pair_long_bool(first_, second_))
    __swig_destroy__ = _StepVector.delete__Pair_long_bool

# Register _Pair_long_bool in _StepVector:
_StepVector._Pair_long_bool_swigregister(_Pair_long_bool)
class _StepVector_Iterator_bool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, first, last_):
        _StepVector._StepVector_Iterator_bool_swiginit(self, _StepVector.new__StepVector_Iterator_bool(first, last_))

    def __next__(self):
        return _StepVector._StepVector_Iterator_bool___next__(self)

    def __iter__(self):
        return _StepVector._StepVector_Iterator_bool___iter__(self)
    __swig_destroy__ = _StepVector.delete__StepVector_Iterator_bool

# Register _StepVector_Iterator_bool in _StepVector:
_StepVector._StepVector_Iterator_bool_swigregister(_StepVector_Iterator_bool)
class _StepVector_bool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _StepVector._StepVector_bool_swiginit(self, _StepVector.new__StepVector_bool())

    def set_value(self, _from, to, value):
        return _StepVector._StepVector_bool_set_value(self, _from, to, value)

    def remove_step(self, i):
        return _StepVector._StepVector_bool_remove_step(self, i)

    def add_value(self, _from, to, value):
        return _StepVector._StepVector_bool_add_value(self, _from, to, value)

    def get_all_values_pystyle(self):
        return _StepVector._StepVector_bool_get_all_values_pystyle(self)

    def get_values_pystyle(self, _from):
        return _StepVector._StepVector_bool_get_values_pystyle(self, _from)

    def num_values(self):
        return _StepVector._StepVector_bool_num_values(self)
    __swig_destroy__ = _StepVector.delete__StepVector_bool

# Register _StepVector_bool in _StepVector:
_StepVector._StepVector_bool_swigregister(_StepVector_bool)
_StepVector_bool.min_index = _StepVector.cvar._StepVector_bool_min_index
_StepVector_bool.max_index = _StepVector.cvar._StepVector_bool_max_index

class _Pair_long_obj(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    first = property(_StepVector._Pair_long_obj_first_get, _StepVector._Pair_long_obj_first_set)
    second = property(_StepVector._Pair_long_obj_second_get, _StepVector._Pair_long_obj_second_set)

    def __init__(self, first_, second_):
        _StepVector._Pair_long_obj_swiginit(self, _StepVector.new__Pair_long_obj(first_, second_))
    __swig_destroy__ = _StepVector.delete__Pair_long_obj

# Register _Pair_long_obj in _StepVector:
_StepVector._Pair_long_obj_swigregister(_Pair_long_obj)
class _StepVector_Iterator_obj(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, first, last_):
        _StepVector._StepVector_Iterator_obj_swiginit(self, _StepVector.new__StepVector_Iterator_obj(first, last_))

    def __next__(self):
        return _StepVector._StepVector_Iterator_obj___next__(self)

    def __iter__(self):
        return _StepVector._StepVector_Iterator_obj___iter__(self)
    __swig_destroy__ = _StepVector.delete__StepVector_Iterator_obj

# Register _StepVector_Iterator_obj in _StepVector:
_StepVector._StepVector_Iterator_obj_swigregister(_StepVector_Iterator_obj)
class _StepVector_obj(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _StepVector._StepVector_obj_swiginit(self, _StepVector.new__StepVector_obj())

    def set_value(self, _from, to, value):
        return _StepVector._StepVector_obj_set_value(self, _from, to, value)

    def remove_step(self, i):
        return _StepVector._StepVector_obj_remove_step(self, i)

    def add_value(self, _from, to, value):
        return _StepVector._StepVector_obj_add_value(self, _from, to, value)

    def get_all_values_pystyle(self):
        return _StepVector._StepVector_obj_get_all_values_pystyle(self)

    def get_values_pystyle(self, _from):
        return _StepVector._StepVector_obj_get_values_pystyle(self, _from)

    def num_values(self):
        return _StepVector._StepVector_obj_num_values(self)
    __swig_destroy__ = _StepVector.delete__StepVector_obj

# Register _StepVector_obj in _StepVector:
_StepVector._StepVector_obj_swigregister(_StepVector_obj)
_StepVector_obj.min_index = _StepVector.cvar._StepVector_obj_min_index
_StepVector_obj.max_index = _StepVector.cvar._StepVector_obj_max_index



import sys

class StepVector(object):
    """A step vector is a vector with integer indices that is able to store
    data efficiently if it is piece-wise constant, i.e., if the values change
    in "steps". So, if a number of adjacent vectort elements have the same
    value, this values will be stored only once.

    The data can be either one of a number of elementary types, or any object.

    Usage example:

    >>> sv = StepVector.StepVector(20)
    >>> sv[5:17] = 13
    >>> sv[12]
    13.0
    >>> list(sv)
    [0.0, 0.0, 0.0, 0.0, 0.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 0.0, 0.0, 0.0]
    >>> list(sv.get_steps())
    [(0, 5, 0.0), (5, 17, 13.0), (17, 20, 0.0)]

    """

    @classmethod
    def create(cls, length=sys.maxsize, typecode='d', start_index=0):
        """Construct a StepVector of the given length, with indices starting
        at the given start_index and counting up to (but not including)
        start_index + length.

        The typecode may be:
          'd' for float values (C type 'double'),
          'i' for int values,
          'l' for long int values,
          'b' for Boolean values,
          'O' for arbitrary Python objects as value.

        The vector is initialized with the value zero (or, for typecode 'O',
        with None).
        """
        if typecode == 'd':
            swigclass = _StepVector_float
        elif typecode == 'i':
            swigclass = _StepVector_int
        elif typecode == 'l':
            swigclass = _StepVector_long
        elif typecode == 'b':
            swigclass = _StepVector_bool
        elif typecode == 'O':
            swigclass = _StepVector_obj
        else:
            raise ValueError("unsupported typecode")
        obj = cls()
        obj._typecode = typecode
        obj._swigobj = swigclass()
        obj.start = start_index
        obj.stop = start_index + length
        return obj

    def __setitem__(self, index, value):
        """To set element i of StepVector sv to the value v, write
            sv[i] = v
        If you want to set a whole step, say, all values from i to j (not
        including j), write
            sv[i:j] = v
        Note that the StepVector class will only notice that all the values
        from i to j are equal if you assign them in this fashion. Assigning each
        item individually in a loop from i to j will result in the value v being
        stored many times.
        """
        if isinstance(value, StepVector):
            if self._swigobj is value._swigobj and \
                    value.start == index.start and value.stop == index.stop:
                return
            else:
                raise NotImplemented("Stepvector-to-Stepvector assignment still missing")
        if isinstance(index, slice):
            if index.step is not None and index.step != 1:
                 raise ValueError("Striding slices (i.e., step != 1) are not supported")
            if index.start is None:
                start = self.start
            else:
                if index.start < self.start:
                    raise IndexError("start too small")
                start = index.start
            if index.stop is None:
                stop = self.stop
            else:
                if index.stop > self.stop:
                    raise IndexError("stop too large")
                stop = index.stop

# Note the "-1": The C++ object uses closed intervals, but we follow
# Python convention here and use half-open ones.
            self._swigobj.set_value(start, stop-1, value)

        else:
            self._swigobj.set_value(index, index, value)

    def get_steps(self, values_only=False, merge_steps=True):
        """Iterate over the steps of the vector.

        Args:
            values_only (bool): Return only the values of the StepVector, without
            the index boundaries.

            merge_steps (bool): Perform on-the-fly merging of consecutive steps if
            their value is the same. Setting this option ensures that consecutive
            steps have distinct values.

        Returns: an iterator of triplets, with each triplet containing the start
            index, end index, and value of that step. If values_only is True, the
            function returns an iterator of the values only.
        """
        startvals = self._swigobj.get_values_pystyle(self.start)
        prevstart = self.start
        prevval = next(startvals).second
        for pair in startvals:
            stepstart, value = pair.first, pair.second
            if merge_steps and value == prevval:
                continue
            if (self.stop is not None) and (stepstart >= self.stop):
                if not values_only:
                    yield prevstart, self.stop, prevval
                else:
                    yield prevval
                return
            if not values_only:
                yield prevstart, stepstart, prevval
            else:
                yield prevval
            prevstart, prevval = stepstart, value
        else:
            if not values_only:
                yield prevstart, min(self.stop, self._swigobj.max_index + 1), prevval
            else:
                yield prevval

    def __getitem__(self, index):
        """Given a StepVector sv, writing sv[i] returns sv's element i (where i
        is an integer). 

        If you use a slice, i.e. 'sv[i:j]', you get a view on the StepVector,
        i.e., the same data, but changed boundaries.

        Striding slices, i.e. 'sv[i:j:2]' are not supported.
        """
        if isinstance(index, slice):
            if index.step is not None and index.step != 1:
                 raise ValueError("Striding slices (i.e., step != 1) are not supported")
            if index.start is None:
                start = self.start
            else:
                if index.start < self.start:
                    raise IndexError("start too small")
                start = index.start
            if index.stop is None:
                stop = self.stop
            else:
                if index.stop > self.stop:
                    raise IndexError("stop too large")
                stop = index.stop
            res = self.__class__()
            res._typecode = self.typecode
            res._swigobj = self._swigobj
            res.start = start
            res.stop = stop
            return res
        else:
            return next(self._swigobj.get_values_pystyle(index)).second

    def remove_step(self, start):
        """Remve a step with this starting coordinate, in place.

        Args:
            start: Starting coordinate of the step.
        """
        self._swigobj.remove_step(start)

    def __iter__(self):
        """When asked to provide an iterator, a StepVector will yield all its
        values, repeating each value according to the length of the step.
        Hence, calling, e.g., 'list(sv)' will transform the StepVector 'sv'
        into an ordinary list.
        """
        for start, stop, value in self.get_steps():
            for i in range(start, stop):
                yield value

    def __repr__(self):
        if self.start == -sys.maxsize - 1:
            start_s = "-inf"
        else:
            start_s = str(self.start)
        if self.stop == sys.maxsize:
            stop_s = "inf"
        else:
            stop_s = str(self.stop)
        return "<%s object, type '%s', index range %s:%s, %d step(s)>" % (
            self.__class__.__name__, self.typecode(), start_s,
            stop_s, self.num_steps())

    def typecode(self):
        "Returns the typecode."
        return self._typecode

    def __len__(self):
        """The length of a StepVector is defined by its index range, not by
        the number of steps.
        """
        return self.stop - self.start

    def num_steps(self):
        """Returns the number of steps, i.e., the number of triples that get_steps
        returns.
        """
        return self._swigobj.num_values()

    def __eq__(self, other):
        """StepVectors can be compared for equality. This is conceptually done
        element for element, but, for performance, taking steps in one go.
        """
        if self.start_index() != other.start_index() or len(self) != len(other) or \
                self.typecode() != other.typecode():
            print("Mark A")
            return False
        selfsteps = self.get_steps()
        othrsteps = other.get_steps()
        selfstart, selfstop, selfval = next(selfsteps)
        othrstart, othrstop, othrval = next(othrsteps)
        while selfstop < self.start_index() + len(self) and \
                othrstop < other.start_index() + len(other):
            assert selfstart < othrstop and othrstart < selfstop
            if not(selfval == othrval):
                return False
            if selfstop < othrstop:
                selfstart, selfstop, selfval = next(selfsteps)
            elif othrstop < selfstop:
                othrstart, othrstop, othrval = next(othrsteps)
            else:
                selfstart, selfstop, selfval = next(selfsteps)
                othrstart, othrstop, othrval = next(othrsteps)
        return True

    def __neq__(self, other):
        return not (self == other)

    def __reduce__(self):
        if self.__class__ is not StepVector:
            raise NotImplemented(
                 "Attempting to pickle a subclass of StepVector without redefined __reduce__.")
        return ( 
            _StepVector_unpickle, 
            (self.stop - self.start, self._typecode, self.start),
            None,
            None,
            ((slice(start, stop), val) for start, stop, val in self.get_steps()))

    def __iadd__(self, value):
        self._swigobj.add_value(self.start, self.stop-1, value)
        return self

    def apply(self, func, start=None, stop=None):
# TODO: check!
        for stepstart, stepstop, value in self.get_steps(start, stop):
            self[stepstart:stepstop] = func(value)

def _StepVector_unpickle(length, typecode, start):
    return StepVector.create(length, typecode, start)



