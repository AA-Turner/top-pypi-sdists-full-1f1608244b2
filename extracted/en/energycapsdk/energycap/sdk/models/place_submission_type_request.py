# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceSubmissionTypeRequest(Model):
    """PlaceSubmissionTypeRequest.

    :param submission_type: The submission type to apply <span
     class='property-internal'>One of Automatic, Manual </span> <span
     class='property-internal'>Required (defined)</span>
    :type submission_type: str
    :param place_ids: The list of places whose submission types will be
     updated <span class='property-internal'>Cannot be Empty</span> <span
     class='property-internal'>Required (defined)</span>
    :type place_ids: list[int]
    """

    _attribute_map = {
        'submission_type': {'key': 'submissionType', 'type': 'str'},
        'place_ids': {'key': 'placeIds', 'type': '[int]'},
    }

    def __init__(self, **kwargs):
        super(PlaceSubmissionTypeRequest, self).__init__(**kwargs)
        self.submission_type = kwargs.get('submission_type', None)
        self.place_ids = kwargs.get('place_ids', None)
