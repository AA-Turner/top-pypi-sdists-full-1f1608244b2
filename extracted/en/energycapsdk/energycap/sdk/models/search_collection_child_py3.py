# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SearchCollectionChild(Model):
    """SearchCollectionChild.

    :param result:
    :type result: ~energycap.sdk.models.SearchCollectionChildSearchCollection
    """

    _attribute_map = {
        'result': {'key': 'result', 'type': 'SearchCollectionChildSearchCollection'},
    }

    def __init__(self, *, result=None, **kwargs) -> None:
        super(SearchCollectionChild, self).__init__(**kwargs)
        self.result = result
