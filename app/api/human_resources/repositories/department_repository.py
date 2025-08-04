from sqlmodel import select
from sqlmodel import Session
from app.api.human_resources.models.department_model import Department
from typing import List, Optional

class DepartmentRepository:
    def __init__(self, session: Session):
        self._session = session

    def bulk_create(self, departments: List[Department]):
        print( self._session)
        self._session.add_all(departments)
        self._session.commit()

    def get_all(self) -> List[Department]:
        statement = select(Department)
        results = self._session.exec(statement)
        return results.all()

    def get_by_id(self, department_id: int) -> Optional[Department]:
        statement = select(Department).where(Department.id == department_id)
        result = self._session.exec(statement).first()
        return result