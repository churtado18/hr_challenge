from typing import List, Optional
from sqlmodel import Session
from datetime import datetime
from app.api.human_resources.repositories.department_repository import DepartmentRepository
from app.api.human_resources.repositories.hired_employees_repository import HiredEmployeeRepository
from app.api.human_resources.models.hired_employees_model import HiredEmployee
from app.api.human_resources.dtos.hired_employees_dto import HiredEmployeesCreate
from app.api.human_resources.repositories.job_repository import JobRepository

class HiredEmployeeService:
    def __init__(self, session: Session):
        self.repository = HiredEmployeeRepository(session)
        self.jobs_repository = JobRepository(session)
        self.departments_repository = DepartmentRepository(session)
        

    def create_hired_employee(self, hired_employee_dtos: List[HiredEmployeesCreate]):
        summary = {
            "inserted": 0,
            "skipped": 0,
            "failed": 0,
            "validations": [],
            "errors": []
        }

        for dto in hired_employee_dtos:
            try:
                #Validations for existing employee, department, and job
                employee = self.get_hired_employee_by_id(dto.id)
                if employee is not None:
                    summary["skipped"] += 1                    
                    summary["validations"].append({"id": dto.id, "message": "Employee with this ID already exists."})
                    continue

                department = self.departments_repository.get_by_id(dto.department_id)
                if department is None:
                    summary["skipped"] += 1
                    summary["validations"].append({"department_id": dto.department_id, "message": "Department with this ID doesn't exist."})
                    continue
                
                job = self.jobs_repository.get_by_id(dto.job_id)
                if job is None:
                    summary["skipped"] += 1
                    summary["validations"].append({"job_id": dto.job_id, "message": "Job with this ID doesn't exist."})
                    continue
                
                hired_employee = HiredEmployee(id = dto.id, 
                                        name = dto.name, 
                                        datetime = datetime.fromisoformat(dto.hired_datetime.replace("Z", "+00:00")).isoformat(), 
                                        department_id = dto.department_id, 
                                        job_id = dto.job_id                                
                                    )     
                self.repository.create(hired_employee)
                summary["inserted"] += 1
            
            except Exception as e:
                summary["failed"] += 1
                summary["errors"].append({"id": dto.id, "error": "internal server error"})
            
        return summary

    def get_all_hired_employee(self) -> List[HiredEmployee]:
        return self.repository.get_all()

    def get_hired_employee_by_id(self, employee_id: int) -> Optional[HiredEmployee]:
        return self.repository.get_by_id(employee_id)