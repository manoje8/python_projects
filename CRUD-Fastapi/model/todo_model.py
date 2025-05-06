from sqlalchemy import Column, String, Boolean, Integer
from dbConfig.database import Base


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    status = Column(Boolean, default=False, index=True)