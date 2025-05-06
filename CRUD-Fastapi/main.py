from fastapi import FastAPI
from dbConfig.database import engine
from model.user_model import Base
from routers.main_router import router
from fastapi.middleware.cors import CORSMiddleware

# Table creation
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple CRUD Methods")

origins = [
    "http://localhost:3000",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"message": "Welcome to the Server!!!"}

app.include_router(router)
