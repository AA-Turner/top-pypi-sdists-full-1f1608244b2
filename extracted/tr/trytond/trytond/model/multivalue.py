# This file is part of Tryton.  The COPYRIGHT file at the toplevel of this
# repository contains the full copyright notices and license terms.
from threading import Lock

from trytond.cache import Cache
from trytond.pool import Pool

from .fields import MultiValue
from .match import MatchMixin
from .model import Model
from .modelstorage import ModelStorage


class MultiValueMixin(object):
    __slots__ = ()

    @classmethod
    def multivalue_model(cls, field):
        pool = Pool()
        Value = pool.get('%s.%s' % (cls.__name__, field))
        assert issubclass(Value, ValueMixin), (
            "%s is not a subclass of ValueMixin" % Value)
        return Value

    def multivalue_records(self, field):
        Value = self.multivalue_model(field)
        for fname, field in self._fields.items():
            if (field._type == 'one2many'
                    and field.model_name == Value.__name__
                    and not field.filter):
                return getattr(self, fname)
        return Value.values()

    def multivalue_record(self, field, **pattern):
        Value = self.multivalue_model(field)
        for fname, field in Value._fields.items():
            if (field._type == 'many2one'
                    and field.model_name == self.__name__):
                pattern = pattern.copy()
                pattern[fname] = self
                break
        record = Value(**pattern)
        for oname, ofield in self._fields.items():
            if (oname != field
                    and isinstance(ofield, MultiValue)
                    and self.multivalue_model(oname) == Value):
                func = getattr(self, 'default_%s' % oname, None)
                if func:
                    setattr(record, oname, func(**pattern))
        return record

    def __values(self, field, pattern, match_none=True):
        return [v for v in self.multivalue_records(field)
            if v.match(pattern, match_none=match_none)]

    def get_multivalue(self, name, **pattern):
        Value = self.multivalue_model(name)
        pattern = filter_pattern(pattern, Value)
        values = self.__values(name, pattern, match_none=False)
        if not values:
            value = Value(**pattern)
            func = getattr(self, 'default_%s' % name, lambda **kw: None)
            setattr(value, name, func(**pattern))
        else:
            value = values[0]
        return getattr(value, name)

    def _multivalue_getter(self, name):
        Value = self.multivalue_model(name)
        value = self.get_multivalue(name)
        if isinstance(value, Model):
            if Value._fields[name]._type == 'reference':
                return str(value)
            return value.id
        elif isinstance(value, (list, tuple)):
            return tuple(r.id if isinstance(r, Model) else r for r in value)
        else:
            return value

    def set_multivalue(self, name, value, save=True, **pattern):
        Value = self.multivalue_model(name)
        pattern = filter_pattern(pattern, Value)
        values = self.__values(name, pattern, match_none=True)
        if not values:
            values = [self.multivalue_record(name, **pattern)]
        for record in values:
            current_value = getattr(record, name, None)
            if isinstance(current_value, Model):
                current_value = current_value.id
            elif isinstance(current_value, (list, tuple)):
                current_value = [
                    r.id if isinstance(r, Model) else r for r in current_value]
            if current_value != value:
                setattr(record, name, value)
        if save:
            Value.save(values)
        else:
            return values

    @classmethod
    def _multivalue_setter(cls, records, name, val):
        Value = cls.multivalue_model(name)
        to_save = []
        for record in records:
            to_save.extend(record.set_multivalue(name, val, save=False))
        Value.save(to_save)


class ValueMixin(MatchMixin, ModelStorage):
    __slots__ = ()

    __caches = {}
    __caches_lock = Lock()

    def match(self, pattern, match_none=True):
        return super().match(pattern, match_none=match_none)

    @classmethod
    def _values_cache(cls):
        if (cache := cls.__caches.get(cls.__name__)) is None:
            with cls.__caches_lock:
                if (cache := cls.__caches.get(cls.__name__)) is None:
                    cache = Cache(cls.__name__ + '.values')
                    cls.__caches[cls.__name__] = cache
        return cache

    @classmethod
    def values(cls):
        cache = cls._values_cache()
        if (ids := cache.get(None)) is not None:
            return cls.browse(ids)
        records = cls.search([])
        cache.set(None, [r.id for r in records])
        return records

    @classmethod
    def on_modification(cls, mode, records, field_names=None):
        super().on_modification(mode, records, field_names=field_names)
        cls._values_cache().clear()


def filter_pattern(pattern, Value):
    return {f: v for f, v in pattern.items() if f in Value._fields}
