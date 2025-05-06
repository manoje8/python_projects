from sqlalchemy.orm import Session
from model.user_model import User
from utils.hashing import Hashing


class UserService:
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def create(db: Session, user: User):
        hashed_pwd = Hashing.password_hash(user.password)
        db_user = User(name= user.name,email=user.email, password= hashed_pwd)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
