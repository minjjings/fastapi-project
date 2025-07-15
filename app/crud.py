# app/crud.py
from sqlalchemy.orm import Session
from app.models import User
from typing import Optional


# CREATE
def create_user(db: Session, name: str, email: str) -> User:
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# READ
def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


# UPDATE
def update_user(db: Session, user_id: int, name: Optional[str] = None, email: Optional[str] = None) -> Optional[User]:
    user = get_user_by_id(db, user_id)
    if not user:
        return None

    if name:
        user.name = name
    if email:
        user.email = email

    db.commit()
    db.refresh(user)
    return user


# DELETE
def delete_user(db: Session, user_id: int) -> bool:
    user = get_user_by_id(db, user_id)
    if not user:
        return False

    db.delete(user)
    db.commit()
    return True
