from fastapi import FastAPI, HTTPException
from db import session
from model import TaskTable
from schema import Task, TaskUpdate, TaskCreate

app = FastAPI()

# タスクデータの取得
@app.get("/tasks")
def read_tasks():
    tasks = session.query(TaskTable).all()
    Tasks = list(map( lambda task : Task(id=task.id, title=task.title, done=task.done) , tasks))
    return Tasks

# タスクデータの更新
@app.put("/tasks/{task_id}")
def update_task( task : TaskUpdate, task_id : int):
    if len(task.title) == 0 and task.done in [0,1]:
        raise HTTPException(status_code=400, detail="Bad Request")
    
    selected_task = session.query(TaskTable).filter(TaskTable.id == task_id).first()
    if selected_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    selected_task.title = task.title
    selected_task.done = task.done
    session.commit()

# タスクデータの追加
@app.post("/tasks")
def create_task( task : TaskCreate):
    if len(task.title) == 0 :
        raise HTTPException(status_code=400, detail="Bad Request")
    add_task = TaskTable(
        title = task.title,
    )
    session.add(add_task)
    session.commit()