from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
