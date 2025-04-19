from fastapi import FastAPI, Depends, HTTPException
from backend.routers import user_router
from backend import database, models

# Table creation
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Simple CRUD Methods")


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(user_router.router)

