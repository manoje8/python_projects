from typing import Optional
from pydantic import BaseModel


class AddTodo(BaseModel):
    title: str


class Todo(BaseModel):
    title: Optional[str] = None
    status: Optional[bool] = False


class TodoResponse(BaseModel):
    id: int
    title: str
    status: bool

    class Config:
        from_attributes = True
