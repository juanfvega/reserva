from pony.orm import Database
from models.customer import getCustomer
from models.creditcard import getCreditCard
from models.menu import getMenu
from models.table import getTable
from models.ticket import getTicket

class DatabaseManager():
    def __init__(self, db):
        self.db = db
        self.tables = {}


    def connectDatabase(self):
        print("connecting to db")
        self.db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

        self.addTable("Customer", getCustomer(self.db))
        self.addTable("CreditCard", getCreditCard(self.db))
        self.addTable("getMenu", getMenu(self.db))
        self.addTable("getTable", getTable(self.db))
        self.addTable("getTicket", getTicket(self.db))
        
        self.db.generate_mapping(create_tables=True)

    def getTable(self, table):
        return self.tables[table]

    def addTable(self, table, entity):
        self.tables[table] = entity





DatabaseManager = DatabaseManager(Database())