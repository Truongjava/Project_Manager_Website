from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.project_service import create_project, get_project_by_id, get_projects, update_project, delete_project
from app.schemas.project import ProjectCreate, ProjectResponse, ProjectUpdate
from app.db.database import get_db

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/", response_model=ProjectResponse)
def create_new_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = create_project(db, project)
    return db_project

@router.get("/{project_id}", response_model=ProjectResponse)
def read_project(project_id: str, db: Session = Depends(get_db)):
    project = get_project_by_id(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.get("/", response_model=list[ProjectResponse])
def list_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_projects(db, skip=skip, limit=limit)

@router.put("/{project_id}", response_model=ProjectResponse)
def update_project_info(project_id: str, project: ProjectUpdate, db: Session = Depends(get_db)):
    db_project = update_project(db, project_id, project)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.delete("/{project_id}", response_model=ProjectResponse)
def delete_project_info(project_id: str, db: Session = Depends(get_db)):
    db_project = delete_project(db, project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project
