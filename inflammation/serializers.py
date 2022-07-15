from inflammation import models


class PatientSerializer:
    model = models.Patient

    @classmethod
    def serialize(cls, instances):
        raise NotImplementedError

    @classmethod
    def save(cls, instances, path):
        raise NotImplementedError

    @classmethod
    def deserialize(cls, data):
        raise NotImplementedError

    @classmethod
    def load(cls, path):
        raise NotImplementedError
