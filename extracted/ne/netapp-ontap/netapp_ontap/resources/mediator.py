r"""
Copyright &copy; 2024 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
You can use this API to add or remove a mediator to MetroCluster over IP configuration, or get the status and details of the existing mediator in MetroCluster over IP configuration. The GET operation returns the status of the mediator along with the mediator details. The DELETE operation removes the mediator. The POST operation adds the mediator.
## Adding a mediator
A mediator can be added to MetroCluster over IP configuration by issuing a POST on /cluster/mediators. Parameters are provided in the body of the POST request. There are no optional parameters for adding a mediator.
### Required configuration fields
These fields are always required for any POST /cluster/mediators request.

* `ip_address`         - Specifies the IP address of the mediator.
* `user`               - Specifies a user name credential.
* `password`           - Specifies a password credential.
### Polling the setup job
After a successful POST /cluster/mediators is issued, an HTTP status code of 202 (Accepted) is returned along with a job UUID and a link in the body of the response. The setup job continues asynchronously and can be monitored by using the job UUID and the /cluster/jobs API. The "message" field in the response of the GET /cluster/jobs/{uuid} request shows the current step in the job, and the "state" field shows the overall state of the job.
## Deleting a Mediator
A mediator can be deleted from MetroCluster over IP configuration by issuing a DELETE to /cluster/mediators/{uuid}. Parameters are provided in the body of the DELETE request. There are no optional parameters for adding a mediator.
### Required configuration fields
These fields are always required for any DELETE /cluster/mediators/{uuid} request.

* `user`               - Specifies a user name credential.
* `password`           - Specifies a password credential.
### Polling the delete job
After a successful DELETE /cluster/mediators/{uuid} is issued, an HTTP status code of 202 (Accepted) is returned along with a job UUID and a link in the body of the response. The delete job continues asynchronously and can be monitored by using the job UUID and the /cluster/jobs API. The "message" field in the response of the GET /cluster/jobs/{uuid} request shows the current step in the job, and the "state" field shows the overall state of the job.
<br/>
---
## Examples
### Setting up a mediator for a 4-Node MetroCluster over IP Configuration
This example shows the POST body when setting up a mediator for a 4-Node MetroCluster over IP configuration. The only prerequisite is that MetroCluster over IP is configured.
```
# API
/api/cluster/mediators
```
### POST body included from file
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Mediator

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Mediator()
    resource.ip_address = "1.1.1.1"
    resource.user = "username"
    resource.password = "password"
    resource.post(hydrate=True)
    print(resource)

```

### Inline POST body
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Mediator

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Mediator()
    resource.ip_address = "1.1.1.1"
    resource.user = "username"
    resource.password = "password"
    resource.post(hydrate=True)
    print(resource)

```

### POST Response
```
HTTP/1.1 202 Accepted
Date: Tue, 22 Sep 2020 07:40:59 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/cluster/metrocluster
Content-Length: 189
Content-Type: application/hal+json
{
  "job": {
    "uuid": "f567b48b-fca6-11ea-acaf-005056bb47c1",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/f567b48b-fca6-11ea-acaf-005056bb47c1"
      }
    }
  }
}
```
### Monitoring the job progress
Use the link provided in the response to the POST request to fetch information for the mediator setup job.
<br/>
#### Request
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Job

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Job(uuid="f567b48b-fca6-11ea-acaf-005056bb47c1")
    resource.get()
    print(resource)

```

<br/>
#### Job status response
```
HTTP/1.1 202 Accepted
Date: Tue, 22 Sep 2020 07:41:29 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/cluster/metrocluster
Content-Length: 189
Content-Type: application/hal+json
{
  "uuid": "f567b48b-fca6-11ea-acaf-005056bb47c1",
  "description": "POST /api/cluster/mediators/",
  "state": "running",
  "start_time": "2020-09-22T03:41:00-04:00",
  "_links": {
    "self": {
      "href": "/api/cluster/jobs/f567b48b-fca6-11ea-acaf-005056bb47c1"
    }
  }
}
```
#### Final status of a successful Mediator add
```
HTTP/1.1 202 Accepted
Date: Tue, 22 Sep 2020 07:43:38 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/cluster/metrocluster
Content-Length: 358
Content-Type: application/hal+json
{
  "uuid": "f567b48b-fca6-11ea-acaf-005056bb47c1",
  "description": "POST /api/cluster/mediators/",
  "state": "success",
  "message": "success",
  "code": 0,
  "start_time": "2020-09-22T03:41:00-04:00",
  "end_time": "2020-09-22T03:42:10-04:00",
  "_links": {
    "self": {
      "href": "/api/cluster/jobs/f567b48b-fca6-11ea-acaf-005056bb47c1"
    }
  }
}
```
### Retrieving the existing mediator configurations
#### Request
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Mediator

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(Mediator.get_collection()))

```

<br/>
#### Response
```
HTTP/1.1 202 Accepted
Date: Tue, 22 Sep 2020 08:53:18 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/cluster/metrocluster
Content-Length: 320
Content-Type: application/hal+json
{
  "records": [
    {
      "uuid": "f89e8906-fca6-11ea-acaf-005056bb47c1",
      "_links": {
        "self": {
          "href": "/api/cluster/mediators/f89e8906-fca6-11ea-acaf-005056bb47c1"
        }
      }
    }
  ],
  "num_records": 1,
  "_links": {
    "self": {
      "href": "/api/cluster/mediators"
    }
  }
}
```
### Retrieving a specific mediator using the uuid
#### Request
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Mediator

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Mediator(uuid="f89e8906-fca6-11ea-acaf-005056bb47c1")
    resource.get()
    print(resource)

```

<br/>
#### Response
```
HTTP/1.1 202 Accepted
Date: Tue, 22 Sep 2020 08:59:40 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/cluster/metrocluster
Content-Length: 347
Content-Type: application/hal+json
{
  "uuid": "f89e8906-fca6-11ea-acaf-005056bb47c1",
  "ip_address": "10.234.173.40",
  "port": 31784,
  "reachable": true,
  "peer_cluster": {
    "name": "mcc_siteB",
    "uuid": "38779fd1-fc6b-11ea-9421-005056bb21d8"
  },
  "peer_mediator_connectivity": "connected",
  "_links": {
    "self": {
      "href": "/api/cluster/mediators/f89e8906-fca6-11ea-acaf-005056bb47c1"
    }
  }
}
```
### Deleting a configured Mediator using the uuid
#### Request
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Mediator

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Mediator(uuid="{uuid}")
    resource.delete(body={"user": "username", "password": "password"})

```

#### Response
```
HTTP/1.1 202 Accepted
Date: Tue, 22 Sep 2020 09:13:52 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/cluster/metrocluster
Content-Length: 189
Content-Type: application/hal+json
{
  "job": {
    "uuid": "eeb71ccd-fcb3-11ea-acaf-005056bb47c1",
    "_links": {
      "self": {
        "href": "/api/cluster/jobs/eeb71ccd-fcb3-11ea-acaf-005056bb47c1"
      }
    }
  }
}
```
### Monitoring the job progress
Use the link provided in the response to the DELETE request to fetch information for the delete job.
<br/>
#### Request
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Job

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Job(uuid="eeb71ccd-fcb3-11ea-acaf-005056bb47c1")
    resource.get()
    print(resource)

```

#### Job status response
```
HTTP/1.1 202 Accepted
Date: Tue, 22 Sep 2020 09:14:20 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/cluster/metrocluster
Content-Length: 316
Content-Type: application/hal+json
{
  "uuid": "eeb71ccd-fcb3-11ea-acaf-005056bb47c1",
  "description": "DELETE /api/cluster/mediators/f89e8906-fca6-11ea-acaf-005056bb47c1",
  "state": "running",
  "start_time": "2020-09-22T05:13:52-04:00",
  "_links": {
    "self": {
      "href": "/api/cluster/jobs/eeb71ccd-fcb3-11ea-acaf-005056bb47c1"
    }
  }
}
```
#### Final status of the Mediator DELETE job
```
HTTP/1.1 202 Accepted
Date: Tue, 22 Sep 2020 09:21:46 GMT
Server: libzapid-httpd
X-Content-Type-Options: nosniff
Cache-Control: no-cache,no-store,must-revalidate
Location: /api/cluster/metrocluster
Content-Length: 396
Content-Type: application/hal+json
{
  "uuid": "eeb71ccd-fcb3-11ea-acaf-005056bb47c1",
  "description": "DELETE /api/cluster/mediators/f89e8906-fca6-11ea-acaf-005056bb47c1",
  "state": "success",
  "message": "success",
  "code": 0,
  "start_time": "2020-09-22T05:13:52-04:00",
  "end_time": "2020-09-22T05:14:24-04:00",
  "_links": {
    "self": {
      "href": "/api/cluster/jobs/eeb71ccd-fcb3-11ea-acaf-005056bb47c1"
    }
  }
}
```"""

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


__all__ = ["Mediator", "MediatorSchema"]
__pdoc__ = {
    "MediatorSchema.resource": False,
    "MediatorSchema.opts": False,
}


class MediatorSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Mediator object"""

    ca_certificate = marshmallow_fields.Str(
        data_key="ca_certificate",
        allow_none=True,
    )
    r""" CA certificate for ONTAP Mediator. This is optional if the certificate is already installed."""

    dr_group = marshmallow_fields.Nested("netapp_ontap.resources.metrocluster_dr_group.MetroclusterDrGroupSchema", data_key="dr_group", unknown=EXCLUDE, allow_none=True)
    r""" The dr_group field of the mediator."""

    ip_address = marshmallow_fields.Str(
        data_key="ip_address",
        allow_none=True,
    )
    r""" The IP address of the mediator.

Example: 10.10.10.7"""

    password = marshmallow_fields.Str(
        data_key="password",
        allow_none=True,
    )
    r""" The password used to connect to the REST server on the mediator.

Example: mypassword"""

    peer_cluster = marshmallow_fields.Nested("netapp_ontap.resources.cluster_peer.ClusterPeerSchema", data_key="peer_cluster", unknown=EXCLUDE, allow_none=True)
    r""" The peer_cluster field of the mediator."""

    peer_mediator_connectivity = marshmallow_fields.Str(
        data_key="peer_mediator_connectivity",
        allow_none=True,
    )
    r""" Indicates the mediator connectivity status of the peer cluster. Possible values are connected, unreachable, unknown.

Example: connected"""

    port = Size(
        data_key="port",
        allow_none=True,
    )
    r""" The REST server's port number on the mediator.

Example: 31784"""

    reachable = marshmallow_fields.Boolean(
        data_key="reachable",
        allow_none=True,
    )
    r""" Indicates the connectivity status of the mediator.

Example: true"""

    user = marshmallow_fields.Str(
        data_key="user",
        allow_none=True,
    )
    r""" The username used to connect to the REST server on the mediator.

Example: myusername"""

    uuid = marshmallow_fields.Str(
        data_key="uuid",
        allow_none=True,
    )
    r""" The unique identifier for the mediator service."""

    @property
    def resource(self):
        return Mediator

    gettable_fields = [
        "ip_address",
        "peer_cluster.links",
        "peer_cluster.name",
        "peer_cluster.uuid",
        "peer_mediator_connectivity",
        "port",
        "reachable",
        "uuid",
    ]
    """ip_address,peer_cluster.links,peer_cluster.name,peer_cluster.uuid,peer_mediator_connectivity,port,reachable,uuid,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
        "ca_certificate",
        "ip_address",
        "password",
        "peer_cluster.name",
        "peer_cluster.uuid",
        "port",
        "user",
    ]
    """ca_certificate,ip_address,password,peer_cluster.name,peer_cluster.uuid,port,user,"""

class Mediator(Resource):
    r""" Mediator information """

    _schema = MediatorSchema
    _path = "/api/cluster/mediators"
    _keys = ["uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r""""Retrieves a Mediator configured in the cluster."
### Related ONTAP commands
* `storage iscsi-initiator show`

### Learn more
* [`DOC /cluster/mediators`](#docs-cluster-cluster_mediators)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all Mediator resources that match the provided query"""
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
        """Returns a list of RawResources that represent Mediator resources that match the provided query"""
        return super()._get_collection(
            *args, connection=connection, max_records=max_records, raw=True, **kwargs
        )

    fast_get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)


    @classmethod
    def post_collection(
        cls,
        records: Iterable["Mediator"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["Mediator"], NetAppResponse]:
        r"""Creates and connect a mediator.
### Learn more
* [`DOC /cluster/mediators`](#docs-cluster-cluster_mediators)"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)

    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["Mediator"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes the mediator.
### Learn more
* [`DOC /cluster/mediators`](#docs-cluster-cluster_mediators)"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r""""Retrieves a Mediator configured in the cluster."
### Related ONTAP commands
* `storage iscsi-initiator show`

### Learn more
* [`DOC /cluster/mediators`](#docs-cluster-cluster_mediators)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r""""Retrieves the Mediator state and configuration."
### Related ONTAP commands
* `storage iscsi-initiator show`

### Learn more
* [`DOC /cluster/mediators`](#docs-cluster-cluster_mediators)"""
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
        r"""Creates and connect a mediator.
### Learn more
* [`DOC /cluster/mediators`](#docs-cluster-cluster_mediators)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)


    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes the mediator.
### Learn more
* [`DOC /cluster/mediators`](#docs-cluster-cluster_mediators)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)


