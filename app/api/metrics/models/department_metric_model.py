from sqlmodel import SQLModel

class DepartmentMetric(SQLModel):
    id: int
    department: str
    hired_number: int