from sqlmodel import select
from sqlmodel import Session
from app.api.human_resources.models.job_model import Job
from typing import List, Optional

class JobRepository:
    def __init__(self, session: Session):
        self._session = session

    def bulk_create(self, jobs: List[Job]):
        self._session.add_all(jobs)
        self._session.commit()

    def get_all(self) -> List[Job]:
        statement = select(Job)
        results = self._session.exec(statement)
        return results.all()

    def get_by_id(self, job_id: int) -> Optional[Job]:
        statement = select(Job).where(Job.id == job_id)
        result = self._session.exec(statement).first()
        return result