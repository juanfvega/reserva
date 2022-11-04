from pony.orm import *


def getCustomer(db):

    class Customer(db.Entity):
        id = PrimaryKey(int, auto=True)
        name = Required(str)
        age = Required(int, unsigned=True)
        email = Optional(str)
        credit_cards = Set('CreditCard')
        tables = Set('Table')

    return Customer