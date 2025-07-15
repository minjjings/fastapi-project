# app/database.py
# DB연결 및 세션 관련 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import get_secret

class __MySQLDB:
    def __init__(self):
        self.__engine = None
        self.__SessionLocal = None

    def connect(self):
        self.__engine = create_engine(
            get_secret("MYSQL_URL"),
            echo=get_secret("MYSQL_ECHO", "false").lower() == "true",
            pool_size=int(get_secret("MYSQL_POOL_SIZE", "10")),
            max_overflow=int(get_secret("MYSQL_MAX_OVERFLOW", "20")),
        )
        self.__SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)

    def close(self):
        if self.__engine:
            self.__engine.dispose()

    @property
    def engine(self):
        return self.__engine

    @property
    def sessionmaker(self):
        return self.__SessionLocal

mysqldb = __MySQLDB()
