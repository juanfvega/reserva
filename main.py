from fastapi import FastAPI
from models.databaseManager import DatabaseManager
from routers.router import configRouters
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DatabaseManager.connectDatabase()
configRouters(app)

