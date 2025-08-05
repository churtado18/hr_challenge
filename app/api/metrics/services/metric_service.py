from typing import List, Optional
from sqlmodel import Session
from app.api.metrics.repositories.metric_repository import MetricRepository
from app.api.metrics.models.department_metric_model import DepartmentMetric
from app.api.metrics.models.quarter_metric_model import QuarterMetric

class MetricService:
    def __init__(self, session: Session):
        self.repository = MetricRepository(session)

    def get_department_by_year(self, year: int) -> List[DepartmentMetric]:
        return self.repository.get_department_by_year(year)
    
    def get_quarter_by_year(self, year: int) -> List[QuarterMetric]:
        return self.repository.get_quarter_by_year(year)