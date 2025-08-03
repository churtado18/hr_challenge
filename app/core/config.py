from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # Cargar el archivo .env

class Settings(BaseSettings):
    env: str = os.getenv("ENV")
    database_url: str = os.getenv("DATABASE_URL")
    api_title: str = os.getenv("API_TITLE", "My FastAPI")
    api_version: str = os.getenv("API_VERSION", "1.0.0")
    api_description: str = os.getenv("API_DESCRIPTION", "Receives and stores HR data like jobs, departments, and hired employees")

settings = Settings()
