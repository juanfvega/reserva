from pony.orm import *
from models.databaseManager import DatabaseManager
from fastapi import HTTPException
from datetime import date

@db_session
def createTable(customerId:int, date:date, status:bool):
    customerTable = DatabaseManager.getTable('Customer')
    query = customerTable.select(lambda x: x.id == customerId)
    print("query exists?")
    print(query.exists())
    if query.exists():
        print("query exists")
        customer = query.first()
        table = DatabaseManager.getTable('Table')
        newTable = table(date=date, status=status, customer=customer)
        print("new table is")
        print(newTable)
        return newTable.to_dict()
    else:
        return HTTPException(status_code=404, detail="customer not found")
