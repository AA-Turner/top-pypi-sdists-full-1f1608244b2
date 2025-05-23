# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TopmostPlace(Model):
    """TopmostPlace.

    :param is_multi_topmost_place: User's topmost combines multiple places
    :type is_multi_topmost_place: bool
    :param multi_topmost_places:
    :type multi_topmost_places: list[~energycap.sdk.models.PlaceChild]
    :param place_type:
    :type place_type: ~energycap.sdk.models.PlaceTypeResponse
    :param place_id: The place identifier
    :type place_id: int
    :param place_code: The place code
    :type place_code: str
    :param place_info: The place info
    :type place_info: str
    """

    _attribute_map = {
        'is_multi_topmost_place': {'key': 'isMultiTopmostPlace', 'type': 'bool'},
        'multi_topmost_places': {'key': 'multiTopmostPlaces', 'type': '[PlaceChild]'},
        'place_type': {'key': 'placeType', 'type': 'PlaceTypeResponse'},
        'place_id': {'key': 'placeId', 'type': 'int'},
        'place_code': {'key': 'placeCode', 'type': 'str'},
        'place_info': {'key': 'placeInfo', 'type': 'str'},
    }

    def __init__(self, *, is_multi_topmost_place: bool=None, multi_topmost_places=None, place_type=None, place_id: int=None, place_code: str=None, place_info: str=None, **kwargs) -> None:
        super(TopmostPlace, self).__init__(**kwargs)
        self.is_multi_topmost_place = is_multi_topmost_place
        self.multi_topmost_places = multi_topmost_places
        self.place_type = place_type
        self.place_id = place_id
        self.place_code = place_code
        self.place_info = place_info
