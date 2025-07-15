from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import (
    create_user,
    get_user_by_id,
    update_user,
    delete_user
)
from app.deps import get_db

router = APIRouter()

@router.post("/users")
def create_user_route(name: str, email: str, db: Session = Depends(get_db)):
    return create_user(db, name, email)

@router.get("/users/{user_id}")
def get_user_route(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}")
def update_user_route(user_id: int, name: str = "", email: str = "", db: Session = Depends(get_db)):
    user = update_user(db, user_id, name or None, email or None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    success = delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}
