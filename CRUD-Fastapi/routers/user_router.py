from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dbConfig.dependency import db_connect
from service.user_service import UserService
from schema.user_schema import UserResponse, User
import logging


logger = logging.getLogger(__name__)
user_router = APIRouter(prefix='/users', tags=['users'])


@user_router.get("/", response_model=UserResponse)
async def fetch_users(db: Session = Depends(db_connect)):
    try:
        return db.query(User).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@user_router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: User, db: Session = Depends(db_connect)):
    try:
        db_user = UserService.get_user_by_email(db, email=user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        user_created = UserService.create(db, user)
        return user_created
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@user_router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(db_connect)):
    find_user = UserService.get_user_by_id(db, user_id)
    if find_user is None:
        raise HTTPException(status_code=404, detail="User not found!")
    return find_user


@user_router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: User, db: Session = Depends(db_connect)):
    find_user = UserService.get_user_by_id(db, user_id)
    if find_user is None:
        raise HTTPException(status_code=404, detail="User not found!!")

    update_data = user.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        if value is not None:
            setattr(find_user, field, user)

    db.commit()
    db.refresh(find_user)
    return find_user


@user_router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(db_connect)):
    find_user = UserService.get_user_by_id(db, user_id)

    if find_user is None:
        raise HTTPException(status_code=404, detail="User not found!!!")

    db.delete(find_user)
    db.commit()

    return {"message": "User deleted successfully"}
