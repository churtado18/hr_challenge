from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.db import get_session
from app.api.human_resources.dtos.job_dto import JobBatch
from app.api.human_resources.services.job_service import JobService
from app.api.human_resources.repositories.job_repository import JobRepository

router = APIRouter(prefix="/human-resources", tags=["Human Resources"])

@router.post("/jobs", status_code=201, summary="Insert one or many job records")
def create_jobs_batch(payload: JobBatch, session: Session = Depends(get_session)):
    service = JobService(session)
    service.create_jobs(payload.jobs)
    return {"message": f"{len(payload.jobs)} jobs inserted successfully."}

@router.get("/jobs", summary="Get all job records")
def get_all_jobs(session: Session = Depends(get_session)):
    service = JobService(session)
    jobs = service.get_all_jobs()
    return jobs

@router.get("/jobs/{job_id}", summary="Get a single job by ID")
def get_job_by_id(job_id: int, session: Session = Depends(get_session)):
    service = JobService(session)
    job = service.get_job_by_id(job_id)
    if not job:
        return {"error": f"Job with id {job_id} not found."}
    return job


