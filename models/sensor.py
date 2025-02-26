from pydantic import BaseModel
from datetime import datetime


class Sensor(BaseModel):
    sensor_type: str
    value: float
    timestamp: datetime
