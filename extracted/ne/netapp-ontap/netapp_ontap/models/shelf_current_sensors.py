r"""
Copyright &copy; 2024 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["ShelfCurrentSensors", "ShelfCurrentSensorsSchema"]
__pdoc__ = {
    "ShelfCurrentSensorsSchema.resource": False,
    "ShelfCurrentSensorsSchema.opts": False,
    "ShelfCurrentSensors": False,
}


class ShelfCurrentSensorsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ShelfCurrentSensors object"""

    current = Size(data_key="current", allow_none=True)
    r""" Current, in milliamps

Example: 14410 """

    id = Size(data_key="id", allow_none=True)
    r""" The id field of the shelf_current_sensors.

Example: 1 """

    installed = marshmallow_fields.Boolean(data_key="installed", allow_none=True)
    r""" The installed field of the shelf_current_sensors.

Example: true """

    location = marshmallow_fields.Str(data_key="location", allow_none=True)
    r""" The location field of the shelf_current_sensors.

Example: rear of the shelf on the lower left power supply """

    state = marshmallow_fields.Str(data_key="state", allow_none=True)
    r""" The state field of the shelf_current_sensors.

Valid choices:

* ok
* error """

    @property
    def resource(self):
        return ShelfCurrentSensors

    gettable_fields = [
        "current",
        "id",
        "installed",
        "location",
        "state",
    ]
    """current,id,installed,location,state,"""

    patchable_fields = [
        "current",
        "id",
        "installed",
        "location",
        "state",
    ]
    """current,id,installed,location,state,"""

    postable_fields = [
        "current",
        "id",
        "installed",
        "location",
        "state",
    ]
    """current,id,installed,location,state,"""


class ShelfCurrentSensors(Resource):

    _schema = ShelfCurrentSensorsSchema
