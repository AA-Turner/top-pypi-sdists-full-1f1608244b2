r"""
Copyright &copy; 2024 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["MongoDbOnSanDataset", "MongoDbOnSanDatasetSchema"]
__pdoc__ = {
    "MongoDbOnSanDatasetSchema.resource": False,
    "MongoDbOnSanDatasetSchema.opts": False,
    "MongoDbOnSanDataset": False,
}


class MongoDbOnSanDatasetSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the MongoDbOnSanDataset object"""

    element_count = Size(data_key="element_count", allow_none=True)
    r""" The number of storage elements (LUNs for SAN) of the database to maintain.  Must be an even number between 2 and 16.  Odd numbers will be rounded up to the next even number within range. """

    replication_factor = Size(data_key="replication_factor", allow_none=True)
    r""" The number of data bearing members of the replicaset, including 1 primary and at least 1 secondary. """

    size = Size(data_key="size", allow_none=True)
    r""" The size of the database. Usage: {&lt;integer&gt;[KB|MB|GB|TB|PB]} """

    storage_service = marshmallow_fields.Nested("netapp_ontap.models.mongo_db_on_san_dataset_storage_service.MongoDbOnSanDatasetStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service", allow_none=True)
    r""" The storage_service field of the mongo_db_on_san_dataset. """

    @property
    def resource(self):
        return MongoDbOnSanDataset

    gettable_fields = [
        "element_count",
        "replication_factor",
        "size",
        "storage_service",
    ]
    """element_count,replication_factor,size,storage_service,"""

    patchable_fields = [
        "size",
        "storage_service",
    ]
    """size,storage_service,"""

    postable_fields = [
        "element_count",
        "replication_factor",
        "size",
        "storage_service",
    ]
    """element_count,replication_factor,size,storage_service,"""


class MongoDbOnSanDataset(Resource):

    _schema = MongoDbOnSanDatasetSchema
