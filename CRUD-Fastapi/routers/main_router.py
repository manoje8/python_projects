from fastapi import APIRouter

from routers import user_router, todo_router

router = APIRouter()

router.include_router(user_router.user_router)
router.include_router(todo_router.todo_router)