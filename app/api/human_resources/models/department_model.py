from sqlalchemy import Column
from sqlmodel import Integer, SQLModel, Field

class Department(SQLModel, table=True):
    __tablename__ = "departments"

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=False), title="Id of the department")
    department: str = Field(min_length=1, max_length=250, title="Name of the department")