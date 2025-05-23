from rest_framework.reverse import reverse

from wbcore.contrib.documents.models import ShareableLinkAccess
from wbcore.metadata.configs.endpoints import EndpointViewConfig


class ShareableLinkEndpointConfig(EndpointViewConfig):
    def get_list_endpoint(self, **kwargs):
        base_url = "wbcore:documents:link-list"

        if doc_id := self.request.GET.get("document", None):
            return f"{reverse(base_url, request=self.request)}?document={doc_id}"

        return reverse(base_url, request=self.request)

    def get_create_endpoint(self, **kwargs):
        base_url = "wbcore:documents:link-list"

        if doc_id := self.request.GET.get("document", None):
            return f"{reverse(base_url, request=self.request)}?document={doc_id}"

        return reverse(base_url, request=self.request)

    def get_delete_endpoint(self, **kwargs):
        try:
            if ShareableLinkAccess.objects.filter(shareable_link=self.view.get_object()).exists():
                return None
        except AssertionError:
            pass
        return self.get_endpoint()


class ShareableLinkAccessEndpointConfig(EndpointViewConfig):
    def get_list_endpoint(self, **kwargs):
        base_url = "wbcore:documents:linkaccess-list"

        if link_id := self.request.GET.get("shareable_link", None):
            return f"{reverse(base_url, request=self.request)}?shareable_link={link_id}"

        return reverse(base_url, request=self.request)

    def get_create_endpoint(self, **kwargs):
        return None

    def get_instance_endpoint(self, **kwargs):
        return None
