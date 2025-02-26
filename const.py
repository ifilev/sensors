from enum import Enum, auto

class SENSOR_TYPES(Enum):
    temperature = auto()
    humidity = auto()
    vibration = auto()

    @classmethod
    def list(cls):
        return list(cls.__members__)

