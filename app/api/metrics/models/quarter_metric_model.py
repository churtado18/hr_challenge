from sqlmodel import SQLModel

class QuarterMetric(SQLModel):
    department: str
    job: str
    q1: int
    q2: int
    q3: int
    q4: int
