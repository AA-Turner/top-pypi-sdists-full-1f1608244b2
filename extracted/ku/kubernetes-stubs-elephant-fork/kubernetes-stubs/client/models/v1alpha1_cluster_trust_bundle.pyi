import datetime
import typing

import kubernetes.client

class V1alpha1ClusterTrustBundle:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1alpha1ClusterTrustBundleSpec
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ..., spec: kubernetes.client.V1alpha1ClusterTrustBundleSpec) -> None:
        ...
    def to_dict(self) -> V1alpha1ClusterTrustBundleDict:
        ...
class V1alpha1ClusterTrustBundleDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    spec: kubernetes.client.V1alpha1ClusterTrustBundleSpecDict
