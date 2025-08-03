from sqlalchemy import Column
from sqlmodel import Integer, SQLModel, Field

class Job(SQLModel, table=True):
    __tablename__ = "jobs"

    id: int = Field(sa_column=Column(Integer, primary_key=True, autoincrement=False), title="Id of the job")
    job: str = Field(min_length=1, max_length=300, title="Name of the job")