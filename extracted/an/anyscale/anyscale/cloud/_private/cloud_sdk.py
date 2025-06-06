from typing import List, Optional

from anyscale._private.sdk.base_sdk import BaseSDK
from anyscale.client.openapi_client.models import (
    Cloud as CloudModel,
    CreateCloudCollaborator as CreateCloudCollaboratorModel,
)
from anyscale.cloud.models import (
    Cloud,
    CloudProvider,
    ComputeStack,
    CreateCloudCollaborator,
)


class PrivateCloudSDK(BaseSDK):
    def add_collaborators(
        self, cloud: str, collaborators: List[CreateCloudCollaborator]
    ) -> None:
        cloud_id = self.client.get_cloud_id(cloud_name=cloud, compute_config_id=None)

        self.client.add_cloud_collaborators(
            cloud_id=cloud_id,
            collaborators=[
                CreateCloudCollaboratorModel(
                    email=collaborator.email,
                    permission_level=collaborator.permission_level.lower(),
                )
                for collaborator in collaborators
            ],
        )

    def get(
        self, id: Optional[str], name: Optional[str],  # noqa: A002
    ) -> Optional[Cloud]:
        if (id and name) or (not id and not name):
            raise ValueError("Provide exactly one of 'id' or 'name'.")

        if id:
            openapi_cloud = self.client.get_cloud(cloud_id=id)
        else:
            assert name is not None, "Name must be provided if id is not."
            openapi_cloud = self.client.get_cloud_by_name(name=name)

        return self._to_sdk_cloud(openapi_cloud)

    def get_default(self) -> Optional[Cloud]:
        openapi_cloud = self.client.get_default_cloud()

        return self._to_sdk_cloud(openapi_cloud)

    def _to_sdk_cloud(self, openapi_cloud: Optional["CloudModel"]) -> Optional[Cloud]:
        if openapi_cloud is None:
            return None

        # Validate provider, default to UNKNOWN if validation fails
        if openapi_cloud.provider is not None:
            try:
                provider = CloudProvider.validate(openapi_cloud.provider)
            except ValueError:
                provider = CloudProvider.UNKNOWN
        else:
            provider = CloudProvider.UNKNOWN

        # Validate compute_stack, default to UNKNOWN if validation fails
        if openapi_cloud.compute_stack is not None:
            try:
                compute_stack = ComputeStack.validate(openapi_cloud.compute_stack)
            except ValueError:
                compute_stack = ComputeStack.UNKNOWN
        else:
            compute_stack = ComputeStack.UNKNOWN

        return Cloud(
            id=openapi_cloud.id,
            name=openapi_cloud.name,
            provider=provider,
            region=openapi_cloud.region,
            created_at=openapi_cloud.created_at,
            is_default=openapi_cloud.is_default,
            compute_stack=compute_stack,
        )
