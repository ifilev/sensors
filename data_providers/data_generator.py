import random
from const import SENSOR_TYPES
from data_providers.base_provider import BaseProvider
from repository.sensor_data_entity import SensorData
from typing import List


class DataGenerator(BaseProvider):
    """Simulates sensor data"""

    def fetch_data(self):
        return self.generate_sensor_data()

    @classmethod
    def generate_sensor_data(cls) -> List[SensorData]:
        """Generates the numbers for every sensor we have in the list with sensor types"""
        data = []
        for sensor in SENSOR_TYPES:
            value = round(random.uniform(20, 30), 1) if sensor.name == "temperature" else round(random.uniform(30, 60), 2)
            data.append(SensorData(sensor_type=sensor.name, value=value))
        return data
