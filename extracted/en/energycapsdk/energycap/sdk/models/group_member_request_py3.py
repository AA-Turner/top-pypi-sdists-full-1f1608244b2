# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GroupMemberRequest(Model):
    """GroupMemberRequest.

    All required parameters must be populated in order to send to Azure.

    :param include_in_charts: Required. The flag determining whether the
     member is included in group charts <span
     class='property-internal'>Required</span>
    :type include_in_charts: bool
    """

    _validation = {
        'include_in_charts': {'required': True},
    }

    _attribute_map = {
        'include_in_charts': {'key': 'includeInCharts', 'type': 'bool'},
    }

    def __init__(self, *, include_in_charts: bool, **kwargs) -> None:
        super(GroupMemberRequest, self).__init__(**kwargs)
        self.include_in_charts = include_in_charts
