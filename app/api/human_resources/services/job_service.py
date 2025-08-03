from typing import List, Optional
from sqlmodel import Session
from app.api.human_resources.repositories.job_repository import JobRepository
from app.api.human_resources.models.job_model import Job
from app.api.human_resources.dtos.job_dto import JobCreate

class JobService:
    def __init__(self, session: Session):
        self.repository = JobRepository(session)

    def create_jobs(self, job_dtos: List[JobCreate]):
        jobs = [Job(id=dto.id, job=dto.job) for dto in job_dtos]
        print("jobs", jobs)
        self.repository.bulk_create(jobs)

    def get_all_jobs(self) -> List[Job]:
        return self.repository.get_all()

    def get_job_by_id(self, job_id: int) -> Optional[Job]:
        return self.repository.get_by_id(job_id)