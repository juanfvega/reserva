from pony.orm import *

db = Database()

def getTicket():

    class Ticket(db.Entity):
        id = PrimaryKey(int, auto=True)
        total = Optional(float)
        table = Required('Table')

    return Ticket