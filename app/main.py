from fastapi import FastAPI

app = FastAPI(title="Job Tracker API")

try:
    from app.routers import auth, jobs
    app.include_router(auth.router)
    app.include_router(jobs.router)
except Exception as e:
    print("IMPORT ERROR:", e)

@app.get("/")
def root():
    return {"message": "API running 🚀"}