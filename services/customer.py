from pony.orm import *
from models.databaseManager import DatabaseManager
from pydantic import EmailStr
from fastapi import HTTPException
from typing import Union

@db_session
def createCustomer(name:str, age:int, email:EmailStr):
    customer = DatabaseManager.getTable('Customer')
    #table = DatabaseManager.getTable(table)
    newCustomer = customer(name=name, age=age, email=email)
    return newCustomer.to_dict()


@db_session
def readCustomer(customerId:int):
    customer = DatabaseManager.getTable('Customer')
    query = select(c for c in customer if c.id == customerId)
    
    if(query.exists()):
        return query.first().to_dict()
    else:
        return HTTPException(status_code=404, detail='Customer not found')


@db_session
def updateCustomer(customerId:int, name:Union[str, None], age:Union[int, None], email:Union[EmailStr, None]):
    customer = DatabaseManager.getTable('Customer')
    query = select(c for c in customer if c.id == customerId)
    if(query.exists()):        
        customerObj = query.first()
        if name:
            print('in name')
            customerObj.name = name
        if age:
            print('in age')
            customerObj.age = age
        if email: 
            print('in email')
            customerObj.email = email
        
        return customerObj.to_dict()
    else:
        return HTTPException(status_code=404, detail='Customer not found')
        

@db_session
def deleteCustomer(customerId: int):
    customer = DatabaseManager.getTable('Customer')
    query = select(c for c in customer if c.id == customerId)
    if query.exists():
        customerDeleted = query.first()
        customerDeleted.delete()
        return customerDeleted.id
    else:
        return HTTPException(status_code=404, detail='Customer not found')
    