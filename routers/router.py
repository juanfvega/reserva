from routers.customer import customerRouter
from routers.table import tableRouter
from routers.creditcard import creditCardRouter
from routers.menu import menuRouter

def configRouters(app):
    app.include_router(customerRouter)
    app.include_router(tableRouter)
    app.include_router(creditCardRouter)
    app.include_router(menuRouter)