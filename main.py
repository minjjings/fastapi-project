from fastapi import FastAPI
from app.database import mysqldb
from app.models import Base
from app.routers import user

def create_app():
    app = FastAPI()

    mysqldb.connect()
    Base.metadata.create_all(bind=mysqldb.engine)

    app.include_router(user.router)

    @app.on_event("shutdown")
    def shutdown():
        mysqldb.close()

    return app

app = create_app()
