from fastapi import FastAPI
from routers.user_router import router
from database import engine
from models import Base

# Table creation
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple CRUD Methods")


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router)

