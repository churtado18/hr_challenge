from sqlmodel import select
from sqlmodel import Session
from app.api.human_resources.models.hired_employees_model import HiredEmployee
from typing import List, Optional

class HiredEmployeeRepository:
    def __init__(self, session: Session):
        self._session = session

    def create(self, hired_employees: HiredEmployee):
        self._session.add(hired_employees)
        self._session.commit()

    def bulk_create(self, hired_employees: List[HiredEmployee]):
        self._session.add_all(hired_employees)
        self._session.commit()

    def get_all(self) -> List[HiredEmployee]:
        statement = select(HiredEmployee)
        results = self._session.exec(statement)
        return results.all()

    def get_by_id(self, employee_id: int) -> Optional[HiredEmployee]:
        statement = select(HiredEmployee).where(HiredEmployee.id == employee_id)
        result = self._session.exec(statement).first()
        return result