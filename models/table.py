from datetime import date
from pony.orm import *


def getTable(db):

    class Table(db.Entity):
        id = PrimaryKey(int, auto=True)
        date = Optional(date)
        status = Optional(bool)
        ticket = Optional('Ticket')
        customer = Required('Customer')
        menus = Set('Menu')

    return Table