from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.dependency import db_connect
from backend.controller.user_service import UserService
from backend.schema import UserResponse, User
from backend import models

router = APIRouter(prefix='/users', tags=['users'])

router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: User, db: Session = Depends(db_connect)):
    db_user = UserService.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return UserService.create(db, user)


router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(db_connect)):
    find_user = db.query(models.User).filter(models.User.id == user_id).first()
    if find_user is None:
        raise HTTPException(status_code=404, detail="User not found!")
    return find_user


router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: User, db: Session = Depends(db_connect)):
    find_user = db.query(models.User).filter(models.User.id == user_id).first()
    if find_user is None:
        raise HTTPException(status_code=404, detail="User not found!!")

    if user.name is not None:
        find_user.name = user.name
    if user.email is not None:
        existing_email = db.query(models.User).filter(models.User.email == user.email).first()

        if existing_email and existing_email.id != user_id:
            raise HTTPException(status_code=400, detail="Email is already registered!")
        find_user.email = user.email
    db.commit()
    db.refresh(find_user)
    return find_user


router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(db_connect)):
    find_user = db.query(models.User).filter(models.User.id == user_id).first()

    if find_user is None:
        raise HTTPException(status_code=404, detail="User not found!!!")

    db.delete(find_user)
    db.commit()

    return {"message": "User deleted successfully"}
