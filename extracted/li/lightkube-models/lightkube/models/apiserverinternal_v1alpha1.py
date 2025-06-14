# autogenerated module
from typing import List, Optional, TYPE_CHECKING

from ._schema import dataclass, field, DictMixin

if TYPE_CHECKING:   # Fix for pycharm autocompletion https://youtrack.jetbrains.com/issue/PY-54560
    from dataclasses import dataclass, field

from . import meta_v1
from typing import Dict


@dataclass
class ServerStorageVersion(DictMixin):
    r"""An API server instance reports the version it can decode and the version it
      encodes objects to when persisting objects in the backend.

      **parameters**

      * **apiServerID** ``Optional[str]`` - The ID of the reporting API server.
      * **decodableVersions** ``Optional[List[str]]`` - The API server can decode objects encoded in these versions. The
        encodingVersion must be included in the decodableVersions.
      * **encodingVersion** ``Optional[str]`` - The API server encodes the object to this version when persisting it in the
        backend (e.g., etcd).
      * **servedVersions** ``Optional[List[str]]`` - The API server can serve these versions. DecodableVersions must include all
        ServedVersions.
    """
    apiServerID: 'Optional[str]' = None
    decodableVersions: 'Optional[List[str]]' = None
    encodingVersion: 'Optional[str]' = None
    servedVersions: 'Optional[List[str]]' = None


@dataclass
class StorageVersion(DictMixin):
    r"""Storage version of a specific resource.

      **parameters**

      * **spec** ``StorageVersionSpec`` - Spec is an empty spec. It is here to comply with Kubernetes API style.
      * **status** ``StorageVersionStatus`` - API server instances report the version they can decode and the version they
        encode objects to when persisting objects in the backend.
      * **apiVersion** ``Optional[str]`` - APIVersion defines the versioned schema of this representation of an object.
        Servers should convert recognized schemas to the latest internal value, and
        may reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
      * **kind** ``Optional[str]`` - Kind is a string value representing the REST resource this object represents.
        Servers may infer this from the endpoint the client submits requests to.
        Cannot be updated. In CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
      * **metadata** ``Optional[meta_v1.ObjectMeta]`` - The name is <group>.<resource>.
    """
    spec: 'StorageVersionSpec'
    status: 'StorageVersionStatus'
    apiVersion: 'Optional[str]' = None
    kind: 'Optional[str]' = None
    metadata: 'Optional[meta_v1.ObjectMeta]' = None

    def __post_init__(self):
        self.apiVersion = 'internal.apiserver.k8s.io/v1alpha1'
        self.kind = 'StorageVersion'


@dataclass
class StorageVersionCondition(DictMixin):
    r"""Describes the state of the storageVersion at a certain point.

      **parameters**

      * **message** ``str`` - A human readable message indicating details about the transition.
      * **reason** ``str`` - The reason for the condition's last transition.
      * **status** ``str`` - Status of the condition, one of True, False, Unknown.
      * **type** ``str`` - Type of the condition.
      * **lastTransitionTime** ``Optional[meta_v1.Time]`` - Last time the condition transitioned from one status to another.
      * **observedGeneration** ``Optional[int]`` - If set, this represents the .metadata.generation that the condition was set
        based upon.
    """
    message: 'str'
    reason: 'str'
    status: 'str'
    type: 'str'
    lastTransitionTime: 'Optional[meta_v1.Time]' = None
    observedGeneration: 'Optional[int]' = None


@dataclass
class StorageVersionList(DictMixin):
    r"""A list of StorageVersions.

      **parameters**

      * **items** ``List[StorageVersion]`` - Items holds a list of StorageVersion
      * **apiVersion** ``Optional[str]`` - APIVersion defines the versioned schema of this representation of an object.
        Servers should convert recognized schemas to the latest internal value, and
        may reject unrecognized values. More info:
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
      * **kind** ``Optional[str]`` - Kind is a string value representing the REST resource this object represents.
        Servers may infer this from the endpoint the client submits requests to.
        Cannot be updated. In CamelCase. More info:
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
      * **metadata** ``Optional[meta_v1.ListMeta]`` - Standard list metadata. More info:
        https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    items: 'List[StorageVersion]'
    apiVersion: 'Optional[str]' = None
    kind: 'Optional[str]' = None
    metadata: 'Optional[meta_v1.ListMeta]' = None

    def __post_init__(self):
        self.apiVersion = 'internal.apiserver.k8s.io/v1alpha1'
        self.kind = 'StorageVersionList'


StorageVersionSpec = Dict


@dataclass
class StorageVersionStatus(DictMixin):
    r"""API server instances report the versions they can decode and the version they
      encode objects to when persisting objects in the backend.

      **parameters**

      * **commonEncodingVersion** ``Optional[str]`` - If all API server instances agree on the same encoding storage version, then
        this field is set to that version. Otherwise this field is left empty. API
        servers should finish updating its storageVersionStatus entry before serving
        write operations, so that this field will be in sync with the reality.
      * **conditions** ``Optional[List[StorageVersionCondition]]`` - The latest available observations of the storageVersion's state.
      * **storageVersions** ``Optional[List[ServerStorageVersion]]`` - The reported versions per API server instance.
    """
    commonEncodingVersion: 'Optional[str]' = None
    conditions: 'Optional[List[StorageVersionCondition]]' = None
    storageVersions: 'Optional[List[ServerStorageVersion]]' = None


