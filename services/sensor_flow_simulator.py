import asyncio
from repository.queries import save_sensor_data
from data_providers.data_generator import DataGenerator


class SensorFlowSimulator:
    """Simulated sensor data generator with a stop mechanism."""

    def __init__(self, session):
        self.db_session = session
        self.stop_event = asyncio.Event()

    async def generate_data_flow(self):
        """Generates and save sensor data to the DB until stopped"""
        print("Start data simulation")
        print(self.stop_event.is_set())
        while not self.stop_event.is_set():
            with self.db_session as session:
                print(session)
                data = DataGenerator.generate_sensor_data()
                print(f"DATA: {data}")
                await save_sensor_data(session, data)
                print("Data saved successfully!")
            await asyncio.sleep(10)

    def stop(self):
        """Stops the data generation loop"""
        self.stop_event.set()