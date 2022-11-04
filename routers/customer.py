from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from services.customer import createCustomer

customerRouter = APIRouter(prefix="/customer")


class Customer(BaseModel):
    name:str
    age:int
    email:EmailStr

@customerRouter.post("/create")
async def create_customer(data: Customer):
    return createCustomer(name=data.name, age=data.age, email=data.email)