# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ShareRequest(Model):
    """ShareRequest.

    All required parameters must be populated in order to send to Azure.

    :param shared_with_everyone: Required. Set to True to share the item
     everyone
     When true, SharedUsers and SharedUserGroups should be set to empty lists
     [] <span class='property-internal'>Required</span>
    :type shared_with_everyone: bool
    :param shared_user_ids: Required. The list of individual user ids an item
     should be shared with
     Should be an empty list [], when SharedWithEveryone is true <span
     class='property-internal'>Required</span>
    :type shared_user_ids: list[int]
    :param shared_user_group_ids: Required. The list of user group ids an item
     should be shared with
     Should be an empty list [], when SharedWithEveryone is true <span
     class='property-internal'>Required</span>
    :type shared_user_group_ids: list[int]
    """

    _validation = {
        'shared_with_everyone': {'required': True},
        'shared_user_ids': {'required': True},
        'shared_user_group_ids': {'required': True},
    }

    _attribute_map = {
        'shared_with_everyone': {'key': 'sharedWithEveryone', 'type': 'bool'},
        'shared_user_ids': {'key': 'sharedUserIds', 'type': '[int]'},
        'shared_user_group_ids': {'key': 'sharedUserGroupIds', 'type': '[int]'},
    }

    def __init__(self, *, shared_with_everyone: bool, shared_user_ids, shared_user_group_ids, **kwargs) -> None:
        super(ShareRequest, self).__init__(**kwargs)
        self.shared_with_everyone = shared_with_everyone
        self.shared_user_ids = shared_user_ids
        self.shared_user_group_ids = shared_user_group_ids
