from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    done: int
    
    
class TaskUpdate(BaseModel):
    title: str
    done: int
    
    
class TaskCreate(BaseModel):
    title: str