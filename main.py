from fastapi import FastAPI
import data_providers.data_generator
from fastapi.middleware.cors import CORSMiddleware
from repository.db import engine, Base
from api.router import router

# Create tables
Base.metadata.create_all(bind=engine)
app = FastAPI()
#data_provider = data_providers.data_generator.DataGenerator()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "ws://localhost:4200", "http://127.0.0.1:4200", "ws://127.0.0.1:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Sensor API is running!"}


app.include_router(router)
