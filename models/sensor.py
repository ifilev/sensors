from pydantic import BaseModel
from datetime import datetime


class Sensor(BaseModel):
    """Sensor pydantic model"""
    sensor_type: str
    value: float
    timestamp: datetime
