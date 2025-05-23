# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SubmissionTypeResponse(Model):
    """SubmissionTypeResponse.

    :param submission_type_id: The identifier for the submission type
    :type submission_type_id: int
    :param submission_type_name: The name of the submission type
    :type submission_type_name: str
    """

    _attribute_map = {
        'submission_type_id': {'key': 'submissionTypeId', 'type': 'int'},
        'submission_type_name': {'key': 'submissionTypeName', 'type': 'str'},
    }

    def __init__(self, *, submission_type_id: int=None, submission_type_name: str=None, **kwargs) -> None:
        super(SubmissionTypeResponse, self).__init__(**kwargs)
        self.submission_type_id = submission_type_id
        self.submission_type_name = submission_type_name
