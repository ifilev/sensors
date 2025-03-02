from sqlalchemy import Column, Integer, Float, DateTime, String
from repository.db import Base
from datetime import datetime


class SensorData(Base):
    """Database entity"""
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    sensor_type = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}