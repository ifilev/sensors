from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from repository.db import engine, Base
from api.router import router
import logging
from os import path
from datetime import datetime

# Create the tables
Base.metadata.create_all(bind=engine)
app = FastAPI()

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - [%(levelname)s]: %(message)s")
logger = logging.getLogger("sensors-fastapi")
logger.addHandler(logging.StreamHandler())
logger.addHandler(
    logging.FileHandler(path.join('logs', f"{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.log"))
)

# handle CORS policies
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
