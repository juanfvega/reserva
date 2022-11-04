from pony.orm import *



def getTicket(db):

    class Ticket(db.Entity):
        id = PrimaryKey(int, auto=True)
        total = Optional(float)
        table = Required('Table')

    return Ticket