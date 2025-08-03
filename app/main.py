from fastapi import FastAPI

app = FastAPI(title="HR data challenge API",
              description="API for HR data challenge",
              version="1.0.0")

@app.get("/")
def root():
    return {"message": "Hello, FastAPI"}
