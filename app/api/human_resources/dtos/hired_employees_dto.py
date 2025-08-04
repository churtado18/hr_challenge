from sqlmodel import SQLModel, Field
from pydantic import BaseModel, conlist
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, field_validator

class HiredEmployeesCreate(SQLModel):
    id: int
    name: str = Field(max_length=200)
    hired_datetime: str = Field(max_length=20)
    department_id: int
    job_id: int

    @field_validator("hired_datetime")
    def validate_datetime(cls, v):
        try:
            datetime.fromisoformat(v.replace("Z", "+00:00"))
        except ValueError:
            raise ValueError("datetime must be in ISO 8601 format (e.g., 2021-11-07T02:48:42Z)")
        return v

class HiredEmployeesBatch(BaseModel):
    hired_employees: Annotated[
        conlist(item_type=HiredEmployeesCreate, min_length=1, max_length=1000),
        ...
    ]
