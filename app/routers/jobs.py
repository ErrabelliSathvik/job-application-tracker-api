from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models.job import Job
from app.models.user import User
from app.routers.auth import get_current_user

router = APIRouter(prefix="/jobs", tags=["Jobs"])


# ✅ Request schema
class JobCreate(BaseModel):
    company_name: str
    role: str


# ✅ Create Job (Protected)
@router.post("/")
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_job = Job(
        company_name=job.company_name,
        role=job.role,
        owner_id=current_user.id
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return {
        "message": "Job created successfully",
        "job": {
            "id": new_job.id,
            "company_name": new_job.company_name,
            "role": new_job.role
        }
    }


# ✅ Get Jobs (Protected)
@router.get("/")
def get_jobs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    jobs = db.query(Job).filter(Job.owner_id == current_user.id).all()
    return jobs
from fastapi import HTTPException

@router.put("/{job_id}")
def update_job(
    job_id: int,
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing_job = db.query(Job).filter(
        Job.id == job_id,
        Job.owner_id == current_user.id
    ).first()

    if not existing_job:
        raise HTTPException(status_code=404, detail="Job not found")

    existing_job.company_name = job.company_name
    existing_job.role = job.role
    existing_job.status = job.status

    db.commit()

    return {"message": "Job updated"}
from fastapi import HTTPException

@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # 🔍 Find job belonging to current user
    job = db.query(Job).filter(
        Job.id == job_id,
        Job.owner_id == current_user.id
    ).first()

    # ❌ If not found
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    # 🗑️ Delete job
    db.delete(job)
    db.commit()

    return {"message": "Job deleted successfully"}