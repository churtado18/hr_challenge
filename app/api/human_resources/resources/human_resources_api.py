from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.db import get_session
from app.api.human_resources.dtos.job_dto import JobBatch
from app.api.human_resources.services.job_service import JobService
from app.api.human_resources.dtos.department_dto import DepartmentBatch
from app.api.human_resources.services.department_service import DepartmentService

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

@router.post("/departments", status_code=201, summary="Insert one or many departments records")
def create_departments_batch(payload: DepartmentBatch, session: Session = Depends(get_session)):
    service = DepartmentService(session)
    service.create_departments(payload.departments)
    return {"message": f"{len(payload.departments)} departments inserted successfully."}

@router.get("/departments", summary="Get all department records")
def get_all_departments(session: Session = Depends(get_session)):
    service = DepartmentService(session)
    departments = service.get_all_departments()
    return departments

@router.get("/departments/{department_id}", summary="Get a single department by ID")
def get_department_by_id(department_id: int, session: Session = Depends(get_session)):
    service = DepartmentService(session)
    department = service.get_department_by_id(department_id)
    if not department:
        return {"error": f"Department with id {department_id} not found."}
    return department