from fastapi import FastAPI
import data_providers.data_generator
from repository.db import engine, Base
from api.router import router

# Create tables
Base.metadata.create_all(bind=engine)
app = FastAPI()
#data_provider = data_providers.data_generator.DataGenerator()


@app.get("/")
def read_root():
    return {"message": "Sensor API is running!"}


app.include_router(router)
