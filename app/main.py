from fastapi import FastAPI
from app.routers import auth, jobs
from app.database import Base, engine

app = FastAPI(title="Job Tracker API")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(jobs.router)

@app.get("/")
def root():
    return {"message": "API is running 🚀"}