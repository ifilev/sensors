from unittest.mock import MagicMock


def get_mock_db():
    mock_db = MagicMock()
    return mock_db


# mock data for database queries
def mock_sensor_data():
    from repository.sensor_data_entity import SensorData
    return [
        SensorData(id=1, sensor_type="temperature", value=22.5, timestamp="2025-03-01T12:00:00"),
        SensorData(id=2, sensor_type="vibration", value=51.9, timestamp="2025-03-01T12:00:00"),
    ]


def test_query_get_sensor_data():
    from repository.queries import get_sensor_data
    mock_db = get_mock_db()
    mock_db.query.return_value.order_by.return_value.limit.return_value.all.return_value = mock_sensor_data()

    result = get_sensor_data(mock_db)
    assert isinstance(result, list)
    assert result[0]["sensor_type"] == "temperature" and result[0]["value"] == 22.5
