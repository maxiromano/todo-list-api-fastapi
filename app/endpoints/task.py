from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.task import Task, TaskCreate
from auth.utils import current_user, get_db
from crud import task as crud_task
from models.user import User

router = APIRouter()

@router.post("/tasks", response_model=Task)
def create(task: TaskCreate, db: Session = Depends(get_db), user: User = Depends(current_user)):
    return crud_task.create_task(db, task)

@router.get("/tasks", response_model=list[Task])
def get_all(db: Session = Depends(get_db), user: User = Depends(current_user)):
    return crud_task.get_all_tasks(db)

@router.get("/tasks/{task_id}", response_model=Task)
def get(task_id: int, db: Session = Depends(get_db), user: User = Depends(current_user)):
    task = crud_task.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task

@router.put("/tasks/{task_id}", response_model=Task)
def update(task_id: int, task_data: TaskCreate, db: Session = Depends(get_db), user: User = Depends(current_user)):
    result = crud_task.update_task(db, task_id, task_data)
    if not result:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return result

@router.delete("/tasks/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db), user: User = Depends(current_user)):
    return crud_task.delete_task(db, task_id)
