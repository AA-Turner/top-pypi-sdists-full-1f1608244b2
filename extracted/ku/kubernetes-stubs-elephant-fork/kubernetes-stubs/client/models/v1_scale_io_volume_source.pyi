import datetime
import typing

import kubernetes.client

class V1ScaleIOVolumeSource:
    fs_type: typing.Optional[str]
    gateway: str
    protection_domain: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_ref: kubernetes.client.V1LocalObjectReference
    ssl_enabled: typing.Optional[bool]
    storage_mode: typing.Optional[str]
    storage_pool: typing.Optional[str]
    system: str
    volume_name: typing.Optional[str]
    
    def __init__(self, *, fs_type: typing.Optional[str] = ..., gateway: str, protection_domain: typing.Optional[str] = ..., read_only: typing.Optional[bool] = ..., secret_ref: kubernetes.client.V1LocalObjectReference, ssl_enabled: typing.Optional[bool] = ..., storage_mode: typing.Optional[str] = ..., storage_pool: typing.Optional[str] = ..., system: str, volume_name: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1ScaleIOVolumeSourceDict:
        ...
class V1ScaleIOVolumeSourceDict(typing.TypedDict, total=False):
    fsType: typing.Optional[str]
    gateway: str
    protectionDomain: typing.Optional[str]
    readOnly: typing.Optional[bool]
    secretRef: kubernetes.client.V1LocalObjectReferenceDict
    sslEnabled: typing.Optional[bool]
    storageMode: typing.Optional[str]
    storagePool: typing.Optional[str]
    system: str
    volumeName: typing.Optional[str]
