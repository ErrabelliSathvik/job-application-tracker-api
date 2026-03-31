from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    role = Column(String, nullable=False)

    # ✅ New field
    status = Column(String, default="applied")

    # ✅ Foreign key (important for user-based jobs)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # ✅ Relationship
    owner = relationship("User", back_populates="jobs")