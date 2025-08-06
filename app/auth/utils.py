from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from schemas.user import User, UserCreate
from db.database import SessionLocal
from db import models
import time

router = APIRouter()
security = HTTPBasic()
SESSIONS = {}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

@router.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.username == credentials.username,
        models.User.password == credentials.password
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    token = f"{credentials.username}:{int(time.time())}"
    SESSIONS[token] = user
    return {"access_token": token}

def current_user(request: Request):
    token = request.headers.get("Authorization")
    if not token or token not in SESSIONS:
        raise HTTPException(status_code=401, detail="Token inválido o ausente")
    return SESSIONS[token]

@router.get("/users/me")
def me(user: User = Depends(current_user)):
    return user

@router.post("/users/create", response_model=User)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user_data.email).first()
    if existing:
        raise HTTPException(status_code=409, detail="El usuario ya existe")

    new_user = models.User(**user_data.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
