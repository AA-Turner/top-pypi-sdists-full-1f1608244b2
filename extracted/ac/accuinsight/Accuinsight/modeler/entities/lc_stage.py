from Accuinsight.modeler.entities.lc_view_type import ViewType
from Accuinsight.modeler.exceptions import ModelerException


class LifecycleStage(object):
    ACTIVE = "active"
    DELETED = "deleted"
    _VALID_STAGES = set([ACTIVE, DELETED])

    @classmethod
    def view_type_to_stages(cls, view_type=ViewType.ALL):
        stages = []
        if view_type == ViewType.ACTIVE_ONLY or view_type == ViewType.ALL:
            stages.append(cls.ACTIVE)
        if view_type == ViewType.DELETED_ONLY or view_type == ViewType.ALL:
            stages.append(cls.DELETED)
        return stages

    @classmethod
    def is_valid(cls, lifecycle_stage):
        return lifecycle_stage in cls._VALID_STAGES

    @classmethod
    def matches_view_type(cls, view_type, lifecycle_stage):
        if not cls.is_valid(lifecycle_stage):
            raise ModelerException("Invalid lifecycle stage '%s'" % str(lifecycle_stage))

        if view_type == ViewType.ALL:
            return True
        elif view_type == ViewType.ACTIVE_ONLY:
            return lifecycle_stage == LifecycleStage.ACTIVE
        elif view_type == ViewType.DELETED_ONLY:
            return lifecycle_stage == LifecycleStage.DELETED
        else:
            raise ModelerException("Invalid view type '%s'" % str(view_type))
