from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date 
from services.creditcard import addCreditCard

creditCardRouter = APIRouter(prefix="/creditcard")

class CreditCard(BaseModel):
    number:int
    valid:date
    bank:str

@creditCardRouter.post("/add/{customerId}")
async def add_CreditCard(data: CreditCard, customerId:int):
    return addCreditCard(number=data.number, valid=data.valid, bank=data.bank, customerId=customerId)

