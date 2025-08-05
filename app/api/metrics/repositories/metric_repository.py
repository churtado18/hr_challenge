from sqlmodel import Session
from app.api.metrics.models.department_metric_model import DepartmentMetric
from app.api.metrics.models.quarter_metric_model import QuarterMetric

from typing import Optional

class MetricRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_department_by_year(self, year: int) -> Optional[DepartmentMetric]:    
        result =  self._session.connection().exec_driver_sql(
                        "EXEC employees_hired_by_department @anio = ?",
                         (year,)
                        )
        rows = result.fetchall()
        metric_result = [DepartmentMetric(**dict(row._mapping)) for row in rows]
        return metric_result
    
    def get_quarter_by_year(self, year: int) -> Optional[QuarterMetric]:    
        result =  self._session.connection().exec_driver_sql(
                        "EXEC employees_hired_by_quarter @anio = ?",
                         (year,)
                        )
        rows = result.fetchall()
        metric_result = [QuarterMetric(**dict(row._mapping)) for row in rows]
        return metric_result