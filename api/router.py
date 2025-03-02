from fastapi import APIRouter, Depends, WebSocket
from sqlalchemy.orm import Session
from repository.db import get_db
from typing import List
from models.sensor import Sensor
from repository.queries import get_sensor_data_by_type, get_sensor_data, save_sensor_data
from data_providers.data_generator import DataGenerator
import asyncio
import json

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
            data = get_sensor_data(db)
            json_data = [json.loads(Sensor.model_validate(ent).model_dump_json()) for ent in data]
            await websocket.send_json(json_data)
            await asyncio.sleep(10)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        print("WebSocket connection closed")
