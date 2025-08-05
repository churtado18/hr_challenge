from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.db import get_session
from app.api.human_resources.dtos.job_dto import JobBatch
from app.api.metrics.services.metric_service import MetricService


router = APIRouter(prefix="/metrics", tags=["Metrics"])

@router.get("/quarter", summary="Get number of employees hired for each job and department by year and quarter.")
def get_quarter_by_year(year: int, session: Session = Depends(get_session)):
    service = MetricService(session)
    metrics = service.get_quarter_by_year(year)
    return metrics

@router.get("/departments", summary="Get number of employees hired of each department that hired more employees than the mean of employees hired in a year.")
def get_department_by_year(year: int, session: Session = Depends(get_session)):
    service = MetricService(session)
    metrics = service.get_department_by_year(year)
    return metrics