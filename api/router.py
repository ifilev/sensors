from fastapi import APIRouter, Depends, WebSocket
from sqlalchemy.orm import Session
from repository.db import get_db
from typing import List
from models.sensor import Sensor
from repository.queries import get_sensor_data_by_type, get_sensor_data, save_sensor_data
from data_providers.data_generator import DataGenerator
from time import sleep

router = APIRouter()
data_provider = DataGenerator()


@router.get("/sensor_data", response_model=List[Sensor])
def fetch_sensor_data(sensor: str = None, db: Session = Depends(get_db)):
    if sensor:
        return get_sensor_data_by_type(sensor, db)
    else:
        return get_sensor_data(db)


@router.websocket("/realtime")
async def get_sensors_realtime(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    try:
        while True:
            save_sensor_data(db, data_provider.fetch_data())
            r = await websocket.receive_text()
            data = get_sensor_data(db)
            await websocket.send_json(dict(data))
            sleep(10)
    except:
        return
