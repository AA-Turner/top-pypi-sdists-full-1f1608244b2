# Code generated - EDITING IS FUTILE. DO NOT EDIT.

from json import JSONEncoder as BaseJSONEncoder


class JSONEncoder(BaseJSONEncoder):
    def default(self, obj):
        obj_to_json = getattr(obj, "to_json", None)
        if callable(obj_to_json):
            return obj_to_json()

        return BaseJSONEncoder.default(self, obj)
