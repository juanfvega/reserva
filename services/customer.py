from pony.orm import *
from models.databaseManager import DatabaseManager
from pydantic import EmailStr

@db_session
def createCustomer(name:str, age:int, email:EmailStr):
    customer = DatabaseManager.getTable('Customer')
    #table = DatabaseManager.getTable(table)
    newCustomer = customer(name=name, age=age, email=email)
    return newCustomer.to_dict()