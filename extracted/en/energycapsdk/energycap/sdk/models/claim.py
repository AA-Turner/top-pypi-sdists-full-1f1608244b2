# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Claim(Model):
    """Claim.

    :param claim_type: Type of claim
    :type claim_type: str
    :param value: Claim value
    :type value: str
    """

    _attribute_map = {
        'claim_type': {'key': 'claimType', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Claim, self).__init__(**kwargs)
        self.claim_type = kwargs.get('claim_type', None)
        self.value = kwargs.get('value', None)
