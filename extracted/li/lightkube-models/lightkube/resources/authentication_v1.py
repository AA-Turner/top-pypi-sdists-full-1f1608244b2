# autogenerated module
from typing import ClassVar

from ..core import resource as res
from ..models import authentication_v1 as m_authentication_v1


class SelfSubjectReview(res.GlobalResource, m_authentication_v1.SelfSubjectReview):
    """* **Extends**: ``models.authentication_v1.SelfSubjectReview``
       * **Type**: Global Resource
       * **Accepted client methods**: `create`
    """
    _api_info = res.ApiInfo(
        resource=res.ResourceDef('authentication.k8s.io', 'v1', 'SelfSubjectReview'),
        plural='selfsubjectreviews',
        verbs=['post'],
    )


class TokenReview(res.GlobalResource, m_authentication_v1.TokenReview):
    """* **Extends**: ``models.authentication_v1.TokenReview``
       * **Type**: Global Resource
       * **Accepted client methods**: `create`
    """
    _api_info = res.ApiInfo(
        resource=res.ResourceDef('authentication.k8s.io', 'v1', 'TokenReview'),
        plural='tokenreviews',
        verbs=['post'],
    )

