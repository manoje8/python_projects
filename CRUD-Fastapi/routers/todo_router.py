from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schema.todo_schema import Todo, TodoResponse, AddTodo
from dbConfig.dependency import db_connect
from service.todo_service import TodoService
from utils.logger import logger
from typing import List

todo_router = APIRouter(prefix="/todo", tags=['todo'])


@todo_router.get("/", response_model=List[TodoResponse])
async def todo_list(db: Session = Depends(db_connect)):
    try:
        todos = TodoService.find_all(db)
        return todos
    except Exception as e:
        logger.info("Error creating todo: %s", str(e))
        raise HTTPException(status_code=500, detail="Failed to get todo list!")


@todo_router.get("/{todo_id}", response_model=TodoResponse)
async def todo_by_id(todo_id: int, db: Session = Depends(db_connect)):
    try:
        find_todo = TodoService.find_todo(db, todo_id)
        if find_todo is None:
            raise HTTPException(status_code=404, detail="Todo not found!")

        logger.info(" find todo:%s", str(find_todo))
        return find_todo
    except Exception as e:
        logger.info("Error getting todo:%s", str(e))
        raise HTTPException(status_code=500, detail="Failed to get todo list!")


@todo_router.post("/", response_model=TodoResponse)
async def create_todo(todo: AddTodo, db: Session = Depends(db_connect)):
    try:
        return TodoService.create_todo(db, todo)
    except Exception as e:
        logger.info("Error creating todo: %s", str(e))
        raise HTTPException(status_code=500, detail="Failed to create todo")


@todo_router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: int, todo: Todo, db: Session = Depends(db_connect)):
    try:
        find_todo = TodoService.find_todo(db, todo_id)
        if find_todo is None:
            raise HTTPException(status_code=404, detail="Todo not found!")

        update_data = todo.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            if value is not None:
                setattr(find_todo, field, value)
        db.commit()
        db.refresh(find_todo)
        return find_todo

    except Exception as e:
        logger.info("Error updating todo: %s", str(e))
        raise HTTPException(status_code=500, detail="error updating todo")


@todo_router.delete("/{todo_id}", response_model=dict)
async def delete_todo(todo_id: int, db: Session = Depends(db_connect)):
    try:
        find_todo = TodoService.find_todo(db, todo_id)

        if find_todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")

        db.delete(find_todo)
        db.commit()
        return {"message": "Todo deleted successfully"}

    except Exception as e:
        logger.info("Error deleting todo: %s", str(e))
        raise HTTPException(status_code=500, detail="Error deleting todo")