from pony.orm import *
from models.databaseManager import DatabaseManager
from fastapi import HTTPException
from datetime import date

@db_session
def createTable(date:date, status:bool, customerId:int):
    customerTable = DatabaseManager.getTable('Customer')
    query = customerTable.select(lambda x: x.id == customerId)
    try:
        if(query.exists()):
            customer = query.first()
            table = DatabaseManager.getTable('Table')
            newTable = table(date=date, status=status,customer=customer)
            return newTable.to_dict()
    except ValueError:
        return HTTPException(status_code=404, detail="customer not found")
