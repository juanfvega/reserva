from routers.customer import customerRouter


def configRouters(app):
    app.include_router(customerRouter)