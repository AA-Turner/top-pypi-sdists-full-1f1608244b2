# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChargebackTaskRequest(Model):
    """ChargebackTaskRequest.

    All required parameters must be populated in order to send to Azure.

    :param comment: Required. Comment to add to the task <span
     class='property-internal'>Required</span>
    :type comment: str
    """

    _validation = {
        'comment': {'required': True},
    }

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
    }

    def __init__(self, *, comment: str, **kwargs) -> None:
        super(ChargebackTaskRequest, self).__init__(**kwargs)
        self.comment = comment
