'''
IPDB
----

Deprecated since 0.7.12, removed from the library.

The current `pyroute2.ipdb` implementation is a wrapper around NDB
only to provide minimal compatibility for the old legacy code. Do
NOT use IPDB.
'''

import errno
import logging
import warnings

from pyroute2.ndb.main import NDB
from pyroute2.netlink.exceptions import NetlinkError

log = logging.getLogger(__name__)


class CreateException(Exception):
    pass


class CommitException(Exception):
    pass


class ObjectProxy(dict):

    _translate_keys = {}

    def __init__(self, obj, ready=True):
        self._obj = obj
        self._ready = ready

    def __getattribute__(self, key):
        if key[:4] == 'set_':

            def set_value(value):
                self[key[4:]] = value
                return self

            return set_value
        try:
            return self[key]
        except KeyError:
            return super(ObjectProxy, self).__getattribute__(key)

    def __setattr__(self, key, value):
        if key in ('_obj', '_ready', '_translate_keys'):
            super(ObjectProxy, self).__setattr__(key, value)
        else:
            super(ObjectProxy, self).__getattribute__('_obj')[key] = value

    def __getitem__(self, key):
        tk = super().__getattribute__('_translate_keys')
        if isinstance(key, str) and key in tk:
            return super().__getattribute__('_obj')[tk[key](self)]
        return super(ObjectProxy, self).__getattribute__('_obj')[key]

    def __setitem__(self, key, value):
        tk = super().__getattribute__('_translate_keys')
        if isinstance(key, str) and key in tk:
            super().__getattribute__('_obj')[tk[key](self)] = value
        super(ObjectProxy, self).__getattribute__('_obj')[key] = value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if hasattr(self, 'commit'):
            self.commit()

    def __repr__(self):
        return repr(super(ObjectProxy, self).__getattribute__('_obj'))

    def __contains__(self, key):
        return key in super(ObjectProxy, self).__getattribute__('_obj')

    def get_ndb_object(self):
        return self._obj

    def get(self, key, *argv):
        return self._obj.get(key, *argv)

    def keys(self):
        return self._obj.keys()

    def items(self):
        return self._obj.items()

    def values(self):
        return self._obj.values()

    def __iter__(self):
        return self._obj.__iter__()

    @property
    def _mode(self):
        return 'implicit'


class Interface(ObjectProxy):

    _translate_keys = {'mode': lambda x: f'{x["kind"]}_mode'}

    def add_ip(self, address=None, prefixlen=None, **kwarg):
        if address is not None:
            kwarg['address'] = address
        if prefixlen is not None:
            kwarg['prefixlen'] = prefixlen
        self._obj.add_ip(spec=kwarg)
        return self

    def del_ip(self, address=None, prefixlen=None, **kwarg):
        if address is not None:
            kwarg['address'] = address
        if prefixlen is not None:
            kwarg['prefixlen'] = prefixlen
        self._obj.del_ip(spec=kwarg)
        return self

    def add_port(self, *argv, **kwarg):
        self._obj.add_port(*argv, **kwarg)
        return self

    def del_port(self, *argv, **kwarg):
        self._obj.del_port(*argv, **kwarg)
        return self

    def commit(self, *argv, **kwarg):
        try:
            self._obj.commit(*argv, **kwarg)
        except Exception as e:
            if self._ready:
                raise CommitException(e)
            else:
                raise CreateException(e)
        self._ready = True
        return self

    def up(self):
        self._obj.set('state', 'up')
        return self

    def down(self):
        self._obj.set('state', 'down')
        return self

    def remove(self):
        self._obj.remove()
        return self

    @property
    def if_master(self):
        return self._obj.get('master', None)

    @property
    def ipaddr(self):
        report = self._obj.ipaddr.dump()
        report.select_fields('address', 'prefixlen')
        return tuple(report)


class Interfaces(ObjectProxy):
    text_create = '''
When `create().commit()` fails, the failed interface object behaves
differently in IPDB and NDB. IPDB saves the failed object in the database,
while the NDB database contains only the system reflection, and the failed
object may stay only being referenced by a variable.
'''

    def __getitem__(self, key):
        return Interface(super(Interfaces, self).__getitem__(key))

    def __iter__(self):
        return iter(self.keys())

    def add(self, *argv, **kwarg):
        return self.create(*argv, **kwarg)

    def get(self, spec, *argv):
        try:
            return self[spec]
        except KeyError:
            if len[argv] > 0:
                return argv[0]
            raise

    def create(self, *argv, **kwarg):
        log.warning(self.text_create)
        key = dict(
            filter(lambda x: x[0] in ('ifname', 'index'), kwarg.items())
        )
        if key in self:
            if kwarg.get('reuse'):
                return self[key]
            raise CreateException(NetlinkError(errno.EEXIST, 'object exists'))
        return Interface(self._obj.create(*argv, **kwarg), ready=False)

    def keys(self):
        ret = []
        for record in self._obj.dump():
            ret += [record.ifname, record.index]
        return ret

    def has_key(self, key):
        return key in self.keys()


class IPDB(object):
    text_create = '''
IPDB has a shortcut method to create interfaces: `ipdb.create(...)`.

NDB has `create()` methods only under respective views:
`ndb.interfaces.create(...)`, `ndb.addresses.create(...)` etc.
'''

    text_nl = '''
Unlike IPDB, NDB can work with many netlink sources. The default one
referenced as `localhost`::

    #
    # these two statements are equivalent:
    #
    ndb.sources['localhost'].nl.get_links()
    ipdb.nl.get_links()

'''

    def __init__(self, *argv, **kwarg):
        warnings.warn(
            '''
            IPDB module is deprecated and removed.
            This IPDB instance is just a wrapper around
            NDB. See more:

            https://github.com/svinota/pyroute2/wiki/IPDB-EOL
            ''',
            DeprecationWarning,
        )
        sources = kwarg.pop('sources', [{'target': 'localhost'}])
        if argv or kwarg:
            log.warning(
                '%s does not support IPDB parameters, ignoring',
                self.__class__.__name__,
            )
        if len(argv) > 0 or 'nl' in kwarg:
            log.warning(
                '%s does not support shared netlink sources,'
                ' ignoring `nl` and starting with local IPRoute',
                self.__class__.__name__,
            )

        self._ndb = NDB(sources=sources)
        self.interfaces = Interfaces(self._ndb.interfaces)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.release()

    @property
    def nl(self):
        log.warning(self.text_nl)
        return self._ndb.sources['localhost'].nl

    @property
    def ipaddr(self):
        ret = dict([(x.index, []) for x in self._ndb.interfaces.dump()])
        for record in self._ndb.addresses.dump():
            ret[record.index].append((record.address, record.prefixlen))
        return ret

    def create(self, *argv, **kwarg):
        log.warning(self.text_create)
        return self.interfaces.create(*argv, **kwarg)

    def release(self):
        self._ndb.close()
