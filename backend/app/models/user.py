from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    full_name = Column(String, nullable=True)
    profile_picture = Column(String, nullable=True)
    password = Column(String, nullable=False)

    # Quan hệ với bảng projects
    projects = relationship("Project", back_populates="created_by_user")
