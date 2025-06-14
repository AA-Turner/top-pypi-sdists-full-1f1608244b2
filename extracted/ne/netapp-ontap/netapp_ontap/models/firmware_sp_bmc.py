r"""
Copyright &copy; 2024 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["FirmwareSpBmc", "FirmwareSpBmcSchema"]
__pdoc__ = {
    "FirmwareSpBmcSchema.resource": False,
    "FirmwareSpBmcSchema.opts": False,
    "FirmwareSpBmc": False,
}


class FirmwareSpBmcSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the FirmwareSpBmc object"""

    autoupdate = marshmallow_fields.Boolean(data_key="autoupdate", allow_none=True)
    r""" The autoupdate field of the firmware_sp_bmc.

Example: false """

    end_time = ImpreciseDateTime(data_key="end_time", allow_none=True)
    r""" The end_time field of the firmware_sp_bmc.

Example: 2020-05-17T20:00:00.000+0000 """

    fw_type = marshmallow_fields.Str(data_key="fw_type", allow_none=True)
    r""" The fw_type field of the firmware_sp_bmc.

Valid choices:

* SP
* BMC """

    image = marshmallow_fields.Str(data_key="image", allow_none=True)
    r""" The image field of the firmware_sp_bmc.

Valid choices:

* primary
* backup """

    in_progress = marshmallow_fields.Boolean(data_key="in_progress", allow_none=True)
    r""" The in_progress field of the firmware_sp_bmc. """

    is_current = marshmallow_fields.Boolean(data_key="is_current", allow_none=True)
    r""" The is_current field of the firmware_sp_bmc.

Example: true """

    last_update_state = marshmallow_fields.Str(data_key="last_update_state", allow_none=True)
    r""" The last_update_state field of the firmware_sp_bmc.

Valid choices:

* passed
* failed """

    percent_done = Size(data_key="percent_done", allow_none=True)
    r""" The percent_done field of the firmware_sp_bmc.

Example: 100 """

    running_version = marshmallow_fields.Str(data_key="running_version", allow_none=True)
    r""" The running_version field of the firmware_sp_bmc.

Example: 1.2.3.4 """

    start_time = ImpreciseDateTime(data_key="start_time", allow_none=True)
    r""" The start_time field of the firmware_sp_bmc.

Example: 2020-05-17T20:00:00.000+0000 """

    state = marshmallow_fields.Str(data_key="state", allow_none=True)
    r""" The state field of the firmware_sp_bmc.

Valid choices:

* installed
* corrupt
* updating
* autoupdating
* none """

    @property
    def resource(self):
        return FirmwareSpBmc

    gettable_fields = [
        "autoupdate",
        "end_time",
        "fw_type",
        "image",
        "in_progress",
        "is_current",
        "last_update_state",
        "percent_done",
        "running_version",
        "start_time",
        "state",
    ]
    """autoupdate,end_time,fw_type,image,in_progress,is_current,last_update_state,percent_done,running_version,start_time,state,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class FirmwareSpBmc(Resource):

    _schema = FirmwareSpBmcSchema
