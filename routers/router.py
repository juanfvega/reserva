from routers.customer import customerRouter
from routers.table import tableRouter

def configRouters(app):
    app.include_router(customerRouter)
    app.include_router(tableRouter)