from sqlalchemy import Column
from sqlmodel import Integer, SQLModel, Field

class HiredEmployee(SQLModel, table=True):
    __tablename__ = "hired_employees"

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=False), title="Id of the employee")
    name: str = Field(min_length=1, max_length=200, title="Name and surname of the employee")
    datetime: str = Field(nullable=False, title="Hire datetime in ISO format")
    department_id: int = Field(foreign_key="departments.id", nullable=False, title="Id of the department which the employee was hired for")
    job_id: int = Field(foreign_key="jobs.id", nullable=False, title="Id of the job which the employee was hired for")