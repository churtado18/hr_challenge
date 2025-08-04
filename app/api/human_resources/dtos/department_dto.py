from sqlmodel import SQLModel, Field
from pydantic import BaseModel, conlist
from typing import Annotated

class DepartmentCreate(SQLModel):
    id: int
    department: str = Field(max_length=250)

class DepartmentBatch(BaseModel):
    departments: Annotated[
        conlist(item_type=DepartmentCreate, min_length=1, max_length=1000),
        ...
    ]