from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date
from services.table import createTable

tableRouter = APIRouter(prefix="/table")

class Table(BaseModel):
    date:date
    status:bool


@tableRouter.get("/")
async def greet():
    return "hello table"


@tableRouter.post("/create")
async def create_table(data:Table):
    return createTable(date=data.date, status=data.status)