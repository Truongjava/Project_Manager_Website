from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProjectBase(BaseModel):
    project_name: str
    description: Optional[str]
    start_date: datetime
    end_date: Optional[datetime]
    status: str
    budget: int
    target: Optional[str]

class ProjectCreate(ProjectBase):
    project_id: str
    created_by: str  # user_id của người tạo dự án

class ProjectUpdate(ProjectBase):
    project_name: Optional[str]
    description: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    status: Optional[str]
    budget: Optional[int]
    target: Optional[str]

class ProjectResponse(ProjectBase):
    project_id: str
    created_by: str
    update_time: datetime

    class Config:
        from_attributes = True  # Tương thích với Pydantic V2
