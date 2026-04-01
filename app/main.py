from fastapi import FastAPI
from app.routers import auth, jobs

app = FastAPI()

app.include_router(auth.router)
app.include_router(jobs.router)