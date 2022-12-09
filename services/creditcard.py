from pony.orm import *
from models.databaseManager import DatabaseManager
from datetime import date
from fastapi import HTTPException


@db_session
def addCreditCard(number:int, valid:date, bank:str, customerId:int):
    customerCC = DatabaseManager.getTable('Customer')
    query = customerCC.select(lambda x: x.id == customerId)
    try:
        if(query.exists()):
            customer = query.first()
            creditcardt = DatabaseManager.getTable('CreditCard')
            newCreditCard =  creditcardt(number=number, valid=valid, bank=bank, customer=customer)
            return newCreditCard.to_dict()            
    except ValueError:
        return HTTPException(status_code=404, detail="customer not found")