from unittest import mock

from mongomock import Collection as MongoMockCollection
from mongomock.collection import Cursor as MongoMockCursor
from mongomock import Database as MongoMockDatabase

try:
    from gridfs.grid_file import GridOut as PyMongoGridOut
    from gridfs.grid_file import GridOutCursor as PyMongoGridOutCursor
    from pymongo.collection import Collection as PyMongoCollection
    from pymongo.database import Database as PyMongoDatabase

    _HAVE_PYMONGO = True
except ImportError:
    _HAVE_PYMONGO = False


# This is a copy of GridOutCursor but with a different base. Note that we
# need both classes as one might want to access both mongomock and real
# MongoDb.
class _MongoMockGridOutCursor(MongoMockCursor):
    def __init__(self, collection, *args, **kwargs):
        self.__root_collection = collection
        super().__init__(collection.files, *args, **kwargs)

    def next(self):
        next_file = super().next()
        return PyMongoGridOut(self.__root_collection, file_document=next_file, session=self.session)

    __next__ = next

    def add_option(self, *args, **kwargs):
        raise NotImplementedError()

    def remove_option(self, *args, **kwargs):
        raise NotImplementedError()

    def _clone_base(self, session):
        return _MongoMockGridOutCursor(self.__root_collection, session=session)


def _create_grid_out_cursor(collection, *args, **kwargs):
    if isinstance(collection, MongoMockCollection):
        return _MongoMockGridOutCursor(collection, *args, **kwargs)
    return PyMongoGridOutCursor(collection, *args, **kwargs)


def enable_gridfs_integration():
    """This function enables the use of mongomock Database's and Collection's inside gridfs

    Gridfs library use `isinstance` to make sure the passed elements
    are valid `pymongo.Database/Collection` so we monkey patch those types in the gridfs modules
    (luckily in the modules they are used, they are only used with isinstance).
    """

    if not _HAVE_PYMONGO:
        raise NotImplementedError("gridfs mocking requires pymongo to work")

    Database = (PyMongoDatabase, MongoMockDatabase)
    Collection = (PyMongoCollection, MongoMockCollection)

    try:
        mock.patch("gridfs.synchronous.grid_file.Database", Database).start()
        mock.patch("gridfs.synchronous.grid_file.Collection", Collection).start()
        mock.patch("gridfs.synchronous.grid_file.GridOutCursor", _create_grid_out_cursor).start()
    except (AttributeError, ModuleNotFoundError):
        mock.patch("gridfs.Database", Database).start()
        mock.patch("gridfs.grid_file.Collection", Collection).start()
        mock.patch("gridfs.GridOutCursor", _create_grid_out_cursor).start()
