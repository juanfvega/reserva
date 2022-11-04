from pony.orm import * 



def getMenu(db):
    
    class Menu(db.Entity):
        id = PrimaryKey(int, auto=True)
        table = Required('Table')
        name = Optional(str)
        qty = Optional(int, unsigned=True)
        price = Optional(float)
        photo = Optional(buffer)
    
    return Menu