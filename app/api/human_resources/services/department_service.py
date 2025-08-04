from typing import List, Optional
from sqlmodel import Session
from app.api.human_resources.repositories.department_repository import DepartmentRepository
from app.api.human_resources.models.department_model import Department
from app.api.human_resources.dtos.department_dto import DepartmentCreate

class DepartmentService:
    def __init__(self, session: Session):
        self.repository = DepartmentRepository(session)

    def create_departments(self, department_dtos: List[DepartmentCreate]):
        departments = [Department(id=dto.id, department=dto.department) for dto in department_dtos]
        self.repository.bulk_create(departments)

    def get_all_departments(self) -> List[Department]:
        return self.repository.get_all()

    def get_department_by_id(self, department_id: int) -> Optional[Department]:
        return self.repository.get_by_id(department_id)