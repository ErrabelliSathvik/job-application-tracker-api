from fastapi import FastAPI
from app.routers import auth, jobs
from app.database import Base, engine
from app.models import user, job   # 👈 IMPORTANT

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Application Tracker API")

app.include_router(auth.router)
app.include_router(jobs.router)

@app.get("/")
def root():
    return {"message": "API is running 🚀"}
import os

port = int(os.environ.get("PORT", 8000))
