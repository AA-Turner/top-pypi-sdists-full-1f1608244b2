# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FlagEventChild(Model):
    """FlagEventChild.

    :param flag_event_id: The flag event identifier
    :type flag_event_id: int
    :param created_by:
    :type created_by: ~energycap.sdk.models.UserChild
    :param created_date: Date that this flag event was created
    :type created_date: datetime
    :param comment: Comment about the flag event
    :type comment: str
    :param description: Description of the flag event
    :type description: str
    :param flag_action:
    :type flag_action: ~energycap.sdk.models.FlagActionChild
    """

    _attribute_map = {
        'flag_event_id': {'key': 'flagEventId', 'type': 'int'},
        'created_by': {'key': 'createdBy', 'type': 'UserChild'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'comment': {'key': 'comment', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'flag_action': {'key': 'flagAction', 'type': 'FlagActionChild'},
    }

    def __init__(self, *, flag_event_id: int=None, created_by=None, created_date=None, comment: str=None, description: str=None, flag_action=None, **kwargs) -> None:
        super(FlagEventChild, self).__init__(**kwargs)
        self.flag_event_id = flag_event_id
        self.created_by = created_by
        self.created_date = created_date
        self.comment = comment
        self.description = description
        self.flag_action = flag_action
