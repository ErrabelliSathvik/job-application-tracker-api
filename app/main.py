from fastapi import FastAPI

app = FastAPI(title="Job Tracker API")

@app.get("/")
def root():
    return {"message": "API running 🚀"}