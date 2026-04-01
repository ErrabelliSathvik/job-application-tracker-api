from fastapi import FastAPI
import sys
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Render working 🚀",
        "python_version": sys.version,
        "cwd": os.getcwd(),
        "files": os.listdir()
    }