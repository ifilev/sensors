import pytest
from fastapi.testclient import TestClient
from main import app
from unittest.mock import MagicMock
import json

client = TestClient(app)


# Mock Database Session
def get_mock_db():
    mock_db = MagicMock()
    return mock_db


# Test root endpoint
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Sensor API is running!" in response.json()["message"]


# Test fetching sensor data
def test_get_sensor_data():
    response = client.get("/sensor_data")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# test WebSocket connection
@pytest.mark.asyncio
async def test_websocket():
    async with client.websocket_connect("/ws") as websocket:

        # Receive a message from the WebSocket
        data = await websocket.receive_text()
        response = json.loads(data)

        assert "sensor_type" in response
        assert "value" in response
        assert "timestamp" in response