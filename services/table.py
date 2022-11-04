from pony.orm import *
from models.databaseManager import DatabaseManager
from datetime import date

@db_session
def createTable(date:date, status:bool):
    table = DatabaseManager.getTable('Table')
    newTable = table(date=date, status=status)
    return newTable.to_dict()