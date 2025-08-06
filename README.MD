# To-Do List API con FastAPI

Este es un proyecto simple de una API de lista de tareas (to-do list) desarrollado con **FastAPI**. Incluye autenticación basada en tokens (sin cifrado) y almacenamiento de datos en **SQLite**.

## Características

- CRUD completo para tareas
- Autenticación simple con token (no cifrado)
- SQLite como base de datos
- Estructurado en múltiples archivos para mayor organización

## Instalación

### 1. **Clona el repositorio:**

git clone https://github.com/tu-usuario/tu-repo.git

### 2. **Crea un entorno virtual y actívalo:**

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

### 3. **Instala las dependencias:**

pip install -r requirements.txt

### 4. **Ejecuta el servidor:**

uvicorn main:app --reload


La API estará disponible en: http://localhost:8000


## API Endpoints

Autenticación
POST /login: Ingresa y recibe un token.

Cuerpo JSON:
{
  "username": "admin",
  "password": "admin"
}

Tareas
⚠️ Todos los endpoints de tareas requieren el header:

Authorization: Bearer <token>

- GET /tasks: Lista todas las tareas

- GET /tasks/{task_id}: Obtener una tarea por ID

- POST /tasks: Crear una nueva tarea

- PUT /tasks/{task_id}: Actualizar una tarea

- DELETE /tasks/{task_id}: Eliminar una tarea

## Base de Datos

La base de datos se crea automáticamente en el archivo todo.db.
Puedes explorarla con:

sqlite3 todo.db

Y luego ejecutar:

.tables
SELECT * FROM tasks
