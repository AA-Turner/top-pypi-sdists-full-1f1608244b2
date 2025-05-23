# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WebhookCreateRequest(Model):
    """WebhookCreateRequest.

    All required parameters must be populated in order to send to Azure.

    :param webhook_name: Required. The name of the webhook <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 64 characters</span>
    :type webhook_name: str
    :param webhook_description: The description for the webhook
    :type webhook_description: str
    :param webhook_event_type_id: Required. The type of event that will
     trigger the webhook <span class='property-internal'>Required</span>
    :type webhook_event_type_id: int
    :param mailing_list: Required. List of email addresses. Each recipient in
     this list will receive an email when a webhook fails or gets disabled
     <span class='property-internal'>Required</span> <span
     class='property-internal'>Cannot be Empty</span>
    :type mailing_list: list[str]
    :param url: Required. The URL to be invoked by the webhook <span
     class='property-internal'>Required</span>
    :type url: str
    :param secret: Required. The encryption secret. <span
     class='property-internal'>Required</span>
    :type secret: str
    """

    _validation = {
        'webhook_name': {'required': True, 'max_length': 64, 'min_length': 0},
        'webhook_event_type_id': {'required': True},
        'mailing_list': {'required': True},
        'url': {'required': True},
        'secret': {'required': True},
    }

    _attribute_map = {
        'webhook_name': {'key': 'webhookName', 'type': 'str'},
        'webhook_description': {'key': 'webhookDescription', 'type': 'str'},
        'webhook_event_type_id': {'key': 'webhookEventTypeId', 'type': 'int'},
        'mailing_list': {'key': 'mailingList', 'type': '[str]'},
        'url': {'key': 'url', 'type': 'str'},
        'secret': {'key': 'secret', 'type': 'str'},
    }

    def __init__(self, *, webhook_name: str, webhook_event_type_id: int, mailing_list, url: str, secret: str, webhook_description: str=None, **kwargs) -> None:
        super(WebhookCreateRequest, self).__init__(**kwargs)
        self.webhook_name = webhook_name
        self.webhook_description = webhook_description
        self.webhook_event_type_id = webhook_event_type_id
        self.mailing_list = mailing_list
        self.url = url
        self.secret = secret
