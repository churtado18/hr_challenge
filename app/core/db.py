from dotenv import load_dotenv
from sqlmodel import create_engine, Session, SQLModel
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "mssql+pyodbc://user:password@server/db?driver=ODBC+Driver+17+for+SQL+Server")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    return Session(engine)

def init_db():
    from app.api.human_resources.models.job_model import Job
    SQLModel.metadata.create_all(engine)
