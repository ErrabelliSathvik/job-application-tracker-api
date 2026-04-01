from fastapi import APIRouter

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/")
def get_jobs():
    return {"msg": "jobs working"}