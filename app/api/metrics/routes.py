from fastapi import APIRouter
from .resources.metrics_api import router as hr_router

api_router = APIRouter()
api_router.include_router(hr_router)