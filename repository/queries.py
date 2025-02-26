from sqlalchemy.orm import Session
from repository.sensor_data_entity import SensorData


def save_sensor_data(db: Session, data: list):
    for sensor_data in data:
        db.add(sensor_data)
        db.commit()
        db.refresh(sensor_data)


def get_sensor_data(db: Session, limit: int = 10):
    return db.query(SensorData).order_by(SensorData.timestamp.desc()).limit(limit).all()


def get_sensor_data_by_type(sensor_type: str, db: Session, limit: int = 10):
    return db.query(SensorData)\
        .where(SensorData.sensor_type == sensor_type)\
        .order_by(SensorData.timestamp.desc()) \
        .limit(limit)\
        .all()