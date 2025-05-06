from sqlalchemy.orm import Session
from model.todo_model import Todo


class TodoService:
    @staticmethod
    def find_all(db: Session):
        return db.query(Todo).all()

    @staticmethod
    def create_todo(db: Session, todo:Todo):
        add_todo = Todo(**todo.model_dump())
        db.add(add_todo)
        db.commit()
        db.refresh(add_todo)
        return add_todo

    @staticmethod
    def find_todo(db: Session, todo_id: int):
        return db.query(Todo).filter(Todo.id == todo_id).first()
