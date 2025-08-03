from fastapi import APIRouter
from .resources.human_resources_api import router as hr_router

api_router = APIRouter()
api_router.include_router(hr_router)
