r"""
Copyright &copy; 2024 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

import asyncio
from datetime import datetime
import inspect
from typing import Callable, Iterable, List, Optional, Union

from marshmallow import fields as marshmallow_fields, EXCLUDE  # type: ignore

import netapp_ontap
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size
from netapp_ontap.raw_resource import RawResource

from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["Application", "ApplicationSchema"]
__pdoc__ = {
    "ApplicationSchema.resource": False,
    "ApplicationSchema.opts": False,
}


class ApplicationSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Application object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.application_links.ApplicationLinksSchema", data_key="_links", unknown=EXCLUDE, allow_none=True)
    r""" The links field of the application."""

    creation_timestamp = marshmallow_fields.Str(
        data_key="creation_timestamp",
        allow_none=True,
    )
    r""" The time when the application was created."""

    delete_data = marshmallow_fields.Boolean(
        data_key="delete_data",
        allow_none=True,
    )
    r""" Should application storage elements be deleted? An application is considered to use storage elements from a shared storage pool. Possible values are 'true' and 'false'. If the value is 'true', the application will be deleted in its entirety. If the value is 'false', the storage elements will be disassociated from the application and preserved. The application will then be deleted."""

    generation = Size(
        data_key="generation",
        allow_none=True,
    )
    r""" The generation number of the application. This indicates which features are supported on the application. For example, generation 1 applications do not support Snapshot copies. Support for Snapshot copies was added at generation 2. Any future generation numbers and their feature set will be documented."""

    mongo_db_on_san = marshmallow_fields.Nested("netapp_ontap.models.mongo_db_on_san.MongoDbOnSanSchema", data_key="mongo_db_on_san", unknown=EXCLUDE, allow_none=True)
    r""" MongoDB using SAN."""

    name = marshmallow_fields.Str(
        data_key="name",
        allow_none=True,
    )
    r""" Application Name. This field is user supplied when the application is created."""

    nas = marshmallow_fields.Nested("netapp_ontap.models.nas.NasSchema", data_key="nas", unknown=EXCLUDE, allow_none=True)
    r""" A generic NAS application."""

    nvme = marshmallow_fields.Nested("netapp_ontap.models.zapp_nvme.ZappNvmeSchema", data_key="nvme", unknown=EXCLUDE, allow_none=True)
    r""" An NVME application."""

    oracle_on_nfs = marshmallow_fields.Nested("netapp_ontap.models.oracle_on_nfs.OracleOnNfsSchema", data_key="oracle_on_nfs", unknown=EXCLUDE, allow_none=True)
    r""" Oracle using NFS."""

    oracle_on_san = marshmallow_fields.Nested("netapp_ontap.models.oracle_on_san.OracleOnSanSchema", data_key="oracle_on_san", unknown=EXCLUDE, allow_none=True)
    r""" Oracle using SAN."""

    oracle_rac_on_nfs = marshmallow_fields.Nested("netapp_ontap.models.oracle_rac_on_nfs.OracleRacOnNfsSchema", data_key="oracle_rac_on_nfs", unknown=EXCLUDE, allow_none=True)
    r""" Oracle RAC using NFS."""

    oracle_rac_on_san = marshmallow_fields.Nested("netapp_ontap.models.oracle_rac_on_san.OracleRacOnSanSchema", data_key="oracle_rac_on_san", unknown=EXCLUDE, allow_none=True)
    r""" Oracle RAC using SAN."""

    protection_granularity = marshmallow_fields.Str(
        data_key="protection_granularity",
        validate=enum_validation(['application', 'component']),
        allow_none=True,
    )
    r""" Protection granularity determines the scope of Snapshot copy operations for the application. Possible values are "application" and "component". If the value is "application", Snapshot copy operations are performed on the entire application. If the value is "component", Snapshot copy operations are performed separately on the application components.

Valid choices:

* application
* component"""

    rpo = marshmallow_fields.Nested("netapp_ontap.models.application_rpo.ApplicationRpoSchema", data_key="rpo", unknown=EXCLUDE, allow_none=True)
    r""" The rpo field of the application."""

    s3_bucket = marshmallow_fields.Nested("netapp_ontap.models.zapp_s3_bucket.ZappS3BucketSchema", data_key="s3_bucket", unknown=EXCLUDE, allow_none=True)
    r""" A generic S3 bucket application."""

    san = marshmallow_fields.Nested("netapp_ontap.models.san.SanSchema", data_key="san", unknown=EXCLUDE, allow_none=True)
    r""" A generic SAN application."""

    smart_container = marshmallow_fields.Boolean(
        data_key="smart_container",
        allow_none=True,
    )
    r""" Identifies if this is a smart container or not."""

    sql_on_san = marshmallow_fields.Nested("netapp_ontap.models.sql_on_san.SqlOnSanSchema", data_key="sql_on_san", unknown=EXCLUDE, allow_none=True)
    r""" Microsoft SQL using SAN."""

    sql_on_smb = marshmallow_fields.Nested("netapp_ontap.models.sql_on_smb.SqlOnSmbSchema", data_key="sql_on_smb", unknown=EXCLUDE, allow_none=True)
    r""" Microsoft SQL using SMB."""

    state = marshmallow_fields.Str(
        data_key="state",
        validate=enum_validation(['creating', 'deleting', 'modifying', 'online', 'restoring']),
        allow_none=True,
    )
    r""" The state of the application. For full functionality, applications must be in the online state. Other states indicate that the application is in a transient state and not all operations are supported.

Valid choices:

* creating
* deleting
* modifying
* online
* restoring"""

    statistics = marshmallow_fields.Nested("netapp_ontap.models.application_statistics.ApplicationStatisticsSchema", data_key="statistics", unknown=EXCLUDE, allow_none=True)
    r""" The statistics field of the application."""

    svm = marshmallow_fields.Nested("netapp_ontap.models.application_svm.ApplicationSvmSchema", data_key="svm", unknown=EXCLUDE, allow_none=True)
    r""" The svm field of the application."""

    template = marshmallow_fields.Nested("netapp_ontap.models.application_template1.ApplicationTemplate1Schema", data_key="template", unknown=EXCLUDE, allow_none=True)
    r""" The template field of the application."""

    uuid = marshmallow_fields.Str(
        data_key="uuid",
        allow_none=True,
    )
    r""" Application UUID. This field is generated when the application is created."""

    vdi_on_nas = marshmallow_fields.Nested("netapp_ontap.models.vdi_on_nas.VdiOnNasSchema", data_key="vdi_on_nas", unknown=EXCLUDE, allow_none=True)
    r""" A VDI application using NAS."""

    vdi_on_san = marshmallow_fields.Nested("netapp_ontap.models.vdi_on_san.VdiOnSanSchema", data_key="vdi_on_san", unknown=EXCLUDE, allow_none=True)
    r""" A VDI application using SAN."""

    vsi_on_nas = marshmallow_fields.Nested("netapp_ontap.models.vsi_on_nas.VsiOnNasSchema", data_key="vsi_on_nas", unknown=EXCLUDE, allow_none=True)
    r""" A VSI application using NAS."""

    vsi_on_san = marshmallow_fields.Nested("netapp_ontap.models.vsi_on_san.VsiOnSanSchema", data_key="vsi_on_san", unknown=EXCLUDE, allow_none=True)
    r""" A VSI application using SAN."""

    @property
    def resource(self):
        return Application

    gettable_fields = [
        "links",
        "creation_timestamp",
        "generation",
        "mongo_db_on_san",
        "name",
        "nas",
        "nvme",
        "oracle_on_nfs",
        "oracle_on_san",
        "oracle_rac_on_nfs",
        "oracle_rac_on_san",
        "protection_granularity",
        "rpo",
        "s3_bucket",
        "san",
        "smart_container",
        "sql_on_san",
        "sql_on_smb",
        "state",
        "statistics",
        "svm",
        "template",
        "uuid",
        "vdi_on_nas",
        "vdi_on_san",
        "vsi_on_nas",
        "vsi_on_san",
    ]
    """links,creation_timestamp,generation,mongo_db_on_san,name,nas,nvme,oracle_on_nfs,oracle_on_san,oracle_rac_on_nfs,oracle_rac_on_san,protection_granularity,rpo,s3_bucket,san,smart_container,sql_on_san,sql_on_smb,state,statistics,svm,template,uuid,vdi_on_nas,vdi_on_san,vsi_on_nas,vsi_on_san,"""

    patchable_fields = [
        "mongo_db_on_san",
        "nas",
        "nvme",
        "oracle_on_nfs",
        "oracle_on_san",
        "oracle_rac_on_nfs",
        "oracle_rac_on_san",
        "s3_bucket",
        "san",
        "sql_on_san",
        "sql_on_smb",
        "template",
        "vdi_on_nas",
        "vdi_on_san",
        "vsi_on_nas",
        "vsi_on_san",
    ]
    """mongo_db_on_san,nas,nvme,oracle_on_nfs,oracle_on_san,oracle_rac_on_nfs,oracle_rac_on_san,s3_bucket,san,sql_on_san,sql_on_smb,template,vdi_on_nas,vdi_on_san,vsi_on_nas,vsi_on_san,"""

    postable_fields = [
        "delete_data",
        "mongo_db_on_san",
        "name",
        "nas",
        "nvme",
        "oracle_on_nfs",
        "oracle_on_san",
        "oracle_rac_on_nfs",
        "oracle_rac_on_san",
        "s3_bucket",
        "san",
        "smart_container",
        "sql_on_san",
        "sql_on_smb",
        "svm",
        "template",
        "vdi_on_nas",
        "vdi_on_san",
        "vsi_on_nas",
        "vsi_on_san",
    ]
    """delete_data,mongo_db_on_san,name,nas,nvme,oracle_on_nfs,oracle_on_san,oracle_rac_on_nfs,oracle_rac_on_san,s3_bucket,san,smart_container,sql_on_san,sql_on_smb,svm,template,vdi_on_nas,vdi_on_san,vsi_on_nas,vsi_on_san,"""

class Application(Resource):
    r""" Applications """

    _schema = ApplicationSchema
    _path = "/api/application/applications"
    _keys = ["uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves applications.
### Expensive properties
There is an added computational cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more.
* `<template>` the property corresponding to the `template.name` of the application
### Query examples
Numerous queries are available for classifying and sorting applications:
1. Return a list of applications sorted by name.
    ```
    GET /application/applications?order_by=name
    ```
    <br/>
2. Return a list of applications for a specific SVM.
    ```
    GET /application/applications?svm.name=<name>
    ```
    <br/>
3. Return a list of all SQL applications.
    ```
    GET /application/applications?template.name=sql*
    ```
    <br/>
4. Return a list of all applications that can be accessed via SAN.<br/>
    ```
    GET /application/applications?template.protocol=san
    ```
    <br/>
5. Return the top five applications consuming the most IOPS.<br/>
    ```
    GET /application/applications?order_by=statistics.iops.total desc&max_records=5
    ```
<br/>The above examples are not comprehensive. There are many more properties available for queries. Also, multiple queries can be mixed and matched with other query parameters for a large variety of requests. See the per-property documentation below for the full list of supported query parameters.
### Learn more
* [`DOC /application`](#docs-application-overview)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all Application resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)


    @classmethod
    def fast_get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["RawResource"]:
        """Returns a list of RawResources that represent Application resources that match the provided query"""
        return super()._get_collection(
            *args, connection=connection, max_records=max_records, raw=True, **kwargs
        )

    fast_get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        records: Iterable["Application"] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the properties of an application.

### Overview
Similar to creating an application, modification is done using the template properties of an application. The `storage_service`, `size`, and `igroup_name` of an application may be modified.
### `storage_service`
Storage service modifications are processed in place, meaning that the storage can not be moved to a location with more performance headroom to accommodate the request. If the current backing storage of the application is in a location that can support increased performance, the QoS policies associated with the application will be modified to allow it. If not, an error will be returned. A storage service modification to a lower tier of performance is always allowed, but the reverse modification may not be supported if the cluster is over provisioned and the cluster is unlikely to be able to fulfil the original storage service.
### `size`
Size modifications are processed in a variety of ways depending on the type of application. For NAS applications, volumes are grown or new volumes are added. For SAN applications, LUNs are grown, new LUNs are added to existing volumes, or new LUNs are added to new volumes. If new storage elements are created, they can be found using the [`GET /application/applications/{application.uuid}/components`](#operations-application-application_component_collection_get) interface. The creation time of each storage object is included, and the newly created objects will use the same naming scheme as the previous objects. Resize follows the best practices associated with the type of application being expanded. Reducing the size of an application is not supported.
### `igroup_name`
Modification of the igroup name allows an entire application to be mapped from one initiator group to another. Data access will be interrupted as the LUNs are unmapped from the original igroup and remapped to the new one.
### Application state
During a modification, the `state` property of the application updates to indicate `modifying`. In `modifying` state, statistics are not available and snapshot operations are not allowed. If the modification fails, it is possible for the application to be left in an inconsistent state, with the underlying ONTAP storage elements not matching across a component. When this occurs, the application is left in the `modifying` state until the command is either retried and succeeds or a call to restore the original state is successful.
### Examples
1. Change the storage service of the database of the Oracle application to _extreme_ and resize the redo logs to _100GB_.
    ```
    {
      "oracle_on_nfs": {
        "db": {
          "storage_service": {
            "name": "extreme"
          }
        },
        "redo_log": {
          "size": "100GB"
        }
      }
    }
    ```
    <br/>
2. Change the storage service, size, and igroup of a generic application by component name.
    ```
    {
      "san": {
        "application_components": [
          {
            "name": "component1",
            "storage_service": {
              "name": "value"
            }
          },
          {
            "name": "component2",
            "size": "200GB"
          },
          {
            "name": "component3",
            "igroup_name": "igroup5"
          }
        ]
      }
    }
    ```
    <br/>
### Learn more
* [`DOC /application`](#docs-application-overview)
* [`Asynchronous operations`](#Synchronous_and_asynchronous_operations)
"""
        return super()._patch_collection(
            body, *args, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)

    @classmethod
    def post_collection(
        cls,
        records: Iterable["Application"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["Application"], NetAppResponse]:
        r"""Creates an application.

### Template properties
The application APIs appear to be complex and long in this documentation because we document every possible template, of which there are currently 14. When creating an application, only a single template is used, so it is best to focus only on the template of interest. Other than the properties for the chosen template, only the `name` and `svm` of the application must be provided. The following three sections provided guidelines on using the properties of the templates, but the whole idea behind the templates is to automatically follow the best practices of the given application, so the only way to determine the exact list of required properties and default values is to dig in to the model section of the template. The templates are all top level properties of the application object with names matching the values returned by [`GET /application/templates`](#operations-application-application_template_collection_get).
### Required properties
* `svm.uuid` or `svm.name` - The existing SVM in which to create the application.
* `name` - The name for the application.
* `<template>` - Properties for one template must be provided. In general, the following properties are required, however the naming of these may vary slightly from template to template.
  * `<template>.name` - The generic templates require names for the components of the application. Other templates name the components automatically.
  * `<template>.application_component.size` - This generally refers to the size of an application component, which may be spread across multiple underlying storage objects (volumes, LUNs, etc...).
  * One of the following must be specified:
      * `nas.nfs_access` or an identifier (name or id) of an existing `export-policy`.
      * `nas.cifs_access`
      * `san.application_application.igroup_name`
  * To specify that a NAS application is not to be exposed via NFS nor CIFS:
      * `nas.application_component.export_policy.name` is 'none', and
      * `nas.application.cifs_share_name` is 'none'.
  * The name of the CIFS share can be provided through the `nas.application.cifs_share_name` attribute. If not provided, the CIFS share name will be the same as the `nas.application_component.name` attribute, including any suffix applied due to creating multiple application components in one post.
  * `san.os_type` - All SAN applications require an os_type to be specified in some way. Some templates refer to this as the `hypervisor`.
### Recommended optional properties
* `<template>` - The following properties are available in some templates.
  * `san.new_igroups.*` - SAN applications can use existing initiator groups or create new ones. When creating new initiator groups, `new_igroups.name` is required and the other properties may be used to fully specify the new initiator group.
### Default property values
If not specified in POST, the follow default property values are assigned. It is recommended that most of these properties be provided explicitly rather than relying upon the defaults. The defaults are intended to make it as easy as possible to provision and connect to an application.
* `template.name` - Defaults to match the `<template>` provided. If specified, the value of this property must match the provided template properties.
* `<template>` - The majority of template properties have default values. The defaults may vary from template to template. See the model of each template for complete details. In general the following patterns are common across all template properties. The location of these properties varies from template to template.
  * `<template>.storage_service.name` - _value_
  * `<template>.protection_type.local_rpo` - _hourly_ (Hourly snapshots)
  * `<template>.protection_type.remote_rpo` - _none_ (Not MetroCluster)
  * `san.new_igroups.os_type` - Defaults to match the `os_type` provided for the application, but may need to be provided explicitly when using virtualization.
### Optional components
A common pattern across many templates are objects that are optional, but once any property in the object is specified, other properties within the object become required. Many applications have optional components. For example, provisioning a database without a component to store the logs is supported. If the properties related to the logs are omitted, no storage will be provisioned for logs. But when the additional component is desired, the size is required. Specifying any other property of a component without specifying the size is not supported. In the model of each template, the required components are indicated with a red '*'. When a `size` property is listed as optional, that means the component itself is optional, and the size should be specified to include that component in the application.
### POST body examples
1. Create a generic SAN application that exposes four LUNs to an existing initiator group, _igroup_1_.<br/>
    ```
    {
      "name": "app1",
      "svm": { "name": "svm1" },
      "san": {
        "os_type": "linux",
        "application_components": [
          { "name": "component1", "total_size": "10GB", "lun_count": 4, "igroup_name": "igroup_1" }
        ]
      }
    }
    ```
    <br/>
2. Create an SQL application that can be accessed via initiator _iqn.2017-01.com.example:foo_ from a new initiator group, _igroup_2_.<br/>
    ```
    {
      "name": "app2",
      "svm": { "name": "svm1" },
      "sql_on_san": {
        "db": { "size": "5GB" },
        "log": { "size": "1GB" },
        "temp_db": { "size": "2GB" },
        "igroup_name": "igroup_2",
        "new_igroups": [
          { "name": "igroup_2", "initiators": [ "iqn.2017-01.com.example:foo" ] }
        ]
      }
    }
    ```
    <br/>
3. The following body creates the exact same SQL application, but manually provides all the defaults that were excluded from the previous call. Note: The model of a _sql_on_san_ application documents all these default values.<br/>
    ```
    {
      "name": "app3",
      "svm": { "name": "svm1" },
      "template": { "name": "sql_on_san" },
      "sql_on_san": {
        "os_type": "windows_2008",
        "server_cores_count": 8,
        "db": { "size": "5GB", "storage_service": { "name": "value" } },
        "log": { "size": "1GB", "storage_service": { "name": "value" } },
        "temp_db": { "size": "2GB", "storage_service": { "name": "value" } },
        "igroup_name": "igroup_2",
        "new_igroups": [
          {
            "name": "igroup_2",
            "protocol": "mixed",
            "os_type": "windows",
            "initiators": [ "iqn.a.new.initiator" ]
          }
        ],
        "protection_type": { "local_rpo": "none" }
      }
    }
    ```
### Learn more
* [`DOC /application`](#docs-application-overview)
* [`Asynchronous operations`](#Synchronous_and_asynchronous_operations)
"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)

    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["Application"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes an application and all associated data.

### Warning - this deletes it all, including your data
This deletes everything created with the application, including any volumes, LUNs, NFS export policies, CIFS shares, and initiator groups. Initiator groups are only destroyed if they were created as part of an application and are no longer in use by other applications.
### Learn more
* [`DOC /application`](#docs-application-overview)
* [`Asynchronous operations`](#Synchronous_and_asynchronous_operations)
"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves applications.
### Expensive properties
There is an added computational cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more.
* `<template>` the property corresponding to the `template.name` of the application
### Query examples
Numerous queries are available for classifying and sorting applications:
1. Return a list of applications sorted by name.
    ```
    GET /application/applications?order_by=name
    ```
    <br/>
2. Return a list of applications for a specific SVM.
    ```
    GET /application/applications?svm.name=<name>
    ```
    <br/>
3. Return a list of all SQL applications.
    ```
    GET /application/applications?template.name=sql*
    ```
    <br/>
4. Return a list of all applications that can be accessed via SAN.<br/>
    ```
    GET /application/applications?template.protocol=san
    ```
    <br/>
5. Return the top five applications consuming the most IOPS.<br/>
    ```
    GET /application/applications?order_by=statistics.iops.total desc&max_records=5
    ```
<br/>The above examples are not comprehensive. There are many more properties available for queries. Also, multiple queries can be mixed and matched with other query parameters for a large variety of requests. See the per-property documentation below for the full list of supported query parameters.
### Learn more
* [`DOC /application`](#docs-application-overview)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an application
### Expensive properties
There is an added computational cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more.
* `<template>` the property corresponding to the `template.name` of the application
### Property overview
An application includes three main groups or properties.
* Generic properties - such as the `name`, `template.name`, and `state` of the application. These properties are all inexpensive to retrieve and their meaning is consistent for every type of application.
* `statistics.*` - application statistics report live usage data about the application and its components. Various space and IOPS details are included at both the application level and at a per component level. The application model includes a detailed description of each property. These properties are slightly more expensive than the generic properties because live data must be collected from every storage element in the application.
* `<template>` - the property corresponding to the value of the `template.name` returns the contents of the application in the same layout that was used to provision the application. This information is very expensive to retrieve because it requires collecting information about all the storage and access settings for every element of the application. There are a few notable limitations to what can be returned in the `<template>` section:
  * The `new_igroups` array of many SAN templates is not returned by GET. This property allows igroup creation in the same call that creates an application, but is not a property of the application itself. The `new_igroups` array is allowed during PATCH operations, but that does not modify the `new_igroups` of the application. It is another way to allow igroup creation while updating the application to use a different igroup.
  * The `vdi_on_san` and `vdi_on_nas` `desktops.count` property is rounded to the nearest 1000 during creation, and is reported with that rounding applied.
  * The `mongo_db_on_san` `dataset.element_count` property is rounded up to an even number, and is reported with that rounding applied.
  * The `sql_on_san` and `sql_on_smb` `server_cores_count` property is limited to 8 for GET operations. Higher values are accepted by POST, but the impact of the `server_cores_count` property on the application layout currently reaches its limit at 8.
### Learn more
* [`DOC /application`](#docs-application-overview)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates an application.

### Template properties
The application APIs appear to be complex and long in this documentation because we document every possible template, of which there are currently 14. When creating an application, only a single template is used, so it is best to focus only on the template of interest. Other than the properties for the chosen template, only the `name` and `svm` of the application must be provided. The following three sections provided guidelines on using the properties of the templates, but the whole idea behind the templates is to automatically follow the best practices of the given application, so the only way to determine the exact list of required properties and default values is to dig in to the model section of the template. The templates are all top level properties of the application object with names matching the values returned by [`GET /application/templates`](#operations-application-application_template_collection_get).
### Required properties
* `svm.uuid` or `svm.name` - The existing SVM in which to create the application.
* `name` - The name for the application.
* `<template>` - Properties for one template must be provided. In general, the following properties are required, however the naming of these may vary slightly from template to template.
  * `<template>.name` - The generic templates require names for the components of the application. Other templates name the components automatically.
  * `<template>.application_component.size` - This generally refers to the size of an application component, which may be spread across multiple underlying storage objects (volumes, LUNs, etc...).
  * One of the following must be specified:
      * `nas.nfs_access` or an identifier (name or id) of an existing `export-policy`.
      * `nas.cifs_access`
      * `san.application_application.igroup_name`
  * To specify that a NAS application is not to be exposed via NFS nor CIFS:
      * `nas.application_component.export_policy.name` is 'none', and
      * `nas.application.cifs_share_name` is 'none'.
  * The name of the CIFS share can be provided through the `nas.application.cifs_share_name` attribute. If not provided, the CIFS share name will be the same as the `nas.application_component.name` attribute, including any suffix applied due to creating multiple application components in one post.
  * `san.os_type` - All SAN applications require an os_type to be specified in some way. Some templates refer to this as the `hypervisor`.
### Recommended optional properties
* `<template>` - The following properties are available in some templates.
  * `san.new_igroups.*` - SAN applications can use existing initiator groups or create new ones. When creating new initiator groups, `new_igroups.name` is required and the other properties may be used to fully specify the new initiator group.
### Default property values
If not specified in POST, the follow default property values are assigned. It is recommended that most of these properties be provided explicitly rather than relying upon the defaults. The defaults are intended to make it as easy as possible to provision and connect to an application.
* `template.name` - Defaults to match the `<template>` provided. If specified, the value of this property must match the provided template properties.
* `<template>` - The majority of template properties have default values. The defaults may vary from template to template. See the model of each template for complete details. In general the following patterns are common across all template properties. The location of these properties varies from template to template.
  * `<template>.storage_service.name` - _value_
  * `<template>.protection_type.local_rpo` - _hourly_ (Hourly snapshots)
  * `<template>.protection_type.remote_rpo` - _none_ (Not MetroCluster)
  * `san.new_igroups.os_type` - Defaults to match the `os_type` provided for the application, but may need to be provided explicitly when using virtualization.
### Optional components
A common pattern across many templates are objects that are optional, but once any property in the object is specified, other properties within the object become required. Many applications have optional components. For example, provisioning a database without a component to store the logs is supported. If the properties related to the logs are omitted, no storage will be provisioned for logs. But when the additional component is desired, the size is required. Specifying any other property of a component without specifying the size is not supported. In the model of each template, the required components are indicated with a red '*'. When a `size` property is listed as optional, that means the component itself is optional, and the size should be specified to include that component in the application.
### POST body examples
1. Create a generic SAN application that exposes four LUNs to an existing initiator group, _igroup_1_.<br/>
    ```
    {
      "name": "app1",
      "svm": { "name": "svm1" },
      "san": {
        "os_type": "linux",
        "application_components": [
          { "name": "component1", "total_size": "10GB", "lun_count": 4, "igroup_name": "igroup_1" }
        ]
      }
    }
    ```
    <br/>
2. Create an SQL application that can be accessed via initiator _iqn.2017-01.com.example:foo_ from a new initiator group, _igroup_2_.<br/>
    ```
    {
      "name": "app2",
      "svm": { "name": "svm1" },
      "sql_on_san": {
        "db": { "size": "5GB" },
        "log": { "size": "1GB" },
        "temp_db": { "size": "2GB" },
        "igroup_name": "igroup_2",
        "new_igroups": [
          { "name": "igroup_2", "initiators": [ "iqn.2017-01.com.example:foo" ] }
        ]
      }
    }
    ```
    <br/>
3. The following body creates the exact same SQL application, but manually provides all the defaults that were excluded from the previous call. Note: The model of a _sql_on_san_ application documents all these default values.<br/>
    ```
    {
      "name": "app3",
      "svm": { "name": "svm1" },
      "template": { "name": "sql_on_san" },
      "sql_on_san": {
        "os_type": "windows_2008",
        "server_cores_count": 8,
        "db": { "size": "5GB", "storage_service": { "name": "value" } },
        "log": { "size": "1GB", "storage_service": { "name": "value" } },
        "temp_db": { "size": "2GB", "storage_service": { "name": "value" } },
        "igroup_name": "igroup_2",
        "new_igroups": [
          {
            "name": "igroup_2",
            "protocol": "mixed",
            "os_type": "windows",
            "initiators": [ "iqn.a.new.initiator" ]
          }
        ],
        "protection_type": { "local_rpo": "none" }
      }
    }
    ```
### Learn more
* [`DOC /application`](#docs-application-overview)
* [`Asynchronous operations`](#Synchronous_and_asynchronous_operations)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the properties of an application.

### Overview
Similar to creating an application, modification is done using the template properties of an application. The `storage_service`, `size`, and `igroup_name` of an application may be modified.
### `storage_service`
Storage service modifications are processed in place, meaning that the storage can not be moved to a location with more performance headroom to accommodate the request. If the current backing storage of the application is in a location that can support increased performance, the QoS policies associated with the application will be modified to allow it. If not, an error will be returned. A storage service modification to a lower tier of performance is always allowed, but the reverse modification may not be supported if the cluster is over provisioned and the cluster is unlikely to be able to fulfil the original storage service.
### `size`
Size modifications are processed in a variety of ways depending on the type of application. For NAS applications, volumes are grown or new volumes are added. For SAN applications, LUNs are grown, new LUNs are added to existing volumes, or new LUNs are added to new volumes. If new storage elements are created, they can be found using the [`GET /application/applications/{application.uuid}/components`](#operations-application-application_component_collection_get) interface. The creation time of each storage object is included, and the newly created objects will use the same naming scheme as the previous objects. Resize follows the best practices associated with the type of application being expanded. Reducing the size of an application is not supported.
### `igroup_name`
Modification of the igroup name allows an entire application to be mapped from one initiator group to another. Data access will be interrupted as the LUNs are unmapped from the original igroup and remapped to the new one.
### Application state
During a modification, the `state` property of the application updates to indicate `modifying`. In `modifying` state, statistics are not available and snapshot operations are not allowed. If the modification fails, it is possible for the application to be left in an inconsistent state, with the underlying ONTAP storage elements not matching across a component. When this occurs, the application is left in the `modifying` state until the command is either retried and succeeds or a call to restore the original state is successful.
### Examples
1. Change the storage service of the database of the Oracle application to _extreme_ and resize the redo logs to _100GB_.
    ```
    {
      "oracle_on_nfs": {
        "db": {
          "storage_service": {
            "name": "extreme"
          }
        },
        "redo_log": {
          "size": "100GB"
        }
      }
    }
    ```
    <br/>
2. Change the storage service, size, and igroup of a generic application by component name.
    ```
    {
      "san": {
        "application_components": [
          {
            "name": "component1",
            "storage_service": {
              "name": "value"
            }
          },
          {
            "name": "component2",
            "size": "200GB"
          },
          {
            "name": "component3",
            "igroup_name": "igroup5"
          }
        ]
      }
    }
    ```
    <br/>
### Learn more
* [`DOC /application`](#docs-application-overview)
* [`Asynchronous operations`](#Synchronous_and_asynchronous_operations)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes an application and all associated data.

### Warning - this deletes it all, including your data
This deletes everything created with the application, including any volumes, LUNs, NFS export policies, CIFS shares, and initiator groups. Initiator groups are only destroyed if they were created as part of an application and are no longer in use by other applications.
### Learn more
* [`DOC /application`](#docs-application-overview)
* [`Asynchronous operations`](#Synchronous_and_asynchronous_operations)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)


