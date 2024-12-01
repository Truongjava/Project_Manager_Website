from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

class Project(Base):
    __tablename__ = "projects"

    project_id = Column(String(50), primary_key=True, index=True)  # Chỉ định chiều dài
    project_name = Column(String(255), nullable=False)  # Chỉ định chiều dài
    description = Column(Text, nullable=True)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
    status = Column(String(50), nullable=False)  # Chỉ định chiều dài
    budget = Column(Integer, nullable=False)
    created_by = Column(String(50), ForeignKey("users.user_id"))  # Chỉ định chiều dài
    update_time = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    target = Column(Text, nullable=True)

    # Relationship với bảng users
    created_by_user = relationship("User", back_populates="projects")
