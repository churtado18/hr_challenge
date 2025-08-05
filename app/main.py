from fastapi import FastAPI
from app.api.human_resources.routes import api_router as hr_api_router
from app.api.metrics.routes import api_router as metrics_api_router
from app.core.db import init_db
from app.core.config import settings
from app.core.exception_handlers import validation_exception_handler
from fastapi.exceptions import RequestValidationError

app = FastAPI(
    title=settings.api_title,
    description=settings.api_description,
    version=settings.api_version
)

app.add_exception_handler(RequestValidationError, validation_exception_handler)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(hr_api_router)
app.include_router(metrics_api_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"message": "Hello from Azure!"}

