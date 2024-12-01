from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.models.user import User
from datetime import datetime

# Hàm tạo dự án
def create_project(db: Session, project: ProjectCreate):
    db_project = Project(
        project_id=project.project_id,
        project_name=project.project_name,
        description=project.description,
        start_date=project.start_date,
        end_date=project.end_date,
        status=project.status,
        budget=project.budget,
        created_by=project.created_by,
        target=project.target
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# Hàm lấy dự án theo project_id
def get_project_by_id(db: Session, project_id: str):
    return db.query(Project).filter(Project.project_id == project_id).first()

# Hàm lấy danh sách dự án
def get_projects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Project).offset(skip).limit(limit).all()

# Hàm cập nhật dự án
def update_project(db: Session, project_id: str, project: ProjectUpdate):
    db_project = db.query(Project).filter(Project.project_id == project_id).first()
    if db_project:
        if project.project_name:
            db_project.project_name = project.project_name
        if project.description:
            db_project.description = project.description
        if project.start_date:
            db_project.start_date = project.start_date
        if project.end_date:
            db_project.end_date = project.end_date
        if project.status:
            db_project.status = project.status
        if project.budget:
            db_project.budget = project.budget
        if project.target:
            db_project.target = project.target
        db.commit()
        db.refresh(db_project)
        return db_project
    return None

# Hàm xóa dự án
def delete_project(db: Session, project_id: str):
    db_project = db.query(Project).filter(Project.project_id == project_id).first()
    if db_project:
        db.delete(db_project)
        db.commit()
        return db_project
    return None
