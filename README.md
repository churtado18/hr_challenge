# Human Resources data challenge

This project provides an API for human resources management and metrics, supporting bulk data migration to a new database system. It is built with FastAPI and SQLModel.

---
## Challenge
### Data movement and API
1. Move historic data from files in CSV format to the new database.
2. Create a Rest API service to receive new data. This service must have:
2.1. Each new transaction must fit the data dictionary rules.
2.2. Be able to insert batch transactions (1 up to 1000 rows) with one request.
2.3. Receive the data for each table in the same service.
2.4. Keep in mind the data rules for each table.

### Metrics
3. Number of employees hired for each job and department in 2021 divided by quarter. The
table must be ordered alphabetically by department and job.
4. List of ids, name and number of employees hired of each department that hired more
employees than the mean of employees hired in 2021 for all the departments, ordered
by the number of employees hired (descending).

---
## High-level architecture

![HR Challenge Architecture](https://github.com/churtado18/hr_challenge_data_migration/blob/develop/Architecture.png?raw=true)

### Data movement
1. Pipelines in Azure Data Factory obtain information on jobs, departments, and hired employees in CSV format from the Azure Blob storage repository.
2. Pipelines in Azure Data Factory store the information obtained in the Azure SQL database.
3. Pipelines in Azure Data Factory perform the following operations:
3.1 Full backups of the jobs, departments, and hired employees tables and store them in Azure Blob storage in AVRO file format.
3.2 Full restore AVRO files for jobs, departments, and hired employees to the jobs, departments, and hired employees tables.
4. The following REST APIs were developed using FastAPI and deployed to Azure App Service:
    - **Human Resources:** Provides read and write access to the jobs, departments, and hired_employees tables.
    - **Metrics:** Retrieves quarterly metrics on hired employees by department.
5. IAPs can be accessed by internal and external systems through Azure API Management.
---

## Implemented APIs

### Human Resources Endpoints (`/human-resources`)
- **POST /jobs**: Insert one or many job records.
- **GET /jobs**: Retrieve all job records.
- **GET /jobs/{job_id}**: Retrieve a job by its ID.
- **POST /departments**: Insert one or many department records.
- **GET /departments**: Retrieve all department records.
- **GET /departments/{department_id}**: Retrieve a department by its ID.
- **POST /hired-employees**: Insert one or many hired employee records.
- **GET /hired-employees**: Retrieve all hired employee records.
- **GET /hired-employees/{employee_id}**: Retrieve a hired employee by their ID.

### Metrics Endpoints (`/metrics`)
- **GET /metrics/quarter**: Get the number of employees hired for each job and department by year and quarter (query param: `year`).
- **GET /metrics/departments**: Get the number of employees hired in each department that hired more employees than the mean in a given year (query param: `year`).

---

## Environment Variables

Create a `.env` file in the project root with the following variables:

```
DB_SERVER=<your_server>
DB_NAME=<your_database>
DB_USERNAME=<your_username>
DB_PASSWORD=<your_password>
DB_PORT=1433
DB_DRIVER=ODBC Driver 17 for SQL Server
DATABASE_URL=mssql+pyodbc://<user>:<password>@<server>/<db>?driver=ODBC+Driver+17+for+SQL+Server
API_TITLE=Your API Title
API_VERSION=1.0.0
API_DESCRIPTION=Receives and stores HR data like jobs, departments, and hired employees
```

---

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your `.env` file** with the correct database credentials.

3. **Start the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## Accessing OpenAPI Documentation

Once the app is running, access the interactive API docs at:

- [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)
- [http://localhost:8000/redoc](http://localhost:8000/redoc) (ReDoc)

production endpoints:

- [https://hr-challenge-app-gjg3dje5hufxcchy.eastus2-01.azurewebsites.net/docs] (Swagger UI)
- [https://hr-challenge-app-gjg3dje5hufxcchy.eastus2-01.azurewebsites.net/redoc] (ReDoc) 

All endpoints for human resources and metrics are available and documented there.
