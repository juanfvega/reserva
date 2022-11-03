from pony.orm import *
from datetime import date

db = Database()

def getCreditCard():
    
    class CreditCard(db.Entity):
        id = PrimaryKey(int, auto=True)
        number = Optional(int, unique=True, unsigned=True)
        valid = Optional(date)
        bank = Optional(str)
        customer = Required('Customer')

    return CreditCard