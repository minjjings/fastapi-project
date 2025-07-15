# app/deps.py
# DB 세션 의존성 
from app.database import mysqldb
from sqlalchemy.orm import Session

def get_db():
    db: Session = mysqldb.sessionmaker()
    try:
        yield db
    finally:
        db.close()
