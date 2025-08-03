import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()
#DATABASE_URL = os.getenv("DATABASE_URL", "mssql+pyodbc://user:password@server/db?driver=ODBC+Driver+17+for+SQL+Server")
DB_SERVER=os.getenv("DB_SERVER","nada")
DB_NAME=os.getenv("DB_NAME")
DB_USERNAME=os.getenv("DB_USERNAME")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_PORT=1433
DB_DRIVER=os.getenv("DB_DRIVER")


conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER=tcp:{DB_SERVER};'
    f'DATABASE={DB_NAME};'
    f'UID={DB_USERNAME};'
    f'PWD={DB_PASSWORD};'
    'Encrypt=yes;'
    'TrustServerCertificate=yes;'
    'Connection Timeout=30;'
)
print(conn_str)

conn = pyodbc.connect(conn_str)

print("Conexión exitosa a Azure SQL")
conn.close()
