from fastapi import FastAPI
from db.database import Base, engine
from endpoints import task
from auth import utils

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir routers
app.include_router(task.router)
app.include_router(utils.router)

@app.get("/")
def home():
    return {"message": "Bienvenido a la API de tareas con SQL"}
