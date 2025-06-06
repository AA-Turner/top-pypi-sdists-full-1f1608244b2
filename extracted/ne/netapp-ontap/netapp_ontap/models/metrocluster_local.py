r"""
Copyright &copy; 2024 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["MetroclusterLocal", "MetroclusterLocalSchema"]
__pdoc__ = {
    "MetroclusterLocalSchema.resource": False,
    "MetroclusterLocalSchema.opts": False,
    "MetroclusterLocal": False,
}


class MetroclusterLocalSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the MetroclusterLocal object"""

    automatic_uso_failure_domain = marshmallow_fields.Str(data_key="automatic_uso_failure_domain", allow_none=True)
    r""" This parameter specifies the configuration of automatic switchover.
The valid values for the parameter are ':'
cluster':' triggers an unplanned switchover if all nodes in a DR cluster are down.
dr_group':' triggers an unplanned switchover if both nodes of a DR group are down.
disabled':' automatic switchover is disabled.
If the cluster is not reachable due to errors, the parameter value will be set to
not_reachable. This value is read only.
If the cluster configuration is unknown, the parameter value will be set to
unknown and the value is read only.


Valid choices:

* dr_group
* cluster
* disabled
* not_reachable
* unknown """

    cluster = marshmallow_fields.Nested("netapp_ontap.resources.cluster.ClusterSchema", unknown=EXCLUDE, data_key="cluster", allow_none=True)
    r""" The cluster field of the metrocluster_local. """

    configuration_state = marshmallow_fields.Str(data_key="configuration_state", allow_none=True)
    r""" Indicates the state of the local cluster configuration.

Valid choices:

* configuration_error
* configured
* not_configured
* not_reachable
* partially_configured
* unknown """

    mode = marshmallow_fields.Str(data_key="mode", allow_none=True)
    r""" Specifies the mode of operation of the local cluster.

Valid choices:

* normal
* not_configured
* not_reachable
* partial_switchback
* partial_switchover
* switchover
* unknown
* waiting_for_switchback """

    partner_cluster_reachable = marshmallow_fields.Boolean(data_key="partner_cluster_reachable", allow_none=True)
    r""" Specifies whether the partner cluster is reachable from the local cluster. """

    periodic_check_enabled = marshmallow_fields.Boolean(data_key="periodic_check_enabled", allow_none=True)
    r""" Indicates whether or not a periodic check is enabled on the local cluster. """

    @property
    def resource(self):
        return MetroclusterLocal

    gettable_fields = [
        "automatic_uso_failure_domain",
        "cluster.links",
        "cluster.name",
        "cluster.uuid",
        "configuration_state",
        "mode",
        "partner_cluster_reachable",
        "periodic_check_enabled",
    ]
    """automatic_uso_failure_domain,cluster.links,cluster.name,cluster.uuid,configuration_state,mode,partner_cluster_reachable,periodic_check_enabled,"""

    patchable_fields = [
        "automatic_uso_failure_domain",
        "cluster.name",
        "cluster.uuid",
    ]
    """automatic_uso_failure_domain,cluster.name,cluster.uuid,"""

    postable_fields = [
        "automatic_uso_failure_domain",
        "cluster.name",
        "cluster.uuid",
    ]
    """automatic_uso_failure_domain,cluster.name,cluster.uuid,"""


class MetroclusterLocal(Resource):

    _schema = MetroclusterLocalSchema
