from typing import List
from sqlmodel import SQLModel, Field

class JobCreate(SQLModel):
    id: int
    job: str = Field(max_length=300)

class JobBatch(SQLModel):
    jobs: List[JobCreate]
