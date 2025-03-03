from sqlalchemy.orm import Session
from repository.sensor_data_entity import SensorData


def save_sensor_data(db: Session, data: list):
    """
    Store data into the DB
    :param db: Database session
    :param data: list with sensors data objects
    :return:
    """
    for sensor_data in data:
        db.add(sensor_data)
        db.commit()
        db.refresh(sensor_data)


def get_sensor_data(db: Session, limit: int = 10):
    """
    Fetch data from the DB, by default last 10 records.
    :param db: Database session
    :param limit: Limit the rows pulled from the DB
    :return: list with data entities
    """
    db_rows = db.query(SensorData).order_by(SensorData.timestamp.desc()).limit(limit).all()
    return list(map(
        lambda entity: entity.as_dict(),  # serialize
        db_rows
    ))


def get_sensor_data_by_type(sensor_type: str, db: Session, limit: int = 10):
    """
    Filter by sensor type.
    :param sensor_type:
    :param db: Database session
    :param limit: Limit the rows pulled from the DB
    :return: list with data entities
    """
    db_rows = db.query(SensorData)\
        .where(SensorData.sensor_type == sensor_type)\
        .order_by(SensorData.timestamp.desc()) \
        .limit(limit)\
        .all()
    return list(map(
        lambda entity: entity.as_dict(),  # serialize
        db_rows
    ))