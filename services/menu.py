from pony.orm import *
from models.databaseManager import DatabaseManager

@db_session
def createMenu(tableId:int, name:str, qty:int, price:float):
    menu = DatabaseManager.getTable('Menu')
    newMenu = menu(table=tableId, name=name, qty=qty, price=price)
    return newMenu.to_dict()