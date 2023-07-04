from pydantic import BaseModel


# Schema定義 
class Task(BaseModel):
    id: int
    title: str
    done: int


class TaskCreate(BaseModel):
    title: str
    
    
class TaskUpdate(BaseModel):
    title: str
    done: int