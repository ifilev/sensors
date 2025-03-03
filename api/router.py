from fastapi import APIRouter, Depends, WebSocket
from sqlalchemy.orm import Session
from repository.db import get_db
from typing import List
from models.sensor import Sensor
from repository.queries import get_sensor_data_by_type, get_sensor_data, save_sensor_data
from data_providers.data_generator import DataGenerator
import asyncio
import json
import logging

router = APIRouter()
data_provider = DataGenerator()
logger = logging.getLogger("sensors-fastapi")


@router.get("/sensor_data", response_model=List[Sensor])
def fetch_sensor_data(sensor: str = None, db: Session = Depends(get_db)):
    """
    Returns the last 10 records from the DB. You can filter by sensor_type,
    passing the 'sensor' param.
    :param sensor: Optional. Sensor type could be ["temperature", "vibration, "humidity"]
    :param db: Database session
    :return: List with sensors data objects
    """
    if sensor:
        return get_sensor_data_by_type(sensor, db)
    else:
        return get_sensor_data(db)


@router.websocket("/realtime")
async def get_sensors_realtime(websocket: WebSocket, db: Session = Depends(get_db)):
    """
    Handles WebSocket connection. Generates sensors data, stores it in the DB
    and pulls the last 10 records from the DB and transmit the data via the WebSocket
    every 10 seconds.
    :param websocket: WebSocket
    :param db: Database session
    :return: None
    """
    await websocket.accept()
    try:
        while True:
            # Generates sensors data and stores it in the DB
            save_sensor_data(db, data_provider.fetch_data())
            # get last 10 records from the DB
            data = get_sensor_data(db)
            # covert the DB entity into a json
            json_data = [json.loads(Sensor.model_validate(ent).model_dump_json()) for ent in data]
            await websocket.send_json(json_data)
            await asyncio.sleep(10)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
    finally:
        logger.info("WebSocket connection closed")
