from Accuinsight.modeler.entities._modeler_object import _ModelerObject
from Accuinsight.modeler.protos.service_pb2 import Metric as ProtoMetric


class Metric(_ModelerObject):
    """
    Metric object.
    """

    def __init__(self, key, value, timestamp, step):
        self._key = key
        self._value = value
        self._timestamp = timestamp
        self._step = step

    @property
    def key(self):
        """String key corresponding to the metric name."""
        return self._key

    @property
    def value(self):
        """Float value of the metric."""
        return self._value

    @property
    def timestamp(self):
        """Metric timestamp as an integer (milliseconds since the Unix epoch)."""
        return self._timestamp

    @property
    def step(self):
        """Integer metric step (x-coordinate)."""
        return self._step

    def to_proto(self):
        metric = ProtoMetric()
        metric.key = self.key
        metric.value = self.value
        metric.timestamp = self.timestamp
        metric.step = self.step
        return metric

    @classmethod
    def from_proto(cls, proto):
        return cls(proto.key, proto.value, proto.timestamp, proto.step)
