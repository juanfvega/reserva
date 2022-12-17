from fastapi import APIRouter, UploadFile
from pydantic import BaseModel
from datetime import date
from typing import Union
from services.menu import createMenu


menuRouter = APIRouter(prefix="/menu")


class Menu(BaseModel):
    name:str
    qty:int
    price:float


@menuRouter.post("/create/{tableId}")
async def create_menu(tableId:int, data: Menu):
    return createMenu(tableId=tableId, name=data.name, qty=data.qty, price=data.price)