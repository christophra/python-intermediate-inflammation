from inflammation import models
import json


class Serializer:
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


class ObservationSerializer(Serializer):
    model = models.Observation

    @classmethod
    def serialize(cls, instances):
        return [{"day": instance.day,
                 "value": instance.value,
                 } for instance in instances
                ]

    @classmethod
    def deserialize(cls, data):
        # Observation.__init__ kwargs have same names its attributes
        return [cls.model(**object) for object in data]


class PatientSerializer(Serializer):
    model = models.Patient

    @classmethod
    def serialize(cls, instances):
        """Serialize list of patients to list of dicts"""
        return [{'name': instance.name,
                 #'observations': instance.observations, # don't have to serialize this too?
                 'observations': ObservationSerializer.serialize(instance.observations), # => yes :-)
                 } for instance in instances]

    @classmethod
    def save(cls, instances, path):
        raise NotImplementedError

    @classmethod
    def deserialize(cls, data):
        instances = []

        for item in data:
            item['observations'] = ObservationSerializer.deserialize(item.pop('observations'))
            instances.append(cls.model(**item))

        return instances


    @classmethod
    def load(cls, path):
        raise NotImplementedError


class PatientJSONSerializer(PatientSerializer):
    """Serializing patients, now with more JSON"""

    @classmethod
    def save(cls, instances, path):
        with open(path, 'w') as f:
            json.dump(cls.serialize(instances), f)

    @classmethod
    def load(cls, path):
        with open(path) as f:
            data = json.load(f)
        return cls.deserialize(data)
