from fastapi import FastAPI

app = FastAPI(title="Job Tracker API")

try:
    from app.routers import auth, jobs
    app.include_router(auth.router)
    app.include_router(jobs.router)
    print("✅ Routers loaded")
except Exception as e:
    print("❌ Router error:", e)

@app.get("/")
def root():
    return {"message": "API running 🚀"}