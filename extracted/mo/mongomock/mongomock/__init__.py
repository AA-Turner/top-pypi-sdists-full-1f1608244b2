import os

try:
    from pymongo.errors import PyMongoError
except ImportError:
    class PyMongoError(Exception):
        pass
try:
    from pymongo.errors import OperationFailure
except ImportError:
    class OperationFailure(PyMongoError):

        def __init__(self, message, code=None, details=None):
            super().__init__()
            self._message = message
            self._code = code
            self._details = details

        code = property(lambda self: self._code)
        details = property(lambda self: self._details)

        def __str__(self):
            return self._message

try:
    from pymongo.errors import WriteError
except ImportError:
    class WriteError(OperationFailure):
        pass


try:
    from pymongo.errors import DuplicateKeyError
except ImportError:
    class DuplicateKeyError(WriteError):
        pass

try:
    from pymongo.errors import BulkWriteError
except ImportError:
    class BulkWriteError(OperationFailure):

        def __init__(self, results):
            super().__init__(
                'batch op errors occurred', 65, results)


try:
    from pymongo.errors import CollectionInvalid
except ImportError:
    class CollectionInvalid(PyMongoError):
        pass

try:
    from pymongo.errors import InvalidName
except ImportError:
    class InvalidName(PyMongoError):
        pass

try:
    from pymongo.errors import InvalidOperation
except ImportError:
    class InvalidOperation(PyMongoError):
        pass

try:
    from pymongo.errors import ConfigurationError
except ImportError:
    class ConfigurationError(PyMongoError):
        pass

try:
    from pymongo.errors import InvalidURI
except ImportError:
    class InvalidURI(ConfigurationError):
        pass

from .helpers import ObjectId, utcnow  # noqa
from mongomock.__version__ import __version__


__all__ = [
    '__version__',
    'Database',
    'DuplicateKeyError',
    'Collection',
    'CollectionInvalid',
    'InvalidName',
    'MongoClient',
    'ObjectId',
    'OperationFailure',
    'WriteConcern',
    'ignore_feature',
    'patch',
    'warn_on_feature',
    'SERVER_VERSION',
]

from .collection import Collection
from .database import Database
from .mongo_client import MongoClient
from .patch import patch
from .write_concern import WriteConcern
from .not_implemented import ignore_feature, warn_on_feature

# The version of the server faked by mongomock. Callers may patch it before creating connections to
# update the behavior of mongomock.
# Keep the default version in sync with docker-compose.yml and travis.yml.
SERVER_VERSION = os.getenv('MONGODB', '5.0.5')
