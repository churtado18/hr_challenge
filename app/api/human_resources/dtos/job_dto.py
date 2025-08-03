from sqlmodel import SQLModel, Field
from pydantic import BaseModel, conlist
from typing import Annotated

class JobCreate(SQLModel):
    id: int
    job: str = Field(max_length=300)

class JobBatch(BaseModel):
    jobs: Annotated[
        conlist(item_type=JobCreate, min_length=1, max_length=1000),
        ...
    ]