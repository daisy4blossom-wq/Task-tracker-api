from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class TaskStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TaskCreate(BaseModel):
    title:str = Field(min_length=3, max_length=30)
    description: str = Field(min_length=5, max_length=100)
    priority: TaskPriority = TaskPriority.MEDIUM

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=30)
    description: Optional[str] = Field(default=None, max_length=100)
    priority: Optional[TaskPriority] = None
    status: Optional[TaskStatus] = None

class TaskGet(BaseModel):
    id: str
    title: str
    description: str
    priority: TaskPriority
    status: TaskStatus
