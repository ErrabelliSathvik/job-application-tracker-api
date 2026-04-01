from fastapi import FastAPI

print("🚀 MAIN FILE LOADED")

# Try importing routers
try:
    from app.routers import auth, jobs
    print("✅ IMPORT SUCCESS: routers loaded")
except Exception as e:
    print("❌ IMPORT FAILED:", e)

app = FastAPI(title="Job Tracker API")

# Try including routers
try:
    app.include_router(auth.router)
    app.include_router(jobs.router)
    print("✅ ROUTERS ADDED")
except Exception as e:
    print("❌ ROUTER ERROR:", e)


@app.get("/")
def root():
    return {"message": "API is running 🚀"}