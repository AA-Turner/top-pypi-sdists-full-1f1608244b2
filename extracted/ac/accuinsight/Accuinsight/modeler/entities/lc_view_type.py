from Accuinsight.modeler.protos import service_pb2


class ViewType(object):
    """Enum to filter requested experiment types."""
    ACTIVE_ONLY, DELETED_ONLY, ALL = range(1, 4)
    _VIEW_TO_STRING = {
        ACTIVE_ONLY: "active_only",
        DELETED_ONLY: "deleted_only",
        ALL: "all",
    }
    _STRING_TO_VIEW = {value: key for key, value in _VIEW_TO_STRING.items()}

    @classmethod
    def from_string(cls, view_str):
        if view_str not in cls._STRING_TO_VIEW:
            raise Exception(
                "Could not get valid view type corresponding to string %s. "
                "Valid view types are %s" % (view_str, list(cls._STRING_TO_VIEW.keys())))
        return cls._STRING_TO_VIEW[view_str]

    @classmethod
    def to_string(cls, view_type):
        if view_type not in cls._VIEW_TO_STRING:
            raise Exception(
                "Could not get valid view type corresponding to string %s. "
                "Valid view types are %s" % (view_type, list(cls._VIEW_TO_STRING.keys())))
        return cls._VIEW_TO_STRING[view_type]

    @classmethod
    def to_proto(cls, view_type):
        if view_type == cls.ACTIVE_ONLY:
            return service_pb2.ACTIVE_ONLY
        elif view_type == cls.DELETED_ONLY:
            return service_pb2.DELETED_ONLY
        elif view_type == cls.ALL:
            return service_pb2.ALL
        raise ValueError('Unexpected view_type: {}'.format(view_type))

    @classmethod
    def from_proto(cls, proto_view_type):
        if proto_view_type == service_pb2.ACTIVE_ONLY:
            return cls.ACTIVE_ONLY
        elif proto_view_type == service_pb2.DELETED_ONLY:
            return cls.DELETED_ONLY
        elif proto_view_type == service_pb2.ALL:
            return cls.ALL
        raise ValueError('Unexpected proto_view_type: {}'.format(proto_view_type))
