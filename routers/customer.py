from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from typing import Union
from services.customer import createCustomer
from services.customer import readCustomer
from services.customer import updateCustomer
from services.customer import deleteCustomer


customerRouter = APIRouter(prefix="/customer")

class Customer(BaseModel):
    name:Union[str, None] = None
    age:Union[int, None] = None
    email:Union[EmailStr, None] = None

@customerRouter.post("/create")
async def create_customer(data: Customer):
    return createCustomer(name=data.name, age=data.age, email=data.email)


@customerRouter.get("/read/{customerId}")
async def read_customer(customerId: int):
    return readCustomer(customerId=customerId)


@customerRouter.put("/update/{customerId}")
async def update_customer(customerId: int, data:Customer):
        return updateCustomer(customerId=customerId, name=data.name, age=data.age, email=data.email)


@customerRouter.delete("/delete/{customerId}")
async def delete_customer(customerId: int):
        return deleteCustomer(customerId=customerId)