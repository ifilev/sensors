from abc import ABC, abstractmethod
from typing import List
from repository.sensor_data_entity import SensorData


class BaseProvider(ABC):
    """Abstract base class for data providers"""

    @abstractmethod
    async def fetch_data(self) -> List[SensorData]:
        """Returns the sensor data from generator or real world source"""
        pass