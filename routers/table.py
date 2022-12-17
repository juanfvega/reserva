from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date
from services.table import createTable

tableRouter = APIRouter(prefix="/table")

class Table(BaseModel):
    date:date
    status:bool


@tableRouter.post("/create/{customerId}")
async def create_table(customerId:int, data:Table):
    return createTable(customerId=customerId, date=data.date, status=data.status)