from fastapi import FastAPI
import os

print("🚀 APP STARTING...")
print("PORT ENV:", os.getenv("PORT"))

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}
print("THIS FILE IS RUNNING")
